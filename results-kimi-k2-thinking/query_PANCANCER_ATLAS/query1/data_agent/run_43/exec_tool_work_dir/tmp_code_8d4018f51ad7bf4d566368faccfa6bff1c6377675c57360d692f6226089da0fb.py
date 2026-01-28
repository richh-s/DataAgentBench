code = """import json
import re
import math
from collections import defaultdict

# Load LGG patient data
lgg_file = locals()['var_functions.query_db:34']
with open(lgg_file, 'r') as f:
    lgg_data = json.load(f)

# Build patient map
patient_map = {}
for record in lgg_data:
    hist_type = record['histological_type']
    if '[' in hist_type or ']' in hist_type:
        continue
    
    patient_desc = record['Patient_description']
    match = re.search(r'(TCGA-\w+-\w+)', patient_desc)
    if match:
        barcode = match.group(1)
        patient_map[barcode] = hist_type

# Load IGF2 expression data
igf2_file = locals()['var_functions.query_db:56']
igf2_data = igf2_file  # This is already a list

print("Loaded {} IGF2 expression records for {} patients".format(len(igf2_data), len(set([rec['ParticipantBarcode'] for rec in igf2_data]))))
print("Sample data:", igf2_data[:3])

# Build a more comprehensive query for IGF2 data for all LGG patients
lgg_barcodes = list(patient_map.keys())
print("Total LGG patients to query: {}".format(len(lgg_barcodes)))
print("Sample barcodes:", lgg_barcodes[:10])

print('__RESULT__:')
print(json.dumps({
    'lgg_patient_count': len(patient_map),
    'sample_barcodes': lgg_barcodes[:5],
    'igf2_records_found': len(igf2_data)
}))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'histological_type': 'Astrocytoma'}, {'histological_type': 'Glioblastoma Multiforme (GBM)'}, {'histological_type': 'Oligoastrocytoma'}, {'histological_type': 'Oligodendroglioma'}, {'histological_type': 'Paraganglioma'}, {'histological_type': 'Paraganglioma; Extra-adrenal Pheochromocytoma'}, {'histological_type': 'Treated primary GBM'}, {'histological_type': 'Untreated primary (de novo) GBM'}], 'var_functions.list_db:6': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': [{'ParticipantBarcode': 'TCGA-AB-2908', 'SampleBarcode': 'TCGA-AB-2908-03A', 'Symbol': 'IGF2', 'normalized_count': '167.272646747735'}, {'ParticipantBarcode': 'TCGA-19-5960', 'SampleBarcode': 'TCGA-19-5960-01A', 'Symbol': 'IGF2', 'normalized_count': '185.236'}, {'ParticipantBarcode': 'TCGA-21-1071', 'SampleBarcode': 'TCGA-21-1071-01A', 'Symbol': 'IGF2', 'normalized_count': '80.6827'}, {'ParticipantBarcode': 'TCGA-30-1862', 'SampleBarcode': 'TCGA-30-1862-01A', 'Symbol': 'IGF2', 'normalized_count': '13105.3695494317'}, {'ParticipantBarcode': 'TCGA-66-2795', 'SampleBarcode': 'TCGA-66-2795-01A', 'Symbol': 'IGF2', 'normalized_count': '613.474'}, {'ParticipantBarcode': 'TCGA-A8-A082', 'SampleBarcode': 'TCGA-A8-A082-01A', 'Symbol': 'IGF2', 'normalized_count': '630.54'}, {'ParticipantBarcode': 'TCGA-B5-A3FA', 'SampleBarcode': 'TCGA-B5-A3FA-01A', 'Symbol': 'IGF2', 'normalized_count': '423.628'}, {'ParticipantBarcode': 'TCGA-BH-A1EX', 'SampleBarcode': 'TCGA-BH-A1EX-01A', 'Symbol': 'IGF2', 'normalized_count': '1151.13'}, {'ParticipantBarcode': 'TCGA-BT-A20O', 'SampleBarcode': 'TCGA-BT-A20O-01A', 'Symbol': 'IGF2', 'normalized_count': '369.106'}, {'ParticipantBarcode': 'TCGA-CD-5799', 'SampleBarcode': 'TCGA-CD-5799-01A', 'Symbol': 'IGF2', 'normalized_count': '3936.02070028943'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': {'status': 'checked variables'}, 'var_functions.execute_python:32': {'status': 'ready for next step', 'message': 'Need to query data in smaller chunks'}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:38': {'records_sample': 2, 'status': 'proceeding to query molecular data'}, 'var_functions.execute_python:40': {'step': 'ready_to_query_clinical_data_for_LGG_patients'}, 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.execute_python:46': {'type': "<class 'list'>", 'length': 513}, 'var_functions.execute_python:54': {'total_patients': 513, 'skipped_patients': 0, 'histology_types': ['Oligodendroglioma', 'Oligoastrocytoma', 'Astrocytoma'], 'groups': {'Oligodendroglioma': 189, 'Oligoastrocytoma': 130, 'Astrocytoma': 194}}, 'var_functions.query_db:56': [{'ParticipantBarcode': 'TCGA-DH-A7US', 'Symbol': 'IGF2', 'normalized_count': '418.886'}]}

exec(code, env_args)
