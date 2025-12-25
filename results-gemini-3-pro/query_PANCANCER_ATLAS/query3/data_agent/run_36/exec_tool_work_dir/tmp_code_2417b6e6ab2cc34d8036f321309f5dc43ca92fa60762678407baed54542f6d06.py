code = """import json
import pandas as pd
import re

# Load clinical data
with open(locals()['var_function-call-14196932171295168847'], 'r') as f:
    clinical_data = json.load(f)

# Load mutation data
with open(locals()['var_function-call-9919463818421012845'], 'r') as f:
    mutation_data = json.load(f)

# Extract barcodes from mutation data
mutated_barcodes = set(item['ParticipantBarcode'] for item in mutation_data)

# Process clinical data
patients = []
for entry in clinical_data:
    desc = entry['Patient_description']
    hist_type = entry['histological_type']
    
    # Extract barcode (TCGA-XX-XXXX)
    match = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', desc)
    if match:
        barcode = match.group(1)
        
        # Check if histological type is valid (known)
        if hist_type and hist_type.lower() not in ['[not applicable]', 'none', 'unknown', '[unknown]']:
            # Determine mutation status
            is_mutated = barcode in mutated_barcodes
            
            patients.append({
                'barcode': barcode,
                'histological_type': hist_type,
                'has_mutation': is_mutated
            })

df = pd.DataFrame(patients)

# Filter categories with marginal totals <= 10
# Marginal totals usually refer to the counts of histological types (rows) or mutation status (cols).
# Since we want to assess association between histological types and mutation, we likely exclude rare histological types.
type_counts = df['histological_type'].value_counts()
valid_types = type_counts[type_counts > 10].index.tolist()

df_filtered = df[df['histological_type'].isin(valid_types)]

# Create contingency table
contingency_table = pd.crosstab(df_filtered['histological_type'], df_filtered['has_mutation'])

# Calculate Chi-square
# formula: sum((O - E)^2 / E)
chi2 = 0
grand_total = contingency_table.values.sum()
row_totals = contingency_table.sum(axis=1)
col_totals = contingency_table.sum(axis=0)

if grand_total > 0 and not contingency_table.empty:
    for r_idx, row_label in enumerate(contingency_table.index):
        for c_idx, col_label in enumerate(contingency_table.columns):
            observed = contingency_table.iloc[r_idx, c_idx]
            expected = (row_totals.iloc[r_idx] * col_totals.iloc[c_idx]) / grand_total
            if expected > 0:
                chi2 += (observed - expected)**2 / expected

print("__RESULT__:")
print(json.dumps({
    "chi_square_statistic": chi2,
    "contingency_table": contingency_table.to_dict(),
    "filtered_types": valid_types,
    "total_patients": int(grand_total)
}))"""

env_args = {'var_function-call-11173919191599259187': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_function-call-2060280981035903930': [{'tumor_tissue_site': 'Chest - Breast'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Small Intestines'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum|Retroperitoneum/Upper abdominal - Small Intestines|Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Intraabdominal'}, {'tumor_tissue_site': 'Superficial Trunk - Back'}, {'tumor_tissue_site': 'Chest - Chest wall'}, {'tumor_tissue_site': 'Choroid|Ciliary body|Iris'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_tissue_site': 'Rectum'}, {'tumor_tissue_site': 'Chest - Mediastinum'}, {'tumor_tissue_site': 'Gynecological - Uterus|Gynecological - Other (please specify'}, {'tumor_tissue_site': 'Esophagus'}, {'tumor_tissue_site': 'Extra-adrenal Site'}, {'tumor_tissue_site': 'Omentum'}, {'tumor_tissue_site': 'Endometrial'}, {'tumor_tissue_site': 'Chest - Other (please specify'}, {'tumor_tissue_site': 'Chest - Lung/pleura'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum'}, {'tumor_tissue_site': 'Gynecological - Uterus'}, {'tumor_tissue_site': 'Colon'}, {'tumor_tissue_site': 'None'}, {'tumor_tissue_site': 'Lung'}, {'tumor_tissue_site': 'Choroid|Ciliary body'}, {'tumor_tissue_site': 'Upper Extremity - Upper arm/elbow'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Kidney|Retroperitoneum/Upper abdominal - Liver|Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_tissue_site': 'Other  Specify'}, {'tumor_tissue_site': 'Head and Neck - Neck|Head and Neck - Other (please specify'}, {'tumor_tissue_site': 'Gynecological - Ovary'}, {'tumor_tissue_site': 'Lower Extremity - Lower leg/calf'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Other (please specify'}, {'tumor_tissue_site': 'Uterus'}, {'tumor_tissue_site': 'Extremities'}, {'tumor_tissue_site': 'Thyroid'}, {'tumor_tissue_site': 'Cervical'}, {'tumor_tissue_site': 'Choroid'}, {'tumor_tissue_site': 'Ovary'}, {'tumor_tissue_site': 'Upper Extremity - Shoulder/axilla'}, {'tumor_tissue_site': 'Peritoneum ovary'}, {'tumor_tissue_site': 'Stomach'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Pelvic'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Bladder'}, {'tumor_tissue_site': 'Head and Neck - Head'}, {'tumor_tissue_site': 'Kidney'}, {'tumor_tissue_site': 'Head and Neck'}, {'tumor_tissue_site': 'Lower Extremity - Other (please specify'}, {'tumor_tissue_site': 'Pancreas'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Pelvic|Gynecological - Uterus'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum|Retroperitoneum/Upper abdominal - Intraabdominal|Lower abdominal/Pelvic - Pelvic'}, {'tumor_tissue_site': 'Extremities|Extremities'}, {'tumor_tissue_site': 'Pleura'}, {'tumor_tissue_site': 'Brain'}, {'tumor_tissue_site': 'Anterior Mediastinum'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Colon'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Gastric'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Kidney'}, {'tumor_tissue_site': 'Testes'}, {'tumor_tissue_site': 'Trunk'}, {'tumor_tissue_site': 'Breast'}, {'tumor_tissue_site': 'Extremities|Trunk'}, {'tumor_tissue_site': 'Prostate'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Spermatic Cord'}, {'tumor_tissue_site': 'Head and Neck - Other (please specify'}, {'tumor_tissue_site': 'Head and Neck - Head|Chest - Chest wall'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Pancreas'}, {'tumor_tissue_site': 'Lower Extremity - Thigh/knee'}, {'tumor_tissue_site': 'Trunk|[Not Available]'}, {'tumor_tissue_site': 'Central nervous system'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Intraabdominal|Retroperitoneum/Upper abdominal - Small Intestines'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Intraabdominal|Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_tissue_site': 'Adrenal gland'}, {'tumor_tissue_site': 'Bile duct'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Small Intestines|Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum|Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_tissue_site': 'Superficial Trunk - Buttock'}, {'tumor_tissue_site': 'Lower Extremity - Groin'}, {'tumor_tissue_site': 'Liver'}, {'tumor_tissue_site': 'Trunk|Extremities'}, {'tumor_tissue_site': 'Adrenal'}, {'tumor_tissue_site': 'Bladder'}, {'tumor_tissue_site': 'Thymus'}, {'tumor_tissue_site': '[Unknown]'}, {'tumor_tissue_site': 'Gynecological - Uterus|Gynecological - Cervix'}, {'tumor_tissue_site': 'Superficial Trunk - Abdominal wall'}, {'tumor_tissue_site': 'Superficial Trunk - Flank'}, {'tumor_tissue_site': 'Lower Extremity - Foot/ankle'}], 'var_function-call-7177789943032943722': [{'Patient_description': "Patient TCGA-DK-A6AW, registered under UUID 01C815BA-7BDA-4F7E-865C-0C5776FEBF2C, belongs to the Bladder urothelial carcinoma cohort. This MALE patient's vital status is Alive.", 'tumor_tissue_site': 'Bladder', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'Patient_description': 'In the Bladder urothelial carcinoma dataset, patient TCGA-GD-A3OQ (UUID 2E85C30C-C4C4-4096-9EEF-4EB2C7D991A3) is recorded as a MALE with vital status: Alive.', 'tumor_tissue_site': 'Bladder', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'Patient_description': 'The individual with barcode TCGA-CF-A47W and UUID 122FC134-8915-47DB-96C9-AB1853C3CD18 is a MALE case of Bladder urothelial carcinoma, documented with vital status = Alive.', 'tumor_tissue_site': 'Bladder', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'Patient_description': 'Patient TCGA-CF-A3MF (MALE, UUID 1E308B12-0590-4DAE-94D0-A539FCF25DF7) is enrolled in the study of Bladder urothelial carcinoma. Vital status: Alive.', 'tumor_tissue_site': 'Bladder', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'Patient_description': 'Case DE810AF0-4C18-4E8F-9836-F8ABC425E3EB, linked to barcode TCGA-DK-A2I6, corresponds to a MALE patient diagnosed with Bladder urothelial carcinoma, with vital status Alive.', 'tumor_tissue_site': 'Bladder', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}], 'var_function-call-2668562209944944197': [{'Patient_description': 'Clinical entry D13FB44B-291B-4EA4-920C-142DAA8D1989 identifies patient TCGA-AC-A5EH, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.', 'tumor_tissue_site': 'Breast', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Record 09A5E9FD-D816-4F8C-BAA9-0E40BA607B16 refers to patient TCGA-LL-A7SZ, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'tumor_tissue_site': 'Breast', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': "Patient TCGA-AN-A0FY, registered under UUID de75d0b9-0f47-4732-8df5-05c350cfcd32, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive.", 'tumor_tissue_site': 'Breast', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Patient TCGA-AC-A2FB (UUID 02BBB632-0F7F-439D-B8F0-C86A06237424) is a FEMALE diagnosed with Breast invasive carcinoma. Current vital status: Alive.', 'tumor_tissue_site': 'Breast', 'histological_type': 'Infiltrating Lobular Carcinoma'}, {'Patient_description': 'The individual with barcode TCGA-AO-A1KR and UUID b7f74ae1-6f58-447c-be50-a7666eb19d9a is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'tumor_tissue_site': 'Breast', 'histological_type': 'Infiltrating Ductal Carcinoma'}], 'var_function-call-14196932171295168847': 'file_storage/function-call-14196932171295168847.json', 'var_function-call-9919463818421012845': 'file_storage/function-call-9919463818421012845.json'}

exec(code, env_args)
