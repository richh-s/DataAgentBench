code = """import json, pandas as pd
from collections import defaultdict

# Load full clinical female breast data
path = var_call_JdhEd57jqAZeHaZdN9nMIvqM
with open(path, 'r') as f:
    clinical = json.load(f)
clinical_df = pd.DataFrame(clinical)

# Extract patient barcode from Patient_description (string contains 'patient TCGA-XX-XXXX' or 'barcode TCGA-XX-XXXX')
import re

def extract_barcode(desc):
    m = re.search(r'(?:patient|barcode) (TCGA-[A-Z0-9-]+)', desc)
    return m.group(1) if m else None

clinical_df['ParticipantBarcode'] = clinical_df['Patient_description'].apply(extract_barcode)
clinical_df = clinical_df.dropna(subset=['ParticipantBarcode', 'histological_type'])

# Load CDH1 mutation data and keep reliable entries (FILTER='PASS')
import os
path_mut = var_call_1uui1qfiw5qmNKwx6p9FGIBG
with open(path_mut, 'r') as f:
    mut = json.load(f)
mut_df = pd.DataFrame(mut)
mut_df = mut_df[mut_df['FILTER'] == 'PASS']

# For each patient, define CDH1_mutated = 1 if any PASS mutation present
mutated_patients = set(mut_df['ParticipantBarcode'].unique())
clinical_df['CDH1_mutated'] = clinical_df['ParticipantBarcode'].isin(mutated_patients)

# Build contingency table: histological_type x CDH1_mutated
ct = pd.crosstab(clinical_df['histological_type'], clinical_df['CDH1_mutated'])
ct = ct.rename(columns={False:'CDH1_not_mutated', True:'CDH1_mutated'})

# Exclude categories with marginal totals <= 10
row_totals = ct.sum(axis=1)
col_totals = ct.sum(axis=0)
valid_rows = row_totals[row_totals > 10].index
valid_cols = col_totals[col_totals > 10].index
ct_filtered = ct.loc[valid_rows, valid_cols]

grand_total = ct_filtered.values.sum()

# Compute chi-square
import numpy as np
chi2 = 0.0
for i in range(ct_filtered.shape[0]):
    for j in range(ct_filtered.shape[1]):
        observed = ct_filtered.iat[i, j]
        expected = row_totals[ct_filtered.index[i]] * col_totals[ct_filtered.columns[j]] / grand_total
        if expected > 0:
            chi2 += (observed - expected) ** 2 / expected

result = {
    'contingency_table': ct_filtered.to_dict(),
    'chi_square_statistic': chi2,
    'grand_total': int(grand_total),
    'note': 'Only female Breast invasive carcinoma cases with known histological_type and PASS CDH1 mutations; histological and mutation-status categories with marginal totals <=10 excluded.'
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_1uui1qfiw5qmNKwx6p9FGIBG': 'file_storage/call_1uui1qfiw5qmNKwx6p9FGIBG.json', 'var_call_h8FrSmdxm2s9BeK1IoI0lxRe': ['clinical_info'], 'var_call_K0SGGZmKvIKrstazIFdqgyjd': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_call_jpYpOow3fWqJ8qbZs6hDofae': [], 'var_call_JdhEd57jqAZeHaZdN9nMIvqM': 'file_storage/call_JdhEd57jqAZeHaZdN9nMIvqM.json'}

exec(code, env_args)
