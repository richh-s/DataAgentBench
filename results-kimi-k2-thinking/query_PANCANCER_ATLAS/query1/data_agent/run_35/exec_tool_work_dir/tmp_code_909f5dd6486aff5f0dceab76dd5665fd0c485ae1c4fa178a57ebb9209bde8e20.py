code = """import os, json, re, math

# Check what files exist in /tmp
print('JSON files in /tmp:')
json_files = [f for f in os.listdir('/tmp') if f.endswith('.json')]
for f in json_files:
    filepath = f'/tmp/{f}'
    size = os.path.getsize(filepath)
    print(f'  {f} ({size} bytes)')
    
    # Load and check content
    with open(filepath, 'r') as file:
        data = json.load(file)
        print(f'    Records: {len(data)}')
        if len(data) > 0:
            print(f'    Sample: {data[0]}\n')
        else:
            print(f'    Empty file\n')

# Identify which file is which based on content
lgg_file = None
igf2_file = None

for f in json_files:
    filepath = f'/tmp/{f}'
    with open(filepath, 'r') as file:
        data = json.load(file)
        if len(data) > 0:
            # Check if it's LGG patient data (has Patient_description and histological_type)
            if 'Patient_description' in data[0] and 'histological_type' in data[0]:
                lgg_file = filepath
                print(f'LGG file identified: {f}')
            # Check if it's IGF2 expression data (has ParticipantBarcode and normalized_count)
            elif 'ParticipantBarcode' in data[0] and 'normalized_count' in data[0]:
                igf2_file = filepath
                print(f'IGF2 file identified: {f}')

if not lgg_file or not igf2_file:
    print('ERROR: Could not identify data files')
    exit(1)

# Load the data
with open(lgg_file, 'r') as f:
    lgg_patients = json.load(f)

with open(igf2_file, 'r') as f:
    igf2_expression = json.load(f)

print(f'\nLoaded {len(lgg_patients)} LGG patients')
print(f'Loaded {len(igf2_expression)} IGF2 expression records')

# Process the data
# Filter valid histologies (not in square brackets)
valid_patients = []
for p in lgg_patients:
    hist = p.get('histological_type', '')
    if hist and not (hist.startswith('[') and hist.endswith(']')):
        valid_patients.append(p)

print(f'Patients with valid histology: {len(valid_patients)}')

# Map barcodes to histology
barcode_histology = {}
for p in valid_patients:
    bc_match = re.search(r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}', p['Patient_description'])
    if bc_match:
        barcode_histology[bc_match.group(0)] = p['histological_type']

print(f'Barcodes mapped to histology: {len(barcode_histology)}')

# Group IGF2 expression by histology
histology_logs = {}
matched = 0
for rec in igf2_expression:
    bc = rec['ParticipantBarcode']
    if bc in barcode_histology:
        matched += 1
        hist = barcode_histology[bc]
        norm = float(rec['normalized_count'])
        log_val = math.log10(norm + 1)
        if hist not in histology_logs:
            histology_logs[hist] = []
        histology_logs[hist].append(log_val)

print(f'Matched patients with IGF2 data: {matched}')
print(f'Histology types: {list(histology_logs.keys())}')

# Calculate averages
results = {}
for hist, vals in histology_logs.items():
    results[hist] = round(sum(vals) / len(vals), 4)

# Format output
output = []
for hist in sorted(results.keys()):
    output.append(f"{hist}: {results[hist]:.4f}")

print("\n__RESULT__:")
print(";".join(output))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:8': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_functions.query_db:10': [], 'var_functions.query_db:12': [{'histological_type': 'Oligodendroglioma'}, {'histological_type': 'Paraganglioma'}, {'histological_type': 'Paraganglioma; Extra-adrenal Pheochromocytoma'}], 'var_functions.query_db:14': [{'Patient_description': 'Case 739CC9F1-71BE-4F81-A5D1-EDA673903E45, linked to barcode TCGA-RY-A83X, corresponds to a FEMALE patient diagnosed with Brain lower grade glioma, with vital status Alive.'}, {'Patient_description': 'The individual with barcode TCGA-FG-A60K and UUID A85AEBDA-B182-41BA-815A-3FF055E22829 is a FEMALE case of Brain lower grade glioma, documented with vital status = Alive.'}, {'Patient_description': 'Patient TCGA-DB-A4XH (UUID 5CCD86AB-2587-4F35-B96A-4F4320B10FB9) is a FEMALE diagnosed with Brain lower grade glioma. Current vital status: Alive.'}, {'Patient_description': 'Case 1701F4AD-58C5-40D8-90C4-99E3ACAC0104, linked to barcode TCGA-DB-A4XE, corresponds to a FEMALE patient diagnosed with Brain lower grade glioma, with vital status Alive.'}, {'Patient_description': 'The individual with barcode TCGA-DB-A4XC and UUID 33615113-791B-4286-A23A-AD3D1F8D4B09 is a MALE case of Brain lower grade glioma, documented with vital status = Alive.'}, {'Patient_description': 'Patient TCGA-P5-A5F0 (MALE, UUID 7EB5D055-E1C8-4B93-9205-A49A6E79DFD4) is enrolled in the study of Brain lower grade glioma. Vital status: Alive.'}, {'Patient_description': 'Patient TCGA-S9-A6U1 (UUID A5E10E2E-5157-487B-88DC-6C70AD5E244A) is a FEMALE diagnosed with Brain lower grade glioma. Current vital status: Alive.'}, {'Patient_description': 'The individual with barcode TCGA-TM-A7C3 and UUID D13AC936-87A9-4164-BDAB-02CCF3908CFE is a FEMALE case of Brain lower grade glioma, documented with vital status = Dead.'}, {'Patient_description': 'Case 8E44FB97-C649-4056-80AC-257CEF61D226, linked to barcode TCGA-S9-A7R2, corresponds to a MALE patient diagnosed with Brain lower grade glioma, with vital status Dead.'}, {'Patient_description': 'Record 21BBE030-8DBB-47EB-A670-13EB57C12159 refers to patient TCGA-TM-A84R, a MALE diagnosed with Brain lower grade glioma. Vital status recorded as Alive.'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
