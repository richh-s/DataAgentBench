code = """import pandas as pd
import json

# Access the full result from the file path
with open(locals()['var_function-call-17903615919587865458']['query_db_response']['results']) as f:
    publication_data = json.load(f)

# Create a DataFrame
df = pd.DataFrame(publication_data)

# Extract year from 'filing_date'
df['filing_year'] = df['filing_date'].str.extract(r'(\d{4})')
df['filing_year'] = pd.to_numeric(df['filing_year'], errors='coerce')

# Drop rows where filing_year is NaN
df.dropna(subset=['filing_year'], inplace=True)
df['filing_year'] = df['filing_year'].astype(int)

# Extract CPC codes and flatten the list
all_cpc_codes = []
for index, row in df.iterrows():
    try:
        cpc_list = json.loads(row['cpc'])
        for cpc_item in cpc_list:
            all_cpc_codes.append({'cpc_code': cpc_item['code'], 'filing_year': row['filing_year']})
    except (json.JSONDecodeError, TypeError):
        # Handle cases where 'cpc' might not be a valid JSON string or is None
        continue

cpc_df = pd.DataFrame(all_cpc_codes)

# Get unique CPC codes to query the CPCDefinition_database
unique_cpc_codes = cpc_df['cpc_code'].unique().tolist()

# Filter for CPC codes at level 5
# To do this, I need to query the CPCDefinition_database for level 5 CPC codes.
# This part will be done in the next step by querying the CPCDefinition_database.

# Print a preview of the processed data to ensure it's correct
print('__RESULT__:')
print(cpc_df.head().to_json(orient='records'))"""

env_args = {'var_function-call-17903615919587865458': 'file_storage/function-call-17903615919587865458.json'}

exec(code, env_args)
