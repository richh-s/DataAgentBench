code = """import json
import pandas as pd
import re

# Load the large JSON data from the file
with open(locals()['var_function-call-1961943814564711613'], 'r') as f:
    data = json.load(f)

# Initialize lists to store parsed data
cpc_codes = []
filing_years = []

for record in data:
    cpc_str = record['cpc']
    filing_date_str = record['filing_date']

    # Extract year from filing_date using regex for robustness
    filing_year = None
    if filing_date_str:
        match = re.search(r'\b(19|20)\d{2}\b', filing_date_str) # Matches 4-digit years starting with 19 or 20
        if match:
            filing_year = int(match.group(0))
    
    # Parse CPC codes
    if cpc_str:
        try:
            cpc_entries = json.loads(cpc_str)
            for entry in cpc_entries:
                cpc_codes.append(entry['code'])
                filing_years.append(filing_year)
        except json.JSONDecodeError:
            continue

# Create a DataFrame
df_filings = pd.DataFrame({'cpc_code': cpc_codes, 'filing_year': filing_years})

# Drop rows where filing_year is None and filter for valid years
df_filings.dropna(subset=['filing_year'], inplace=True)
df_filings['filing_year'] = df_filings['filing_year'].astype(int)
df_filings = df_filings[(df_filings['filing_year'] >= 1900) & (df_filings['filing_year'] <= 2023)]

# Get unique CPC codes for the next step
unique_cpc_codes = df_filings['cpc_code'].unique().tolist()

print('__RESULT__:')
print(json.dumps(unique_cpc_codes))"""

env_args = {'var_function-call-17019213161780401760': 'file_storage/function-call-17019213161780401760.json', 'var_function-call-1961943814564711613': 'file_storage/function-call-1961943814564711613.json'}

exec(code, env_args)
