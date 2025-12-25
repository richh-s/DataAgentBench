code = """import pandas as pd
import json
import re

clinical_path = locals()['var_function-call-12490264463406204080']
mutation_path = locals()['var_function-call-12490264463406205985']
clinical_data = json.load(open(clinical_path))
mutation_data = json.load(open(mutation_path))
cdh1_barcodes = set([item['ParticipantBarcode'] for item in mutation_data])

processed_records = []

for record in clinical_data:
    desc = record['Patient_description']
    hist_type = record['histological_type']
    
    # Check for Bladder cancer or BRCA hint
    is_target = False
    if "bladder" in desc.lower():
        is_target = True
    elif "brca" in desc.lower(): # Case insensitive check for BRCA
        is_target = True
    
    if not is_target:
        continue

    # Extract Vital Status
    status_match = re.search(r'vital status\s*(?:=|:|recorded as)\s*([A-Za-z]+)', desc, re.IGNORECASE)
    if not status_match:
        continue
    status = status_match.group(1).title()
    
    if status == 'Alive':
        # Extract Barcode
        barcode_match = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', desc)
        if not barcode_match:
            continue
        barcode = barcode_match.group(1)
        
        has_mutation = barcode in cdh1_barcodes
        processed_records.append({
            'histological_type': hist_type,
            'has_mutation': has_mutation
        })

df = pd.DataFrame(processed_records)

# Filter out 'None'
df = df[df['histological_type'].notna() & (df['histological_type'] != 'None')]

if df.empty:
    print("__RESULT__:")
    print(json.dumps([]))
else:
    result = df.groupby('histological_type').agg(
        total_count=('has_mutation', 'count'),
        mutation_count=('has_mutation', 'sum')
    )
    result['percentage'] = (result['mutation_count'] / result['total_count']) * 100
    
    # Sort
    top_3 = result.sort_values(by='percentage', ascending=False).head(3)
    
    output = top_3.reset_index()[['histological_type', 'percentage']].to_dict(orient='records')
    print("__RESULT__:")
    print(json.dumps(output))"""

env_args = {'var_function-call-4296324932446097147': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_function-call-4296324932446096622': [{'ParticipantBarcode': 'TCGA-AX-A3G8', 'Tumor_SampleBarcode': 'TCGA-AX-A3G8-01A', 'Tumor_AliquotBarcode': 'TCGA-AX-A3G8-01A-11D-A228-09', 'Normal_SampleBarcode': 'TCGA-AX-A3G8-10A', 'Normal_AliquotBarcode': 'TCGA-AX-A3G8-10A-01D-A22A-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'GLI3', 'HGVSp_Short': 'p.P1033Rfs*46', 'Variant_Classification': 'Frame_Shift_Del', 'HGVSc': 'c.3098delC', 'CENTERS': 'INDELOCATOR|VARSCANI', 'FILTER': 'ndp'}], 'var_function-call-1747832039180313026': [{'count': '10761'}], 'var_function-call-12490264463406204080': 'file_storage/function-call-12490264463406204080.json', 'var_function-call-12490264463406205985': 'file_storage/function-call-12490264463406205985.json', 'var_function-call-14328409868447232391': [{'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'percentage': 2.73972602739726}, {'histological_type': 'None', 'percentage': 0.0}]}

exec(code, env_args)
