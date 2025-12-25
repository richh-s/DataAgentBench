code = """import json
import pandas as pd
import re
import numpy as np

# Load clinical data
with open('var_function-call-4902066877342671258.json', 'r') as f:
    clinical_data = json.load(f)

# Load molecular data
with open('var_function-call-12604965360875268429.json', 'r') as f:
    molecular_data = json.load(f)

df_clinical = pd.DataFrame(clinical_data)
df_molecular = pd.DataFrame(molecular_data)

# Extract ParticipantBarcode from Patient_description
def extract_barcode(desc):
    if not isinstance(desc, str):
        return None
    match = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', desc)
    if match:
        return match.group(1)
    return None

df_clinical['ParticipantBarcode'] = df_clinical['Patient_description'].apply(extract_barcode)

# Filter clinical data
# 1. Must have valid ParticipantBarcode
df_clinical = df_clinical.dropna(subset=['ParticipantBarcode'])
# 2. Histology annotations not enclosed in square brackets
df_clinical = df_clinical[~df_clinical['histological_type'].astype(str).str.startswith('[')]
df_clinical = df_clinical[~df_clinical['histological_type'].astype(str).str.endswith(']')]
# Also exclude "None" or similar if considered invalid, but prompt specifically mentions square brackets.
# The previous list showed types like "Oligodendroglioma", "Astrocytoma", "Oligoastrocytoma". These are fine.

# Merge with molecular data
# Molecular data has 'ParticipantBarcode' and 'normalized_count'
# Ensure normalized_count is float
df_molecular['normalized_count'] = pd.to_numeric(df_molecular['normalized_count'], errors='coerce')
df_molecular = df_molecular.dropna(subset=['normalized_count'])

# Merge
merged_df = pd.merge(df_clinical, df_molecular, on='ParticipantBarcode', how='inner')

# Compute log10(normalized_count + 1)
merged_df['log_expression'] = np.log10(merged_df['normalized_count'] + 1)

# Group by histology and compute mean
result_df = merged_df.groupby('histological_type')['log_expression'].mean().reset_index()

# Format the result
result_dict = {}
for index, row in result_df.iterrows():
    result_dict[row['histological_type']] = round(row['log_expression'], 4)

print("__RESULT__:")
print(json.dumps(result_dict))"""

env_args = {'var_function-call-8286828986587696797': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_function-call-8286828986587693352': [{'ParticipantBarcode': 'TCGA-06-0675', 'SampleBarcode': 'TCGA-06-0675-11A', 'AliquotBarcode': 'TCGA-06-0675-11A-32R-A36H-07', 'SampleTypeLetterCode': 'NT', 'SampleType': 'Solid Tissue Normal', 'Symbol': 'LXN', 'Entrez': '56925', 'normalized_count': '69.7259'}], 'var_function-call-5684079126192316181': [{'diagnosis': 'Lung Adenocarcinoma', 'histological_type': 'Lung Mucinous Adenocarcinoma', 'tumor_tissue_site': 'Lung'}, {'diagnosis': 'None', 'histological_type': 'None', 'tumor_tissue_site': 'None'}, {'diagnosis': 'None', 'histological_type': 'Pheochromocytoma', 'tumor_tissue_site': 'Extra-adrenal Site'}, {'diagnosis': 'None', 'histological_type': 'Malignant Peripheral Nerve Sheath Tumors (MPNST)', 'tumor_tissue_site': 'Chest - Chest wall'}, {'diagnosis': 'None', 'histological_type': 'Malignant Peripheral Nerve Sheath Tumors (MPNST)', 'tumor_tissue_site': 'Superficial Trunk - Buttock'}, {'diagnosis': 'None', 'histological_type': 'Non-Seminoma; Embryonal Carcinoma|[Not Available]|[Not Available]|[Not Available]', 'tumor_tissue_site': 'Testes'}, {'diagnosis': 'None', 'histological_type': 'Infiltrating Ductal Carcinoma', 'tumor_tissue_site': 'Breast'}, {'diagnosis': 'None', 'histological_type': 'Non-Seminoma; Choriocarcinoma|Non-Seminoma; Embryonal Carcinoma|Non-Seminoma; Yolk Sac Tumor|Non-Seminoma; Teratoma (Mature)|Non-Seminoma; Teratoma (Immature)', 'tumor_tissue_site': 'Testes'}, {'diagnosis': 'Lung Squamous Cell Carcinoma', 'histological_type': 'Lung Squamous Cell Carcinoma- Not Otherwise Specified (NOS)', 'tumor_tissue_site': 'Lung'}, {'diagnosis': 'None', 'histological_type': "Pleomorphic 'MFH'/ Undifferentiated pleomorphic sarcoma", 'tumor_tissue_site': 'Lower Extremity - Thigh/knee'}, {'diagnosis': 'None', 'histological_type': 'None', 'tumor_tissue_site': 'Trunk|[Not Available]'}, {'diagnosis': 'None', 'histological_type': 'Seminoma; NOS|Non-Seminoma; Yolk Sac Tumor|Non-Seminoma; Teratoma (Mature)|Non-Seminoma; Teratoma (Immature)', 'tumor_tissue_site': 'Testes'}, {'diagnosis': 'None', 'histological_type': 'Synovial Sarcoma - Monophasic', 'tumor_tissue_site': 'Chest - Lung/pleura'}, {'diagnosis': 'Lung Adenocarcinoma', 'histological_type': 'Lung Bronchioloalveolar Carcinoma Mucinous', 'tumor_tissue_site': 'Lung'}, {'diagnosis': 'None', 'histological_type': 'Head and Neck Squamous Cell Carcinoma  Spindle Cell Variant', 'tumor_tissue_site': 'Head and Neck'}, {'diagnosis': 'None', 'histological_type': 'Leiomyosarcoma (LMS)', 'tumor_tissue_site': 'Gynecological - Uterus'}, {'diagnosis': 'None', 'histological_type': "Pleomorphic 'MFH'/ Undifferentiated pleomorphic sarcoma", 'tumor_tissue_site': 'Chest - Chest wall'}, {'diagnosis': 'None', 'histological_type': 'Dedifferentiated liposarcoma', 'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum|Retroperitoneum/Upper abdominal - Small Intestines|Retroperitoneum/Upper abdominal - Other (please specify'}, {'diagnosis': 'None', 'histological_type': 'Synovial Sarcoma - Monophasic', 'tumor_tissue_site': 'Lower Extremity - Thigh/knee'}, {'diagnosis': 'None', 'histological_type': 'Non-Seminoma; Teratoma (Immature)|Non-Seminoma; Yolk Sac Tumor|Non-Seminoma; Embryonal Carcinoma', 'tumor_tissue_site': 'Testes'}], 'var_function-call-10617133677857632899': [], 'var_function-call-6212545484384079706': [{'tumor_tissue_site': 'Brain'}], 'var_function-call-11327684411503799887': [{'diagnosis': 'None', 'histological_type': 'Glioblastoma Multiforme (GBM)'}, {'diagnosis': 'None', 'histological_type': 'Treated primary GBM'}, {'diagnosis': 'None', 'histological_type': 'Untreated primary (de novo) GBM'}], 'var_function-call-13249796655233824226': [{'histological_type': 'Oligodendroglioma'}, {'histological_type': 'Astrocytoma'}], 'var_function-call-7072095728685547681': [{'tumor_tissue_site': 'Central nervous system', 'diagnosis': 'None'}], 'var_function-call-9738939881731736404': [{'histological_type': 'Oligodendroglioma'}, {'histological_type': 'Astrocytoma'}, {'histological_type': 'Oligoastrocytoma'}], 'var_function-call-4902066877342671258': 'file_storage/function-call-4902066877342671258.json', 'var_function-call-12604965360875268429': 'file_storage/function-call-12604965360875268429.json'}

exec(code, env_args)
