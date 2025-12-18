code = """import json
import pandas as pd
import numpy as np

lgg_patients = pd.read_json(locals()['var_function-call-17120724368233479518'])
igf2_expression = pd.read_json(locals()['var_function-call-10206940615103676154'])

# Ensure 'normalized_count' is numeric and handle potential errors
igf2_expression['normalized_count'] = pd.to_numeric(igf2_expression['normalized_count'], errors='coerce')

# Merge dataframes
merged_data = pd.merge(lgg_patients, igf2_expression, on='ParticipantBarcode', how='inner')

# Filter out invalid IGF2 expression values (NaNs from coerce or non-positive after adding 1)
merged_data = merged_data.dropna(subset=['normalized_count'])
merged_data = merged_data[merged_data['normalized_count'] >= 0]

# Apply log10 transformation
merged_data['log10_expression'] = np.log10(merged_data['normalized_count'] + 1)

# Group by histology type and compute the average log10-transformed expression
average_expression = merged_data.groupby('histological_type')['log10_expression'].mean().reset_index()

# Format the average values to at least four decimal places
average_expression['average_log10_expression'] = average_expression['log10_expression'].apply(lambda x: f'{x:.4f}')

# Prepare the result for output
result = average_expression[['histological_type', 'average_log10_expression']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-4957086281897016977': ['clinical_info'], 'var_function-call-416097526651329997': 'file_storage/function-call-416097526651329997.json', 'var_function-call-3730502989688273455': [], 'var_function-call-15383304184964350761': 'file_storage/function-call-15383304184964350761.json', 'var_function-call-12761025957224578765': 'file_storage/function-call-12761025957224578765.json', 'var_function-call-17120724368233479518': 'file_storage/function-call-17120724368233479518.json', 'var_function-call-10206940615103676154': 'file_storage/function-call-10206940615103676154.json'}

exec(code, env_args)
