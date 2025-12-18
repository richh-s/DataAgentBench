code = """import pandas as pd
import json
import re

# Load publication data
with open(locals()['var_function-call-8060160587968561136'], 'r') as f:
    publication_data = json.load(f)
pub_df = pd.DataFrame(publication_data)

# Load level 5 CPC symbols
with open(locals()['var_function-call-9827459070647117279'], 'r') as f:
    cpc_level5_data = json.load(f)
cpc_level5_df = pd.DataFrame(cpc_level5_data)
level5_symbols = set(cpc_level5_df['symbol'].unique())

# Function to extract year from filing_date
def extract_year(date_str):
    if isinstance(date_str, str):
        match = re.search(r'\d{4}', date_str)
        if match:
            return int(match.group(0))
    return None

# Function to extract CPC codes and filter for level 5
def extract_and_filter_cpc_codes(cpc_str, level5_symbols):
    if isinstance(cpc_str, str):
        try:
            cpc_list = json.loads(cpc_str)
            return [cpc['code'] for cpc in cpc_list if 'code' in cpc and cpc['code'] in level5_symbols]
        except json.JSONDecodeError:
            return []
    return []

pub_df['filing_year'] = pub_df['filing_date'].apply(extract_year)
pub_df = pub_df.dropna(subset=['filing_year'])
pub_df['filing_year'] = pub_df['filing_year'].astype(int)

pub_df['cpc_codes'] = pub_df['cpc'].apply(lambda x: extract_and_filter_cpc_codes(x, level5_symbols))
pub_df_exploded = pub_df.explode('cpc_codes')

# Filter out rows where cpc_codes is empty or None after explode
pub_df_exploded = pub_df_exploded[pub_df_exploded['cpc_codes'].apply(lambda x: isinstance(x, str) and len(x) > 0)]

# Group by year and CPC code to count filings
filings_by_year_cpc = pub_df_exploded.groupby(['filing_year', 'cpc_codes']).size().reset_index(name='filings')

# Ensure all years are present for each CPC code for EMA calculation
all_years = range(filings_by_year_cpc['filing_year'].min(), filings_by_year_cpc['filing_year'].max() + 1)
all_cpc_codes = filings_by_year_cpc['cpc_codes'].unique()

# Create a complete DataFrame for all CPCs and all years, filling missing filings with 0
multiindex = pd.MultiIndex.from_product([all_years, all_cpc_codes], names=['filing_year', 'cpc_codes'])
complete_filings = filings_by_year_cpc.set_index(['filing_year', 'cpc_codes']).reindex(multiindex, fill_value=0).reset_index()

# Calculate EMA more efficiently using groupby and apply
smoothing_factor = 0.2
ema_df = complete_filings.groupby('cpc_codes')['filings'].apply(lambda x: x.ewm(alpha=smoothing_factor, adjust=False).mean()).reset_index(name='ema')
ema_df['filing_year'] = complete_filings['filing_year'] # Re-add the filing_year column

# Find the year with the highest EMA for each CPC code
highest_ema_year = ema_df.loc[ema_df.groupby('cpc_codes')['ema'].idxmax()]

# Filter for CPC codes whose best year is 2022
cpc_codes_2022_best = highest_ema_year[highest_ema_year['filing_year'] == 2022]['cpc_codes'].tolist()

print("__RESULT__:")
print(json.dumps(cpc_codes_2022_best))"""

env_args = {'var_function-call-8060160587968561136': 'file_storage/function-call-8060160587968561136.json', 'var_function-call-9827459070647117279': 'file_storage/function-call-9827459070647117279.json'}

exec(code, env_args)
