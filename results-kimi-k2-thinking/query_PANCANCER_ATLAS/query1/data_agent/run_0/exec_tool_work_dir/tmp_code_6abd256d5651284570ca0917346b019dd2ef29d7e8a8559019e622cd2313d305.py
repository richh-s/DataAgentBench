code = """import json
import pandas as pd
import math

# Access the stored query results using the provided keys
lgg_patients = var_58  # This should be the key for query_db:58
igf2_expression = var_36  # This should be the key for query_db:36

# Create DataFrames
df_lgg = pd.DataFrame(lgg_patients)
df_igf2 = pd.DataFrame(igf2_expression)

# Extract ParticipantBarcode from Patient_description
def extract_barcode(desc):
    desc_str = str(desc)
    if 'TCGA-' in desc_str:
        parts = desc_str.split('TCGA-')
        if len(parts) > 1:
            barcode_part = parts[1].split()[0]
            return 'TCGA-' + barcode_part
    return None

df_lgg['ParticipantBarcode'] = df_lgg['Patient_description'].apply(extract_barcode)

# Filter for valid histology (not in square brackets) and valid barcodes
valid_histology = ~df_lgg['histological_type'].astype(str).str.startswith('[')
valid_barcode = df_lgg['ParticipantBarcode'].notna()
filtered_lgg = df_lgg[valid_histology & valid_barcode].copy()

# Process IGF2 expression data - convert to numeric
df_igf2['normalized_count'] = pd.to_numeric(df_igf2['normalized_count'], errors='coerce')

# Merge LGG patients with IGF2 expression data
merged = filtered_lgg.merge(
    df_igf2[['ParticipantBarcode', 'normalized_count']],
    on='ParticipantBarcode',
    how='inner'
)

# Calculate log10(normalized_count + 1)
merged['log10_expression'] = merged['normalized_count'].apply(
    lambda x: math.log10(x + 1) if pd.notna(x) and x >= 0 else None
)

# Filter for valid log10 values
final_data = merged.dropna(subset=['log10_expression']).copy()

# Group by histological type and calculate mean log10 expression
results = final_data.groupby('histological_type')['log10_expression'].agg([
    'count', 'mean'
]).round(6)

# Create output dictionary with values rounded to 4 decimal places
output_dict = {}
for histology, row in results.iterrows():
    if row['count'] > 0:
        output_dict[histology] = round(float(row['mean']), 4)

print(json.dumps(output_dict, indent=2))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [], 'var_functions.query_db:14': [{'total_count': '10761'}], 'var_functions.query_db:16': [{'ParticipantBarcode': 'TCGA-AB-2908', 'SampleBarcode': 'TCGA-AB-2908-03A', 'AliquotBarcode': 'TCGA-AB-2908-03A-01T-0740-13', 'SampleTypeLetterCode': 'TB', 'SampleType': 'Primary Blood Derived Cancer - Peripheral Blood', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '167.272646747735'}, {'ParticipantBarcode': 'TCGA-19-5960', 'SampleBarcode': 'TCGA-19-5960-01A', 'AliquotBarcode': 'TCGA-19-5960-01A-11R-1850-01', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '185.236'}, {'ParticipantBarcode': 'TCGA-21-1071', 'SampleBarcode': 'TCGA-21-1071-01A', 'AliquotBarcode': 'TCGA-21-1071-01A-01R-0692-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '80.6827'}, {'ParticipantBarcode': 'TCGA-30-1862', 'SampleBarcode': 'TCGA-30-1862-01A', 'AliquotBarcode': 'TCGA-30-1862-01A-02R-1568-13', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '13105.3695494317'}, {'ParticipantBarcode': 'TCGA-66-2795', 'SampleBarcode': 'TCGA-66-2795-01A', 'AliquotBarcode': 'TCGA-66-2795-01A-02R-0980-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '613.474'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:46': {'lgg_count': 39, 'igf2_count': 39}, 'var_functions.list_db:54': ['clinical_info'], 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json'}

exec(code, env_args)
