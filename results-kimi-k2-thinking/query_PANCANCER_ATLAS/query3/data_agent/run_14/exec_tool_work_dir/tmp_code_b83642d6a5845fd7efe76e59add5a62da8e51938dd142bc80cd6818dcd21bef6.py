code = """import json
import pandas as pd

# Load the clinical data
clinical_file = var_functions.query_db:5
if isinstance(clinical_file, str):
    with open(clinical_file, 'r') as f:
        clinical_data = json.load(f)
else:
    clinical_data = clinical_file

# Convert to DataFrame to explore
df = pd.DataFrame(clinical_data)

# Check basic info
print('__RESULT__:')
print(f'Total rows: {len(df)}')
print(f'Columns count: {len(df.columns)}')

# Find cancer type info - check Patient_description for BRCA
if 'Patient_description' in df.columns:
    brca_patients = df[df['Patient_description'].str.contains('BRCA', case=False, na=False)]
    print(f'BRCA patients found: {len(brca_patients)}')
    
    if len(brca_patients) > 0:
        print(f'\nSample BRCA patient descriptions:')
        for i, desc in enumerate(brca_patients['Patient_description'].head(3)):
            print(f'  {i+1}: {desc[:150]}...')

# Check for gender info
for col in df.columns:
    if 'gender' in col.lower():
        print(f'\nGender column: {col}')
        print(f'  Unique values: {df[col].unique()}')
        print(f'  Value counts: {df[col].value_counts().to_dict()}')

# Check histological_type
df['histological_type_short'] = df['histological_type'].str[:100]
print(f'\nHistological types summary:')
print(df['histological_type_short'].value_counts().head(10).to_string())"""

env_args = {'var_functions.list_db:2': ['clinical_info'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
