code = """import json
import pandas as pd
import re
import math

# Load the clinical LGG results
data_clinical = None
if isinstance(var_call_4N8hYOlTod45LZIjiwJkTmEI, str):
    with open(var_call_4N8hYOlTod45LZIjiwJkTmEI, 'r') as f:
        data_clinical = json.load(f)
else:
    data_clinical = var_call_4N8hYOlTod45LZIjiwJkTmEI

# Load the IGF2 expression results
data_expr = None
if isinstance(var_call_Oai0ghYksscNWNCCjFsod7F9, str):
    with open(var_call_Oai0ghYksscNWNCCjFsod7F9, 'r') as f:
        data_expr = json.load(f)
else:
    data_expr = var_call_Oai0ghYksscNWNCCjFsod7F9

# Clinical dataframe
df_clin = pd.DataFrame(data_clinical)
# Keep only relevant columns
if 'Patient_description' not in df_clin.columns:
    raise ValueError('Patient_description not in clinical data')
if 'histological_type' not in df_clin.columns:
    df_clin['histological_type'] = None

# Extract ParticipantBarcode from Patient_description using regex
def extract_barcode(text):
    if not isinstance(text, str):
        return None
    m = re.search(r'(TCGA-[A-Za-z0-9-]+)', text)
    if m:
        return m.group(1)
    return None

df_clin['ParticipantBarcode'] = df_clin['Patient_description'].apply(extract_barcode)
# Drop rows without barcode
df_clin = df_clin.dropna(subset=['ParticipantBarcode'])
# Keep histology and barcode
df_clin = df_clin[['ParticipantBarcode', 'histological_type']].drop_duplicates()

# Expression dataframe
df_expr = pd.DataFrame(data_expr)
# Ensure columns exist
if 'ParticipantBarcode' not in df_expr.columns or 'normalized_count' not in df_expr.columns:
    raise ValueError('Expression data missing required columns')

# Convert normalized_count to float where possible, drop invalid
def to_float(x):
    try:
        return float(x)
    except Exception:
        return None

df_expr['normalized_count'] = df_expr['normalized_count'].apply(to_float)
# Drop rows with null normalized_count
df_expr = df_expr.dropna(subset=['normalized_count'])

# Compute log10(normalized_count + 1)
import numpy as np
# guard against negative counts
df_expr = df_expr[df_expr['normalized_count'] >= 0]

df_expr['log10_expr'] = np.log10(df_expr['normalized_count'] + 1)

# Aggregate expression per participant (mean across samples for a participant)
df_participant = df_expr.groupby('ParticipantBarcode', as_index=False)['log10_expr'].mean()

# Merge with clinical LGG patient histology
df_merged = pd.merge(df_clin, df_participant, on='ParticipantBarcode', how='inner')

# Filter out histological_type annotations enclosed in square brackets
def valid_hist(h):
    if not isinstance(h, str):
        return False
    # Exclude if contains [ or ] or starts/ends with brackets
    if '[' in h or ']' in h:
        return False
    # Also exclude empty
    if h.strip() == '':
        return False
    return True

df_merged = df_merged[df_merged['histological_type'].apply(valid_hist)]

# Group by histological_type and compute mean of participant-level mean log10
result = df_merged.groupby('histological_type', as_index=False)['log10_expr'].mean()

# Prepare output mapping with at least four decimal places
out = {}
for _, row in result.iterrows():
    hist = row['histological_type']
    val = row['log10_expr']
    # format to 4 decimal places
    out[hist] = "{:.4f}".format(float(val))

# Sort keys for consistent output
out_sorted = {k: out[k] for k in sorted(out.keys())}

print("__RESULT__:")
print(json.dumps(out_sorted))"""

env_args = {'var_call_KHRAv5jgza4kLlPgfPtWjl47': ['clinical_info'], 'var_call_GfFiajTBf0Aw0vphJEBDyDrH': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_CadNxHcQP6EoleQoD8AvpxmW': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_7flneP63feHTgbUesnVqUKj6': 'file_storage/call_7flneP63feHTgbUesnVqUKj6.json', 'var_call_4N8hYOlTod45LZIjiwJkTmEI': 'file_storage/call_4N8hYOlTod45LZIjiwJkTmEI.json', 'var_call_FbXvbEIytsGULKg4NuKWSppX': [{'ParticipantBarcode': 'TCGA-C5-A2M2'}, {'ParticipantBarcode': 'TCGA-AA-3693'}, {'ParticipantBarcode': 'TCGA-HT-7478'}, {'ParticipantBarcode': 'TCGA-75-7030'}, {'ParticipantBarcode': 'TCGA-P4-AAVM'}, {'ParticipantBarcode': 'TCGA-EM-A3AQ'}, {'ParticipantBarcode': 'TCGA-HC-A9TH'}, {'ParticipantBarcode': 'TCGA-CV-7433'}, {'ParticipantBarcode': 'TCGA-DX-A3U8'}, {'ParticipantBarcode': 'TCGA-FE-A235'}, {'ParticipantBarcode': 'TCGA-OR-A5LS'}, {'ParticipantBarcode': 'TCGA-AG-4021'}, {'ParticipantBarcode': 'TCGA-XU-A931'}, {'ParticipantBarcode': 'TCGA-21-1071'}, {'ParticipantBarcode': 'TCGA-30-1862'}, {'ParticipantBarcode': 'TCGA-66-2795'}, {'ParticipantBarcode': 'TCGA-PA-A5YG'}, {'ParticipantBarcode': 'TCGA-A2-A259'}, {'ParticipantBarcode': 'TCGA-FS-A1ZC'}, {'ParticipantBarcode': 'TCGA-BP-4326'}, {'ParticipantBarcode': 'TCGA-EE-A2M5'}, {'ParticipantBarcode': 'TCGA-IG-A51D'}, {'ParticipantBarcode': 'TCGA-AC-A2FO'}, {'ParticipantBarcode': 'TCGA-HC-A632'}, {'ParticipantBarcode': 'TCGA-AR-A0TP'}, {'ParticipantBarcode': 'TCGA-E9-A1N8'}, {'ParticipantBarcode': 'TCGA-CR-6472'}, {'ParticipantBarcode': 'TCGA-CV-5436'}, {'ParticipantBarcode': 'TCGA-55-8092'}, {'ParticipantBarcode': 'TCGA-34-7107'}, {'ParticipantBarcode': 'TCGA-BH-A0BP'}, {'ParticipantBarcode': 'TCGA-22-A5C4'}, {'ParticipantBarcode': 'TCGA-B5-A0K9'}, {'ParticipantBarcode': 'TCGA-AB-2949'}, {'ParticipantBarcode': 'TCGA-CQ-A4CH'}, {'ParticipantBarcode': 'TCGA-VS-A8EL'}, {'ParticipantBarcode': 'TCGA-D8-A1XQ'}, {'ParticipantBarcode': 'TCGA-D1-A17D'}, {'ParticipantBarcode': 'TCGA-2H-A9GK'}, {'ParticipantBarcode': 'TCGA-OL-A5RZ'}, {'ParticipantBarcode': 'TCGA-G3-A7M6'}, {'ParticipantBarcode': 'TCGA-H6-A45N'}, {'ParticipantBarcode': 'TCGA-FW-A3R5'}, {'ParticipantBarcode': 'TCGA-AB-2908'}, {'ParticipantBarcode': 'TCGA-K1-A6RV'}, {'ParticipantBarcode': 'TCGA-44-4112'}, {'ParticipantBarcode': 'TCGA-62-A46V'}, {'ParticipantBarcode': 'TCGA-CF-A47S'}, {'ParticipantBarcode': 'TCGA-E1-A7Z2'}, {'ParticipantBarcode': 'TCGA-21-1079'}, {'ParticipantBarcode': 'TCGA-46-3769'}, {'ParticipantBarcode': 'TCGA-A2-A0SW'}, {'ParticipantBarcode': 'TCGA-B6-A0IB'}, {'ParticipantBarcode': 'TCGA-91-7771'}, {'ParticipantBarcode': 'TCGA-VN-A88N'}, {'ParticipantBarcode': 'TCGA-CH-5788'}, {'ParticipantBarcode': 'TCGA-G7-7502'}, {'ParticipantBarcode': 'TCGA-B5-A11M'}, {'ParticipantBarcode': 'TCGA-CV-A45X'}, {'ParticipantBarcode': 'TCGA-CV-7183'}, {'ParticipantBarcode': 'TCGA-EO-A2CH'}, {'ParticipantBarcode': 'TCGA-22-1000'}, {'ParticipantBarcode': 'TCGA-AA-A01F'}, {'ParticipantBarcode': 'TCGA-NF-A4WU'}, {'ParticipantBarcode': 'TCGA-EJ-7791'}, {'ParticipantBarcode': 'TCGA-EJ-A65E'}, {'ParticipantBarcode': 'TCGA-DJ-A3UM'}, {'ParticipantBarcode': 'TCGA-WB-A816'}, {'ParticipantBarcode': 'TCGA-2G-AAGI'}, {'ParticipantBarcode': 'TCGA-24-1557'}, {'ParticipantBarcode': 'TCGA-OR-A5J5'}, {'ParticipantBarcode': 'TCGA-86-A4JF'}, {'ParticipantBarcode': 'TCGA-AJ-A23O'}, {'ParticipantBarcode': 'TCGA-97-7938'}, {'ParticipantBarcode': 'TCGA-CJ-4916'}, {'ParticipantBarcode': 'TCGA-CV-5442'}, {'ParticipantBarcode': 'TCGA-FF-8062'}, {'ParticipantBarcode': 'TCGA-AQ-A1H3'}, {'ParticipantBarcode': 'TCGA-CN-5364'}, {'ParticipantBarcode': 'TCGA-CV-6953'}, {'ParticipantBarcode': 'TCGA-DU-7007'}, {'ParticipantBarcode': 'TCGA-DU-A7TI'}, {'ParticipantBarcode': 'TCGA-D1-A2G7'}, {'ParticipantBarcode': 'TCGA-AB-2935'}, {'ParticipantBarcode': 'TCGA-HT-7860'}, {'ParticipantBarcode': 'TCGA-DB-A64V'}, {'ParticipantBarcode': 'TCGA-FW-A3TU'}, {'ParticipantBarcode': 'TCGA-3G-AB0Q'}, {'ParticipantBarcode': 'TCGA-G7-6790'}, {'ParticipantBarcode': 'TCGA-C5-A1BM'}, {'ParticipantBarcode': 'TCGA-EW-A1PB'}, {'ParticipantBarcode': 'TCGA-ZX-AA5X'}, {'ParticipantBarcode': 'TCGA-WC-A87T'}, {'ParticipantBarcode': 'TCGA-BT-A20N'}, {'ParticipantBarcode': 'TCGA-D7-6518'}, {'ParticipantBarcode': 'TCGA-DD-AAD5'}, {'ParticipantBarcode': 'TCGA-S7-A7X0'}, {'ParticipantBarcode': 'TCGA-V1-A9OH'}, {'ParticipantBarcode': 'TCGA-B0-4828'}, {'ParticipantBarcode': 'TCGA-DD-AAD1'}, {'ParticipantBarcode': 'TCGA-BR-6802'}, {'ParticipantBarcode': 'TCGA-GN-A26D'}, {'ParticipantBarcode': 'TCGA-AR-A1AV'}, {'ParticipantBarcode': 'TCGA-62-8394'}, {'ParticipantBarcode': 'TCGA-BP-4334'}, {'ParticipantBarcode': 'TCGA-G9-6361'}, {'ParticipantBarcode': 'TCGA-KL-8346'}, {'ParticipantBarcode': 'TCGA-S7-A7WR'}, {'ParticipantBarcode': 'TCGA-TM-A7CA'}, {'ParticipantBarcode': 'TCGA-WE-A8ZR'}, {'ParticipantBarcode': 'TCGA-55-A57B'}, {'ParticipantBarcode': 'TCGA-78-7535'}, {'ParticipantBarcode': 'TCGA-A2-A0EN'}, {'ParticipantBarcode': 'TCGA-JW-A5VG'}, {'ParticipantBarcode': 'TCGA-69-7764'}, {'ParticipantBarcode': 'TCGA-BH-A18L'}, {'ParticipantBarcode': 'TCGA-2J-AABU'}, {'ParticipantBarcode': 'TCGA-C8-A131'}, {'ParticipantBarcode': 'TCGA-A2-A0T5'}, {'ParticipantBarcode': 'TCGA-BH-A209'}, {'ParticipantBarcode': 'TCGA-D5-6534'}, {'ParticipantBarcode': 'TCGA-YT-A95G'}, {'ParticipantBarcode': 'TCGA-HF-7136'}, {'ParticipantBarcode': 'TCGA-LT-A8JT'}, {'ParticipantBarcode': 'TCGA-CS-6670'}, {'ParticipantBarcode': 'TCGA-E2-A15C'}, {'ParticipantBarcode': 'TCGA-CV-A45Y'}, {'ParticipantBarcode': 'TCGA-43-7657'}, {'ParticipantBarcode': 'TCGA-57-1993'}, {'ParticipantBarcode': 'TCGA-B6-A0RU'}, {'ParticipantBarcode': 'TCGA-RW-A680'}, {'ParticipantBarcode': 'TCGA-VD-A8KF'}, {'ParticipantBarcode': 'TCGA-CH-5761'}, {'ParticipantBarcode': 'TCGA-BH-A0E9'}, {'ParticipantBarcode': 'TCGA-DD-AACG'}, {'ParticipantBarcode': 'TCGA-B6-A402'}, {'ParticipantBarcode': 'TCGA-F6-A8O3'}, {'ParticipantBarcode': 'TCGA-ED-A7PX'}, {'ParticipantBarcode': 'TCGA-HU-A4GD'}, {'ParticipantBarcode': 'TCGA-C5-A1BJ'}, {'ParticipantBarcode': 'TCGA-66-2767'}, {'ParticipantBarcode': 'TCGA-E2-A3DX'}, {'ParticipantBarcode': 'TCGA-95-7043'}, {'ParticipantBarcode': 'TCGA-XQ-A8TA'}, {'ParticipantBarcode': 'TCGA-F7-A50J'}, {'ParticipantBarcode': 'TCGA-XU-AAY1'}, {'ParticipantBarcode': 'TCGA-78-7540'}, {'ParticipantBarcode': 'TCGA-55-8620'}, {'ParticipantBarcode': 'TCGA-94-8035'}, {'ParticipantBarcode': 'TCGA-G9-6351'}, {'ParticipantBarcode': 'TCGA-78-7633'}, {'ParticipantBarcode': 'TCGA-BA-A6DD'}, {'ParticipantBarcode': 'TCGA-DI-A1BU'}, {'ParticipantBarcode': 'TCGA-DJ-A1QQ'}, {'ParticipantBarcode': 'TCGA-C5-A2LS'}, {'ParticipantBarcode': 'TCGA-EA-A1QT'}, {'ParticipantBarcode': 'TCGA-DK-AA6T'}, {'ParticipantBarcode': 'TCGA-A2-A3KD'}, {'ParticipantBarcode': 'TCGA-X7-A8M0'}, {'ParticipantBarcode': 'TCGA-S9-A7J1'}, {'ParticipantBarcode': 'TCGA-V4-A9EU'}, {'ParticipantBarcode': 'TCGA-MQ-A6BR'}, {'ParticipantBarcode': 'TCGA-EJ-7315'}, {'ParticipantBarcode': 'TCGA-EL-A3ZR'}, {'ParticipantBarcode': 'TCGA-BJ-A2N9'}, {'ParticipantBarcode': 'TCGA-AF-6136'}, {'ParticipantBarcode': 'TCGA-WB-A81H'}, {'ParticipantBarcode': 'TCGA-C5-A7UC'}, {'ParticipantBarcode': 'TCGA-D3-A5GO'}, {'ParticipantBarcode': 'TCGA-58-8386'}, {'ParticipantBarcode': 'TCGA-A7-A6VW'}, {'ParticipantBarcode': 'TCGA-G9-A9S0'}, {'ParticipantBarcode': 'TCGA-25-1632'}, {'ParticipantBarcode': 'TCGA-06-2561'}, {'ParticipantBarcode': 'TCGA-YL-A9WH'}, {'ParticipantBarcode': 'TCGA-VS-A9V4'}, {'ParticipantBarcode': 'TCGA-OR-A5J6'}, {'ParticipantBarcode': 'TCGA-EY-A5W2'}, {'ParticipantBarcode': 'TCGA-C5-A8YQ'}, {'ParticipantBarcode': 'TCGA-E8-A419'}, {'ParticipantBarcode': 'TCGA-A8-A082'}, {'ParticipantBarcode': 'TCGA-BH-A1EX'}, {'ParticipantBarcode': 'TCGA-TT-A6YP'}, {'ParticipantBarcode': 'TCGA-06-0190'}, {'ParticipantBarcode': 'TCGA-14-0787'}, {'ParticipantBarcode': 'TCGA-PL-A8LY'}, {'ParticipantBarcode': 'TCGA-EM-A1CW'}, {'ParticipantBarcode': 'TCGA-24-2023'}, {'ParticipantBarcode': 'TCGA-68-8251'}, {'ParticipantBarcode': 'TCGA-CM-6679'}, {'ParticipantBarcode': 'TCGA-D5-6926'}, {'ParticipantBarcode': 'TCGA-ZF-AA4X'}, {'ParticipantBarcode': 'TCGA-HM-A6W2'}, {'ParticipantBarcode': 'TCGA-VV-A829'}, {'ParticipantBarcode': 'TCGA-ZP-A9D1'}, {'ParticipantBarcode': 'TCGA-DB-A4XD'}, {'ParticipantBarcode': 'TCGA-CV-6945'}, {'ParticipantBarcode': 'TCGA-KL-8331'}, {'ParticipantBarcode': 'TCGA-L5-A43I'}, {'ParticipantBarcode': 'TCGA-A6-5665'}], 'var_call_Oai0ghYksscNWNCCjFsod7F9': 'file_storage/call_Oai0ghYksscNWNCCjFsod7F9.json'}

exec(code, env_args)
