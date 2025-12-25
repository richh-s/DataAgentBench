code = """import json
import pandas as pd
import re

# Get file paths from variables
mutation_file_path = locals()['var_function-call-13997121369006260002']
clinical_file_path = locals()['var_function-call-10252881042370382474']

# Load mutation data
with open(mutation_file_path, 'r') as f:
    mutation_data = json.load(f)
mutation_barcodes = set(item['ParticipantBarcode'] for item in mutation_data)

# Load clinical data
with open(clinical_file_path, 'r') as f:
    clinical_data = json.load(f)

def extract_info(desc):
    # Extract barcode
    barcode_match = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', desc)
    barcode = barcode_match.group(1) if barcode_match else None
    
    dataset = None
    desc_lower = desc.lower()
    
    if "ovarian serous cystadenocarcinoma" in desc_lower:
        dataset = "Ovarian Serous Cystadenocarcinoma"
    elif "bladder urothelial carcinoma" in desc_lower:
        dataset = "Bladder Urothelial Carcinoma"
    elif "breast invasive carcinoma" in desc_lower:
        dataset = "Breast Invasive Carcinoma"
    elif "brain lower grade glioma" in desc_lower:
        dataset = "Brain Lower Grade Glioma"
    else:
        # Fallback regex
        if "dataset" in desc:
            m = re.search(r'In the ([\w\s]+) dataset', desc)
            if m: dataset = m.group(1)
            
    if dataset:
        dataset = dataset.strip()
        
    return barcode, dataset

parsed_data = []
datasets_found = set()

for entry in clinical_data:
    desc = entry['Patient_description']
    hist_type = entry['histological_type']
    barcode, dataset = extract_info(desc)
    
    if barcode and dataset:
        parsed_data.append({
            'barcode': barcode,
            'dataset': dataset,
            'hist_type': hist_type,
            'has_mutation': barcode in mutation_barcodes
        })
        datasets_found.add(dataset)

# Target: BRCA means Bladder urothelial carcinoma (per hint)
target_dataset = None
for d in datasets_found:
    if "Bladder Urothelial Carcinoma" == d:
        target_dataset = d
        break

# If not found, check Breast
if not target_dataset:
    for d in datasets_found:
        if "Breast Invasive Carcinoma" == d:
            target_dataset = d
            break

if target_dataset:
    df = pd.DataFrame([d for d in parsed_data if d['dataset'] == target_dataset])

    # Filter histological types
    df = df[df['hist_type'].notna() & (df['hist_type'] != 'None')]
    type_counts = df['hist_type'].value_counts()
    valid_types = type_counts[type_counts > 10].index.tolist()
    df_filtered = df[df['hist_type'].isin(valid_types)]

    # Crosstab
    ct = pd.crosstab(df_filtered['hist_type'], df_filtered['has_mutation'])

    # Ensure columns
    if not ct.empty:
        if False not in ct.columns:
            ct[False] = 0
        if True not in ct.columns:
            ct[True] = 0
        ct = ct[[False, True]]
        
        observed = ct.values
        row_totals = observed.sum(axis=1)
        col_totals = observed.sum(axis=0)
        grand_total = observed.sum()
        
        expected = []
        chi2 = 0
        for i in range(len(row_totals)):
            for j in range(len(col_totals)):
                if grand_total > 0:
                    E = (row_totals[i] * col_totals[j]) / grand_total
                    O = observed[i][j]
                    if E > 0:
                        chi2 += ((O - E) ** 2) / E
        
        result = {
            "chi2": chi2,
            "dataset": target_dataset,
            "counts": ct.to_dict()
        }
    else:
        result = {"error": "Empty contingency table", "dataset": target_dataset}
else:
    result = {"error": "Target dataset not found", "available": list(datasets_found)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-6366351482672258515': ['clinical_info'], 'var_function-call-4090389325294480539': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_function-call-13997121369006260002': 'file_storage/function-call-13997121369006260002.json', 'var_function-call-10252881042370382474': 'file_storage/function-call-10252881042370382474.json'}

exec(code, env_args)
