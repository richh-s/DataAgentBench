code = """import json
import pandas as pd
import re
import math

# Load the clinical LGG results (stored in a .json file path)
clinical_path = var_call_1XQ7UyxdOYbYS1Fjxe3jmVlW
with open(clinical_path, 'r') as f:
    clinical_data = json.load(f)

# Load the IGF2 expression results
mol_path = var_call_ULeWqBz6psOvL6PA81XsYoec
with open(mol_path, 'r') as f:
    mol_data = json.load(f)

# Create DataFrames
df_clin = pd.DataFrame(clinical_data)
# keep only relevant columns if present
if 'Patient_description' not in df_clin.columns or 'histological_type' not in df_clin.columns:
    # ensure columns exist
    df_clin = df_clin[['patient_id', 'Patient_description', 'histological_type']]

# Extract TCGA barcode from Patient_description using regex
pattern = re.compile(r'(TCGA-[A-Za-z0-9-]+?)\b')

def extract_barcode(desc):
    if not isinstance(desc, str):
        return None
    m = pattern.search(desc)
    if m:
        return m.group(1)
    return None

df_clin['tcga_barcode'] = df_clin['Patient_description'].apply(extract_barcode)
# Drop rows without barcode or without histology
df_clin = df_clin.dropna(subset=['tcga_barcode', 'histological_type'])

# Filter out histological_type entries enclosed in square brackets (contain [ or ])
mask = ~df_clin['histological_type'].str.contains(r"\[|\]", regex=True)
df_clin = df_clin[mask].copy()

# Molecular df
df_mol = pd.DataFrame(mol_data)
# Ensure normalized_count is numeric
df_mol = df_mol[df_mol['Symbol']=='IGF2'].copy()
# Convert normalized_count to float, coerce errors
df_mol['normalized_count'] = pd.to_numeric(df_mol['normalized_count'], errors='coerce')
# Drop invalid or negative
df_mol = df_mol.dropna(subset=['normalized_count'])
# Keep non-negative
df_mol = df_mol[df_mol['normalized_count'] >= 0].copy()

# For each clinical row, find matching molecular rows where ParticipantBarcode startswith tcga_barcode
# Collect pairs of (histology, normalized_count)
pairs = []
for _, row in df_clin.iterrows():
    cb = row['tcga_barcode']
    hist = row['histological_type']
    # Find matches
    matches = df_mol[df_mol['ParticipantBarcode'].str.startswith(cb, na=False)]
    if matches.empty:
        # Also try matching by patient_id fragment if barcode not matching
        continue
    for _, m in matches.iterrows():
        pairs.append({'histology': hist, 'normalized_count': float(m['normalized_count'])})

# If no pairs found, return empty
if len(pairs) == 0:
    result = {}
else:
    df_pairs = pd.DataFrame(pairs)
    import numpy as np
    # compute log10(normalized_count + 1)
    df_pairs['log10_expr'] = np.log10(df_pairs['normalized_count'] + 1)
    # group by histology and compute mean
    grouped = df_pairs.groupby('histology', dropna=False)['log10_expr'].mean()
    # Format to at least 4 decimal places
    result = {hist: float(f"{val:.4f}") for hist, val in grouped.items()}

# Print result as JSON string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_QUsWqlT3K2sSqukT2KMGTDav': ['clinical_info'], 'var_call_2AJrb291QSJnHelDgGsX7JWC': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_faNbmtaz3AEUOcXegIGSjltD': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_E4XXD0EEOWSLtylqF7YxTLIA': 'file_storage/call_E4XXD0EEOWSLtylqF7YxTLIA.json', 'var_call_1XQ7UyxdOYbYS1Fjxe3jmVlW': 'file_storage/call_1XQ7UyxdOYbYS1Fjxe3jmVlW.json', 'var_call_ULeWqBz6psOvL6PA81XsYoec': 'file_storage/call_ULeWqBz6psOvL6PA81XsYoec.json'}

exec(code, env_args)
