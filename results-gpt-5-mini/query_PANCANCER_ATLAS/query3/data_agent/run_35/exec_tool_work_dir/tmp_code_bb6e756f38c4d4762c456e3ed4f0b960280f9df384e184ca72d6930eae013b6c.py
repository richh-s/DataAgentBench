code = """import pandas as pd
import re
import json

clinical_path = var_call_CpER4D8kxe0emTc45fgMCaUH
mut_path = var_call_hk8JPyVKGwxzlQ9AneWjnDX9

out = {}
try:
    df_clin = pd.read_json(clinical_path)
    df_mut = pd.read_json(mut_path)
    out['clin_rows'] = int(df_clin.shape[0])
    out['mut_rows'] = int(df_mut.shape[0])
    out['clin_columns'] = list(df_clin.columns[:50])
    out['mut_columns'] = list(df_mut.columns)
    # show first 5 patient_descriptions
    out['pd_sample'] = df_clin['Patient_description'].astype(str).head(5).tolist()

    # barcode extraction
    def extract_barcode(text):
        if not isinstance(text, str):
            return None
        m = re.search(r'(TCGA-[A-Z0-9]+-[A-Z0-9]+)', text, re.I)
        if m:
            return m.group(1).upper()
        return None
    df_clin['barcode'] = df_clin['Patient_description'].astype(str).apply(extract_barcode)
    out['barcode_sample'] = df_clin['barcode'].head(10).tolist()
    out['barcode_nulls'] = int(df_clin['barcode'].isna().sum())

    # check histological_type unique values sample
    out['hist_unique_sample'] = df_clin['histological_type'].dropna().unique()[:20].tolist()

    # masks
    df_clin['pd_lower'] = df_clin['Patient_description'].astype(str).str.lower()
    mask_breast = df_clin['pd_lower'].str.contains('breast') | df_clin['pd_lower'].str.contains('brca')
    mask_female = df_clin['Patient_description'].astype(str).str.contains('FEMALE', case=False, na=False)
    out['mask_breast_count'] = int(mask_breast.sum())
    out['mask_female_count'] = int(mask_female.sum())
    out['both_mask_count'] = int((mask_breast & mask_female).sum())

    bad_hist = set(['None','[Not Applicable]','[Not Available]','Not Reported','Unknown','',None])
    def hist_known(x):
        if pd.isna(x):
            return False
        s = str(x).strip()
        if s == '':
            return False
        if s in bad_hist:
            return False
        return True
    mask_hist_known = df_clin['histological_type'].apply(hist_known)
    out['mask_hist_known_count'] = int(mask_hist_known.sum())

    df_brca_female = df_clin[mask_breast & mask_female & mask_hist_known].copy()
    out['df_brca_female_count'] = int(df_brca_female.shape[0])
    out['df_brca_female_sample_pd'] = df_brca_female['Patient_description'].head(5).tolist()
    out['df_brca_female_sample_hist'] = df_brca_female['histological_type'].head(5).tolist()
    out['df_brca_female_barcodes_sample'] = df_brca_female['barcode'].head(10).tolist()

    # dedupe
    df_brca_female = df_brca_female.drop_duplicates(subset=['barcode'])
    out['dedup_count'] = int(df_brca_female.shape[0])

    mut_barcodes = set(df_mut['ParticipantBarcode'].astype(str).str.upper().unique())
    out['mut_unique_barcodes'] = len(mut_barcodes)
    # intersect
    out['intersect_barcodes_count'] = int(len(set(df_brca_female['barcode'].astype(str).unique()) & mut_barcodes))

    # build crosstab
    df_brca_female['CDH1_mut'] = df_brca_female['barcode'].apply(lambda x: x in mut_barcodes)
    ct = pd.crosstab(df_brca_female['histological_type'], df_brca_female['CDH1_mut'])
    out['ct_shape'] = list(ct.shape)
    out['ct_head'] = ct.head(20).to_dict()

    # ensure columns
    cols = ct.columns.tolist()
    out['ct_columns'] = cols
    # Now try selecting columns [True, False] safely
    yes_col = True if True in cols else None
    no_col = False if False in cols else None
    out['yes_col_present'] = yes_col is not None
    out['no_col_present'] = no_col is not None

    # compute row sums
    ct['row_sum'] = ct.sum(axis=1)
    out['row_sum_stats'] = {'min': int(ct['row_sum'].min()), 'max': int(ct['row_sum'].max())}
    ct_included = ct[ct['row_sum'] > 10].drop(columns=['row_sum'])
    out['included_rows'] = int(ct_included.shape[0])
    out['included_ct'] = ct_included.to_dict()

    # compute chi2
    if ct_included.shape[0] == 0:
        out['error'] = 'No histological categories with marginal totals > 10 after filtering; cannot compute chi-square.'
    else:
        observed = ct_included.values.astype(float)
        row_totals = observed.sum(axis=1).reshape(-1,1)
        col_totals = observed.sum(axis=0).reshape(1,-1)
        grand_total = observed.sum()
        expected = (row_totals @ col_totals) / grand_total
        chi2 = (((observed - expected) ** 2) / expected).sum()
        out['chi2'] = float(chi2)
        out['grand_total'] = int(grand_total)

except Exception as e:
    out['exception'] = str(e)

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_WUTduE6YXwIB0XzZJkiicgTn': ['clinical_info'], 'var_call_raxK4sfkMMSuTsT8liLto0mB': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_CpER4D8kxe0emTc45fgMCaUH': 'file_storage/call_CpER4D8kxe0emTc45fgMCaUH.json', 'var_call_hk8JPyVKGwxzlQ9AneWjnDX9': 'file_storage/call_hk8JPyVKGwxzlQ9AneWjnDX9.json'}

exec(code, env_args)
