code = """import pandas as pd
import json
import numpy as np

# Access file paths from local variables
file_path_clin = locals()['var_function-call-14324599992114814266']
file_path_mol = locals()['var_function-call-5457605271203438579']

# Load data
clinical_data = json.load(open(file_path_clin))
molecular_data = json.load(open(file_path_mol))

df_clin = pd.DataFrame(clinical_data)
df_mol = pd.DataFrame(molecular_data)

# Construct ParticipantBarcode in clinical
# Format: TCGA-{tissue_source_site}-{patient_id}
# Ensure strings
df_clin['tissue_source_site'] = df_clin['tissue_source_site'].astype(str).str.strip()
df_clin['patient_id'] = df_clin['patient_id'].astype(str).str.strip()
df_clin['ParticipantBarcode'] = 'TCGA-' + df_clin['tissue_source_site'] + '-' + df_clin['patient_id']

# Filter molecular data for valid counts
df_mol['normalized_count'] = pd.to_numeric(df_mol['normalized_count'], errors='coerce')
df_mol = df_mol.dropna(subset=['normalized_count'])

# Average expression per patient if multiple samples exist
df_mol_agg = df_mol.groupby('ParticipantBarcode')['normalized_count'].mean().reset_index()

# Merge
merged = pd.merge(df_clin, df_mol_agg, on='ParticipantBarcode', how='inner')

# Compute log10(normalized_count + 1)
merged['log10_expr'] = np.log10(merged['normalized_count'] + 1)

# Group by histological_type and compute mean
result = merged.groupby('histological_type')['log10_expr'].mean()

# Format result
output = {}
for histology, value in result.items():
    output[histology] = round(value, 4)

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_function-call-16848251565459269308': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_function-call-6085710608501832475': 'file_storage/function-call-6085710608501832475.json', 'var_function-call-16221689677385875384': [{'histological_type': 'Treated primary GBM', 'tumor_tissue_site': 'Brain'}, {'histological_type': 'Glioblastoma Multiforme (GBM)', 'tumor_tissue_site': 'Brain'}, {'histological_type': 'Untreated primary (de novo) GBM', 'tumor_tissue_site': 'Brain'}], 'var_function-call-12468084953328886178': [], 'var_function-call-16968906832507551346': [{'histological_type': 'Oligodendroglioma'}, {'histological_type': 'Astrocytoma'}], 'var_function-call-3046995861225854404': [{'histological_type': 'Untreated primary (de novo) GBM'}, {'histological_type': 'Glioblastoma Multiforme (GBM)'}, {'histological_type': 'Treated primary GBM'}], 'var_function-call-1215444286453936341': [{'tumor_tissue_site': 'Central nervous system'}], 'var_function-call-17447845612472052735': [{'histological_type': 'Oligodendroglioma'}, {'histological_type': 'Astrocytoma'}, {'histological_type': 'Oligoastrocytoma'}], 'var_function-call-7445578468119943200': [{'ParticipantBarcode': 'TCGA-06-0675', 'Symbol': 'LXN', 'normalized_count': '69.7259'}, {'ParticipantBarcode': 'TCGA-06-0675', 'Symbol': 'ZNF770', 'normalized_count': '1195.92'}, {'ParticipantBarcode': 'TCGA-06-0675', 'Symbol': 'AMELY', 'normalized_count': '0.0'}, {'ParticipantBarcode': 'TCGA-06-0675', 'Symbol': 'TPTE2P1', 'normalized_count': '214.576'}, {'ParticipantBarcode': 'TCGA-06-0675', 'Symbol': 'ITGB3', 'normalized_count': '13.6303'}], 'var_function-call-801724323384181052': [{'histological_type': '[Discrepancy]'}], 'var_function-call-14324599992114814266': 'file_storage/function-call-14324599992114814266.json', 'var_function-call-9488326689904384361': 'file_storage/function-call-9488326689904384361.json', 'var_function-call-11784874233267229494': [{'SampleType': 'Metastatic', 'cnt': '369349'}, {'SampleType': 'Primary solid Tumor', 'cnt': '8747238'}, {'SampleType': 'Recurrent Solid Tumor', 'cnt': '42261'}, {'SampleType': 'Solid Tissue Normal', 'cnt': '662878'}, {'SampleType': 'Additional Metastatic', 'cnt': '1030'}, {'SampleType': 'Primary Blood Derived Cancer - Peripheral Blood', 'cnt': '163015'}, {'SampleType': 'Additional - New Primary', 'cnt': '10106'}], 'var_function-call-5457605271203438579': 'file_storage/function-call-5457605271203438579.json'}

exec(code, env_args)
