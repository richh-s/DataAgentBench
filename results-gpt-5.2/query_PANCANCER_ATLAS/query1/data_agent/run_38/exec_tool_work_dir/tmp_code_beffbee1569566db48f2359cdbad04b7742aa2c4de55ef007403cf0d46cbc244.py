code = """import json, re, math, pandas as pd

# load IGF2 expression rows
igf2_src = var_call_7KJUsnbfRiSpzM3PYUQXgJLc
if isinstance(igf2_src, str):
    with open(igf2_src, 'r') as f:
        igf2 = json.load(f)
else:
    igf2 = igf2_src

# load LGG clinical rows (patient_description contains barcode)
clin_src = var_call_bpBnFFZGdLhxflpPF4PpPsUd
if isinstance(clin_src, str):
    with open(clin_src, 'r') as f:
        clin = json.load(f)
else:
    clin = clin_src

# parse barcode from Patient_description
pat = []
for r in clin:
    desc = r.get('Patient_description') or ''
    m = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', desc)
    if not m:
        continue
    hist = r.get('histological_type')
    if hist is None:
        continue
    # exclude histology enclosed in square brackets
    hs = str(hist).strip()
    if re.fullmatch(r'\[.*\]', hs):
        continue
    pat.append({'ParticipantBarcode': m.group(1), 'histological_type': hs})

clin_df = pd.DataFrame(pat).drop_duplicates()

expr_df = pd.DataFrame(igf2)
# ensure numeric
expr_df['normalized_count'] = pd.to_numeric(expr_df['normalized_count'], errors='coerce')
expr_df = expr_df.dropna(subset=['normalized_count'])
expr_df['log10_expr'] = (expr_df['normalized_count'] + 1).apply(lambda x: math.log10(x) if x>0 else float('nan'))
expr_df = expr_df.dropna(subset=['log10_expr'])

merged = expr_df.merge(clin_df, on='ParticipantBarcode', how='inner')

res = (merged.groupby('histological_type')['log10_expr']
       .mean()
       .reset_index()
       .sort_values('histological_type'))
res['avg_log10_igf2'] = res['log10_expr'].map(lambda v: float(f"{v:.4f}"))
res = res[['histological_type','avg_log10_igf2']]

out = res.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_nHAqGPUdfBgzSS3JKkIFj2EK': ['clinical_info'], 'var_call_xXsH7dic1kl9UXZuI7BJKVqO': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_4bgIEGPF3YMx3zs7SmvTXl5u': [{'column_name': 'Patient_description'}, {'column_name': 'days_to_birth'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'stopped_smoking_year'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'prior_glioma'}], 'var_call_8qaEq0hyLnObKALzMQK0yHuS': [{'diagnosis': 'Lung Adenocarcinoma'}, {'diagnosis': 'Lung Squamous Cell Carcinoma'}], 'var_call_5i9OqehhcdFQWiXVeT2M6BFm': [{'tumor_tissue_site': 'Adrenal'}, {'tumor_tissue_site': 'Adrenal gland'}, {'tumor_tissue_site': 'Anterior Mediastinum'}, {'tumor_tissue_site': 'Bile duct'}, {'tumor_tissue_site': 'Bladder'}, {'tumor_tissue_site': 'Brain'}, {'tumor_tissue_site': 'Breast'}, {'tumor_tissue_site': 'Central nervous system'}, {'tumor_tissue_site': 'Cervical'}, {'tumor_tissue_site': 'Chest - Breast'}, {'tumor_tissue_site': 'Chest - Chest wall'}, {'tumor_tissue_site': 'Chest - Lung/pleura'}, {'tumor_tissue_site': 'Chest - Mediastinum'}, {'tumor_tissue_site': 'Chest - Other (please specify'}, {'tumor_tissue_site': 'Choroid'}, {'tumor_tissue_site': 'Choroid|Ciliary body'}, {'tumor_tissue_site': 'Choroid|Ciliary body|Iris'}, {'tumor_tissue_site': 'Colon'}, {'tumor_tissue_site': 'Endometrial'}, {'tumor_tissue_site': 'Esophagus'}, {'tumor_tissue_site': 'Extra-adrenal Site'}, {'tumor_tissue_site': 'Extremities'}, {'tumor_tissue_site': 'Extremities|Extremities'}, {'tumor_tissue_site': 'Extremities|Trunk'}, {'tumor_tissue_site': 'Gynecological - Ovary'}, {'tumor_tissue_site': 'Gynecological - Uterus'}, {'tumor_tissue_site': 'Gynecological - Uterus|Gynecological - Cervix'}, {'tumor_tissue_site': 'Gynecological - Uterus|Gynecological - Other (please specify'}, {'tumor_tissue_site': 'Head and Neck'}, {'tumor_tissue_site': 'Head and Neck - Head'}, {'tumor_tissue_site': 'Head and Neck - Head|Chest - Chest wall'}, {'tumor_tissue_site': 'Head and Neck - Neck|Head and Neck - Other (please specify'}, {'tumor_tissue_site': 'Head and Neck - Other (please specify'}, {'tumor_tissue_site': 'Kidney'}, {'tumor_tissue_site': 'Liver'}, {'tumor_tissue_site': 'Lower Extremity - Foot/ankle'}, {'tumor_tissue_site': 'Lower Extremity - Groin'}, {'tumor_tissue_site': 'Lower Extremity - Lower leg/calf'}, {'tumor_tissue_site': 'Lower Extremity - Other (please specify'}, {'tumor_tissue_site': 'Lower Extremity - Thigh/knee'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Bladder'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Other (please specify'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Pelvic'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Pelvic|Gynecological - Uterus'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Spermatic Cord'}, {'tumor_tissue_site': 'Lung'}, {'tumor_tissue_site': 'Omentum'}, {'tumor_tissue_site': 'Other  Specify'}, {'tumor_tissue_site': 'Ovary'}, {'tumor_tissue_site': 'Pancreas'}], 'var_call_kGi2OcOBNyM77agfHi4ghZgZ': [{'n': '496'}], 'var_call_7KJUsnbfRiSpzM3PYUQXgJLc': 'file_storage/call_7KJUsnbfRiSpzM3PYUQXgJLc.json', 'var_call_cGYwNjtmqeDDozFbJlkbhjoD': 'file_storage/call_cGYwNjtmqeDDozFbJlkbhjoD.json', 'var_call_m2eEXMnPF6VQHew40zM1Kxpy': [], 'var_call_bpBnFFZGdLhxflpPF4PpPsUd': 'file_storage/call_bpBnFFZGdLhxflpPF4PpPsUd.json'}

exec(code, env_args)
