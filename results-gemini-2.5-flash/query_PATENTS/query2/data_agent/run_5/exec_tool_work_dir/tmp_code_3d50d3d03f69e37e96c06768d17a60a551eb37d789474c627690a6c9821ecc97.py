code = """import pandas as pd
import json

def parse_date_optimized(date_str):
    if not isinstance(date_str, str):
        return pd.NaT
    # Attempt to parse common formats
    try:
        return pd.to_datetime(date_str, format='%dth %B %Y', errors='coerce')
    except ValueError:
        pass
    try:
        return pd.to_datetime(date_str, format='%B %dth, %Y', errors='coerce')
    except ValueError:
        pass
    try:
        return pd.to_datetime(date_str, format='dated %dth %B %Y', errors='coerce')
    except ValueError:
        pass
    try:
        return pd.to_datetime(date_str, format='%d %B %Y', errors='coerce')
    except ValueError:
        pass
    try:
        return pd.to_datetime(date_str, format='dated %d %B %Y', errors='coerce')
    except ValueError:
        pass
    # Fallback to general parser if specific formats fail
    return pd.to_datetime(date_str, errors='coerce')


def extract_country_code_optimized(patent_info):
    if isinstance(patent_info, str) and "German patent" in patent_info:
        return "DE"
    return None

# Load the JSON data from the file
with open(locals()['var_function-call-18001159190617317211'], 'r') as f:
    raw_data = json.load(f)

df = pd.DataFrame(raw_data)

df['grant_date_parsed'] = df['grant_date'].apply(parse_date_optimized)
df['filing_date_parsed'] = df['filing_date'].apply(parse_date_optimized)
df['country_code'] = df['Patents_info'].apply(extract_country_code_optimized)

# Filter for patents granted in the second half of 2019 in Germany
start_date = pd.to_datetime('2019-07-01')
end_date = pd.to_datetime('2019-12-31')

filtered_df = df[(df['grant_date_parsed'] >= start_date) &
                 (df['grant_date_parsed'] <= end_date) &
                 (df['country_code'] == 'DE')].copy()

# Extract CPC level 4 codes and filing year
cpc_data = []
for index, row in filtered_df.iterrows():
    if row['cpc']:
        try:
            cpc_list = json.loads(row['cpc'])
            for cpc_entry in cpc_list:
                cpc_code = cpc_entry['code']
                if len(cpc_code) >= 4:
                    cpc_group_level4 = cpc_code[:4]
                    if pd.notna(row['filing_date_parsed']):
                        filing_year = row['filing_date_parsed'].year
                        cpc_data.append({'cpc_group_level4': cpc_group_level4, 'filing_year': filing_year})
        except json.JSONDecodeError:
            # Handle cases where cpc is not a valid JSON string
            continue

cpc_df = pd.DataFrame(cpc_data)

if not cpc_df.empty:
    # Calculate annual filing counts for each CPC group
    filings_by_cpc_year = cpc_df.groupby(['cpc_group_level4', 'filing_year']).size().reset_index(name='filings')

    # Calculate EMA
    smoothing_factor = 0.1
    ema_results = []

    for cpc_group in filings_by_cpc_year['cpc_group_level4'].unique():
        group_df = filings_by_cpc_year[filings_by_cpc_year['cpc_group_level4'] == cpc_group].sort_values(by='filing_year')
        # Ensure that there are enough data points for EMA calculation; otherwise, fill with 0
        if not group_df.empty:
            # Reindex to ensure all years are present for correct EMA calculation across time
            all_years = range(group_df['filing_year'].min(), group_df['filing_year'].max() + 1)
            group_df = group_df.set_index('filing_year').reindex(all_years, fill_value=0).reset_index()
            group_df.rename(columns={'index': 'filing_year'}, inplace=True)

            group_df['ema'] = group_df['filings'].ewm(alpha=smoothing_factor, adjust=False).mean()
            best_year_row = group_df.loc[group_df['ema'].idxmax()]
            ema_results.append({
                'cpc_group_level4': cpc_group,
                'best_year': int(best_year_row['filing_year']),
                'highest_ema': best_year_row['ema']
            })
    ema_df = pd.DataFrame(ema_results)
else:
    ema_df = pd.DataFrame(columns=['cpc_group_level4', 'best_year', 'highest_ema'])

print("__RESULT__:")
print(ema_df.to_json(orient='records'))"""

env_args = {'var_function-call-18001159190617317211': 'file_storage/function-call-18001159190617317211.json'}

exec(code, env_args)
