code = """import json, re, pandas as pd

def load_result(var):
    if isinstance(var, str):
        with open(var, 'r') as f:
            return json.load(f)
    return var

clin = load_result(var_call_EE79U5QuHFJN62mGTXO59efr)
mut = load_result(var_call_CYvK1QI8G8QvQ07a9MIFoWej)

df_clin = pd.DataFrame(clin)
# Extract TCGA barcode from participant description
pat = df_clin['participant'].str.extract(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', expand=False)
df_clin['barcode'] = pat
# alive: days_to_death is not numeric / is null / [Not Applicable]
# We'll treat numeric as dead (has days_to_death)
# Coerce to numeric
num = pd.to_numeric(df_clin['days_to_death'], errors='coerce')
df_clin['alive'] = num.isna()

df_clin_alive = df_clin[df_clin['alive'] & df_clin['barcode'].notna()].copy()

# mutation carriers set
mut_df = pd.DataFrame(mut)
mut_df['mut_count'] = pd.to_numeric(mut_df['mut_count'], errors='coerce').fillna(0).astype(int)
mut_barcodes = set(mut_df['participant'].astype(str))

df_clin_alive['has_cdh1_mut'] = df_clin_alive['barcode'].astype(str).isin(mut_barcodes)

# group by histological type
agg = df_clin_alive.groupby('hist_type', dropna=False).agg(
    n_alive=('barcode','nunique'),
    n_mut=('has_cdh1_mut','sum')
).reset_index()
agg['pct_mut'] = (agg['n_mut'] / agg['n_alive'] * 100).round(2)

# filter out very small groups? not specified, keep all.
# take top 3 by pct_mut, break ties by n_alive desc then n_mut desc
agg_sorted = agg.sort_values(['pct_mut','n_alive','n_mut'], ascending=[False, False, False]).head(3)

result = agg_sorted.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_kGJqbbva1KuOPT5jcir6TyVe': ['clinical_info'], 'var_call_m8yWHtgIPfy3xECotzXjILrj': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_u6oni6vf2O7lRVFv6alZCyVJ': [{'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'histological_type'}, {'column_name': 'histological_type_other'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'margin_status'}, {'column_name': 'menopause_status'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'person_neoplasm_cancer_status'}], 'var_call_ukLW7szXVWN2AGgWAfYYBtZQ': [{'column_name': 'days_to_death'}, {'column_name': 'patient_death_reason'}], 'var_call_iZW9x4c9Q1170BmIM59Zlw9w': [], 'var_call_7gj2pTocXToETNvyHsOT1NVU': [{'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'histological_type'}, {'column_name': 'histological_type_other'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'person_neoplasm_cancer_status'}], 'var_call_NXpJQI1bOAu6bvI3oxz5lT82': [{'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'residual_tumor'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'tumor_tissue_site_other'}], 'var_call_EE79U5QuHFJN62mGTXO59efr': 'file_storage/call_EE79U5QuHFJN62mGTXO59efr.json', 'var_call_CYvK1QI8G8QvQ07a9MIFoWej': 'file_storage/call_CYvK1QI8G8QvQ07a9MIFoWej.json'}

exec(code, env_args)
