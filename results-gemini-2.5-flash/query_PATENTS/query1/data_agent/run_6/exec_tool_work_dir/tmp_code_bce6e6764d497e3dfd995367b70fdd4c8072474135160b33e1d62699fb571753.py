code = """import pandas as pd
import json
import re

# Load the full result from the JSON file
with open(locals()['var_function-call-14622800233827138684'], 'r') as f:
    data = json.load(f)

records = []
for entry in data:
    filing_date_str = entry.get('filing_date')
    cpc_data = entry.get('cpc')

    if filing_date_str and cpc_data:
        # Efficiently extract year using regex
        year_match = re.search(r'\b(19|20)\d{2}\b', filing_date_str)
        if not year_match:
            continue # Skip if year cannot be extracted
        filing_year = int(year_match.group(0))

        try:
            # Parse CPC codes
            cpc_list = json.loads(cpc_data)
            for cpc_item in cpc_list:
                cpc_code = cpc_item.get('code')
                if cpc_code:
                    records.append({'cpc_code': cpc_code, 'filing_year': filing_year})
        except json.JSONDecodeError:
            continue # Skip if cpc_data is not valid JSON

df = pd.DataFrame(records)

# Count patent filings per CPC code per year
filings_per_year = df.groupby(['cpc_code', 'filing_year']).size().reset_index(name='filings')

# Calculate EMA
smoothing_factor = 0.2
ema_results = []

# Process only relevant CPC codes to avoid unnecessary computations
# Sort by cpc_code and filing_year for efficient grouped EMA calculation
filings_per_year = filings_per_year.sort_values(by=['cpc_code', 'filing_year'])

def calculate_ema(group):
    group['ema'] = group['filings'].ewm(alpha=smoothing_factor, adjust=False).mean()
    return group

ema_df = filings_per_year.groupby('cpc_code').apply(calculate_ema)

# Find the year with the highest EMA for each CPC code
best_ema_year = ema_df.loc[ema_df.groupby('cpc_code')['ema'].idxmax()]

# Filter for CPC codes whose best year is 2022
cpc_codes_2022_best = best_ema_year[best_ema_year['filing_year'] == 2022]['cpc_code'].tolist()

print("__RESULT__:")
print(json.dumps(cpc_codes_2022_best))"""

env_args = {'var_function-call-16036621143290588479': ['publicationinfo'], 'var_function-call-17677642065960427698': 'file_storage/function-call-17677642065960427698.json', 'var_function-call-6409921778620027728': ['cpc_definition'], 'var_function-call-14622800233827138684': 'file_storage/function-call-14622800233827138684.json'}

exec(code, env_args)
