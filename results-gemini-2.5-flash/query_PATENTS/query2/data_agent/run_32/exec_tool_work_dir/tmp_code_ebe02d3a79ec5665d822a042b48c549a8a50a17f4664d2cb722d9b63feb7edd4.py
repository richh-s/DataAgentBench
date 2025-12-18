code = """import pandas as pd
import json

# Load data efficiently
with open(locals()['var_function-call-9247441433640274170'], 'r') as f:
    data = json.load(f)
df = pd.DataFrame(data)

# Convert date columns to datetime objects, coercing errors
df['grant_date_parsed'] = pd.to_datetime(df['grant_date'].str.replace('st|'nd|'rd|'th', '', regex=True).str.replace('of ', '', regex=False).str.replace('dated ', '', regex=False), errors='coerce')
df['filing_date_parsed'] = pd.to_datetime(df['filing_date'].str.replace('st|'nd|'rd|'th', '', regex=True).str.replace('of ', '', regex=False).str.replace('dated ', '', regex=False), errors='coerce')

# Filter for patents granted in Germany and in the second half of 2019
germany_patents_2019 = df[
    df['Patents_info'].str.contains('Germany|DE', na=False) &
    (df['grant_date_parsed'] >= '2019-07-01') &
    (df['grant_date_parsed'] <= '2019-12-31')
].copy()

# Extract CPC codes at level 4 and filing year
cpc_filings = []
for _, row in germany_patents_2019.iterrows():
    try:
        cpc_list = json.loads(row['cpc'])
        filing_year = row['filing_date_parsed'].year
        for cpc_item in cpc_list:
            code = cpc_item.get('code')
            if code:
                # Extract CPC group at level 4 (first 7 characters for most cases, or full code if shorter)
                cpc_group_level_4 = code[:7] if len(code) >= 7 else code
                cpc_filings.append({'cpc_group': cpc_group_level_4, 'filing_year': filing_year})
    except (json.JSONDecodeError, AttributeError):
        continue

cpc_filings_df = pd.DataFrame(cpc_filings)
cpc_filings_df = cpc_filings_df.dropna(subset=['filing_year'])
cpc_filings_df['filing_year'] = cpc_filings_df['filing_year'].astype(int)

# Group by CPC group and filing year, then count filings
yearly_filings = cpc_filings_df.groupby(['cpc_group', 'filing_year']).size().reset_index(name='filings')

# Calculate Exponential Moving Average (EMA)
alpha = 0.1
ema_results = []
for cpc_group in yearly_filings['cpc_group'].unique():
    group_data = yearly_filings[yearly_filings['cpc_group'] == cpc_group].sort_values(by='filing_year')
    if not group_data.empty:
        group_data['ema'] = group_data['filings'].ewm(alpha=alpha, adjust=False).mean()
        ema_results.append(group_data)

ema_df = pd.concat(ema_results)

# Find the best year for each CPC group based on the highest EMA
best_year_per_cpc = ema_df.loc[ema_df.groupby('cpc_group')['ema'].idxmax()]

# Select relevant columns and prepare for output
result = best_year_per_cpc[['cpc_group', 'filing_year']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-9247441433640274170': 'file_storage/function-call-9247441433640274170.json'}

exec(code, env_args)
