code = """import pandas as pd
import json
import re
from collections import defaultdict

# Load the data from the large JSON file
with open(locals()['var_function-call-17167868496260196259'], 'r') as f:
    data = json.load(f)

yearly_cpc_filings = defaultdict(lambda: defaultdict(int))

for row in data:
    filing_date_str = row.get('filing_date')
    cpc_str = row.get('cpc')

    if not filing_date_str or not cpc_str:
        continue

    # Extract year from 'filing_date'
    match = re.search(r'\\d{4}', filing_date_str)
    if not match:
        continue
    filing_year = int(match.group(0))

    # Filter years to only include up to 2022 for EMA calculation
    if filing_year > 2022:
        continue

    try:
        cpc_list = json.loads(cpc_str)
        for cpc_item in cpc_list:
            cpc_code = cpc_item.get('code')
            if cpc_code:
                yearly_cpc_filings[cpc_code][filing_year] += 1
    except (json.JSONDecodeError, TypeError):
        continue

# Convert the nested dictionary to a list of records for DataFrame
records = []
for cpc_code, years_data in yearly_cpc_filings.items():
    for year, filings in years_data.items():
        records.append({'cpc_code': cpc_code, 'filing_year': year, 'filings': filings})

yearly_filings_df = pd.DataFrame(records)

if yearly_filings_df.empty:
    print('__RESULT__:')
    print(json.dumps([]))
    exit()

# Sort for EMA calculation
yearly_filings_df = yearly_filings_df.sort_values(by=['cpc_code', 'filing_year'])

# Calculate EMA (smoothing factor 0.2)
alpha = 0.2

def calculate_ema_for_group(group):
    group['ema'] = group['filings'].ewm(alpha=alpha, adjust=False).mean()
    return group

ema_filings = yearly_filings_df.groupby('cpc_code', group_keys=False).apply(calculate_ema_for_group)

# Find the year with the highest EMA for each CPC code
# Use idxmax for efficiency, it returns the index of the first occurrence of the maximum value
idx_max_ema = ema_filings.groupby('cpc_code')['ema'].idxmax()
max_ema_year = ema_filings.loc[idx_max_ema]

# Filter for CPC codes whose best year is 2022
best_in_2022_cpc_candidates = max_ema_year[max_ema_year['filing_year'] == 2022]

# Get unique CPC codes
level_5_cpc_codes_to_check = best_in_2022_cpc_candidates['cpc_code'].unique().tolist()

print('__RESULT__:')
print(json.dumps(level_5_cpc_codes_to_check))"""

env_args = {'var_function-call-17167868496260196259': 'file_storage/function-call-17167868496260196259.json'}

exec(code, env_args)
