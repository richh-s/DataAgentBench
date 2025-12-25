code = """import pandas as pd
import json
import re

# Load data
with open(locals()['var_function-call-3155819053312316145'], 'r') as f:
    clinical_data = json.load(f)
with open(locals()['var_function-call-15954805365380015615'], 'r') as f:
    mutation_data = json.load(f)

# Process Clinical Data
clinical_rows = []
for entry in clinical_data:
    desc = entry.get('Patient_description', '')
    hist_type = entry.get('histological_type', 'Unknown')
    
    # Extract Barcode
    # Pattern: TCGA-XX-XXXX
    match = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', desc)
    if match:
        barcode = match.group(1)
        clinical_rows.append({'ParticipantBarcode': barcode, 'histological_type': hist_type})

df_clinical = pd.DataFrame(clinical_rows)

# Process Mutation Data
# We only care if the patient has a CDH1 mutation (PASS filter was already applied in query)
# "presence of CDH1 gene mutations" -> binary
mutated_barcodes = set(item['ParticipantBarcode'] for item in mutation_data)

# Merge
df_clinical['has_cdh1_mutation'] = df_clinical['ParticipantBarcode'].apply(lambda x: x in mutated_barcodes)

# Filter Histological Types
# "known histological types" -> exclude 'Unknown', 'None', 'Other specify', '[Not Available]'
# Also prompt: "excluding categories with marginal totals less than or equal to 10"
# We'll treat 'categories' as Histological Types.

# Clean up types slightly if needed?
# Let's inspect unique types first in the code logic.
# We will filter out "explicitly unknown" types first.
unknown_indicators = ['Unknown', 'None', 'Other  specify', '[Not Available]', '[Unknown]', 'Other']
df_clinical = df_clinical[~df_clinical['histological_type'].isin(unknown_indicators)]

# Calculate marginal totals (row counts)
type_counts = df_clinical['histological_type'].value_counts()
valid_types = type_counts[type_counts > 10].index.tolist()

df_analysis = df_clinical[df_clinical['histological_type'].isin(valid_types)]

# Create Contingency Table
# Rows: Histological Type
# Cols: Mutation Presence (True/False)
contingency_table = pd.crosstab(df_analysis['histological_type'], df_analysis['has_cdh1_mutation'])

# Rename columns for clarity
contingency_table.columns = ['WildType', 'Mutated']

# Calculate Chi-Square
# Formula: χ² = Σ (Oij - Eij)² / Eij
# Grand Total
grand_total = contingency_table.sum().sum()

# Row Totals
row_totals = contingency_table.sum(axis=1)
# Col Totals
col_totals = contingency_table.sum(axis=0)

chi2 = 0
details = []

for idx, row in contingency_table.iterrows():
    for col in contingency_table.columns:
        observed = row[col]
        expected = (row_totals[idx] * col_totals[col]) / grand_total
        contribution = ((observed - expected) ** 2) / expected
        chi2 += contribution
        details.append({
            'type': idx,
            'mutation_status': col,
            'observed': observed,
            'expected': expected,
            'contribution': contribution
        })

result = {
    'chi_square_statistic': chi2,
    'contingency_table': contingency_table.to_dict(),
    'degrees_of_freedom': (len(row_totals) - 1) * (len(col_totals) - 1),
    'marginal_counts': type_counts.to_dict()
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-13556895125532411285': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_function-call-16017009830547384919': [{'tumor_tissue_site': 'Chest - Breast', 'count': '1'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Small Intestines', 'count': '2'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum|Retroperitoneum/Upper abdominal - Small Intestines|Retroperitoneum/Upper abdominal - Other (please specify', 'count': '1'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Intraabdominal', 'count': '3'}, {'tumor_tissue_site': 'Superficial Trunk - Back', 'count': '5'}, {'tumor_tissue_site': 'Chest - Chest wall', 'count': '7'}, {'tumor_tissue_site': 'Choroid|Ciliary body|Iris', 'count': '2'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Other (please specify', 'count': '2'}, {'tumor_tissue_site': 'Rectum', 'count': '156'}, {'tumor_tissue_site': 'Chest - Mediastinum', 'count': '1'}, {'tumor_tissue_site': 'Gynecological - Uterus|Gynecological - Other (please specify', 'count': '1'}, {'tumor_tissue_site': 'Esophagus', 'count': '183'}, {'tumor_tissue_site': 'Extra-adrenal Site', 'count': '32'}, {'tumor_tissue_site': 'Omentum', 'count': '3'}, {'tumor_tissue_site': 'Endometrial', 'count': '530'}, {'tumor_tissue_site': 'Chest - Other (please specify', 'count': '2'}, {'tumor_tissue_site': 'Chest - Lung/pleura', 'count': '2'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum', 'count': '69'}, {'tumor_tissue_site': 'Gynecological - Uterus', 'count': '25'}, {'tumor_tissue_site': 'Colon', 'count': '442'}, {'tumor_tissue_site': 'None', 'count': '100'}, {'tumor_tissue_site': 'Lung', 'count': '1004'}, {'tumor_tissue_site': 'Choroid|Ciliary body', 'count': '22'}, {'tumor_tissue_site': 'Upper Extremity - Upper arm/elbow', 'count': '5'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Kidney|Retroperitoneum/Upper abdominal - Liver|Retroperitoneum/Upper abdominal - Other (please specify', 'count': '1'}, {'tumor_tissue_site': 'Other  Specify', 'count': '14'}, {'tumor_tissue_site': 'Head and Neck - Neck|Head and Neck - Other (please specify', 'count': '1'}, {'tumor_tissue_site': 'Gynecological - Ovary', 'count': '1'}, {'tumor_tissue_site': 'Lower Extremity - Lower leg/calf', 'count': '17'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Other (please specify', 'count': '2'}, {'tumor_tissue_site': 'Uterus', 'count': '57'}, {'tumor_tissue_site': 'Extremities', 'count': '193'}, {'tumor_tissue_site': 'Thyroid', 'count': '503'}, {'tumor_tissue_site': 'Cervical', 'count': '306'}, {'tumor_tissue_site': 'Choroid', 'count': '56'}, {'tumor_tissue_site': 'Ovary', 'count': '579'}, {'tumor_tissue_site': 'Upper Extremity - Shoulder/axilla', 'count': '7'}, {'tumor_tissue_site': 'Peritoneum ovary', 'count': '2'}, {'tumor_tissue_site': 'Stomach', 'count': '440'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Pelvic', 'count': '9'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Bladder', 'count': '1'}, {'tumor_tissue_site': 'Head and Neck - Head', 'count': '1'}, {'tumor_tissue_site': 'Kidney', 'count': '869'}, {'tumor_tissue_site': 'Head and Neck', 'count': '560'}, {'tumor_tissue_site': 'Lower Extremity - Other (please specify', 'count': '4'}, {'tumor_tissue_site': 'Pancreas', 'count': '184'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Pelvic|Gynecological - Uterus', 'count': '2'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum|Retroperitoneum/Upper abdominal - Intraabdominal|Lower abdominal/Pelvic - Pelvic', 'count': '1'}, {'tumor_tissue_site': 'Extremities|Extremities', 'count': '1'}, {'tumor_tissue_site': 'Pleura', 'count': '87'}, {'tumor_tissue_site': 'Brain', 'count': '590'}, {'tumor_tissue_site': 'Anterior Mediastinum', 'count': '27'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Colon', 'count': '4'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Gastric', 'count': '2'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Kidney', 'count': '7'}, {'tumor_tissue_site': 'Testes', 'count': '133'}, {'tumor_tissue_site': 'Trunk', 'count': '169'}, {'tumor_tissue_site': 'Breast', 'count': '1087'}, {'tumor_tissue_site': 'Extremities|Trunk', 'count': '2'}, {'tumor_tissue_site': 'Prostate', 'count': '495'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Spermatic Cord', 'count': '2'}, {'tumor_tissue_site': 'Head and Neck - Other (please specify', 'count': '2'}, {'tumor_tissue_site': 'Head and Neck - Head|Chest - Chest wall', 'count': '1'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Pancreas', 'count': '1'}, {'tumor_tissue_site': 'Lower Extremity - Thigh/knee', 'count': '44'}, {'tumor_tissue_site': 'Trunk|[Not Available]', 'count': '1'}, {'tumor_tissue_site': 'Central nervous system', 'count': '513'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Intraabdominal|Retroperitoneum/Upper abdominal - Small Intestines', 'count': '1'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Intraabdominal|Retroperitoneum/Upper abdominal - Other (please specify', 'count': '1'}, {'tumor_tissue_site': 'Adrenal gland', 'count': '146'}, {'tumor_tissue_site': 'Bile duct', 'count': '36'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Small Intestines|Retroperitoneum/Upper abdominal - Other (please specify', 'count': '1'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum|Retroperitoneum/Upper abdominal - Other (please specify', 'count': '2'}, {'tumor_tissue_site': 'Superficial Trunk - Buttock', 'count': '4'}, {'tumor_tissue_site': 'Lower Extremity - Groin', 'count': '2'}, {'tumor_tissue_site': 'Liver', 'count': '374'}, {'tumor_tissue_site': 'Trunk|Extremities', 'count': '2'}, {'tumor_tissue_site': 'Adrenal', 'count': '91'}, {'tumor_tissue_site': 'Bladder', 'count': '412'}, {'tumor_tissue_site': 'Thymus', 'count': '97'}, {'tumor_tissue_site': '[Unknown]', 'count': '5'}, {'tumor_tissue_site': 'Gynecological - Uterus|Gynecological - Cervix', 'count': '2'}, {'tumor_tissue_site': 'Superficial Trunk - Abdominal wall', 'count': '2'}, {'tumor_tissue_site': 'Superficial Trunk - Flank', 'count': '1'}, {'tumor_tissue_site': 'Lower Extremity - Foot/ankle', 'count': '4'}], 'var_function-call-2074556540388731130': [{'Patient_description': 'Clinical entry D13FB44B-291B-4EA4-920C-142DAA8D1989 identifies patient TCGA-AC-A5EH, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.'}, {'Patient_description': 'Record 09A5E9FD-D816-4F8C-BAA9-0E40BA607B16 refers to patient TCGA-LL-A7SZ, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.'}, {'Patient_description': "Patient TCGA-AN-A0FY, registered under UUID de75d0b9-0f47-4732-8df5-05c350cfcd32, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive."}, {'Patient_description': 'Patient TCGA-AC-A2FB (UUID 02BBB632-0F7F-439D-B8F0-C86A06237424) is a FEMALE diagnosed with Breast invasive carcinoma. Current vital status: Alive.'}, {'Patient_description': 'The individual with barcode TCGA-AO-A1KR and UUID b7f74ae1-6f58-447c-be50-a7666eb19d9a is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.'}], 'var_function-call-12253099597288388766': [{'Patient_description': "Patient TCGA-DK-A6AW, registered under UUID 01C815BA-7BDA-4F7E-865C-0C5776FEBF2C, belongs to the Bladder urothelial carcinoma cohort. This MALE patient's vital status is Alive."}, {'Patient_description': 'In the Bladder urothelial carcinoma dataset, patient TCGA-GD-A3OQ (UUID 2E85C30C-C4C4-4096-9EEF-4EB2C7D991A3) is recorded as a MALE with vital status: Alive.'}, {'Patient_description': 'The individual with barcode TCGA-CF-A47W and UUID 122FC134-8915-47DB-96C9-AB1853C3CD18 is a MALE case of Bladder urothelial carcinoma, documented with vital status = Alive.'}, {'Patient_description': 'Patient TCGA-CF-A3MF (MALE, UUID 1E308B12-0590-4DAE-94D0-A539FCF25DF7) is enrolled in the study of Bladder urothelial carcinoma. Vital status: Alive.'}, {'Patient_description': 'Case DE810AF0-4C18-4E8F-9836-F8ABC425E3EB, linked to barcode TCGA-DK-A2I6, corresponds to a MALE patient diagnosed with Bladder urothelial carcinoma, with vital status Alive.'}], 'var_function-call-16341322148222736229': [{'count': '108'}], 'var_function-call-3155819053312316145': 'file_storage/function-call-3155819053312316145.json', 'var_function-call-15954805365380015615': 'file_storage/function-call-15954805365380015615.json'}

exec(code, env_args)
