code = """import json
import pandas as pd
import re

# Load clinical data (Breast)
with open(locals()['var_function-call-16082043096577375108'], 'r') as f:
    clinical_data = json.load(f)

# Load mutation data
with open(locals()['var_function-call-11650657680070858035'], 'r') as f:
    mutation_data = json.load(f)

# Create Mutation Set
mutated_barcodes = set(item['ParticipantBarcode'] for item in mutation_data)

# Process Clinical Data
clinical_records = []
for entry in clinical_data:
    desc = entry.get('Patient_description', '')
    hist_type = entry.get('histological_type', 'None')
    
    # Extract Barcode
    match = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', desc)
    if match:
        barcode = match.group(1)
        clinical_records.append({
            'ParticipantBarcode': barcode,
            'histological_type': hist_type
        })

df_clinical = pd.DataFrame(clinical_records)

# Filter out None
df_clinical = df_clinical[df_clinical['histological_type'] != 'None']
# Maybe filter out 'Other  specify' if it's not a real type, but the prompt asks for histological types. 
# I will keep it as it is a category in the data.

# Mark mutations
df_clinical['has_cdh1'] = df_clinical['ParticipantBarcode'].isin(mutated_barcodes)

# Group by histological type
summary = df_clinical.groupby('histological_type').agg(
    total=('ParticipantBarcode', 'count'),
    mutated=('has_cdh1', 'sum')
).reset_index()

summary['percentage'] = (summary['mutated'] / summary['total']) * 100

# Sort
summary = summary.sort_values(by='percentage', ascending=False)

# Get Top 3
# I'll print the whole summary first to debug/verify, then filter for result.
print("DEBUG SUMMARY:")
print(summary.to_string())

top_3 = summary.head(3)[['histological_type', 'percentage']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(top_3))"""

env_args = {'var_function-call-16500875047121465705': ['clinical_info'], 'var_function-call-17448327437279529341': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_function-call-17054074113607652585': 'file_storage/function-call-17054074113607652585.json', 'var_function-call-11650657680070858035': 'file_storage/function-call-11650657680070858035.json', 'var_function-call-12641434634769753740': [{'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'percentage': 3.070175438596491}], 'var_function-call-17535181861303441439': [{'count': '1087'}], 'var_function-call-6796542864995917638': ['Muscle invasive urothelial carcinoma (pT2 or above)', 'None'], 'var_function-call-16082043096577375108': 'file_storage/function-call-16082043096577375108.json'}

exec(code, env_args)
