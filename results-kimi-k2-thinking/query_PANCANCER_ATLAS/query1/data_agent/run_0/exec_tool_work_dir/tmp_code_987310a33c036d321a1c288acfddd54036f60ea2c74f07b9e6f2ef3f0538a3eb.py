code = """import json
import pandas as pd
import math

# First, we need to determine the variable name for the LGG query result
# Based on the error message, it should be var_functions.query_db:82
lgg_data_key = 'var_functions.query_db:82'
lgg_patients = globals()[lgg_data_key]

# If it's a file path string, load it
if isinstance(lgg_patients, str) and '.json' in lgg_patients:
    with open(lgg_patients, 'r') as f:
        lgg_patients = json.load(f)

# Get IGF2 expression data
igf2_expr_key = 'var_functions.query_db:36'
igf2_expression = globals()[igf2_expr_key]

if isinstance(igf2_expression, str) and '.json' in igf2_expression:
    with open(igf2_expression, 'r') as f:
        igf2_expression = json.load(f)

# Create dataframes and process
df_lgg = pd.DataFrame(lgg_patients)
df_igf2 = pd.DataFrame(igf2_expression)

# Extract barcodes
def get_barcode(desc):
    parts = str(desc).split('TCGA-')
    return 'TCGA-' + parts[1].split()[0] if len(parts) > 1 else None

df_lgg['ParticipantBarcode'] = df_lgg['Patient_description'].apply(get_barcode)

# Filter valid histology and barcodes
df_filtered = df_lgg[(~df_lgg['histological_type'].astype(str).str.startswith('[')) & 
                     df_lgg['ParticipantBarcode'].notna()]

# Process expression  
df_igf2['normalized_count'] = pd.to_numeric(df_igf2['normalized_count'], errors='coerce')

# Merge
df_merged = df_filtered.merge(df_igf2[['ParticipantBarcode', 'normalized_count']], 
                              on='ParticipantBarcode', how='inner')

# Calculate log10
df_merged['log10_expr'] = df_merged['normalized_count'].apply(
    lambda x: math.log10(x + 1) if pd.notna(x) and x >= 0 else None
)

# Group by histology
results = df_merged.dropna(subset=['log10_expr']).groupby('histological_type')['log10_expr'].mean().round(4)

print('__RESULT__:')
print(json.dumps(results.to_dict()))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [], 'var_functions.query_db:14': [{'total_count': '10761'}], 'var_functions.query_db:16': [{'ParticipantBarcode': 'TCGA-AB-2908', 'SampleBarcode': 'TCGA-AB-2908-03A', 'AliquotBarcode': 'TCGA-AB-2908-03A-01T-0740-13', 'SampleTypeLetterCode': 'TB', 'SampleType': 'Primary Blood Derived Cancer - Peripheral Blood', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '167.272646747735'}, {'ParticipantBarcode': 'TCGA-19-5960', 'SampleBarcode': 'TCGA-19-5960-01A', 'AliquotBarcode': 'TCGA-19-5960-01A-11R-1850-01', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '185.236'}, {'ParticipantBarcode': 'TCGA-21-1071', 'SampleBarcode': 'TCGA-21-1071-01A', 'AliquotBarcode': 'TCGA-21-1071-01A-01R-0692-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '80.6827'}, {'ParticipantBarcode': 'TCGA-30-1862', 'SampleBarcode': 'TCGA-30-1862-01A', 'AliquotBarcode': 'TCGA-30-1862-01A-02R-1568-13', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '13105.3695494317'}, {'ParticipantBarcode': 'TCGA-66-2795', 'SampleBarcode': 'TCGA-66-2795-01A', 'AliquotBarcode': 'TCGA-66-2795-01A-02R-0980-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '613.474'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:46': {'lgg_count': 39, 'igf2_count': 39}, 'var_functions.list_db:54': ['clinical_info'], 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json', 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json', 'var_functions.query_db:76': 'file_storage/functions.query_db:76.json', 'var_functions.query_db:78': 'file_storage/functions.query_db:78.json', 'var_functions.query_db:82': 'file_storage/functions.query_db:82.json'}

exec(code, env_args)
