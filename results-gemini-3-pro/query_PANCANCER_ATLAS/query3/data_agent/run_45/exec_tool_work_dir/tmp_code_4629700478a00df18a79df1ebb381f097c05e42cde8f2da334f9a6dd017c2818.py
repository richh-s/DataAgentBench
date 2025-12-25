code = """import json
import pandas as pd
from scipy.stats import chi2_contingency

# Load data
with open(locals()['var_function-call-10282961493402598584'], 'r') as f:
    target_patients = json.load(f)

with open(locals()['var_function-call-15377687020714808944'], 'r') as f:
    mutations = json.load(f)

mutated_barcodes = set(m['ParticipantBarcode'] for m in mutations)

# Create DataFrame
data = []
for p in target_patients:
    status = 'Present' if p['barcode'] in mutated_barcodes else 'Absent'
    data.append({
        'histological_type': p['histological_type'],
        'status': status
    })

df = pd.DataFrame(data)

# Create Contingency Table
# columns: Present, Absent
# index: histological_type
contingency = pd.crosstab(df['histological_type'], df['status'])

# Ensure both columns exist
if 'Present' not in contingency.columns:
    contingency['Present'] = 0
if 'Absent' not in contingency.columns:
    contingency['Absent'] = 0

# Filter categories with marginal total <= 10
# Marginal total here is the sum of row (Present + Absent)
contingency['Total'] = contingency['Present'] + contingency['Absent']
filtered_contingency = contingency[contingency['Total'] > 10].copy()

# Drop the Total column for the chi-square test
observed = filtered_contingency[['Present', 'Absent']]

# Calculate Chi-square
# chi2, p, dof, expected = chi2_contingency(observed)
if observed.shape[0] < 2:
    result = "Not enough categories to perform Chi-square test."
    chi2_stat = None
else:
    chi2_stat, p, dof, expected = chi2_contingency(observed)
    result = chi2_stat

print("__RESULT__:")
print(json.dumps({
    "contingency_table_before_filter": contingency.to_dict(orient='index'),
    "contingency_table_after_filter": observed.to_dict(orient='index'),
    "chi_square_statistic": result
}))"""

env_args = {'var_function-call-1803655151740534663': ['clinical_info'], 'var_function-call-7053211078668699123': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_function-call-16473721734446585115': 'file_storage/function-call-16473721734446585115.json', 'var_function-call-17565863393017369473': {'cancer_types_found': ['Bladder Urothelial Carcinoma', 'Brain Lower Grade Glioma', 'Glioblastoma Multiforme', 'Breast Invasive Carcinoma', 'Ovarian Serous Cystadenocarcinoma'], 'sample_parsed': [{'barcode': 'TCGA-31-1953', 'gender': 'FEMALE', 'cancer_type': 'Ovarian Serous Cystadenocarcinoma', 'histological_type': 'Serous Cystadenocarcinoma'}, {'barcode': 'TCGA-36-1576', 'gender': 'FEMALE', 'cancer_type': 'Ovarian Serous Cystadenocarcinoma', 'histological_type': 'Serous Cystadenocarcinoma'}, {'barcode': 'TCGA-25-2408', 'gender': 'FEMALE', 'cancer_type': 'Ovarian Serous Cystadenocarcinoma', 'histological_type': 'Serous Cystadenocarcinoma'}, {'barcode': 'TCGA-29-2427', 'gender': 'FEMALE', 'cancer_type': 'Ovarian Serous Cystadenocarcinoma', 'histological_type': 'Serous Cystadenocarcinoma'}, {'barcode': 'TCGA-10-0933', 'gender': 'FEMALE', 'cancer_type': 'Ovarian Serous Cystadenocarcinoma', 'histological_type': 'Serous Cystadenocarcinoma'}], 'count': 10198}, 'var_function-call-10282961493402598584': 'file_storage/function-call-10282961493402598584.json', 'var_function-call-15377687020714808944': 'file_storage/function-call-15377687020714808944.json'}

exec(code, env_args)
