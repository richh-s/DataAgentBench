code = """import json
import pandas as pd
import numpy as np
import math

# Load data
brca_result = locals()['var_functions.query_db:24']
cdh1_result = locals()['var_functions.query_db:32']

# Load JSON data
for var_name in ['brca_result', 'cdh1_result']:
    var_value = locals()[var_name]
    if isinstance(var_value, str) and var_value.endswith('.json'):
        with open(var_value, 'r') as f:
            locals()[var_name + '_data'] = json.load(f)
    else:
        locals()[var_name + '_data'] = var_value

brca_data = locals()['brca_result_data']
cdh1_data = locals()['cdh1_result_data']

# Process patients
patient_histology = []
for rec in brca_data:
    desc = rec.get('Patient_description', '')
    hist_type = rec.get('histological_type', 'Unknown')
    
    import re
    match = re.search(r'TCGA-[A-Z0-9-]+', desc)
    if match:
        barcode = match.group(0)
        patient_histology.append({
            'ParticipantBarcode': barcode,
            'histological_type': hist_type
        })

# Create DataFrames
patients_df = pd.DataFrame(patient_histology)

# Filter known histological types
patients_df = patients_df[
    (patients_df['histological_type'] != 'Unknown') & 
    (patients_df['histological_type'] != 'None')
].dropna(subset=['histological_type'])

# Process CDH1 mutations
cdh1_df = pd.DataFrame(cdh1_data)
cdh1_pass = cdh1_df[cdh1_df['FILTER'] == 'PASS'].copy()
cdh1_patients = set(cdh1_pass['ParticipantBarcode'].unique())

# Add mutation status
patients_df['CDH1_mutated'] = patients_df['ParticipantBarcode'].isin(cdh1_patients)

# Create contingency table
contingency = pd.crosstab(patients_df['histological_type'], patients_df['CDH1_mutated'])
contingency.columns = ['CDH1_Wildtype', 'CDH1_Mutated']

# Filter out rows with marginal totals <= 10
row_totals = contingency.sum(axis=1)
filtered_contingency = contingency[row_totals > 10]

# Check column totals
col_totals = filtered_contingency.sum(axis=0)

# Manually calculate chi-square test
if filtered_contingency.shape[0] >= 2 and filtered_contingency.shape[1] >= 2:
    # Convert to numpy array for calculations
    observed = filtered_contingency.values
    row_totals_np = filtered_contingency.sum(axis=1).values
    col_totals_np = filtered_contingency.sum(axis=0).values
    grand_total = observed.sum()
    
    # Calculate expected frequencies
    expected = np.outer(row_totals_np, col_totals_np) / grand_total
    
    # Calculate chi-square statistic
    chi2_stat = np.sum((observed - expected) ** 2 / expected)
    
    # Calculate degrees of freedom
    dof = (observed.shape[0] - 1) * (observed.shape[1] - 1)
    
    result = {
        'chi_square_statistic': float(chi2_stat),
        'degrees_of_freedom': int(dof),
        'contingency_table': filtered_contingency.to_dict(),
        'expected_frequencies': expected.tolist(),
        'total_patients_analyzed': int(observed.sum()),
        'histological_types_included': int(observed.shape[0]),
        'cdh1_mutated_patients': int(col_totals_np[1]),
        'cdh1_wildtype_patients': int(col_totals_np[0]),
        'row_totals': row_totals_np.tolist(),
        'col_totals': col_totals_np.tolist(),
        'grand_total': int(grand_total),
        'filter_applied': 'Excluded histological types with row totals <= 10'
    }
else:
    result = {
        'error': 'Insufficient data after filtering',
        'filtered_contingency_shape': filtered_contingency.shape
    }

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:8': [], 'var_functions.query_db:10': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': [{'ParticipantBarcode': 'TCGA-A8-A091', 'Tumor_SampleBarcode': 'TCGA-A8-A091-01A', 'Tumor_AliquotBarcode': 'TCGA-A8-A091-01A-11W-A019-09', 'Normal_SampleBarcode': 'TCGA-A8-A091-10A', 'Normal_AliquotBarcode': 'TCGA-A8-A091-10A-01W-A021-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.E243K', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.727G>A', 'CENTERS': 'MUTECT|RADIA|SOMATICSNIPER|MUSE|VARSCANS', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-A8-A0A1', 'Tumor_SampleBarcode': 'TCGA-A8-A0A1-01A', 'Tumor_AliquotBarcode': 'TCGA-A8-A0A1-01A-11W-A019-09', 'Normal_SampleBarcode': 'TCGA-A8-A0A1-10A', 'Normal_AliquotBarcode': 'TCGA-A8-A0A1-10A-01W-A021-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.Q307Hfs*2', 'Variant_Classification': 'Frame_Shift_Del', 'HGVSc': 'c.921_955delAGATCCTGAGCTCCCTGACAAAAATATGTTCACCA', 'CENTERS': 'INDELOCATOR*|VARSCANI*|PINDEL', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-A8-A0A9', 'Tumor_SampleBarcode': 'TCGA-A8-A0A9-01A', 'Tumor_AliquotBarcode': 'TCGA-A8-A0A9-01A-11W-A019-09', 'Normal_SampleBarcode': 'TCGA-A8-A0A9-10A', 'Normal_AliquotBarcode': 'TCGA-A8-A0A9-10A-01W-A021-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.Q503*', 'Variant_Classification': 'Nonsense_Mutation', 'HGVSc': 'c.1507C>T', 'CENTERS': 'SOMATICSNIPER|RADIA|MUTECT|MUSE|VARSCANS', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-AA-3821', 'Tumor_SampleBarcode': 'TCGA-AA-3821-01A', 'Tumor_AliquotBarcode': 'TCGA-AA-3821-01A-01W-0995-10', 'Normal_SampleBarcode': 'TCGA-AA-3821-10A', 'Normal_AliquotBarcode': 'TCGA-AA-3821-10A-01W-0995-10', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.V365I', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.1093G>A', 'CENTERS': 'SOMATICSNIPER|RADIA|MUTECT|MUSE|VARSCANS', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-A2-A0YL', 'Tumor_SampleBarcode': 'TCGA-A2-A0YL-01A', 'Tumor_AliquotBarcode': 'TCGA-A2-A0YL-01A-21D-A10G-09', 'Normal_SampleBarcode': 'TCGA-A2-A0YL-10A', 'Normal_AliquotBarcode': 'TCGA-A2-A0YL-10A-01D-A10G-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.T364Hfs*4', 'Variant_Classification': 'Frame_Shift_Del', 'HGVSc': 'c.1090_1100delACAGTCACTGA', 'CENTERS': 'INDELOCATOR*|PINDEL', 'FILTER': 'PASS'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:30': {'count': 1075, 'sample': {'Patient_description': 'Clinical entry D13FB44B-291B-4EA4-920C-142DAA8D1989 identifies patient TCGA-AC-A5EH, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:34': {'total_female_brca': 1075, 'sample_patient': {'ParticipantBarcode': 'TCGA-AC-A5EH', 'histological_type': 'Infiltrating Ductal Carcinoma'}}, 'var_functions.execute_python:36': {'female_brca_total': 1075, 'with_known_histology': 1074, 'cdh1_mutations_total': 318, 'cdh1_pass_mutations': 261, 'cdh1_mutated_patients': 247, 'sample_patients': [{'ParticipantBarcode': 'TCGA-AC-A5EH', 'histological_type': 'Infiltrating Ductal Carcinoma', 'CDH1_mutated': False}, {'ParticipantBarcode': 'TCGA-LL-A7SZ', 'histological_type': 'Infiltrating Ductal Carcinoma', 'CDH1_mutated': False}, {'ParticipantBarcode': 'TCGA-AN-A0FY', 'histological_type': 'Infiltrating Ductal Carcinoma', 'CDH1_mutated': False}]}}

exec(code, env_args)
