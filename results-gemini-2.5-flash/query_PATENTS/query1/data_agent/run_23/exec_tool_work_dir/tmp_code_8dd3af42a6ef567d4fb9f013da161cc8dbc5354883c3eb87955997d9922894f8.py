code = """import pandas as pd
import json
import re

data = pd.read_json(locals()['var_function-call-14696505315028543546'])

def parse_year(date_str):
    if isinstance(date_str, str):
        match = re.search(r'\d{4}', date_str)
        if match:
            return int(match.group(0))
    return None

data['filing_year'] = data['filing_date'].apply(parse_year)

all_cpc_codes = []
for index, row in data.iterrows():
    cpc_list_str = row['cpc']
    filing_year = row['filing_year']
    if pd.isna(cpc_list_str) or filing_year is None:
        continue
    try:
        cpc_list = json.loads(cpc_list_str)
        for cpc_item in cpc_list:
            if 'code' in cpc_item:
                all_cpc_codes.append({'cpc_code': cpc_item['code'], 'filing_year': filing_year})
    except json.JSONDecodeError:
        continue

cpc_df = pd.DataFrame(all_cpc_codes)

# Filter for years up to 2022 as the problem asks for best year 2022.
cpc_df = cpc_df[cpc_df['filing_year'] <= 2022]

# Calculate annual filings for each CPC code
annual_filings = cpc_df.groupby(['cpc_code', 'filing_year']).size().reset_index(name='patent_count')

# Prepare for EMA calculation - ensure all years are present for each CPC code
all_years = pd.RangeIndex(min(annual_filings['filing_year']), 2023) # Ensure years up to 2022 are included
all_cpc_codes_unique = annual_filings['cpc_code'].unique()

full_annual_filings = []
for cpc_code in all_cpc_codes_unique:
    for year in all_years:
        count = annual_filings[(annual_filings['cpc_code'] == cpc_code) & (annual_filings['filing_year'] == year)]['patent_count']
        full_annual_filings.append({'cpc_code': cpc_code, 'filing_year': year, 'patent_count': count.iloc[0] if not count.empty else 0})

full_annual_filings_df = pd.DataFrame(full_annual_filings)
full_annual_filings_df = full_annual_filings_df.sort_values(by=['cpc_code', 'filing_year']).reset_index(drop=True)

# Calculate EMA
smoothing_factor = 0.2
full_annual_filings_df['ema'] = full_annual_filings_df.groupby('cpc_code')['patent_count'].transform(lambda x: x.ewm(alpha=smoothing_factor, adjust=False).mean())

# Find the best year for each CPC code
best_year_per_cpc = full_annual_filings_df.loc[full_annual_filings_df.groupby('cpc_code')['ema'].idxmax()]

# Filter for CPC codes whose best year is 2022
cpc_best_in_2022 = best_year_per_cpc[best_year_per_cpc['filing_year'] == 2022]['cpc_code'].tolist()

print("__RESULT__:")
print(json.dumps(cpc_best_in_2022))"""

env_args = {'var_function-call-14696505315028543546': 'file_storage/function-call-14696505315028543546.json'}

exec(code, env_args)
