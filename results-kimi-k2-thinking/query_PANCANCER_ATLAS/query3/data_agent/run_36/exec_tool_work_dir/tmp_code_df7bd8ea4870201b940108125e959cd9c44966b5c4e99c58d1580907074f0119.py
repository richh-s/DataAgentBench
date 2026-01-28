code = """import json
import pandas as pd
import numpy as np

# Load clinical data (female BRCA patients with histology)
clinical_file = '/mnt/data/tmpbuew5n4.json'
with open(clinical_file, 'r') as f:
    clinical_data = json.load(f)

# Load CDH1 mutation data (reliable PASS mutations)
mutation_file = '/mnt/data/tmp2k8p0x0g.json'
with open(mutation_file, 'r') as f:
    mutation_data = json.load(f)

# Convert to DataFrames
df_clinical = pd.DataFrame(clinical_data)
df_mutations = pd.DataFrame(mutation_data)

# Create a set of patients with CDH1 mutations
cdh1_mutated_patients = set(df_mutations['ParticipantBarcode'].tolist())

# Add mutation status to clinical data
df_clinical['has_cdh1_mutation'] = df_clinical['barcode'].isin(cdh1_mutated_patients)

# Filter for valid histological types only
df_clinical_filtered = df_clinical[
    (df_clinical['histology'].notna()) & 
    (df_clinical['histology'] != '') &
    (~df_clinical['histology'].str.contains('Other', na=False)) &
    (df_clinical['histology'] != 'Mixed Histology (please specify)') &
    (df_clinical['histology'] != 'Infiltrating Carcinoma NOS')
].copy()

# Create contingency table
def create_and_filter_contingency(df):
    """Create contingency table and filter categories with row totals <= 10"""
    # Create raw contingency table
    contingency_raw = pd.crosstab(
        df['histology'],
        df['has_cdh1_mutation'],
        dropna=False
    )
    
    # Add missing columns if needed
    if 0 not in contingency_raw.columns:
        contingency_raw[0] = 0
    if 1 not in contingency_raw.columns:
        contingency_raw[1] = 0
    
    # Rename columns for clarity
    contingency_raw = contingency_raw.rename(columns={0: 'No CDH1 Mutation', 1: 'CDH1 Mutation'})
    
    # Calculate row totals and filter
    row_totals = contingency_raw.sum(axis=1)
    contingency_filtered = contingency_raw[row_totals > 10]
    
    return contingency_raw, contingency_filtered, row_totals

# Get contingency tables
contingency_raw, contingency_filtered, row_totals = create_and_filter_contingency(df_clinical_filtered)

# Summary statistics
total_patients = len(df_clinical_filtered)
total_with_mutations = df_clinical_filtered['has_cdh1_mutation'].sum()
categories_before = len(contingency_raw)
categories_after = len(contingency_filtered)

# Calculate chi-square statistic if we have sufficient data
if contingency_filtered.shape[0] >= 2:
    # Get observed frequencies
    observed = contingency_filtered.values
    
    # Calculate expected frequencies: Eij = (row_total * col_total) / grand_total
    row_totals_arr = contingency_filtered.sum(axis=1).values
    col_totals_arr = contingency_filtered.sum(axis=0).values
    grand_total = observed.sum()
    
    expected = np.outer(row_totals_arr, col_totals_arr) / grand_total
    
    # Calculate chi-square: χ² = Σ (Oij - Eij)² / Eij
    chi_square_contributions = (observed - expected) ** 2 / expected
    chi2_statistic = np.sum(chi_square_contributions)
    
    # Degrees of freedom: (rows - 1) * (columns - 1)
    dof = (contingency_filtered.shape[0] - 1) * (contingency_filtered.shape[1] - 1)
    
    # Prepare detailed results
    results = {
        'summary': {
            'total_female_brca_patients': int(total_patients),
            'patients_with_cdh1_mutations': int(total_with_mutations),
            'histology_categories_initial': int(categories_before),
            'histology_categories_after_filtering': int(categories_after)
        },
        'chi_square_analysis': {
            'chi_square_statistic': float(round(chi2_statistic, 4)),
            'degrees_of_freedom': int(dof),
            'contingency_table': {
                'rows': contingency_filtered.index.tolist(),
                'columns': contingency_filtered.columns.tolist(),
                'data': contingency_filtered.values.tolist()
            },
            'expected_frequencies': {
                'rows': contingency_filtered.index.tolist(),
                'columns': ['No CDH1 Mutation', 'CDH1 Mutation'],
                'data': expected.round(2).tolist()
            },
            'chi_square_contributions': {
                'rows': contingency_filtered.index.tolist(),
                'columns': ['No CDH1 Mutation', 'CDH1 Mutation'],
                'data': chi_square_contributions.round(4).tolist()
            }
        }
    }
else:
    results = {
        'summary': {
            'total_female_brca_patients': int(total_patients),
            'patients_with_cdh1_mutations': int(total_with_mutations),
            'histology_categories_initial': int(categories_before),
            'histology_categories_after_filtering': int(categories_after)
        },
        'error': 'Insufficient data for chi-square test after applying filters.',
        'raw_contingency_table': {
            'rows': contingency_raw.index.tolist(),
            'row_totals': row_totals.to_dict(),
            'data': contingency_raw.values.tolist()
        }
    }

print('__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.list_db:2': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:8': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_functions.query_db:10': [], 'var_functions.query_db:12': [{'total': '0'}], 'var_functions.query_db:14': [{'cancer_type': 'None'}, {'cancer_type': 'Liver hepatocellular carcinoma'}, {'cancer_type': 'Pheochromocytoma and Paraganglioma'}, {'cancer_type': 'Breast invasive carcinoma'}, {'cancer_type': 'Ovarian serous cystadenocarcinoma'}, {'cancer_type': 'Bladder urothelial carcinoma'}, {'cancer_type': 'Skin Cutaneous Melanoma'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:22': [{'Patient_description': 'Clinical entry D13FB44B-291B-4EA4-920C-142DAA8D1989 identifies patient TCGA-AC-A5EH, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma', 'gender': 'FEMALE', 'barcode': 'TCGA-AC-A5EH'}, {'Patient_description': 'Record 09A5E9FD-D816-4F8C-BAA9-0E40BA607B16 refers to patient TCGA-LL-A7SZ, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma', 'gender': 'FEMALE', 'barcode': 'TCGA-LL-A7SZ'}, {'Patient_description': "Patient TCGA-AN-A0FY, registered under UUID de75d0b9-0f47-4732-8df5-05c350cfcd32, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive.", 'histological_type': 'Infiltrating Ductal Carcinoma', 'gender': 'FEMALE', 'barcode': 'TCGA-AN-A0FY'}, {'Patient_description': 'Patient TCGA-AC-A2FB (UUID 02BBB632-0F7F-439D-B8F0-C86A06237424) is a FEMALE diagnosed with Breast invasive carcinoma. Current vital status: Alive.', 'histological_type': 'Infiltrating Lobular Carcinoma', 'gender': 'FEMALE', 'barcode': 'TCGA-AC-A2FB'}, {'Patient_description': 'The individual with barcode TCGA-AO-A1KR and UUID b7f74ae1-6f58-447c-be50-a7666eb19d9a is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma', 'gender': 'FEMALE', 'barcode': 'TCGA-AO-A1KR'}, {'Patient_description': 'Clinical entry C07B122E-AC50-4DB2-ADD2-5617A5D0E976 identifies patient TCGA-GM-A2DA, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Dead.', 'histological_type': 'Infiltrating Ductal Carcinoma', 'gender': 'FEMALE', 'barcode': 'TCGA-GM-A2DA'}, {'Patient_description': 'The individual with barcode TCGA-3C-AAAU and UUID 6E7D5EC6-A469-467C-B748-237353C23416 is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'histological_type': 'Infiltrating Lobular Carcinoma', 'gender': 'FEMALE', 'barcode': 'TCGA-3C-AAAU'}, {'Patient_description': "Patient TCGA-A7-A26I, registered under UUID b2ecbc0f-2c30-4200-8d5e-7b95424bcadb, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive.", 'histological_type': 'Infiltrating Ductal Carcinoma', 'gender': 'FEMALE', 'barcode': 'TCGA-A7-A26I'}, {'Patient_description': 'Record 523E24A2-51B9-4658-BE2F-42E5FCCEBB17 refers to patient TCGA-A7-A5ZW, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma', 'gender': 'FEMALE', 'barcode': 'TCGA-A7-A5ZW'}, {'Patient_description': 'The individual with barcode TCGA-C8-A26Z and UUID dc11b1c7-1f00-4813-b4b5-ecf776b2eb37 is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma', 'gender': 'FEMALE', 'barcode': 'TCGA-C8-A26Z'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:40': [{'total_female_brca': '1029'}], 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json'}

exec(code, env_args)
