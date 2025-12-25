code = """import json
import pandas as pd
import re
import numpy as np

# Load clinical data
with open(locals()['var_function-call-10951833064531510723'], 'r') as f:
    clinical_data = json.load(f)

# Load molecular data
with open(locals()['var_function-call-16206894195861881261'], 'r') as f:
    molecular_data = json.load(f)

df_clinical = pd.DataFrame(clinical_data)
df_molecular = pd.DataFrame(molecular_data)

# Extract barcode from Patient_description
def extract_barcode(desc):
    match = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', desc)
    if match:
        return match.group(1)
    return None

df_clinical['Barcode'] = df_clinical['Patient_description'].apply(extract_barcode)

# Filter out rows where barcode extraction failed (if any)
df_clinical = df_clinical.dropna(subset=['Barcode'])

# Merge
# Molecular data has ParticipantBarcode. Check if it matches the 12-char format or is longer.
# The preview showed 12-char barcodes in molecular data mostly.
# However, sometimes they have suffix. Let's truncate molecular barcode to 12 chars just in case, 
# or match exactly if they are already 12 chars.
# Preview showed "TCGA-AB-2908".
# Let's check length of molecular barcodes in the dataframe.
df_molecular['Barcode'] = df_molecular['ParticipantBarcode'].apply(lambda x: x[:12])

# Merge on Barcode
merged = pd.merge(df_clinical, df_molecular, on='Barcode', how='inner')

# Calculate log10(normalized_count + 1)
merged['normalized_count'] = pd.to_numeric(merged['normalized_count'], errors='coerce')
merged = merged.dropna(subset=['normalized_count']) # Drop invalid expression values
merged['log10_expression'] = np.log10(merged['normalized_count'] + 1)

# Group by histological_type
result_df = merged.groupby('histological_type')['log10_expression'].mean().reset_index()

# Rename columns
result_df.columns = ['histological_type', 'average_log10_expression']

# Round to 4 decimal places
result_df['average_log10_expression'] = result_df['average_log10_expression'].round(4)

# Convert to list of dicts
result = result_df.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-186851494954711175': ['clinical_info'], 'var_function-call-9479945891521333739': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_function-call-7902580598240630417': [{'tumor_tissue_site': 'Chest - Breast'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Small Intestines'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum|Retroperitoneum/Upper abdominal - Small Intestines|Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Intraabdominal'}, {'tumor_tissue_site': 'Superficial Trunk - Back'}, {'tumor_tissue_site': 'Chest - Chest wall'}, {'tumor_tissue_site': 'Choroid|Ciliary body|Iris'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_tissue_site': 'Rectum'}, {'tumor_tissue_site': 'Chest - Mediastinum'}, {'tumor_tissue_site': 'Gynecological - Uterus|Gynecological - Other (please specify'}, {'tumor_tissue_site': 'Esophagus'}, {'tumor_tissue_site': 'Extra-adrenal Site'}, {'tumor_tissue_site': 'Omentum'}, {'tumor_tissue_site': 'Endometrial'}, {'tumor_tissue_site': 'Chest - Other (please specify'}, {'tumor_tissue_site': 'Chest - Lung/pleura'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum'}, {'tumor_tissue_site': 'Gynecological - Uterus'}, {'tumor_tissue_site': 'Colon'}, {'tumor_tissue_site': 'None'}, {'tumor_tissue_site': 'Lung'}, {'tumor_tissue_site': 'Choroid|Ciliary body'}, {'tumor_tissue_site': 'Upper Extremity - Upper arm/elbow'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Kidney|Retroperitoneum/Upper abdominal - Liver|Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_tissue_site': 'Other  Specify'}, {'tumor_tissue_site': 'Head and Neck - Neck|Head and Neck - Other (please specify'}, {'tumor_tissue_site': 'Gynecological - Ovary'}, {'tumor_tissue_site': 'Lower Extremity - Lower leg/calf'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Other (please specify'}, {'tumor_tissue_site': 'Uterus'}, {'tumor_tissue_site': 'Extremities'}, {'tumor_tissue_site': 'Thyroid'}, {'tumor_tissue_site': 'Cervical'}, {'tumor_tissue_site': 'Choroid'}, {'tumor_tissue_site': 'Ovary'}, {'tumor_tissue_site': 'Upper Extremity - Shoulder/axilla'}, {'tumor_tissue_site': 'Peritoneum ovary'}, {'tumor_tissue_site': 'Stomach'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Pelvic'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Bladder'}, {'tumor_tissue_site': 'Head and Neck - Head'}, {'tumor_tissue_site': 'Kidney'}, {'tumor_tissue_site': 'Head and Neck'}, {'tumor_tissue_site': 'Lower Extremity - Other (please specify'}, {'tumor_tissue_site': 'Pancreas'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Pelvic|Gynecological - Uterus'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum|Retroperitoneum/Upper abdominal - Intraabdominal|Lower abdominal/Pelvic - Pelvic'}, {'tumor_tissue_site': 'Extremities|Extremities'}, {'tumor_tissue_site': 'Pleura'}, {'tumor_tissue_site': 'Brain'}, {'tumor_tissue_site': 'Anterior Mediastinum'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Colon'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Gastric'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Kidney'}, {'tumor_tissue_site': 'Testes'}, {'tumor_tissue_site': 'Trunk'}, {'tumor_tissue_site': 'Breast'}, {'tumor_tissue_site': 'Extremities|Trunk'}, {'tumor_tissue_site': 'Prostate'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Spermatic Cord'}, {'tumor_tissue_site': 'Head and Neck - Other (please specify'}, {'tumor_tissue_site': 'Head and Neck - Head|Chest - Chest wall'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Pancreas'}, {'tumor_tissue_site': 'Lower Extremity - Thigh/knee'}, {'tumor_tissue_site': 'Trunk|[Not Available]'}, {'tumor_tissue_site': 'Central nervous system'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Intraabdominal|Retroperitoneum/Upper abdominal - Small Intestines'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Intraabdominal|Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_tissue_site': 'Adrenal gland'}, {'tumor_tissue_site': 'Bile duct'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Small Intestines|Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum|Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_tissue_site': 'Superficial Trunk - Buttock'}, {'tumor_tissue_site': 'Lower Extremity - Groin'}, {'tumor_tissue_site': 'Liver'}, {'tumor_tissue_site': 'Trunk|Extremities'}, {'tumor_tissue_site': 'Adrenal'}, {'tumor_tissue_site': 'Bladder'}, {'tumor_tissue_site': 'Thymus'}, {'tumor_tissue_site': '[Unknown]'}, {'tumor_tissue_site': 'Gynecological - Uterus|Gynecological - Cervix'}, {'tumor_tissue_site': 'Superficial Trunk - Abdominal wall'}, {'tumor_tissue_site': 'Superficial Trunk - Flank'}, {'tumor_tissue_site': 'Lower Extremity - Foot/ankle'}], 'var_function-call-11490055776287208059': [], 'var_function-call-194408102950400133': [], 'var_function-call-10381046610534255231': [{'histological_type': 'Untreated primary (de novo) GBM'}, {'histological_type': 'Glioblastoma Multiforme (GBM)'}, {'histological_type': 'Treated primary GBM'}], 'var_function-call-11369679035384988593': [{'histological_type': 'Oligodendroglioma'}, {'histological_type': 'Astrocytoma'}, {'histological_type': 'Oligoastrocytoma'}], 'var_function-call-12008505857715535507': [{'Patient_description': 'Case 739CC9F1-71BE-4F81-A5D1-EDA673903E45, linked to barcode TCGA-RY-A83X, corresponds to a FEMALE patient diagnosed with Brain lower grade glioma, with vital status Alive.'}], 'var_function-call-10951833064531510723': 'file_storage/function-call-10951833064531510723.json', 'var_function-call-13716372521414978848': [{'ParticipantBarcode': 'TCGA-06-0675', 'SampleBarcode': 'TCGA-06-0675-11A', 'AliquotBarcode': 'TCGA-06-0675-11A-32R-A36H-07', 'SampleTypeLetterCode': 'NT', 'SampleType': 'Solid Tissue Normal', 'Symbol': 'LXN', 'Entrez': '56925', 'normalized_count': '69.7259'}], 'var_function-call-16206894195861881261': 'file_storage/function-call-16206894195861881261.json'}

exec(code, env_args)
