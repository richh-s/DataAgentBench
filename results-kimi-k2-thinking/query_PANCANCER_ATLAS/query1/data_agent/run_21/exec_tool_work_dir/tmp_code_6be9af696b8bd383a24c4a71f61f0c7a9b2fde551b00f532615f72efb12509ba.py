code = """import json
import re
import math

# Access LGG clinical data (file path)
lgg_file_path = locals()['var_functions.query_db:52']

# Read LGG patient data
with open(lgg_file_path, 'r') as f:
    lgg_patients = json.load(f)

# Access IGF2 expression data (file path)
igf2_file_path = locals()['var_functions.query_db:15']

# Read IGF2 expression data
with open(igf2_file_path, 'r') as f:
    igf2_expression = json.load(f)

# Extract barcodes and histology from LGG patients
lgg_data = []
barcode_pattern = re.compile(r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}')

for patient in lgg_patients:
    desc = patient['Patient_description']
    hist_type = patient['histological_type']
    
    # Extract barcode
    match = barcode_pattern.search(desc)
    if match:
        barcode = match.group(0)
        lgg_data.append({
            'barcode': barcode,
            'histology': hist_type
        })

# Create IGF2 expression dictionary
igf2_dict = {}
for record in igf2_expression:
    try:
        if record['normalized_count'] is not None:
            igf2_dict[record['ParticipantBarcode']] = float(record['normalized_count'])
    except (ValueError, TypeError, KeyError):
        continue

# Match patients with expression data and compute log10 values
histology_groups = {}
matched_patients = 0

for patient in lgg_data:
    barcode = patient['barcode']
    histology = patient['histology']
    
    if barcode in igf2_dict:
        expr_value = igf2_dict[barcode]
        # Compute log10(normalized_count + 1)
        log_transformed = math.log10(expr_value + 1)
        
        if histology not in histology_groups:
            histology_groups[histology] = []
        histology_groups[histology].append(log_transformed)
        matched_patients += 1

# Calculate averages for each histology type
results = {}
for histology, values in sorted(histology_groups.items()):
    if values:
        avg = sum(values) / len(values)
        results[histology] = {
            'average_log10_expression': round(avg, 4),
            'sample_count': len(values)
        }

# Prepare final output
final_results = {
    'summary': {
        'total_lgg_patients': len(lgg_patients),
        'patients_with_igf2_data': matched_patients,
        'histology_types_analyzed': len(results)
    },
    'averages_by_histology': results
}

print('__RESULT__:')
print(json.dumps(final_results, indent=2))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.list_db:2': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:6': [{'column_name': 'stopped_smoking_year', 'data_type': 'double precision'}, {'column_name': 'days_to_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'number_of_lymphnodes_positive_by_he', 'data_type': 'double precision'}, {'column_name': 'age_at_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'year_of_tobacco_smoking_onset', 'data_type': 'double precision'}, {'column_name': 'year_of_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'height', 'data_type': 'double precision'}, {'column_name': 'weight', 'data_type': 'double precision'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc', 'data_type': 'double precision'}, {'column_name': 'days_to_birth', 'data_type': 'double precision'}, {'column_name': 'total_pelv_lnr', 'data_type': 'double precision'}, {'column_name': 'total_aor_lnr', 'data_type': 'double precision'}, {'column_name': 'number_pack_years_smoked', 'data_type': 'double precision'}, {'column_name': 'prior_dx', 'data_type': 'text'}, {'column_name': 'ethnicity', 'data_type': 'text'}], 'var_functions.query_db:8': [{'column_name': 'Patient_description', 'data_type': 'text'}, {'column_name': 'days_to_birth', 'data_type': 'double precision'}, {'column_name': 'days_to_death', 'data_type': 'text'}, {'column_name': 'days_to_last_followup', 'data_type': 'text'}, {'column_name': 'days_to_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'age_at_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'icd_10', 'data_type': 'text'}, {'column_name': 'tissue_retrospective_collection_indicator', 'data_type': 'text'}, {'column_name': 'icd_o_3_histology', 'data_type': 'text'}, {'column_name': 'tissue_prospective_collection_indicator', 'data_type': 'text'}, {'column_name': 'history_of_neoadjuvant_treatment', 'data_type': 'text'}, {'column_name': 'icd_o_3_site', 'data_type': 'text'}, {'column_name': 'tumor_tissue_site', 'data_type': 'text'}, {'column_name': 'new_tumor_event_after_initial_treatment', 'data_type': 'text'}, {'column_name': 'radiation_therapy', 'data_type': 'text'}, {'column_name': 'race', 'data_type': 'text'}, {'column_name': 'prior_dx', 'data_type': 'text'}, {'column_name': 'ethnicity', 'data_type': 'text'}, {'column_name': 'informed_consent_verified', 'data_type': 'text'}, {'column_name': 'person_neoplasm_cancer_status', 'data_type': 'text'}, {'column_name': 'patient_id', 'data_type': 'text'}, {'column_name': 'year_of_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'histological_type', 'data_type': 'text'}, {'column_name': 'tissue_source_site', 'data_type': 'text'}, {'column_name': 'form_completion_date', 'data_type': 'text'}, {'column_name': 'pathologic_T', 'data_type': 'text'}, {'column_name': 'pathologic_M', 'data_type': 'text'}, {'column_name': 'clinical_M', 'data_type': 'text'}, {'column_name': 'pathologic_N', 'data_type': 'text'}, {'column_name': 'system_version', 'data_type': 'text'}], 'var_functions.query_db:10': [{'histological_type': 'Oligodendroglioma'}, {'histological_type': 'Paraganglioma'}, {'histological_type': 'Paraganglioma; Extra-adrenal Pheochromocytoma'}], 'var_functions.query_db:12': [{'icd_o_3_histology': '8680/1', 'histological_type': 'Paraganglioma; Extra-adrenal Pheochromocytoma'}, {'icd_o_3_histology': '8680/3', 'histological_type': 'Paraganglioma'}, {'icd_o_3_histology': '8691/1', 'histological_type': 'Paraganglioma'}, {'icd_o_3_histology': '8693/1', 'histological_type': 'Paraganglioma'}, {'icd_o_3_histology': '8693/1', 'histological_type': 'Paraganglioma; Extra-adrenal Pheochromocytoma'}, {'icd_o_3_histology': '8693/3', 'histological_type': 'Paraganglioma'}, {'icd_o_3_histology': '8693/3', 'histological_type': 'Paraganglioma; Extra-adrenal Pheochromocytoma'}, {'icd_o_3_histology': '8700/3', 'histological_type': 'Paraganglioma'}, {'icd_o_3_histology': '9382/3', 'histological_type': 'Oligodendroglioma'}, {'icd_o_3_histology': '9450/3', 'histological_type': 'Oligodendroglioma'}, {'icd_o_3_histology': '9451/3', 'histological_type': 'Oligodendroglioma'}], 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json', 'var_functions.query_db:18': [{'icd_o_3_histology': '9400/3', 'histological_type': 'Astrocytoma'}, {'icd_o_3_histology': '9400/3', 'histological_type': 'Oligoastrocytoma'}, {'icd_o_3_histology': '9440/3', 'histological_type': 'Treated primary GBM'}, {'icd_o_3_histology': '9382/3', 'histological_type': 'Oligodendroglioma'}, {'icd_o_3_histology': '9440/3', 'histological_type': 'Glioblastoma Multiforme (GBM)'}, {'icd_o_3_histology': '9440/3', 'histological_type': 'Untreated primary (de novo) GBM'}, {'icd_o_3_histology': '9401/3', 'histological_type': 'Astrocytoma'}, {'icd_o_3_histology': '9382/3', 'histological_type': 'Oligoastrocytoma'}, {'icd_o_3_histology': '9382/3', 'histological_type': 'Astrocytoma'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:50': [{'Patient_description': 'Case 739CC9F1-71BE-4F81-A5D1-EDA673903E45, linked to barcode TCGA-RY-A83X, corresponds to a FEMALE patient diagnosed with Brain lower grade glioma, with vital status Alive.', 'histological_type': 'Oligodendroglioma'}, {'Patient_description': 'The individual with barcode TCGA-FG-A60K and UUID A85AEBDA-B182-41BA-815A-3FF055E22829 is a FEMALE case of Brain lower grade glioma, documented with vital status = Alive.', 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': 'Patient TCGA-DB-A4XH (UUID 5CCD86AB-2587-4F35-B96A-4F4320B10FB9) is a FEMALE diagnosed with Brain lower grade glioma. Current vital status: Alive.', 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': 'Case 1701F4AD-58C5-40D8-90C4-99E3ACAC0104, linked to barcode TCGA-DB-A4XE, corresponds to a FEMALE patient diagnosed with Brain lower grade glioma, with vital status Alive.', 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': 'The individual with barcode TCGA-DB-A4XC and UUID 33615113-791B-4286-A23A-AD3D1F8D4B09 is a MALE case of Brain lower grade glioma, documented with vital status = Alive.', 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': 'Patient TCGA-P5-A5F0 (MALE, UUID 7EB5D055-E1C8-4B93-9205-A49A6E79DFD4) is enrolled in the study of Brain lower grade glioma. Vital status: Alive.', 'histological_type': 'Oligodendroglioma'}, {'Patient_description': 'Patient TCGA-S9-A6U1 (UUID A5E10E2E-5157-487B-88DC-6C70AD5E244A) is a FEMALE diagnosed with Brain lower grade glioma. Current vital status: Alive.', 'histological_type': 'Astrocytoma'}, {'Patient_description': 'The individual with barcode TCGA-TM-A7C3 and UUID D13AC936-87A9-4164-BDAB-02CCF3908CFE is a FEMALE case of Brain lower grade glioma, documented with vital status = Dead.', 'histological_type': 'Astrocytoma'}, {'Patient_description': 'Case 8E44FB97-C649-4056-80AC-257CEF61D226, linked to barcode TCGA-S9-A7R2, corresponds to a MALE patient diagnosed with Brain lower grade glioma, with vital status Dead.', 'histological_type': 'Astrocytoma'}, {'Patient_description': 'Record 21BBE030-8DBB-47EB-A670-13EB57C12159 refers to patient TCGA-TM-A84R, a MALE diagnosed with Brain lower grade glioma. Vital status recorded as Alive.', 'histological_type': 'Oligodendroglioma'}], 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json'}

exec(code, env_args)
