code = """import json, re, math
import pandas as pd

def load_records(x):
    if isinstance(x, str):
        with open(x, 'r') as f:
            return json.load(f)
    return x

clin = load_records(var_call_Gt6nuajEvmFLN8HUOPPd76pq)
expr = load_records(var_call_9h6i5wf400KNX5HOQ2tXDJo8)

# parse TCGA barcode from Patient_description-like field
pat = re.compile(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})')
clin_rows = []
for r in clin:
    desc = r.get('ParticipantBarcode') or r.get('participantbarcode')
    hist = r.get('histology')
    if desc is None or hist is None:
        continue
    m = pat.search(desc)
    if not m:
        continue
    barcode = m.group(1)
    clin_rows.append({'ParticipantBarcode': barcode, 'histology': hist})

clin_df = pd.DataFrame(clin_rows).drop_duplicates()
expr_df = pd.DataFrame(expr)
expr_df['normalized_count'] = pd.to_numeric(expr_df['normalized_count'], errors='coerce')
expr_df = expr_df.dropna(subset=['normalized_count'])

# Only include LGG patients: infer LGG by histology types typical for lower grade glioma
# (exclude GBM-related types)
# Keep rows whose histology contains Astrocytoma, Oligodendroglioma, or Mixed glioma/oligoastrocytoma
hist_series = clin_df['histology'].astype(str)
mask_lgg = hist_series.str.contains('astrocytoma', case=False, na=False) | \
           hist_series.str.contains('oligodendroglioma', case=False, na=False) | \
           hist_series.str.contains('oligoastrocytoma', case=False, na=False) | \
           hist_series.str.contains('mixed glioma', case=False, na=False)
clin_lgg = clin_df[mask_lgg].copy()

merged = clin_lgg.merge(expr_df, on='ParticipantBarcode', how='inner')
merged['log10_expr'] = merged['normalized_count'].apply(lambda v: math.log10(v + 1.0))

out = (merged.groupby('histology', as_index=False)
       .agg(n=('log10_expr','size'), avg_log10_igf2=('log10_expr','mean'))
       .sort_values('histology'))

# format avg with >=4 decimals
out['avg_log10_igf2'] = out['avg_log10_igf2'].map(lambda x: float(f"{x:.4f}"))
res = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_9h6i5wf400KNX5HOQ2tXDJo8': 'file_storage/call_9h6i5wf400KNX5HOQ2tXDJo8.json', 'var_call_mri4SQcJVnNjnmz1DXKWgw4M': ['clinical_info'], 'var_call_viOtUCnhjoEYDxVXdu5kHHMC': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_call_MNiKquOuFZDCYz1JukOUPU3T': [], 'var_call_Gt6nuajEvmFLN8HUOPPd76pq': 'file_storage/call_Gt6nuajEvmFLN8HUOPPd76pq.json'}

exec(code, env_args)
