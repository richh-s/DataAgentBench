code = """import json
import pandas as pd
import math
import numpy as np

# Load data from the stored query results
lgg_patients = var_functions.query_db_24
igf2_expression = var_functions.query_db_36

# Create DataFrames
df_lgg = pd.DataFrame(lgg_patients)
df_igf2 = pd.DataFrame(igf2_expression)

# Extract ParticipantBarcode from Patient_description
def extract_barcode(desc):
    desc_str = str(desc)
    if 'TCGA-' in desc_str:
        parts = desc_str.split('TCGA-')
        if len(parts) > 1:
            return 'TCGA-' + parts[1].split()[0]
    return None

df_lgg['ParticipantBarcode'] = df_lgg['Patient_description'].apply(extract_barcode)

# Filter LGG patients: exclude histological types in square brackets and missing barcodes
filtered_lgg = df_lgg[
    (~df_lgg['histological_type'].astype(str).str.startswith('[')) &
    (df_lgg['ParticipantBarcode'].notna())
].copy()

# Process IGF2 expression data
df_igf2['normalized_count'] = pd.to_numeric(df_igf2['normalized_count'], errors='coerce')

# Merge LGG patients with IGF2 expression
merged = filtered_lgg.merge(
    df_igf2[['ParticipantBarcode', 'normalized_count']],
    on='ParticipantBarcode',
    how='inner'
)

# Calculate log10(normalized_count + 1)
merged['log10_expression'] = merged['normalized_count'].apply(
    lambda x: math.log10(x + 1) if pd.notna(x) and x >= 0 else np.nan
)

# Filter for valid expression values
final_data = merged[merged['log10_expression'].notna()].copy()

# Group by histology and calculate average log10 expression
results = final_data.groupby('histological_type').agg({
    'log10_expression': ['count', 'mean']
}).round(4)

results.columns = results.columns.droplevel(0)
results = results.reset_index()

# Create output dictionary
result_dict = {}
for _, row in results.iterrows():
    histology = row['histological_type']
    mean_val = row['mean']
    count = int(row['count'])
    if count > 0:
        result_dict[histology] = float(mean_val)

print('__RESULT__:')
print(json.dumps(result_dict))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [], 'var_functions.query_db:14': [{'total_count': '10761'}], 'var_functions.query_db:16': [{'ParticipantBarcode': 'TCGA-AB-2908', 'SampleBarcode': 'TCGA-AB-2908-03A', 'AliquotBarcode': 'TCGA-AB-2908-03A-01T-0740-13', 'SampleTypeLetterCode': 'TB', 'SampleType': 'Primary Blood Derived Cancer - Peripheral Blood', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '167.272646747735'}, {'ParticipantBarcode': 'TCGA-19-5960', 'SampleBarcode': 'TCGA-19-5960-01A', 'AliquotBarcode': 'TCGA-19-5960-01A-11R-1850-01', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '185.236'}, {'ParticipantBarcode': 'TCGA-21-1071', 'SampleBarcode': 'TCGA-21-1071-01A', 'AliquotBarcode': 'TCGA-21-1071-01A-01R-0692-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '80.6827'}, {'ParticipantBarcode': 'TCGA-30-1862', 'SampleBarcode': 'TCGA-30-1862-01A', 'AliquotBarcode': 'TCGA-30-1862-01A-02R-1568-13', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '13105.3695494317'}, {'ParticipantBarcode': 'TCGA-66-2795', 'SampleBarcode': 'TCGA-66-2795-01A', 'AliquotBarcode': 'TCGA-66-2795-01A-02R-0980-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '613.474'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:46': {'lgg_count': 39, 'igf2_count': 39}}

exec(code, env_args)
