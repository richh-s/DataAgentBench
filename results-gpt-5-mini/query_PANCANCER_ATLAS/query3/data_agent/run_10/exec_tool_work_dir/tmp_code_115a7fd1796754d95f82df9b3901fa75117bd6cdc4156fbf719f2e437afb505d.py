code = """import json
import pandas as pd
import re

# Load data from storage-provided file paths
with open(var_call_uff3DvwezHVrQSn74xUYdK9j, 'r') as f:
    clinical = json.load(f)
with open(var_call_3HM3mVQjbix23JCO7IQB11Ur, 'r') as f:
    mutations = json.load(f)

# Create DataFrames
clin_df = pd.DataFrame(clinical)
mut_df = pd.DataFrame(mutations)

# Filter clinical for Breast and FEMALE and known histological_type
clin_df = clin_df[clin_df.get('Patient_description', '').str.contains('Breast', case=False, na=False)]
clin_df = clin_df[clin_df.get('Patient_description', '').str.contains('FEMALE', case=False, na=False)]
clin_df = clin_df[clin_df['histological_type'].notna()]
clin_df = clin_df[clin_df['histological_type'].str.strip().ne('')]
# Exclude vague 'Other' entries
clin_df = clin_df[~clin_df['histological_type'].str.lower().str.startswith('other')]

# Standardize patient_id (use the patient_id column if present)
clin_df['patient_id'] = clin_df['patient_id'].astype(str).str.upper()

# Process mutations: only CDH1 and FILTER == 'PASS'
mut_df = mut_df[mut_df.get('Hugo_Symbol', '') == 'CDH1']
mut_df = mut_df[mut_df.get('FILTER', '') == 'PASS']
mut_df = mut_df[mut_df['ParticipantBarcode'].notna()]

# Extract patient_id from ParticipantBarcode (last segment after second dash)
def extract_pid(pb):
    try:
        parts = pb.split('-')
        if len(parts) >= 3:
            return parts[2].upper()
        else:
            return parts[-1].upper()
    except:
        return None

mut_df['patient_id'] = mut_df['ParticipantBarcode'].astype(str).apply(extract_pid)

# Build set of mutated patient_ids
mutated_set = set(mut_df['patient_id'].dropna().unique())

# Filter clinical to only unique patients (one record per patient)
clin_unique = clin_df.drop_duplicates(subset=['patient_id']).copy()

# Determine mutation presence
clin_unique['CDH1_mutation'] = clin_unique['patient_id'].apply(lambda x: 'Yes' if x in mutated_set else 'No')

# Contingency table
ct = pd.crosstab(clin_unique['histological_type'], clin_unique['CDH1_mutation'])

# Ensure both columns Yes and No exist
for col in ['Yes','No']:
    if col not in ct.columns:
        ct[col] = 0
ct = ct[['Yes','No']]

# Compute marginal totals
ct['row_total'] = ct.sum(axis=1)
col_totals = ct[['Yes','No']].sum(axis=0).to_dict()
grand_total = ct['row_total'].sum()

# Exclude rows or columns with marginal totals <= 10
# Identify rows to keep
rows_keep = ct[ct['row_total'] > 10].index.tolist()
# Identify columns to keep
cols_keep = [c for c,v in col_totals.items() if v > 10]

# Apply exclusions
ct_filtered = ct.loc[rows_keep, cols_keep].copy()
ct_filtered['row_total'] = ct_filtered.sum(axis=1)
col_totals_filtered = ct_filtered[cols_keep].sum(axis=0).to_dict() if len(cols_keep)>0 else {}
grand_total_filtered = ct_filtered['row_total'].sum()

# Compute chi-square if possible
chi2 = None
details = {}
if grand_total_filtered > 0 and len(rows_keep) >= 2 and len(cols_keep) >= 2:
    chi2_val = 0.0
    # For each cell compute expected and add to chi2
    for r in ct_filtered.index:
        for c in cols_keep:
            O = float(ct_filtered.at[r,c])
            E = (ct_filtered.at[r,'row_total'] * col_totals_filtered[c]) / grand_total_filtered
            if E > 0:
                chi2_val += (O - E)**2 / E
    chi2 = chi2_val
    details['chi2'] = chi2
else:
    details['error'] = 'Not enough data after excluding margins <= 10 to compute chi-square.'

# Prepare output
output = {
    'contingency_table_all': ct.reset_index().to_dict(orient='records'),
    'row_totals_all': ct['row_total'].to_dict(),
    'col_totals_all': col_totals,
    'grand_total_all': int(grand_total),
    'rows_kept_after_exclusion': rows_keep,
    'cols_kept_after_exclusion': cols_keep,
    'contingency_table_filtered': ct_filtered.reset_index().to_dict(orient='records'),
    'row_totals_filtered': ct_filtered['row_total'].to_dict() if not ct_filtered.empty else {},
    'col_totals_filtered': col_totals_filtered,
    'grand_total_filtered': int(grand_total_filtered),
    'result': details
}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_MxPEPKk7HUZ2s8R6YVumLkLF': [{'column_name': 'stopped_smoking_year', 'data_type': 'double precision'}, {'column_name': 'days_to_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'number_of_lymphnodes_positive_by_he', 'data_type': 'double precision'}, {'column_name': 'age_at_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'year_of_tobacco_smoking_onset', 'data_type': 'double precision'}, {'column_name': 'year_of_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'height', 'data_type': 'double precision'}, {'column_name': 'weight', 'data_type': 'double precision'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc', 'data_type': 'double precision'}, {'column_name': 'days_to_birth', 'data_type': 'double precision'}, {'column_name': 'total_pelv_lnr', 'data_type': 'double precision'}, {'column_name': 'total_aor_lnr', 'data_type': 'double precision'}, {'column_name': 'number_pack_years_smoked', 'data_type': 'double precision'}, {'column_name': 'prior_dx', 'data_type': 'text'}, {'column_name': 'ethnicity', 'data_type': 'text'}, {'column_name': 'informed_consent_verified', 'data_type': 'text'}, {'column_name': 'person_neoplasm_cancer_status', 'data_type': 'text'}, {'column_name': 'patient_id', 'data_type': 'text'}, {'column_name': 'histological_type', 'data_type': 'text'}, {'column_name': 'tissue_source_site', 'data_type': 'text'}, {'column_name': 'form_completion_date', 'data_type': 'text'}, {'column_name': 'pathologic_T', 'data_type': 'text'}, {'column_name': 'pathologic_M', 'data_type': 'text'}, {'column_name': 'clinical_M', 'data_type': 'text'}, {'column_name': 'pathologic_N', 'data_type': 'text'}, {'column_name': 'system_version', 'data_type': 'text'}, {'column_name': 'pathologic_stage', 'data_type': 'text'}, {'column_name': 'clinical_stage', 'data_type': 'text'}, {'column_name': 'clinical_T', 'data_type': 'text'}, {'column_name': 'clinical_N', 'data_type': 'text'}, {'column_name': 'extranodal_involvement', 'data_type': 'text'}, {'column_name': 'postoperative_rx_tx', 'data_type': 'text'}, {'column_name': 'primary_therapy_outcome_success', 'data_type': 'text'}, {'column_name': 'lymph_node_examined_count', 'data_type': 'text'}, {'column_name': 'primary_lymph_node_presentation_assessment', 'data_type': 'text'}, {'column_name': 'initial_pathologic_diagnosis_method', 'data_type': 'text'}, {'column_name': 'eastern_cancer_oncology_group', 'data_type': 'text'}, {'column_name': 'anatomic_neoplasm_subdivision', 'data_type': 'text'}, {'column_name': 'residual_tumor', 'data_type': 'text'}, {'column_name': 'histological_type_other', 'data_type': 'text'}, {'column_name': 'init_pathology_dx_method_other', 'data_type': 'text'}, {'column_name': 'karnofsky_performance_score', 'data_type': 'text'}, {'column_name': 'neoplasm_histologic_grade', 'data_type': 'text'}, {'column_name': 'tobacco_smoking_history', 'data_type': 'text'}, {'column_name': 'performance_status_scale_timing', 'data_type': 'text'}, {'column_name': 'laterality', 'data_type': 'text'}, {'column_name': 'targeted_molecular_therapy', 'data_type': 'text'}, {'column_name': 'anatomic_neoplasm_subdivision_other', 'data_type': 'text'}, {'column_name': 'patient_death_reason', 'data_type': 'text'}, {'column_name': 'tumor_tissue_site_other', 'data_type': 'text'}, {'column_name': 'menopause_status', 'data_type': 'text'}, {'column_name': 'margin_status', 'data_type': 'text'}, {'column_name': 'kras_gene_analysis_performed', 'data_type': 'text'}, {'column_name': 'venous_invasion', 'data_type': 'text'}, {'column_name': 'lymphatic_invasion', 'data_type': 'text'}, {'column_name': 'perineural_invasion_present', 'data_type': 'text'}, {'column_name': 'her2_immunohistochemistry_level_result', 'data_type': 'text'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status', 'data_type': 'text'}, {'column_name': 'breast_carcinoma_surgical_procedure_name', 'data_type': 'text'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text', 'data_type': 'text'}, {'column_name': 'axillary_lymph_node_stage_method_type', 'data_type': 'text'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status', 'data_type': 'text'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi', 'data_type': 'text'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status', 'data_type': 'text'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type', 'data_type': 'text'}, {'column_name': 'additional_pharmaceutical_therapy', 'data_type': 'text'}, {'column_name': 'additional_radiation_therapy', 'data_type': 'text'}, {'column_name': 'lymphovascular_invasion_present', 'data_type': 'text'}, {'column_name': 'location_in_lung_parenchyma', 'data_type': 'text'}, {'column_name': 'pulmonary_function_test_performed', 'data_type': 'text'}, {'column_name': 'egfr_mutation_performed', 'data_type': 'text'}, {'column_name': 'diagnosis', 'data_type': 'text'}, {'column_name': 'eml4_alk_translocation_performed', 'data_type': 'text'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment', 'data_type': 'text'}, {'column_name': 'hemoglobin_result', 'data_type': 'text'}, {'column_name': 'serum_calcium_result', 'data_type': 'text'}, {'column_name': 'platelet_qualitative_result', 'data_type': 'text'}, {'column_name': 'number_of_lymphnodes_positive', 'data_type': 'text'}, {'column_name': 'white_cell_count_result', 'data_type': 'text'}, {'column_name': 'alcohol_history_documented', 'data_type': 'text'}, {'column_name': 'family_history_of_cancer', 'data_type': 'text'}, {'column_name': 'braf_gene_analysis_performed', 'data_type': 'text'}, {'column_name': 'city_of_procurement', 'data_type': 'text'}, {'column_name': 'surgical_approach', 'data_type': 'text'}, {'column_name': 'peritoneal_wash', 'data_type': 'text'}, {'column_name': 'Patient_description', 'data_type': 'text'}, {'column_name': 'prior_glioma', 'data_type': 'text'}, {'column_name': 'days_to_death', 'data_type': 'text'}, {'column_name': 'days_to_last_followup', 'data_type': 'text'}, {'column_name': 'icd_10', 'data_type': 'text'}, {'column_name': 'tissue_retrospective_collection_indicator', 'data_type': 'text'}, {'column_name': 'icd_o_3_histology', 'data_type': 'text'}, {'column_name': 'tissue_prospective_collection_indicator', 'data_type': 'text'}, {'column_name': 'history_of_neoadjuvant_treatment', 'data_type': 'text'}, {'column_name': 'icd_o_3_site', 'data_type': 'text'}, {'column_name': 'tumor_tissue_site', 'data_type': 'text'}, {'column_name': 'new_tumor_event_after_initial_treatment', 'data_type': 'text'}, {'column_name': 'radiation_therapy', 'data_type': 'text'}, {'column_name': 'race', 'data_type': 'text'}], 'var_call_sxfUHFYQDZzUKsORf5P4KA1J': [], 'var_call_Dv4M0D7TQvLIEMHIC7Ip0nrP': 'file_storage/call_Dv4M0D7TQvLIEMHIC7Ip0nrP.json', 'var_call_uff3DvwezHVrQSn74xUYdK9j': 'file_storage/call_uff3DvwezHVrQSn74xUYdK9j.json', 'var_call_3HM3mVQjbix23JCO7IQB11Ur': 'file_storage/call_3HM3mVQjbix23JCO7IQB11Ur.json'}

exec(code, env_args)
