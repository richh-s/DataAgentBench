code = """import json, re, math
import pandas as pd

def load_records(var):
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r') as f:
            return json.load(f)
    return var

expr = load_records(var_call_rCV9g5y2kxryMiOpZK7gFjSt)
clin = load_records(var_call_vPAMC9wSEFbGx6seG1Zf5rRE)

expr_df = pd.DataFrame(expr)
expr_df['normalized_count'] = pd.to_numeric(expr_df['normalized_count'], errors='coerce')
expr_df = expr_df.dropna(subset=['normalized_count'])

clin_df = pd.DataFrame(clin)
# derive cancer type acronym from Patient_description using pattern 'In the X dataset'
pat = re.compile(r'In the ([^,]+?) dataset', re.IGNORECASE)
clin_df['dataset'] = clin_df['Patient_description'].str.extract(pat, expand=False)
# map dataset to TCGA acronym
map_acr = {
    'Brain Lower Grade Glioma':'LGG',
    'Brain lower grade glioma':'LGG',
    'Lower Grade Glioma':'LGG',
    'LGG':'LGG'
}
clin_df['cancer_type_acronym'] = clin_df['dataset'].map(map_acr)
# also handle descriptions like 'diagnosed with ...' lacking dataset phrase by leaving NaN

# choose barcode from description: 'patient TCGA-..' or 'Patient TCGA-..'
bar_pat = re.compile(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})')
clin_df['barcode_extracted'] = clin_df['Patient_description'].str.extract(bar_pat, expand=False)
# ParticipantBarcode in hint is Patient_description, but it's full description; expression uses actual barcode.
# We'll join using extracted barcode.

clin_df = clin_df.rename(columns={'histological_type':'histology'})
clin_df['histology'] = clin_df['histology'].astype(str)
valid_hist = ~clin_df['histology'].str.match(r'^\[.*\]$')
clin_df = clin_df[valid_hist]

lgg_clin = clin_df[clin_df['cancer_type_acronym']=='LGG'].copy()

merged = pd.merge(expr_df, lgg_clin, left_on='ParticipantBarcode', right_on='barcode_extracted', how='inner')
merged = merged.dropna(subset=['normalized_count','histology'])
merged['log10_expr'] = (merged['normalized_count'] + 1.0).apply(lambda x: math.log10(x) if x>0 else float('nan'))
merged = merged.dropna(subset=['log10_expr'])

res = merged.groupby('histology', as_index=False).agg(avg_log10_igf2=('log10_expr','mean'), n=('log10_expr','size'))
res['avg_log10_igf2'] = res['avg_log10_igf2'].round(6)
res = res.sort_values('avg_log10_igf2', ascending=False)

out = res.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_rCV9g5y2kxryMiOpZK7gFjSt': 'file_storage/call_rCV9g5y2kxryMiOpZK7gFjSt.json', 'var_call_Onnlyg579F6av1zyd049RIQO': ['clinical_info'], 'var_call_vPAMC9wSEFbGx6seG1Zf5rRE': 'file_storage/call_vPAMC9wSEFbGx6seG1Zf5rRE.json', 'var_call_hy5MvcGSLaJba84QorzdLWl5': [], 'var_call_p5yrSamFc52exTjAMUL6lYDG': [{'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'person_neoplasm_cancer_status'}], 'var_call_9ywxTl8WqYMViMVJIXxQzmrk': []}

exec(code, env_args)
