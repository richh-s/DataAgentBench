code = """import json
import re

# Query all clinical data
clinical_result = locals()['var_functions.query_db:2']
with open(clinical_result, 'r') as f:
    clinical_data = json.load(f)

print(f'Loaded {len(clinical_data)} clinical records')

# Parse records to extract information
parsed_records = []
for record in clinical_data:
    desc = record.get('Patient_description', '')
    hist_type = record.get('histological_type', '')
    
    # Extract patient barcode
    barcode_match = re.search(r'(TCGA-\d+-\d+)', desc)
    barcode = barcode_match.group(1) if barcode_match else None
    
    # Extract vital status
    vital_status = None
    if 'vital status:' in desc.lower() or 'Vital status:' in desc:
        if 'alive' in desc.lower():
            vital_status = 'Alive'
        elif 'dead' in desc.lower():
            vital_status = 'Dead'
    
    # Check for BRCA/bladder/breast mentions in description or histological type
    is_brca = False
    if any(term in desc.lower() for term in ['brca', 'bladder', 'breast']):
        is_brca = True
    if any(term in hist_type.lower() for term in ['brca', 'bladder', 'breast']):
        is_brca = True
    
    parsed_records.append({
        'barcode': barcode,
        'histological_type': hist_type,
        'vital_status': vital_status,
        'is_brca': is_brca,
        'description': desc
    })

# Filter for BRCA patients who are alive
brca_alive = [r for r in parsed_records if r['is_brca'] and r['vital_status'] == 'Alive' and r['barcode']]

print(f'Found {len(brca_alive)} BRCA patients who are alive')

# Show some examples
for i, patient in enumerate(brca_alive[:3]):
    print(f"  {i+1}. {patient['barcode']} - {patient['histological_type']}")

# Save barcodes for molecular data query
brca_alive_barcodes = [p['barcode'] for p in brca_alive]

print('\nTop histological types among BRCA alive patients:')
from collections import Counter
hist_counts = Counter([p['histological_type'] for p in brca_alive])
for hist, count in hist_counts.most_common(10):
    print(f'  {hist}: {count}')

# Store results
result = {
    'brca_alive_patients': brca_alive,
    'barcodes': brca_alive_barcodes,
    'total_brca_alive': len(brca_alive)
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Patient TCGA-36-1576 (UUID 3445c524-5a37-40b6-8614-956d76eed939) is a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Current vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Record fdd4adb8-9295-480a-9352-305b5eb51187 refers to patient TCGA-25-2408, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.', 'histological_type': 'Serous Cystadenocarcinoma'}], 'var_functions.query_db:14': [], 'var_functions.list_db:16': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:18': []}

exec(code, env_args)
