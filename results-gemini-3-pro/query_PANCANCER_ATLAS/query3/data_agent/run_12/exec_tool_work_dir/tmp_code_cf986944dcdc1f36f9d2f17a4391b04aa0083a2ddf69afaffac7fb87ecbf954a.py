code = """import json
import re
import pandas as pd

# Load data
with open(locals()['var_function-call-3145426949494474129'], 'r') as f:
    clinical_data = json.load(f)

with open(locals()['var_function-call-17781900019803178841'], 'r') as f:
    mutation_data = json.load(f)

# Set of mutated patients
mutated_patients = set()
for m in mutation_data:
    # ParticipantBarcode usually 12 chars: TCGA-XX-XXXX
    # Ensure we handle potential suffixes if any, though preview showed 12 chars.
    bc = m.get('ParticipantBarcode')
    if bc:
        mutated_patients.add(bc)

# Process clinical data
records = []
barcode_pattern = re.compile(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})')

for entry in clinical_data:
    desc = entry.get('Patient_description', '')
    hist_type = entry.get('histological_type')
    
    # Check for FEMALE
    if 'FEMALE' not in desc:
        continue
        
    # Extract Barcode
    match = barcode_pattern.search(desc)
    if not match:
        continue
    barcode = match.group(1)
    
    # Determine mutation status
    has_mutation = 1 if barcode in mutated_patients else 0
    
    records.append({
        'histological_type': hist_type,
        'has_mutation': has_mutation
    })

df = pd.DataFrame(records)

# Group by histological type
# We need counts of Mutation (1) and No Mutation (0)
# Pivot table: Index=histological_type, Columns=has_mutation, Values=count
contingency = pd.crosstab(df['histological_type'], df['has_mutation'])

# Ensure both columns 0 and 1 exist (in case no mutations found for any, or all mutated)
if 0 not in contingency.columns:
    contingency[0] = 0
if 1 not in contingency.columns:
    contingency[1] = 0

contingency = contingency[[0, 1]] # Order: Wildtype, Mutated (or vice versa, doesn't matter for Chi2)

# Filter by marginal totals (row sums) > 10
contingency['total'] = contingency[0] + contingency[1]
filtered_contingency = contingency[contingency['total'] > 10].drop(columns=['total'])

# Calculate Chi-Square manually
# Observed
obs = filtered_contingency.values
row_totals = obs.sum(axis=1)
col_totals = obs.sum(axis=0)
grand_total = obs.sum()

chi2_stat = 0.0

for i in range(len(row_totals)):
    for j in range(len(col_totals)):
        O_ij = obs[i, j]
        E_ij = (row_totals[i] * col_totals[j]) / grand_total
        if E_ij > 0:
            chi2_stat += ((O_ij - E_ij) ** 2) / E_ij

print("__RESULT__:")
print(json.dumps({
    "chi_square_statistic": chi2_stat,
    "contingency_table": filtered_contingency.to_dict(),
    "filtered_types": filtered_contingency.index.tolist()
}))"""

env_args = {'var_function-call-7598718398071722398': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_function-call-13647773958914267842': [{'breast_count': '1087', 'bladder_count': '412'}], 'var_function-call-7260272696838531730': [{'histological_type': 'None'}, {'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}], 'var_function-call-3962853977545954679': [{'histological_type': 'None'}, {'histological_type': 'Infiltrating Ductal Carcinoma'}, {'histological_type': 'Mucinous Carcinoma'}, {'histological_type': 'Metaplastic Carcinoma'}, {'histological_type': 'Mixed Histology (please specify)'}, {'histological_type': 'Infiltrating Lobular Carcinoma'}, {'histological_type': 'Other  specify'}, {'histological_type': 'Medullary Carcinoma'}, {'histological_type': 'Infiltrating Carcinoma NOS'}], 'var_function-call-3145426949494474129': 'file_storage/function-call-3145426949494474129.json', 'var_function-call-17781900019803178841': 'file_storage/function-call-17781900019803178841.json'}

exec(code, env_args)
