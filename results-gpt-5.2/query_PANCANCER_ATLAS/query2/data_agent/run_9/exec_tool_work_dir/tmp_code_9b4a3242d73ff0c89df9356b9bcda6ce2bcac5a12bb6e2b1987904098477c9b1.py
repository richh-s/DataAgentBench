code = """import json, re, pandas as pd

# load clinical alive breast records
path = var_call_8OkzjPqvLye4KXq3uVFVkPXG
with open(path,'r') as f:
    clin = json.load(f)

df_clin = pd.DataFrame(clin)
# extract TCGA barcode from Patient_description
pat = re.compile(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})')
df_clin['ParticipantBarcode'] = df_clin['Patient_description'].str.extract(pat)[0]
df_clin = df_clin.dropna(subset=['ParticipantBarcode'])

# load mutation CDH1 list
pathm = var_call_9vYyXCmcajaVP64ZikQftajl
with open(pathm,'r') as f:
    muts = json.load(f)
df_mut = pd.DataFrame(muts).drop_duplicates(subset=['ParticipantBarcode'])
df_mut['CDH1_mut'] = 1

# merge
m = df_clin.merge(df_mut[['ParticipantBarcode','CDH1_mut']], on='ParticipantBarcode', how='left')
m['CDH1_mut'] = m['CDH1_mut'].fillna(0).astype(int)

# group by histological_type
agg = m.groupby('histological_type', dropna=False).agg(
    n_alive=('ParticipantBarcode','nunique'),
    n_mut=('CDH1_mut','sum')
).reset_index()
agg['pct_mut'] = (agg['n_mut'] / agg['n_alive'] * 100).round(2)
agg = agg.sort_values(['pct_mut','n_alive'], ascending=[False,False])

# choose top 3 with at least some patients
top3 = agg.head(3)
res = top3.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_NIUs5kKRPTVx5wo6V4Cx8cby': ['clinical_info'], 'var_call_9o5i6VUp4YPdbWuLA0mqwEqj': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_9vYyXCmcajaVP64ZikQftajl': 'file_storage/call_9vYyXCmcajaVP64ZikQftajl.json', 'var_call_uuutKSYLKleL7rUERDf5XdPk': [], 'var_call_YpNbWSZ6VWbANlAFUYVjSDo8': [{'column_name': 'Patient_description'}, {'column_name': 'status'}, {'column_name': 'wal_status'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'histological_type'}, {'column_name': 'histological_type_other'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}], 'var_call_EFlowLPjgqME6gwJuRRZkvxl': [], 'var_call_PLJWsq6KJltTh8t7VtivnO4D': [], 'var_call_RWVcy4SBIqkIcIkJyyKH6gek': [{'column_name': 'Patient_description'}, {'column_name': 'days_to_birth'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}], 'var_call_e6wEFb6n3SQ04jwxMdHYPby5': [{'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'margin_status'}, {'column_name': 'menopause_status'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'person_neoplasm_cancer_status'}], 'var_call_UrTmCwv3W4vNVRRS5reJEHSB': [{'person_neoplasm_cancer_status': 'TUMOR FREE', 'n': '6264'}, {'person_neoplasm_cancer_status': 'WITH TUMOR', 'n': '3328'}, {'person_neoplasm_cancer_status': 'None', 'n': '673'}, {'person_neoplasm_cancer_status': '[Unknown]', 'n': '487'}, {'person_neoplasm_cancer_status': '[Discrepancy]', 'n': '9'}], 'var_call_Z7uV0Glzk3OI6FNmKa5XQl1S': [{'Patient_description': 'Case 57a1604c-60b7-4b30-a75e-f70939532c5c, linked to barcode TCGA-BH-A0B2, corresponds to a FEMALE patient diagnosed with Breast invasive carcinoma, with vital status Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}], 'var_call_IRjQpNDMtCSokb4WI32P8ABn': [], 'var_call_BAmolNEsEaaWWF5giLWE35EV': [{'tumor_tissue_site': 'Breast', 'n': '1087'}, {'tumor_tissue_site': 'Lung', 'n': '1004'}, {'tumor_tissue_site': 'Kidney', 'n': '869'}, {'tumor_tissue_site': 'Brain', 'n': '590'}, {'tumor_tissue_site': 'Ovary', 'n': '579'}, {'tumor_tissue_site': 'Head and Neck', 'n': '560'}, {'tumor_tissue_site': 'Endometrial', 'n': '530'}, {'tumor_tissue_site': 'Central nervous system', 'n': '513'}, {'tumor_tissue_site': 'Thyroid', 'n': '503'}, {'tumor_tissue_site': 'Prostate', 'n': '495'}, {'tumor_tissue_site': 'Colon', 'n': '442'}, {'tumor_tissue_site': 'Stomach', 'n': '440'}, {'tumor_tissue_site': 'Bladder', 'n': '412'}, {'tumor_tissue_site': 'Liver', 'n': '374'}, {'tumor_tissue_site': 'Cervical', 'n': '306'}, {'tumor_tissue_site': 'Extremities', 'n': '193'}, {'tumor_tissue_site': 'Pancreas', 'n': '184'}, {'tumor_tissue_site': 'Esophagus', 'n': '183'}, {'tumor_tissue_site': 'Trunk', 'n': '169'}, {'tumor_tissue_site': 'Rectum', 'n': '156'}, {'tumor_tissue_site': 'Adrenal gland', 'n': '146'}, {'tumor_tissue_site': 'Testes', 'n': '133'}, {'tumor_tissue_site': 'None', 'n': '100'}, {'tumor_tissue_site': 'Thymus', 'n': '97'}, {'tumor_tissue_site': 'Adrenal', 'n': '91'}, {'tumor_tissue_site': 'Pleura', 'n': '87'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum', 'n': '69'}, {'tumor_tissue_site': 'Uterus', 'n': '57'}, {'tumor_tissue_site': 'Choroid', 'n': '56'}, {'tumor_tissue_site': 'Lower Extremity - Thigh/knee', 'n': '44'}], 'var_call_5UDRGGs4xa1yI8pBBIqabZzm': [{'Patient_description': 'Case 57a1604c-60b7-4b30-a75e-f70939532c5c, linked to barcode TCGA-BH-A0B2, corresponds to a FEMALE patient diagnosed with Breast invasive carcinoma, with vital status Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}], 'var_call_CDXZA78sst8zMhlLmieRWSxR': [{'n_breast': '1087'}], 'var_call_HtSwgq7Mgg9tzZYeqXFCCT2v': [{'alive_breast': '1'}], 'var_call_fcTHue5iM0XMuQVcQNkWPuWx': [{'dtd_null': 'NOT_NULL', 'n': '1086'}, {'dtd_null': 'NULL', 'n': '1'}], 'var_call_BWJBPPayhJCiBIHrDcsEv05Q': [{'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'patient_death_reason'}], 'var_call_WXZqW2o5utC9O2XR1JSf2auv': [{'Patient_description': 'Clinical entry D13FB44B-291B-4EA4-920C-142DAA8D1989 identifies patient TCGA-AC-A5EH, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.'}, {'Patient_description': 'Record 09A5E9FD-D816-4F8C-BAA9-0E40BA607B16 refers to patient TCGA-LL-A7SZ, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.'}, {'Patient_description': "Patient TCGA-AN-A0FY, registered under UUID de75d0b9-0f47-4732-8df5-05c350cfcd32, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive."}, {'Patient_description': 'Patient TCGA-AC-A2FB (UUID 02BBB632-0F7F-439D-B8F0-C86A06237424) is a FEMALE diagnosed with Breast invasive carcinoma. Current vital status: Alive.'}, {'Patient_description': 'The individual with barcode TCGA-AO-A1KR and UUID b7f74ae1-6f58-447c-be50-a7666eb19d9a is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.'}], 'var_call_rtk4j2X1yOXczj9VVEBE3Yst': [{'alive_breast': '936'}], 'var_call_8OkzjPqvLye4KXq3uVFVkPXG': 'file_storage/call_8OkzjPqvLye4KXq3uVFVkPXG.json'}

exec(code, env_args)
