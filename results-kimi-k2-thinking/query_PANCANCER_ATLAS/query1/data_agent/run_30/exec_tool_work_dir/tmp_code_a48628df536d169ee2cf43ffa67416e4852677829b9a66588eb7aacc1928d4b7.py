code = """import json, math, re, sys, os

with open('file_storage/functions.query_db:14.json') as f:
    lgg_data = json.load(f)
with open('file_storage/functions.query_db:16.json') as f:
    igf2_data = json.load(f)

lgg_patients = []
for item in lgg_data:
    desc = item.get('Patient_description','')
    hist = item.get('histological_type','')
    if hist and not (hist[0]=='[' and hist[-1]==']'):
        m = re.search(r'(TCGA-\w+)', desc)
        if m:
            lgg_patients.append([m.group(1), hist])

igf2_dict = {}
for item in igf2_data:
    bc = item.get('ParticipantBarcode')
    cnt = item.get('normalized_count')
    if bc and cnt:
        try:
            igf2_dict[bc] = float(str(cnt))
        except:
            pass

pairs = []
for p in lgg_patients:
    bc = p[0]
    if bc in igf2_dict:
        cnt = igf2_dict[bc]
        if cnt >= 0:
            log_val = math.log10(cnt + 1)
            pairs.append([p[1], log_val])

groups = {}
for entry in pairs:
    h = entry[0]
    if h not in groups:
        groups[h] = []
    groups[h].append(entry[1])

totals = {}
for h, vals in groups.items():
    avg = sum(vals) / len(vals)
    totals[h] = round(avg, 6)

lines = []
for h in sorted(totals.keys()):
    line = f"{h}: {totals[h]:.4f}"
    lines.append(line)

answer = "|||".join(lines)

result = {'report': answer}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.list_db:2': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'ParticipantBarcode': 'TCGA-AB-2908', 'SampleBarcode': 'TCGA-AB-2908-03A', 'AliquotBarcode': 'TCGA-AB-2908-03A-01T-0740-13', 'SampleTypeLetterCode': 'TB', 'SampleType': 'Primary Blood Derived Cancer - Peripheral Blood', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '167.272646747735'}, {'ParticipantBarcode': 'TCGA-19-5960', 'SampleBarcode': 'TCGA-19-5960-01A', 'AliquotBarcode': 'TCGA-19-5960-01A-11R-1850-01', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '185.236'}, {'ParticipantBarcode': 'TCGA-21-1071', 'SampleBarcode': 'TCGA-21-1071-01A', 'AliquotBarcode': 'TCGA-21-1071-01A-01R-0692-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '80.6827'}, {'ParticipantBarcode': 'TCGA-30-1862', 'SampleBarcode': 'TCGA-30-1862-01A', 'AliquotBarcode': 'TCGA-30-1862-01A-02R-1568-13', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '13105.3695494317'}, {'ParticipantBarcode': 'TCGA-66-2795', 'SampleBarcode': 'TCGA-66-2795-01A', 'AliquotBarcode': 'TCGA-66-2795-01A-02R-0980-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '613.474'}], 'var_functions.query_db:10': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Patient TCGA-36-1576 (UUID 3445c524-5a37-40b6-8614-956d76eed939) is a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Current vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Record fdd4adb8-9295-480a-9352-305b5eb51187 refers to patient TCGA-25-2408, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Record 6f25001a-f890-4fd0-a994-e62a9ea5c6f3 refers to patient TCGA-29-2427, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Case 9446e349-71e6-455a-aa8f-53ec96597146, linked to barcode TCGA-10-0933, corresponds to a FEMALE patient diagnosed with Ovarian serous cystadenocarcinoma, with vital status Dead.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': "Patient TCGA-23-1124, registered under UUID 8a6d2ce3-cc57-451b-9b07-8263782aa23f, belongs to the Ovarian serous cystadenocarcinoma cohort. This FEMALE patient's vital status is Dead.", 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-23-2641 (UUID 49e5ee61-a1c9-4038-84ac-92683e573a65) is recorded as a FEMALE with vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Patient TCGA-23-1118 (FEMALE, UUID 700e91bb-d675-41b2-bbbd-935767c7b447) is enrolled in the study of Ovarian serous cystadenocarcinoma. Vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-23-1120 (UUID fdf83fdf-dfbb-4306-9a1b-b4487d18b402) is recorded as a FEMALE with vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'The individual with barcode TCGA-23-2081 and UUID 41178cbc-db73-4007-b5d8-febebf7f578d is a FEMALE case of Ovarian serous cystadenocarcinoma, documented with vital status = Dead.', 'histological_type': 'Serous Cystadenocarcinoma'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:24': 'file_storage/functions.execute_python:24.json'}

exec(code, env_args)
