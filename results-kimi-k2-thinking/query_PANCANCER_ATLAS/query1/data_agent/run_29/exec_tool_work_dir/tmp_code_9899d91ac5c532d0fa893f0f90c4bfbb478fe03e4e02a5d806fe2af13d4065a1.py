code = """import json
import re
import math

# Load LGG patient data
lgg_file = locals()['var_functions.query_db:42']
with open(lgg_file, 'r') as f:
    lgg_patients = json.load(f)

# Create mapping of ParticipantBarcode to histological type for LGG patients
lgg_histology_map = {}
histogram = {}

for patient in lgg_patients:
    # Extract barcode
    patient_desc = patient['Patient_description']
    barcode_match = re.search(r'(TCGA-[A-Z0-9]+-[A-Z0-9]+)', patient_desc)
    if not barcode_match:
        continue
    
    barcode = barcode_match.group(1)
    hist_type = patient['histological_type']
    
    # Skip bracketed histological types
    if hist_type and hist_type.startswith('[') and hist_type.endswith(']'):
        continue
        
    lgg_histology_map[barcode] = hist_type
    histogram[hist_type] = histogram.get(hist_type, 0) + 1

# Load IGF2 expression data
igf2_file = locals()['var_functions.query_db:50']
with open(igf2_file, 'r') as f:
    igf2_data = json.load(f)

# Filter IGF2 data for LGG patients and compute log10 values
histology_expression = {}
matched_patients = 0

for record in igf2_data:
    barcode = record['ParticipantBarcode']
    
    # Check if this is an LGG patient
    if barcode in lgg_histology_map:
        try:
            # Get normalized count and convert to float
            norm_count = float(record['normalized_count'])
            
            # Compute log10(normalized_count + 1)
            log10_expr = math.log10(norm_count + 1)
            
            # Get histological type
            hist_type = lgg_histology_map[barcode]
            
            # Add to list for this histology type
            if hist_type not in histology_expression:
                histology_expression[hist_type] = []
            histology_expression[hist_type].append(log10_expr)
            matched_patients += 1
            
        except (ValueError, TypeError):
            # Skip invalid expression values
            continue

# Calculate averages for each histology type
results = {}
for hist_type, expressions in sorted(histology_expression.items()):
    if expressions:
        avg_log10 = sum(expressions) / len(expressions)
        results[hist_type] = {
            'average_log10_expression': round(avg_log10, 6),
            'patient_count': len(expressions)
        }

summary = {
    'total_lgg_patients': len(lgg_histology_map),
    'matched_with_expression': matched_patients,
    'histology_counts': histogram,
    'results_by_histology': results
}

print('__RESULT__:')
print(json.dumps(summary, indent=2))"""

env_args = {'var_functions.query_db:0': [{'column_name': 'stopped_smoking_year', 'data_type': 'double precision'}, {'column_name': 'days_to_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'number_of_lymphnodes_positive_by_he', 'data_type': 'double precision'}, {'column_name': 'age_at_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'year_of_tobacco_smoking_onset', 'data_type': 'double precision'}, {'column_name': 'year_of_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'height', 'data_type': 'double precision'}, {'column_name': 'weight', 'data_type': 'double precision'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc', 'data_type': 'double precision'}, {'column_name': 'days_to_birth', 'data_type': 'double precision'}, {'column_name': 'total_pelv_lnr', 'data_type': 'double precision'}, {'column_name': 'total_aor_lnr', 'data_type': 'double precision'}, {'column_name': 'number_pack_years_smoked', 'data_type': 'double precision'}, {'column_name': 'prior_dx', 'data_type': 'text'}, {'column_name': 'ethnicity', 'data_type': 'text'}, {'column_name': 'informed_consent_verified', 'data_type': 'text'}, {'column_name': 'person_neoplasm_cancer_status', 'data_type': 'text'}, {'column_name': 'patient_id', 'data_type': 'text'}, {'column_name': 'histological_type', 'data_type': 'text'}, {'column_name': 'tissue_source_site', 'data_type': 'text'}, {'column_name': 'form_completion_date', 'data_type': 'text'}, {'column_name': 'pathologic_T', 'data_type': 'text'}, {'column_name': 'pathologic_M', 'data_type': 'text'}, {'column_name': 'clinical_M', 'data_type': 'text'}, {'column_name': 'pathologic_N', 'data_type': 'text'}, {'column_name': 'system_version', 'data_type': 'text'}, {'column_name': 'pathologic_stage', 'data_type': 'text'}, {'column_name': 'clinical_stage', 'data_type': 'text'}, {'column_name': 'clinical_T', 'data_type': 'text'}, {'column_name': 'clinical_N', 'data_type': 'text'}, {'column_name': 'extranodal_involvement', 'data_type': 'text'}, {'column_name': 'postoperative_rx_tx', 'data_type': 'text'}, {'column_name': 'primary_therapy_outcome_success', 'data_type': 'text'}, {'column_name': 'lymph_node_examined_count', 'data_type': 'text'}, {'column_name': 'primary_lymph_node_presentation_assessment', 'data_type': 'text'}, {'column_name': 'initial_pathologic_diagnosis_method', 'data_type': 'text'}, {'column_name': 'eastern_cancer_oncology_group', 'data_type': 'text'}, {'column_name': 'anatomic_neoplasm_subdivision', 'data_type': 'text'}, {'column_name': 'residual_tumor', 'data_type': 'text'}, {'column_name': 'histological_type_other', 'data_type': 'text'}, {'column_name': 'init_pathology_dx_method_other', 'data_type': 'text'}, {'column_name': 'karnofsky_performance_score', 'data_type': 'text'}, {'column_name': 'neoplasm_histologic_grade', 'data_type': 'text'}, {'column_name': 'tobacco_smoking_history', 'data_type': 'text'}, {'column_name': 'performance_status_scale_timing', 'data_type': 'text'}, {'column_name': 'laterality', 'data_type': 'text'}, {'column_name': 'targeted_molecular_therapy', 'data_type': 'text'}, {'column_name': 'anatomic_neoplasm_subdivision_other', 'data_type': 'text'}, {'column_name': 'patient_death_reason', 'data_type': 'text'}, {'column_name': 'tumor_tissue_site_other', 'data_type': 'text'}], 'var_functions.query_db:2': [{'column_name': 'tumor_tissue_site'}, {'column_name': 'wait_event_type'}, {'column_name': 'type'}, {'column_name': 'vartype'}, {'column_name': 'trftype'}, {'column_name': 'reltype'}, {'column_name': 'user_defined_type_schema'}, {'column_name': 'privilege_type'}, {'column_name': 'user_defined_type_name'}, {'column_name': 'privilege_type'}, {'column_name': 'data_type'}, {'column_name': 'parameter_types'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'user_defined_type_catalog'}, {'column_name': 'data_type'}, {'column_name': 'result_cast_type_udt_name'}, {'column_name': 'deptype'}, {'column_name': 'result_cast_interval_type'}, {'column_name': 'prslextype'}, {'column_name': 'user_defined_type_category'}, {'column_name': 'privilege_type'}, {'column_name': 'data_type'}, {'column_name': 'typbasetype'}, {'column_name': 'table_type'}, {'column_name': 'foreign_server_type'}, {'column_name': 'confdeltype'}, {'column_name': 'rngsubtype'}, {'column_name': 'data_type'}, {'column_name': 'privtype'}, {'column_name': 'type_udt_name'}, {'column_name': 'slot_type'}, {'column_name': 'data_type'}, {'column_name': 'ev_type'}, {'column_name': 'transform_type'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'type'}, {'column_name': 'object_type'}, {'column_name': 'contype'}, {'column_name': 'interval_type'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'data_type'}, {'column_name': 'deptype'}, {'column_name': 'privilege_type'}, {'column_name': 'object_type'}, {'column_name': 'user_defined_type_catalog'}, {'column_name': 'privilege_type'}, {'column_name': 'interval_type'}, {'column_name': 'constraint_type'}, {'column_name': 'user_defined_type_name'}, {'column_name': 'privilege_type'}, {'column_name': 'data_type'}, {'column_name': 'protrftypes'}, {'column_name': 'interval_type'}, {'column_name': 'histological_type_other'}, {'column_name': 'amtype'}, {'column_name': 'proargtypes'}, {'column_name': 'privilege_type'}, {'column_name': 'histological_type'}, {'column_name': 'srvtype'}, {'column_name': 'residual_tumor'}, {'column_name': 'defaclobjtype'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'backend_type'}, {'column_name': 'reloftype'}, {'column_name': 'amprocrighttype'}, {'column_name': 'routine_type'}, {'column_name': 'data_type'}, {'column_name': 'foreign_server_type'}, {'column_name': 'typtype'}, {'column_name': 'object_type'}, {'column_name': 'is_typed'}, {'column_name': 'objtype'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'interval_type'}, {'column_name': 'interval_type'}, {'column_name': 'aggtranstype'}, {'column_name': 'amproclefttype'}, {'column_name': 'object_type'}, {'column_name': 'maptokentype'}, {'column_name': 'result_types'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'result_cast_type_udt_catalog'}, {'column_name': 'typelem'}, {'column_name': 'collctype'}, {'column_name': 'proallargtypes'}, {'column_name': 'reference_type'}, {'column_name': 'tgtype'}, {'column_name': 'user_defined_type_schema'}, {'column_name': 'security_type'}, {'column_name': 'collection_type_identifier'}, {'column_name': 'data_type'}, {'column_name': 'result_cast_type_udt_schema'}, {'column_name': 'datctype'}, {'column_name': 'privilege_type'}, {'column_name': 'opcintype'}, {'column_name': 'result_cast_from_data_type'}, {'column_name': 'amoprighttype'}, {'column_name': 'opckeytype'}, {'column_name': 'type_udt_catalog'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'interval_type'}, {'column_name': 'worker_type'}, {'column_name': 'type_udt_schema'}, {'column_name': 'confmatchtype'}, {'column_name': 'privilege_type'}, {'column_name': 'privilege_type'}, {'column_name': 'prorettype'}, {'column_name': 'locktype'}, {'column_name': 'confupdtype'}, {'column_name': 'aggmtranstype'}, {'column_name': 'backend_type'}, {'column_name': 'amoplefttype'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'interval_type'}, {'column_name': 'type'}, {'column_name': 'oprcode'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [], 'var_functions.query_db:8': [{'column_name': 'typbasetype'}, {'column_name': 'confmatchtype'}, {'column_name': 'opcintype'}, {'column_name': 'opckeytype'}, {'column_name': 'amtype'}, {'column_name': 'amoplefttype'}, {'column_name': 'amoprighttype'}, {'column_name': 'amproclefttype'}, {'column_name': 'amprocrighttype'}, {'column_name': 'aggtranstype'}, {'column_name': 'aggmtranstype'}, {'column_name': 'ev_type'}, {'column_name': 'tgtype'}, {'column_name': 'deptype'}, {'column_name': 'proargtypes'}, {'column_name': 'deptype'}, {'column_name': 'maptokentype'}, {'column_name': 'prslextype'}, {'column_name': 'proallargtypes'}, {'column_name': 'defaclobjtype'}], 'var_functions.query_db:10': [{'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'histological_type'}, {'column_name': 'histological_type_other'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'residual_tumor'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'tumor_tissue_site_other'}], 'var_functions.query_db:12': [{'ParticipantBarcode': 'TCGA-06-0675', 'SampleBarcode': 'TCGA-06-0675-11A', 'AliquotBarcode': 'TCGA-06-0675-11A-32R-A36H-07', 'SampleTypeLetterCode': 'NT', 'SampleType': 'Solid Tissue Normal', 'Symbol': 'LXN', 'Entrez': '56925', 'normalized_count': '69.7259'}, {'ParticipantBarcode': 'TCGA-06-0675', 'SampleBarcode': 'TCGA-06-0675-11A', 'AliquotBarcode': 'TCGA-06-0675-11A-32R-A36H-07', 'SampleTypeLetterCode': 'NT', 'SampleType': 'Solid Tissue Normal', 'Symbol': 'ZNF770', 'Entrez': '54989', 'normalized_count': '1195.92'}, {'ParticipantBarcode': 'TCGA-06-0675', 'SampleBarcode': 'TCGA-06-0675-11A', 'AliquotBarcode': 'TCGA-06-0675-11A-32R-A36H-07', 'SampleTypeLetterCode': 'NT', 'SampleType': 'Solid Tissue Normal', 'Symbol': 'AMELY', 'Entrez': '266', 'normalized_count': '0.0'}], 'var_functions.query_db:14': [{'tumor_tissue_site': 'None'}, {'tumor_tissue_site': 'Choroid|Ciliary body'}, {'tumor_tissue_site': 'Upper Extremity - Upper arm/elbow'}, {'tumor_tissue_site': 'Head and Neck - Neck|Head and Neck - Other (please specify'}, {'tumor_tissue_site': 'Uterus'}, {'tumor_tissue_site': 'Thyroid'}, {'tumor_tissue_site': 'Choroid'}, {'tumor_tissue_site': 'Ovary'}, {'tumor_tissue_site': 'Upper Extremity - Shoulder/axilla'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Pelvic'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Bladder'}, {'tumor_tissue_site': 'Head and Neck - Head'}, {'tumor_tissue_site': 'Kidney'}, {'tumor_tissue_site': 'Pancreas'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Pelvic|Gynecological - Uterus'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum|Retroperitoneum/Upper abdominal - Intraabdominal|Lower abdominal/Pelvic - Pelvic'}, {'tumor_tissue_site': 'Extremities|Extremities'}, {'tumor_tissue_site': 'Pleura'}, {'tumor_tissue_site': 'Brain'}, {'tumor_tissue_site': 'Anterior Mediastinum'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': [{'icd_10': 'C74.9'}, {'icd_10': 'C38.0'}, {'icd_10': 'C71.1'}, {'icd_10': 'C75.5'}, {'icd_10': 'C49.3'}, {'icd_10': 'C76.0'}, {'icd_10': 'C48.0'}, {'icd_10': 'C74.1'}, {'icd_10': 'C71.0'}, {'icd_10': 'C71.9'}, {'icd_10': 'C74.0'}, {'icd_10': 'C49.5'}, {'icd_10': 'C71.2'}, {'icd_10': 'C49.6'}, {'icd_10': 'C71.3'}, {'icd_10': 'C38.3'}, {'icd_10': 'C49.4'}, {'icd_10': 'C71.4'}, {'icd_10': 'C72.9'}, {'icd_10': 'C76.1'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:26': [{'count': '513'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:36': {'total_patients': 513, 'valid_patients': 513, 'invalid_histology': 0, 'histology_counts': {'Astrocytoma': 194, 'Oligoastrocytoma': 130, 'Oligodendroglioma': 189}, 'unique_barcodes': 513}, 'var_functions.query_db:40': [{'count': '496'}], 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.execute_python:44': {'total_lgg_patients': 513, 'valid_patients': 513, 'barcodes_for_query': "'TCGA-RY-A83X','TCGA-FG-A60K','TCGA-DB-A4XH','TCGA-DB-A4XE','TCGA-DB-A4XC','TCGA-P5-A5F0','TCGA-S9-A6U1','TCGA-TM-A7C3','TCGA-S9-A7R2','TCGA-TM-A84R','TCGA-S9-A6TU','TCGA-HW-7490','TCGA-P5-A733','TCGA"}, 'var_functions.query_db:46': [{'ParticipantBarcode': 'TCGA-S9-A7J1', 'normalized_count': '407.007'}, {'ParticipantBarcode': 'TCGA-DH-A7US', 'normalized_count': '418.886'}], 'var_functions.execute_python:48': {'barcodes_count': 513, 'sample_barcodes': ['TCGA-RY-A83X', 'TCGA-FG-A60K', 'TCGA-DB-A4XH', 'TCGA-DB-A4XE', 'TCGA-DB-A4XC', 'TCGA-P5-A5F0', 'TCGA-S9-A6U1', 'TCGA-TM-A7C3', 'TCGA-S9-A7R2', 'TCGA-TM-A84R'], 'barcodes_file': '/tmp/lgg_barcodes.json'}, 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json'}

exec(code, env_args)
