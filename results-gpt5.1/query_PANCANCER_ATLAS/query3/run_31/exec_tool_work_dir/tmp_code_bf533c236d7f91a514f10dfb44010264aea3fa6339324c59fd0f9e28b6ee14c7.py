code = """import json, pandas as pd
from collections import Counter

# Load full mutation data
path = var_call_xIvfahSGTLQJV2QyXzX3ehs8
with open(path, 'r') as f:
    mut = json.load(f)
mut_df = pd.DataFrame(mut)

# Keep only reliable mutation entries (FILTER == 'PASS')
mut_pass = mut_df[mut_df['FILTER'] == 'PASS'].copy()
mut_patients = set(mut_pass['ParticipantBarcode'].unique())

# Load full clinical BRCA female data
path2 = var_call_CN8Zu5MhGwADqjTQBVm7Snsp
with open(path2, 'r') as f:
    clin = json.load(f)
clin_df = pd.DataFrame(clin)

# Extract patient barcode from Patient_description text (pattern 'patient TCGA-..-....' or 'barcode TCGA-..-....')
import re

def extract_barcode(desc):
    if not isinstance(desc, str):
        return None
    m = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', desc)
    return m.group(1) if m else None

clin_df['ParticipantBarcode'] = clin_df['Patient_description'].apply(extract_barcode)
clin_df = clin_df.dropna(subset=['ParticipantBarcode', 'histological_type'])

# Limit to unique patients (if duplicates, keep first)
clin_df = clin_df.drop_duplicates(subset=['ParticipantBarcode'])

# Define CDH1 mutation presence (reliable entries only)
clin_df['CDH1_mut'] = clin_df['ParticipantBarcode'].isin(mut_patients)

# Build contingency table: histological_type x CDH1_mut
ct = pd.crosstab(clin_df['histological_type'], clin_df['CDH1_mut'])

# Exclude histological categories with marginal totals <=10
row_totals = ct.sum(axis=1)
col_totals = ct.sum(axis=0)

valid_rows = row_totals[row_totals > 10].index
valid_cols = col_totals[col_totals > 10].index

ct_filtered = ct.loc[valid_rows, valid_cols]

# Compute chi-square statistic manually
import numpy as np

O = ct_filtered.values.astype(float)
row_sums = O.sum(axis=1, keepdims=True)
col_sums = O.sum(axis=0, keepdims=True)
grand_total = O.sum()

if grand_total == 0 or O.size == 0:
    result = {
        'error': 'Insufficient data after filtering to compute chi-square.',
        'contingency_table': ct.to_dict()
    }
else:
    E = row_sums @ col_sums / grand_total
    with np.errstate(divide='ignore', invalid='ignore'):
        chi_sq = np.nansum((O - E)**2 / E)
    dof = (O.shape[0]-1) * (O.shape[1]-1)
    result = {
        'chi_square': float(chi_sq),
        'degrees_of_freedom': int(dof),
        'contingency_table_filtered': ct_filtered.to_dict(),
        'row_totals': row_totals.to_dict(),
        'col_totals': col_totals.to_dict()
    }

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_xIvfahSGTLQJV2QyXzX3ehs8': 'file_storage/call_xIvfahSGTLQJV2QyXzX3ehs8.json', 'var_call_n9ZUeHTfamHPInXbsmAjfN2J': ['clinical_info'], 'var_call_dXP5WfudremsZIlIbAtRYMDk': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_call_NmRvsg10vBBNZUVYeRCc6FmO': [], 'var_call_CN8Zu5MhGwADqjTQBVm7Snsp': 'file_storage/call_CN8Zu5MhGwADqjTQBVm7Snsp.json'}

exec(code, env_args)
