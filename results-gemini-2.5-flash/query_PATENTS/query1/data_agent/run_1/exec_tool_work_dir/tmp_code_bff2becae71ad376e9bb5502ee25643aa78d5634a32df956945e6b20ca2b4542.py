code = """import json
import pandas as pd
import re

# Load the full result from the file
with open(locals()['var_function-call-12637477994751349657'], 'r') as f:
    records = json.load(f)

all_cpc_data = []

for record in records:
    cpc_codes_str = record.get('cpc')
    filing_date_str = record.get('filing_date')

    filing_year = None
    if filing_date_str:
        year_match = re.search(r'\b(19|20)\d{2}\b', filing_date_str)
        if year_match:
            filing_year = int(year_match.group(0))

    if cpc_codes_str and filing_year:
        try:
            cpc_entries = json.loads(cpc_codes_str)
            for entry in cpc_entries:
                code = entry.get('code')
                if code:
                    all_cpc_data.append({'cpc_code': code, 'filing_year': filing_year})
        except json.JSONDecodeError:
            pass

df_cpc = pd.DataFrame(all_cpc_data)

# Check if df_cpc is empty. If it is, no further processing is needed.
if df_cpc.empty:
    print("__RESULT__:")
    print(json.dumps([]))
else:
    # Count patent filings per CPC code per year
    cpc_counts_per_year = df_cpc.groupby(['cpc_code', 'filing_year']).size().reset_index(name='patent_count')

    # Create a DataFrame with all possible CPC codes and years up to 2022
    all_years = range(df_cpc['filing_year'].min(), 2023)
    all_cpc_codes = df_cpc['cpc_code'].unique()

    # Create a MultiIndex for all combinations of CPC codes and years
    idx = pd.MultiIndex.from_product([all_cpc_codes, all_years], names=['cpc_code', 'filing_year'])
    full_cpc_counts = cpc_counts_per_year.set_index(['cpc_code', 'filing_year']).reindex(idx, fill_value=0).reset_index()

    # Sort by cpc_code and filing_year for correct EMA calculation
    full_cpc_counts = full_cpc_counts.sort_values(by=['cpc_code', 'filing_year'])

    alpha = 0.2
    # Calculate EMA grouped by cpc_code
    full_cpc_counts['ema'] = full_cpc_counts.groupby('cpc_code')['patent_count'].transform(lambda x: x.ewm(alpha=alpha, adjust=False).mean())

    # Filter for years up to 2022 for the best year calculation
    ema_up_to_2022 = full_cpc_counts[full_cpc_counts['filing_year'] <= 2022]

    # Find the year with the highest EMA for each CPC code
    idx_max_ema = ema_up_to_2022.groupby('cpc_code')['ema'].idxmax()
    best_year_for_cpc = ema_up_to_2022.loc[idx_max_ema]

    # Filter for CPC codes whose best year is 2022
    cpc_codes_best_in_2022 = best_year_for_cpc[best_year_for_cpc['filing_year'] == 2022]['cpc_code'].tolist()

    print("__RESULT__:")
    print(json.dumps(cpc_codes_best_in_2022))"""

env_args = {'var_function-call-12637477994751349657': 'file_storage/function-call-12637477994751349657.json'}

exec(code, env_args)
