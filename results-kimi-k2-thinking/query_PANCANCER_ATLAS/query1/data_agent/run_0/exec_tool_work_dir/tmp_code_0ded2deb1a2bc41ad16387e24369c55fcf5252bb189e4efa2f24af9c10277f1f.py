code = """import json
import pandas as pd

# Load LGG patient data
result_file = './storage/query_result_var_functions.query_db___24.json'
with open(result_file, 'r') as f:
    lgg_patients = json.load(f)

# Create DataFrame and extract barcodes
df_lgg = pd.DataFrame(lgg_patients)

# Extract TCGA barcode from Patient_description
def extract_barcode(description):
    if 'TCGA-' in description:
        parts = description.split('TCGA-')
        if len(parts) > 1:
            barcode_part = 'TCGA-' + parts[1].split()[0]
            return barcode_part
    return None

df_lgg['ParticipantBarcode'] = df_lgg['Patient_description'].apply(extract_barcode)

# Filter out histological types in square brackets
df_filtered = df_lgg[(~df_lgg['histological_type'].str.startswith('[')) & 
                     (df_lgg['histological_type'] != '[Not Applicable]') &
                     (df_lgg['ParticipantBarcode'].notna())]

print('Total LGG patients:', len(df_lgg))
print('After filtering:', len(df_filtered))
print('Histological types found:')
print(df_filtered['histological_type'].value_counts().head())

# Get unique barcodes
lggsm = ','.join([f"'{bc}'" for bc in df_filtered['ParticipantBarcode'].unique()])
print('__RESULT__:')
print(lggsm)"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [], 'var_functions.query_db:14': [{'total_count': '10761'}], 'var_functions.query_db:16': [{'ParticipantBarcode': 'TCGA-AB-2908', 'SampleBarcode': 'TCGA-AB-2908-03A', 'AliquotBarcode': 'TCGA-AB-2908-03A-01T-0740-13', 'SampleTypeLetterCode': 'TB', 'SampleType': 'Primary Blood Derived Cancer - Peripheral Blood', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '167.272646747735'}, {'ParticipantBarcode': 'TCGA-19-5960', 'SampleBarcode': 'TCGA-19-5960-01A', 'AliquotBarcode': 'TCGA-19-5960-01A-11R-1850-01', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '185.236'}, {'ParticipantBarcode': 'TCGA-21-1071', 'SampleBarcode': 'TCGA-21-1071-01A', 'AliquotBarcode': 'TCGA-21-1071-01A-01R-0692-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '80.6827'}, {'ParticipantBarcode': 'TCGA-30-1862', 'SampleBarcode': 'TCGA-30-1862-01A', 'AliquotBarcode': 'TCGA-30-1862-01A-02R-1568-13', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '13105.3695494317'}, {'ParticipantBarcode': 'TCGA-66-2795', 'SampleBarcode': 'TCGA-66-2795-01A', 'AliquotBarcode': 'TCGA-66-2795-01A-02R-0980-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '613.474'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
