code = """import json
import re
import math

# Access the variables using the correct keys
lgg_patients = locals()['var_functions.query_db:24']
igf2_file_path = locals()['var_functions.query_db:15']

# Read IGF2 expression data from file
with open(igf2_file_path, 'r') as f:
    igf2_expression_data = json.load(f)

# Extract LGG patient barcodes and histology types
lgg_patients_data = []
barcode_pattern = re.compile(r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}')

for patient in lgg_patients:
    desc = patient['Patient_description']
    hist_type = patient['histological_type']
    
    match = barcode_pattern.search(desc)
    if match:
        barcode = match.group(0)
        lgg_patients_data.append({
            'ParticipantBarcode': barcode,
            'histological_type': hist_type
        })

# Create IGF2 expression dictionary
igf2_dict = {}
for record in igf2_expression_data:
    try:
        if record['normalized_count'] is not None:
            igf2_dict[record['ParticipantBarcode']] = float(record['normalized_count'])
    except (ValueError, TypeError, KeyError):
        continue

# Match and compute log10 expression
histology_groups = {}
successful_matches = 0

for patient in lgg_patients_data:
    barcode = patient['ParticipantBarcode']
    histology = patient['histological_type']
    
    if barcode in igf2_dict:
        expr_value = igf2_dict[barcode]
        log_transformed = math.log10(expr_value + 1)
        
        if histology not in histology_groups:
            histology_groups[histology] = []
        histology_groups[histology].append(log_transformed)
        successful_matches += 1

# Calculate averages for each histology type
results = {}
for histology, values in histology_groups.items():
    if values:
        avg_value = sum(values) / len(values)
        results[histology] = {
            'average_log10_expression': round(avg_value, 4),
            'sample_size': len(values)
        }

# Create final summary
final_output = {
    'total_lgg_patients': len(lgg_patients),
    'matched_with_expression_data': successful_matches,
    'average_expression_by_histology': results
}

print('__RESULT__:')
print(json.dumps(final_output, indent=2))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.list_db:2': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:6': [{'column_name': 'stopped_smoking_year', 'data_type': 'double precision'}, {'column_name': 'days_to_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'number_of_lymphnodes_positive_by_he', 'data_type': 'double precision'}, {'column_name': 'age_at_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'year_of_tobacco_smoking_onset', 'data_type': 'double precision'}, {'column_name': 'year_of_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'height', 'data_type': 'double precision'}, {'column_name': 'weight', 'data_type': 'double precision'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc', 'data_type': 'double precision'}, {'column_name': 'days_to_birth', 'data_type': 'double precision'}, {'column_name': 'total_pelv_lnr', 'data_type': 'double precision'}, {'column_name': 'total_aor_lnr', 'data_type': 'double precision'}, {'column_name': 'number_pack_years_smoked', 'data_type': 'double precision'}, {'column_name': 'prior_dx', 'data_type': 'text'}, {'column_name': 'ethnicity', 'data_type': 'text'}], 'var_functions.query_db:8': [{'column_name': 'Patient_description', 'data_type': 'text'}, {'column_name': 'days_to_birth', 'data_type': 'double precision'}, {'column_name': 'days_to_death', 'data_type': 'text'}, {'column_name': 'days_to_last_followup', 'data_type': 'text'}, {'column_name': 'days_to_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'age_at_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'icd_10', 'data_type': 'text'}, {'column_name': 'tissue_retrospective_collection_indicator', 'data_type': 'text'}, {'column_name': 'icd_o_3_histology', 'data_type': 'text'}, {'column_name': 'tissue_prospective_collection_indicator', 'data_type': 'text'}, {'column_name': 'history_of_neoadjuvant_treatment', 'data_type': 'text'}, {'column_name': 'icd_o_3_site', 'data_type': 'text'}, {'column_name': 'tumor_tissue_site', 'data_type': 'text'}, {'column_name': 'new_tumor_event_after_initial_treatment', 'data_type': 'text'}, {'column_name': 'radiation_therapy', 'data_type': 'text'}, {'column_name': 'race', 'data_type': 'text'}, {'column_name': 'prior_dx', 'data_type': 'text'}, {'column_name': 'ethnicity', 'data_type': 'text'}, {'column_name': 'informed_consent_verified', 'data_type': 'text'}, {'column_name': 'person_neoplasm_cancer_status', 'data_type': 'text'}, {'column_name': 'patient_id', 'data_type': 'text'}, {'column_name': 'year_of_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'histological_type', 'data_type': 'text'}, {'column_name': 'tissue_source_site', 'data_type': 'text'}, {'column_name': 'form_completion_date', 'data_type': 'text'}, {'column_name': 'pathologic_T', 'data_type': 'text'}, {'column_name': 'pathologic_M', 'data_type': 'text'}, {'column_name': 'clinical_M', 'data_type': 'text'}, {'column_name': 'pathologic_N', 'data_type': 'text'}, {'column_name': 'system_version', 'data_type': 'text'}], 'var_functions.query_db:10': [{'histological_type': 'Oligodendroglioma'}, {'histological_type': 'Paraganglioma'}, {'histological_type': 'Paraganglioma; Extra-adrenal Pheochromocytoma'}], 'var_functions.query_db:12': [{'icd_o_3_histology': '8680/1', 'histological_type': 'Paraganglioma; Extra-adrenal Pheochromocytoma'}, {'icd_o_3_histology': '8680/3', 'histological_type': 'Paraganglioma'}, {'icd_o_3_histology': '8691/1', 'histological_type': 'Paraganglioma'}, {'icd_o_3_histology': '8693/1', 'histological_type': 'Paraganglioma'}, {'icd_o_3_histology': '8693/1', 'histological_type': 'Paraganglioma; Extra-adrenal Pheochromocytoma'}, {'icd_o_3_histology': '8693/3', 'histological_type': 'Paraganglioma'}, {'icd_o_3_histology': '8693/3', 'histological_type': 'Paraganglioma; Extra-adrenal Pheochromocytoma'}, {'icd_o_3_histology': '8700/3', 'histological_type': 'Paraganglioma'}, {'icd_o_3_histology': '9382/3', 'histological_type': 'Oligodendroglioma'}, {'icd_o_3_histology': '9450/3', 'histological_type': 'Oligodendroglioma'}, {'icd_o_3_histology': '9451/3', 'histological_type': 'Oligodendroglioma'}], 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json', 'var_functions.query_db:18': [{'icd_o_3_histology': '9400/3', 'histological_type': 'Astrocytoma'}, {'icd_o_3_histology': '9400/3', 'histological_type': 'Oligoastrocytoma'}, {'icd_o_3_histology': '9440/3', 'histological_type': 'Treated primary GBM'}, {'icd_o_3_histology': '9382/3', 'histological_type': 'Oligodendroglioma'}, {'icd_o_3_histology': '9440/3', 'histological_type': 'Glioblastoma Multiforme (GBM)'}, {'icd_o_3_histology': '9440/3', 'histological_type': 'Untreated primary (de novo) GBM'}, {'icd_o_3_histology': '9401/3', 'histological_type': 'Astrocytoma'}, {'icd_o_3_histology': '9382/3', 'histological_type': 'Oligoastrocytoma'}, {'icd_o_3_histology': '9382/3', 'histological_type': 'Astrocytoma'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
