code = """import pandas as pd
import json
import re

with open(locals()['var_function-call-13367685561179644137'], 'r') as f:
    clinical_data = json.load(f)

with open(locals()['var_function-call-1297996372214098068'], 'r') as f:
    mutation_data = json.load(f)

clin_records = []
for entry in clinical_data:
    desc = entry.get('Patient_description', '')
    hist_type = entry.get('histological_type')
    
    # Extract Barcode
    match = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', desc)
    barcode = match.group(1) if match else None
    
    # Extract Gender - simplied regex
    if 'FEMALE' in desc.upper():
        gender = 'FEMALE'
    elif 'MALE' in desc.upper():
        gender = 'MALE'
    else:
        gender = None
    
    if barcode and gender == 'FEMALE' and hist_type and hist_type != 'None':
        clin_records.append({
            'ParticipantBarcode': barcode,
            'histological_type': hist_type
        })

df_clin = pd.DataFrame(clin_records)

mutated_barcodes = set()
for item in mutation_data:
    if isinstance(item, dict):
        val = item.get('ParticipantBarcode')
        if val:
            mutated_barcodes.add(val)

df_clin['has_mutation'] = df_clin['ParticipantBarcode'].isin(mutated_barcodes)

contingency_table = pd.crosstab(df_clin['histological_type'], df_clin['has_mutation'])

# Filter rows with sum <= 10
row_sums = contingency_table.sum(axis=1)
filtered_table = contingency_table[row_sums > 10]

grand_total = filtered_table.values.sum()
col_totals = filtered_table.sum(axis=0)
row_totals = filtered_table.sum(axis=1)

chi2 = 0
for row_idx in filtered_table.index:
    for col_idx in filtered_table.columns:
        O = filtered_table.at[row_idx, col_idx]
        E = (row_totals[row_idx] * col_totals[col_idx]) / grand_total
        if E > 0:
            chi2 += ((O - E) ** 2) / E

# Formatting result
# Convert boolean columns to str for json
filtered_table.columns = [str(c) for c in filtered_table.columns]

print("__RESULT__:")
print(json.dumps({
    "chi_square_statistic": chi2,
    "filtered_table": filtered_table.to_dict(),
    "original_row_counts": row_sums.to_dict(),
    "num_patients": len(df_clin)
}))"""

env_args = {'var_function-call-4362257245335172234': ['clinical_info'], 'var_function-call-11458167224637955690': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_function-call-2028626036414233186': [{'tumor_tissue_site': 'Breast', 'histological_type': 'None', 'count': '1'}, {'tumor_tissue_site': 'Breast', 'histological_type': 'Infiltrating Ductal Carcinoma', 'count': '777'}, {'tumor_tissue_site': 'Breast', 'histological_type': 'Mucinous Carcinoma', 'count': '17'}, {'tumor_tissue_site': 'Breast', 'histological_type': 'Metaplastic Carcinoma', 'count': '8'}, {'tumor_tissue_site': 'Breast', 'histological_type': 'Mixed Histology (please specify)', 'count': '30'}, {'tumor_tissue_site': 'Breast', 'histological_type': 'Infiltrating Lobular Carcinoma', 'count': '201'}, {'tumor_tissue_site': 'Breast', 'histological_type': 'Other  specify', 'count': '46'}, {'tumor_tissue_site': 'Breast', 'histological_type': 'Medullary Carcinoma', 'count': '6'}, {'tumor_tissue_site': 'Breast', 'histological_type': 'Infiltrating Carcinoma NOS', 'count': '1'}], 'var_function-call-13367685561179644137': 'file_storage/function-call-13367685561179644137.json', 'var_function-call-1297996372214098068': 'file_storage/function-call-1297996372214098068.json', 'var_function-call-8280041105654717650': {'error': 'No clinical records found matching criteria'}, 'var_function-call-6899824498488722150': 'debug_done', 'var_function-call-2184653120178821384': {'total_entries': 1087, 'sample_entry': {'Patient_description': 'Clinical entry D13FB44B-291B-4EA4-920C-142DAA8D1989 identifies patient TCGA-AC-A5EH, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, 'barcode_match': 'TCGA-AC-A5EH', 'gender_match': 'No match', 'hist_type': 'Infiltrating Ductal Carcinoma'}}

exec(code, env_args)
