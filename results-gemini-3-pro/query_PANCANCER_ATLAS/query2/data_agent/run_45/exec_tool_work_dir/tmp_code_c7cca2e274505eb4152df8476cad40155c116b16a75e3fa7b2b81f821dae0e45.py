code = """import json
import re

# Load clinical data
clinical_key = 'var_function-call-8701612506116882773'
with open(locals()[clinical_key], 'r') as f:
    clinical_data = json.load(f)

# Load mutation data
mutation_key = 'var_function-call-5428035111591218947'
with open(locals()[mutation_key], 'r') as f:
    mutation_data = json.load(f)

# Extract barcodes and map to histological type for alive BRCA (Bladder) patients
patient_histology = {}
barcode_pattern = re.compile(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})')

for record in clinical_data:
    desc = record.get('Patient_description', '')
    hist_type = record.get('histological_type', 'Unknown')
    
    # Extract barcode
    match = barcode_pattern.search(desc)
    if match:
        barcode = match.group(1)
        # Store or update. Assuming one histology per patient.
        patient_histology[barcode] = hist_type

# Create a set of patients with CDH1 mutations
mutated_patients = set()
for record in mutation_data:
    bc = record.get('ParticipantBarcode')
    if bc:
        mutated_patients.add(bc)

# Aggregate counts per histological type
# Stats structure: {hist_type: {'total': 0, 'mutated': 0}}
stats = {}

for barcode, h_type in patient_histology.items():
    if h_type == 'None' or h_type == 'Unknown':
        continue # skip None histological type
        
    if h_type not in stats:
        stats[h_type] = {'total': 0, 'mutated': 0}
    
    stats[h_type]['total'] += 1
    if barcode in mutated_patients:
        stats[h_type]['mutated'] += 1

# Calculate percentages
results = []
for h_type, counts in stats.items():
    if counts['total'] > 0:
        percentage = (counts['mutated'] / counts['total']) * 100
        results.append({
            'histological_type': h_type,
            'percentage': percentage,
            'mutated': counts['mutated'],
            'total': counts['total']
        })

# Sort by percentage descending
results.sort(key=lambda x: x['percentage'], reverse=True)

# Top 3
top_3 = results[:3]

print("__RESULT__:")
print(json.dumps(top_3))"""

env_args = {'var_function-call-724816171416864179': ['clinical_info'], 'var_function-call-6307938628307616171': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_function-call-13179663749873490839': [{'dataset_name': 'Breast invasive carcinoma dataset, patie', 'count': '140'}, {'dataset_name': 'Uterine Corpus Endometrial Carcinoma dat', 'count': '86'}, {'dataset_name': 'Ovarian serous cystadenocarcinoma datase', 'count': '79'}, {'dataset_name': 'Glioblastoma multiforme dataset, patient', 'count': '74'}, {'dataset_name': 'Colon adenocarcinoma dataset, patient TC', 'count': '69'}, {'dataset_name': 'Thyroid carcinoma dataset, patient TCGA-', 'count': '68'}, {'dataset_name': 'Kidney renal clear cell carcinoma datase', 'count': '67'}, {'dataset_name': 'Prostate adenocarcinoma dataset, patient', 'count': '64'}, {'dataset_name': 'Head and Neck squamous cell carcinoma da', 'count': '62'}, {'dataset_name': 'Bladder urothelial carcinoma dataset, pa', 'count': '60'}], 'var_function-call-8701612506116882773': 'file_storage/function-call-8701612506116882773.json', 'var_function-call-5428035111591218947': 'file_storage/function-call-5428035111591218947.json'}

exec(code, env_args)
