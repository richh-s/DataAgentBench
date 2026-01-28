code = """import json
import re
import math

# Read the LGG patient data
lgg_file = var_functions.query_db_14
with open(lgg_file, 'r') as f:
    lgg_patients = json.load(f)

print(f"Total LGG patients: {len(lgg_patients)}")

# Extract ParticipantBarcode from Patient_description and filter histology
def extract_barcode(description):
    match = re.search(r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}', description)
    return match.group() if match else None

lgg_data = []
for patient in lgg_patients:
    desc = patient['Patient_description']
    histology = patient['histological_type']
    
    # Skip histology values enclosed in square brackets
    if histology and histology.startswith('[') and histology.endswith(']'):
        continue
    
    barcode = extract_barcode(desc)
    if barcode:
        lgg_data.append({
            'ParticipantBarcode': barcode,
            'histological_type': histology
        })

print(f"LGG patients with valid barcodes and histology: {len(lgg_data)}")
print("Sample records:", lgg_data[:5])

# Count by histology
from collections import Counter
histology_counts = Counter([p['histological_type'] for p in lgg_data])
print("Histology distribution:", dict(histology_counts))

# Save to file for next step
import pandas as pd
df_lgg = pd.DataFrame(lgg_data)
df_lgg.to_json('/tmp/lgg_patients.json', orient='records', indent=2)

print('__RESULT__:')
print(json.dumps({'count': len(lgg_data), 'histologies': list(histology_counts.keys())}))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
