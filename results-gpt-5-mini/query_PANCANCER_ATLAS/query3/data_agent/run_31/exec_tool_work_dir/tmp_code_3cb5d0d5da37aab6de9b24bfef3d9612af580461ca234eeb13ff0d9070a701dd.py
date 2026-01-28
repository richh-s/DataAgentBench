code = """import json, os, re
import pandas as pd

# Load clinical data from storage var_call_KmGsPB4MYwdWhgp4gf6nUQdW
clin_var = var_call_KmGsPB4MYwdWhgp4gf6nUQdW
if isinstance(clin_var, str) and os.path.exists(clin_var):
    with open(clin_var, 'r') as f:
        clinical = json.load(f)
else:
    clinical = clin_var

# Load mutation data from storage var_call_eCMxPYh97ZbtYPgBbiSrKRSi
mut_var = var_call_eCMxPYh97ZbtYPgBbiSrKRSi
if isinstance(mut_var, str) and os.path.exists(mut_var):
    with open(mut_var, 'r') as f:
        mutations = json.load(f)
else:
    mutations = mut_var

# Compile barcode regex
barcode_re = re.compile(r'(TCGA-[A-Za-z0-9]{2}-[A-Za-z0-9]{4,6})')

records = []
for rec in clinical:
    pd_desc = rec.get('Patient_description', '')
    if not pd_desc:
        continue
    # filter for breast and FEMALE
    if 'breast' in pd_desc.lower() and 'FEMALE' in pd_desc.upper():
        m = barcode_re.search(pd_desc)
        if not m:
            continue
        barcode = m.group(1)
        hist = rec.get('histological_type')
        if hist is None:
            continue
        hist_str = str(hist).strip()
        if hist_str == '' or hist_str.lower().startswith('other'):
            continue
        records.append({'ParticipantBarcode': barcode, 'histological_type': hist_str})

# Deduplicate by barcode keeping first
if len(records) == 0:
    result = {'error': 'No female BRCA clinical records with known histological_type found after corrected filtering.'}
    print('__RESULT__:')
    print(json.dumps(result))
else:
    df_clin = pd.DataFrame(records).drop_duplicates(subset=['ParticipantBarcode'])

    # reliable mutations: FILTER == 'PASS' (case-insensitive)
    mutated_barcodes = set()
    for m in mutations:
        filt = str(m.get('FILTER','')).upper()
        if filt == 'PASS':
            pb = m.get('ParticipantBarcode')
            if pb:
                mutated_barcodes.add(pb)

    df_clin['mutated'] = df_clin['ParticipantBarcode'].apply(lambda x: x in mutated_barcodes)

    cont = df_clin.groupby(['histological_type','mutated']).size().unstack(fill_value=0)
    # Ensure both mutated True/False present
    for col in [False, True]:
        if col not in cont.columns:
            cont[col] = 0
    cont = cont.sort_index(axis=1)
    cont = cont.rename(columns={True: 'mutated', False: 'not_mutated'})

    cont['row_total'] = cont['mutated'] + cont['not_mutated']
    # Exclude categories with marginal totals <= 10
    cont_filtered = cont[cont['row_total'] > 10].copy()

    grand_total = int(cont_filtered['row_total'].sum())

    if grand_total == 0 or cont_filtered.shape[0] == 0:
        result = {'error': 'No histological categories remain after excluding marginal totals <= 10.'}
        print('__RESULT__:')
        print(json.dumps(result))
    else:
        mutated_total = int(cont_filtered['mutated'].sum())
        not_mut_total = int(cont_filtered['not_mutated'].sum())
        chi2 = 0.0
        for idx, row in cont_filtered.iterrows():
            for col in ['mutated','not_mutated']:
                O = float(row[col])
                col_total = mutated_total if col=='mutated' else not_mut_total
                row_total = float(row['row_total'])
                E = (row_total * col_total) / float(grand_total) if grand_total>0 else 0.0
                if E > 0:
                    chi2 += (O - E)**2 / E
        df = (cont_filtered.shape[0] - 1) * (2 - 1)

        table_dict = {}
        for idx, row in cont_filtered.iterrows():
            table_dict[idx] = {'mutated': int(row['mutated']), 'not_mutated': int(row['not_mutated']), 'row_total': int(row['row_total'])}

        excluded = []
        for idx, row in cont.iterrows():
            if row['row_total'] <= 10:
                excluded.append({'histological_type': idx, 'row_total': int(row['row_total'])})

        result = {
            'chi2': round(chi2, 6),
            'df': int(df),
            'grand_total': grand_total,
            'contingency_table': table_dict,
            'excluded_histological_types_marginal_<=10': excluded
        }
        print('__RESULT__:')
        print(json.dumps(result))"""

env_args = {'var_call_WfaCfJAknZEYsE1AzCo1VO2N': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_GH7JjqHLk0A7WKqMGgJLewbm': [], 'var_call_HYRwR7jR38nUQRsM5c6E0RrA': 'file_storage/call_HYRwR7jR38nUQRsM5c6E0RrA.json', 'var_call_Wpwep3E67aegIpIcWxGl9Rfq': [{'count': '0'}], 'var_call_KwCk4LHWzgYftU9n7QPGyxc8': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_eCMxPYh97ZbtYPgBbiSrKRSi': 'file_storage/call_eCMxPYh97ZbtYPgBbiSrKRSi.json', 'var_call_KmGsPB4MYwdWhgp4gf6nUQdW': 'file_storage/call_KmGsPB4MYwdWhgp4gf6nUQdW.json', 'var_call_kr9qDSrwaI6fSajteplySkq2': {'error': 'No female BRCA clinical records with known histological_type found.'}}

exec(code, env_args)
