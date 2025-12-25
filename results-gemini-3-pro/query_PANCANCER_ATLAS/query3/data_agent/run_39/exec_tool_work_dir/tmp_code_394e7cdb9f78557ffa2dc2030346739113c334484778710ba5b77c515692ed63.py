code = """import json
import pandas as pd
import re

try:
    mutation_file_path = locals()['var_function-call-13997121369006260002']
    clinical_file_path = locals()['var_function-call-10252881042370382474']

    with open(mutation_file_path, 'r') as f:
        mutation_data = json.load(f)
    mutation_barcodes = set(item['ParticipantBarcode'] for item in mutation_data)

    with open(clinical_file_path, 'r') as f:
        clinical_data = json.load(f)

    def extract_info(desc):
        barcode_match = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', desc)
        barcode = barcode_match.group(1) if barcode_match else None
        
        dataset = None
        desc_lower = desc.lower()
        if "breast invasive carcinoma" in desc_lower:
            dataset = "Breast Invasive Carcinoma"
        elif "bladder urothelial carcinoma" in desc_lower:
            dataset = "Bladder Urothelial Carcinoma"
            
        return barcode, dataset

    parsed_data = []
    for entry in clinical_data:
        desc = entry['Patient_description']
        hist = entry['histological_type']
        bc, ds = extract_info(desc)
        if bc and ds:
            parsed_data.append({
                "hist": hist,
                "mut": bc in mutation_barcodes,
                "ds": ds
            })
    
    # Use Breast Invasive Carcinoma
    target = "Breast Invasive Carcinoma"
    df = pd.DataFrame([p for p in parsed_data if p['ds'] == target])
    
    # Filter types > 10
    if not df.empty:
        hist_counts = {}
        for h in df['hist']:
            hist_counts[h] = hist_counts.get(h, 0) + 1
        
        valid_hists = {h for h, c in hist_counts.items() if c > 10}
        df_final = df[df['hist'].isin(valid_hists)]
        
        # Contingency table
        # We need counts for (Hist, Mutated) and (Hist, Not Mutated)
        table = {h: {False: 0, True: 0} for h in valid_hists}
        for _, row in df_final.iterrows():
            h = row['hist']
            m = row['mut']
            table[h][m] += 1
            
        # Prepare matrix
        hists_sorted = sorted(list(valid_hists))
        observed = []
        for h in hists_sorted:
            observed.append([table[h][False], table[h][True]])
            
        # Chi2 Calculation
        grand_total = sum(sum(row) for row in observed)
        row_totals = [sum(row) for row in observed]
        col_totals = [sum(row[i] for row in observed) for i in range(2)]
        
        chi2 = 0
        for i in range(len(observed)):
            for j in range(2):
                O = observed[i][j]
                E = (row_totals[i] * col_totals[j]) / grand_total
                if E > 0:
                    chi2 += ((O - E)**2) / E
                    
        print("__RESULT__:")
        print(json.dumps({
            "chi2": chi2,
            "dataset": target,
            "table": table,
            "dof": (len(observed)-1)*(2-1)
        }))
    else:
        print("__RESULT__:")
        print(json.dumps({"error": "No data for Breast"}))

except Exception as e:
    print("__RESULT__:")
    print(json.dumps({"error": str(e)}))"""

env_args = {'var_function-call-6366351482672258515': ['clinical_info'], 'var_function-call-4090389325294480539': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_function-call-13997121369006260002': 'file_storage/function-call-13997121369006260002.json', 'var_function-call-10252881042370382474': 'file_storage/function-call-10252881042370382474.json', 'var_function-call-6394138374943278716': {'chi2': 0.0, 'dataset': 'Bladder Urothelial Carcinoma', 'table': {'Muscle invasive urothelial carcinoma (pT2 or above)': {'false': 102, 'true': 6}}}, 'var_function-call-9819989052447950507': {'Bladder Urothelial Carcinoma': {'Muscle invasive urothelial carcinoma (pT2 or above)': 108}, 'Breast Invasive Carcinoma': {'Infiltrating Ductal Carcinoma': 766, 'Infiltrating Lobular Carcinoma': 201, 'Other  specify': 45, 'Mixed Histology (please specify)': 30, 'Mucinous Carcinoma': 17, 'Metaplastic Carcinoma': 8, 'Medullary Carcinoma': 6, 'Infiltrating Carcinoma NOS': 1, 'None': 1}}}

exec(code, env_args)
