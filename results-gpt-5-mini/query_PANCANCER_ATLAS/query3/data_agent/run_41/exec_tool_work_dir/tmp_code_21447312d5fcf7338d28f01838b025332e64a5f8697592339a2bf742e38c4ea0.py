code = """import json
# Load mapping of female breast participants and histological types
fp = var_call_dEB2hPG98k6ZxR3ZQn4lpipG
with open(fp, 'r') as f:
    clinical = json.load(f)
mapping = clinical.get('mapping', []) if isinstance(clinical, dict) else clinical
# Load mutants list
mutants_info = var_call_hzFthaahWkP6SXpbF9Y3F5BZ
if isinstance(mutants_info, dict):
    mutants = set(mutants_info.get('mutants', []))
else:
    mutants = set()
# Build counts per histological type
counts = {}
for rec in mapping:
    p = rec.get('ParticipantBarcode')
    hist = rec.get('histological_type')
    if not p or not hist:
        continue
    # normalize hist
    hist = hist.strip()
    if hist == '':
        continue
    if hist not in counts:
        counts[hist] = {'mutated': 0, 'not_mutated': 0}
    if p in mutants:
        counts[hist]['mutated'] += 1
    else:
        counts[hist]['not_mutated'] += 1
# Compute totals and exclude hist types with marginal totals <= 10
rows = []
for hist, ct in counts.items():
    total = ct['mutated'] + ct['not_mutated']
    rows.append({'histological_type': hist, 'mutated': ct['mutated'], 'not_mutated': ct['not_mutated'], 'total': total})
# sort rows by total desc
rows.sort(key=lambda x: x['total'], reverse=True)
included = [r for r in rows if r['total'] > 10]
excluded = [r for r in rows if r['total'] <= 10]
# Build contingency for included
grand_total = sum(r['total'] for r in included)
# column totals
col_mut = sum(r['mutated'] for r in included)
col_not = sum(r['not_mutated'] for r in included)
# If no included rows or grand_total==0, set chi to None
chi2 = None
df = 0
if grand_total > 0 and len(included) >= 2:
    chi2 = 0.0
    for r in included:
        row_tot = r['total']
        # expected mutated
        E_mut = row_tot * col_mut / grand_total if grand_total>0 else 0
        E_not = row_tot * col_not / grand_total if grand_total>0 else 0
        O_mut = r['mutated']
        O_not = r['not_mutated']
        if E_mut>0:
            chi2 += (O_mut - E_mut)**2 / E_mut
        if E_not>0:
            chi2 += (O_not - E_not)**2 / E_not
    df = (len(included)-1)*(2-1)
# Prepare result
result = {
    'grand_total_included': grand_total,
    'n_included_hist_types': len(included),
    'degrees_of_freedom': df,
    'chi_square': chi2,
    'included': included,
    'excluded': excluded,
    'column_totals': {'mutated': col_mut, 'not_mutated': col_not}
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_CB5KdZIMgLhuxySlzeaJW4tB': ['clinical_info'], 'var_call_ESp9aSqT5bXBiOhiMlrD8D36': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_jEt3KQOIyAAqbVDWtMPaZXWa': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_hnEG1wTi3ZnKe9XsveUeNjri': [], 'var_call_whpEJiJ7cfpEQFCmA7BO3aAe': 'file_storage/call_whpEJiJ7cfpEQFCmA7BO3aAe.json', 'var_call_gcW1kiiVcoUodRqkYhxT5b1B': 'file_storage/call_gcW1kiiVcoUodRqkYhxT5b1B.json', 'var_call_bqBgLQYuKM0nqAqS9Qdavsup': 'file_storage/call_bqBgLQYuKM0nqAqS9Qdavsup.json', 'var_call_dEB2hPG98k6ZxR3ZQn4lpipG': 'file_storage/call_dEB2hPG98k6ZxR3ZQn4lpipG.json', 'var_call_5DbqjmMFwjANg4k8NPZAIw6K': 'file_storage/call_5DbqjmMFwjANg4k8NPZAIw6K.json', 'var_call_hzFthaahWkP6SXpbF9Y3F5BZ': {'n_mutants': 247, 'mutants': ['TCGA-05-5428', 'TCGA-06-0210', 'TCGA-06-5416', 'TCGA-21-5787', 'TCGA-22-1016', 'TCGA-2W-A8YY', 'TCGA-2Y-A9H5', 'TCGA-3M-AB47', 'TCGA-42-2590', 'TCGA-4H-AAAK', 'TCGA-50-6590', 'TCGA-55-8614', 'TCGA-55-A4DF', 'TCGA-5L-AAT0', 'TCGA-63-A5MH', 'TCGA-63-A5MM', 'TCGA-66-2759', 'TCGA-77-8009', 'TCGA-77-A5G1', 'TCGA-94-7943', 'TCGA-95-7567', 'TCGA-A1-A0SE', 'TCGA-A2-A0CK', 'TCGA-A2-A0CR', 'TCGA-A2-A0EW', 'TCGA-A2-A0SY', 'TCGA-A2-A0T4', 'TCGA-A2-A0T6', 'TCGA-A2-A0YD', 'TCGA-A2-A0YK', 'TCGA-A2-A0YL', 'TCGA-A2-A1FV', 'TCGA-A2-A1G0', 'TCGA-A2-A25A', 'TCGA-A2-A4S2', 'TCGA-A5-A0VO', 'TCGA-A5-A1OF', 'TCGA-A6-5661', 'TCGA-A7-A425', 'TCGA-A7-A4SC', 'TCGA-A7-A5ZX', 'TCGA-AA-A00N', 'TCGA-AA-A01R', 'TCGA-AC-A2B8', 'TCGA-AC-A2FB', 'TCGA-AC-A2FF', 'TCGA-AC-A2FG', 'TCGA-AC-A2FO', 'TCGA-AC-A3OD', 'TCGA-AC-A3QQ', 'TCGA-AC-A3YI', 'TCGA-AC-A4ZE', 'TCGA-AC-A5XS', 'TCGA-AC-A6IV', 'TCGA-AC-A6IX', 'TCGA-AC-A8OS', 'TCGA-AD-6964', 'TCGA-AH-6544', 'TCGA-AO-A128', 'TCGA-AP-A0LM', 'TCGA-AR-A1AL', 'TCGA-AR-A1AT', 'TCGA-AR-A24X', 'TCGA-AR-A2LE', 'TCGA-AR-A2LK', 'TCGA-AR-A2LN', 'TCGA-AR-A5QM', 'TCGA-AX-A06L', 'TCGA-AX-A0J0', 'TCGA-AX-A1CE', 'TCGA-AX-A2HA', 'TCGA-AX-A2HC', 'TCGA-AX-A2HD', 'TCGA-B0-5692', 'TCGA-B5-A0JY', 'TCGA-B5-A11E', 'TCGA-B5-A11F', 'TCGA-B5-A11G', 'TCGA-B5-A11U', 'TCGA-B5-A1MW', 'TCGA-B6-A0IH', 'TCGA-B6-A0RQ', 'TCGA-B6-A0X7', 'TCGA-B6-A2IU', 'TCGA-B6-A40B', 'TCGA-B6-A40C', 'TCGA-B7-A5TI', 'TCGA-B9-A8YI', 'TCGA-BB-A5HY', 'TCGA-BF-A3DL', 'TCGA-BH-A0C1', 'TCGA-BH-A0E9', 'TCGA-BH-A0HP', 'TCGA-BH-A18F', 'TCGA-BH-A18P', 'TCGA-BH-A209', 'TCGA-BH-A28Q', 'TCGA-BH-A8FY', 'TCGA-BH-AB28', 'TCGA-BR-4187', 'TCGA-BR-4188', 'TCGA-BR-4279', 'TCGA-BR-4292', 'TCGA-BR-6452', 'TCGA-BR-6566', 'TCGA-BR-6803', 'TCGA-BR-8058', 'TCGA-BR-8364', 'TCGA-BR-8370', 'TCGA-BR-8592', 'TCGA-BR-8677', 'TCGA-BR-8686', 'TCGA-BR-A44T', 'TCGA-BR-A453', 'TCGA-BR-A4IV', 'TCGA-BR-A4J9', 'TCGA-BR-A4QM', 'TCGA-BS-A0TE', 'TCGA-BS-A0U8', 'TCGA-BS-A0UV', 'TCGA-C4-A0F0', 'TCGA-C8-A1HO', 'TCGA-C8-A274', 'TCGA-C8-A3M7', 'TCGA-CA-6717', 'TCGA-CC-5260', 'TCGA-CD-5799', 'TCGA-CD-5813', 'TCGA-CD-A4MG', 'TCGA-CG-4474', 'TCGA-CK-6747', 'TCGA-CN-6024', 'TCGA-CR-7370', 'TCGA-CV-6937', 'TCGA-D1-A103', 'TCGA-D5-6928', 'TCGA-D7-6518', 'TCGA-D7-6522', 'TCGA-D7-8572', 'TCGA-D7-8574', 'TCGA-D7-A4YU', 'TCGA-D7-A6EY', 'TCGA-D7-A748', 'TCGA-D8-A1XO', 'TCGA-D8-A1Y1', 'TCGA-D8-A27G', 'TCGA-D8-A27I', 'TCGA-D8-A27V', 'TCGA-D8-A3Z6', 'TCGA-DD-A4NK', 'TCGA-DD-AADA', 'TCGA-DD-AADI', 'TCGA-DD-AAE3', 'TCGA-DF-A2KV', 'TCGA-DK-A1AG', 'TCGA-DK-A6AW', 'TCGA-DK-AA6Q', 'TCGA-DU-6392', 'TCGA-E1-A7YJ', 'TCGA-E2-A10F', 'TCGA-E2-A1IH', 'TCGA-E2-A1IJ', 'TCGA-E2-A1L8', 'TCGA-E2-A576', 'TCGA-E6-A1LX', 'TCGA-E9-A2JT', 'TCGA-E9-A3X8', 'TCGA-E9-A5FK', 'TCGA-E9-A6HE', 'TCGA-EB-A3XC', 'TCGA-EB-A5UM', 'TCGA-EE-A29E', 'TCGA-EE-A2A6', 'TCGA-EJ-7782', 'TCGA-EO-A22R', 'TCGA-EO-A22U', 'TCGA-EO-A22X', 'TCGA-EO-A3AZ', 'TCGA-EW-A1IZ', 'TCGA-EW-A1J5', 'TCGA-EW-A423', 'TCGA-EW-A6SC', 'TCGA-EY-A548', 'TCGA-EY-A5W2', 'TCGA-F1-6874', 'TCGA-F4-6570', 'TCGA-F4-6856', 'TCGA-F5-6814', 'TCGA-FI-A2D0', 'TCGA-FI-A2D5', 'TCGA-FP-8210', 'TCGA-FP-A8CX', 'TCGA-FS-A1ZK', 'TCGA-FW-A3R5', 'TCGA-G2-A3IE', 'TCGA-G4-6586', 'TCGA-G4-6628', 'TCGA-G9-6365', 'TCGA-GC-A3I6', 'TCGA-GI-A2C8']}}

exec(code, env_args)
