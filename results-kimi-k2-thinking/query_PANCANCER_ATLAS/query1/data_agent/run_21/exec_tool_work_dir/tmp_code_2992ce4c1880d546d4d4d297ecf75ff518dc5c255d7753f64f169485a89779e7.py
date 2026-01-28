code = """import json
import re
import math

# Access LGG clinical data from query_db_24
lgg_patients = var_functions.query_db_24

# Access IGF2 expression data from query_db_15
igf2_expr = var_functions.query_db_15

# Extract barcodes and histological types from LGG patients
lgg_data = []
for patient in lgg_patients:
    desc = patient['Patient_description']
    hist_type = patient['histological_type']
    
    # Extract TCGA barcode from description (pattern: TCGA-XX-XXXX)
    match = re.search(r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}', desc)
    if match:
        barcode = match.group(0)
        lgg_data.append({
            'ParticipantBarcode': barcode,
            'histological_type': hist_type
        })

# Convert IGF2 expression data to dictionary for fast lookup by barcode
igf2_dict = {}
for item in igf2_expr:
    try:
        # Handle cases where normalized_count might be a string
        count_str = item['normalized_count']
        if count_str is not None and count_str != '':
            igf2_dict[item['ParticipantBarcode']] = float(count_str)
    except (ValueError, TypeError):
        continue

# Match LGG patients with IGF2 expression data and compute log10-transformed values
histology_groups = {}
total_matched = 0

for patient in lgg_data:
    barcode = patient['ParticipantBarcode']
    hist_type = patient['histological_type']
    
    if barcode in igf2_dict:
        expr_value = igf2_dict[barcode]
        # Compute log10(normalized_count + 1) as per standard practice
        log_expr = math.log10(expr_value + 1)
        
        if hist_type not in histology_groups:
            histology_groups[hist_type] = []
        histology_groups[hist_type].append(log_expr)
        total_matched += 1

# Compute average log10 expression for each histology type
averages = {}
for hist_type, values in histology_groups.items():
    if values:  # Only include histology types with data
        avg_log10 = sum(values) / len(values)
        averages[hist_type] = {
            'average_log10_expression': round(avg_log10, 4),
            'sample_count': len(values)
        }

# Create summary
result = {
    'total_lgg_patients_identified': len(lgg_patients),
    'patients_with_igf2_data': total_matched,
    'histology_type_averages': averages
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.list_db:2': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:6': [{'column_name': 'stopped_smoking_year', 'data_type': 'double precision'}, {'column_name': 'days_to_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'number_of_lymphnodes_positive_by_he', 'data_type': 'double precision'}, {'column_name': 'age_at_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'year_of_tobacco_smoking_onset', 'data_type': 'double precision'}, {'column_name': 'year_of_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'height', 'data_type': 'double precision'}, {'column_name': 'weight', 'data_type': 'double precision'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc', 'data_type': 'double precision'}, {'column_name': 'days_to_birth', 'data_type': 'double precision'}, {'column_name': 'total_pelv_lnr', 'data_type': 'double precision'}, {'column_name': 'total_aor_lnr', 'data_type': 'double precision'}, {'column_name': 'number_pack_years_smoked', 'data_type': 'double precision'}, {'column_name': 'prior_dx', 'data_type': 'text'}, {'column_name': 'ethnicity', 'data_type': 'text'}], 'var_functions.query_db:8': [{'column_name': 'Patient_description', 'data_type': 'text'}, {'column_name': 'days_to_birth', 'data_type': 'double precision'}, {'column_name': 'days_to_death', 'data_type': 'text'}, {'column_name': 'days_to_last_followup', 'data_type': 'text'}, {'column_name': 'days_to_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'age_at_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'icd_10', 'data_type': 'text'}, {'column_name': 'tissue_retrospective_collection_indicator', 'data_type': 'text'}, {'column_name': 'icd_o_3_histology', 'data_type': 'text'}, {'column_name': 'tissue_prospective_collection_indicator', 'data_type': 'text'}, {'column_name': 'history_of_neoadjuvant_treatment', 'data_type': 'text'}, {'column_name': 'icd_o_3_site', 'data_type': 'text'}, {'column_name': 'tumor_tissue_site', 'data_type': 'text'}, {'column_name': 'new_tumor_event_after_initial_treatment', 'data_type': 'text'}, {'column_name': 'radiation_therapy', 'data_type': 'text'}, {'column_name': 'race', 'data_type': 'text'}, {'column_name': 'prior_dx', 'data_type': 'text'}, {'column_name': 'ethnicity', 'data_type': 'text'}, {'column_name': 'informed_consent_verified', 'data_type': 'text'}, {'column_name': 'person_neoplasm_cancer_status', 'data_type': 'text'}, {'column_name': 'patient_id', 'data_type': 'text'}, {'column_name': 'year_of_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'histological_type', 'data_type': 'text'}, {'column_name': 'tissue_source_site', 'data_type': 'text'}, {'column_name': 'form_completion_date', 'data_type': 'text'}, {'column_name': 'pathologic_T', 'data_type': 'text'}, {'column_name': 'pathologic_M', 'data_type': 'text'}, {'column_name': 'clinical_M', 'data_type': 'text'}, {'column_name': 'pathologic_N', 'data_type': 'text'}, {'column_name': 'system_version', 'data_type': 'text'}], 'var_functions.query_db:10': [{'histological_type': 'Oligodendroglioma'}, {'histological_type': 'Paraganglioma'}, {'histological_type': 'Paraganglioma; Extra-adrenal Pheochromocytoma'}], 'var_functions.query_db:12': [{'icd_o_3_histology': '8680/1', 'histological_type': 'Paraganglioma; Extra-adrenal Pheochromocytoma'}, {'icd_o_3_histology': '8680/3', 'histological_type': 'Paraganglioma'}, {'icd_o_3_histology': '8691/1', 'histological_type': 'Paraganglioma'}, {'icd_o_3_histology': '8693/1', 'histological_type': 'Paraganglioma'}, {'icd_o_3_histology': '8693/1', 'histological_type': 'Paraganglioma; Extra-adrenal Pheochromocytoma'}, {'icd_o_3_histology': '8693/3', 'histological_type': 'Paraganglioma'}, {'icd_o_3_histology': '8693/3', 'histological_type': 'Paraganglioma; Extra-adrenal Pheochromocytoma'}, {'icd_o_3_histology': '8700/3', 'histological_type': 'Paraganglioma'}, {'icd_o_3_histology': '9382/3', 'histological_type': 'Oligodendroglioma'}, {'icd_o_3_histology': '9450/3', 'histological_type': 'Oligodendroglioma'}, {'icd_o_3_histology': '9451/3', 'histological_type': 'Oligodendroglioma'}], 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json', 'var_functions.query_db:18': [{'icd_o_3_histology': '9400/3', 'histological_type': 'Astrocytoma'}, {'icd_o_3_histology': '9400/3', 'histological_type': 'Oligoastrocytoma'}, {'icd_o_3_histology': '9440/3', 'histological_type': 'Treated primary GBM'}, {'icd_o_3_histology': '9382/3', 'histological_type': 'Oligodendroglioma'}, {'icd_o_3_histology': '9440/3', 'histological_type': 'Glioblastoma Multiforme (GBM)'}, {'icd_o_3_histology': '9440/3', 'histological_type': 'Untreated primary (de novo) GBM'}, {'icd_o_3_histology': '9401/3', 'histological_type': 'Astrocytoma'}, {'icd_o_3_histology': '9382/3', 'histological_type': 'Oligoastrocytoma'}, {'icd_o_3_histology': '9382/3', 'histological_type': 'Astrocytoma'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
