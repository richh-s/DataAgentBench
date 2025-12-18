code = """import pandas as pd
import json
from datetime import datetime
import re
from itertools import product

# Load the full result from the file
with open(locals()['var_function-call-637048258622753994'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Parse filing dates and extract year
def parse_year(date_str):
    try:
        # Attempt to parse common date formats
        date_str = date_str.replace("dated ", "").replace("th", "").replace("rd", "").replace("st", "").replace("nd", "").strip()
        for fmt in ["%d %B %Y", "%B %d %Y", "%Y-%m-%d", "%b %d, %Y", "%B the %d, %Y"]:
            try:
                return datetime.strptime(date_str, fmt).year
            except ValueError:
                pass
        # Fallback for year only if parsing full date fails
        year_match = re.search(r"\b(\d{4})\b", date_str)
        if year_match:
            return int(year_match.group(1))
        return None
    except:
        return None

df['filing_year'] = df['filing_date'].apply(parse_year)

# Extract level 5 CPC codes and count filings per CPC per year
cpc_filings = {}
for index, row in df.iterrows():
    if row['filing_year'] is None or pd.isna(row['cpc']):
        continue
    try:
        cpc_list = json.loads(row['cpc'])
        for cpc_entry in cpc_list:
            code = cpc_entry.get('code')
            if code:
                stripped_code = code.strip()
                # Level 5 CPC codes usually have 9 characters after removing the slash (e.g., A01B1/00)
                if len(stripped_code.replace('/', '')) == 9:
                    group_code = stripped_code # Keep the full code for now
                    if group_code not in cpc_filings:
                        cpc_filings[group_code] = {}
                    cpc_filings[group_code][row['filing_year']] = cpc_filings[group_code].get(row['filing_year'], 0) + 1
    except json.JSONDecodeError:
        continue

# Convert to a DataFrame for easier processing
records = []
for cpc_code, year_counts in cpc_filings.items():
    for year, count in year_counts.items():
        records.append({'cpc_code': cpc_code, 'year': year, 'filings': count})
cpc_filings_df = pd.DataFrame(records)

# Ensure all years from 2000 to 2022 are present for each CPC code for EMA calculation
all_years = range(2000, 2023)
unique_cpc_codes = cpc_filings_df['cpc_code'].unique()

# Create a complete set of cpc_code and year combinations
all_combinations = pd.DataFrame(list(product(unique_cpc_codes, all_years)), columns=['cpc_code', 'year'])

# Merge with the actual filings data, filling missing values with 0
full_df = pd.merge(all_combinations, cpc_filings_df, on=['cpc_code', 'year'], how='left').fillna(0)

full_df = full_df.sort_values(by=['cpc_code', 'year']).reset_index(drop=True)

# Calculate EMA
smoothing_factor = 0.2
full_df['ema'] = full_df.groupby('cpc_code')['filings'].transform(lambda x: x.ewm(alpha=smoothing_factor, adjust=False).mean())

# Identify the best year for each CPC code
idx = full_df.groupby(['cpc_code'])['ema'].idxmax()
best_years = full_df.loc[idx][['cpc_code', 'year']]
best_years = best_years[best_years['year'] == 2022]

# Get the level 5 CPC codes whose best year is 2022
result = best_years['cpc_code'].tolist()

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-637048258622753994': 'file_storage/function-call-637048258622753994.json'}

exec(code, env_args)
