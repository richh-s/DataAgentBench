code = """import json
import pandas as pd
import re

# helper to load stored variable which may be a file path or already data
def load_var(v):
    obj = globals().get(v)
    if isinstance(obj, str) and obj.endswith('.json'):
        with open(obj, 'r') as f:
            return json.load(f)
    return obj

# Load clinical alive BRCA records (from previous query)
clin_records = load_var('var_call_fV8ESXJY7IX0InF6xmOjzKka')
mut_records = load_var('var_call_CAS2fScfX8bGcZcdLzrzZaqZ')

# Convert to DataFrame
df_clin = pd.DataFrame(clin_records)
df_mut = pd.DataFrame(mut_records)

# Extract ParticipantBarcode from Patient_description using regex
pattern = re.compile(r'(TCGA-[A-Za-z0-9]{2}-[A-Za-z0-9]{4,6})')

def extract_barcode(desc):
    if not isinstance(desc, str):
        return None
    m = pattern.search(desc)
    return m.group(1) if m else None

if 'Patient_description' in df_clin.columns:
    df_clin['ParticipantBarcode'] = df_clin['Patient_description'].apply(extract_barcode)
else:
    df_clin['ParticipantBarcode'] = None

# Drop rows without extracted barcode
df_clin = df_clin.dropna(subset=['ParticipantBarcode'])

# Use patient-level unique mapping ParticipantBarcode -> histological_type
df_clin_unique = df_clin.drop_duplicates(subset=['ParticipantBarcode'])[['ParticipantBarcode','histological_type']]

# Ensure mutation participant barcodes are strings
if 'ParticipantBarcode' in df_mut.columns:
    df_mut['ParticipantBarcode'] = df_mut['ParticipantBarcode'].astype(str)
else:
    df_mut['ParticipantBarcode'] = []

mutated_participants = set(df_mut['ParticipantBarcode'].unique())

# For each histological type, compute total alive BRCA patients and mutated patients
group = df_clin_unique.groupby('histological_type')['ParticipantBarcode'].apply(lambda x: set(x)).reset_index()

results = []
for _, row in group.iterrows():
    hist = row['histological_type']
    participants = row['ParticipantBarcode']
    total = len(participants)
    mutated = len(participants & mutated_participants)
    pct = (mutated / total * 100) if total>0 else 0.0
    results.append({'histological_type': hist, 'total_patients': total, 'mutated_patients': mutated, 'percentage': round(pct,4)})

# Sort descending by percentage, then by mutated count, then total
results_sorted = sorted(results, key=lambda x: (-x['percentage'], -x['mutated_patients'], -x['total_patients']))

top3 = results_sorted[:3]

# Prepare JSON-serializable output
output = top3

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_m2iC6a02juln5lOLZY17YFle': ['clinical_info'], 'var_call_ksksuW26DzO8nmGstIYYgSLX': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_Nlf2mD6c3V90wcozrCYfGE0j': 'file_storage/call_Nlf2mD6c3V90wcozrCYfGE0j.json', 'var_call_SzrvkmFj6V8JK1L512MUU8g3': 'file_storage/call_SzrvkmFj6V8JK1L512MUU8g3.json', 'var_call_YzOcT7LfhcB0lTuqgIKW9pfC': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_fV8ESXJY7IX0InF6xmOjzKka': 'file_storage/call_fV8ESXJY7IX0InF6xmOjzKka.json', 'var_call_CAS2fScfX8bGcZcdLzrzZaqZ': 'file_storage/call_CAS2fScfX8bGcZcdLzrzZaqZ.json'}

exec(code, env_args)
