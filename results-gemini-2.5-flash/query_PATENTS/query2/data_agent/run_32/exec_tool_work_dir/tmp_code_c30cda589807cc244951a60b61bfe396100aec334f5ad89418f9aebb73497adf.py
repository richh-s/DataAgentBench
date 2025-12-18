code = """import pandas as pd
import json

# Load data efficiently
with open(locals()['var_function-call-9247441433640274170'], 'r') as f:
    data = json.load(f)
df = pd.DataFrame(data)

# Function to parse natural language dates
def parse_natural_date(date_string):
    if pd.isna(date_string) or not isinstance(date_string, str):
        return pd.NaT
    # Normalize month names and remove ordinal suffixes
    date_string = date_string.replace('January', 'Jan').replace('February', 'Feb').replace('March', 'Mar') \
                             .replace('April', 'Apr').replace('May', 'May').replace('June', 'Jun') \
                             .replace('July', 'Jul').replace('August', 'Aug').replace('September', 'Sep') \
                             .replace('October', 'Oct').replace('November', 'Nov').replace('December', 'Dec') \
                             .replace('st', '').replace('nd', '').replace('rd', '').replace('th', '') \
                             .replace(' of', '').replace('dated ', '')
    try:
        return pd.to_datetime(date_string.strip(), format='%d %b %Y', errors='coerce')
    except ValueError:
        try:
            return pd.to_datetime(date_string.strip(), format='%b %d %Y', errors='coerce')
        except ValueError:
            try:
                return pd.to_datetime(date_string.strip(), format='%Y-%m-%d', errors='coerce')
            except ValueError:
                return pd.NaT

df['grant_date_parsed'] = df['grant_date'].apply(parse_natural_date)
df['filing_date_parsed'] = df['filing_date'].apply(parse_natural_date)

# Filter for patents granted in Germany and in the second half of 2019
germany_patents = df[df['Patents_info'].str.contains('Germany|DE', na=False)].copy()
second_half_2019 = germany_patents[
    (germany_patents['grant_date_parsed'] >= '2019-07-01') &
    (germany_patents['grant_date_parsed'] <= '2019-12-31')
].copy()

# Extract all unique CPC codes and their filing years
cpc_data = []
for _, row in second_half_2019.iterrows():
    try:
        cpc_list = json.loads(row['cpc'])
        filing_year = row['filing_date_parsed'].year
        for cpc_item in cpc_list:
            code = cpc_item.get('code')
            if code:
                cpc_data.append({'symbol': code, 'filing_year': filing_year})
    except (json.JSONDecodeError, AttributeError):
        continue

cpc_codes_df = pd.DataFrame(cpc_data)

# Filter out rows with NaN in 'filing_year' after parsing
cpc_codes_df = cpc_codes_df.dropna(subset=['filing_year'])
cpc_codes_df['filing_year'] = cpc_codes_df['filing_year'].astype(int)

# Group by CPC group and filing year, then count filings
yearly_filings = cpc_codes_df.groupby(['symbol', 'filing_year']).size().reset_index(name='filings')

# Calculate Exponential Moving Average (EMA)
alpha = 0.1
ema_results = []
for cpc_group in yearly_filings['symbol'].unique():
    group_data = yearly_filings[yearly_filings['symbol'] == cpc_group].sort_values(by='filing_year')
    # Ensure there's enough data for EWM; if not, fill with 0 or skip
    if not group_data.empty:
        group_data['ema'] = group_data['filings'].ewm(alpha=alpha, adjust=False).mean()
        ema_results.append(group_data)

ema_df = pd.concat(ema_results)

# Find the best year for each CPC group based on the highest EMA
best_year_per_cpc = ema_df.loc[ema_df.groupby('symbol')['ema'].idxmax()]

# Select relevant columns
result = best_year_per_cpc[['symbol', 'filing_year']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-9247441433640274170': 'file_storage/function-call-9247441433640274170.json'}

exec(code, env_args)
