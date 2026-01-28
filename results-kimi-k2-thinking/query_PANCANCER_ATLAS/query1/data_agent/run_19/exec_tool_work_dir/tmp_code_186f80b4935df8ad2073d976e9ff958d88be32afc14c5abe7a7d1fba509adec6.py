code = """import json

# Get the list of LGG patient barcodes from our clinical data
clinical_data = locals()['var_functions.query_db:8']

if isinstance(clinical_data, str) and 'json' in clinical_data:
    with open(clinical_data, 'r') as f:
        lgg_clinical = json.load(f)
else:
    lgg_clinical = clinical_data

# Extract full barcodes (not just prefixes)
import re
lgg_barcodes = set()
for record in lgg_clinical:
    desc = record['Patient_description']
    match = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]+)', desc)
    if match:
        barcode = match.group(1)
        lgg_barcodes.add(barcode)

print('__RESULT__:')
print(json.dumps({
    'total_lgg_patients': len(lgg_barcodes),
    'sample_barcodes': list(lgg_barcodes)[:10]
}))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.execute_python:14': {'total_records': 513, 'unique_patients': 513, 'histology_counts': {'Oligodendroglioma': 189, 'Oligoastrocytoma': 130, 'Astrocytoma': 194}, 'sample_patients': [{'ParticipantBarcode': 'TCGA-RY-A83X', 'histological_type': 'Oligodendroglioma'}, {'ParticipantBarcode': 'TCGA-FG-A60K', 'histological_type': 'Oligoastrocytoma'}, {'ParticipantBarcode': 'TCGA-DB-A4XH', 'histological_type': 'Oligoastrocytoma'}, {'ParticipantBarcode': 'TCGA-DB-A4XE', 'histological_type': 'Oligoastrocytoma'}, {'ParticipantBarcode': 'TCGA-DB-A4XC', 'histological_type': 'Oligoastrocytoma'}, {'ParticipantBarcode': 'TCGA-P5-A5F0', 'histological_type': 'Oligodendroglioma'}, {'ParticipantBarcode': 'TCGA-S9-A6U1', 'histological_type': 'Astrocytoma'}, {'ParticipantBarcode': 'TCGA-TM-A7C3', 'histological_type': 'Astrocytoma'}, {'ParticipantBarcode': 'TCGA-S9-A7R2', 'histological_type': 'Astrocytoma'}, {'ParticipantBarcode': 'TCGA-TM-A84R', 'histological_type': 'Oligodendroglioma'}]}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'histology_averages': {'Astrocytoma': {'average_log10_expr': 2.5713, 'sample_count': 10}, 'Oligoastrocytoma': {'average_log10_expr': 2.7136, 'sample_count': 5}, 'Oligodendroglioma': {'average_log10_expr': 2.6825, 'sample_count': 8}}, 'total_patients_with_data': 23, 'total_unique_histologies': 3}}

exec(code, env_args)
