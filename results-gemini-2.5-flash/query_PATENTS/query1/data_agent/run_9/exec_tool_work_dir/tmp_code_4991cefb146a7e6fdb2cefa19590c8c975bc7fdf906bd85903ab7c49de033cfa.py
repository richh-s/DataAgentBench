code = """import pandas as pd
import json
import re

# Load the large JSON data from the file
with open(locals()['var_function-call-12031246827532621766'], 'r') as f:
    data = json.load(f)

processed_records = []

for record in data:
    filing_date_str = record.get('filing_date')
    year = None
    if filing_date_str:
        try:
            date_obj = pd.to_datetime(filing_date_str, errors='coerce')
            year = date_obj.year if not pd.isna(date_obj) else None
        except ValueError:
            pass

    if year is None: # Skip records with invalid or missing year
        continue

    cpc_list_str = record.get('cpc')
    if cpc_list_str:
        try:
            cpc_entries = json.loads(cpc_list_str)
            for entry in cpc_entries:
                cpc_code = entry.get('code')
                if cpc_code:
                    cleaned_code = cpc_code.replace(' ', '')
                    # Regex to identify level 5 or deeper CPC codes
                    if re.match(r'^[A-Z]\d{2}[A-Z]\d{1,3}/\d{2,}', cleaned_code):
                        processed_records.append({'cpc_code': cleaned_code, 'year': year})
        except json.JSONDecodeError:
            pass

df = pd.DataFrame(processed_records)

if df.empty:
    print('__RESULT__:')
    print(json.dumps([]))
else:
    # Group by CPC code and year to count filings
    yearly_filings = df.groupby(['cpc_code', 'year']).size().reset_index(name='filings')

    # Calculate EMA for each CPC code using a more efficient method
    smoothing_factor = 0.2
    yearly_filings['ema'] = yearly_filings.groupby('cpc_code')['filings'].transform(lambda x: x.ewm(alpha=smoothing_factor, adjust=False).mean())

    # Find the best year (highest EMA) for each CPC code
    idx = yearly_filings.groupby('cpc_code')['ema'].idxmax()
    best_years_df = yearly_filings.loc[idx]

    # Filter for CPC codes whose best year is 2022
    cpc_codes_2022_best = best_years_df[best_years_df['year'] == 2022]['cpc_code'].tolist()

    print('__RESULT__:')
    print(json.dumps(cpc_codes_2022_best))"""

env_args = {'var_function-call-12031246827532621766': 'file_storage/function-call-12031246827532621766.json'}

exec(code, env_args)
