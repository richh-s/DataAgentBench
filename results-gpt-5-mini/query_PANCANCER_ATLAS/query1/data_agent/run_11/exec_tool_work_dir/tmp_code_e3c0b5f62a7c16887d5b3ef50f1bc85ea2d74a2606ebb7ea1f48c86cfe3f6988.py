code = """import pandas as pd, json
# load the large RNASeq result from storage
rl = var_call_eah2hfNVrGnm6jJkQMSQ7yuk
# it's a file path string? The developer message said large results stored as file paths; check type
if isinstance(rl, str) and rl.endswith('.json'):
    df_rna = pd.read_json(rl)
else:
    df_rna = pd.DataFrame(rl)

# load clinical LGG patients list
clin = var_call_kP764x7N3XCxxQcpNAFLlIka
if isinstance(clin, str) and clin.endswith('.json'):
    df_clin = pd.read_json(clin)
else:
    df_clin = pd.DataFrame(clin)

# Extract patient barcodes from Patient_description: look for TCGA-??-XXXX pattern
import re

def extract_barcode(s):
    if not isinstance(s, str):
        return None
    m = re.search(r"TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}", s)
    return m.group(0) if m else None

df_clin['barcode'] = df_clin['Patient_description'].apply(extract_barcode)
# ParticipantBarcode in RNASeq seems like full TCGA-XX-YYYY or sometimes with extra segments like TCGA-AB-2908 or TCGA-AB-2908? Keep first three fields
# Normalize both to first three parts

def shorten(b):
    if not isinstance(b, str):
        return None
    parts = b.split('-')
    if len(parts) >= 3:
        return '-'.join(parts[:3])
    return b

# normalize
df_clin['pb'] = df_clin['barcode'].apply(shorten)

df_rna['pb'] = df_rna['ParticipantBarcode'].apply(shorten)

# join on pb
merged = pd.merge(df_rna, df_clin[['pb','histological_type']], on='pb', how='inner')
# filter histological_type not null and not enclosed in []
merged = merged[merged['histological_type'].notna()]
merged = merged[~merged['histological_type'].str.match(r"^\[.*\]$")]

# ensure normalized_count valid numeric and positive
merged['normalized_count'] = pd.to_numeric(merged['normalized_count'], errors='coerce')
merged = merged[merged['normalized_count'].notna()]

# compute log10(normalized_count+1)
import numpy as np
merged['log10_expr'] = np.log10(merged['normalized_count'] + 1)

# group by histological_type and compute mean
res = merged.groupby('histological_type')['log10_expr'].mean().reset_index()
# format with at least 4 decimals
res['mean'] = res['log10_expr'].apply(lambda x: float(f"{x:.4f}"))
out = dict(zip(res['histological_type'], res['mean']))

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_v7oqd6cWkwe0I7CqFPDs1Ubj': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_4oY9qw7gEu1hZ4p15NQV9K5w': [], 'var_call_YOo2oOnJ3xeZYq3gQ7ZFg1di': [{'diagnosis': 'Lung Squamous Cell Carcinoma'}, {'diagnosis': 'Lung Adenocarcinoma'}], 'var_call_kP764x7N3XCxxQcpNAFLlIka': 'file_storage/call_kP764x7N3XCxxQcpNAFLlIka.json', 'var_call_FMrAiHgIqz6jIrWhXZnGv2vj': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_LAIJgPz754wZuM88UQh34KkU': [{'Symbol': 'IGF2', 'cnt': '496'}], 'var_call_eah2hfNVrGnm6jJkQMSQ7yuk': 'file_storage/call_eah2hfNVrGnm6jJkQMSQ7yuk.json'}

exec(code, env_args)
