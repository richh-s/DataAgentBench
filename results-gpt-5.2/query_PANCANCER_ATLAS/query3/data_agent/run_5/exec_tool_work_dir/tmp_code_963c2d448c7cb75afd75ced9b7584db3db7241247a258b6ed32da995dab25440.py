code = """import json, re, pandas as pd
from pathlib import Path

def load_records(v):
    if isinstance(v, str) and v.endswith('.json') and Path(v).exists():
        return json.load(open(v,'r'))
    return v

clin = load_records(var_call_6vcKwPoIT43trGT3OWMoIZVk)
mut = load_records(var_call_iWlHfBWYLpdRYl2DMyjV3Qps)

df_clin = pd.DataFrame(clin)
df_mut = pd.DataFrame(mut)

# Extract TCGA participant barcode from Patient_description text
pat = re.compile(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})')
df_clin['barcode'] = df_clin['participant_barcode'].str.extract(pat, expand=False)
# Keep only FEMALE explicitly mentioned (since no gender column)
df_clin = df_clin[df_clin['participant_barcode'].str.contains('FEMALE', na=False)]

df_clin = df_clin.dropna(subset=['barcode','histological_type'])

# mutation presence per patient (PASS already filtered). We'll focus BRCA cohort via clinical list.
df_mut['barcode'] = df_mut['participant_barcode']
df_mut = df_mut[['barcode']].drop_duplicates()
df_mut['has_cdh1_mut'] = 1

# Merge; patients without mutation -> 0
merged = df_clin[['barcode','histological_type']].drop_duplicates().merge(df_mut, on='barcode', how='left')
merged['has_cdh1_mut'] = merged['has_cdh1_mut'].fillna(0).astype(int)

# Build contingency table
ct = pd.crosstab(merged['histological_type'], merged['has_cdh1_mut'])
# Ensure both columns 0 and 1 exist
for c in [0,1]:
    if c not in ct.columns:
        ct[c] = 0
ct = ct[[0,1]]

# Exclude histological categories with marginal totals <=10
ct_filt = ct[ct.sum(axis=1) > 10].copy()

# Exclude columns with marginal totals <=10 (mutation present/absent)
col_totals = ct_filt.sum(axis=0)
keep_cols = [c for c in ct_filt.columns if col_totals[c] > 10]
ct_filt = ct_filt[keep_cols]

# If after filtering we don't have 2 columns, chi-square not defined for association
result = {
    'n_patients_with_known_histology_female_breast_site': int(merged.shape[0]),
    'contingency_table_after_filtering': ct_filt.astype(int).to_dict(orient='index'),
}

if ct_filt.shape[0] >= 2 and ct_filt.shape[1] >= 2:
    obs = ct_filt.to_numpy(dtype=float)
    row_tot = obs.sum(axis=1, keepdims=True)
    col_tot = obs.sum(axis=0, keepdims=True)
    grand = obs.sum()
    exp = row_tot @ (col_tot / grand)
    chi2 = float(((obs-exp)**2/exp).sum())
    dof = int((ct_filt.shape[0]-1)*(ct_filt.shape[1]-1))
    result.update({'chi_square': chi2, 'dof': dof, 'grand_total_after_filtering': int(grand)})
else:
    result.update({'chi_square': None, 'dof': None, 'grand_total_after_filtering': int(ct_filt.to_numpy().sum())})

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_iWlHfBWYLpdRYl2DMyjV3Qps': 'file_storage/call_iWlHfBWYLpdRYl2DMyjV3Qps.json', 'var_call_rR6rmmiU4nGWe9zEnutRg9G5': ['clinical_info'], 'var_call_H5z05TCYapNOwUGn9XBTZTb7': [{'column_name': 'Patient_description'}, {'column_name': 'days_to_birth'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'stopped_smoking_year'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'prior_glioma'}], 'var_call_a89Gcfe9DYLYTXk93GXNlS5h': [], 'var_call_omeEhW2beNZq5yIN5IobNt2F': [], 'var_call_8SEVZ7l7Kowts891M7HCeAA6': [{'diagnosis': 'Lung Adenocarcinoma'}, {'diagnosis': 'None'}, {'diagnosis': 'Lung Squamous Cell Carcinoma'}], 'var_call_tPg7KLh3ejnxsIxz4fhpIT2v': [{'icd_10': 'C54.9'}, {'icd_10': 'C25.9'}, {'icd_10': 'C69.80'}, {'icd_10': 'C13.9'}, {'icd_10': 'C77.4'}, {'icd_10': 'C34.8'}, {'icd_10': 'C77.2'}, {'icd_10': 'C49.20'}, {'icd_10': 'C83.3'}, {'icd_10': 'C67.6'}, {'icd_10': 'C55'}, {'icd_10': 'C03.9'}, {'icd_10': 'C34.0'}, {'icd_10': 'C24.0'}, {'icd_10': 'C16.2'}, {'icd_10': 'C77.0'}, {'icd_10': 'C62.9'}, {'icd_10': 'C40.3'}, {'icd_10': 'C50.8'}, {'icd_10': 'C01'}, {'icd_10': 'C67.4'}, {'icd_10': 'C74.9'}, {'icd_10': 'C00.9'}, {'icd_10': 'C05.9'}, {'icd_10': 'C38.0'}, {'icd_10': 'C71.7'}, {'icd_10': 'C64.9'}, {'icd_10': 'C63.1'}, {'icd_10': 'C03.0'}, {'icd_10': 'C14.8'}, {'icd_10': 'C44.4'}, {'icd_10': 'C41.0'}, {'icd_10': 'C43.51'}, {'icd_10': 'C44.3'}, {'icd_10': 'C34.10'}, {'icd_10': 'C50.919'}, {'icd_10': 'C40.2'}, {'icd_10': 'C54.3'}, {'icd_10': 'C71.1'}, {'icd_10': 'C34.3'}, {'icd_10': 'C53.1'}, {'icd_10': 'C77.3'}, {'icd_10': 'C41.1'}, {'icd_10': 'C04.0'}, {'icd_10': 'C16.9'}, {'icd_10': 'C49.10'}, {'icd_10': 'C03.1'}, {'icd_10': 'C49.9'}, {'icd_10': 'C77.9'}, {'icd_10': 'C34.1'}], 'var_call_5ILqKtsA1dy9k8saIRBxKsbt': [{'tumor_tissue_site': 'Colon'}, {'tumor_tissue_site': 'Lung'}, {'tumor_tissue_site': 'Choroid|Ciliary body'}, {'tumor_tissue_site': 'Upper Extremity - Upper arm/elbow'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Kidney|Retroperitoneum/Upper abdominal - Liver|Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_tissue_site': 'Other  Specify'}, {'tumor_tissue_site': 'Head and Neck - Neck|Head and Neck - Other (please specify'}, {'tumor_tissue_site': 'Gynecological - Ovary'}, {'tumor_tissue_site': 'Lower Extremity - Lower leg/calf'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Other (please specify'}, {'tumor_tissue_site': 'Uterus'}, {'tumor_tissue_site': 'Extremities'}, {'tumor_tissue_site': 'Thyroid'}, {'tumor_tissue_site': 'Cervical'}, {'tumor_tissue_site': 'Choroid'}, {'tumor_tissue_site': 'Ovary'}, {'tumor_tissue_site': 'Upper Extremity - Shoulder/axilla'}, {'tumor_tissue_site': 'Peritoneum ovary'}, {'tumor_tissue_site': 'Stomach'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Pelvic'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Bladder'}, {'tumor_tissue_site': 'Head and Neck - Head'}, {'tumor_tissue_site': 'Kidney'}, {'tumor_tissue_site': 'Head and Neck'}, {'tumor_tissue_site': 'Lower Extremity - Other (please specify'}, {'tumor_tissue_site': 'Pancreas'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Pelvic|Gynecological - Uterus'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum|Retroperitoneum/Upper abdominal - Intraabdominal|Lower abdominal/Pelvic - Pelvic'}, {'tumor_tissue_site': 'Extremities|Extremities'}, {'tumor_tissue_site': 'Pleura'}, {'tumor_tissue_site': 'Brain'}, {'tumor_tissue_site': 'Anterior Mediastinum'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Colon'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Gastric'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Kidney'}, {'tumor_tissue_site': 'Testes'}, {'tumor_tissue_site': 'Trunk'}, {'tumor_tissue_site': 'Breast'}, {'tumor_tissue_site': 'Extremities|Trunk'}, {'tumor_tissue_site': 'Prostate'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Spermatic Cord'}, {'tumor_tissue_site': 'Head and Neck - Other (please specify'}, {'tumor_tissue_site': 'Head and Neck - Head|Chest - Chest wall'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Pancreas'}, {'tumor_tissue_site': 'Lower Extremity - Thigh/knee'}, {'tumor_tissue_site': 'Trunk|[Not Available]'}, {'tumor_tissue_site': 'Central nervous system'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Intraabdominal|Retroperitoneum/Upper abdominal - Small Intestines'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Intraabdominal|Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_tissue_site': 'Adrenal gland'}], 'var_call_6vcKwPoIT43trGT3OWMoIZVk': 'file_storage/call_6vcKwPoIT43trGT3OWMoIZVk.json'}

exec(code, env_args)
