code = """import json
import re

# Load clinical data
clinical_key = 'var_functions.query_db:48'
clinical_result = locals()[clinical_key]

if isinstance(clinical_result, str) and clinical_result.endswith('.json'):
    with open(clinical_result, 'r') as f:
        female_brca_patients = json.load(f)
else:
    female_brca_patients = clinical_result

# Load CDH1 mutation data
mutation_key = 'var_functions.query_db:36'
mutation_result = locals()[mutation_key]

if isinstance(mutation_result, str) and mutation_result.endswith('.json'):
    with open(mutation_result, 'r') as f:
        cdh1_mutations = json.load(f)
else:
    cdh1_mutations = mutation_result

print("Number of female BRCA patients:", len(female_brca_patients))
print("Number of CDH1 mutations:", len(cdh1_mutations))

# Extract patient barcodes and histological types
patient_histology = {}
for record in female_brca_patients:
    patient_desc = record['Patient_description']
    hist_type = record['histological_type']
    
    match = re.search(r'TCGA-[A-Z0-9]+-[A-Z0-9]+', patient_desc)
    if match:
        barcode = match.group(0)
        patient_histology[barcode] = hist_type

print("Extracted patient-histology mappings:", len(patient_histology))

# Get set of patients with CDH1 mutations
cdh1_patients = set()
for mut in cdh1_mutations:
    cdh1_patients.add(mut['ParticipantBarcode'])

print("Patients with CDH1 mutations:", len(cdh1_patients))

# Find overlap between BRCA patients and CDH1 mutation patients
common_patients = set(patient_histology.keys()) & cdh1_patients
print("BRCA patients with CDH1 mutations:", len(common_patients))

# Create contingency table
contingency = {}
for patient, hist_type in patient_histology.items():
    has_cdh1 = patient in cdh1_patients
    if hist_type not in contingency:
        contingency[hist_type] = {'CDH1_mutated': 0, 'CDH1_wildtype': 0}
    
    if has_cdh1:
        contingency[hist_type]['CDH1_mutated'] += 1
    else:
        contingency[hist_type]['CDH1_wildtype'] += 1

print("\nContingency table:")
for hist, counts in contingency.items():
    print(f"{hist}: {counts}")

# Filter out categories with marginal totals <= 10
filtered_contingency = {}
for hist, counts in contingency.items():
    row_total = counts['CDH1_mutated'] + counts['CDH1_wildtype']
    if row_total > 10:
        filtered_contingency[hist] = counts

print("\nFiltered contingency table (row totals > 10):")
for hist, counts in filtered_contingency.items():
    print(f"{hist}: {counts}")

# Calculate marginal totals
grand_total = sum([counts['CDH1_mutated'] + counts['CDH1_wildtype'] for counts in filtered_contingency.values()])
col_mutated_total = sum([counts['CDH1_mutated'] for counts in filtered_contingency.values()])
col_wildtype_total = sum([counts['CDH1_wildtype'] for counts in filtered_contingency.values()])

print(f"\nGrand total: {grand_total}")
print(f"CDH1 mutated column total: {col_mutated_total}")
print(f"CDH1 wildtype column total: {col_wildtype_total}")

# Check if we should exclude based on column totals
if col_mutated_total <= 10 or col_wildtype_total <= 10:
    print("Column totals are <= 10, insufficient data for chi-square test")
    __RESULT__ = "Insufficient data: marginal totals <= 10"
else:
    # Calculate chi-square statistic
    chi_square = 0
    for hist, counts in filtered_contingency.items():
        row_total = counts['CDH1_mutated'] + counts['CDH1_wildtype']
        
        # Expected for CDH1 mutated
        expected_mutated = (row_total * col_mutated_total) / grand_total
        observed_mutated = counts['CDH1_mutated']
        
        # Expected for CDH1 wildtype
        expected_wildtype = (row_total * col_wildtype_total) / grand_total
        observed_wildtype = counts['CDH1_wildtype']
        
        if expected_mutated > 0:
            chi_square += ((observed_mutated - expected_mutated) ** 2) / expected_mutated
        if expected_wildtype > 0:
            chi_square += ((observed_wildtype - expected_wildtype) ** 2) / expected_wildtype
    
    print(f"\nChi-square statistic: {chi_square:.4f}")
    
    # Calculate degrees of freedom
    df = len(filtered_contingency) - 1
    print(f"Degrees of freedom: {df}")
    
    __RESULT__ = json.dumps({
        "chi_square_statistic": round(chi_square, 4),
        "degrees_of_freedom": df,
        "contingency_table": filtered_contingency,
        "grand_total": grand_total,
        "cdh1_mutated_total": col_mutated_total,
        "cdh1_wildtype_total": col_wildtype_total
    })"""

env_args = {'var_functions.query_db:0': [{'column_name': 'Patient_description'}, {'column_name': 'days_to_birth'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'stopped_smoking_year'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'prior_glioma'}], 'var_functions.list_db:2': ['clinical_info'], 'var_functions.query_db:5': [], 'var_functions.query_db:6': [{'diagnosis': 'Lung Adenocarcinoma', 'patient_count': '514'}, {'diagnosis': 'Lung Squamous Cell Carcinoma', 'patient_count': '490'}, {'diagnosis': 'None', 'patient_count': '9757'}], 'var_functions.query_db:8': [], 'var_functions.query_db:10': [{'diagnosis': 'Lung Adenocarcinoma'}, {'diagnosis': 'None'}, {'diagnosis': 'Lung Squamous Cell Carcinoma'}], 'var_functions.query_db:12': [{'patient_id_prefix': 'TCGA-HW-7487'}, {'patient_id_prefix': 'TCGA-HZ-8005'}, {'patient_id_prefix': 'TCGA-HZ-A8P1'}, {'patient_id_prefix': 'TCGA-IB-7646'}, {'patient_id_prefix': 'TCGA-IB-7651'}, {'patient_id_prefix': 'TCGA-IB-7889'}, {'patient_id_prefix': 'TCGA-IB-7891'}, {'patient_id_prefix': 'TCGA-IG-A3Y9'}, {'patient_id_prefix': 'TCGA-IQ-A6SG'}, {'patient_id_prefix': 'TCGA-IR-A3LF'}, {'patient_id_prefix': 'TCGA-K4-A6MB'}, {'patient_id_prefix': 'TCGA-K4-A83P'}, {'patient_id_prefix': 'TCGA-K7-A5RG'}, {'patient_id_prefix': 'TCGA-K7-AAU7'}, {'patient_id_prefix': 'TCGA-KB-A6F7'}, {'patient_id_prefix': 'TCGA-KK-A8IM'}, {'patient_id_prefix': 'TCGA-KL-8326'}, {'patient_id_prefix': 'TCGA-KO-8403'}, {'patient_id_prefix': 'TCGA-KP-A3VZ'}, {'patient_id_prefix': 'TCGA-L5-A4OU'}], 'var_functions.query_db:15': [], 'var_functions.query_db:16': [{'ParticipantBarcode': 'TCGA-FE-A234'}, {'ParticipantBarcode': 'TCGA-FG-7637'}, {'ParticipantBarcode': 'TCGA-FG-8186'}, {'ParticipantBarcode': 'TCGA-FG-A4MU'}, {'ParticipantBarcode': 'TCGA-FI-A2D2'}, {'ParticipantBarcode': 'TCGA-FJ-A3Z9'}, {'ParticipantBarcode': 'TCGA-FR-A3R1'}, {'ParticipantBarcode': 'TCGA-FS-A1YX'}, {'ParticipantBarcode': 'TCGA-FS-A1Z3'}, {'ParticipantBarcode': 'TCGA-FS-A1ZC'}, {'ParticipantBarcode': 'TCGA-FU-A2QG'}, {'ParticipantBarcode': 'TCGA-FX-A48G'}, {'ParticipantBarcode': 'TCGA-FY-A40L'}, {'ParticipantBarcode': 'TCGA-G2-A2EJ'}, {'ParticipantBarcode': 'TCGA-G2-A2EL'}, {'ParticipantBarcode': 'TCGA-G3-A3CK'}, {'ParticipantBarcode': 'TCGA-G6-A8L8'}, {'ParticipantBarcode': 'TCGA-G7-A8LD'}, {'ParticipantBarcode': 'TCGA-G9-6333'}, {'ParticipantBarcode': 'TCGA-G9-6336'}, {'ParticipantBarcode': 'TCGA-G9-6339'}, {'ParticipantBarcode': 'TCGA-G9-6362'}, {'ParticipantBarcode': 'TCGA-GC-A3BM'}, {'ParticipantBarcode': 'TCGA-GF-A2C7'}, {'ParticipantBarcode': 'TCGA-GJ-A6C0'}, {'ParticipantBarcode': 'TCGA-GN-A265'}, {'ParticipantBarcode': 'TCGA-GU-A764'}, {'ParticipantBarcode': 'TCGA-GV-A40E'}, {'ParticipantBarcode': 'TCGA-H2-A421'}, {'ParticipantBarcode': 'TCGA-H5-A2HR'}, {'ParticipantBarcode': 'TCGA-H9-7775'}, {'ParticipantBarcode': 'TCGA-HC-7738'}, {'ParticipantBarcode': 'TCGA-HC-A9TH'}, {'ParticipantBarcode': 'TCGA-HD-7754'}, {'ParticipantBarcode': 'TCGA-HD-8314'}, {'ParticipantBarcode': 'TCGA-HD-A6HZ'}, {'ParticipantBarcode': 'TCGA-HE-A5NH'}, {'ParticipantBarcode': 'TCGA-HE-A5NK'}, {'ParticipantBarcode': 'TCGA-HF-7133'}, {'ParticipantBarcode': 'TCGA-HF-7134'}, {'ParticipantBarcode': 'TCGA-HT-7469'}, {'ParticipantBarcode': 'TCGA-HT-7478'}, {'ParticipantBarcode': 'TCGA-HT-7687'}, {'ParticipantBarcode': 'TCGA-HT-7874'}, {'ParticipantBarcode': 'TCGA-HT-7879'}, {'ParticipantBarcode': 'TCGA-HT-8105'}, {'ParticipantBarcode': 'TCGA-HT-8108'}, {'ParticipantBarcode': 'TCGA-HT-A5RC'}, {'ParticipantBarcode': 'TCGA-HT-A61B'}, {'ParticipantBarcode': 'TCGA-HU-A4GX'}], 'var_functions.query_db:18': [{'column_name': 'indisexclusion'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': [{'name': 'Mutation_Data'}, {'name': 'RNASeq_Expression'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': [{'ParticipantBarcode': 'TCGA-E1-A7YJ'}, {'ParticipantBarcode': 'TCGA-G9-6365'}, {'ParticipantBarcode': 'TCGA-WT-AB44'}, {'ParticipantBarcode': 'TCGA-CA-6717'}, {'ParticipantBarcode': 'TCGA-CG-4474'}, {'ParticipantBarcode': 'TCGA-B0-5692'}, {'ParticipantBarcode': 'TCGA-BR-A4J9'}, {'ParticipantBarcode': 'TCGA-A5-A1OF'}, {'ParticipantBarcode': 'TCGA-E9-A5FK'}, {'ParticipantBarcode': 'TCGA-77-A5G1'}, {'ParticipantBarcode': 'TCGA-A2-A0T4'}, {'ParticipantBarcode': 'TCGA-B6-A0RQ'}, {'ParticipantBarcode': 'TCGA-F1-6874'}, {'ParticipantBarcode': 'TCGA-F5-6814'}, {'ParticipantBarcode': 'TCGA-66-2759'}, {'ParticipantBarcode': 'TCGA-BR-8364'}, {'ParticipantBarcode': 'TCGA-BF-A3DL'}, {'ParticipantBarcode': 'TCGA-BR-A453'}, {'ParticipantBarcode': 'TCGA-EE-A29E'}, {'ParticipantBarcode': 'TCGA-AC-A2FF'}], 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json'}

exec(code, env_args)
