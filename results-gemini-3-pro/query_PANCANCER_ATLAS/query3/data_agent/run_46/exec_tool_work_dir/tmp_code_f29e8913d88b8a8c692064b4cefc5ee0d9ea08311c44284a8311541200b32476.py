code = """import pandas as pd
import json
import re

# Load data
with open(locals()['var_function-call-6174305248407743444'], 'r') as f:
    clinical_data = json.load(f)
with open(locals()['var_function-call-1694462993722135078'], 'r') as f:
    mutation_data = json.load(f)

# Process Clinical Data
patients = []
for record in clinical_data:
    desc = record['Patient_description']
    hist_type = record['histological_type']
    
    # Extract Barcode
    # Look for pattern TCGA-XX-XXXX
    match = re.search(r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}', desc)
    if match:
        barcode = match.group(0)
        # Drop duplicate patients if any, though query didn't group by patient
        patients.append({'barcode': barcode, 'hist_type': hist_type})

df_clinical = pd.DataFrame(patients).drop_duplicates(subset='barcode')

# Filter by marginal totals (histological type count > 10)
hist_counts = df_clinical['hist_type'].value_counts()
valid_types = hist_counts[hist_counts > 10].index.tolist()
df_clinical = df_clinical[df_clinical['hist_type'].isin(valid_types)]

# Process Mutation Data
mutated_barcodes = set()
for record in mutation_data:
    bc = record['ParticipantBarcode']
    if bc and len(bc) >= 12:
        mutated_barcodes.add(bc[:12])

# Assign Mutation Status
df_clinical['mutated'] = df_clinical['barcode'].apply(lambda x: 1 if x in mutated_barcodes else 0)

# Contingency Table
contingency_table = pd.crosstab(df_clinical['hist_type'], df_clinical['mutated'])

# Calculate Chi-Square
chi2_stat = 0.0
grand_total = contingency_table.values.sum()
row_totals = contingency_table.sum(axis=1)
col_totals = contingency_table.sum(axis=0)

# Debug prints (optional, but good for verification in logs)
# print("Contingency Table:")
# print(contingency_table)

for i in range(len(contingency_table)):
    for j in range(len(contingency_table.columns)):
        O = contingency_table.iloc[i, j]
        E = (row_totals.iloc[i] * col_totals.iloc[j]) / grand_total
        if E > 0:
            chi2_stat += ((O - E) ** 2) / E

print("__RESULT__:")
print(json.dumps(chi2_stat))"""

env_args = {'var_function-call-4319574717777598010': ['clinical_info'], 'var_function-call-3264232244128170485': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_function-call-14915337706382406515': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma', 'tumor_tissue_site': 'Ovary'}, {'Patient_description': 'Patient TCGA-36-1576 (UUID 3445c524-5a37-40b6-8614-956d76eed939) is a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Current vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma', 'tumor_tissue_site': 'Ovary'}, {'Patient_description': 'Record fdd4adb8-9295-480a-9352-305b5eb51187 refers to patient TCGA-25-2408, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.', 'histological_type': 'Serous Cystadenocarcinoma', 'tumor_tissue_site': 'Ovary'}, {'Patient_description': 'Record 6f25001a-f890-4fd0-a994-e62a9ea5c6f3 refers to patient TCGA-29-2427, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Alive.', 'histological_type': 'Serous Cystadenocarcinoma', 'tumor_tissue_site': 'Ovary'}, {'Patient_description': 'Case 9446e349-71e6-455a-aa8f-53ec96597146, linked to barcode TCGA-10-0933, corresponds to a FEMALE patient diagnosed with Ovarian serous cystadenocarcinoma, with vital status Dead.', 'histological_type': 'Serous Cystadenocarcinoma', 'tumor_tissue_site': 'Ovary'}], 'var_function-call-14620850449414767674': [{'histological_type': 'None', 'count': '1'}, {'histological_type': 'Infiltrating Ductal Carcinoma', 'count': '766'}, {'histological_type': 'Mucinous Carcinoma', 'count': '17'}, {'histological_type': 'Metaplastic Carcinoma', 'count': '8'}, {'histological_type': 'Mixed Histology (please specify)', 'count': '30'}, {'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'count': '108'}, {'histological_type': 'Infiltrating Lobular Carcinoma', 'count': '201'}, {'histological_type': 'Other  specify', 'count': '45'}, {'histological_type': 'Medullary Carcinoma', 'count': '6'}, {'histological_type': 'Infiltrating Carcinoma NOS', 'count': '1'}], 'var_function-call-7080493790160809274': [{'Patient_description': "Patient TCGA-DK-A6AW, registered under UUID 01C815BA-7BDA-4F7E-865C-0C5776FEBF2C, belongs to the Bladder urothelial carcinoma cohort. This MALE patient's vital status is Alive."}], 'var_function-call-12803302480059474591': [{'Patient_description': 'Clinical entry D13FB44B-291B-4EA4-920C-142DAA8D1989 identifies patient TCGA-AC-A5EH, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.'}], 'var_function-call-14346435000539708229': [{'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'count': '108'}], 'var_function-call-15470009077829445687': [{'histological_type': 'None', 'count': '3'}, {'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'count': '409'}], 'var_function-call-17093235135562389178': [{'patient_id': '1953'}, {'patient_id': '1576'}, {'patient_id': '2408'}], 'var_function-call-449278014253394296': [{'ParticipantBarcode': 'TCGA-AX-A3G8', 'Tumor_SampleBarcode': 'TCGA-AX-A3G8-01A', 'Tumor_AliquotBarcode': 'TCGA-AX-A3G8-01A-11D-A228-09', 'Normal_SampleBarcode': 'TCGA-AX-A3G8-10A', 'Normal_AliquotBarcode': 'TCGA-AX-A3G8-10A-01D-A22A-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'GLI3', 'HGVSp_Short': 'p.P1033Rfs*46', 'Variant_Classification': 'Frame_Shift_Del', 'HGVSc': 'c.3098delC', 'CENTERS': 'INDELOCATOR|VARSCANI', 'FILTER': 'ndp'}, {'ParticipantBarcode': 'TCGA-EO-A22U', 'Tumor_SampleBarcode': 'TCGA-EO-A22U-01A', 'Tumor_AliquotBarcode': 'TCGA-EO-A22U-01A-11D-A17W-09', 'Normal_SampleBarcode': 'TCGA-EO-A22U-10B', 'Normal_AliquotBarcode': 'TCGA-EO-A22U-10B-01D-A17W-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'MUM1L1', 'HGVSp_Short': 'p.Y134Ifs*5', 'Variant_Classification': 'Frame_Shift_Ins', 'HGVSc': 'c.399dupA', 'CENTERS': 'INDELOCATOR|VARSCANI', 'FILTER': 'ndp'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CSF2RA', 'HGVSp_Short': 'p.S351P', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.1051T>C', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}], 'var_function-call-6174305248407743444': 'file_storage/function-call-6174305248407743444.json', 'var_function-call-1694462993722135078': 'file_storage/function-call-1694462993722135078.json'}

exec(code, env_args)
