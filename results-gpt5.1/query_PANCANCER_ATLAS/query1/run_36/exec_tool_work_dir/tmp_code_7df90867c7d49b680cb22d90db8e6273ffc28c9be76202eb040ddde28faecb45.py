code = """import json, math, pandas as pd

# Load full RNA expression result
with open(var_call_m7NYQU1kM63KL2oAcGeg3qob, 'r') as f:
    rna = json.load(f)

# Load full brain clinical result
with open(var_call_oDFyUYUzkdr2JqJZLIPNj7NV, 'r') as f:
    clin = json.load(f)

rna_df = pd.DataFrame(rna)
clin_df = pd.DataFrame(clin)

# Extract patient barcode from Patient_description (e.g., 'Patient TCGA-32-4209 ...' or 'The individual with barcode TCGA-41-3393 ...' )
import re

def extract_barcode(desc):
    if not isinstance(desc, str):
        return None
    m = re.search(r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}', desc)
    return m.group(0) if m else None

clin_df['ParticipantBarcode'] = clin_df['Patient_description'].apply(extract_barcode)

# Filter to LGG patients: those where study is 'Brain lower grade glioma' or similar in description
# Many descriptions contain 'Glioblastoma multiforme'; LGG ones should say 'Brain Lower Grade Glioma' or similar
clin_df['is_LGG'] = clin_df['Patient_description'].str.contains('Lower Grade Glioma', case=False, na=False)

lgg_clin = clin_df[clin_df['is_LGG']].copy()

# If no LGG found, return message
if lgg_clin.empty:
    result = {"error": "No LGG patients identified in clinical_database based on available fields."}
else:
    # Filter histology where value is not enclosed in [] entirely
    def valid_hist(h):
        if not isinstance(h, str):
            return False
        h = h.strip()
        return not (h.startswith('[') and h.endswith(']'))

    # Prefer histological_type_other when valid, else histological_type
    lgg_clin['histology'] = lgg_clin.apply(
        lambda row: row['histological_type_other'] if valid_hist(row.get('histological_type_other')) else row.get('histological_type'),
        axis=1
    )
    lgg_clin = lgg_clin[lgg_clin['histology'].apply(valid_hist)]

    # Merge with RNA on ParticipantBarcode
    rna_df['normalized_count'] = pd.to_numeric(rna_df['normalized_count'], errors='coerce')
    merged = pd.merge(rna_df, lgg_clin[['ParticipantBarcode', 'histology']], on='ParticipantBarcode', how='inner')
    merged = merged.dropna(subset=['normalized_count', 'histology'])

    if merged.empty:
        result = {"error": "No overlapping LGG patients with IGF2 expression and valid histology."}
    else:
        merged['log10_expr'] = (merged['normalized_count'] + 1).apply(lambda x: math.log10(x) if x > 0 else None)
        grouped = merged.groupby('histology')['log10_expr'].mean().dropna()
        result = {k: round(v, 4) for k, v in grouped.to_dict().items()}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_m7NYQU1kM63KL2oAcGeg3qob': 'file_storage/call_m7NYQU1kM63KL2oAcGeg3qob.json', 'var_call_PPiqI1LkA062CuUKsgoDs2Gb': ['clinical_info'], 'var_call_D4SlaXmMWUxTidVlaMern9VE': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_wQyTjgazpTH6XRFHPVZYyw2M': [], 'var_call_Rl57kRnfyjlEpitvFZjbap7C': [], 'var_call_kolu1PXK2StVdfyqRu8YgiTe': [], 'var_call_E8hEWH9UFuN70v5nnqslVDU9': [{'tumor_tissue_site': 'Brain'}], 'var_call_oDFyUYUzkdr2JqJZLIPNj7NV': 'file_storage/call_oDFyUYUzkdr2JqJZLIPNj7NV.json'}

exec(code, env_args)
