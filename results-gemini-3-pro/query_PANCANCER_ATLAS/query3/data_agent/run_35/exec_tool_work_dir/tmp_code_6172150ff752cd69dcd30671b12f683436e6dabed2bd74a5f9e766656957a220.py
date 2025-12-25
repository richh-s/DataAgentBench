code = """import pandas as pd
import json
import re
import scipy.stats as stats

# Load data
with open(locals()['var_function-call-10196676881347648924'], 'r') as f:
    mutation_data = json.load(f)
with open(locals()['var_function-call-17960985335170871815'], 'r') as f:
    clinical_data = json.load(f)

# Convert to DataFrame
df_mut = pd.DataFrame(mutation_data)
df_clin = pd.DataFrame(clinical_data)

# Extract CDH1 mutated samples
# Mutation_Data has ParticipantBarcode
mutated_patients = set(df_mut['ParticipantBarcode'].unique())

# Parse clinical info
# Extract Barcode, Gender, Cancer Type from Patient_description
# Patterns:
# "patient TCGA-XX-XXXX"
# "FEMALE" or "MALE"
# "Breast invasive carcinoma" or "Bladder urothelial carcinoma"

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
        
    # Extract Cohort (Cancer Type)
    cohort = None
    if 'Breast invasive carcinoma' in desc:
        cohort = 'Breast invasive carcinoma'
    elif 'Bladder urothelial carcinoma' in desc:
        cohort = 'Bladder urothelial carcinoma'
    elif 'Brain lower grade glioma' in desc:
        cohort = 'Brain lower grade glioma'
    # Add others if needed
    
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
print(df_parsed.groupby(['Cohort', 'Gender']).size())

# Decide Cohort
# Hint: BRCA means Bladder urothelial carcinoma.
# But check if Female Bladder is viable.
target_cohort = 'Bladder urothelial carcinoma'
target_df = df_parsed[(df_parsed['Cohort'] == target_cohort) & (df_parsed['Gender'] == 'FEMALE')]

if len(target_df) < 10:
    print(f"Warning: Only {len(target_df)} female Bladder patients. Switching to Breast invasive carcinoma.")
    target_cohort = 'Breast invasive carcinoma'
    target_df = df_parsed[(df_parsed['Cohort'] == target_cohort) & (df_parsed['Gender'] == 'FEMALE')]

print(f"Selected Cohort: {target_cohort}, N={len(target_df)}")

# Filter Histological Type
# "excluding categories with marginal totals less than or equal to 10"
# "only focusing on patients with known histological types"
target_df = target_df[target_df['HistologicalType'].notna() & (target_df['HistologicalType'] != 'None')]

# Mark mutation status
target_df['CDH1_Mutation'] = target_df['ParticipantBarcode'].apply(lambda x: 1 if x in mutated_patients else 0)

# Filter categories with <= 10 patients
hist_counts = target_df['HistologicalType'].value_counts()
valid_hist_types = hist_counts[hist_counts > 10].index.tolist()
print("Valid Histological Types:", valid_hist_types)

final_df = target_df[target_df['HistologicalType'].isin(valid_hist_types)]

# Create Contingency Table
contingency_table = pd.crosstab(final_df['HistologicalType'], final_df['CDH1_Mutation'])
print("Contingency Table:")
print(contingency_table)

# Calculate Chi-square
if contingency_table.empty:
    result = "No data for Chi-square"
else:
    chi2, p, dof, ex = stats.chi2_contingency(contingency_table)
    result = {
        "chi2": chi2,
        "p_value": p,
        "dof": dof,
        "expected": ex.tolist()
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-3182473022121965884': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_function-call-10196676881347648924': 'file_storage/function-call-10196676881347648924.json', 'var_function-call-17960985335170871815': 'file_storage/function-call-17960985335170871815.json'}

exec(code, env_args)
