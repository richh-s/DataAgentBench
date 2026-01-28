code = """import json
import pandas as pd
import re
import math

# Load data from previous tool calls (file paths)
clin_file = var_call_7v3xcntQKsVmgRobgrnyOSyp
mut_file = var_call_FAQW1UPkfTzbe8nPEAl5WdEL

with open(clin_file, 'r') as f:
    clin = json.load(f)
with open(mut_file, 'r') as f:
    mut = json.load(f)

df_clin = pd.DataFrame(clin)
df_mut = pd.DataFrame(mut)

# Keep only patients with known (non-null, non-empty) histological_type
df_clin = df_clin[df_clin['histological_type'].notnull()]
# strip whitespace and remove empty strings
df_clin['histological_type'] = df_clin['histological_type'].astype(str).str.strip()
df_clin = df_clin[df_clin['histological_type'] != '']

# Use clinical patient_id (e.g., A2FB) as identifier
# For mutations, extract last segment of ParticipantBarcode after last '-'

def extract_last_segment(x):
    try:
        return x.split('-')[-1]
    except:
        return x

if 'ParticipantBarcode' in df_mut.columns:
    df_mut['patient_id'] = df_mut['ParticipantBarcode'].astype(str).apply(extract_last_segment)
else:
    df_mut['patient_id'] = df_mut.index.astype(str)

# Map mutated patients set (unique patient ids with PASS CDH1 mutations)
mutated_patients = set(df_mut['patient_id'].unique())

# Build per-patient mutation presence for clinical patients
# Keep only clinical patients (female BRCA) from loaded clinical file
# clinical query already filtered to females with breast; ensure patient_id column exists
if 'patient_id' not in df_clin.columns:
    df_clin['patient_id'] = df_clin['Patient_description'].astype(str).str.extract(r'(TCGA-[A-Z0-9]+-[A-Z0-9]+)')
    # fallback to last segment
    df_clin['patient_id'] = df_clin['patient_id'].apply(lambda x: extract_last_segment(x) if pd.notnull(x) else None)

# Ensure patient_id is string
df_clin['patient_id'] = df_clin['patient_id'].astype(str)

# Determine mutation presence
df_clin['CDH1_mutated'] = df_clin['patient_id'].apply(lambda x: 1 if x in mutated_patients else 0)

# Now build contingency table: histological_type x CDH1_mutated
ct = df_clin.groupby(['histological_type', 'CDH1_mutated']).size().unstack(fill_value=0)
# Ensure both columns 0 and 1 exist
for col in [0,1]:
    if col not in ct.columns:
        ct[col] = 0
ct = ct[[1,0]] if 1 in ct.columns else ct
ct = ct.rename(columns={1: 'mutated', 0: 'not_mutated'})

# Exclude categories with marginal totals <= 10 (row totals)
ct['row_total'] = ct.sum(axis=1)
ct_included = ct[ct['row_total'] > 10].drop(columns=['row_total'])

# If no categories remain, return empty result
if ct_included.shape[0] == 0:
    result = {
        'chi2': None,
        'df': None,
        'message': 'No histological categories with row totals > 10.'
    }
else:
    # Build O matrix
    O = ct_included[['mutated','not_mutated']].values.astype(float)
    row_sums = O.sum(axis=1)
    col_sums = O.sum(axis=0)
    grand_total = O.sum()
    # Expected
    E = (row_sums[:, None] * col_sums[None, :]) / grand_total
    # Compute chi-square statistic, avoid division by zero
    mask = E > 0
    chi2 = float(((O - E)**2 / E)[mask].sum())
    df = int((O.shape[0]-1)*(O.shape[1]-1))

    # Prepare contingency dict
    contingency = {}
    for idx, row in ct_included.iterrows():
        contingency[idx] = {'mutated': int(row['mutated']), 'not_mutated': int(row['not_mutated'])}

    result = {
        'chi2': chi2,
        'df': df,
        'grand_total': int(grand_total),
        'included_histological_types_count': int(ct_included.shape[0]),
        'contingency_table': contingency
    }

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_CNSGwdPDhI9TdU9GW3W1y1PT': ['clinical_info'], 'var_call_JrsCWo20cbdBxoVN2fu9lor4': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_S4Q8AUXysAdEPIOHpoqvfZu4': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_7v3xcntQKsVmgRobgrnyOSyp': 'file_storage/call_7v3xcntQKsVmgRobgrnyOSyp.json', 'var_call_FAQW1UPkfTzbe8nPEAl5WdEL': 'file_storage/call_FAQW1UPkfTzbe8nPEAl5WdEL.json'}

exec(code, env_args)
