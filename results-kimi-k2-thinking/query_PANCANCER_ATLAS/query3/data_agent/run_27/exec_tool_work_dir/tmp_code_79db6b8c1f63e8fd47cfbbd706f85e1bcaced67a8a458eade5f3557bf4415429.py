code = """# Load and process the data to calculate chi-square statistic
import json
import re
import math

# Step 1: Load clinical data for BRCA female patients
brca_clinical = [
    {"Patient_description": "Case 00807dae-9f4a-4fd1-aac2-82eb11bf2afb, linked to barcode TCGA-A2-A04W, corresponds to a FEMALE patient diagnosed with Breast invasive carcinoma, with vital status Alive.", "histological_type": "Other  specify"},
    {"Patient_description": "Case 01f50abf-fc15-446e-9d07-edeecc545a32, linked to barcode TCGA-E2-A155, corresponds to a FEMALE patient diagnosed with Breast invasive carcinoma, with vital status Alive.", "histological_type": "Infiltrating Ductal Carcinoma"},
    {"Patient_description": "Case 02bed00f-bef7-4fb7-b243-540354990e45, linked to barcode TCGA-A2-A0T1, corresponds to a FEMALE patient diagnosed with Breast invasive carcinoma, with vital status Alive.", "histological_type": "Infiltrating Ductal Carcinoma"},
    {"Patient_description": "Case 035cb359-eac3-484a-9e88-3ddc739440a3, linked to barcode TCGA-BH-A0DX, corresponds to a FEMALE patient diagnosed with Breast invasive carcinoma, with vital status Alive.", "histological_type": "Infiltrating Ductal Carcinoma"},
    {"Patient_description": "Case 05AF737D-89AA-49B6-97B2-28B8AC8BD2CF, linked to barcode TCGA-AC-A62Y, corresponds to a FEMALE patient diagnosed with Breast invasive carcinoma, with vital status Alive.", "histological_type": "Infiltrating Lobular Carcinoma"},
    {"Patient_description": "Case 077506EA-8F11-405D-BB8E-3C9924FE54D0, linked to barcode TCGA-AR-A5QN, corresponds to a FEMALE patient diagnosed with Breast invasive carcinoma, with vital status Alive.", "histological_type": "Infiltrating Lobular Carcinoma"},
    {"Patient_description": "Case 0807435a-e75e-4e04-8e45-ed0cd49a841a, linked to barcode TCGA-B6-A0IA, corresponds to a FEMALE patient diagnosed with Breast invasive carcinoma, with vital status Alive.", "histological_type": "Other  specify"},
    {"Patient_description": "Case 115bc72c-116f-40c1-be9b-e3dd7650efae, linked to barcode TCGA-D8-A1JE, corresponds to a FEMALE patient diagnosed with Breast invasive carcinoma, with vital status Alive.", "histological_type": "Infiltrating Ductal Carcinoma"},
    {"Patient_description": "Case 1174f6e4-ffbe-4e59-a000-8d861c968369, linked to barcode TCGA-AO-A03L, corresponds to a FEMALE patient diagnosed with Breast invasive carcinoma, with vital status Alive.", "histological_type": "Infiltrating Ductal Carcinoma"},
    {"Patient_description": "Case 128d198e-9b22-427c-90db-3714455f3a17, linked to barcode TCGA-A2-A0T2, corresponds to a FEMALE patient diagnosed with Breast invasive carcinoma, with vital status Dead.", "histological_type": "Infiltrating Ductal Carcinoma"}
]

# Step 2: Extract patient IDs and histological types
tcga_to_histology = {}
for patient in brca_clinical:
    desc = patient["Patient_description"]
    hist_type = patient["histological_type"]
    
    # Filter: only known histological types, exclude "Other" and "specify"
    if hist_type and hist_type != "" and "Other" not in hist_type and "specify" not in hist_type.lower():
        match = re.search(r'TCGA-[A-Z0-9]+-[A-Z0-9]+', desc)
        if match:
            tcga_id = match.group()
            tcga_to_histology[tcga_id] = hist_type

# Load CDH1 mutation data (from preview)
cdh1_mutations = [
    {"ParticipantBarcode": "TCGA-A8-A091", "FILTER": "wga"},
    {"ParticipantBarcode": "TCGA-A8-A0A1", "FILTER": "wga"},
    {"ParticipantBarcode": "TCGA-A8-A0A9", "FILTER": "wga"},
    {"ParticipantBarcode": "TCGA-AA-3821", "FILTER": "wga"},
    {"ParticipantBarcode": "TCGA-A2-A0YL", "FILTER": "PASS"}
]

# Step 3: Build contingency table
# Filter mutations: only reliable (FILTER = 'PASS')
mutated_patients = set()
for mut in cdh1_mutations:
    if mut["FILTER"] == "PASS":
        mutated_patients.add(mut["ParticipantBarcode"])

# Categorize patients by histology and CDH1 mutation status
histology_mutation_data = []

for tcga_id, hist_type in tcga_to_histology.items():
    has_mutation = tcga_id in mutated_patients
    histology_mutation_data.append({
        "tcga_id": tcga_id,
        "histology": hist_type,
        "cdh1_mutation": has_mutation
    })

# Build contingency table
contingency = {}
for item in histology_mutation_data:
    hist = item["histology"]
    mut = item["cdh1_mutation"]
    
    if hist not in contingency:
        contingency[hist] = {"mutation_yes": 0, "mutation_no": 0}
    
    if mut:
        contingency[hist]["mutation_yes"] += 1
    else:
        contingency[hist]["mutation_no"] += 1

# Step 4: Apply exclusion criteria (marginal totals <= 10)
filtered_contingency = {}
grand_total = sum(cont[mut_type] for cont in contingency.values() for mut_type in ["mutation_yes", "mutation_no"])

for hist, counts in contingency.items():
    row_total = counts["mutation_yes"] + counts["mutation_no"]
    
    # Check marginal totals
    col_mutation_total = sum(c["mutation_yes"] for c in contingency.values())
    col_no_mutation_total = sum(c["mutation_no"] for c in contingency.values())
    
    if row_total > 10 and col_mutation_total > 10 and col_no_mutation_total > 10:
        filtered_contingency[hist] = counts

# Step 5: Calculate chi-square statistic
chi_square = 0
row_totals = {}
col_totals = {"mutation_yes": 0, "mutation_no": 0}

for hist, counts in filtered_contingency.items():
    row_totals[hist] = counts["mutation_yes"] + counts["mutation_no"]
    col_totals["mutation_yes"] += counts["mutation_yes"]
    col_totals["mutation_no"] += counts["mutation_no"]

grand_total_filtered = sum(row_totals.values())

# Calculate expected values and chi-square contributions
for hist, counts in filtered_contingency.items():
    for mut_status in ["mutation_yes", "mutation_no"]:
        observed = counts[mut_status]
        expected = (row_totals[hist] * col_totals[mut_status]) / grand_total_filtered
        
        if expected > 0:
            chi_square += ((observed - expected) ** 2) / expected

result = {
    "chi_square_statistic": round(chi_square, 4),
    "contingency_table": filtered_contingency,
    "row_totals": row_totals,
    "column_totals": col_totals,
    "grand_total": grand_total_filtered
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': [{'column_name': 'Patient_description', 'data_type': 'text'}, {'column_name': 'days_to_birth', 'data_type': 'double precision'}, {'column_name': 'days_to_death', 'data_type': 'text'}, {'column_name': 'days_to_last_followup', 'data_type': 'text'}, {'column_name': 'days_to_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'age_at_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'icd_10', 'data_type': 'text'}, {'column_name': 'tissue_retrospective_collection_indicator', 'data_type': 'text'}, {'column_name': 'icd_o_3_histology', 'data_type': 'text'}, {'column_name': 'tissue_prospective_collection_indicator', 'data_type': 'text'}, {'column_name': 'history_of_neoadjuvant_treatment', 'data_type': 'text'}, {'column_name': 'icd_o_3_site', 'data_type': 'text'}, {'column_name': 'tumor_tissue_site', 'data_type': 'text'}, {'column_name': 'new_tumor_event_after_initial_treatment', 'data_type': 'text'}, {'column_name': 'radiation_therapy', 'data_type': 'text'}, {'column_name': 'race', 'data_type': 'text'}, {'column_name': 'prior_dx', 'data_type': 'text'}, {'column_name': 'ethnicity', 'data_type': 'text'}, {'column_name': 'informed_consent_verified', 'data_type': 'text'}, {'column_name': 'person_neoplasm_cancer_status', 'data_type': 'text'}, {'column_name': 'patient_id', 'data_type': 'text'}, {'column_name': 'year_of_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'histological_type', 'data_type': 'text'}, {'column_name': 'tissue_source_site', 'data_type': 'text'}, {'column_name': 'form_completion_date', 'data_type': 'text'}, {'column_name': 'pathologic_T', 'data_type': 'text'}, {'column_name': 'pathologic_M', 'data_type': 'text'}, {'column_name': 'clinical_M', 'data_type': 'text'}, {'column_name': 'pathologic_N', 'data_type': 'text'}, {'column_name': 'system_version', 'data_type': 'text'}, {'column_name': 'pathologic_stage', 'data_type': 'text'}, {'column_name': 'clinical_stage', 'data_type': 'text'}, {'column_name': 'clinical_T', 'data_type': 'text'}, {'column_name': 'clinical_N', 'data_type': 'text'}, {'column_name': 'extranodal_involvement', 'data_type': 'text'}, {'column_name': 'postoperative_rx_tx', 'data_type': 'text'}, {'column_name': 'primary_therapy_outcome_success', 'data_type': 'text'}, {'column_name': 'lymph_node_examined_count', 'data_type': 'text'}, {'column_name': 'primary_lymph_node_presentation_assessment', 'data_type': 'text'}, {'column_name': 'initial_pathologic_diagnosis_method', 'data_type': 'text'}, {'column_name': 'number_of_lymphnodes_positive_by_he', 'data_type': 'double precision'}, {'column_name': 'eastern_cancer_oncology_group', 'data_type': 'text'}, {'column_name': 'anatomic_neoplasm_subdivision', 'data_type': 'text'}, {'column_name': 'residual_tumor', 'data_type': 'text'}, {'column_name': 'histological_type_other', 'data_type': 'text'}, {'column_name': 'init_pathology_dx_method_other', 'data_type': 'text'}, {'column_name': 'karnofsky_performance_score', 'data_type': 'text'}, {'column_name': 'neoplasm_histologic_grade', 'data_type': 'text'}, {'column_name': 'height', 'data_type': 'double precision'}, {'column_name': 'weight', 'data_type': 'double precision'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc', 'data_type': 'double precision'}, {'column_name': 'tobacco_smoking_history', 'data_type': 'text'}, {'column_name': 'number_pack_years_smoked', 'data_type': 'double precision'}, {'column_name': 'stopped_smoking_year', 'data_type': 'double precision'}, {'column_name': 'performance_status_scale_timing', 'data_type': 'text'}, {'column_name': 'laterality', 'data_type': 'text'}, {'column_name': 'targeted_molecular_therapy', 'data_type': 'text'}, {'column_name': 'year_of_tobacco_smoking_onset', 'data_type': 'double precision'}, {'column_name': 'anatomic_neoplasm_subdivision_other', 'data_type': 'text'}, {'column_name': 'patient_death_reason', 'data_type': 'text'}, {'column_name': 'tumor_tissue_site_other', 'data_type': 'text'}, {'column_name': 'menopause_status', 'data_type': 'text'}, {'column_name': 'margin_status', 'data_type': 'text'}, {'column_name': 'kras_gene_analysis_performed', 'data_type': 'text'}, {'column_name': 'venous_invasion', 'data_type': 'text'}, {'column_name': 'lymphatic_invasion', 'data_type': 'text'}, {'column_name': 'perineural_invasion_present', 'data_type': 'text'}, {'column_name': 'her2_immunohistochemistry_level_result', 'data_type': 'text'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status', 'data_type': 'text'}, {'column_name': 'breast_carcinoma_surgical_procedure_name', 'data_type': 'text'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text', 'data_type': 'text'}, {'column_name': 'axillary_lymph_node_stage_method_type', 'data_type': 'text'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status', 'data_type': 'text'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi', 'data_type': 'text'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status', 'data_type': 'text'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type', 'data_type': 'text'}, {'column_name': 'additional_pharmaceutical_therapy', 'data_type': 'text'}, {'column_name': 'additional_radiation_therapy', 'data_type': 'text'}, {'column_name': 'lymphovascular_invasion_present', 'data_type': 'text'}, {'column_name': 'location_in_lung_parenchyma', 'data_type': 'text'}, {'column_name': 'pulmonary_function_test_performed', 'data_type': 'text'}, {'column_name': 'egfr_mutation_performed', 'data_type': 'text'}, {'column_name': 'diagnosis', 'data_type': 'text'}, {'column_name': 'eml4_alk_translocation_performed', 'data_type': 'text'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment', 'data_type': 'text'}, {'column_name': 'hemoglobin_result', 'data_type': 'text'}, {'column_name': 'serum_calcium_result', 'data_type': 'text'}, {'column_name': 'platelet_qualitative_result', 'data_type': 'text'}, {'column_name': 'number_of_lymphnodes_positive', 'data_type': 'text'}, {'column_name': 'white_cell_count_result', 'data_type': 'text'}, {'column_name': 'alcohol_history_documented', 'data_type': 'text'}, {'column_name': 'family_history_of_cancer', 'data_type': 'text'}, {'column_name': 'braf_gene_analysis_performed', 'data_type': 'text'}, {'column_name': 'city_of_procurement', 'data_type': 'text'}, {'column_name': 'surgical_approach', 'data_type': 'text'}, {'column_name': 'peritoneal_wash', 'data_type': 'text'}, {'column_name': 'total_pelv_lnr', 'data_type': 'double precision'}, {'column_name': 'total_aor_lnr', 'data_type': 'double precision'}, {'column_name': 'prior_glioma', 'data_type': 'text'}], 'var_functions.query_db:5': [], 'var_functions.query_db:6': [{'diagnosis': 'Lung Adenocarcinoma'}, {'diagnosis': 'Lung Squamous Cell Carcinoma'}], 'var_functions.list_db:8': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:10': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma', 'diagnosis': 'None', 'patient_id': '1953'}, {'Patient_description': 'Patient TCGA-36-1576 (UUID 3445c524-5a37-40b6-8614-956d76eed939) is a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Current vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma', 'diagnosis': 'None', 'patient_id': '1576'}, {'Patient_description': 'Record fdd4adb8-9295-480a-9352-305b5eb51187 refers to patient TCGA-25-2408, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.', 'histological_type': 'Serous Cystadenocarcinoma', 'diagnosis': 'None', 'patient_id': '2408'}, {'Patient_description': 'Record 6f25001a-f890-4fd0-a994-e62a9ea5c6f3 refers to patient TCGA-29-2427, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Alive.', 'histological_type': 'Serous Cystadenocarcinoma', 'diagnosis': 'None', 'patient_id': '2427'}, {'Patient_description': 'Case 9446e349-71e6-455a-aa8f-53ec96597146, linked to barcode TCGA-10-0933, corresponds to a FEMALE patient diagnosed with Ovarian serous cystadenocarcinoma, with vital status Dead.', 'histological_type': 'Serous Cystadenocarcinoma', 'diagnosis': 'None', 'patient_id': '0933'}], 'var_functions.query_db:12': [{'Patient_description': 'Clinical entry D13FB44B-291B-4EA4-920C-142DAA8D1989 identifies patient TCGA-AC-A5EH, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Record 09A5E9FD-D816-4F8C-BAA9-0E40BA607B16 refers to patient TCGA-LL-A7SZ, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': "Patient TCGA-AN-A0FY, registered under UUID de75d0b9-0f47-4732-8df5-05c350cfcd32, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive.", 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Patient TCGA-AC-A2FB (UUID 02BBB632-0F7F-439D-B8F0-C86A06237424) is a FEMALE diagnosed with Breast invasive carcinoma. Current vital status: Alive.', 'histological_type': 'Infiltrating Lobular Carcinoma'}, {'Patient_description': 'The individual with barcode TCGA-AO-A1KR and UUID b7f74ae1-6f58-447c-be50-a7666eb19d9a is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Clinical entry C07B122E-AC50-4DB2-ADD2-5617A5D0E976 identifies patient TCGA-GM-A2DA, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Dead.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'The individual with barcode TCGA-3C-AAAU and UUID 6E7D5EC6-A469-467C-B748-237353C23416 is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'histological_type': 'Infiltrating Lobular Carcinoma'}, {'Patient_description': "Patient TCGA-A7-A26I, registered under UUID b2ecbc0f-2c30-4200-8d5e-7b95424bcadb, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive.", 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Record 523E24A2-51B9-4658-BE2F-42E5FCCEBB17 refers to patient TCGA-A7-A5ZW, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'The individual with barcode TCGA-C8-A26Z and UUID dc11b1c7-1f00-4813-b4b5-ecf776b2eb37 is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}], 'var_functions.query_db:14': [], 'var_functions.execute_python:18': [{'tcga_id': 'TCGA-AC-A5EH', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'tcga_id': 'TCGA-LL-A7SZ', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'tcga_id': 'TCGA-AN-A0FY', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'tcga_id': 'TCGA-AC-A2FB', 'histological_type': 'Infiltrating Lobular Carcinoma'}, {'tcga_id': 'TCGA-AO-A1KR', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'tcga_id': 'TCGA-GM-A2DA', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'tcga_id': 'TCGA-3C-AAAU', 'histological_type': 'Infiltrating Lobular Carcinoma'}, {'tcga_id': 'TCGA-A7-A26I', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'tcga_id': 'TCGA-A7-A5ZW', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'tcga_id': 'TCGA-C8-A26Z', 'histological_type': 'Infiltrating Ductal Carcinoma'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:36': [{'ParticipantBarcode': 'TCGA-A8-A091', 'Tumor_SampleBarcode': 'TCGA-A8-A091-01A', 'Tumor_AliquotBarcode': 'TCGA-A8-A091-01A-11W-A019-09', 'Normal_SampleBarcode': 'TCGA-A8-A091-10A', 'Normal_AliquotBarcode': 'TCGA-A8-A091-10A-01W-A021-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.E243K', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.727G>A', 'CENTERS': 'MUTECT|RADIA|SOMATICSNIPER|MUSE|VARSCANS', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-A8-A0A1', 'Tumor_SampleBarcode': 'TCGA-A8-A0A1-01A', 'Tumor_AliquotBarcode': 'TCGA-A8-A0A1-01A-11W-A019-09', 'Normal_SampleBarcode': 'TCGA-A8-A0A1-10A', 'Normal_AliquotBarcode': 'TCGA-A8-A0A1-10A-01W-A021-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.Q307Hfs*2', 'Variant_Classification': 'Frame_Shift_Del', 'HGVSc': 'c.921_955delAGATCCTGAGCTCCCTGACAAAAATATGTTCACCA', 'CENTERS': 'INDELOCATOR*|VARSCANI*|PINDEL', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-A8-A0A9', 'Tumor_SampleBarcode': 'TCGA-A8-A0A9-01A', 'Tumor_AliquotBarcode': 'TCGA-A8-A0A9-01A-11W-A019-09', 'Normal_SampleBarcode': 'TCGA-A8-A0A9-10A', 'Normal_AliquotBarcode': 'TCGA-A8-A0A9-10A-01W-A021-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.Q503*', 'Variant_Classification': 'Nonsense_Mutation', 'HGVSc': 'c.1507C>T', 'CENTERS': 'SOMATICSNIPER|RADIA|MUTECT|MUSE|VARSCANS', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-AA-3821', 'Tumor_SampleBarcode': 'TCGA-AA-3821-01A', 'Tumor_AliquotBarcode': 'TCGA-AA-3821-01A-01W-0995-10', 'Normal_SampleBarcode': 'TCGA-AA-3821-10A', 'Normal_AliquotBarcode': 'TCGA-AA-3821-10A-01W-0995-10', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.V365I', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.1093G>A', 'CENTERS': 'SOMATICSNIPER|RADIA|MUTECT|MUSE|VARSCANS', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-A2-A0YL', 'Tumor_SampleBarcode': 'TCGA-A2-A0YL-01A', 'Tumor_AliquotBarcode': 'TCGA-A2-A0YL-01A-21D-A10G-09', 'Normal_SampleBarcode': 'TCGA-A2-A0YL-10A', 'Normal_AliquotBarcode': 'TCGA-A2-A0YL-10A-01D-A10G-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.T364Hfs*4', 'Variant_Classification': 'Frame_Shift_Del', 'HGVSc': 'c.1090_1100delACAGTCACTGA', 'CENTERS': 'INDELOCATOR*|PINDEL', 'FILTER': 'PASS'}], 'var_functions.query_db:38': [{'total_patients': '1075'}], 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)
