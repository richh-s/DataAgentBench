code = """import json, re
# load clinical BRCA alive results
with open(var_call_xYkG7q5w75SfilKi6ZRiXfJu, 'r') as f:
    clinical = json.load(f)
# load CDH1 mutation participant barcodes
with open(var_call_RXvpxDzYbyFfxnOmB0x3Pt7E, 'r') as f:
    muts = json.load(f)
mut_barcodes = set([m['ParticipantBarcode'] for m in muts if m.get('ParticipantBarcode')])

# build mapping barcode -> histological_type from clinical
barcode_to_hist = {}
for rec in clinical:
    pd = rec.get('Patient_description','')
    hist = rec.get('histological_type') or rec.get('histological_type','Unknown')
    # find first token starting with TCGA-
    m = re.search(r'(TCGA[-][A-Za-z0-9-]+)', pd)
    if not m:
        continue
    bc = m.group(1).strip(' ,)')
    # normalize barcode: some have lower/upper, keep as-is
    if bc not in barcode_to_hist:
        barcode_to_hist[bc] = hist

# aggregate per histological type
from collections import defaultdict
hist_totals = defaultdict(set)
hist_mut = defaultdict(set)
for bc, hist in barcode_to_hist.items():
    hist_totals[hist].add(bc)
    if bc in mut_barcodes:
        hist_mut[hist].add(bc)

# compute percentages
results = []
for hist, total_set in hist_totals.items():
    total = len(total_set)
    mutated = len(hist_mut.get(hist, set()))
    pct = (mutated/total*100) if total>0 else 0.0
    results.append({'histological_type': hist, 'total_alive': total, 'mutated_count': mutated, 'percent_mutated': round(pct,2)})

# sort by percent_mutated desc, then mutated_count desc, then total desc
results_sorted = sorted(results, key=lambda x: (-x['percent_mutated'], -x['mutated_count'], -x['total_alive']))
top3 = results_sorted[:3]

print('__RESULT__:')
print(json.dumps(top3))"""

env_args = {'var_call_MbXaRxowvDqekvVK5bzseCV9': 'file_storage/call_MbXaRxowvDqekvVK5bzseCV9.json', 'var_call_KDbdIEkzZKffDDhobk6UMFbN': {'columns': ['Patient_description', 'days_to_birth', 'days_to_death', 'days_to_last_followup', 'days_to_initial_pathologic_diagnosis', 'age_at_initial_pathologic_diagnosis', 'icd_10', 'tissue_retrospective_collection_indicator', 'icd_o_3_histology', 'tissue_prospective_collection_indicator', 'history_of_neoadjuvant_treatment', 'icd_o_3_site', 'tumor_tissue_site', 'new_tumor_event_after_initial_treatment', 'radiation_therapy', 'race', 'prior_dx', 'ethnicity', 'informed_consent_verified', 'person_neoplasm_cancer_status', 'patient_id', 'year_of_initial_pathologic_diagnosis', 'histological_type', 'tissue_source_site', 'form_completion_date', 'pathologic_T', 'pathologic_M', 'clinical_M', 'pathologic_N', 'system_version', 'pathologic_stage', 'clinical_stage', 'clinical_T', 'clinical_N', 'extranodal_involvement', 'postoperative_rx_tx', 'primary_therapy_outcome_success', 'lymph_node_examined_count', 'primary_lymph_node_presentation_assessment', 'initial_pathologic_diagnosis_method', 'number_of_lymphnodes_positive_by_he', 'eastern_cancer_oncology_group', 'anatomic_neoplasm_subdivision', 'residual_tumor', 'histological_type_other', 'init_pathology_dx_method_other', 'karnofsky_performance_score', 'neoplasm_histologic_grade', 'height', 'weight', 'number_of_lymphnodes_positive_by_ihc', 'tobacco_smoking_history', 'number_pack_years_smoked', 'stopped_smoking_year', 'performance_status_scale_timing', 'laterality', 'targeted_molecular_therapy', 'year_of_tobacco_smoking_onset', 'anatomic_neoplasm_subdivision_other', 'patient_death_reason', 'tumor_tissue_site_other', 'menopause_status', 'margin_status', 'kras_gene_analysis_performed', 'venous_invasion', 'lymphatic_invasion', 'perineural_invasion_present', 'her2_immunohistochemistry_level_result', 'breast_carcinoma_progesterone_receptor_status', 'breast_carcinoma_surgical_procedure_name', 'breast_neoplasm_other_surgical_procedure_descriptive_text', 'axillary_lymph_node_stage_method_type', 'breast_carcinoma_estrogen_receptor_status', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi', 'lab_proc_her2_neu_immunohistochemistry_receptor_status', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type', 'additional_pharmaceutical_therapy', 'additional_radiation_therapy', 'lymphovascular_invasion_present', 'location_in_lung_parenchyma', 'pulmonary_function_test_performed', 'egfr_mutation_performed', 'diagnosis', 'eml4_alk_translocation_performed', 'days_to_new_tumor_event_after_initial_treatment', 'hemoglobin_result', 'serum_calcium_result', 'platelet_qualitative_result', 'number_of_lymphnodes_positive', 'white_cell_count_result', 'alcohol_history_documented', 'family_history_of_cancer', 'braf_gene_analysis_performed', 'city_of_procurement', 'surgical_approach', 'peritoneal_wash', 'total_pelv_lnr', 'total_aor_lnr', 'prior_glioma'], 'sample_row': {'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}}, 'var_call_xYkG7q5w75SfilKi6ZRiXfJu': 'file_storage/call_xYkG7q5w75SfilKi6ZRiXfJu.json', 'var_call_1UC4yqqA5mS52APwgDYj6oac': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_RXvpxDzYbyFfxnOmB0x3Pt7E': 'file_storage/call_RXvpxDzYbyFfxnOmB0x3Pt7E.json', 'var_call_sXI5cMsthEV0XcoWXxRazKey': {'total_CDH1_records': 318, 'unique_participants_with_CDH1': 301, 'sample_20_unique': ['TCGA-05-5428', 'TCGA-06-0210', 'TCGA-06-1800', 'TCGA-06-5416', 'TCGA-13-0807', 'TCGA-13-0889', 'TCGA-19-1386', 'TCGA-21-5787', 'TCGA-22-1016', 'TCGA-2W-A8YY', 'TCGA-2Y-A9H5', 'TCGA-3M-AB47', 'TCGA-42-2590', 'TCGA-4H-AAAK', 'TCGA-50-6590', 'TCGA-55-8614', 'TCGA-55-A4DF', 'TCGA-5L-AAT0', 'TCGA-61-1904', 'TCGA-63-A5MH']}}

exec(code, env_args)
