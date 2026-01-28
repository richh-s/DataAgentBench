code = """import json
import re

# Load clinical data
clinical_file = var_functions.query_db:12
with open(clinical_file, 'r') as f:
    clinical_list = json.load(f)

print('Clinical records count:', len(clinical_list))

# Extract barcode from description
def get_barcode(desc):
    match = re.search(r'TCGA-\w{2}-\w{4}', desc)
    return match.group(0) if match else None

# Process clinical data
processed = []
for rec in clinical_list:
    barcode = get_barcode(rec['Patient_description'])
    processed.append({
        'barcode': barcode,
        'histology': rec['histological_type'],
        'desc': rec['Patient_description']
    })

print('First 5 records:')
for i, item in enumerate(processed[:5]):
    print(i+1, item['barcode'], item['histology'])

# Count histologies
hist_counts = {}
for item in processed:
    h = item['histology']
    hist_counts[h] = hist_counts.get(h, 0) + 1

print('Histology counts:')
for h, c in hist_counts.items():
    print(h, c)

result = {'count': len(processed), 'hist_counts': hist_counts}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': [], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:10': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
