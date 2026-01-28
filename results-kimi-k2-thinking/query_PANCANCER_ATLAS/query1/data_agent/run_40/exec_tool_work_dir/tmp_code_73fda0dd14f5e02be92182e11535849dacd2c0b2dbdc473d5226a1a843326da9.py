code = """import json
import re

clinical_data_file = var_functions.query_db:12
with open(clinical_data_file) as f:
    clinical_data = json.load(f)

result = {'record_count': len(clinical_data)}

extracted = []
for item in clinical_data:
    desc = item['Patient_description']
    hist = item['histological_type']
    match = re.search('TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}', desc)
    barcode = match.group(0) if match else None
    extracted.append({'barcode': barcode, 'histology': hist})

# Sample
sample = extracted[:5]

# Count histologies
histology_counts = {}
for item in extracted:
    h = item['histology']
    histology_counts[h] = histology_counts.get(h, 0) + 1

result['extracted_count'] = len(extracted)
result['barcodes_with_null'] = sum(1 for x in extracted if x['barcode'] is None)
result['histology_counts'] = histology_counts

result_json = json.dumps(result)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': [], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:10': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
