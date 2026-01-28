code = """import json, re, pandas as pd

def load_records(maybe_path_or_records):
    if isinstance(maybe_path_or_records, str) and maybe_path_or_records.endswith('.json'):
        with open(maybe_path_or_records, 'r') as f:
            return json.load(f)
    return maybe_path_or_records

clin = load_records(var_call_FWu1TekXp9Y7pNzRQvelnWFC)
mut = load_records(var_call_NTLS5u8qgafhSeuVPrgWkWpK)

clin_df = pd.DataFrame(clin)
mut_df = pd.DataFrame(mut)

# Extract TCGA barcode from Patient_description
clin_df['ParticipantBarcode'] = clin_df['Patient_description'].str.extract(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', expand=False)

# Keep BRCA alive patients with known histology and barcode
clin_df = clin_df.dropna(subset=['ParticipantBarcode'])
clin_df['histological_type'] = clin_df['histological_type'].fillna('Unknown')

alive_brca = clin_df[['ParticipantBarcode','histological_type']].drop_duplicates()

# Determine which of these have CDH1 mutation (any record)
cdh1_set = set(mut_df['ParticipantBarcode'].dropna().unique().tolist())
alive_brca['has_CDH1_mut'] = alive_brca['ParticipantBarcode'].isin(cdh1_set)

# Aggregate by histological_type
grp = alive_brca.groupby('histological_type').agg(
    n_alive=('ParticipantBarcode','nunique'),
    n_cdh1=('has_CDH1_mut','sum')
).reset_index()

grp['pct_cdh1'] = (grp['n_cdh1'] / grp['n_alive'] * 100).where(grp['n_alive']>0)

# Rank: highest percentage; tie-breaker by n_cdh1 then n_alive
res = grp.sort_values(['pct_cdh1','n_cdh1','n_alive'], ascending=[False, False, False]).head(3)

out = res.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_NTLS5u8qgafhSeuVPrgWkWpK': 'file_storage/call_NTLS5u8qgafhSeuVPrgWkWpK.json', 'var_call_GPV8ZKdweVsCSVvzzsZO1J5P': ['clinical_info'], 'var_call_4Ay87UTqJEdVmf2K1l7EiMGJ': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_call_fvC8MltYliULWWYLMIb4apCv': [{'Patient_description': 'Patient TCGA-AC-A2FB (UUID 02BBB632-0F7F-439D-B8F0-C86A06237424) is a FEMALE diagnosed with Breast invasive carcinoma. Current vital status: Alive.', 'histological_type': 'Infiltrating Lobular Carcinoma'}, {'Patient_description': 'Patient TCGA-AC-A3YI (UUID A45D296E-EFC0-479E-B2F6-BAD834668CDF) is a FEMALE diagnosed with Breast invasive carcinoma. Current vital status: Alive.', 'histological_type': 'Infiltrating Lobular Carcinoma'}, {'Patient_description': 'Patient TCGA-EW-A2FS (FEMALE, UUID D34471A1-B367-4F8A-B35A-C5901C4F5503) is enrolled in the study of Breast invasive carcinoma. Vital status: Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Patient TCGA-GM-A5PX (UUID F7064D01-29D8-49A2-AD60-1E0C5F148F3E) is a FEMALE diagnosed with Breast invasive carcinoma. Current vital status: Alive.', 'histological_type': 'Infiltrating Lobular Carcinoma'}, {'Patient_description': 'In the Breast invasive carcinoma dataset, patient TCGA-PE-A5DD (UUID B0700958-5F90-4546-B35F-635CD506889B) is recorded as a FEMALE with vital status: Alive.', 'histological_type': 'Infiltrating Lobular Carcinoma'}], 'var_call_FWu1TekXp9Y7pNzRQvelnWFC': 'file_storage/call_FWu1TekXp9Y7pNzRQvelnWFC.json'}

exec(code, env_args)
