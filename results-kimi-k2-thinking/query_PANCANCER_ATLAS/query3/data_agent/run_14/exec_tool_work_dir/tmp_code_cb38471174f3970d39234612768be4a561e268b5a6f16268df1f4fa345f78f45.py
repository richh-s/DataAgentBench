code = """import json
import pandas as pd

# Access the clinical data - variable name has a colon which needs special handling
clinical_var = globals()['var_functions.query_db:5']

if isinstance(clinical_var, str):
    with open(clinical_var, 'r') as f:
        clinical_data = json.load(f)
else:
    clinical_data = clinical_var

# Convert to DataFrame
df = pd.DataFrame(clinical_data)

print('=== CLINICAL DATA SUMMARY ===')
print(f'Total rows: {len(df)}')
print(f'Columns count: {len(df.columns)}')
print()

# Look for gender information
gender_cols = [col for col in df.columns if 'gender' in col.lower()]
print('Gender-related columns:', gender_cols)

if gender_cols:
    for col in gender_cols:
        print(f'  {col}: {df[col].value_counts().to_dict()}')

# Look for cancer type - check Patient_description column
print()
if 'Patient_description' in df.columns:
    brca_rows = df['Patient_description'].str.contains('BRCA', case=False, na=False)
    brca_count = brca_rows.sum()
    print(f'Patients with BRCA in description: {brca_count}')
    
    # Show some examples
    if brca_count > 0:
        print('Sample BRCA patient descriptions:')
        for i, desc in enumerate(df.loc[brca_rows, 'Patient_description'].head(3)):
            print(f'  {i+1}: {desc[:150]}...')

# Check histological_type
print()
print('Histological type distribution:')
hist_counts = df['histological_type'].value_counts()
print(hist_counts.head(15).to_string())

print()
print('Checking if empty histological types exist:')
empty_hist = df['histological_type'].isnull().sum() + (df['histological_type'] == 'None').sum() + (df['histological_type'] == '').sum()
print(f'Empty or None histological types: {empty_hist}')

# Store for later use
globals()['clinical_df'] = df
print('\nClinical data loaded successfully!')"""

env_args = {'var_functions.list_db:2': ['clinical_info'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
