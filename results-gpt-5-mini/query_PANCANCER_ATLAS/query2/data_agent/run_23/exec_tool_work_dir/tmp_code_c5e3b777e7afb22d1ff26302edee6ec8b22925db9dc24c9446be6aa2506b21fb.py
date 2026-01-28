code = """import json
import pandas as pd

# Load previous query results from storage-provided file paths
with open(var_call_ifllUchzX8rY2EMKRDtDlu3Q, 'r') as f:
    clin = json.load(f)
with open(var_call_5yJuanaiu3vsUeHDX96JHfND, 'r') as f:
    mut = json.load(f)

# Create DataFrames
df_clin = pd.DataFrame(clin)
df_mut = pd.DataFrame(mut)

# Standardize barcode strings (strip whitespace)
df_clin['barcode'] = df_clin['barcode'].str.strip()
df_clin['histological_type'] = df_clin['histological_type'].fillna('Unknown')
df_mut['ParticipantBarcode'] = df_mut['ParticipantBarcode'].str.strip()

# Unique set of participants with CDH1 mutation
cdh1_set = set(df_mut['ParticipantBarcode'].unique())

# For clinical, ensure one record per patient-barcode/histology pair by dropping duplicates
df_clin_unique = df_clin.drop_duplicates(subset=['barcode'])

# Compute totals per histological_type among alive BRCA patients
group = df_clin_unique.groupby('histological_type').agg(total_alive=('barcode','count'))

# Compute mutated counts by histological type
# Mark whether each clinical barcode has CDH1 mutation
df_clin_unique['has_CDH1'] = df_clin_unique['barcode'].apply(lambda x: x in cdh1_set)
mut_counts = df_clin_unique.groupby('histological_type').agg(mutated_count=('has_CDH1','sum'))

# Merge and compute percentage
summary = group.join(mut_counts)
summary['mutated_count'] = summary['mutated_count'].astype(int)
summary['percent_mutated'] = (summary['mutated_count'] / summary['total_alive'] * 100).round(2)

# Select histological types with at least one patient
summary = summary[summary['total_alive'] > 0]

# Sort by percentage desc, then by mutated_count desc, then by total_alive desc
summary_sorted = summary.sort_values(by=['percent_mutated','mutated_count','total_alive'], ascending=[False,False,False])

# Take top 3
top3 = summary_sorted.head(3).reset_index()

# Prepare output list
result = []
for _, row in top3.iterrows():
    result.append({
        'histological_type': row['histological_type'],
        'total_alive': int(row['total_alive']),
        'mutated_count': int(row['mutated_count']),
        'percent_mutated': float(row['percent_mutated'])
    })

# If fewer than 3 results, still output whatever is available
output = json.dumps(result)
print("__RESULT__:")
print(output)"""

env_args = {'var_call_UWIMY9h2Bvt8q6lBEFFp5KQS': 'file_storage/call_UWIMY9h2Bvt8q6lBEFFp5KQS.json', 'var_call_XopNahAYDguAkEi5oijPabVB': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_2W2s4zuSZxQrOPqR90H187oM': 'file_storage/call_2W2s4zuSZxQrOPqR90H187oM.json', 'var_call_ifllUchzX8rY2EMKRDtDlu3Q': 'file_storage/call_ifllUchzX8rY2EMKRDtDlu3Q.json', 'var_call_5yJuanaiu3vsUeHDX96JHfND': 'file_storage/call_5yJuanaiu3vsUeHDX96JHfND.json'}

exec(code, env_args)
