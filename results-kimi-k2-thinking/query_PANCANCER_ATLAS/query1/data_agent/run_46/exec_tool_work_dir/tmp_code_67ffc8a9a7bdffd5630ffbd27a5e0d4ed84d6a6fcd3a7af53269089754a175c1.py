code = """import json
import re
import math
from collections import defaultdict

# The variables from previous queries are stored in locals()
# Let's access them directly
clinical_var_name = 'var_functions.query_db:18'
expression_var_name = 'var_functions.query_db:8'

# Get the raw data from the variables
clinical_raw = locals()[clinical_var_name]
expression_raw = locals()[expression_var_name]

# The data might be stored as JSON strings or as file paths
# Let's try to parse them as JSON first
try:
    clinical_data = json.loads(clinical_raw) if isinstance(clinical_raw, str) else clinical_raw
except:
    # If it's a file path, load from file
    with open(clinical_raw, 'r') as f:
        clinical_data = json.load(f)

try:
    expression_data = json.loads(expression_raw) if isinstance(expression_raw, str) else expression_raw
except:
    # If it's a file path, load from file
    with open(expression_raw, 'r') as f:
        expression_data = json.load(f)

print("Successfully loaded data")
print(f"Clinical records: {len(clinical_data)}")
print(f"Expression records: {len(expression_data)}")

# Process clinical data to extract barcodes and histology
lgg_patients = []
barcode_pattern = re.compile(r'(TCGA-[A-Z0-9-]+)')

for record in clinical_data:
    desc = record['Patient_description']
    hist_type = record['histological_type']
    
    # Find all TCGA barcodes
    matches = barcode_pattern.findall(desc)
    if matches:
        # Use the first match as the primary barcode
        barcode = matches[0]
        lgg_patients.append({
            'barcode': barcode,
            'histology': hist_type
        })

print(f"Found {len(lgg_patients)} LGG patients with barcodes")

# Build expression dictionary
expression_dict = {}
for record in expression_data:
    barcode = record['ParticipantBarcode']
    norm_count = float(record['normalized_count'])
    expression_dict[barcode] = norm_count

print(f"Expression values for {len(expression_dict)} patients")

# Join the data and compute log10 averages
histology_values = defaultdict(list)
matched_count = 0

for patient in lgg_patients:
    barcode = patient['barcode']
    histology = patient['histology']
    
    if barcode in expression_dict:
        norm_count = expression_dict[barcode]
        log_val = math.log10(norm_count + 1)  # Add 1 to avoid log10(0)
        histology_values[histology].append(log_val)
        matched_count += 1

print(f"Matched {matched_count} patients with both clinical and expression data")
print(f"Histology types found: {list(histology_values.keys())}")

# Calculate averages for each histology type
results = {}
for histology, values in histology_values.items():
    avg_val = sum(values) / len(values)
    results[histology] = avg_val

# Sort by histology name and format output
output_lines = []
for histology in sorted(results.keys()):
    avg = results[histology]
    output_lines.append(f"{histology}: {avg:.4f}")

final_output = "; ".join(output_lines)
print("__RESULT__:")
print(final_output)"""

env_args = {'var_functions.query_db:0': [{'column_name': 'Patient_description'}, {'column_name': 'days_to_birth'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'stopped_smoking_year'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'prior_glioma'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'name': 'Mutation_Data'}, {'name': 'RNASeq_Expression'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:16': ['var_functions.query_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', 'var_functions.query_db:6', 'var_functions.query_db:8'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
