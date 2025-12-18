code = """import pandas as pd
import json
import re

def parse_year(date_str):
    if isinstance(date_str, str):
        match = re.search(r'\d{4}', date_str)
        if match:
            return int(match.group(0))
    return None


# Load the full result from the JSON file
with open(locals()['var_function-call-17511125532533073924'], 'r') as f:
    publication_data = json.load(f)

# Prepare lists to store flattened data
all_cpc_codes = []
all_filing_years = []

for record in publication_data:
    filing_date_str = record.get('filing_date')
    filing_year = parse_year(filing_date_str)

    if filing_year is not None:
        cpc_str = record.get('cpc')
        if cpc_str:
            try:
                cpc_entries = json.loads(cpc_str)
                for entry in cpc_entries:
                    if "code" in entry:
                        all_cpc_codes.append(entry["code"])
                        all_filing_years.append(filing_year)
            except json.JSONDecodeError:
                # Handle cases where cpc_str is not valid JSON
                pass

df_cpc_filings = pd.DataFrame({'cpc_code': all_cpc_codes, 'filing_year': all_filing_years})

# Extract the first 5 characters of the CPC code for grouping at level 5, then expand it later
df_cpc_filings['cpc_group_level_5'] = df_cpc_filings['cpc_code'].str.slice(0, 5)

# Filter for years 2017-2022
df_cpc_filings = df_cpc_filings[(df_cpc_filings['filing_year'] >= 2017) & (df_cpc_filings['filing_year'] <= 2022)]

# Group by CPC code and filing year to count patents
patent_counts = df_cpc_filings.groupby(['cpc_group_level_5', 'filing_year']).size().reset_index(name='patent_count')

# Sort for EMA calculation
patent_counts = patent_counts.sort_values(by=['cpc_group_level_5', 'filing_year'])

# Calculate Exponential Moving Average (EMA) for each CPC code
alpha = 0.2  # Smoothing factor
def calculate_ema(series, alpha):
    return series.ewm(alpha=alpha, adjust=False).mean()

ema_results = patent_counts.groupby('cpc_group_level_5')['patent_count'].transform(lambda x: calculate_ema(x, alpha))
patent_counts['ema'] = ema_results

# Identify the best year (highest EMA) for each CPC code
idx_max_ema = patent_counts.loc[patent_counts.groupby('cpc_group_level_5')['ema'].idxmax()]

# Filter for CPC codes whose best year is 2022
cpc_best_in_2022 = idx_max_ema[idx_max_ema['filing_year'] == 2022]['cpc_group_level_5'].tolist()

print("__RESULT__:")
print(json.dumps(cpc_best_in_2022))"""

env_args = {'var_function-call-17511125532533073924': 'file_storage/function-call-17511125532533073924.json'}

exec(code, env_args)
