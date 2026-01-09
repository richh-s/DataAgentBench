code = """import json, re, math, pandas as pd

# Load brain clinical rows
brain_src = var_call_OPZ7a2DeLfVYrj426ucdfe6d
if isinstance(brain_src, str) and brain_src.endswith('.json'):
    with open(brain_src, 'r') as f:
        brain = json.load(f)
else:
    brain = brain_src

# Extract TCGA barcode from Patient_description
pat = re.compile(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})')
rows=[]
for r in brain:
    desc = r.get('participantbarcode') or r.get('ParticipantBarcode') or r.get('Patient_description')
    if not desc:
        continue
    m = pat.search(desc)
    if not m:
        continue
    barcode = m.group(1)
    hist = r.get('histology')
    if hist is None:
        continue
    if re.fullmatch(r'\[.*\]', str(hist)):
        continue
    rows.append({'ParticipantBarcode': barcode, 'histology': str(hist)})
clin_df = pd.DataFrame(rows).drop_duplicates()

# Load IGF2 expression
expr_src = var_call_397BJWqlDPLJYgtTuST1Szjx
if isinstance(expr_src, str) and expr_src.endswith('.json'):
    with open(expr_src, 'r') as f:
        expr = json.load(f)
else:
    expr = expr_src
expr_df = pd.DataFrame(expr)
expr_df['normalized_count'] = pd.to_numeric(expr_df['normalized_count'], errors='coerce')
expr_df = expr_df.dropna(subset=['normalized_count'])

# Filter to LGG patients by requiring they exist in expression and in clinical brain dataset with LGG-like histologies
# We do not have explicit acronym; use histology types typical of LGG (Astrocytoma, Oligodendroglioma, Mixed glioma)
keep_pat = re.compile(r'astro|oligo|mixed|glioma', re.IGNORECASE)
clin_df = clin_df[clin_df['histology'].str.contains(keep_pat, na=False)]

merged = clin_df.merge(expr_df[['ParticipantBarcode','normalized_count']], on='ParticipantBarcode', how='inner')
merged['log10_expr'] = (merged['normalized_count'] + 1).apply(lambda x: math.log10(x))

out = (merged.groupby('histology', as_index=False)
       .agg(n_patients=('ParticipantBarcode','nunique'), avg_log10_igf2=('log10_expr','mean'))
       .sort_values('avg_log10_igf2', ascending=False))

out['avg_log10_igf2'] = out['avg_log10_igf2'].map(lambda v: float(f"{v:.4f}"))
result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_397BJWqlDPLJYgtTuST1Szjx': 'file_storage/call_397BJWqlDPLJYgtTuST1Szjx.json', 'var_call_xD38hNSqdtsjX4wWc9Mggk99': ['clinical_info'], 'var_call_0ROICs88t8D774l8Adgiksfw': 'file_storage/call_0ROICs88t8D774l8Adgiksfw.json', 'var_call_oMCoo9E4S2UgocHzU21THjwO': [{'column_name': 'Patient_description'}, {'column_name': 'days_to_birth'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'stopped_smoking_year'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'prior_glioma'}], 'var_call_cKqXr9HK9jnnRhQwCXxJ1Vlm': [{'tumor_site': 'Adrenal'}, {'tumor_site': 'Adrenal gland'}, {'tumor_site': 'Anterior Mediastinum'}, {'tumor_site': 'Bile duct'}, {'tumor_site': 'Bladder'}, {'tumor_site': 'Brain'}, {'tumor_site': 'Breast'}, {'tumor_site': 'Central nervous system'}, {'tumor_site': 'Cervical'}, {'tumor_site': 'Chest - Breast'}, {'tumor_site': 'Chest - Chest wall'}, {'tumor_site': 'Chest - Lung/pleura'}, {'tumor_site': 'Chest - Mediastinum'}, {'tumor_site': 'Chest - Other (please specify'}, {'tumor_site': 'Choroid'}, {'tumor_site': 'Choroid|Ciliary body'}, {'tumor_site': 'Choroid|Ciliary body|Iris'}, {'tumor_site': 'Colon'}, {'tumor_site': 'Endometrial'}, {'tumor_site': 'Esophagus'}, {'tumor_site': 'Extra-adrenal Site'}, {'tumor_site': 'Extremities'}, {'tumor_site': 'Extremities|Extremities'}, {'tumor_site': 'Extremities|Trunk'}, {'tumor_site': 'Gynecological - Ovary'}, {'tumor_site': 'Gynecological - Uterus'}, {'tumor_site': 'Gynecological - Uterus|Gynecological - Cervix'}, {'tumor_site': 'Gynecological - Uterus|Gynecological - Other (please specify'}, {'tumor_site': 'Head and Neck'}, {'tumor_site': 'Head and Neck - Head'}, {'tumor_site': 'Head and Neck - Head|Chest - Chest wall'}, {'tumor_site': 'Head and Neck - Neck|Head and Neck - Other (please specify'}, {'tumor_site': 'Head and Neck - Other (please specify'}, {'tumor_site': 'Kidney'}, {'tumor_site': 'Liver'}, {'tumor_site': 'Lower Extremity - Foot/ankle'}, {'tumor_site': 'Lower Extremity - Groin'}, {'tumor_site': 'Lower Extremity - Lower leg/calf'}, {'tumor_site': 'Lower Extremity - Other (please specify'}, {'tumor_site': 'Lower Extremity - Thigh/knee'}, {'tumor_site': 'Lower abdominal/Pelvic - Bladder'}, {'tumor_site': 'Lower abdominal/Pelvic - Other (please specify'}, {'tumor_site': 'Lower abdominal/Pelvic - Pelvic'}, {'tumor_site': 'Lower abdominal/Pelvic - Pelvic|Gynecological - Uterus'}, {'tumor_site': 'Lower abdominal/Pelvic - Spermatic Cord'}, {'tumor_site': 'Lung'}, {'tumor_site': 'Omentum'}, {'tumor_site': 'Other  Specify'}, {'tumor_site': 'Ovary'}, {'tumor_site': 'Pancreas'}, {'tumor_site': 'Peritoneum ovary'}, {'tumor_site': 'Pleura'}, {'tumor_site': 'Prostate'}, {'tumor_site': 'Rectum'}, {'tumor_site': 'Retroperitoneum/Upper abdominal - Colon'}, {'tumor_site': 'Retroperitoneum/Upper abdominal - Gastric'}, {'tumor_site': 'Retroperitoneum/Upper abdominal - Intraabdominal'}, {'tumor_site': 'Retroperitoneum/Upper abdominal - Intraabdominal|Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_site': 'Retroperitoneum/Upper abdominal - Intraabdominal|Retroperitoneum/Upper abdominal - Small Intestines'}, {'tumor_site': 'Retroperitoneum/Upper abdominal - Kidney'}, {'tumor_site': 'Retroperitoneum/Upper abdominal - Kidney|Retroperitoneum/Upper abdominal - Liver|Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_site': 'Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_site': 'Retroperitoneum/Upper abdominal - Pancreas'}, {'tumor_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum'}, {'tumor_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum|Retroperitoneum/Upper abdominal - Intraabdominal|Lower abdominal/Pelvic - Pelvic'}, {'tumor_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum|Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum|Retroperitoneum/Upper abdominal - Small Intestines|Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_site': 'Retroperitoneum/Upper abdominal - Small Intestines'}, {'tumor_site': 'Retroperitoneum/Upper abdominal - Small Intestines|Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_site': 'Stomach'}, {'tumor_site': 'Superficial Trunk - Abdominal wall'}, {'tumor_site': 'Superficial Trunk - Back'}, {'tumor_site': 'Superficial Trunk - Buttock'}, {'tumor_site': 'Superficial Trunk - Flank'}, {'tumor_site': 'Testes'}, {'tumor_site': 'Thymus'}, {'tumor_site': 'Thyroid'}, {'tumor_site': 'Trunk'}, {'tumor_site': 'Trunk|Extremities'}, {'tumor_site': 'Trunk|[Not Available]'}, {'tumor_site': 'Upper Extremity - Shoulder/axilla'}, {'tumor_site': 'Upper Extremity - Upper arm/elbow'}, {'tumor_site': 'Uterus'}, {'tumor_site': '[Unknown]'}, {'tumor_site': 'None'}], 'var_call_OPZ7a2DeLfVYrj426ucdfe6d': 'file_storage/call_OPZ7a2DeLfVYrj426ucdfe6d.json'}

exec(code, env_args)
