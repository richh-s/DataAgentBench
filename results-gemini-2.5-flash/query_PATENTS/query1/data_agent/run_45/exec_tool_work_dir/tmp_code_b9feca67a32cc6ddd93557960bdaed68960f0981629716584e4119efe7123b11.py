code = """import pandas as pd
import json

# Read the full result from the file
with open(locals()['var_function-call-5378456248397069076'], 'r') as f:
    publication_data = json.load(f)

# Create a DataFrame
df_publication = pd.DataFrame(publication_data)

# Extract filing year
def extract_year(date_str):
    if isinstance(date_str, str):
        for fmt in ["%dth %B %Y", "%d %B %Y", "%B %dth, %Y", "%B %d, %Y", "%Y"]:
            try:
                return pd.to_datetime(date_str.replace("dated ", "").replace("the ", ""), format=fmt).year
            except ValueError:
                continue
        # Fallback for years in 'YYYY' format at the end of string or other formats
        import re
        match = re.search(r'\b(\d{4})\b', date_str)
        if match:
            return int(match.group(1))
    return None

df_publication['filing_year'] = df_publication['filing_date'].apply(extract_year)

# Explode CPC codes
df_publication['cpc_codes'] = df_publication['cpc'].apply(lambda x: [d['code'] for d in json.loads(x)] if isinstance(x, str) else [])
df_exploded = df_publication.explode('cpc_codes')

# Filter out rows with no valid filing year or CPC codes
df_filtered = df_exploded.dropna(subset=['filing_year', 'cpc_codes'])

# Count filings per CPC code and year
filings_count = df_filtered.groupby(['cpc_codes', 'filing_year']).size().reset_index(name='patent_filings')

# Calculate EMA
alpha = 0.2
filings_count_sorted = filings_count.sort_values(by=['cpc_codes', 'filing_year'])
ema_results = []

for cpc_code, group in filings_count_sorted.groupby('cpc_codes'):
    group = group.sort_values(by='filing_year')
    group['ema'] = group['patent_filings'].ewm(alpha=alpha, adjust=False).mean()
    ema_results.append(group)

df_ema = pd.concat(ema_results)

# Find the year with the highest EMA for each CPC code
df_max_ema_year = df_ema.loc[df_ema.groupby('cpc_codes')['ema'].idxmax()]

# Filter for CPC codes whose best year is 2022
cpc_codes_2022_best_year = df_max_ema_year[df_max_ema_year['filing_year'] == 2022]['cpc_codes'].tolist()

print('__RESULT__:')
print(json.dumps(cpc_codes_2022_best_year))"""

env_args = {'var_function-call-17556746862476761428': 'file_storage/function-call-17556746862476761428.json', 'var_function-call-5378456248397069076': 'file_storage/function-call-5378456248397069076.json'}

exec(code, env_args)
