code = """import json
p = var_call_Jcm29z9v6SOa5AniQaF5UXf2
with open(p, 'r') as f:
    data = json.load(f)

import pandas as pd

df = pd.DataFrame(data)
# Normalize ParticipantBarcode to first 12 chars like TCGA-XX-XXXX
# Many are TCGA-XX-XXXX or include sample-level; we'll extract first three groups of hyphen separated

def patient_barcode(pb):
    if not isinstance(pb, str):
        return None
    parts = pb.split('-')
    if len(parts) >= 3:
        return '-'.join(parts[:3])
    return pb

df['patient_barcode'] = df['ParticipantBarcode'].apply(patient_barcode)

# Count CDH1 mutations per patient
counts = df.groupby('patient_barcode').size().reset_index(name='mutation_count')

result = {
    'n_total_CDH1_records': len(df),
    'n_unique_patients_with_CDH1': int(counts['patient_barcode'].nunique()),
    'sample_patient_barcodes_first20': counts['patient_barcode'].dropna().unique()[:20].tolist()
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_hwMB1cpBoxUiXOxDqSEMOLrH': 'file_storage/call_hwMB1cpBoxUiXOxDqSEMOLrH.json', 'var_call_BZSRPIv9z7M76qAiog2KelFW': [], 'var_call_eSVK0WTf9xykotjwI82eBbvJ': {'columns_sample': ['Patient_description', 'days_to_birth', 'days_to_death', 'days_to_last_followup', 'days_to_initial_pathologic_diagnosis', 'age_at_initial_pathologic_diagnosis', 'icd_10', 'tissue_retrospective_collection_indicator', 'icd_o_3_histology', 'tissue_prospective_collection_indicator', 'history_of_neoadjuvant_treatment', 'icd_o_3_site', 'tumor_tissue_site', 'new_tumor_event_after_initial_treatment', 'radiation_therapy', 'race', 'prior_dx', 'ethnicity', 'informed_consent_verified', 'person_neoplasm_cancer_status', 'patient_id', 'year_of_initial_pathologic_diagnosis', 'histological_type', 'tissue_source_site', 'form_completion_date', 'pathologic_T', 'pathologic_M', 'clinical_M', 'pathologic_N', 'system_version', 'pathologic_stage', 'clinical_stage', 'clinical_T', 'clinical_N', 'extranodal_involvement', 'postoperative_rx_tx', 'primary_therapy_outcome_success', 'lymph_node_examined_count', 'primary_lymph_node_presentation_assessment', 'initial_pathologic_diagnosis_method'], 'n_rows_sample': 50, 'examples_patient_description_first5': ['In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'Patient TCGA-36-1576 (UUID 3445c524-5a37-40b6-8614-956d76eed939) is a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Current vital status: Alive.', 'Record fdd4adb8-9295-480a-9352-305b5eb51187 refers to patient TCGA-25-2408, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.', 'Record 6f25001a-f890-4fd0-a994-e62a9ea5c6f3 refers to patient TCGA-29-2427, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Alive.', 'Case 9446e349-71e6-455a-aa8f-53ec96597146, linked to barcode TCGA-10-0933, corresponds to a FEMALE patient diagnosed with Ovarian serous cystadenocarcinoma, with vital status Dead.'], 'count_contains_brca_in_sample': 0, 'count_contains_breast_in_sample': 0, 'examples_contains_breast_first5': []}, 'var_call_DT2QHmXIh4XHBVg22Zqd8V35': 'file_storage/call_DT2QHmXIh4XHBVg22Zqd8V35.json', 'var_call_p1MYrlHZNI2rIHahh9Cyup1P': {'n_total_breast_records': 1000, 'n_alive_records': 857, 'sample_barcodes_first20': ['TCGA-AC-A5EH', 'TCGA-LL-A7SZ', 'TCGA-AN-A0FY', 'TCGA-AC-A2FB', 'TCGA-AO-A1KR', 'TCGA-3C-AAAU', 'TCGA-A7-A26I', 'TCGA-A7-A5ZW', 'TCGA-C8-A26Z', 'TCGA-EW-A6SA', 'TCGA-C8-A273', 'TCGA-AN-A0FN', 'TCGA-AN-A0FD', 'TCGA-AN-A0FS', 'TCGA-AO-A12H', 'TCGA-AN-A0AL', 'TCGA-AC-A3YI', 'TCGA-C8-A137', 'TCGA-S3-AA11', 'TCGA-LL-A7T0'], 'top_histological_types_alive': {'Infiltrating Ductal Carcinoma': 619, 'Infiltrating Lobular Carcinoma': 165, 'Other  specify': 35, 'Mixed Histology (please specify)': 14, 'Mucinous Carcinoma': 12, 'Metaplastic Carcinoma': 6, 'Medullary Carcinoma': 3, 'Infiltrating Carcinoma NOS': 1, 'Leiomyosarcoma (LMS)': 1, 'None': 1}}, 'var_call_Jcm29z9v6SOa5AniQaF5UXf2': 'file_storage/call_Jcm29z9v6SOa5AniQaF5UXf2.json'}

exec(code, env_args)
