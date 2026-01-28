code = """import json
import pandas as pd
import re

clinical_rows = json.load(open(var_call_1ZjjC6h60mmOndImlSIa4mae))
cdh1_participants = json.load(open(var_call_xQDxRdqOLaqApdv0c0aAGz7V))

# Build set of participant barcodes from CDH1 mutation table
cdh1_set = set()
for r in cdh1_participants:
    val = r.get('ParticipantBarcode')
    if val:
        cdh1_set.add(val.strip())

# Parse clinical rows
records = []
pattern = re.compile(r'(TCGA[-][A-Za-z0-9-]+)')
for r in clinical_rows:
    desc = r.get('Patient_description','')
    hist = r.get('histological_type') or 'Unknown'
    pid = r.get('patient_id')
    m = pattern.search(desc)
    barcode = m.group(1) if m else None
    alive = False
    if isinstance(desc, str) and re.search(r'\balive\b', desc, flags=re.IGNORECASE):
        alive = True
    records.append({'barcode': barcode, 'patient_id': pid, 'histological_type': hist, 'alive': alive})

df = pd.DataFrame(records)
df_alive = df[(df['barcode'].notna()) & (df['alive']==True)].copy()
# Normalize histological_type

df_alive['histological_type'] = df_alive['histological_type'].fillna('Unknown')

# For breast dataset, common hist types include Infiltrating Ductal Carcinoma and Infiltrating Lobular Carcinoma
summary = []
for hist, grp in df_alive.groupby('histological_type'):
    alive_total = grp['barcode'].nunique()
    mutated = grp['barcode'].apply(lambda x: x in cdh1_set).sum()
    percent = (mutated / alive_total * 100) if alive_total>0 else 0
    summary.append({'histological_type': hist, 'alive_count': int(alive_total), 'mutated_count': int(mutated), 'percent_CDH1_mutation': round(percent,4)})

summary_sorted = sorted(summary, key=lambda x: (-x['percent_CDH1_mutation'], -x['alive_count']))

# get top 3
top3 = summary_sorted[:3]
print('__RESULT__:')
print(json.dumps(top3))"""

env_args = {'var_call_480FeO4VltkbJ1l1yt3K704U': ['clinical_info'], 'var_call_7r7LG46jLAvVhsQp2np1IRQ9': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_4F7h0MDIwq2Ye0Tm1Aae6VDm': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_hRtqc0JUSbXRVH8hpAW3jNo0': [], 'var_call_RYF3cOavFqRv1yyPdgGXjSE4': [], 'var_call_sZ0cAAzLodME6ffW9zVT2TL9': [{'cid': '0', 'name': 'ParticipantBarcode', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '1', 'name': 'Tumor_SampleBarcode', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '2', 'name': 'Tumor_AliquotBarcode', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '3', 'name': 'Normal_SampleBarcode', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '4', 'name': 'Normal_AliquotBarcode', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '5', 'name': 'Normal_SampleTypeLetterCode', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '6', 'name': 'Hugo_Symbol', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '7', 'name': 'HGVSp_Short', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '8', 'name': 'Variant_Classification', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '9', 'name': 'HGVSc', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '10', 'name': 'CENTERS', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '11', 'name': 'FILTER', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}], 'var_call_RhGvJMOpQ3J0rXjnTQYWEtSl': 'file_storage/call_RhGvJMOpQ3J0rXjnTQYWEtSl.json', 'var_call_4xUivGBFW00MjcSgQLj84yyj': 'file_storage/call_4xUivGBFW00MjcSgQLj84yyj.json', 'var_call_jjWLod0NBFkXcDq9VMqNDBrZ': [], 'var_call_xQDxRdqOLaqApdv0c0aAGz7V': 'file_storage/call_xQDxRdqOLaqApdv0c0aAGz7V.json', 'var_call_zdrZFEgSMOSBjrWHcYcPidFr': 'file_storage/call_zdrZFEgSMOSBjrWHcYcPidFr.json', 'var_call_Fvt9LvMJ4bOSRvoZaZOhOjvY': [], 'var_call_1ZjjC6h60mmOndImlSIa4mae': 'file_storage/call_1ZjjC6h60mmOndImlSIa4mae.json'}

exec(code, env_args)
