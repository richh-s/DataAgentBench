code = """import json, pandas as pd, math
# load clinical LGG mapping
p = var_call_C2ra6p6G2SigMXWIKgxBVFe8
with open(p,'r') as f:
    clinical = json.load(f)
# build mapping patient->histology, excluding histologies with brackets
mapping = {}
import re
for rec in clinical:
    hist = rec.get('histological_type')
    if not hist:
        continue
    if '[' in hist or ']' in hist:
        continue
    pd_desc = rec.get('Patient_description','')
    m = re.search(r"TCGA[-][A-Za-z0-9-]+", pd_desc)
    if not m:
        m = re.search(r"TCGA[0-9A-Za-z-]+", pd_desc)
    if not m:
        continue
    barcode = m.group(0)
    mapping[barcode] = hist
# load IGF2 expression data
q = var_call_7RvAaKEn5WYyfbmdF5mDKbvM
with open(q,'r') as f:
    expr = json.load(f)
# create dataframe
df_expr = pd.DataFrame(expr)
# Some normalized_count values may be strings; convert to float, coerce errors
df_expr['normalized_count'] = pd.to_numeric(df_expr['normalized_count'], errors='coerce')
# Filter expression for participants present in mapping
df_expr['histological_type'] = df_expr['ParticipantBarcode'].map(mapping)
# keep only those with histology (LGG patients)
df_lgg = df_expr[df_expr['histological_type'].notna()].copy()
# keep valid normalized_count (>=-inf and not null). Also per instructions: Only include patients with valid IGF2 expression values and histology annotations that are not enclosed in square brackets.
df_lgg = df_lgg[df_lgg['normalized_count'].notna()]
# compute log10(normalized_count + 1)
import numpy as np
# Handle potential negative counts by excluding negatives
df_lgg = df_lgg[df_lgg['normalized_count'] >= 0]
if df_lgg.empty:
    result = {}
else:
    df_lgg['log10_expr'] = np.log10(df_lgg['normalized_count'] + 1)
    # group by histological_type and compute mean
    grp = df_lgg.groupby('histological_type')['log10_expr'].mean()
    # format with at least four decimal places
    result = {k: float(f"{v:.4f}") for k,v in grp.to_dict().items()}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_qMNf9coQyRkArRfYiEdHq5Zp': ['clinical_info'], 'var_call_CrYE8uOLRiTw06NBMNknrh5A': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_681dfKoavxcY3dOkK9LQ6Dgd': [{'column_name': 'stopped_smoking_year', 'data_type': 'double precision'}, {'column_name': 'days_to_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'number_of_lymphnodes_positive_by_he', 'data_type': 'double precision'}, {'column_name': 'age_at_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'year_of_tobacco_smoking_onset', 'data_type': 'double precision'}, {'column_name': 'year_of_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'height', 'data_type': 'double precision'}, {'column_name': 'weight', 'data_type': 'double precision'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc', 'data_type': 'double precision'}, {'column_name': 'days_to_birth', 'data_type': 'double precision'}, {'column_name': 'total_pelv_lnr', 'data_type': 'double precision'}, {'column_name': 'total_aor_lnr', 'data_type': 'double precision'}, {'column_name': 'number_pack_years_smoked', 'data_type': 'double precision'}, {'column_name': 'prior_dx', 'data_type': 'text'}, {'column_name': 'ethnicity', 'data_type': 'text'}, {'column_name': 'informed_consent_verified', 'data_type': 'text'}, {'column_name': 'person_neoplasm_cancer_status', 'data_type': 'text'}, {'column_name': 'patient_id', 'data_type': 'text'}, {'column_name': 'histological_type', 'data_type': 'text'}, {'column_name': 'tissue_source_site', 'data_type': 'text'}, {'column_name': 'form_completion_date', 'data_type': 'text'}, {'column_name': 'pathologic_T', 'data_type': 'text'}, {'column_name': 'pathologic_M', 'data_type': 'text'}, {'column_name': 'clinical_M', 'data_type': 'text'}, {'column_name': 'pathologic_N', 'data_type': 'text'}, {'column_name': 'system_version', 'data_type': 'text'}, {'column_name': 'pathologic_stage', 'data_type': 'text'}, {'column_name': 'clinical_stage', 'data_type': 'text'}, {'column_name': 'clinical_T', 'data_type': 'text'}, {'column_name': 'clinical_N', 'data_type': 'text'}, {'column_name': 'extranodal_involvement', 'data_type': 'text'}, {'column_name': 'postoperative_rx_tx', 'data_type': 'text'}, {'column_name': 'primary_therapy_outcome_success', 'data_type': 'text'}, {'column_name': 'lymph_node_examined_count', 'data_type': 'text'}, {'column_name': 'primary_lymph_node_presentation_assessment', 'data_type': 'text'}, {'column_name': 'initial_pathologic_diagnosis_method', 'data_type': 'text'}, {'column_name': 'eastern_cancer_oncology_group', 'data_type': 'text'}, {'column_name': 'anatomic_neoplasm_subdivision', 'data_type': 'text'}, {'column_name': 'residual_tumor', 'data_type': 'text'}, {'column_name': 'histological_type_other', 'data_type': 'text'}, {'column_name': 'init_pathology_dx_method_other', 'data_type': 'text'}, {'column_name': 'karnofsky_performance_score', 'data_type': 'text'}, {'column_name': 'neoplasm_histologic_grade', 'data_type': 'text'}, {'column_name': 'tobacco_smoking_history', 'data_type': 'text'}, {'column_name': 'performance_status_scale_timing', 'data_type': 'text'}, {'column_name': 'laterality', 'data_type': 'text'}, {'column_name': 'targeted_molecular_therapy', 'data_type': 'text'}, {'column_name': 'anatomic_neoplasm_subdivision_other', 'data_type': 'text'}, {'column_name': 'patient_death_reason', 'data_type': 'text'}, {'column_name': 'tumor_tissue_site_other', 'data_type': 'text'}, {'column_name': 'menopause_status', 'data_type': 'text'}, {'column_name': 'margin_status', 'data_type': 'text'}, {'column_name': 'kras_gene_analysis_performed', 'data_type': 'text'}, {'column_name': 'venous_invasion', 'data_type': 'text'}, {'column_name': 'lymphatic_invasion', 'data_type': 'text'}, {'column_name': 'perineural_invasion_present', 'data_type': 'text'}, {'column_name': 'her2_immunohistochemistry_level_result', 'data_type': 'text'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status', 'data_type': 'text'}, {'column_name': 'breast_carcinoma_surgical_procedure_name', 'data_type': 'text'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text', 'data_type': 'text'}, {'column_name': 'axillary_lymph_node_stage_method_type', 'data_type': 'text'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status', 'data_type': 'text'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi', 'data_type': 'text'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status', 'data_type': 'text'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type', 'data_type': 'text'}, {'column_name': 'additional_pharmaceutical_therapy', 'data_type': 'text'}, {'column_name': 'additional_radiation_therapy', 'data_type': 'text'}, {'column_name': 'lymphovascular_invasion_present', 'data_type': 'text'}, {'column_name': 'location_in_lung_parenchyma', 'data_type': 'text'}, {'column_name': 'pulmonary_function_test_performed', 'data_type': 'text'}, {'column_name': 'egfr_mutation_performed', 'data_type': 'text'}, {'column_name': 'diagnosis', 'data_type': 'text'}, {'column_name': 'eml4_alk_translocation_performed', 'data_type': 'text'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment', 'data_type': 'text'}, {'column_name': 'hemoglobin_result', 'data_type': 'text'}, {'column_name': 'serum_calcium_result', 'data_type': 'text'}, {'column_name': 'platelet_qualitative_result', 'data_type': 'text'}, {'column_name': 'number_of_lymphnodes_positive', 'data_type': 'text'}, {'column_name': 'white_cell_count_result', 'data_type': 'text'}, {'column_name': 'alcohol_history_documented', 'data_type': 'text'}, {'column_name': 'family_history_of_cancer', 'data_type': 'text'}, {'column_name': 'braf_gene_analysis_performed', 'data_type': 'text'}, {'column_name': 'city_of_procurement', 'data_type': 'text'}, {'column_name': 'surgical_approach', 'data_type': 'text'}, {'column_name': 'peritoneal_wash', 'data_type': 'text'}, {'column_name': 'Patient_description', 'data_type': 'text'}, {'column_name': 'prior_glioma', 'data_type': 'text'}, {'column_name': 'days_to_death', 'data_type': 'text'}, {'column_name': 'days_to_last_followup', 'data_type': 'text'}, {'column_name': 'icd_10', 'data_type': 'text'}, {'column_name': 'tissue_retrospective_collection_indicator', 'data_type': 'text'}, {'column_name': 'icd_o_3_histology', 'data_type': 'text'}, {'column_name': 'tissue_prospective_collection_indicator', 'data_type': 'text'}, {'column_name': 'history_of_neoadjuvant_treatment', 'data_type': 'text'}, {'column_name': 'icd_o_3_site', 'data_type': 'text'}, {'column_name': 'tumor_tissue_site', 'data_type': 'text'}, {'column_name': 'new_tumor_event_after_initial_treatment', 'data_type': 'text'}, {'column_name': 'radiation_therapy', 'data_type': 'text'}, {'column_name': 'race', 'data_type': 'text'}], 'var_call_sOyORCywspMOhbEJlR71WRNV': 'file_storage/call_sOyORCywspMOhbEJlR71WRNV.json', 'var_call_I38SkmRgv9BBjCpGO19gYyED': 'file_storage/call_I38SkmRgv9BBjCpGO19gYyED.json', 'var_call_C2ra6p6G2SigMXWIKgxBVFe8': 'file_storage/call_C2ra6p6G2SigMXWIKgxBVFe8.json', 'var_call_zUPm7zszMqBsiWfDTqh5crv4': [{'cid': '0', 'name': 'ParticipantBarcode', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '1', 'name': 'SampleBarcode', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '2', 'name': 'AliquotBarcode', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '3', 'name': 'SampleTypeLetterCode', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '4', 'name': 'SampleType', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '5', 'name': 'Symbol', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '6', 'name': 'Entrez', 'type': 'BIGINT', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '7', 'name': 'normalized_count', 'type': 'DOUBLE', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}], 'var_call_gbHhl6hXp6aBz6cqEL3gio81': {'n_participants': 513, 'barcodes_sample': ['TCGA-RY-A83X', 'TCGA-FG-A60K', 'TCGA-DB-A4XH', 'TCGA-DB-A4XE', 'TCGA-DB-A4XC', 'TCGA-P5-A5F0', 'TCGA-S9-A6U1', 'TCGA-TM-A7C3', 'TCGA-S9-A7R2', 'TCGA-TM-A84R', 'TCGA-S9-A6TU', 'TCGA-HW-7490', 'TCGA-P5-A733', 'TCGA-DH-A7US', 'TCGA-HW-8319', 'TCGA-P5-A5F4', 'TCGA-FG-7637', 'TCGA-FG-A4MW', 'TCGA-E1-A7Z3', 'TCGA-S9-A7R4'], 'mapping_count': 513}, 'var_call_7RvAaKEn5WYyfbmdF5mDKbvM': 'file_storage/call_7RvAaKEn5WYyfbmdF5mDKbvM.json'}

exec(code, env_args)
