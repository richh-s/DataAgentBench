code = """import json
import pandas as pd
import re
import scipy.stats as stats

# Load clinical data
clinical_path = locals()['var_function-call-3798515127009661646']
with open(clinical_path, 'r') as f:
    clinical_data = json.load(f)

# Load mutation data
mutation_path = locals()['var_function-call-16084593933792914437']
with open(mutation_path, 'r') as f:
    mutation_data = json.load(f)

# Set of mutated barcodes
mutated_barcodes = set(item['ParticipantBarcode'] for item in mutation_data)

# Process clinical data
parsed_patients = []
dataset_names = set()

# Regex to parse description
# Example: "In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID ...) is recorded as a FEMALE..."
# Example: "Patient TCGA-36-1576 ... is a FEMALE diagnosed with Ovarian serous cystadenocarcinoma."
# Example: "Patient TCGA-32-4209 ... is enrolled in the study of Glioblastoma multiforme."

for entry in clinical_data:
    desc = entry.get('Patient_description', '')
    histo = entry.get('histological_type')
    
    if not desc:
        continue

    # Extract Gender
    gender = None
    if 'FEMALE' in desc:
        gender = 'FEMALE'
    elif 'MALE' in desc:
        gender = 'MALE'
    
    # Extract Barcode (TCGA-XX-XXXX)
    # Looking for pattern TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}
    barcode_match = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', desc)
    barcode = barcode_match.group(1) if barcode_match else None
    
    # Extract Dataset Name
    # This is trickier. It's often "In the [Name] dataset" or "diagnosed with [Name]" or "study of [Name]"
    dataset = None
    if "In the " in desc and " dataset" in desc:
        start = desc.find("In the ") + 7
        end = desc.find(" dataset")
        dataset = desc[start:end]
    elif "diagnosed with " in desc:
        start = desc.find("diagnosed with ") + 15
        # It might end with a period or " dataset" or " cohort" or just end of sentence
        # Let's take strictly until period or "with vital status"
        rest = desc[start:]
        # simplistic split
        dataset = rest.split('.')[0].split(',')[0].strip()
    elif "study of " in desc:
        start = desc.find("study of ") + 9
        dataset = desc[start:].split('.')[0].strip()
    elif "cohort" in desc:
        # "belongs to the [Name] cohort"
        if "belongs to the " in desc:
            start = desc.find("belongs to the ") + 15
            end = desc.find(" cohort")
            dataset = desc[start:end]
    
    if dataset:
        dataset_names.add(dataset)
        
    parsed_patients.append({
        'barcode': barcode,
        'gender': gender,
        'dataset': dataset,
        'histological_type': histo
    })

# Determine target dataset based on "BRCA"
# Hint: "BRCA means Bladder urothelial carcinoma"
target_dataset = None
# Check for Bladder
bladder_names = [name for name in dataset_names if "Bladder" in name and "urothelial" in name]
breast_names = [name for name in dataset_names if "Breast" in name]

# Logic to select
if bladder_names:
    target_dataset = bladder_names[0] # Assume one main dataset for Bladder
    print(f"DEBUG: Found Bladder dataset: {target_dataset}. Using it as per hint.")
elif breast_names:
    target_dataset = breast_names[0]
    print(f"DEBUG: Did not find Bladder dataset. Found Breast dataset: {target_dataset}. Using it.")
else:
    # Fallback or error
    print("DEBUG: Could not identify BRCA dataset.")
    target_dataset = "Unknown"

# Filter patients
filtered_patients = []
for p in parsed_patients:
    if p['gender'] == 'FEMALE' and p['dataset'] == target_dataset:
        # Check histological type
        if p['histological_type'] and p['histological_type'] not in ['None', 'not specified', '[Not Applicable]']:
            filtered_patients.append(p)

# Create contingency table data
# Categories: Histological Type vs Mutation Presence
data_for_chi2 = []
for p in filtered_patients:
    has_mutation = p['barcode'] in mutated_barcodes
    data_for_chi2.append({
        'histological_type': p['histological_type'],
        'has_mutation': has_mutation
    })

df = pd.DataFrame(data_for_chi2)

if df.empty:
    result = {"error": "No data found for criteria"}
else:
    # Contingency Table
    contingency = pd.crosstab(df['histological_type'], df['has_mutation'])
    
    # Filter by marginal totals (row totals > 10)
    # row sums
    row_sums = contingency.sum(axis=1)
    valid_types = row_sums[row_sums > 10].index
    filtered_contingency = contingency.loc[valid_types]
    
    # Ensure we have at least 2 rows and 2 columns for Chi-square?
    # Chi-square can work on R x C.
    # If filtered_contingency is empty or too small, handle it.
    
    if filtered_contingency.shape[0] < 2:
         result = {"error": "Not enough categories with > 10 samples", "table": filtered_contingency.to_dict()}
    else:
        chi2, p, dof, ex = stats.chi2_contingency(filtered_contingency)
        result = chi2

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-5007697578948868958': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_function-call-3853463295306617668': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_function-call-3798515127009661646': 'file_storage/function-call-3798515127009661646.json', 'var_function-call-16084593933792914437': 'file_storage/function-call-16084593933792914437.json'}

exec(code, env_args)
