code = """import json
import pandas as pd
import math
import numpy as np

# Load LGG patient data
lgg_patients = globals()['var_functions.query_db:24']

# Load IGF2 expression data 
igf2_expression = globals()['var_functions.query_db:36']

# Create DataFrames
df_lgg = pd.DataFrame(lgg_patients)
df_igf2 = pd.DataFrame(igf2_expression)

# Extract ParticipantBarcode from Patient_description
def extract_barcode(desc):
    desc_str = str(desc)
    if 'TCGA-' in desc_str:
        parts = desc_str.split('TCGA-')
        if len(parts) > 1:
            barcode = 'TCGA-' + parts[1].split()[0]
            return barcode
    return None

df_lgg['ParticipantBarcode'] = df_lgg['Patient_description'].apply(extract_barcode)

# Filter LGG patients: exclude histological types in square brackets and missing barcodes
filtered_lgg = df_lgg[
    (~df_lgg['histological_type'].astype(str).str.startswith('[')) &
    (df_lgg['histological_type'].astype(str).str.strip() != '') &
    (df_lgg['ParticipantBarcode'].notna())
].copy()

# Process IGF2 expression data
df_igf2['normalized_count'] = pd.to_numeric(df_igf2['normalized_count'], errors='coerce')

# Merge LGG patients with IGF2 expression (inner join to keep only LGG patients with expression data)
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

# Group by histological type and calculate statistics
results = final_data.groupby('histological_type').agg({
    'log10_expression': ['count', 'mean', 'std']
}).round(6)

# Flatten column names
results.columns = ['_'.join(col).strip() for col in results.columns]
results = results.reset_index()

# Filter for histology types with at least 1 patient
results = results[results['log10_expression_count'] > 0]

print('LGG patients with valid histology:', len(filtered_lgg))
print('With IGF2 expression data:', len(final_data))
print('Histology types found:', len(results))
print()

# Format output for user
output = []
for _, row in results.iterrows():
    histology = row['histological_type']
    mean_val = row['log10_expression_mean']
    count = int(row['log10_expression_count'])
    output.append(f"{histology}: {mean_val:.4f}")
    print(f"{histology}: {mean_val:.4f} (n={count})")

result_dict = dict(zip(results['histological_type'], results['log10_expression_mean'].round(4)))

print('__RESULT__:')
print(json.dumps(result_dict))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [], 'var_functions.query_db:14': [{'total_count': '10761'}], 'var_functions.query_db:16': [{'ParticipantBarcode': 'TCGA-AB-2908', 'SampleBarcode': 'TCGA-AB-2908-03A', 'AliquotBarcode': 'TCGA-AB-2908-03A-01T-0740-13', 'SampleTypeLetterCode': 'TB', 'SampleType': 'Primary Blood Derived Cancer - Peripheral Blood', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '167.272646747735'}, {'ParticipantBarcode': 'TCGA-19-5960', 'SampleBarcode': 'TCGA-19-5960-01A', 'AliquotBarcode': 'TCGA-19-5960-01A-11R-1850-01', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '185.236'}, {'ParticipantBarcode': 'TCGA-21-1071', 'SampleBarcode': 'TCGA-21-1071-01A', 'AliquotBarcode': 'TCGA-21-1071-01A-01R-0692-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '80.6827'}, {'ParticipantBarcode': 'TCGA-30-1862', 'SampleBarcode': 'TCGA-30-1862-01A', 'AliquotBarcode': 'TCGA-30-1862-01A-02R-1568-13', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '13105.3695494317'}, {'ParticipantBarcode': 'TCGA-66-2795', 'SampleBarcode': 'TCGA-66-2795-01A', 'AliquotBarcode': 'TCGA-66-2795-01A-02R-0980-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '613.474'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:46': {'lgg_count': 39, 'igf2_count': 39}}

exec(code, env_args)
