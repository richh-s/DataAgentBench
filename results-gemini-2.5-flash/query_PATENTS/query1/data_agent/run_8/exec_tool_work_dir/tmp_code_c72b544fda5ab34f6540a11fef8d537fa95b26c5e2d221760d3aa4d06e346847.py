code = """import pandas as pd
import json
import re

# Load the data from the large JSON file
with open(locals()['var_function-call-17167868496260196259'], 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Extract year from 'filing_date'
def extract_year(date_str):
    if isinstance(date_str, str):
        match = re.search(r'\d{4}', date_str)
        if match:
            return int(match.group(0))
    return None

df['filing_year'] = df['filing_date'].apply(extract_year)

# Explode the 'cpc' column
all_cpc_codes = []
for index, row in df.iterrows():
    try:
        cpc_list = json.loads(row['cpc'])
        for cpc_item in cpc_list:
            all_cpc_codes.append({
                'filing_year': row['filing_year'],
                'cpc_code': cpc_item['code']
            })
    except (json.JSONDecodeError, TypeError):
        continue

cpc_df = pd.DataFrame(all_cpc_codes)

# Filter out rows with missing year or cpc_code
cpc_df = cpc_df.dropna(subset=['filing_year', 'cpc_code'])

# Count filings per CPC code and year
yearly_filings = cpc_df.groupby(['cpc_code', 'filing_year']).size().reset_index(name='filings')

# Calculate EMA (smoothing factor 0.2)
alpha = 0.2

def calculate_ema(group):
    group = group.sort_values(by='filing_year')
    group['ema'] = group['filings'].ewm(alpha=alpha, adjust=False).mean()
    return group

ema_filings = yearly_filings.groupby('cpc_code').apply(calculate_ema)

# Find the year with the highest EMA for each CPC code
max_ema_year = ema_filings.loc[ema_filings.groupby('cpc_code')['ema'].idxmax()]

# Filter for CPC codes whose best year is 2022
best_in_2022_cpc = max_ema_year[max_ema_year['filing_year'] == 2022]

# Get unique CPC codes
level_5_cpc_codes_to_check = best_in_2022_cpc['cpc_code'].unique().tolist()

print('__RESULT__:')
print(json.dumps(level_5_cpc_codes_to_check))"""

env_args = {'var_function-call-17167868496260196259': 'file_storage/function-call-17167868496260196259.json'}

exec(code, env_args)
