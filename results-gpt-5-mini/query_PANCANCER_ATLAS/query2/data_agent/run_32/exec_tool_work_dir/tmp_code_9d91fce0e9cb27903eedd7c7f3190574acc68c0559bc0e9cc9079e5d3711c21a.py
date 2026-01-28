code = """import json
# Load clinical breast alive data
p = var_call_DT2QHmXIh4XHBVg22Zqd8V35
with open(p, 'r') as f:
    clinical = json.load(f)

p2 = var_call_Jcm29z9v6SOa5AniQaF5UXf2
with open(p2, 'r') as f:
    muts = json.load(f)

import pandas as pd

clin = pd.DataFrame(clinical)
mut = pd.DataFrame(muts)

# Extract patient-level barcode from ParticipantBarcode
mut['patient_barcode'] = mut['ParticipantBarcode'].apply(lambda x: '-'.join(x.split('-')[:3]) if isinstance(x, str) else x)

# Extract barcode and alive status from clinical Patient_description
import re

def extract_barcode(s):
    m = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4,6})', s)
    if m:
        return m.group(1)
    return None

clin['patient_barcode'] = clin['Patient_description'].apply(extract_barcode)
clin_alive = clin[clin['Patient_description'].str.contains('Alive', case=False, na=False)].copy()

# Merge CDH1 mutations with clinical alive breast patients by barcode
cdh1 = mut[mut['Hugo_Symbol']=='CDH1'].copy()

merged = pd.merge(clin_alive, cdh1, on='patient_barcode', how='left', indicator=True)

# For each histological_type among alive patients, compute total patients and number with CDH1 mutation
# Need patient-level counts (unique patients)

# Total alive patients per histological_type
alive_unique = clin_alive.dropna(subset=['patient_barcode']).drop_duplicates(subset=['patient_barcode'])

total_per_hist = alive_unique.groupby('histological_type')['patient_barcode'].nunique().reset_index(name='total_patients')

# Patients with CDH1 mutations among alive
cdh1_patients = cdh1.copy()
cdh1_patients_unique = cdh1_patients.dropna(subset=['patient_barcode']).drop_duplicates(subset=['patient_barcode'])
# Join with clinical to get histological type
cdh1_clin = pd.merge(cdh1_patients_unique, clin_alive[['patient_barcode','histological_type']], on='patient_barcode', how='left')

mut_per_hist = cdh1_clin.groupby('histological_type')['patient_barcode'].nunique().reset_index(name='mutated_patients')

# Combine
summary = pd.merge(total_per_hist, mut_per_hist, on='histological_type', how='left').fillna(0)
summary['mutated_patients'] = summary['mutated_patients'].astype(int)
summary['percent_mutated'] = (summary['mutated_patients'] / summary['total_patients']) * 100

summary_sorted = summary.sort_values(by='percent_mutated', ascending=False)

# Take top 3
top3 = summary_sorted.head(3)

result = {
    'n_alive_breast_patients_total': int(alive_unique['patient_barcode'].nunique()),
    'summary_top3_hist_types': top3.to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_hwMB1cpBoxUiXOxDqSEMOLrH': 'file_storage/call_hwMB1cpBoxUiXOxDqSEMOLrH.json', 'var_call_BZSRPIv9z7M76qAiog2KelFW': [], 'var_call_eSVK0WTf9xykotjwI82eBbvJ': {'columns_sample': ['Patient_description', 'days_to_birth', 'days_to_death', 'days_to_last_followup', 'days_to_initial_pathologic_diagnosis', 'age_at_initial_pathologic_diagnosis', 'icd_10', 'tissue_retrospective_collection_indicator', 'icd_o_3_histology', 'tissue_prospective_collection_indicator', 'history_of_neoadjuvant_treatment', 'icd_o_3_site', 'tumor_tissue_site', 'new_tumor_event_after_initial_treatment', 'radiation_therapy', 'race', 'prior_dx', 'ethnicity', 'informed_consent_verified', 'person_neoplasm_cancer_status', 'patient_id', 'year_of_initial_pathologic_diagnosis', 'histological_type', 'tissue_source_site', 'form_completion_date', 'pathologic_T', 'pathologic_M', 'clinical_M', 'pathologic_N', 'system_version', 'pathologic_stage', 'clinical_stage', 'clinical_T', 'clinical_N', 'extranodal_involvement', 'postoperative_rx_tx', 'primary_therapy_outcome_success', 'lymph_node_examined_count', 'primary_lymph_node_presentation_assessment', 'initial_pathologic_diagnosis_method'], 'n_rows_sample': 50, 'examples_patient_description_first5': ['In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'Patient TCGA-36-1576 (UUID 3445c524-5a37-40b6-8614-956d76eed939) is a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Current vital status: Alive.', 'Record fdd4adb8-9295-480a-9352-305b5eb51187 refers to patient TCGA-25-2408, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.', 'Record 6f25001a-f890-4fd0-a994-e62a9ea5c6f3 refers to patient TCGA-29-2427, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Alive.', 'Case 9446e349-71e6-455a-aa8f-53ec96597146, linked to barcode TCGA-10-0933, corresponds to a FEMALE patient diagnosed with Ovarian serous cystadenocarcinoma, with vital status Dead.'], 'count_contains_brca_in_sample': 0, 'count_contains_breast_in_sample': 0, 'examples_contains_breast_first5': []}, 'var_call_DT2QHmXIh4XHBVg22Zqd8V35': 'file_storage/call_DT2QHmXIh4XHBVg22Zqd8V35.json', 'var_call_p1MYrlHZNI2rIHahh9Cyup1P': {'n_total_breast_records': 1000, 'n_alive_records': 857, 'sample_barcodes_first20': ['TCGA-AC-A5EH', 'TCGA-LL-A7SZ', 'TCGA-AN-A0FY', 'TCGA-AC-A2FB', 'TCGA-AO-A1KR', 'TCGA-3C-AAAU', 'TCGA-A7-A26I', 'TCGA-A7-A5ZW', 'TCGA-C8-A26Z', 'TCGA-EW-A6SA', 'TCGA-C8-A273', 'TCGA-AN-A0FN', 'TCGA-AN-A0FD', 'TCGA-AN-A0FS', 'TCGA-AO-A12H', 'TCGA-AN-A0AL', 'TCGA-AC-A3YI', 'TCGA-C8-A137', 'TCGA-S3-AA11', 'TCGA-LL-A7T0'], 'top_histological_types_alive': {'Infiltrating Ductal Carcinoma': 619, 'Infiltrating Lobular Carcinoma': 165, 'Other  specify': 35, 'Mixed Histology (please specify)': 14, 'Mucinous Carcinoma': 12, 'Metaplastic Carcinoma': 6, 'Medullary Carcinoma': 3, 'Infiltrating Carcinoma NOS': 1, 'Leiomyosarcoma (LMS)': 1, 'None': 1}}, 'var_call_Jcm29z9v6SOa5AniQaF5UXf2': 'file_storage/call_Jcm29z9v6SOa5AniQaF5UXf2.json', 'var_call_eOklJkbsBBj4AmECNMI1HqqT': {'n_total_CDH1_records': 318, 'n_unique_patients_with_CDH1': 301, 'sample_patient_barcodes_first20': ['TCGA-05-5428', 'TCGA-06-0210', 'TCGA-06-1800', 'TCGA-06-5416', 'TCGA-13-0807', 'TCGA-13-0889', 'TCGA-19-1386', 'TCGA-21-5787', 'TCGA-22-1016', 'TCGA-2W-A8YY', 'TCGA-2Y-A9H5', 'TCGA-3M-AB47', 'TCGA-42-2590', 'TCGA-4H-AAAK', 'TCGA-50-6590', 'TCGA-55-8614', 'TCGA-55-A4DF', 'TCGA-5L-AAT0', 'TCGA-61-1904', 'TCGA-63-A5MH']}}

exec(code, env_args)
