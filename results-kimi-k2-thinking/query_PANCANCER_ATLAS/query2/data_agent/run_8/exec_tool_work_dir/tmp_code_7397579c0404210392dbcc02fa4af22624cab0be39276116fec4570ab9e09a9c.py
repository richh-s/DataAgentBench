code = """import json
import re

# Read the file with the clinical data
with open('var_functions.query_db:14', 'r') as f:
    brca_alive_patients = json.load(f)

# Extract patient barcodes from Patient_description
patient_barcodes = []
barcode_pattern = r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}'

for patient in brca_alive_patients:
    patient_desc = patient['Patient_description']
    matches = re.findall(barcode_pattern, patient_desc)
    if matches:
        patient_barcodes.append(matches[0])

unique_barcodes = list(set(patient_barcodes))
print('__RESULT__:')
print(json.dumps({
    'total_brca_alive_patients': len(brca_alive_patients),
    'unique_barcodes_extracted': len(unique_barcodes),
    'sample_barcodes': unique_barcodes[:10]
}))"""

env_args = {'var_functions.query_db:0': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}], 'var_functions.query_db:2': [{'column_name': 'Patient_description'}, {'column_name': 'patient_id'}, {'column_name': 'patient_death_reason'}], 'var_functions.query_db:5': [], 'var_functions.query_db:6': [{'person_neoplasm_cancer_status': 'TUMOR FREE'}, {'person_neoplasm_cancer_status': 'WITH TUMOR'}, {'person_neoplasm_cancer_status': '[Discrepancy]'}, {'person_neoplasm_cancer_status': '[Unknown]'}, {'person_neoplasm_cancer_status': 'None'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
