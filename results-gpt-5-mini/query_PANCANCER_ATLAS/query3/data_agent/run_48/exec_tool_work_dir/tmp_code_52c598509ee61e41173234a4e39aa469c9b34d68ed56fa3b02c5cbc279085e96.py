code = """import json
import pandas as pd
import re

# Load previous tool results from storage-provided variables
clinical_path = var_call_gX2T6arGf1RrLlJgtFlue4SA
mutations_path = var_call_PfXFZKEvcBidc3OsZ0iuFour

with open(clinical_path, 'r') as f:
    clinical = json.load(f)
with open(mutations_path, 'r') as f:
    mutations = json.load(f)

# Extract barcode from Patient_description
pattern = re.compile(r'(TCGA-[A-Z0-9]+-[A-Z0-9]+)', re.IGNORECASE)

records = []
for rec in clinical:
    pd_desc = rec.get('Patient_description', '')
    hist = rec.get('histological_type')
    m = pattern.search(pd_desc)
    if m and hist and hist.strip():
        barcode = m.group(1).upper()
        records.append({'barcode': barcode, 'histological_type': hist.strip()})

# Build clinical dataframe
df_clin = pd.DataFrame(records)
if df_clin.empty:
    result = {'error': 'No clinical BRCA female records with histological_type found.'}
    print("__RESULT__:")
    print(json.dumps(result))
else:
    # Deduplicate by barcode, keep first
    df_clin = df_clin.drop_duplicates(subset=['barcode'], keep='first').reset_index(drop=True)

    # Build mutated barcode set from mutations (already filtered to CDH1 PASS via query)
    mutated = set()
    for m in mutations:
        pb = m.get('ParticipantBarcode')
        if pb:
            mutated.add(pb.upper())

    # Map mutation presence
    df_clin['mutated'] = df_clin['barcode'].apply(lambda x: 1 if x in mutated else 0)

    # Filter out unknown or vague histological_type entries
    exclude_hist = set(['Other  specify', 'Other specify', 'Unknown', 'Not Reported', ''])
    df_clin = df_clin[~df_clin['histological_type'].isin(exclude_hist)].copy()

    # Build contingency table
    agg = df_clin.groupby('histological_type').agg(total=('barcode','count'), mutated=('mutated','sum')).reset_index()
    agg['not_mutated'] = agg['total'] - agg['mutated']

    # Exclude categories with marginal totals <= 10
    agg_filtered = agg[agg['total'] > 10].copy()

    if agg_filtered.empty:
        result = {'error': 'No histological categories with total > 10 after filtering.'}
        print("__RESULT__:")
        print(json.dumps(result))
    else:
        # Build contingency matrix
        mutated_total = int(agg_filtered['mutated'].sum())
        not_mutated_total = int(agg_filtered['not_mutated'].sum())
        grand_total = mutated_total + not_mutated_total

        chi2 = 0.0
        rows = []
        for _, row in agg_filtered.iterrows():
            r_total = int(row['total'])
            r_mut = int(row['mutated'])
            r_not = int(row['not_mutated'])
            # expected
            exp_mut = r_total * (mutated_total / grand_total)
            exp_not = r_total * (not_mutated_total / grand_total)
            term_mut = ((r_mut - exp_mut) ** 2) / exp_mut if exp_mut > 0 else 0.0
            term_not = ((r_not - exp_not) ** 2) / exp_not if exp_not > 0 else 0.0
            chi2 += term_mut + term_not
            rows.append({'histological_type': row['histological_type'], 'mutated': r_mut, 'not_mutated': r_not, 'total': r_total,
                         'expected_mutated': exp_mut, 'expected_not_mutated': exp_not})

        result = {'chi2': chi2, 'grand_total': grand_total, 'col_totals': {'mutated': mutated_total, 'not_mutated': not_mutated_total}, 'rows': rows}
        print("__RESULT__:")
        print(json.dumps(result))"""

env_args = {'var_call_HyLuNpvgJ9i3xMuMxrcux6dg': ['clinical_info'], 'var_call_RbEW1w2fywpigFYlP456KpQL': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_T2zJq28s9Dh9hGgKb710liee': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_y0gDVXLCutkwHBt3h31YCGf0': [], 'var_call_0s4ImlzDHbFy41ejB7XOoDYI': [{'diagnosis': 'Lung Squamous Cell Carcinoma'}, {'diagnosis': 'Lung Adenocarcinoma'}], 'var_call_bd71BZjlHMjwmiOiSgrjbVOx': 'file_storage/call_bd71BZjlHMjwmiOiSgrjbVOx.json', 'var_call_rMIKEMn5Vcw066On8iOl2fmv': [{'diagnosis': 'None'}], 'var_call_co4uGzQFQSHBYRzV0Swi0oD6': 'file_storage/call_co4uGzQFQSHBYRzV0Swi0oD6.json', 'var_call_PfXFZKEvcBidc3OsZ0iuFour': 'file_storage/call_PfXFZKEvcBidc3OsZ0iuFour.json', 'var_call_gX2T6arGf1RrLlJgtFlue4SA': 'file_storage/call_gX2T6arGf1RrLlJgtFlue4SA.json'}

exec(code, env_args)
