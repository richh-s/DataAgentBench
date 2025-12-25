code = """import pandas as pd
import json
import re

# Load clinical data
with open(locals()['var_function-call-8113958776897834218'], 'r') as f:
    clinical_list = json.load(f)

# Load mutation data
with open(locals()['var_function-call-12588489646648170295'], 'r') as f:
    mutation_list = json.load(f)

df_clinical = pd.DataFrame(clinical_list)
df_mutation = pd.DataFrame(mutation_list)

# Extract Barcode
def extract_barcode(desc):
    match = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', desc)
    if match:
        return match.group(1)
    return None

df_clinical['Barcode'] = df_clinical['Patient_description'].apply(extract_barcode)

# Filter valid barcodes and histology
df_clinical = df_clinical.dropna(subset=['Barcode', 'icd_o_3_histology'])
df_clinical = df_clinical[df_clinical['icd_o_3_histology'] != 'None']

# Mutation Data
mutated_barcodes = set(df_mutation['ParticipantBarcode'].unique())
df_clinical['has_CDH1'] = df_clinical['Barcode'].apply(lambda x: 1 if x in mutated_barcodes else 0)

# Contingency Table
contingency_table = pd.crosstab(df_clinical['icd_o_3_histology'], df_clinical['has_CDH1'])

# Filter rows with <= 10 total
row_totals = contingency_table.sum(axis=1)
valid_rows = row_totals[row_totals > 10].index
contingency_table_filtered = contingency_table.loc[valid_rows]

# Check if we have enough rows (>= 2) for Chi-square
if len(contingency_table_filtered) < 2:
    result_str = "Not enough categories (>= 2) after filtering."
    chi2 = None
else:
    # Calculate Chi-square
    observed = contingency_table_filtered.values
    total_obs = observed.sum()
    row_sums = observed.sum(axis=1)
    col_sums = observed.sum(axis=0)

    chi2 = 0.0
    for i in range(len(row_sums)):
        for j in range(len(col_sums)):
            expected = (row_sums[i] * col_sums[j]) / total_obs
            if expected > 0:
                o = observed[i, j]
                chi2 += ((o - expected) ** 2) / expected
    result_str = f"{chi2:.4f}"

print("__RESULT__:")
print(json.dumps({
    "chi_square_statistic": chi2,
    "contingency_table": contingency_table_filtered.to_dict(),
    "row_totals": row_totals.to_dict(),
    "filtered_rows": list(valid_rows)
}))"""

env_args = {'var_function-call-1879606401748114136': ['clinical_info'], 'var_function-call-6498945298744507928': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_function-call-1923847231424452402': [{'Patient_description': "Patient TCGA-DK-A6AW, registered under UUID 01C815BA-7BDA-4F7E-865C-0C5776FEBF2C, belongs to the Bladder urothelial carcinoma cohort. This MALE patient's vital status is Alive.", 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'Patient_description': 'In the Bladder urothelial carcinoma dataset, patient TCGA-GD-A3OQ (UUID 2E85C30C-C4C4-4096-9EEF-4EB2C7D991A3) is recorded as a MALE with vital status: Alive.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'Patient_description': 'The individual with barcode TCGA-CF-A47W and UUID 122FC134-8915-47DB-96C9-AB1853C3CD18 is a MALE case of Bladder urothelial carcinoma, documented with vital status = Alive.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'Patient_description': 'Patient TCGA-CF-A3MF (MALE, UUID 1E308B12-0590-4DAE-94D0-A539FCF25DF7) is enrolled in the study of Bladder urothelial carcinoma. Vital status: Alive.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'Patient_description': 'Case DE810AF0-4C18-4E8F-9836-F8ABC425E3EB, linked to barcode TCGA-DK-A2I6, corresponds to a MALE patient diagnosed with Bladder urothelial carcinoma, with vital status Alive.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}], 'var_function-call-16649102306215394573': 'file_storage/function-call-16649102306215394573.json', 'var_function-call-12588489646648170295': 'file_storage/function-call-12588489646648170295.json', 'var_function-call-6724641094032064270': {'chi_square_statistic': 0.0, 'contingency_table': {'0': {'Muscle invasive urothelial carcinoma (pT2 or above)': 102}, '1': {'Muscle invasive urothelial carcinoma (pT2 or above)': 6}}, 'row_totals': {'Muscle invasive urothelial carcinoma (pT2 or above)': 108}, 'filtered_types': ['Muscle invasive urothelial carcinoma (pT2 or above)']}, 'var_function-call-6327971718423017420': {'Muscle invasive urothelial carcinoma (pT2 or above)': 108}, 'var_function-call-1427247882582797301': [], 'var_function-call-2017820308091258300': {'histological_type': {'Muscle invasive urothelial carcinoma (pT2 or above)': 108}, 'icd_o_3_histology': {}, 'histological_type_other': {}}, 'var_function-call-17936447124014648086': 'file_storage/function-call-17936447124014648086.json', 'var_function-call-8113958776897834218': 'file_storage/function-call-8113958776897834218.json'}

exec(code, env_args)
