code = """import pandas as pd
import json

# Load the large JSON data from the file
with open(locals()['var_function-call-12031246827532621766'], 'r') as f:
    data = json.load(f)

# Extract relevant information
cpc_data = []
for record in data:
    filing_date_str = record.get('filing_date')
    if filing_date_str:
        try:
            # Use pandas to_datetime for more robust date parsing
            date_obj = pd.to_datetime(filing_date_str, errors='coerce')
            year = date_obj.year if not pd.isna(date_obj) else None
        except ValueError:
            year = None
    else:
        year = None

    cpc_list_str = record.get('cpc')
    if cpc_list_str:
        try:
            cpc_entries = json.loads(cpc_list_str)
            for entry in cpc_entries:
                cpc_code = entry.get('code')
                if cpc_code and year:
                    # Filter for level 5 CPC codes (heuristic: contains '/' and has at least 6 chars without spaces)
                    if '/' in cpc_code and len(cpc_code.replace(' ', '')) >= 6:
                        cpc_data.append({'cpc_code': cpc_code.replace(' ', ''), 'year': year})
        except json.JSONDecodeError:
            pass

df = pd.DataFrame(cpc_data)

# Count filings per CPC code and year
yearly_filings = df.groupby(['cpc_code', 'year']).size().reset_index(name='filings')

# Calculate EMA for each CPC code using groupby and apply
smoothing_factor = 0.2
ema_df = yearly_filings.sort_values(by=['cpc_code', 'year']).groupby('cpc_code')['filings'].apply(lambda x: x.ewm(alpha=smoothing_factor, adjust=False).mean()).reset_index(name='ema')

# Merge EMA back to yearly_filings to get year information
ema_df = pd.merge(ema_df, yearly_filings, on=['cpc_code', 'level_1'])
ema_df = ema_df.rename(columns={'level_1':'year'})

# Find the best year (highest EMA) for each CPC code
idx = ema_df.groupby('cpc_code')['ema'].idxmax()
best_years_df = ema_df.loc[idx]

# Filter for CPC codes whose best year is 2022
cpc_codes_2022_best = best_years_df[best_years_df['year'] == 2022]['cpc_code'].tolist()

print('__RESULT__:')
print(json.dumps(cpc_codes_2022_best))"""

env_args = {'var_function-call-12031246827532621766': 'file_storage/function-call-12031246827532621766.json'}

exec(code, env_args)
