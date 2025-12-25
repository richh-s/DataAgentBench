code = """import pandas as pd
import json

# Load the full result from the file
with open(locals()['var_function-call-2018874257286241520'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Extract year from 'filing_date'
def extract_year(date_string):
    try:
        # Assuming date_string is like "March 15th, 2020" or "dated 5th March 2019"
        # We need to find the 4-digit year in the string
        import re
        match = re.search(r'\b(\d{4})\b', date_string)
        if match:
            return int(match.group(1))
    except:
        pass
    return None

df['filing_year'] = df['filing_date'].apply(extract_year)

# Filter out rows where filing_year is None
df = df.dropna(subset=['filing_year'])

# Parse 'cpc' JSON string and explode into separate rows
all_cpc_filings = []
for index, row in df.iterrows():
    try:
        cpc_list = json.loads(row['cpc'])
        for cpc_item in cpc_list:
            all_cpc_filings.append({'cpc_code': cpc_item['code'], 'filing_year': int(row['filing_year'])})
    except (json.JSONDecodeError, TypeError):
        continue

cpc_filings_df = pd.DataFrame(all_cpc_filings)

# Filter for years up to 2022 (inclusive)
cpc_filings_df = cpc_filings_df[cpc_filings_df['filing_year'] <= 2022]

# Group by cpc_code and filing_year to count patents
patent_counts = cpc_filings_df.groupby(['cpc_code', 'filing_year']).size().reset_index(name='patent_count')

print('__RESULT__:')
print(patent_counts.to_json(orient='records'))"""

env_args = {'var_function-call-2018874257286241520': 'file_storage/function-call-2018874257286241520.json'}

exec(code, env_args)
