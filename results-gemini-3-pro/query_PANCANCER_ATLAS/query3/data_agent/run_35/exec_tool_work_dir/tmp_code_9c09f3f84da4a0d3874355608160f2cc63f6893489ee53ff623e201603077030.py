code = """import pandas as pd
import json
import re

# Load data
with open(locals()['var_function-call-10196676881347648924'], 'r') as f:
    mutation_data = json.load(f)
with open(locals()['var_function-call-17960985335170871815'], 'r') as f:
    clinical_data = json.load(f)

df_mut = pd.DataFrame(mutation_data)
df_clin = pd.DataFrame(clinical_data)

# Extract CDH1 mutated patients (ParticipantBarcode is 12 chars)
mutated_patients = set(df_mut['ParticipantBarcode'].apply(lambda x: x[:12]).unique())

# Parse clinical info
parsed_records = []
for _, row in df_clin.iterrows():
    desc = row.get('Patient_description', '')
    hist_type = row.get('histological_type')
    
    # Extract Barcode
    barcode_match = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', desc)
    barcode = barcode_match.group(1) if barcode_match else None
    
    # Extract Gender
    gender = None
    if 'FEMALE' in desc:
        gender = 'FEMALE'
    elif 'MALE' in desc:
        gender = 'MALE'
        
    # Extract Cohort
    cohort = None
    if 'Breast invasive carcinoma' in desc:
        cohort = 'Breast invasive carcinoma'
    elif 'Bladder urothelial carcinoma' in desc:
        cohort = 'Bladder urothelial carcinoma'
    elif 'Brain lower grade glioma' in desc:
        cohort = 'Brain lower grade glioma'
        
    if barcode and gender and cohort:
        parsed_records.append({
            'ParticipantBarcode': barcode,
            'Gender': gender,
            'Cohort': cohort,
            'HistologicalType': hist_type
        })

df_parsed = pd.DataFrame(parsed_records)

# Check counts
print("Counts by Cohort and Gender:")
# print(df_parsed.groupby(['Cohort', 'Gender']).size()) # Can't print to stdout effectively if I want JSON output at end.

# Logic to select Cohort
# "BRCA means Bladder urothelial carcinoma"
# Check Female Bladder count
bladder_female_count = len(df_parsed[(df_parsed['Cohort'] == 'Bladder urothelial carcinoma') & (df_parsed['Gender'] == 'FEMALE')])
breast_female_count = len(df_parsed[(df_parsed['Cohort'] == 'Breast invasive carcinoma') & (df_parsed['Gender'] == 'FEMALE')])

# Decision:
# If hint is strict: use Bladder.
# But if Bladder count is too small to be meaningful (e.g., < 10) and Breast is large, use Breast.
# User query: "female BRCA patients".
# If the hint defines BRCA = Bladder, then query = "female Bladder patients".
# I will use Bladder if count >= 10. Else Breast.
if bladder_female_count >= 10:
    selected_cohort = 'Bladder urothelial carcinoma'
else:
    selected_cohort = 'Breast invasive carcinoma'

# Override: The hint is very explicit. "BRCA means Bladder urothelial carcinoma". 
# But "female BRCA" usually means Breast.
# Let's check if the result makes sense.
# I will calculate for the selected cohort.
# NOTE: If I select Bladder and the count is small, the chi-square might be invalid or 0.
# If the user *intended* Breast (ignoring the hint or hint is for acronym mapping only), using Bladder is wrong.
# However, I must follow provided hints.
# Let's proceed with Bladder if sufficient data.

target_df = df_parsed[(df_parsed['Cohort'] == selected_cohort) & (df_parsed['Gender'] == 'FEMALE')]

# Filter Histological Types
target_df = target_df[target_df['HistologicalType'].notna() & (target_df['HistologicalType'] != 'None')]

# Mark Mutation
target_df['CDH1_Mutation'] = target_df['ParticipantBarcode'].apply(lambda x: 1 if x in mutated_patients else 0)

# Filter categories with <= 10 patients
hist_counts = target_df['HistologicalType'].value_counts()
valid_hist_types = hist_counts[hist_counts > 10].index.tolist()
final_df = target_df[target_df['HistologicalType'].isin(valid_hist_types)]

# Contingency Table
# Rows: Histological Type
# Cols: Mutation Status (0, 1)
contingency = pd.crosstab(final_df['HistologicalType'], final_df['CDH1_Mutation'])

# Calculate Chi-square manually
chi2 = 0.0
grand_total = contingency.values.sum()
if grand_total > 0 and contingency.shape[0] > 1 and contingency.shape[1] > 1:
    row_totals = contingency.sum(axis=1)
    col_totals = contingency.sum(axis=0)
    
    for idx in contingency.index:
        for col in contingency.columns:
            O = contingency.loc[idx, col]
            E = (row_totals[idx] * col_totals[col]) / grand_total
            if E > 0:
                chi2 += (O - E)**2 / E

result = {
    "selected_cohort": selected_cohort,
    "bladder_female_count": bladder_female_count,
    "breast_female_count": breast_female_count,
    "valid_histological_types": valid_hist_types,
    "chi_square_statistic": chi2
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-3182473022121965884': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_function-call-10196676881347648924': 'file_storage/function-call-10196676881347648924.json', 'var_function-call-17960985335170871815': 'file_storage/function-call-17960985335170871815.json'}

exec(code, env_args)
