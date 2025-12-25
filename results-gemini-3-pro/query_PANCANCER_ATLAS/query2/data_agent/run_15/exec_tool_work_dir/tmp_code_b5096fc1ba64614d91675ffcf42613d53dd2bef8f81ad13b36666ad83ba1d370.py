code = """import json
import pandas as pd
import re

# Load clinical data
clinical_path = locals()['var_function-call-6242855755621865340']
with open(clinical_path, 'r') as f:
    clinical_data = json.load(f)

# Load mutation data
mutation_path = locals()['var_function-call-2332188952209072271']
with open(mutation_path, 'r') as f:
    mutation_data = json.load(f)

# Create DataFrame for clinical
clinical_df = pd.DataFrame(clinical_data)

# Extract Barcode from Patient_description
# Format: "... patient TCGA-XX-XXXX ..."
def extract_barcode(desc):
    match = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', desc)
    if match:
        return match.group(1)
    return None

clinical_df['barcode'] = clinical_df['Patient_description'].apply(extract_barcode)

# Filter out rows where barcode is not found (shouldn't happen if data is consistent)
clinical_df = clinical_df.dropna(subset=['barcode'])

# Create set of mutated barcodes
# Mutation barcodes might be 12 chars or longer. We match on the first 12 chars (Patient ID).
mutation_barcodes = set()
for item in mutation_data:
    bc = item.get('ParticipantBarcode')
    if bc:
        mutation_barcodes.add(bc[:12])

# Calculate stats per histological type
# Filter out "None" or invalid types if necessary? The query asks for top 3 types.
# I will treat "None" as a type if it exists, or maybe drop it. 
# Usually "None" means missing data. I'll drop rows where histological_type is "None" or "[Not Available]" just to be safe, 
# or keep them if they are significant. The query implies specific types.
# Let's see the types first.

clinical_df['is_mutated'] = clinical_df['barcode'].apply(lambda x: x in mutation_barcodes)

# Group by histological_type
stats = clinical_df.groupby('histological_type').agg(
    total_count=('barcode', 'count'),
    mutated_count=('is_mutated', 'sum')
).reset_index()

# Calculate percentage
stats['percentage'] = (stats['mutated_count'] / stats['total_count']) * 100

# Sort by percentage descending
stats = stats.sort_values(by='percentage', ascending=False)

# Print result
print("__RESULT__:")
print(stats.to_json(orient='records'))"""

env_args = {'var_function-call-12936693648104358544': ['clinical_info'], 'var_function-call-3725522790763581773': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_function-call-8372249275404450992': [{'tumor_tissue_site': 'Chest - Breast'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Small Intestines'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum|Retroperitoneum/Upper abdominal - Small Intestines|Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Intraabdominal'}, {'tumor_tissue_site': 'Superficial Trunk - Back'}, {'tumor_tissue_site': 'Chest - Chest wall'}, {'tumor_tissue_site': 'Choroid|Ciliary body|Iris'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_tissue_site': 'Rectum'}, {'tumor_tissue_site': 'Chest - Mediastinum'}, {'tumor_tissue_site': 'Gynecological - Uterus|Gynecological - Other (please specify'}, {'tumor_tissue_site': 'Esophagus'}, {'tumor_tissue_site': 'Extra-adrenal Site'}, {'tumor_tissue_site': 'Omentum'}, {'tumor_tissue_site': 'Endometrial'}, {'tumor_tissue_site': 'Chest - Other (please specify'}, {'tumor_tissue_site': 'Chest - Lung/pleura'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum'}, {'tumor_tissue_site': 'Gynecological - Uterus'}, {'tumor_tissue_site': 'Colon'}, {'tumor_tissue_site': 'None'}, {'tumor_tissue_site': 'Lung'}, {'tumor_tissue_site': 'Choroid|Ciliary body'}, {'tumor_tissue_site': 'Upper Extremity - Upper arm/elbow'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Kidney|Retroperitoneum/Upper abdominal - Liver|Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_tissue_site': 'Other  Specify'}, {'tumor_tissue_site': 'Head and Neck - Neck|Head and Neck - Other (please specify'}, {'tumor_tissue_site': 'Gynecological - Ovary'}, {'tumor_tissue_site': 'Lower Extremity - Lower leg/calf'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Other (please specify'}, {'tumor_tissue_site': 'Uterus'}, {'tumor_tissue_site': 'Extremities'}, {'tumor_tissue_site': 'Thyroid'}, {'tumor_tissue_site': 'Cervical'}, {'tumor_tissue_site': 'Choroid'}, {'tumor_tissue_site': 'Ovary'}, {'tumor_tissue_site': 'Upper Extremity - Shoulder/axilla'}, {'tumor_tissue_site': 'Peritoneum ovary'}, {'tumor_tissue_site': 'Stomach'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Pelvic'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Bladder'}, {'tumor_tissue_site': 'Head and Neck - Head'}, {'tumor_tissue_site': 'Kidney'}, {'tumor_tissue_site': 'Head and Neck'}, {'tumor_tissue_site': 'Lower Extremity - Other (please specify'}, {'tumor_tissue_site': 'Pancreas'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Pelvic|Gynecological - Uterus'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum|Retroperitoneum/Upper abdominal - Intraabdominal|Lower abdominal/Pelvic - Pelvic'}, {'tumor_tissue_site': 'Extremities|Extremities'}, {'tumor_tissue_site': 'Pleura'}, {'tumor_tissue_site': 'Brain'}, {'tumor_tissue_site': 'Anterior Mediastinum'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Colon'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Gastric'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Kidney'}, {'tumor_tissue_site': 'Testes'}, {'tumor_tissue_site': 'Trunk'}, {'tumor_tissue_site': 'Breast'}, {'tumor_tissue_site': 'Extremities|Trunk'}, {'tumor_tissue_site': 'Prostate'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Spermatic Cord'}, {'tumor_tissue_site': 'Head and Neck - Other (please specify'}, {'tumor_tissue_site': 'Head and Neck - Head|Chest - Chest wall'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Pancreas'}, {'tumor_tissue_site': 'Lower Extremity - Thigh/knee'}, {'tumor_tissue_site': 'Trunk|[Not Available]'}, {'tumor_tissue_site': 'Central nervous system'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Intraabdominal|Retroperitoneum/Upper abdominal - Small Intestines'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Intraabdominal|Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_tissue_site': 'Adrenal gland'}, {'tumor_tissue_site': 'Bile duct'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Small Intestines|Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum|Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_tissue_site': 'Superficial Trunk - Buttock'}, {'tumor_tissue_site': 'Lower Extremity - Groin'}, {'tumor_tissue_site': 'Liver'}, {'tumor_tissue_site': 'Trunk|Extremities'}, {'tumor_tissue_site': 'Adrenal'}, {'tumor_tissue_site': 'Bladder'}, {'tumor_tissue_site': 'Thymus'}, {'tumor_tissue_site': '[Unknown]'}, {'tumor_tissue_site': 'Gynecological - Uterus|Gynecological - Cervix'}, {'tumor_tissue_site': 'Superficial Trunk - Abdominal wall'}, {'tumor_tissue_site': 'Superficial Trunk - Flank'}, {'tumor_tissue_site': 'Lower Extremity - Foot/ankle'}], 'var_function-call-6242855755621865340': 'file_storage/function-call-6242855755621865340.json', 'var_function-call-2332188952209072271': 'file_storage/function-call-2332188952209072271.json'}

exec(code, env_args)
