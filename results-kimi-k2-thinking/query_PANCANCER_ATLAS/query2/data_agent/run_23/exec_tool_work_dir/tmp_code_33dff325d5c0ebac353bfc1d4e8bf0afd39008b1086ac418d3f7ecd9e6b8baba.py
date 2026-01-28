code = """import json, re

clinical_result = locals()['var_functions.query_db:2']
with open(clinical_result, 'r') as f:
    clinical_data = json.load(f)

print('Total records:', len(clinical_data))

parsed = []
for record in clinical_data:
    desc = record.get('Patient_description', '')
    hist = record.get('histological_type', '')
    
    barcode_match = re.search(r'(TCGA-\d+-\d+)', desc)
    barcode = barcode_match.group(1) if barcode_match else None
    
    vital = None
    desc_lc = desc.lower()
    if 'vital status:' in desc_lc:
        if 'alive' in desc_lc:
            vital = 'Alive'
        elif 'dead' in desc_lc:
            vital = 'Dead'
    
    is_brca = any(term in desc_lc for term in ['brca', 'bladder', 'breast'])
    
    parsed.append({'barcode': barcode, 'hist': hist, 'vital': vital, 'is_brca': is_brca})

brca_alive = [p for p in parsed if p['is_brca'] and p['vital'] == 'Alive' and p['barcode']]
print('BRCA alive patients:', len(brca_alive))

from collections import Counter
hist_counts = Counter([p['hist'] for p in brca_alive if p['hist']])
print('Top histological types:')
for hist, count in hist_counts.most_common(10):
    print(hist, ':', count)

result = {'brca_alive': brca_alive, 'barcodes': [p['barcode'] for p in brca_alive], 'total': len(brca_alive)}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Patient TCGA-36-1576 (UUID 3445c524-5a37-40b6-8614-956d76eed939) is a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Current vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Record fdd4adb8-9295-480a-9352-305b5eb51187 refers to patient TCGA-25-2408, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.', 'histological_type': 'Serous Cystadenocarcinoma'}], 'var_functions.query_db:14': [], 'var_functions.list_db:16': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:18': []}

exec(code, env_args)
