code = """import json, pandas as pd

# Load mutation participants (CDH1)
with open(var_call_ShJ9J4vfKAQyNX2VCVnYdb6R, 'r') as f:
    mut_data = json.load(f)

# Load clinical alive BRCA participants with histological_type
with open(var_call_FBk27n7uDs2e0unDTmSIk0Ty, 'r') as f:
    clin_data = json.load(f)

# Create DataFrames
df_mut = pd.DataFrame(mut_data)
# Normalize column name for participant barcode
if 'ParticipantBarcode' in df_mut.columns:
    df_mut['participantbarcode'] = df_mut['ParticipantBarcode'].str.upper()
elif 'participantbarcode' in df_mut.columns:
    df_mut['participantbarcode'] = df_mut['participantbarcode'].str.upper()
else:
    # try any key resembling
    cols = df_mut.columns.tolist()
    if cols:
        df_mut['participantbarcode'] = df_mut[cols[0]].str.upper()

# Unique set of participants with CDH1 mutation
mut_participants = set(df_mut['participantbarcode'].dropna().unique())

# Clinical
df_clin = pd.DataFrame(clin_data)
# Normalize participant barcode column name
if 'participantbarcode' in df_clin.columns:
    df_clin['participantbarcode'] = df_clin['participantbarcode'].str.upper()
elif 'ParticipantBarcode' in df_clin.columns:
    df_clin['participantbarcode'] = df_clin['ParticipantBarcode'].str.upper()
else:
    cols = df_clin.columns.tolist()
    if cols:
        df_clin['participantbarcode'] = df_clin[cols[0]].str.upper()

# Normalize histological_type
if 'histological_type' not in df_clin.columns and 'histologicalType' in df_clin.columns:
    df_clin['histological_type'] = df_clin['histologicalType']

# Drop rows without participantbarcode or histological_type
df_clin = df_clin[df_clin['participantbarcode'].notna() & df_clin['histological_type'].notna()].copy()

# Deduplicate by participantbarcode (keep first)
df_clin = df_clin.drop_duplicates(subset=['participantbarcode'])

# Compute counts by histological type
group = df_clin.groupby('histological_type').agg(total_patients=('participantbarcode', 'count'))
# compute mutated counts
group['mutated_patients'] = df_clin['participantbarcode'].apply(lambda x: x in mut_participants).groupby(df_clin['histological_type']).sum()
# mutation percentage
group['mutation_percentage'] = (group['mutated_patients'] / group['total_patients']) * 100

# Prepare result sorted by percentage desc, then total_patients desc
res = group.reset_index().sort_values(['mutation_percentage', 'total_patients'], ascending=[False, False])
# Round percentage to 2 decimals
res['mutation_percentage'] = res['mutation_percentage'].round(2)

# Get top 3
top3 = res.head(3)

# Convert to list of dicts
result_list = []
for _, row in top3.iterrows():
    result_list.append({
        'histological_type': row['histological_type'],
        'total_patients': int(row['total_patients']),
        'mutated_patients': int(row['mutated_patients']),
        'mutation_percentage': float(row['mutation_percentage'])
    })

output = json.dumps(result_list)
print("__RESULT__:")
print(output)"""

env_args = {'var_call_QNKWYDilbdVFOgHy3OCl6Bxv': ['clinical_info'], 'var_call_uGf7WvYZvncUSceicZbyHTX7': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_oAc3lbxuXVTdFQhS4SAm9lsy': [{'column_name': 'stopped_smoking_year', 'data_type': 'double precision'}, {'column_name': 'days_to_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'number_of_lymphnodes_positive_by_he', 'data_type': 'double precision'}, {'column_name': 'age_at_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'year_of_tobacco_smoking_onset', 'data_type': 'double precision'}, {'column_name': 'year_of_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'height', 'data_type': 'double precision'}, {'column_name': 'weight', 'data_type': 'double precision'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc', 'data_type': 'double precision'}, {'column_name': 'days_to_birth', 'data_type': 'double precision'}, {'column_name': 'total_pelv_lnr', 'data_type': 'double precision'}, {'column_name': 'total_aor_lnr', 'data_type': 'double precision'}, {'column_name': 'number_pack_years_smoked', 'data_type': 'double precision'}, {'column_name': 'prior_dx', 'data_type': 'text'}, {'column_name': 'ethnicity', 'data_type': 'text'}, {'column_name': 'informed_consent_verified', 'data_type': 'text'}, {'column_name': 'person_neoplasm_cancer_status', 'data_type': 'text'}, {'column_name': 'patient_id', 'data_type': 'text'}, {'column_name': 'histological_type', 'data_type': 'text'}, {'column_name': 'tissue_source_site', 'data_type': 'text'}, {'column_name': 'form_completion_date', 'data_type': 'text'}, {'column_name': 'pathologic_T', 'data_type': 'text'}, {'column_name': 'pathologic_M', 'data_type': 'text'}, {'column_name': 'clinical_M', 'data_type': 'text'}, {'column_name': 'pathologic_N', 'data_type': 'text'}, {'column_name': 'system_version', 'data_type': 'text'}, {'column_name': 'pathologic_stage', 'data_type': 'text'}, {'column_name': 'clinical_stage', 'data_type': 'text'}, {'column_name': 'clinical_T', 'data_type': 'text'}, {'column_name': 'clinical_N', 'data_type': 'text'}, {'column_name': 'extranodal_involvement', 'data_type': 'text'}, {'column_name': 'postoperative_rx_tx', 'data_type': 'text'}, {'column_name': 'primary_therapy_outcome_success', 'data_type': 'text'}, {'column_name': 'lymph_node_examined_count', 'data_type': 'text'}, {'column_name': 'primary_lymph_node_presentation_assessment', 'data_type': 'text'}, {'column_name': 'initial_pathologic_diagnosis_method', 'data_type': 'text'}, {'column_name': 'eastern_cancer_oncology_group', 'data_type': 'text'}, {'column_name': 'anatomic_neoplasm_subdivision', 'data_type': 'text'}, {'column_name': 'residual_tumor', 'data_type': 'text'}, {'column_name': 'histological_type_other', 'data_type': 'text'}, {'column_name': 'init_pathology_dx_method_other', 'data_type': 'text'}, {'column_name': 'karnofsky_performance_score', 'data_type': 'text'}, {'column_name': 'neoplasm_histologic_grade', 'data_type': 'text'}, {'column_name': 'tobacco_smoking_history', 'data_type': 'text'}, {'column_name': 'performance_status_scale_timing', 'data_type': 'text'}, {'column_name': 'laterality', 'data_type': 'text'}, {'column_name': 'targeted_molecular_therapy', 'data_type': 'text'}, {'column_name': 'anatomic_neoplasm_subdivision_other', 'data_type': 'text'}, {'column_name': 'patient_death_reason', 'data_type': 'text'}, {'column_name': 'tumor_tissue_site_other', 'data_type': 'text'}, {'column_name': 'menopause_status', 'data_type': 'text'}, {'column_name': 'margin_status', 'data_type': 'text'}, {'column_name': 'kras_gene_analysis_performed', 'data_type': 'text'}, {'column_name': 'venous_invasion', 'data_type': 'text'}, {'column_name': 'lymphatic_invasion', 'data_type': 'text'}, {'column_name': 'perineural_invasion_present', 'data_type': 'text'}, {'column_name': 'her2_immunohistochemistry_level_result', 'data_type': 'text'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status', 'data_type': 'text'}, {'column_name': 'breast_carcinoma_surgical_procedure_name', 'data_type': 'text'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text', 'data_type': 'text'}, {'column_name': 'axillary_lymph_node_stage_method_type', 'data_type': 'text'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status', 'data_type': 'text'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi', 'data_type': 'text'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status', 'data_type': 'text'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type', 'data_type': 'text'}, {'column_name': 'additional_pharmaceutical_therapy', 'data_type': 'text'}, {'column_name': 'additional_radiation_therapy', 'data_type': 'text'}, {'column_name': 'lymphovascular_invasion_present', 'data_type': 'text'}, {'column_name': 'location_in_lung_parenchyma', 'data_type': 'text'}, {'column_name': 'pulmonary_function_test_performed', 'data_type': 'text'}, {'column_name': 'egfr_mutation_performed', 'data_type': 'text'}, {'column_name': 'diagnosis', 'data_type': 'text'}, {'column_name': 'eml4_alk_translocation_performed', 'data_type': 'text'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment', 'data_type': 'text'}, {'column_name': 'hemoglobin_result', 'data_type': 'text'}, {'column_name': 'serum_calcium_result', 'data_type': 'text'}, {'column_name': 'platelet_qualitative_result', 'data_type': 'text'}, {'column_name': 'number_of_lymphnodes_positive', 'data_type': 'text'}, {'column_name': 'white_cell_count_result', 'data_type': 'text'}, {'column_name': 'alcohol_history_documented', 'data_type': 'text'}, {'column_name': 'family_history_of_cancer', 'data_type': 'text'}, {'column_name': 'braf_gene_analysis_performed', 'data_type': 'text'}, {'column_name': 'city_of_procurement', 'data_type': 'text'}, {'column_name': 'surgical_approach', 'data_type': 'text'}, {'column_name': 'peritoneal_wash', 'data_type': 'text'}, {'column_name': 'Patient_description', 'data_type': 'text'}, {'column_name': 'prior_glioma', 'data_type': 'text'}, {'column_name': 'days_to_death', 'data_type': 'text'}, {'column_name': 'days_to_last_followup', 'data_type': 'text'}, {'column_name': 'icd_10', 'data_type': 'text'}, {'column_name': 'tissue_retrospective_collection_indicator', 'data_type': 'text'}, {'column_name': 'icd_o_3_histology', 'data_type': 'text'}, {'column_name': 'tissue_prospective_collection_indicator', 'data_type': 'text'}, {'column_name': 'history_of_neoadjuvant_treatment', 'data_type': 'text'}, {'column_name': 'icd_o_3_site', 'data_type': 'text'}, {'column_name': 'tumor_tissue_site', 'data_type': 'text'}, {'column_name': 'new_tumor_event_after_initial_treatment', 'data_type': 'text'}, {'column_name': 'radiation_therapy', 'data_type': 'text'}, {'column_name': 'race', 'data_type': 'text'}], 'var_call_qHiSiynBv1QhLtuedCSgX7Mo': [], 'var_call_ShJ9J4vfKAQyNX2VCVnYdb6R': 'file_storage/call_ShJ9J4vfKAQyNX2VCVnYdb6R.json', 'var_call_ex7Cm8uvBrGHlopR4fytCwZo': 'file_storage/call_ex7Cm8uvBrGHlopR4fytCwZo.json', 'var_call_FBk27n7uDs2e0unDTmSIk0Ty': 'file_storage/call_FBk27n7uDs2e0unDTmSIk0Ty.json'}

exec(code, env_args)
