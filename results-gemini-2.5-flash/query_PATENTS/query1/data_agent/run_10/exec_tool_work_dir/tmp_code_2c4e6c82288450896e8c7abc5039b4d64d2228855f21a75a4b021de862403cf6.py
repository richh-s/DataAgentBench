code = """import json
import pandas as pd
import re

file_path = locals()['var_function-call-5336319047275791554']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Function to extract year from natural language date string
def extract_year(date_str):
    if pd.isna(date_str) or not isinstance(date_str, str):
        return pd.NA
    # Try to find a 4-digit number that looks like a year
    year_match = re.search(r'\b(19|20)\d{2}\b', date_str)
    if year_match:
        return int(year_match.group(0))
    return pd.NA

df['filing_year'] = df['filing_date'].apply(extract_year)
df = df.dropna(subset=['filing_year'])
df['filing_year'] = df['filing_year'].astype(int)

# Extract CPC codes and flatten the list, taking the first 5 characters as level 5 group
all_cpc_group_codes = []
for index, row in df.iterrows():
    try:
        cpc_list = json.loads(row['cpc'])
        for cpc_item in cpc_list:
            code = cpc_item.get('code')
            if code and len(code) >= 5:
                # Take the first 5 characters as the level 5 group code
                cpc_group_level_5 = code[:5]
                all_cpc_group_codes.append({'cpc_group_level_5': cpc_group_level_5, 'filing_year': row['filing_year']})
    except (json.JSONDecodeError, TypeError):
        continue

cpc_group_df = pd.DataFrame(all_cpc_group_codes)

# Count filings per CPC group code and year
yearly_filings = cpc_group_df.groupby(['cpc_group_level_5', 'filing_year']).size().reset_index(name='filings')

# Calculate Exponential Moving Average
smoothing_factor = 0.2

# Ensure all years from 2000 to 2022 are present for EMA calculation if relevant.
# Or, ensure that the years are sorted and fill missing values for a smooth EMA.
min_year = yearly_filings['filing_year'].min() if not yearly_filings.empty else 2000 # default start year if no data
max_year = yearly_filings['filing_year'].max() if not yearly_filings.empty else 2022 # default end year if no data

all_years = range(min_year, max_year + 1)

ema_results = {}
best_year_for_cpc = {}

for cpc_group_code in yearly_filings['cpc_group_level_5'].unique():
    series_data = yearly_filings[yearly_filings['cpc_group_level_5'] == cpc_group_code].set_index('filing_year')['filings']
    
    # Reindex the series to include all years, filling missing values with 0 for EMA calculation
    full_series = series_data.reindex(all_years, fill_value=0)
    
    if not full_series.empty:
        ema = full_series.ewm(alpha=smoothing_factor, adjust=False).mean()
        ema_results[cpc_group_code] = ema
        best_year = ema.idxmax()
        best_year_for_cpc[cpc_group_code] = best_year

# Filter for CPC codes whose best year is 2022
cpc_codes_best_in_2022 = [cpc for cpc, year in best_year_for_cpc.items() if year == 2022]

print("__RESULT__:")
print(json.dumps(cpc_codes_best_in_2022))"""

env_args = {'var_function-call-5336319047275791554': 'file_storage/function-call-5336319047275791554.json'}

exec(code, env_args)
