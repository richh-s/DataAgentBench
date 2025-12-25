code = """import pandas as pd
import json
import re

# Load the full result from the file path
with open(locals()['var_function-call-13431301354625501947'], 'r') as f:
    publication_data = json.load(f)

df = pd.DataFrame(publication_data)

# Extract year from filing_date. Ensure filing_date is a string and handle missing values.
def extract_year(date_str):
    if not isinstance(date_str, str):
        return None
    match = re.search(r'\\b(19|20)\\d{2}\\b', date_str)
    if match:
        return int(match.group(0))
    return None

df['filing_year'] = df['filing_date'].apply(extract_year)

# Drop rows where 'filing_year' could not be extracted (is None)
df_processed = df.dropna(subset=['filing_year']).copy()

# If after dropping NaNs, the DataFrame is empty, return an empty list
if df_processed.empty:
    print('__RESULT__:')
    print(json.dumps([]))
else:
    df_processed['filing_year'] = df_processed['filing_year'].astype(int)

    # Explode CPC codes and extract level 5 group codes (first 7 characters)
    all_cpc_records = []
    for index, row in df_processed.iterrows():
        if pd.isna(row['cpc']):
            continue
        try:
            cpc_list = json.loads(row['cpc'])
        except json.JSONDecodeError:
            continue

        for cpc_item in cpc_list:
            code = cpc_item.get('code')
            if isinstance(code, str) and len(code) >= 7 and code[6].isalpha(): # Level 5 CPC codes have a letter at the 7th position
                all_cpc_records.append({'cpc_group_code': code[:7], 'filing_year': row['filing_year']})

    if not all_cpc_records:
        print('__RESULT__:')
        print(json.dumps([]))
    else:
        cpc_df = pd.DataFrame(all_cpc_records)

        # Filter for years 2010-2022
        cpc_df = cpc_df[(cpc_df['filing_year'] >= 2010) & (cpc_df['filing_year'] <= 2022)]

        if cpc_df.empty:
            print('__RESULT__:')
            print(json.dumps([]))
        else:
            # Count filings per CPC code and year
            filings_count = cpc_df.groupby(['cpc_group_code', 'filing_year']).size().reset_index(name='filings')

            # Calculate EMA
            alpha = 0.2
            ema_results = []

            for cpc_code in filings_count['cpc_group_code'].unique():
                cpc_data = filings_count[filings_count['cpc_group_code'] == cpc_code].sort_values(by='filing_year')
                
                ema_current = None
                for i in range(len(cpc_data)):
                    current_filings = cpc_data.iloc[i]['filings']
                    if ema_current is None:
                        ema_current = float(current_filings)
                    else:
                        ema_current = (current_filings * alpha) + (ema_current * (1 - alpha))
                    
                    ema_results.append({'cpc_group_code': cpc_code, 'filing_year': cpc_data.iloc[i]['filing_year'], 'ema': ema_current})

            if not ema_results:
                print('__RESULT__:')
                print(json.dumps([]))
            else:
                ema_df = pd.DataFrame(ema_results)

                # Identify the best year (highest EMA) for each CPC code
                best_year_ema = ema_df.loc[ema_df.groupby('cpc_group_code')['ema'].idxmax()]

                # Filter for CPC codes whose best year is 2022
                cpc_codes_2022_best = best_year_ema[best_year_ema['filing_year'] == 2022]['cpc_group_code'].tolist()

                print('__RESULT__:')
                print(json.dumps(cpc_codes_2022_best))"""

env_args = {'var_function-call-1162082034067506253': 'file_storage/function-call-1162082034067506253.json', 'var_function-call-2188090953045820560': 'file_storage/function-call-2188090953045820560.json', 'var_function-call-13431301354625501947': 'file_storage/function-call-13431301354625501947.json', 'var_function-call-9430444578616541012': [{'symbol': 'A01K2227/108', 'level': '9.0'}, {'symbol': 'A01K2227/105', 'level': '9.0'}, {'symbol': 'A01K2227/101', 'level': '9.0'}, {'symbol': 'A01K2227/107', 'level': '9.0'}, {'symbol': 'A01K2227/103', 'level': '9.0'}, {'symbol': 'A01K2227/106', 'level': '9.0'}, {'symbol': 'A01K2227/706', 'level': '9.0'}, {'symbol': 'A01K2227/703', 'level': '9.0'}, {'symbol': 'A01K2267/025', 'level': '9.0'}, {'symbol': 'A01K2267/0393', 'level': '9.0'}]}

exec(code, env_args)
