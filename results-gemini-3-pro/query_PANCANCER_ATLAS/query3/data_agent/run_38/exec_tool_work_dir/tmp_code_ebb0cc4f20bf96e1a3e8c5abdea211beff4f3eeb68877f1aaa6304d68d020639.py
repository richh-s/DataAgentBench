code = """import pandas as pd
import json
import re

# Load data
clinical_path = locals()['var_function-call-2657158926528533153']
mutation_path = locals()['var_function-call-13899398936594413042']

with open(clinical_path, 'r') as f:
    clinical_data = json.load(f)

with open(mutation_path, 'r') as f:
    mutation_data = json.load(f)

# Process Clinical Data
clinical_rows = []
for entry in clinical_data:
    desc = entry.get('Patient_description', '')
    histo = entry.get('histological_type', '')
    
    # Extract Barcode
    # Pattern: TCGA-XX-XXXX
    match = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', desc)
    if match:
        barcode = match.group(1)
        # Filter unknown histological types
        if histo and histo.lower() != 'none':
            clinical_rows.append({'ParticipantBarcode': barcode, 'histological_type': histo})

df_clinical = pd.DataFrame(clinical_rows)

# Process Mutation Data
mutated_barcodes = set(item['ParticipantBarcode'] for item in mutation_data)

# Merge
df_clinical['CDH1_Mutation'] = df_clinical['ParticipantBarcode'].apply(lambda x: 'Mutated' if x in mutated_barcodes else 'WildType')

# Create Contingency Table
contingency_table = pd.crosstab(df_clinical['histological_type'], df_clinical['CDH1_Mutation'])

# Filter by marginal totals
# "excluding categories with marginal totals less than or equal to 10"
# Assuming "categories" refers to histological types (rows)
# Row sums
row_sums = contingency_table.sum(axis=1)
filtered_table = contingency_table[row_sums > 10]

# Calculate Chi-Square
# Formula: sum((O - E)^2 / E)
grand_total = filtered_table.values.sum()
col_totals = filtered_table.sum(axis=0)
row_totals = filtered_table.sum(axis=1)

chi2 = 0.0
for i, row_idx in enumerate(filtered_table.index):
    for j, col_name in enumerate(filtered_table.columns):
        O_ij = filtered_table.loc[row_idx, col_name]
        row_tot = row_totals[row_idx]
        col_tot = col_totals[col_name]
        E_ij = (row_tot * col_tot) / grand_total
        
        if E_ij > 0:
            chi2 += ((O_ij - E_ij) ** 2) / E_ij

result = {
    "contingency_table": filtered_table.to_dict(),
    "chi_square_statistic": chi2,
    "row_totals": row_totals.to_dict()
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-3710461838735960508': ['clinical_info'], 'var_function-call-2156815956622763348': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_function-call-14811967456957168737': [{'dataset': 'None', 'count': '9386'}, {'dataset': 'Kidney Chromophobe', 'count': '9'}, {'dataset': 'Brain lower grade glioma', 'count': '60'}, {'dataset': 'Lung adenocarcinoma', 'count': '58'}, {'dataset': 'Mesothelioma', 'count': '16'}, {'dataset': 'Colon adenocarcinoma', 'count': '69'}, {'dataset': 'Uveal Melanoma', 'count': '10'}, {'dataset': 'Thymoma', 'count': '20'}, {'dataset': 'Kidney renal papillary cell carcinoma', 'count': '34'}, {'dataset': 'Sarcoma', 'count': '32'}, {'dataset': 'Lymphoid Neoplasm Diffuse Large B-cell Lymphoma', 'count': '8'}, {'dataset': 'Liver hepatocellular carcinoma', 'count': '45'}, {'dataset': 'Head and Neck squamous cell carcinoma', 'count': '62'}, {'dataset': 'Lung squamous cell carcinoma', 'count': '50'}, {'dataset': 'Cholangiocarcinoma', 'count': '3'}, {'dataset': 'Pheochromocytoma and Paraganglioma', 'count': '22'}, {'dataset': 'Breast invasive carcinoma', 'count': '140'}, {'dataset': 'Esophageal carcinoma', 'count': '23'}, {'dataset': 'Uterine Carcinosarcoma', 'count': '5'}, {'dataset': 'Pancreatic adenocarcinoma', 'count': '17'}, {'dataset': 'Thyroid carcinoma', 'count': '68'}, {'dataset': 'Ovarian serous cystadenocarcinoma', 'count': '79'}, {'dataset': 'Cervical squamous cell carcinoma and endocervical adenocarcinoma', 'count': '41'}, {'dataset': 'Bladder urothelial carcinoma', 'count': '60'}, {'dataset': 'Testicular Germ Cell Tumors', 'count': '22'}, {'dataset': 'Kidney renal clear cell carcinoma', 'count': '67'}, {'dataset': 'Uterine Corpus Endometrial Carcinoma', 'count': '86'}, {'dataset': 'Stomach adenocarcinoma', 'count': '54'}, {'dataset': 'Skin Cutaneous Melanoma', 'count': '52'}, {'dataset': 'Rectum adenocarcinoma', 'count': '16'}, {'dataset': 'Adrenocortical carcinoma', 'count': '9'}, {'dataset': 'Glioblastoma multiforme', 'count': '74'}, {'dataset': 'Prostate adenocarcinoma', 'count': '64'}], 'var_function-call-2459900518048886580': [{'dataset': 'None', 'count': '4884'}, {'dataset': 'Kidney Chromophobe', 'count': '5'}, {'dataset': 'Brain lower grade glioma', 'count': '32'}, {'dataset': 'Lung adenocarcinoma', 'count': '29'}, {'dataset': 'Breast invasive carcinoma', 'count': '140'}, {'dataset': 'Mesothelioma', 'count': '1'}, {'dataset': 'Esophageal carcinoma', 'count': '4'}, {'dataset': 'Uterine Carcinosarcoma', 'count': '5'}, {'dataset': 'Colon adenocarcinoma', 'count': '32'}, {'dataset': 'Pancreatic adenocarcinoma', 'count': '9'}, {'dataset': 'Thyroid carcinoma', 'count': '49'}, {'dataset': 'Ovarian serous cystadenocarcinoma', 'count': '79'}, {'dataset': 'Uveal Melanoma', 'count': '4'}, {'dataset': 'Thymoma', 'count': '8'}, {'dataset': 'Kidney renal papillary cell carcinoma', 'count': '7'}, {'dataset': 'Cervical squamous cell carcinoma and endocervical adenocarcinoma', 'count': '41'}, {'dataset': 'Bladder urothelial carcinoma', 'count': '20'}, {'dataset': 'Kidney renal clear cell carcinoma', 'count': '22'}, {'dataset': 'Uterine Corpus Endometrial Carcinoma', 'count': '86'}, {'dataset': 'Stomach adenocarcinoma', 'count': '19'}, {'dataset': 'Skin Cutaneous Melanoma', 'count': '20'}, {'dataset': 'Sarcoma', 'count': '19'}, {'dataset': 'Lymphoid Neoplasm Diffuse Large B-cell Lymphoma', 'count': '4'}, {'dataset': 'Liver hepatocellular carcinoma', 'count': '13'}, {'dataset': 'Head and Neck squamous cell carcinoma', 'count': '14'}, {'dataset': 'Lung squamous cell carcinoma', 'count': '20'}, {'dataset': 'Cholangiocarcinoma', 'count': '1'}, {'dataset': 'Rectum adenocarcinoma', 'count': '9'}, {'dataset': 'Adrenocortical carcinoma', 'count': '6'}, {'dataset': 'Pheochromocytoma and Paraganglioma', 'count': '13'}, {'dataset': 'Glioblastoma multiforme', 'count': '28'}], 'var_function-call-12458324598549244967': [{'histological_type': 'None', 'count': '1'}, {'histological_type': 'Infiltrating Ductal Carcinoma', 'count': '777'}, {'histological_type': 'Mucinous Carcinoma', 'count': '17'}, {'histological_type': 'Metaplastic Carcinoma', 'count': '8'}, {'histological_type': 'Mixed Histology (please specify)', 'count': '30'}, {'histological_type': 'Infiltrating Lobular Carcinoma', 'count': '201'}, {'histological_type': 'Other  specify', 'count': '46'}, {'histological_type': 'Medullary Carcinoma', 'count': '6'}, {'histological_type': 'Infiltrating Carcinoma NOS', 'count': '1'}], 'var_function-call-10047092852495969868': [{'histological_type': 'None', 'count': '3'}, {'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'count': '409'}], 'var_function-call-2657158926528533153': 'file_storage/function-call-2657158926528533153.json', 'var_function-call-13899398936594413042': 'file_storage/function-call-13899398936594413042.json'}

exec(code, env_args)
