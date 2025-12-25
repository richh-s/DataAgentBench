code = """import pandas as pd
import json
import re

# Read the large JSON file
with open(locals()['var_function-call-6040878569849289475'], 'r') as f:
    data = json.load(f)

# Create a list to store parsed data
parsed_data = []

for record in data:
    cpc_str = record.get('cpc')
    filing_date_str = record.get('filing_date')

    if cpc_str and filing_date_str:
        try:
            # Extract year from filing_date
            year_match = re.search(r'\\d{4}', filing_date_str)
            filing_year = int(year_match.group(0)) if year_match else None

            # Parse CPC codes
            cpc_list = json.loads(cpc_str)
            for cpc_item in cpc_list:
                cpc_code = cpc_item.get('code')
                if cpc_code and filing_year:
                    parsed_data.append({'cpc_code_full': cpc_code, 'filing_year': filing_year})
        except (json.JSONDecodeError, ValueError) as e:
            continue

df_filings = pd.DataFrame(parsed_data)

# Aggregate filings by cpc_code_full and filing_year
filings_count = df_filings.groupby(['cpc_code_full', 'filing_year']).size().reset_index(name='filings')

# Sort by cpc_code_full and filing_year for correct EMA calculation
filings_count = filings_count.sort_values(by=['cpc_code_full', 'filing_year'])

# Calculate EMA using pandas ewm function
smoothing_factor = 0.2
# span = 2 / alpha - 1  (approximately, for alpha=0.2, span=9)
# However, pandas ewm uses alpha directly in its formula, so we can pass alpha directly.
filings_count['ema'] = filings_count.groupby('cpc_code_full')['filings'].transform(lambda x: x.ewm(alpha=smoothing_factor, adjust=False).mean())

# Find the best year for each CPC code based on EMA
# Get the index of the max EMA for each cpc_code_full
idx = filings_count.groupby('cpc_code_full')['ema'].idxmax()
best_year_ema = filings_count.loc[idx]

# Filter for CPC codes whose best year is 2022
cpc_codes_2022_best = best_year_ema[best_year_ema['filing_year'] == 2022]['cpc_code_full'].tolist()

print('__RESULT__:')
print(json.dumps(cpc_codes_2022_best))"""

env_args = {'var_function-call-6040878569849289475': 'file_storage/function-call-6040878569849289475.json'}

exec(code, env_args)
