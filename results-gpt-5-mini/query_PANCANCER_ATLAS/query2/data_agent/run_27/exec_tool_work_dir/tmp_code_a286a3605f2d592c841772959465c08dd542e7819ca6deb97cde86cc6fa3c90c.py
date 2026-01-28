code = """import json
import pandas as pd

# read mutation file (path or json string)
mut_path = var_call_4Ht36IvZdpGccMAqF1c9iCVM
try:
    mutations = pd.read_json(mut_path)
except Exception:
    # if it's already a list
    mutations = pd.DataFrame(var_call_4Ht36IvZdpGccMAqF1c9iCVM)

# read clinical file
clin_path = var_call_kbAsW7Ty01Fy6558Gi0x8Qi5
try:
    clinical = pd.read_json(clin_path)
except Exception:
    clinical = pd.DataFrame(var_call_kbAsW7Ty01Fy6558Gi0x8Qi5)

# show samples
mut_samples = mutations['ParticipantBarcode'].dropna().unique()[:30].tolist()
clin_samples = clinical['Patient_description'].dropna().head(30).tolist()

# try extracting TCGA barcode with different regex patterns
import re

def extract1(s):
    m = re.search(r'TCGA[-A-Z0-9]{2,}-[A-Z0-9]{2,}-[A-Z0-9]{4,}', s)
    return m.group(0) if m else None

def extract2(s):
    m = re.search(r'(TCGA[-A-Z0-9]{2,}-[A-Z0-9]{2,}-[0-9]{4,})', s)
    return m.group(0) if m else None

def extract3(s):
    m = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', s)
    return m.group(0) if m else None

examples = []
for i,desc in enumerate(clin_samples):
    examples.append({'index':i,'desc':desc,'ext1': extract1(desc),'ext2': extract2(desc),'ext3': extract3(desc)})

# show first 30 mutation barcodes
mut_examples = mut_samples

out = {'mutation_barcodes_sample': mut_examples, 'clinical_examples': examples}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_ZcJhKyusQtvT3R0vivULW3FL': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_nmhjZvbvCkurCSR1sqBhQWr7': [], 'var_call_j8wvmBP5OD4v2thIa0g41MiT': 'file_storage/call_j8wvmBP5OD4v2thIa0g41MiT.json', 'var_call_Ze1BcOhFxBx8zfo6rDwOHSdm': [], 'var_call_kbAsW7Ty01Fy6558Gi0x8Qi5': 'file_storage/call_kbAsW7Ty01Fy6558Gi0x8Qi5.json', 'var_call_cZCkyGzLrDWpoQ4dVwWKUtwv': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_MANPaCGiKpuSeTv8jJidsCRv': [{'Hugo_Symbol': 'A1BG'}, {'Hugo_Symbol': 'A1CF'}, {'Hugo_Symbol': 'A2M'}, {'Hugo_Symbol': 'A2ML1'}, {'Hugo_Symbol': 'A3GALT2'}, {'Hugo_Symbol': 'A4GALT'}, {'Hugo_Symbol': 'A4GNT'}, {'Hugo_Symbol': 'AAAS'}, {'Hugo_Symbol': 'AACS'}, {'Hugo_Symbol': 'AACSP1'}, {'Hugo_Symbol': 'AADAC'}, {'Hugo_Symbol': 'AADACL2'}, {'Hugo_Symbol': 'AADACL3'}, {'Hugo_Symbol': 'AADACL4'}, {'Hugo_Symbol': 'AADAT'}, {'Hugo_Symbol': 'AAED1'}, {'Hugo_Symbol': 'AAGAB'}, {'Hugo_Symbol': 'AAK1'}, {'Hugo_Symbol': 'AAMDC'}, {'Hugo_Symbol': 'AAMP'}, {'Hugo_Symbol': 'AANAT'}, {'Hugo_Symbol': 'AAR2'}, {'Hugo_Symbol': 'AARD'}, {'Hugo_Symbol': 'AARS'}, {'Hugo_Symbol': 'AARS2'}, {'Hugo_Symbol': 'AARSD1'}, {'Hugo_Symbol': 'AASDH'}, {'Hugo_Symbol': 'AASDHPPT'}, {'Hugo_Symbol': 'AASS'}, {'Hugo_Symbol': 'AATF'}, {'Hugo_Symbol': 'AATK'}, {'Hugo_Symbol': 'ABAT'}, {'Hugo_Symbol': 'ABCA1'}, {'Hugo_Symbol': 'ABCA10'}, {'Hugo_Symbol': 'ABCA12'}, {'Hugo_Symbol': 'ABCA13'}, {'Hugo_Symbol': 'ABCA2'}, {'Hugo_Symbol': 'ABCA3'}, {'Hugo_Symbol': 'ABCA4'}, {'Hugo_Symbol': 'ABCA5'}, {'Hugo_Symbol': 'ABCA6'}, {'Hugo_Symbol': 'ABCA7'}, {'Hugo_Symbol': 'ABCA8'}, {'Hugo_Symbol': 'ABCA9'}, {'Hugo_Symbol': 'ABCB1'}, {'Hugo_Symbol': 'ABCB10'}, {'Hugo_Symbol': 'ABCB11'}, {'Hugo_Symbol': 'ABCB4'}, {'Hugo_Symbol': 'ABCB5'}, {'Hugo_Symbol': 'ABCB6'}], 'var_call_4Ht36IvZdpGccMAqF1c9iCVM': 'file_storage/call_4Ht36IvZdpGccMAqF1c9iCVM.json', 'var_call_dWwvqT48hRbrrRKnnAIFgXtp': []}

exec(code, env_args)
