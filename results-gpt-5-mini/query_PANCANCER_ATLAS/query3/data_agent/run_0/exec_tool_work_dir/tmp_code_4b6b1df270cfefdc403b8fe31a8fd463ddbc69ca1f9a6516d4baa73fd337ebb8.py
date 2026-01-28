code = """import json, re
import pandas as pd
import math

# Load data from storage files
with open(var_call_n87WclNqBXnSVwQzLeOjtk02, 'r') as f:
    clinical = json.load(f)
with open(var_call_DCPE8kaJUb4ZuG5voSQblBHA, 'r') as f:
    muts = json.load(f)

# Build DataFrames
dfc = pd.DataFrame(clinical)
dfm = pd.DataFrame(muts)

# Extract ParticipantBarcode from Patient_description
pattern = re.compile(r'(TCGA-[A-Za-z0-9]+-[A-Za-z0-9]+)')

def extract_barcode(s):
    if not isinstance(s, str):
        return None
    m = pattern.search(s)
    return m.group(1) if m else None

if 'Patient_description' in dfc.columns:
    dfc['ParticipantBarcode'] = dfc['Patient_description'].apply(extract_barcode)
else:
    dfc['ParticipantBarcode'] = None

# Ensure histological_type exists
if 'histological_type' not in dfc.columns:
    dfc['histological_type'] = None

# Drop incomplete rows
dfc = dfc.dropna(subset=['ParticipantBarcode','histological_type'])
# Keep unique patients
dfc = dfc.drop_duplicates(subset=['ParticipantBarcode'])

# Prepare mutation set (only PASS entries were queried)
mut_set = set(dfm['ParticipantBarcode'].astype(str).tolist())

# Flag mutation presence
dfc['CDH1_mut'] = dfc['ParticipantBarcode'].apply(lambda x: x in mut_set)

# Exclude histological categories with marginal totals <= 10
counts = dfc['histological_type'].value_counts()
included = counts[counts > 10].index.tolist()

dfc_incl = dfc[dfc['histological_type'].isin(included)].copy()

# If no categories included, return early
if len(included) == 0:
    result = {"error": "No histological categories with total > 10 found."}
    print("__RESULT__:")
    print(json.dumps(result))
else:
    # Build contingency table
    ct = pd.crosstab(dfc_incl['histological_type'], dfc_incl['CDH1_mut'])
    # Ensure both False and True columns exist
    if True not in ct.columns:
        ct[True] = 0
    if False not in ct.columns:
        ct[False] = 0
    ct = ct[[False, True]]

    observed = ct.values.astype(float)
    row_totals = observed.sum(axis=1)
    col_totals = observed.sum(axis=0)
    grand_total = observed.sum()

    # Compute expected
    expected = (row_totals.reshape(-1,1) * col_totals.reshape(1,-1)) / grand_total

    # Compute chi-square statistic (handle zeros in expected to avoid division by zero)
    chi2 = 0.0
    rows, cols = observed.shape
    for i in range(rows):
        for j in range(cols):
            E = expected[i,j]
            O = observed[i,j]
            if E > 0:
                chi2 += (O - E)**2 / E

    dof = (rows - 1) * (cols - 1)

    # Build output dictionary
    contingency = {}
    for idx, hist in enumerate(ct.index.tolist()):
        contingency[hist] = {
            "mut_present": int(ct.iloc[idx][True]),
            "mut_absent": int(ct.iloc[idx][False]),
            "row_total": int(row_totals[idx])
        }

    result = {
        "chi2": float(chi2),
        "degrees_of_freedom": int(dof),
        "grand_total": int(grand_total),
        "included_histological_types": included,
        "contingency_table": contingency,
        "col_totals": {"mut_absent": int(col_totals[0]), "mut_present": int(col_totals[1])}
    }

    print("__RESULT__:")
    print(json.dumps(result))"""

env_args = {'var_call_rKKXYkSmWk6IpiNPcCwTwRbD': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_DCPE8kaJUb4ZuG5voSQblBHA': 'file_storage/call_DCPE8kaJUb4ZuG5voSQblBHA.json', 'var_call_lP43upZt0vqFcI3znBEqIKiO': ['stopped_smoking_year', 'days_to_initial_pathologic_diagnosis', 'number_of_lymphnodes_positive_by_he', 'age_at_initial_pathologic_diagnosis', 'year_of_tobacco_smoking_onset', 'year_of_initial_pathologic_diagnosis', 'height', 'weight', 'number_of_lymphnodes_positive_by_ihc', 'days_to_birth', 'total_pelv_lnr', 'total_aor_lnr', 'number_pack_years_smoked', 'prior_dx', 'ethnicity', 'informed_consent_verified', 'person_neoplasm_cancer_status', 'patient_id', 'histological_type', 'tissue_source_site', 'form_completion_date', 'pathologic_T', 'pathologic_M', 'clinical_M', 'pathologic_N', 'system_version', 'pathologic_stage', 'clinical_stage', 'clinical_T', 'clinical_N', 'extranodal_involvement', 'postoperative_rx_tx', 'primary_therapy_outcome_success', 'lymph_node_examined_count', 'primary_lymph_node_presentation_assessment', 'initial_pathologic_diagnosis_method', 'eastern_cancer_oncology_group', 'anatomic_neoplasm_subdivision', 'residual_tumor', 'histological_type_other', 'init_pathology_dx_method_other', 'karnofsky_performance_score', 'neoplasm_histologic_grade', 'tobacco_smoking_history', 'performance_status_scale_timing', 'laterality', 'targeted_molecular_therapy', 'anatomic_neoplasm_subdivision_other', 'patient_death_reason', 'tumor_tissue_site_other', 'menopause_status', 'margin_status', 'kras_gene_analysis_performed', 'venous_invasion', 'lymphatic_invasion', 'perineural_invasion_present', 'her2_immunohistochemistry_level_result', 'breast_carcinoma_progesterone_receptor_status', 'breast_carcinoma_surgical_procedure_name', 'breast_neoplasm_other_surgical_procedure_descriptive_text', 'axillary_lymph_node_stage_method_type', 'breast_carcinoma_estrogen_receptor_status', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi', 'lab_proc_her2_neu_immunohistochemistry_receptor_status', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type', 'additional_pharmaceutical_therapy', 'additional_radiation_therapy', 'lymphovascular_invasion_present', 'location_in_lung_parenchyma', 'pulmonary_function_test_performed', 'egfr_mutation_performed', 'diagnosis', 'eml4_alk_translocation_performed', 'days_to_new_tumor_event_after_initial_treatment', 'hemoglobin_result', 'serum_calcium_result', 'platelet_qualitative_result', 'number_of_lymphnodes_positive', 'white_cell_count_result', 'alcohol_history_documented', 'family_history_of_cancer', 'braf_gene_analysis_performed', 'city_of_procurement', 'surgical_approach', 'peritoneal_wash', 'Patient_description', 'prior_glioma', 'days_to_death', 'days_to_last_followup', 'icd_10', 'tissue_retrospective_collection_indicator', 'icd_o_3_histology', 'tissue_prospective_collection_indicator', 'history_of_neoadjuvant_treatment', 'icd_o_3_site', 'tumor_tissue_site', 'new_tumor_event_after_initial_treatment', 'radiation_therapy', 'race'], 'var_call_5D3dIq9Ywv2v0VGwqjDJrkHv': 'file_storage/call_5D3dIq9Ywv2v0VGwqjDJrkHv.json', 'var_call_n87WclNqBXnSVwQzLeOjtk02': 'file_storage/call_n87WclNqBXnSVwQzLeOjtk02.json'}

exec(code, env_args)
