code = """import json
import re
import math
from collections import defaultdict

# Read the clinical data using the correct locals() syntax
clinical_key = 'var_functions.query_db:44'
clinical_data = locals()[clinical_key]
print(f"Clinical data type: {type(clinical_data)}")

if isinstance(clinical_data, str) and clinical_data.endswith('.json'):
    with open(clinical_data, 'r') as f:
        clinical_data = json.load(f)

print(f"Total clinical records: {len(clinical_data)}")

# Extract LGG patients with valid histology (not in square brackets)
lgg_patients = {}
for record in clinical_data:
    hist_type = record.get('histological_type', '') or ''
    patient_desc = record.get('Patient_description', '') or ''
    
    # Check if it's LGG
    is_lgg = False
    if str(hist_type) and 'Brain lower grade glioma' not in str(hist_type):
        # Check specific LGG histology types
        lgg_types = ['oligodendroglioma', 'astrocytoma', 'oligoastrocytoma', 'mixed glioma']
        hist_lower = str(hist_type).lower()
        is_lgg = any(lgg_type in hist_lower for lgg_type in lgg_types)
    elif 'Brain lower grade glioma' in str(patient_desc):
        is_lgg = True
    
    if is_lgg:
        # Extract barcode from Patient_description
        barcode_match = re.search(r'TCGA-[A-Z0-9]+-[A-Z0-9]+', str(patient_desc))
        if barcode_match:
            barcode = barcode_match.group(0)
            hist_clean = str(hist_type).strip()
            
            # Check histology is not in square brackets
            has_brackets = '[' in hist_clean and ']' in hist_clean
            if hist_clean and not has_brackets:
                lgg_patients[barcode] = hist_clean

print(f"Found {len(lgg_patients)} LGG patients with valid histology")

# Get IGF2 data
igf2_key = 'var_functions.query_db:34'
igf2_data = locals()[igf2_key]
print(f"IGF2 data type: {type(igf2_data)}")

if isinstance(igf2_data, str) and igf2_data.endswith('.json'):
    with open(igf2_data, 'r') as f:
        igf2_data = json.load(f)

print(f"Total IGF2 records: {len(igf2_data)}")

# Filter IGF2 data for LGG patients only
lgg_igf2_data = []
for record in igf2_data:
    barcode = record.get('ParticipantBarcode')
    if barcode in lgg_patients:
        lgg_igf2_data.append({
            'barcode': barcode,
            'histology': lgg_patients[barcode],
            'normalized_count': float(record.get('normalized_count', 0))
        })

print(f"Found {len(lgg_igf2_data)} IGF2 records for LGG patients")

# Group by histology and calculate average log10 expression
histology_groups = defaultdict(list)
for record in lgg_igf2_data:
    histology = record['histology']
    norm_count = record['normalized_count']
    # Calculate log10(normalized_count + 1)
    if norm_count >= 0:
        log10_expr = math.log10(norm_count + 1)
        histology_groups[histology].append(log10_expr)

# Calculate averages
averages = {}
for histology, values in histology_groups.items():
    if values:
        avg = sum(values) / len(values)
        averages[histology] = {
            'average_log10_expression': round(avg, 4),
            'sample_count': len(values)
        }

# Sort by histology name
sorted_averages = dict(sorted(averages.items()))

result = {
    'averages_by_histology': sorted_averages,
    'total_patients': len(lgg_igf2_data),
    'total_histology_types': len(averages)
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}], 'var_functions.query_db:6': [{'column_name': 'Patient_description'}, {'column_name': 'days_to_birth'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'stopped_smoking_year'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'prior_glioma'}], 'var_functions.query_db:10': [], 'var_functions.query_db:12': [{'diagnosis': 'Lung Adenocarcinoma'}, {'diagnosis': 'Lung Squamous Cell Carcinoma'}], 'var_functions.list_db:14': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:16': [{'Symbol': 'CXorf66'}, {'Symbol': 'CHST9'}, {'Symbol': 'CERK'}, {'Symbol': 'CD38'}, {'Symbol': 'SNORD116-12'}, {'Symbol': 'NGF'}, {'Symbol': 'GPN1'}, {'Symbol': 'LOC284900'}, {'Symbol': 'SEMA4C'}, {'Symbol': 'SPAM1'}, {'Symbol': 'CARHSP1'}, {'Symbol': 'MTVR2'}, {'Symbol': 'C16orf73'}, {'Symbol': 'CRLF1'}, {'Symbol': 'PDPN'}, {'Symbol': 'C14orf23'}, {'Symbol': 'PINX1'}, {'Symbol': 'AGBL5'}, {'Symbol': 'FAM120AOS'}, {'Symbol': 'LOC284578'}], 'var_functions.query_db:18': [{'diagnosis': 'Lung Adenocarcinoma'}, {'diagnosis': 'Lung Squamous Cell Carcinoma'}], 'var_functions.query_db:20': [{'ParticipantBarcode': 'TCGA-AB-2908'}, {'ParticipantBarcode': 'TCGA-D8-A1XQ'}, {'ParticipantBarcode': 'TCGA-VS-A8EL'}, {'ParticipantBarcode': 'TCGA-NF-A4WU'}, {'ParticipantBarcode': 'TCGA-E1-A7Z2'}, {'ParticipantBarcode': 'TCGA-21-1079'}, {'ParticipantBarcode': 'TCGA-46-3769'}, {'ParticipantBarcode': 'TCGA-D1-A17D'}, {'ParticipantBarcode': 'TCGA-2H-A9GK'}, {'ParticipantBarcode': 'TCGA-B5-A11M'}, {'ParticipantBarcode': 'TCGA-CV-A45X'}, {'ParticipantBarcode': 'TCGA-CQ-A4CH'}, {'ParticipantBarcode': 'TCGA-62-A46V'}, {'ParticipantBarcode': 'TCGA-OL-A5RZ'}, {'ParticipantBarcode': 'TCGA-K1-A6RV'}, {'ParticipantBarcode': 'TCGA-B5-A0K9'}, {'ParticipantBarcode': 'TCGA-G3-A7M6'}, {'ParticipantBarcode': 'TCGA-H6-A45N'}, {'ParticipantBarcode': 'TCGA-AA-A01F'}, {'ParticipantBarcode': 'TCGA-CH-5788'}], 'var_functions.query_db:22': [{'total_patients': '10761'}], 'var_functions.query_db:24': [{'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'histological_type'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'histological_type_other'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'prior_glioma'}], 'var_functions.query_db:30': [{'Symbol': 'IGF2', 'count': '496'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
