code = """import json, re, math, pandas as pd

# Load IGF2 expression rows (large file)
path_expr = var_call_JDdOb10C6ART0yFZ3wJWqUqT
with open(path_expr, 'r') as f:
    expr_rows = json.load(f)

df_expr = pd.DataFrame(expr_rows)
# Ensure numeric
for col in ['normalized_count']:
    df_expr[col] = pd.to_numeric(df_expr[col], errors='coerce')
df_expr = df_expr.dropna(subset=['ParticipantBarcode','normalized_count'])

# Load clinical brain histology rows
path_clin = var_call_bq5EXxErODF5uZ0z6Nlg8DLc
with open(path_clin, 'r') as f:
    clin_rows = json.load(f)

df_clin = pd.DataFrame(clin_rows)
# normalize column names from postgres lowercasing in json
# expect 'participantbarcode' and 'histology'
if 'ParticipantBarcode' not in df_clin.columns and 'participantbarcode' in df_clin.columns:
    df_clin = df_clin.rename(columns={'participantbarcode':'ParticipantBarcode'})
if 'Histology' not in df_clin.columns and 'histology' in df_clin.columns:
    df_clin = df_clin.rename(columns={'histology':'Histology'})

def extract_barcode(s):
    if s is None:
        return None
    m = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', str(s))
    return m.group(1) if m else None

df_clin['PatientBarcode'] = df_clin['ParticipantBarcode'].apply(extract_barcode)
# LGG patients inferred via histology types typical of LGG: Astrocytoma, Oligoastrocytoma, Oligodendroglioma
lgg_hist = {'Astrocytoma','Oligoastrocytoma','Oligodendroglioma'}
# filter histology not in square brackets
df_clin = df_clin.dropna(subset=['PatientBarcode','Histology'])
df_clin = df_clin[~df_clin['Histology'].astype(str).str.match(r'^\s*\[.*\]\s*$')]
df_lgg = df_clin[df_clin['Histology'].isin(lgg_hist)].copy()

# join expression with clinical on patient barcode
merged = df_lgg.merge(df_expr, left_on='PatientBarcode', right_on='ParticipantBarcode', how='inner')
merged = merged.dropna(subset=['normalized_count'])
merged['log10_expr'] = (merged['normalized_count'] + 1.0).apply(lambda x: math.log10(x) if x>0 else float('nan'))
merged = merged.dropna(subset=['log10_expr'])

res = merged.groupby('Histology', as_index=False).agg(
    n_samples=('log10_expr','size'),
    avg_log10_igf2=('log10_expr','mean')
)
res['avg_log10_igf2'] = res['avg_log10_igf2'].map(lambda v: float(f"{v:.4f}"))
res = res.sort_values('Histology')

out = res.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_JDdOb10C6ART0yFZ3wJWqUqT': 'file_storage/call_JDdOb10C6ART0yFZ3wJWqUqT.json', 'var_call_GTijWeXO8pqMVMcFVRHkv0HZ': ['clinical_info'], 'var_call_gDwVdRgl4lawxCCCBbGkfd74': [{'column_name': 'icd_o_3_histology'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'histological_type'}, {'column_name': 'histological_type_other'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}], 'var_call_Uxc0BDzfEfwIQlUxlo4hZQbp': [], 'var_call_9r4TA81YhXYXgesAuIUb4s5E': [{'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'residual_tumor'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}], 'var_call_VVl93PJssgo5TC0IUKEHwA7G': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma', 'tumor_tissue_site': 'Ovary'}, {'Patient_description': 'Patient TCGA-36-1576 (UUID 3445c524-5a37-40b6-8614-956d76eed939) is a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Current vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma', 'tumor_tissue_site': 'Ovary'}, {'Patient_description': 'Record fdd4adb8-9295-480a-9352-305b5eb51187 refers to patient TCGA-25-2408, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.', 'histological_type': 'Serous Cystadenocarcinoma', 'tumor_tissue_site': 'Ovary'}, {'Patient_description': 'Record 6f25001a-f890-4fd0-a994-e62a9ea5c6f3 refers to patient TCGA-29-2427, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Alive.', 'histological_type': 'Serous Cystadenocarcinoma', 'tumor_tissue_site': 'Ovary'}, {'Patient_description': 'Case 9446e349-71e6-455a-aa8f-53ec96597146, linked to barcode TCGA-10-0933, corresponds to a FEMALE patient diagnosed with Ovarian serous cystadenocarcinoma, with vital status Dead.', 'histological_type': 'Serous Cystadenocarcinoma', 'tumor_tissue_site': 'Ovary'}], 'var_call_bq5EXxErODF5uZ0z6Nlg8DLc': 'file_storage/call_bq5EXxErODF5uZ0z6Nlg8DLc.json'}

exec(code, env_args)
