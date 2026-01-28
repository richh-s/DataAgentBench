code = """import json
import pandas as pd
import math

# Load the data
lgg_patients_file = './storage/query_result_var_functions.query_db___24.json'
with open(lgg_patients_file, 'r') as f:
    lgg_patients = json.load(f)

igf2_file = './storage/query_result_var_functions.query_db___36.json'
with open(igf2_file, 'r') as f:
    igf2_expression = json.load(f)

# Create DataFrames
df_lgg = pd.DataFrame(lgg_patients)
df_igf2 = pd.DataFrame(igf2_expression)

# Extract TCGA barcode from Patient_description
def extract_barcode(description):
    if 'TCGA-' in str(description):
        parts = str(description).split('TCGA-')
        if len(parts) > 1:
            barcode_part = 'TCGA-' + parts[1].split()[0]
            return barcode_part
    return None

# Extract barcodes and filter LGG patients
df_lgg['ParticipantBarcode'] = df_lgg['Patient_description'].apply(extract_barcode)

# Filter: exclude histological types in square brackets and missing barcodes
df_lgg_filtered = df_lgg[
    (~df_lgg['histological_type'].astype(str).str.startswith('[')) & 
    (df_lgg['histological_type'].astype(str) != '[Not Applicable]') &
    (df_lgg['ParticipantBarcode'].notna())
].copy()

print('LGG patients found:', len(df_lgg))
print('After filtering histology:', len(df_lgg_filtered))
print('\nHistological types:')
print(df_lgg_filtered['histological_type'].value_counts())

# Convert IGF2 expression to numeric
df_igf2['normalized_count'] = pd.to_numeric(df_igf2['normalized_count'], errors='coerce')

# Merge LGG patients with IGF2 expression
df_merged = df_lgg_filtered.merge(
    df_igf2[['ParticipantBarcode', 'normalized_count']], 
    on='ParticipantBarcode', 
    how='inner'
)

print('\nAfter merging with IGF2 expression:')
print('Total with expression data:', len(df_merged))

# Calculate log10 expression
df_merged['log10_expression'] = df_merged['normalized_count'].apply(
    lambda x: math.log10(x + 1) if pd.notna(x) and x >= 0 else None
)

# Filter for valid expression values
df_final = df_merged[df_merged['log10_expression'].notna()].copy()

print('With valid log10 expression:', len(df_final))

# Group by histology and calculate average log10 expression
results = df_final.groupby('histological_type')['log10_expression'].agg([
    'count', 'mean'
]).round(6)

print('\nRESULTS:')
for histology, row in results.iterrows():
    if row['count'] > 0:
        print(f"{histology}: {row['mean']:.4f} (n={int(row['count'])})")

# Also return as a dictionary
result_dict = {}
for histology, row in results.iterrows():
    if row['count'] > 0:
        result_dict[histology] = round(row['mean'], 4)

print('__RESULT__:')
print(json.dumps(result_dict, indent=2))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [], 'var_functions.query_db:14': [{'total_count': '10761'}], 'var_functions.query_db:16': [{'ParticipantBarcode': 'TCGA-AB-2908', 'SampleBarcode': 'TCGA-AB-2908-03A', 'AliquotBarcode': 'TCGA-AB-2908-03A-01T-0740-13', 'SampleTypeLetterCode': 'TB', 'SampleType': 'Primary Blood Derived Cancer - Peripheral Blood', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '167.272646747735'}, {'ParticipantBarcode': 'TCGA-19-5960', 'SampleBarcode': 'TCGA-19-5960-01A', 'AliquotBarcode': 'TCGA-19-5960-01A-11R-1850-01', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '185.236'}, {'ParticipantBarcode': 'TCGA-21-1071', 'SampleBarcode': 'TCGA-21-1071-01A', 'AliquotBarcode': 'TCGA-21-1071-01A-01R-0692-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '80.6827'}, {'ParticipantBarcode': 'TCGA-30-1862', 'SampleBarcode': 'TCGA-30-1862-01A', 'AliquotBarcode': 'TCGA-30-1862-01A-02R-1568-13', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '13105.3695494317'}, {'ParticipantBarcode': 'TCGA-66-2795', 'SampleBarcode': 'TCGA-66-2795-01A', 'AliquotBarcode': 'TCGA-66-2795-01A-02R-0980-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '613.474'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
