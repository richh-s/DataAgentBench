code = """import pandas as pd
import json
import re

# Load the data from the stored file
with open(locals()['var_function-call-9353694163356258651'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Function to extract year from filing_date
def extract_year(date_str):
    if isinstance(date_str, str):
        match = re.search(r'\d{4}', date_str)
        if match:
            return int(match.group(0))
    return None

df['filing_year'] = df['filing_date'].apply(extract_year)

# Function to extract CPC codes
def extract_cpc_codes(cpc_str):
    if isinstance(cpc_str, str):
        try:
            cpc_list = json.loads(cpc_str)
            return [cpc_item['code'] for cpc_item in cpc_list if 'code' in cpc_item]
        except json.JSONDecodeError:
            return []
    return []

df['cpc_codes'] = df['cpc'].apply(extract_cpc_codes)

# Explode the cpc_codes list to have one row per CPC code
df_exploded = df.explode('cpc_codes')

# Filter out rows with no valid CPC codes or filing year
df_filtered = df_exploded.dropna(subset=['cpc_codes', 'filing_year'])

# Select relevant columns
df_final = df_filtered[['cpc_codes', 'filing_year']]

# Rename column for clarity
df_final = df_final.rename(columns={'cpc_codes': 'cpc_symbol'})

# Print the result
print("__RESULT__:")
print(df_final.to_json(orient='records'))"""

env_args = {'var_function-call-9353694163356258651': 'file_storage/function-call-9353694163356258651.json'}

exec(code, env_args)
