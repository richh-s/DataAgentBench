code = """import json, re, math, pandas as pd

# Load IGF2 expression (all cancers) from file
path_expr = var_call_GPvXZA6dKN94UK0ZHss1XX4C
with open(path_expr, 'r') as f:
    expr = json.load(f)
df_expr = pd.DataFrame(expr)
# ensure numeric
df_expr['normalized_count'] = pd.to_numeric(df_expr['normalized_count'], errors='coerce')
df_expr = df_expr.dropna(subset=['ParticipantBarcode','normalized_count'])

# Load LGG clinical subset from file
path_clin = var_call_Ve6EEefhsSEvpwrds2fMs5nw
with open(path_clin, 'r') as f:
    clin = json.load(f)
df_clin = pd.DataFrame(clin)

# Extract TCGA barcode from Patient_description text
def extract_barcode(s):
    if s is None:
        return None
    m = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', str(s))
    return m.group(1) if m else None

df_clin['ParticipantBarcode_extracted'] = df_clin['participantbarcode'].apply(extract_barcode)
# Clean histology filter: exclude those enclosed in square brackets (e.g., [Not Applicable])
# condition: after stripping, startswith '[' and endswith ']'
def is_bracketed(x):
    if x is None:
        return True
    t = str(x).strip()
    return len(t)>=2 and t[0]=='[' and t[-1]==']'

df_clin = df_clin.dropna(subset=['ParticipantBarcode_extracted','histology'])
df_clin = df_clin[~df_clin['histology'].apply(is_bracketed)]

# Merge clinical LGG with expression IGF2
merged = df_clin.merge(df_expr, left_on='ParticipantBarcode_extracted', right_on='ParticipantBarcode', how='inner')
# log10(normalized_count + 1)
merged['log10_expr'] = merged['normalized_count'].apply(lambda v: math.log10(v + 1.0) if pd.notnull(v) else None)
merged = merged.dropna(subset=['log10_expr'])

# group by histology
res = (merged.groupby('histology', as_index=False)
       .agg(n_patients=('ParticipantBarcode_extracted','nunique'),
            mean_log10_igf2=('log10_expr','mean')))

# format with >=4 decimals
res['mean_log10_igf2'] = res['mean_log10_igf2'].map(lambda x: float(f"{x:.4f}"))
res = res.sort_values('histology')

out = res.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_GPvXZA6dKN94UK0ZHss1XX4C': 'file_storage/call_GPvXZA6dKN94UK0ZHss1XX4C.json', 'var_call_o8S3tiZufLF4GTUFPALWWZaD': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_call_b8METLrDWztdibn6nNALij8B': 'file_storage/call_b8METLrDWztdibn6nNALij8B.json', 'var_call_Ve6EEefhsSEvpwrds2fMs5nw': 'file_storage/call_Ve6EEefhsSEvpwrds2fMs5nw.json'}

exec(code, env_args)
