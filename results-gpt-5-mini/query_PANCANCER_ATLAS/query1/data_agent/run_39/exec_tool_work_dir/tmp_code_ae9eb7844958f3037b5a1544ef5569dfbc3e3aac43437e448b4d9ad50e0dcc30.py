code = """import json
import re
import math
import pandas as pd

# Load clinical LGG query results
data_clinical = var_call_Q8wIuWmzclUAppCKsx6xjvd7
if isinstance(data_clinical, str):
    # it's a file path
    with open(data_clinical, 'r') as f:
        data_clinical = json.load(f)

# Load molecular IGF2 results
data_mol = var_call_Mvku8q1R5IyKkOT2L3frnAr8
if isinstance(data_mol, str):
    with open(data_mol, 'r') as f:
        data_mol = json.load(f)

# Create DataFrames
df_clin = pd.DataFrame(data_clinical)
# Normalize column names
if 'histological_type' not in df_clin.columns and 'histological type' in df_clin.columns:
    df_clin = df_clin.rename(columns={'histological type':'histological_type'})

# Extract ParticipantBarcode from Patient_description using regex
pattern = re.compile(r'(TCGA-[A-Za-z0-9]+-[A-Za-z0-9]+)', flags=re.IGNORECASE)

def extract_barcode(text):
    if not isinstance(text, str):
        return None
    m = pattern.search(text)
    if m:
        return m.group(1).upper()
    return None

if 'Patient_description' in df_clin.columns:
    df_clin['ParticipantBarcode'] = df_clin['Patient_description'].apply(extract_barcode)
else:
    df_clin['ParticipantBarcode'] = None

# Filter out rows without ParticipantBarcode or without histological_type
df_clin = df_clin[df_clin['ParticipantBarcode'].notnull()]

# Exclude histological_type values enclosed in square brackets entirely (e.g., '[Not Available]')
def is_bracket_enclosed(x):
    if not isinstance(x, str):
        return True
    x_strip = x.strip()
    return bool(re.match(r'^\[.*\]$', x_strip))

# Keep rows where histological_type exists and is not bracket enclosed
df_clin = df_clin[df_clin['histological_type'].notnull()]
mask = df_clin['histological_type'].apply(lambda x: not is_bracket_enclosed(x))
df_clin = df_clin[mask]

# Load molecular data
df_mol = pd.DataFrame(data_mol)
# Ensure ParticipantBarcode column exists
if 'ParticipantBarcode' not in df_mol.columns and 'ParticipantBarcode'.lower() in [c.lower() for c in df_mol.columns]:
    # try case-insensitive match
    for c in df_mol.columns:
        if c.lower() == 'participantbarcode':
            df_mol = df_mol.rename(columns={c: 'ParticipantBarcode'})
            break

# Convert normalized_count to float and filter valid
def to_float(x):
    try:
        return float(x)
    except Exception:
        return None

if 'normalized_count' in df_mol.columns:
    df_mol['normalized_count'] = df_mol['normalized_count'].apply(to_float)
else:
    df_mol['normalized_count'] = None

# Uppercase participant barcodes
if 'ParticipantBarcode' in df_mol.columns:
    df_mol['ParticipantBarcode'] = df_mol['ParticipantBarcode'].astype(str).str.upper()

# Merge clinical LGG patients with IGF2 expression by ParticipantBarcode
# Note: there may be multiple samples per participant in RNASeq; we will keep all samples (per-sample average across samples for histology)
merged = pd.merge(df_clin[['ParticipantBarcode', 'histological_type']], df_mol[['ParticipantBarcode', 'normalized_count']], on='ParticipantBarcode', how='inner')

# Keep only rows with valid normalized_count (not null and >=0)
merged = merged[merged['normalized_count'].notnull()]
merged = merged[merged['normalized_count'] >= 0]

# Compute log10(normalized_count + 1)
merged['log10_expr'] = merged['normalized_count'].apply(lambda x: math.log10(x + 1.0))

# Group by histological_type and compute mean
grouped = merged.groupby('histological_type', dropna=True)['log10_expr'].mean().reset_index()

# Format results with at least four decimal places
result_list = []
for _, row in grouped.iterrows():
    hist = row['histological_type']
    val = row['log10_expr']
    # Ensure at least four decimal places
    formatted = float(f"{val:.4f}")
    result_list.append({"histological_type": hist, "avg_log10_IGF2": formatted})

# Sort results by histological_type for consistency
result_list = sorted(result_list, key=lambda x: x['histological_type'])

# Output as JSON string
out = json.dumps(result_list)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_XfpRiWAy6Yrnenn4Vy0sJwTX': ['clinical_info'], 'var_call_mD2Hx8Odbkr14FaABwstnGeW': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_1LbuXT5aM4VLUm2joKKhkmAU': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_tF4QbN72so3ixF7A61u8Lqa1': 'file_storage/call_tF4QbN72so3ixF7A61u8Lqa1.json', 'var_call_Q8wIuWmzclUAppCKsx6xjvd7': 'file_storage/call_Q8wIuWmzclUAppCKsx6xjvd7.json', 'var_call_4Kl0VRenZVKM0VvwBn5vaWbo': [{'cid': '0', 'name': 'ParticipantBarcode', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '1', 'name': 'SampleBarcode', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '2', 'name': 'AliquotBarcode', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '3', 'name': 'SampleTypeLetterCode', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '4', 'name': 'SampleType', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '5', 'name': 'Symbol', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '6', 'name': 'Entrez', 'type': 'BIGINT', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '7', 'name': 'normalized_count', 'type': 'DOUBLE', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}], 'var_call_Mvku8q1R5IyKkOT2L3frnAr8': [{'ParticipantBarcode': 'TCGA-AB-2908', 'SampleBarcode': 'TCGA-AB-2908-03A', 'Symbol': 'IGF2', 'normalized_count': '167.272646747735'}, {'ParticipantBarcode': 'TCGA-19-5960', 'SampleBarcode': 'TCGA-19-5960-01A', 'Symbol': 'IGF2', 'normalized_count': '185.236'}, {'ParticipantBarcode': 'TCGA-21-1071', 'SampleBarcode': 'TCGA-21-1071-01A', 'Symbol': 'IGF2', 'normalized_count': '80.6827'}, {'ParticipantBarcode': 'TCGA-30-1862', 'SampleBarcode': 'TCGA-30-1862-01A', 'Symbol': 'IGF2', 'normalized_count': '13105.3695494317'}, {'ParticipantBarcode': 'TCGA-66-2795', 'SampleBarcode': 'TCGA-66-2795-01A', 'Symbol': 'IGF2', 'normalized_count': '613.474'}, {'ParticipantBarcode': 'TCGA-A8-A082', 'SampleBarcode': 'TCGA-A8-A082-01A', 'Symbol': 'IGF2', 'normalized_count': '630.54'}, {'ParticipantBarcode': 'TCGA-B5-A3FA', 'SampleBarcode': 'TCGA-B5-A3FA-01A', 'Symbol': 'IGF2', 'normalized_count': '423.628'}, {'ParticipantBarcode': 'TCGA-BH-A1EX', 'SampleBarcode': 'TCGA-BH-A1EX-01A', 'Symbol': 'IGF2', 'normalized_count': '1151.13'}, {'ParticipantBarcode': 'TCGA-BT-A20O', 'SampleBarcode': 'TCGA-BT-A20O-01A', 'Symbol': 'IGF2', 'normalized_count': '369.106'}, {'ParticipantBarcode': 'TCGA-CD-5799', 'SampleBarcode': 'TCGA-CD-5799-01A', 'Symbol': 'IGF2', 'normalized_count': '3936.02070028943'}, {'ParticipantBarcode': 'TCGA-CF-A8HY', 'SampleBarcode': 'TCGA-CF-A8HY-01A', 'Symbol': 'IGF2', 'normalized_count': '10085.9'}, {'ParticipantBarcode': 'TCGA-D8-A1XQ', 'SampleBarcode': 'TCGA-D8-A1XQ-01A', 'Symbol': 'IGF2', 'normalized_count': '177.388'}, {'ParticipantBarcode': 'TCGA-EM-A3AQ', 'SampleBarcode': 'TCGA-EM-A3AQ-01A', 'Symbol': 'IGF2', 'normalized_count': '651.559'}, {'ParticipantBarcode': 'TCGA-ET-A39M', 'SampleBarcode': 'TCGA-ET-A39M-01A', 'Symbol': 'IGF2', 'normalized_count': '440.072'}, {'ParticipantBarcode': 'TCGA-EY-A1GH', 'SampleBarcode': 'TCGA-EY-A1GH-01A', 'Symbol': 'IGF2', 'normalized_count': '937.086888477115'}, {'ParticipantBarcode': 'TCGA-FG-A713', 'SampleBarcode': 'TCGA-FG-A713-01A', 'Symbol': 'IGF2', 'normalized_count': '617.408'}, {'ParticipantBarcode': 'TCGA-IB-8126', 'SampleBarcode': 'TCGA-IB-8126-01A', 'Symbol': 'IGF2', 'normalized_count': '1993.98'}, {'ParticipantBarcode': 'TCGA-K1-A6RV', 'SampleBarcode': 'TCGA-K1-A6RV-01A', 'Symbol': 'IGF2', 'normalized_count': '154.408'}, {'ParticipantBarcode': 'TCGA-L5-A8NK', 'SampleBarcode': 'TCGA-L5-A8NK-01A', 'Symbol': 'IGF2', 'normalized_count': '257.032354514832'}, {'ParticipantBarcode': 'TCGA-OR-A5J5', 'SampleBarcode': 'TCGA-OR-A5J5-01A', 'Symbol': 'IGF2', 'normalized_count': '261089.0'}, {'ParticipantBarcode': 'TCGA-PA-A5YG', 'SampleBarcode': 'TCGA-PA-A5YG-01A', 'Symbol': 'IGF2', 'normalized_count': '92165.1999999999'}, {'ParticipantBarcode': 'TCGA-PL-A8LY', 'SampleBarcode': 'TCGA-PL-A8LY-01A', 'Symbol': 'IGF2', 'normalized_count': '616.245'}, {'ParticipantBarcode': 'TCGA-WW-A8ZI', 'SampleBarcode': 'TCGA-WW-A8ZI-01A', 'Symbol': 'IGF2', 'normalized_count': '508.63'}, {'ParticipantBarcode': 'TCGA-XU-AAY1', 'SampleBarcode': 'TCGA-XU-AAY1-01A', 'Symbol': 'IGF2', 'normalized_count': '799.319'}, {'ParticipantBarcode': 'TCGA-EM-A1CW', 'SampleBarcode': 'TCGA-EM-A1CW-01A', 'Symbol': 'IGF2', 'normalized_count': '136.844'}, {'ParticipantBarcode': 'TCGA-G9-A9S0', 'SampleBarcode': 'TCGA-G9-A9S0-01A', 'Symbol': 'IGF2', 'normalized_count': '102.295'}, {'ParticipantBarcode': 'TCGA-NF-A4WU', 'SampleBarcode': 'TCGA-NF-A4WU-01A', 'Symbol': 'IGF2', 'normalized_count': '212060.0'}, {'ParticipantBarcode': 'TCGA-OR-A5LE', 'SampleBarcode': 'TCGA-OR-A5LE-01A', 'Symbol': 'IGF2', 'normalized_count': '613480.0'}, {'ParticipantBarcode': 'TCGA-P4-A5E7', 'SampleBarcode': 'TCGA-P4-A5E7-01A', 'Symbol': 'IGF2', 'normalized_count': '39.0971'}, {'ParticipantBarcode': 'TCGA-QS-A8F1', 'SampleBarcode': 'TCGA-QS-A8F1-01A', 'Symbol': 'IGF2', 'normalized_count': '41121.4'}, {'ParticipantBarcode': 'TCGA-RW-A680', 'SampleBarcode': 'TCGA-RW-A680-01A', 'Symbol': 'IGF2', 'normalized_count': '232663.0'}, {'ParticipantBarcode': 'TCGA-UD-AAC7', 'SampleBarcode': 'TCGA-UD-AAC7-01A', 'Symbol': 'IGF2', 'normalized_count': '686.399'}, {'ParticipantBarcode': 'TCGA-VD-A8KF', 'SampleBarcode': 'TCGA-VD-A8KF-01A', 'Symbol': 'IGF2', 'normalized_count': '72.6016'}, {'ParticipantBarcode': 'TCGA-WB-A81H', 'SampleBarcode': 'TCGA-WB-A81H-01A', 'Symbol': 'IGF2', 'normalized_count': '74708.5'}, {'ParticipantBarcode': 'TCGA-G9-6351', 'SampleBarcode': 'TCGA-G9-6351-11A', 'Symbol': 'IGF2', 'normalized_count': '340.286'}, {'ParticipantBarcode': 'TCGA-AB-2812', 'SampleBarcode': 'TCGA-AB-2812-03A', 'Symbol': 'IGF2', 'normalized_count': '6.62708205956115'}, {'ParticipantBarcode': 'TCGA-EE-A2GI', 'SampleBarcode': 'TCGA-EE-A2GI-06A', 'Symbol': 'IGF2', 'normalized_count': '45.0246'}, {'ParticipantBarcode': 'TCGA-EE-A2M5', 'SampleBarcode': 'TCGA-EE-A2M5-06A', 'Symbol': 'IGF2', 'normalized_count': '9.4175'}, {'ParticipantBarcode': 'TCGA-25-1323', 'SampleBarcode': 'TCGA-25-1323-01A', 'Symbol': 'IGF2', 'normalized_count': '320115.343345439'}, {'ParticipantBarcode': 'TCGA-61-2111', 'SampleBarcode': 'TCGA-61-2111-01A', 'Symbol': 'IGF2', 'normalized_count': '54856.2069084881'}, {'ParticipantBarcode': 'TCGA-62-A46V', 'SampleBarcode': 'TCGA-62-A46V-01A', 'Symbol': 'IGF2', 'normalized_count': '2246.39'}, {'ParticipantBarcode': 'TCGA-78-7633', 'SampleBarcode': 'TCGA-78-7633-01A', 'Symbol': 'IGF2', 'normalized_count': '1424.86'}, {'ParticipantBarcode': 'TCGA-A2-A0T5', 'SampleBarcode': 'TCGA-A2-A0T5-01A', 'Symbol': 'IGF2', 'normalized_count': '1632.34'}, {'ParticipantBarcode': 'TCGA-AA-3971', 'SampleBarcode': 'TCGA-AA-3971-01A', 'Symbol': 'IGF2', 'normalized_count': '112.620881000749'}, {'ParticipantBarcode': 'TCGA-AP-A1DV', 'SampleBarcode': 'TCGA-AP-A1DV-01A', 'Symbol': 'IGF2', 'normalized_count': '219.254681397153'}, {'ParticipantBarcode': 'TCGA-BH-A209', 'SampleBarcode': 'TCGA-BH-A209-01A', 'Symbol': 'IGF2', 'normalized_count': '985.679000000001'}, {'ParticipantBarcode': 'TCGA-CN-5366', 'SampleBarcode': 'TCGA-CN-5366-01A', 'Symbol': 'IGF2', 'normalized_count': '4700.61'}, {'ParticipantBarcode': 'TCGA-CV-7433', 'SampleBarcode': 'TCGA-CV-7433-01A', 'Symbol': 'IGF2', 'normalized_count': '1456.34'}, {'ParticipantBarcode': 'TCGA-DX-A3U8', 'SampleBarcode': 'TCGA-DX-A3U8-01A', 'Symbol': 'IGF2', 'normalized_count': '1444.23'}, {'ParticipantBarcode': 'TCGA-DX-AB2V', 'SampleBarcode': 'TCGA-DX-AB2V-01A', 'Symbol': 'IGF2', 'normalized_count': '246825.0'}]}

exec(code, env_args)
