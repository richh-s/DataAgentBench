code = """import pandas as pd
import json
import re

# Load the data from the stored file
with open(locals()['var_function-call-13225136143239241627'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Function to extract year from filing_date
def extract_year(date_string):
    if isinstance(date_string, str):
        match = re.search(r'\b(\d{4})\b', date_string)
        if match:
            return int(match.group(1))
    return None

# Function to extract level 5 CPC codes
def extract_level_5_cpc(cpc_json_string):
    cpc_codes = []
    if isinstance(cpc_json_string, str):
        try:
            cpc_entries = json.loads(cpc_json_string)
            for entry in cpc_entries:
                code = entry.get('code')
                if code and len(code) > 4 and code[4].isalpha() and len(code.split('/')[0]) == 4: # Checking for A01B type format, where it's AXXXB/XX
                    if len(code) >= 7 and code[4].isalpha() and code[5:].isdigit() and (len(code.split('/'))>1 and len(code.split('/')[1])>0): # Assuming Level 5 looks like A01B 1/00 (A01B part, then 1/00 part)
                        main_group = code.split('/')[0]
                        sub_group = code.split('/')[1]
                        if len(main_group) == 4 and len(sub_group) >= 2:
                            cpc_codes.append(f"{main_group}{sub_group[:2]}00".strip()) # taking only first two digits of subgroup, example C01B33/00 takes C01B3300
                elif code and len(code) >= 7 and code[4].isalpha() and code[5].isdigit() and (len(code.split('/'))>1 and len(code.split('/')[1])>0): # this is for C01B33/00 where length is 7
                    main_group = code.split('/')[0]
                    sub_group = code.split('/')[1]
                    if len(main_group) == 5 and len(sub_group) >= 2:
                        cpc_codes.append(f"{main_group}{sub_group[:2]}0".strip()) # taking only first two digits of subgroup
                elif code and len(code) == 7 and code[4].isalpha() and len(code.split('/')) == 1: # for A61K 8/06 where code is A61K806 in the json-like string.
                    if code[4].isalpha() and code[5:].isdigit():
                        cpc_codes.append(f"{code[:4]}{code[4:6]}00".strip())
                elif code and len(code) > 4 and code[4].isalpha() and not code[5].isalpha() and (len(code.split('/'))>1 and len(code.split('/')[1])>0): # for A01B/1/00 format
                    main_group = code.split('/')[0]
                    sub_group = code.split('/')[1]
                    if len(main_group) >= 4 and len(sub_group) >= 2 :
                        cpc_codes.append(f"{main_group}{sub_group[:2]}00".strip())
        except json.JSONDecodeError:
            pass
    return list(set(cpc_codes))

df['filing_year'] = df['filing_date'].apply(extract_year)
df['level_5_cpc'] = df['cpc'].apply(extract_level_5_cpc)

# Explode the DataFrame to have one CPC code per row
df_exploded = df.explode('level_5_cpc')

# Filter out rows with no valid year or CPC code
df_filtered = df_exploded.dropna(subset=['filing_year', 'level_5_cpc'])

# Count patent filings per CPC code per year
filings_per_year_cpc = df_filtered.groupby(['level_5_cpc', 'filing_year']).size().reset_index(name='filings')

# Calculate EMA
smoothing_factor = 0.2
ema_results = {}

for cpc_code in filings_per_year_cpc['level_5_cpc'].unique():
    cpc_data = filings_per_year_cpc[filings_per_year_cpc['level_5_cpc'] == cpc_code].sort_values(by='filing_year')
    ema = []
    if not cpc_data.empty:
        ema_current = cpc_data.iloc[0]['filings']
        ema.append(ema_current)
        for i in range(1, len(cpc_data)):
            ema_current = (cpc_data.iloc[i]['filings'] * smoothing_factor) + (ema_current * (1 - smoothing_factor))
            ema.append(ema_current)
    cpc_data['ema'] = ema
    ema_results[cpc_code] = cpc_data

# Find the best year (highest EMA) for each CPC code
best_year_cpc = {}
for cpc_code, cpc_df in ema_results.items():
    if not cpc_df.empty:
        best_year = cpc_df.loc[cpc_df['ema'].idxmax()]
        best_year_cpc[cpc_code] = best_year['filing_year']

# Filter for CPC codes whose best year is 2022
cpc_best_in_2022 = [cpc for cpc, year in best_year_cpc.items() if year == 2022]

print('__RESULT__:')
print(json.dumps(cpc_best_in_2022))"""

env_args = {'var_function-call-13225136143239241627': 'file_storage/function-call-13225136143239241627.json'}

exec(code, env_args)
