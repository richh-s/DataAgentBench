code = """import json
import re

clinical_data_file = var_functions.query_db:12
with open(clinical_data_file, 'r') as f:
    clinical_data = json.load(f)

print('Number of clinical records: ' + str(len(clinical_data)))

def extract_barcode(patient_desc):
    match = re.search(r'TCGA-\w{2}-\w{4}', patient_desc)
    if match:
        return match.group(0)
    return None

clinical_df = []
for record in clinical_data:
    barcode = extract_barcode(record['Patient_description'])
    clinical_df.append({
        'barcode': barcode,
        'histological_type': record['histological_type'],
        'patient_description': record['Patient_description']
    })

print('Sample clinical records with extracted barcodes:')
for i, row in enumerate(clinical_df[:5]):
    print(str(i+1) + '. barcode: ' + str(row['barcode']) + ', histological_type: ' + str(row['histological_type']))

histology_counts = {}
for row in clinical_df:
    hist_type = row['histological_type']
    if hist_type not in histology_counts:
        histology_counts[hist_type] = 0
    histology_counts[hist_type] += 1

print('Histological type counts:')
for hist_type, count in histology_counts.items():
    print(hist_type + ': ' + str(count))

result_dict = {
    'clinical_records_count': len(clinical_data),
    'histology_counts': histology_counts
}

print('__RESULT__:')
print(json.dumps(result_dict))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': [], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:10': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
