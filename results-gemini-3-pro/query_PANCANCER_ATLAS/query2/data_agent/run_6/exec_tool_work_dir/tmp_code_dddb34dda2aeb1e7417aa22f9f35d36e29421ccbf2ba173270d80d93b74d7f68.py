code = """import json
import re
import pandas as pd

# Load clinical data for Breast Cancer
with open(locals()['var_function-call-16918217456976190030'], 'r') as f:
    clinical_data = json.load(f)

# Load mutation data
with open(locals()['var_function-call-940698615471361902'], 'r') as f:
    mutation_data = json.load(f)

# Parse clinical data
parsed_clinical = []
barcode_pattern = re.compile(r"(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})")
vital_status_pattern = re.compile(r"vital status[:\s=]+(Alive|Dead)", re.IGNORECASE)

for record in clinical_data:
    desc = record.get("Patient_description", "")
    hist_type = record.get("histological_type", "Unknown")
    
    # Extract Barcode
    barcode_match = barcode_pattern.search(desc)
    barcode = barcode_match.group(1) if barcode_match else None
    
    # Extract Vital Status
    vital_match = vital_status_pattern.search(desc)
    if not vital_match:
        if 'vital status' in desc.lower():
            part = desc.lower().split('vital status')[1]
            if 'alive' in part:
                vital_status = 'Alive'
            elif 'dead' in part:
                vital_status = 'Dead'
            else:
                vital_status = 'Unknown'
        else:
            vital_status = 'Unknown'
    else:
        vital_status = vital_match.group(1).capitalize()
    
    if barcode and vital_status == 'Alive':
        parsed_clinical.append({
            "Barcode": barcode,
            "Histological_Type": hist_type
        })

# Create DataFrame for clinical
df_clinical = pd.DataFrame(parsed_clinical)

if df_clinical.empty:
    print("__RESULT__:")
    print("[]")
else:
    # Create set of mutated barcodes
    mutated_barcodes = set(m["ParticipantBarcode"] for m in mutation_data)

    # Add mutation status
    df_clinical["Has_CDH1_Mutation"] = df_clinical["Barcode"].apply(lambda x: x in mutated_barcodes)

    # Group by histological type
    results = []
    for ht, group in df_clinical.groupby("Histological_Type"):
        total = len(group)
        mutated = group["Has_CDH1_Mutation"].sum()
        percentage = (mutated / total) * 100 if total > 0 else 0
        results.append({
            "Histological_Type": ht,
            "Total": total,
            "Mutated": mutated,
            "Percentage": percentage
        })

    # Sort by percentage descending
    results_df = pd.DataFrame(results).sort_values(by="Percentage", ascending=False)

    print("__RESULT__:")
    print(results_df.head(10).to_json(orient="records"))"""

env_args = {'var_function-call-13681501465962856199': ['clinical_info'], 'var_function-call-11447464790721382465': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_function-call-14433176652829598597': [], 'var_function-call-4617589526121320282': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.'}, {'Patient_description': 'Patient TCGA-36-1576 (UUID 3445c524-5a37-40b6-8614-956d76eed939) is a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Current vital status: Alive.'}, {'Patient_description': 'Record fdd4adb8-9295-480a-9352-305b5eb51187 refers to patient TCGA-25-2408, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.'}, {'Patient_description': 'Record 6f25001a-f890-4fd0-a994-e62a9ea5c6f3 refers to patient TCGA-29-2427, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Alive.'}, {'Patient_description': 'Case 9446e349-71e6-455a-aa8f-53ec96597146, linked to barcode TCGA-10-0933, corresponds to a FEMALE patient diagnosed with Ovarian serous cystadenocarcinoma, with vital status Dead.'}, {'Patient_description': "Patient TCGA-23-1124, registered under UUID 8a6d2ce3-cc57-451b-9b07-8263782aa23f, belongs to the Ovarian serous cystadenocarcinoma cohort. This FEMALE patient's vital status is Dead."}, {'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-23-2641 (UUID 49e5ee61-a1c9-4038-84ac-92683e573a65) is recorded as a FEMALE with vital status: Alive.'}, {'Patient_description': 'Patient TCGA-23-1118 (FEMALE, UUID 700e91bb-d675-41b2-bbbd-935767c7b447) is enrolled in the study of Ovarian serous cystadenocarcinoma. Vital status: Alive.'}, {'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-23-1120 (UUID fdf83fdf-dfbb-4306-9a1b-b4487d18b402) is recorded as a FEMALE with vital status: Alive.'}, {'Patient_description': 'The individual with barcode TCGA-23-2081 and UUID 41178cbc-db73-4007-b5d8-febebf7f578d is a FEMALE case of Ovarian serous cystadenocarcinoma, documented with vital status = Dead.'}, {'Patient_description': 'Case 1db60f09-7f5a-4f21-8003-06a6abc781db, linked to barcode TCGA-29-1694, corresponds to a FEMALE patient diagnosed with Ovarian serous cystadenocarcinoma, with vital status Dead.'}, {'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-WR-A838 (UUID B8023162-5E82-40E6-AD8C-8ACF81821F01) is recorded as a FEMALE with vital status: Dead.'}, {'Patient_description': "Patient TCGA-31-1955, registered under UUID cce34351-1700-405b-818f-a598f63a33e8, belongs to the Ovarian serous cystadenocarcinoma cohort. This FEMALE patient's vital status is Alive."}, {'Patient_description': 'Patient TCGA-32-4209 (MALE, UUID 5438322c-9db0-4974-ba01-801020559f97) is enrolled in the study of Glioblastoma multiforme. Vital status: Dead.'}, {'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-29-1696 (UUID 8a98a6e6-b763-4824-858b-fd2738e6c9a3) is recorded as a FEMALE with vital status: Dead.'}, {'Patient_description': 'Record 40635bf3-d8ba-4833-b623-547e55e5d07e refers to patient TCGA-29-2425, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Alive.'}, {'Patient_description': 'Case 05019013-7ea5-4905-ac79-901146ba2ee2, linked to barcode TCGA-29-1688, corresponds to a FEMALE patient diagnosed with Ovarian serous cystadenocarcinoma, with vital status Dead.'}, {'Patient_description': 'Record 13319c20-02f6-4b5f-b24f-3d8f4084094c refers to patient TCGA-25-1318, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.'}, {'Patient_description': 'Record 79fd602b-3e8e-4353-aa78-4f5f170b607d refers to patient TCGA-25-1328, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.'}, {'Patient_description': 'The individual with barcode TCGA-57-1584 and UUID ed21615c-0de3-421c-9e8d-8996026c4431 is a FEMALE case of Ovarian serous cystadenocarcinoma, documented with vital status = Alive.'}], 'var_function-call-5168221999614525605': [{'bladder_count': '0', 'breast_count': '0'}], 'var_function-call-8497871221049058424': [{'Patient_description': "Patient TCGA-DK-A6AW, registered under UUID 01C815BA-7BDA-4F7E-865C-0C5776FEBF2C, belongs to the Bladder urothelial carcinoma cohort. This MALE patient's vital status is Alive."}, {'Patient_description': 'In the Bladder urothelial carcinoma dataset, patient TCGA-GD-A3OQ (UUID 2E85C30C-C4C4-4096-9EEF-4EB2C7D991A3) is recorded as a MALE with vital status: Alive.'}, {'Patient_description': 'The individual with barcode TCGA-CF-A47W and UUID 122FC134-8915-47DB-96C9-AB1853C3CD18 is a MALE case of Bladder urothelial carcinoma, documented with vital status = Alive.'}, {'Patient_description': 'Patient TCGA-CF-A3MF (MALE, UUID 1E308B12-0590-4DAE-94D0-A539FCF25DF7) is enrolled in the study of Bladder urothelial carcinoma. Vital status: Alive.'}, {'Patient_description': 'Case DE810AF0-4C18-4E8F-9836-F8ABC425E3EB, linked to barcode TCGA-DK-A2I6, corresponds to a MALE patient diagnosed with Bladder urothelial carcinoma, with vital status Alive.'}], 'var_function-call-9514083833643278339': 'file_storage/function-call-9514083833643278339.json', 'var_function-call-940698615471361902': 'file_storage/function-call-940698615471361902.json', 'var_function-call-1402491605699045258': [{'Histological_Type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'Total': 228, 'Mutated': 7, 'Percentage': 3.0701754386}, {'Histological_Type': 'None', 'Total': 2, 'Mutated': 0, 'Percentage': 0.0}], 'var_function-call-5711092014623023313': [{'histological_type': 'None'}, {'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}], 'var_function-call-7306693443673635609': [{'histological_type': 'Thyroid Papillary Carcinoma - Classical/usual'}, {'histological_type': 'Pancreas-Colloid (mucinous non-cystic) Carcinoma'}, {'histological_type': 'None'}, {'histological_type': 'Stomach  Adenocarcinoma  Diffuse Type'}, {'histological_type': 'Prostate Adenocarcinoma  Other Subtype'}, {'histological_type': 'Fibrolamellar Carcinoma'}, {'histological_type': 'Infiltrating Ductal Carcinoma'}, {'histological_type': 'Untreated primary (de novo) GBM'}, {'histological_type': 'Synovial Sarcoma - Biphasic'}, {'histological_type': 'Mucinous Adenocarcinoma of Endocervical Type'}, {'histological_type': 'Pancreas-Adenocarcinoma-Other Subtype'}, {'histological_type': 'Thymoma; Type B1|Thymoma; Type B2'}, {'histological_type': 'Seminoma; NOS|Non-Seminoma; Teratoma (Mature)|Non-Seminoma; Embryonal Carcinoma|Non-Seminoma; Yolk Sac Tumor'}, {'histological_type': 'Non-Seminoma; Yolk Sac Tumor|Non-Seminoma; Teratoma (Mature)'}, {'histological_type': 'Non-Seminoma; Choriocarcinoma|Non-Seminoma; Embryonal Carcinoma|Non-Seminoma; Yolk Sac Tumor|Non-Seminoma; Teratoma (Mature)|Non-Seminoma; Teratoma (Immature)'}, {'histological_type': 'Oligodendroglioma'}, {'histological_type': 'Non-Seminoma; Embryonal Carcinoma|Non-Seminoma; Yolk Sac Tumor|Non-Seminoma; Teratoma (Immature)'}, {'histological_type': 'Lung Clear Cell Adenocarcinoma'}, {'histological_type': 'Seminoma; NOS|Non-Seminoma; Embryonal Carcinoma'}, {'histological_type': 'Pheochromocytoma'}], 'var_function-call-6518695112137348245': [{'Patient_description': 'Clinical entry D13FB44B-291B-4EA4-920C-142DAA8D1989 identifies patient TCGA-AC-A5EH, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.'}], 'var_function-call-13307035786198868253': [{'histological_type': 'Infiltrating Ductal Carcinoma', 'cnt': '777'}, {'histological_type': 'Infiltrating Lobular Carcinoma', 'cnt': '201'}, {'histological_type': 'Other  specify', 'cnt': '46'}, {'histological_type': 'Mixed Histology (please specify)', 'cnt': '30'}, {'histological_type': 'Mucinous Carcinoma', 'cnt': '17'}], 'var_function-call-16918217456976190030': 'file_storage/function-call-16918217456976190030.json'}

exec(code, env_args)
