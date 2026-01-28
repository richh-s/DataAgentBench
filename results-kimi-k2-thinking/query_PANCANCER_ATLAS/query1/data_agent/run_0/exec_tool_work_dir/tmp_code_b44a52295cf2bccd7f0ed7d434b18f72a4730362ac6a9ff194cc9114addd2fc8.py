code = """import json

# Let's get the LGG patients data from the stored result
print('Checking available variables...')
all_vars = list(globals().keys())
for var in all_vars:
    if 'query_db' in var:
        print(f'Variable: {var}')
        
# Access the most recent query result
lgg_patients = var_functions.query_db:82

print(f'Found {len(lgg_patients)} LGG patients')
print('First patient:', lgg_patients[0] if lgg_patients else 'None')

# Extract barcodes from LGG patients
def extract_barcode(desc):
    desc_str = str(desc)
    if 'TCGA-' in desc_str:
        parts = desc_str.split('TCGA-')
        if len(parts) > 1:
            barcode_part = parts[1].split()[0]
            return 'TCGA-' + barcode_part
    return None

barcodes = []
for patient in lgg_patients:
    desc = patient.get('Patient_description', '')
    barcode = extract_barcode(desc)
    if barcode:
        barcodes.append(barcode)

print(f'Extracted {len(barcodes)} barcodes')
if barcodes:
    print('First few barcodes:', barcodes[:5])

# Create comma-separated list for SQL
barcode_list = "','".join(barcodes)
sql_condition = f"ParticipantBarcode IN ('{barcode_list}')"

print('SQL condition length:', len(sql_condition))
print('__RESULT__:')
print(json.dumps({'barcode_count': len(barcodes), 'sql_condition': sql_condition}))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [], 'var_functions.query_db:14': [{'total_count': '10761'}], 'var_functions.query_db:16': [{'ParticipantBarcode': 'TCGA-AB-2908', 'SampleBarcode': 'TCGA-AB-2908-03A', 'AliquotBarcode': 'TCGA-AB-2908-03A-01T-0740-13', 'SampleTypeLetterCode': 'TB', 'SampleType': 'Primary Blood Derived Cancer - Peripheral Blood', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '167.272646747735'}, {'ParticipantBarcode': 'TCGA-19-5960', 'SampleBarcode': 'TCGA-19-5960-01A', 'AliquotBarcode': 'TCGA-19-5960-01A-11R-1850-01', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '185.236'}, {'ParticipantBarcode': 'TCGA-21-1071', 'SampleBarcode': 'TCGA-21-1071-01A', 'AliquotBarcode': 'TCGA-21-1071-01A-01R-0692-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '80.6827'}, {'ParticipantBarcode': 'TCGA-30-1862', 'SampleBarcode': 'TCGA-30-1862-01A', 'AliquotBarcode': 'TCGA-30-1862-01A-02R-1568-13', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '13105.3695494317'}, {'ParticipantBarcode': 'TCGA-66-2795', 'SampleBarcode': 'TCGA-66-2795-01A', 'AliquotBarcode': 'TCGA-66-2795-01A-02R-0980-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '613.474'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:46': {'lgg_count': 39, 'igf2_count': 39}, 'var_functions.list_db:54': ['clinical_info'], 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json', 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json', 'var_functions.query_db:76': 'file_storage/functions.query_db:76.json', 'var_functions.query_db:78': 'file_storage/functions.query_db:78.json', 'var_functions.query_db:82': 'file_storage/functions.query_db:82.json'}

exec(code, env_args)
