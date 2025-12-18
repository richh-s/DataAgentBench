code = """import pandas as pd
import json
import re
from datetime import datetime

# Load the full data from the JSON file
with open(locals()['var_function-call-4049284340112575991'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Filter for Germany
df_germany = df[df['Patents_info'].str.contains('country_code=DE') | df['Patents_info'].str.contains('in Germany') | df['Patents_info'].str.contains('Germany')]

# Function to parse natural language date strings
def parse_date(date_str):
    if pd.isna(date_str):
        return None
    date_str = date_str.replace("dated", "").replace("the", "").replace(",", "").strip()
    try:
        return datetime.strptime(date_str, "%d %B %Y")
    except ValueError:
        try:
            return datetime.strptime(date_str, "%B %d %Y")
        except ValueError:
            try:
                return datetime.strptime(date_str, "%Y-%m-%d")
            except ValueError:
                # Handle other formats if necessary
                return None

# Apply date parsing
df_germany['grant_date_parsed'] = df_germany['grant_date'].apply(parse_date)
df_germany['filing_date_parsed'] = df_germany['filing_date'].apply(parse_date)

# Filter for patents granted in the second half of 2019
start_date = datetime(2019, 7, 1)
end_date = datetime(2019, 12, 31)
df_filtered = df_germany[(df_germany['grant_date_parsed'] >= start_date) & (df_germany['grant_date_parsed'] <= end_date)].copy()

# Extract CPC codes at level 4 and filing year
cpc_data = []
for index, row in df_filtered.iterrows():
    try:
        cpc_list = json.loads(row['cpc'])
        for cpc_item in cpc_list:
            code = cpc_item['code']
            # Extract CPC group at level 4 (e.g., A61B, A61B1/00, A61B1/000)
            # Level 4 means we keep up to the first 4 characters after the section letter, then optionally the subgroup
            match = re.match(r'([A-Z]\d{2}[A-Z])/?(\d{1,3}/\d{1,6})?.*?', code)
            if match:
                cpc_group = match.group(1)
                subgroup = match.group(2)
                if subgroup:
                    # Keep the subgroup part if it exists
                    cpc_group_level4 = cpc_group + subgroup.split('/')[0]
                else:
                    cpc_group_level4 = cpc_group
                
                if row['filing_date_parsed']:
                    filing_year = row['filing_date_parsed'].year
                    cpc_data.append({'cpc_group_level4': cpc_group_level4, 'filing_year': filing_year})
    except (json.JSONDecodeError, TypeError):
        continue

cpc_df = pd.DataFrame(cpc_data)

# Group by CPC group at level 4 and filing year, then count filings
filings_by_cpc_year = cpc_df.groupby(['cpc_group_level4', 'filing_year']).size().reset_index(name='filing_count')

# Calculate EMA for each CPC group
smoothing_factor = 0.1

def calculate_ema(group):
    group = group.sort_values(by='filing_year')
    ema = []
    if not group.empty:
        ema.append(group['filing_count'].iloc[0]) # Initialize EMA with the first value
        for i in range(1, len(group)):
            ema.append((group['filing_count'].iloc[i] * smoothing_factor) + (ema[-1] * (1 - smoothing_factor)))
    group['ema'] = ema
    return group

ema_results = filings_by_cpc_year.groupby('cpc_group_level4').apply(calculate_ema)

# Find the best year (highest EMA) for each CPC group
best_ema_per_cpc = ema_results.loc[ema_results.groupby('cpc_group_level4')['ema'].idxmax()]

# Prepare result for next step
result = best_ema_per_cpc[['cpc_group_level4', 'filing_year', 'ema']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-4049284340112575991': 'file_storage/function-call-4049284340112575991.json'}

exec(code, env_args)
