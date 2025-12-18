code = """import pandas as pd
import json

# Load the full result from the JSON file
with open(locals()['var_function-call-17677642065960427698'], 'r') as f:
    data = json.load(f)

records = []
for entry in data:
    filing_date_str = entry.get('filing_date')
    cpc_data = entry.get('cpc')

    if filing_date_str and cpc_data:
        try:
            # Extract year from filing_date string
            # Assuming filing_date can be parsed to find a 4-digit year
            year_match = pd.to_datetime(filing_date_str, errors='coerce').year
            if pd.isna(year_match):
                # Fallback for complex date strings, try to extract year directly
                import re
                year_match_re = re.search(r'\b(19|20)\d{2}\b', filing_date_str)
                if year_match_re:
                    filing_year = int(year_match_re.group(0))
                else:
                    continue # Skip if year cannot be extracted
            else:
                filing_year = int(year_match)

            # Parse CPC codes
            cpc_list = json.loads(cpc_data)
            for cpc_item in cpc_list:
                cpc_code = cpc_item.get('code')
                if cpc_code:
                    records.append({'cpc_code': cpc_code, 'filing_year': filing_year})
        except (json.JSONDecodeError, AttributeError, TypeError):
            # Handle cases where cpc_data is not valid JSON or other parsing errors
            continue

df = pd.DataFrame(records)

# Count patent filings per CPC code per year
filings_per_year = df.groupby(['cpc_code', 'filing_year']).size().reset_index(name='filings')

# Calculate EMA
smoothing_factor = 0.2
ema_results = []

for cpc_code, group in filings_per_year.groupby('cpc_code'):
    group = group.sort_values(by='filing_year')
    group['ema'] = group['filings'].ewm(alpha=smoothing_factor, adjust=False).mean()
    ema_results.append(group)

ema_df = pd.concat(ema_results)

# Find the year with the highest EMA for each CPC code
best_ema_year = ema_df.loc[ema_df.groupby('cpc_code')['ema'].idxmax()]

# Filter for CPC codes whose best year is 2022
cpc_codes_2022_best = best_ema_year[best_ema_year['filing_year'] == 2022]['cpc_code'].tolist()

print("__RESULT__:")
print(json.dumps(cpc_codes_2022_best))"""

env_args = {'var_function-call-16036621143290588479': ['publicationinfo'], 'var_function-call-17677642065960427698': 'file_storage/function-call-17677642065960427698.json'}

exec(code, env_args)
