code = """import pandas as pd
import json
# load mutation data result
mutations = pd.read_json(var_call_4Ht36IvZdpGccMAqF1c9iCVM)
# load clinical BRCA entries
clinical_brca = pd.read_json(var_call_kbAsW7Ty01Fy6558Gi0x8Qi5)

# Extract patient barcode (first 12 chars) to match patient_id/barcode patterns
mutations['PatientBarcode12'] = mutations['ParticipantBarcode'].str.slice(0,12)

# From clinical Patient_description, extract the TCGA barcode if present
import re

def extract_tcga(desc):
    if not isinstance(desc, str):
        return None
    m = re.search(r'(TCGA[-A-Z0-9]{2,}-[A-Z0-9]{2,}-[0-9]{4,}|TCGA[-A-Z0-9]{2,}-[0-9]{2}-[0-9]{4})', desc)
    if m:
        return m.group(0)
    m2 = re.search(r'(TCGA[-A-Z0-9]{2,}-[A-Z0-9]{2,}-[A-Z0-9]{4,})', desc)
    if m2:
        return m2.group(0)
    return None

clinical_brca['TCGA_barcode'] = clinical_brca['Patient_description'].map(extract_tcga)

# For matching, create patient id field similar format: some patient_ids are like A5EH which map to TCGA-AC-A5EH, but Patient_description contains full barcode. We'll use TCGA_barcode when available
# Filter clinical rows to those with a TCGA barcode
clinical_brca = clinical_brca[clinical_brca['TCGA_barcode'].notna()].copy()

# Merge by barcode
merged = mutations.merge(clinical_brca, left_on='PatientBarcode12', right_on='TCGA_barcode', how='inner')

# Filter to patients who are alive per Patient_description containing 'Alive' (case-insensitive)
merged['is_alive'] = merged['Patient_description'].str.contains('Alive', case=False, na=False)
merged_alive = merged[merged['is_alive']]

# Now for BRCA cohort only: ensure tumor_tissue_site or Patient_description indicates Breast invasive carcinoma
# Use presence of 'Breast' or 'BRCA' in Patient_description
merged_alive_brca = merged_alive[merged_alive['Patient_description'].str.contains('Breast', case=False, na=False)]

# Compute counts per histological_type: number of patients with CDH1 mutation / total alive patients in that histology
# First get unique patients with CDH1 mutation per histology
mut_per_hist = merged_alive_brca.groupby(['histological_type'])['PatientBarcode12'].nunique().reset_index().rename(columns={'PatientBarcode12':'mutated_patients'})

# Total alive patients per histology from clinical_brca (using TCGA_barcode and Alive)
clinical_brca['is_alive'] = clinical_brca['Patient_description'].str.contains('Alive', case=False, na=False)
total_alive_per_hist = clinical_brca[clinical_brca['is_alive'] & clinical_brca['Patient_description'].str.contains('Breast', case=False, na=False)].groupby('histological_type')['TCGA_barcode'].nunique().reset_index().rename(columns={'TCGA_barcode':'total_alive'})

# Merge and compute percentage
df = total_alive_per_hist.merge(mut_per_hist, on='histological_type', how='left')
df['mutated_patients'] = df['mutated_patients'].fillna(0).astype(int)
df['percent_mutated'] = (df['mutated_patients'] / df['total_alive']) * 100

# Get top 3 histological types by percent_mutated
top3 = df.sort_values('percent_mutated', ascending=False).head(3)

result = top3[['histological_type','mutated_patients','total_alive','percent_mutated']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ZcJhKyusQtvT3R0vivULW3FL': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_nmhjZvbvCkurCSR1sqBhQWr7': [], 'var_call_j8wvmBP5OD4v2thIa0g41MiT': 'file_storage/call_j8wvmBP5OD4v2thIa0g41MiT.json', 'var_call_Ze1BcOhFxBx8zfo6rDwOHSdm': [], 'var_call_kbAsW7Ty01Fy6558Gi0x8Qi5': 'file_storage/call_kbAsW7Ty01Fy6558Gi0x8Qi5.json', 'var_call_cZCkyGzLrDWpoQ4dVwWKUtwv': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_MANPaCGiKpuSeTv8jJidsCRv': [{'Hugo_Symbol': 'A1BG'}, {'Hugo_Symbol': 'A1CF'}, {'Hugo_Symbol': 'A2M'}, {'Hugo_Symbol': 'A2ML1'}, {'Hugo_Symbol': 'A3GALT2'}, {'Hugo_Symbol': 'A4GALT'}, {'Hugo_Symbol': 'A4GNT'}, {'Hugo_Symbol': 'AAAS'}, {'Hugo_Symbol': 'AACS'}, {'Hugo_Symbol': 'AACSP1'}, {'Hugo_Symbol': 'AADAC'}, {'Hugo_Symbol': 'AADACL2'}, {'Hugo_Symbol': 'AADACL3'}, {'Hugo_Symbol': 'AADACL4'}, {'Hugo_Symbol': 'AADAT'}, {'Hugo_Symbol': 'AAED1'}, {'Hugo_Symbol': 'AAGAB'}, {'Hugo_Symbol': 'AAK1'}, {'Hugo_Symbol': 'AAMDC'}, {'Hugo_Symbol': 'AAMP'}, {'Hugo_Symbol': 'AANAT'}, {'Hugo_Symbol': 'AAR2'}, {'Hugo_Symbol': 'AARD'}, {'Hugo_Symbol': 'AARS'}, {'Hugo_Symbol': 'AARS2'}, {'Hugo_Symbol': 'AARSD1'}, {'Hugo_Symbol': 'AASDH'}, {'Hugo_Symbol': 'AASDHPPT'}, {'Hugo_Symbol': 'AASS'}, {'Hugo_Symbol': 'AATF'}, {'Hugo_Symbol': 'AATK'}, {'Hugo_Symbol': 'ABAT'}, {'Hugo_Symbol': 'ABCA1'}, {'Hugo_Symbol': 'ABCA10'}, {'Hugo_Symbol': 'ABCA12'}, {'Hugo_Symbol': 'ABCA13'}, {'Hugo_Symbol': 'ABCA2'}, {'Hugo_Symbol': 'ABCA3'}, {'Hugo_Symbol': 'ABCA4'}, {'Hugo_Symbol': 'ABCA5'}, {'Hugo_Symbol': 'ABCA6'}, {'Hugo_Symbol': 'ABCA7'}, {'Hugo_Symbol': 'ABCA8'}, {'Hugo_Symbol': 'ABCA9'}, {'Hugo_Symbol': 'ABCB1'}, {'Hugo_Symbol': 'ABCB10'}, {'Hugo_Symbol': 'ABCB11'}, {'Hugo_Symbol': 'ABCB4'}, {'Hugo_Symbol': 'ABCB5'}, {'Hugo_Symbol': 'ABCB6'}], 'var_call_4Ht36IvZdpGccMAqF1c9iCVM': 'file_storage/call_4Ht36IvZdpGccMAqF1c9iCVM.json'}

exec(code, env_args)
