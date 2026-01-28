code = """import json
import re

clin_file = locals()['var_functions.query_db:12']
with open(clin_file) as f:
    clinical_data = json.load(f)

print('Clinical records: ' + str(len(clinical_data)))

# Extract barcodes
bc_hist = []
for item in clinical_data:
    desc = item['Patient_description']
    hist = item['histological_type']
    m = re.search(r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}', desc)
    bc = m.group(0) if m else None
    bc_hist.append([bc, hist])

# Sample
print('First 3:')
for i in range(min(3, len(bc_hist))):
    print(bc_hist[i][0], bc_hist[i][1])

# Count histology types
hist_dict = {}
for entry in bc_hist:
    h = entry[1]
    hist_dict[h] = hist_dict.get(h, 0) + 1

print('Histology counts:')
for k, v in hist_dict.items():
    print(k + ':' + str(v))

result = {'total': len(bc_hist), 'hist_counts': hist_dict}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': [], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:10': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
