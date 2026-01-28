code = """import json
p = var_call_DT2QHmXIh4XHBVg22Zqd8V35
with open(p, 'r') as f:
    data = json.load(f)

import pandas as pd

df = pd.DataFrame(data)
# Filter for Alive in Patient_description
alive = df[df['Patient_description'].str.contains('Alive', case=False, na=False)]

# Extract TCGA barcodes from Patient_description using coarse regex
import re

def extract_barcode(s):
    m = re.search(r'TCGA[-\w]{2,15}', s)
    if m:
        return m.group(0)
    m2 = re.search(r'barcode\s+([A-Z0-9-]+)', s, re.IGNORECASE)
    if m2:
        return m2.group(1)
    return None

alive['barcode'] = alive['Patient_description'].apply(extract_barcode)

result = {
    'n_total_breast_records': len(df),
    'n_alive_records': int(len(alive)),
    'sample_barcodes_first20': alive['barcode'].dropna().unique()[:20].tolist(),
    'top_histological_types_alive': alive['histological_type'].value_counts().head(10).to_dict()
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_hwMB1cpBoxUiXOxDqSEMOLrH': 'file_storage/call_hwMB1cpBoxUiXOxDqSEMOLrH.json', 'var_call_BZSRPIv9z7M76qAiog2KelFW': [], 'var_call_eSVK0WTf9xykotjwI82eBbvJ': {'columns_sample': ['Patient_description', 'days_to_birth', 'days_to_death', 'days_to_last_followup', 'days_to_initial_pathologic_diagnosis', 'age_at_initial_pathologic_diagnosis', 'icd_10', 'tissue_retrospective_collection_indicator', 'icd_o_3_histology', 'tissue_prospective_collection_indicator', 'history_of_neoadjuvant_treatment', 'icd_o_3_site', 'tumor_tissue_site', 'new_tumor_event_after_initial_treatment', 'radiation_therapy', 'race', 'prior_dx', 'ethnicity', 'informed_consent_verified', 'person_neoplasm_cancer_status', 'patient_id', 'year_of_initial_pathologic_diagnosis', 'histological_type', 'tissue_source_site', 'form_completion_date', 'pathologic_T', 'pathologic_M', 'clinical_M', 'pathologic_N', 'system_version', 'pathologic_stage', 'clinical_stage', 'clinical_T', 'clinical_N', 'extranodal_involvement', 'postoperative_rx_tx', 'primary_therapy_outcome_success', 'lymph_node_examined_count', 'primary_lymph_node_presentation_assessment', 'initial_pathologic_diagnosis_method'], 'n_rows_sample': 50, 'examples_patient_description_first5': ['In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'Patient TCGA-36-1576 (UUID 3445c524-5a37-40b6-8614-956d76eed939) is a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Current vital status: Alive.', 'Record fdd4adb8-9295-480a-9352-305b5eb51187 refers to patient TCGA-25-2408, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.', 'Record 6f25001a-f890-4fd0-a994-e62a9ea5c6f3 refers to patient TCGA-29-2427, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Alive.', 'Case 9446e349-71e6-455a-aa8f-53ec96597146, linked to barcode TCGA-10-0933, corresponds to a FEMALE patient diagnosed with Ovarian serous cystadenocarcinoma, with vital status Dead.'], 'count_contains_brca_in_sample': 0, 'count_contains_breast_in_sample': 0, 'examples_contains_breast_first5': []}, 'var_call_DT2QHmXIh4XHBVg22Zqd8V35': 'file_storage/call_DT2QHmXIh4XHBVg22Zqd8V35.json'}

exec(code, env_args)
