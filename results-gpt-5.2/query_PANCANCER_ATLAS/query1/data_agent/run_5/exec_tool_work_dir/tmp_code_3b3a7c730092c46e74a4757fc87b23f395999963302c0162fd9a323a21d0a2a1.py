code = """import json, re, math, pandas as pd

def load_result(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r') as f:
            return json.load(f)
    return v

expr = load_result(var_call_346BWcZXz0YzSbnJTcgBYMOV)
clin = load_result(var_call_8kk4FlcgYRLLLPEIU7sDt0qT)

df_expr = pd.DataFrame(expr)
df_expr['normalized_count'] = pd.to_numeric(df_expr['normalized_count'], errors='coerce')
df_expr = df_expr.dropna(subset=['normalized_count'])

df_clin = pd.DataFrame(clin)
# fix column name casing from query result preview
if 'ParticipantBarcode' not in df_clin.columns and 'participantbarcode' in df_clin.columns:
    df_clin = df_clin.rename(columns={'participantbarcode':'ParticipantBarcode'})

# extract TCGA barcode from Patient_description text
pat = re.compile(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})')
df_clin['ParticipantBarcode_extracted'] = df_clin['ParticipantBarcode'].astype(str).str.extract(pat, expand=False)

df = df_clin.merge(df_expr, left_on='ParticipantBarcode_extracted', right_on='ParticipantBarcode', how='inner')

# keep LGG only: infer from histological_type being LGG-like (exclude GBM). We'll filter by histological_type containing 'astrocytoma' or 'oligodendro' or 'oligoastro' and not containing 'GBM'/'Glioblastoma'
h = df['histological_type'].astype(str)
mask_lgg = (~h.str.contains('GBM|Glioblastoma', case=False, na=False))
df = df[mask_lgg].copy()

# valid histology not enclosed in square brackets
hist = df['histological_type'].astype(str).str.strip()
df = df[~hist.str.match(r'^\[.*\]$')].copy()

df['log10_expr'] = (df['normalized_count'] + 1).apply(lambda x: math.log10(x) if pd.notna(x) and x>=0 else float('nan'))
df = df.dropna(subset=['log10_expr','histological_type'])

res = df.groupby('histological_type')['log10_expr'].mean().sort_index()
# format with 4 decimals
out_lines = []
for k,v in res.items():
    out_lines.append(f"{k}: {v:.4f}")
answer = "\n".join(out_lines) if out_lines else "No matching LGG patients with valid IGF2 expression and histology."
print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_346BWcZXz0YzSbnJTcgBYMOV': 'file_storage/call_346BWcZXz0YzSbnJTcgBYMOV.json', 'var_call_1q6YXllIHS2kFPEG1D32Uajh': ['clinical_info'], 'var_call_islrdbOptVTnof8kic5adBMu': [{'column_name': 'Patient_description'}, {'column_name': 'days_to_birth'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'stopped_smoking_year'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'prior_glioma'}], 'var_call_tFEaGW6yYBFvqiDFg1rLwPji': [{'diagnosis': 'None'}, {'diagnosis': 'Lung Adenocarcinoma'}, {'diagnosis': 'Lung Squamous Cell Carcinoma'}], 'var_call_EE4Npb5YbLS6JSyceLVqCMbj': [], 'var_call_9kwzUF2Onzjea58oYlqvNHIJ': [{'tumor_tissue_site': 'Brain'}], 'var_call_8kk4FlcgYRLLLPEIU7sDt0qT': 'file_storage/call_8kk4FlcgYRLLLPEIU7sDt0qT.json'}

exec(code, env_args)
