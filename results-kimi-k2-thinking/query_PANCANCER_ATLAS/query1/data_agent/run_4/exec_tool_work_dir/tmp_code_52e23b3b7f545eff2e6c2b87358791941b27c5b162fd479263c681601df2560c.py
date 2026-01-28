code = """import json
import re

# Read the LGG patients data from file
lgg_file_path = locals()['var_functions.query_db:16']
with open(lgg_file_path, 'r') as f:
    lgg_patients_raw = json.load(f)

# Read the IGF2 expression data from file
igf2_file_path = locals()['var_functions.query_db:14']
with open(igf2_file_path, 'r') as f:
    igf2_expression_raw = json.load(f)

# Extract LGG patient info with barcode and histology
lgg_patients = []
for record in lgg_patients_raw:
    patient_desc = record['Patient_description']
    hist_type = record['histological_type']
    
    # Extract barcode from patient description using regex
    barcode_match = re.search(r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}', patient_desc)
    if barcode_match:
        barcode = barcode_match.group(0)
        # Skip histology types enclosed in brackets
        if hist_type and not (hist_type.startswith('[') and hist_type.endswith(']')):
            lgg_patients.append({
                'ParticipantBarcode': barcode,
                'histological_type': hist_type
            })

# Create a dictionary of IGF2 expression values
igf2_dict = {}
for record in igf2_expression_raw:
    barcode = record['ParticipantBarcode']
    # Convert normalized_count to float
    try:
        norm_count = float(record['normalized_count'])
        igf2_dict[barcode] = norm_count
    except (ValueError, TypeError):
        continue

# Find LGG patients with IGF2 expression data
lgg_with_igf2 = []
for patient in lgg_patients:
    barcode = patient['ParticipantBarcode']
    if barcode in igf2_dict:
        lgg_with_igf2.append({
            'ParticipantBarcode': barcode,
            'histological_type': patient['histological_type'],
            'igf2_expression': igf2_dict[barcode]
        })

# Group by histology type and compute average log10 expression
from collections import defaultdict
import math

histology_groups = defaultdict(list)
for patient in lgg_with_igf2:
    hist_type = patient['histological_type']
    expr = patient['igf2_expression']
    log_expr = math.log10(expr + 1)  # log10(normalized_count + 1)
    histology_groups[hist_type].append(log_expr)

# Compute averages
averages = {}
for hist_type, log_values in histology_groups.items():
    if log_values:  # Only include if there are valid values
        avg = sum(log_values) / len(log_values)
        averages[hist_type] = {
            'average_log10_expression': round(avg, 4),
            'sample_count': len(log_values)
        }

print('__RESULT__:')
print(json.dumps({
    'total_lgg_patients': len(lgg_patients),
    'lgg_with_igf2_expression': len(lgg_with_igf2),
    'histology_type_averages': averages,
    'histology_types_found': list(histology_groups.keys())
}, indent=2))"""

env_args = {'var_functions.query_db:0': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_functions.query_db:2': [], 'var_functions.query_db:5': [], 'var_functions.query_db:6': [{'diagnosis': 'Lung Adenocarcinoma'}, {'diagnosis': 'Lung Squamous Cell Carcinoma'}, {'diagnosis': 'None'}], 'var_functions.query_db:8': [{'histological_type': 'Adenosquamous'}, {'histological_type': 'Adrenocortical Carcinoma- Myxoid Type'}, {'histological_type': 'Adrenocortical Carcinoma- Oncocytic Type'}, {'histological_type': 'Adrenocortical carcinoma- Usual Type'}, {'histological_type': 'Astrocytoma'}, {'histological_type': 'Biphasic mesothelioma'}, {'histological_type': 'Cervical Squamous Cell Carcinoma'}, {'histological_type': 'Cholangiocarcinoma; distal'}, {'histological_type': 'Cholangiocarcinoma; hilar/perihilar'}, {'histological_type': 'Cholangiocarcinoma; intrahepatic'}, {'histological_type': 'Colon Adenocarcinoma'}, {'histological_type': 'Colon Mucinous Adenocarcinoma'}, {'histological_type': 'Dedifferentiated liposarcoma'}, {'histological_type': 'Desmoid Tumor'}, {'histological_type': 'Diffuse large B-cell lymphoma (DLBCL) NOS (any anatomic site nodal or extranodal)'}, {'histological_type': 'Diffuse malignant mesothelioma - NOS'}, {'histological_type': 'Endocervical Adenocarcinoma of the Usual Type'}, {'histological_type': 'Endocervical Type of Adenocarcinoma'}, {'histological_type': 'Endometrioid Adenocarcinoma of Endocervix'}, {'histological_type': 'Endometrioid endometrial adenocarcinoma'}, {'histological_type': 'Epithelioid mesothelioma'}, {'histological_type': 'Esophagus Adenocarcinoma  NOS'}, {'histological_type': 'Esophagus Squamous Cell Carcinoma'}, {'histological_type': 'Fibrolamellar Carcinoma'}, {'histological_type': "Giant cell 'MFH' / Undifferentiated pleomorphic sarcoma with giant cells"}, {'histological_type': 'Glioblastoma Multiforme (GBM)'}, {'histological_type': 'Head and Neck Squamous Cell Carcinoma'}, {'histological_type': 'Head and Neck Squamous Cell Carcinoma  Spindle Cell Variant'}, {'histological_type': 'Head and Neck Squamous Cell Carcinoma Basaloid Type'}, {'histological_type': 'Hepatocellular Carcinoma'}], 'var_functions.query_db:10': [{'Patient_description': 'Case 739CC9F1-71BE-4F81-A5D1-EDA673903E45, linked to barcode TCGA-RY-A83X, corresponds to a FEMALE patient diagnosed with Brain lower grade glioma, with vital status Alive.', 'histological_type': 'Oligodendroglioma'}, {'Patient_description': 'The individual with barcode TCGA-FG-A60K and UUID A85AEBDA-B182-41BA-815A-3FF055E22829 is a FEMALE case of Brain lower grade glioma, documented with vital status = Alive.', 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': 'Patient TCGA-DB-A4XH (UUID 5CCD86AB-2587-4F35-B96A-4F4320B10FB9) is a FEMALE diagnosed with Brain lower grade glioma. Current vital status: Alive.', 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': 'Case 1701F4AD-58C5-40D8-90C4-99E3ACAC0104, linked to barcode TCGA-DB-A4XE, corresponds to a FEMALE patient diagnosed with Brain lower grade glioma, with vital status Alive.', 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': 'The individual with barcode TCGA-DB-A4XC and UUID 33615113-791B-4286-A23A-AD3D1F8D4B09 is a MALE case of Brain lower grade glioma, documented with vital status = Alive.', 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': 'Patient TCGA-P5-A5F0 (MALE, UUID 7EB5D055-E1C8-4B93-9205-A49A6E79DFD4) is enrolled in the study of Brain lower grade glioma. Vital status: Alive.', 'histological_type': 'Oligodendroglioma'}, {'Patient_description': 'Record 21BBE030-8DBB-47EB-A670-13EB57C12159 refers to patient TCGA-TM-A84R, a MALE diagnosed with Brain lower grade glioma. Vital status recorded as Alive.', 'histological_type': 'Oligodendroglioma'}, {'Patient_description': 'Patient TCGA-DH-A7US (MALE, UUID 82FD02AB-D628-469F-8853-4C603CF04964) is enrolled in the study of Brain lower grade glioma. Vital status: Alive.', 'histological_type': 'Oligodendroglioma'}, {'Patient_description': 'Patient TCGA-P5-A5F4 (FEMALE, UUID 0557B788-5AED-4919-85EB-A503AD893D75) is enrolled in the study of Brain lower grade glioma. Vital status: Alive.', 'histological_type': 'Oligodendroglioma'}, {'Patient_description': 'Patient TCGA-FG-7637 (MALE, UUID c40ab957-fe46-43b1-992d-b4e2040a3f57) is enrolled in the study of Brain lower grade glioma. Vital status: Alive.', 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': "Patient TCGA-FG-A4MW, registered under UUID DCE168B1-D2A9-4409-8437-AB382F6D7D31, belongs to the Brain lower grade glioma cohort. This MALE patient's vital status is Dead.", 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': "Patient TCGA-S9-A6TV, registered under UUID 048056CD-39DD-4134-A58B-70BEBB3DD2FF, belongs to the Brain lower grade glioma cohort. This MALE patient's vital status is Alive.", 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': 'Record 9B161C41-4F76-4ED1-B60F-2B093BC70EDB refers to patient TCGA-TM-A84L, a MALE diagnosed with Brain lower grade glioma. Vital status recorded as Dead.', 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': "Patient TCGA-IK-7675, registered under UUID a5f851c5-6130-4ea1-9f86-be59331a92f7, belongs to the Brain lower grade glioma cohort. This MALE patient's vital status is Dead.", 'histological_type': 'Oligodendroglioma'}, {'Patient_description': 'Clinical entry 5b9d7565-a933-449d-8ffa-ec5f82db2e77 identifies patient TCGA-FN-7833, a MALE subject with Brain lower grade glioma. Their current vital status is Alive.', 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': 'Patient TCGA-HW-A5KJ (MALE, UUID 8996DC64-8C5E-4E07-8ED8-2EB11C03626B) is enrolled in the study of Brain lower grade glioma. Vital status: Dead.', 'histological_type': 'Oligodendroglioma'}, {'Patient_description': 'Case dcd45077-f068-490b-bdcc-4d4a62285116, linked to barcode TCGA-FG-8186, corresponds to a FEMALE patient diagnosed with Brain lower grade glioma, with vital status Alive.', 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': 'In the Brain lower grade glioma dataset, patient TCGA-S9-A7J3 (UUID 032096A6-1923-44B9-A1CB-181BED041C8E) is recorded as a FEMALE with vital status: Alive.', 'histological_type': 'Oligodendroglioma'}, {'Patient_description': 'The individual with barcode TCGA-DB-A4XG and UUID 7704E4A8-C7AA-4288-B1ED-68C23ABBE924 is a MALE case of Brain lower grade glioma, documented with vital status = Alive.', 'histological_type': 'Oligodendroglioma'}, {'Patient_description': 'Patient TCGA-VM-A8CA (UUID CDD1FD4C-3427-496C-8391-4AEB6730D3CC) is a MALE diagnosed with Brain lower grade glioma. Current vital status: Alive.', 'histological_type': 'Oligodendroglioma'}], 'var_functions.execute_python:12': {'patient_count': 20, 'sample_barcodes': ['TCGA-RY-A83X', 'TCGA-FG-A60K', 'TCGA-DB-A4XH', 'TCGA-DB-A4XE', 'TCGA-DB-A4XC', 'TCGA-P5-A5F0', 'TCGA-TM-A84R', 'TCGA-DH-A7US', 'TCGA-P5-A5F4', 'TCGA-FG-7637'], 'sample_hist_types': ['Oligodendroglioma', 'Oligoastrocytoma', 'Oligoastrocytoma', 'Oligoastrocytoma', 'Oligoastrocytoma', 'Oligodendroglioma', 'Oligodendroglioma', 'Oligodendroglioma', 'Oligodendroglioma', 'Oligoastrocytoma'], 'all_hist_types': ['Oligoastrocytoma', 'Oligodendroglioma']}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
