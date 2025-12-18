code = """import pandas as pd
import json
import re

# Helper functions (same as before)
def parse_date(date_str):
    try:
        if 'dated ' in date_str:
            date_str = date_str.replace('dated ', '')
        date_str = re.sub(r'(st|nd|rd|th),', ',', date_str)
        return pd.to_datetime(date_str, errors='coerce', dayfirst=False)
    except:
        return pd.NaT

def extract_country_code_strict(patent_info):
    match_id = re.search(r'ID\s+DE-', patent_info)
    match_in = re.search(r'In\s+DE,', patent_info)
    if match_id or match_in:
        return 'DE'
    return None

# Load patent data from the previous query
with open(locals()['var_function-call-5068727344322754251'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Process patent data (same as before)
df['grant_date'] = df['grant_date'].apply(parse_date)
df['filing_date'] = df['filing_date'].apply(parse_date)
df['country_code'] = df['Patents_info'].apply(extract_country_code_strict)

df_germany_filtered = df[(df['grant_date'].dt.year == 2019) & 
                         (df['grant_date'].dt.month >= 7) & 
                         (df['country_code'] == 'DE')].copy()

cpc_data = []
for index, row in df_germany_filtered.iterrows():
    try:
        cpc_list = json.loads(row['cpc'])
        filing_year = row['filing_date'].year
        for cpc_item in cpc_list:
            code = cpc_item['code']
            if isinstance(code, str) and len(code) >= 4:
                cpc_group_4 = code[:4] # Extract first 4 chars as base for EMA calculation
                cpc_data.append({'cpc_group_4': cpc_group_4, 'filing_year': filing_year})
    except (json.JSONDecodeError, TypeError):
        continue

cpc_df = pd.DataFrame(cpc_data)

filings_by_cpc_year = cpc_df.groupby(['cpc_group_4', 'filing_year']).size().reset_index(name='filings')

smoothing_factor = 0.1
ema_calculated_df = filings_by_cpc_year.sort_values(by=['cpc_group_4', 'filing_year'])
ema_calculated_df['ema'] = ema_calculated_df.groupby('cpc_group_4')['filings'].transform(lambda x: x.ewm(alpha=smoothing_factor, adjust=False).mean())

best_ema_for_cpc = ema_calculated_df.loc[ema_calculated_df.groupby('cpc_group_4')['ema'].idxmax()]

ema_results_df = best_ema_for_cpc[['cpc_group_4', 'filing_year', 'ema']].rename(columns={'filing_year': 'best_year', 'ema': 'max_ema'})

# Load CPC definitions (all levels)
with open(locals()['var_function-call-14745830415751959940'], 'r') as f:
    cpc_definitions_data = json.load(f)
cpc_definitions_df_full = pd.DataFrame(cpc_definitions_data)

# Convert 'level' to numeric for proper filtering
cpc_definitions_df_full['level'] = pd.to_numeric(cpc_definitions_df_full['level'], errors='coerce')

# Filter for level 4 definitions
cpc_definitions_level_4_df = cpc_definitions_df_full[cpc_definitions_df_full['level'] == 4.0].copy()

final_output_list = []

# Iterate through the EMA results to find the corresponding level 4 CPC group and its title
for _, ema_row in ema_results_df.iterrows():
    patent_cpc_4_group = ema_row['cpc_group_4']
    best_year = ema_row['best_year']
    
    # Try to find the most specific (longest) level 4 symbol that is a prefix of patent_cpc_4_group
    matching_definitions = cpc_definitions_level_4_df[
        cpc_definitions_level_4_df['symbol'].apply(lambda x: isinstance(x, str) and patent_cpc_4_group.startswith(x))
    ]
    
    if not matching_definitions.empty:
        # Sort by length of symbol in descending order to find the longest prefix match
        matching_definitions = matching_definitions.copy()
        matching_definitions['symbol_len'] = matching_definitions['symbol'].apply(len)
        longest_match = matching_definitions.sort_values(by='symbol_len', ascending=False).iloc[0]
        
        final_output_list.append({
            'titleFull': longest_match['titleFull'],
            'cpc_group_code': longest_match['symbol'], # Use the actual level 4 symbol
            'best_year': best_year
        })

final_results_df = pd.DataFrame(final_output_list)

print("__RESULT__:")
print(final_results_df.to_json(orient='records'))"""

env_args = {'var_function-call-297126640787404012': 'file_storage/function-call-297126640787404012.json', 'var_function-call-5068727344322754251': 'file_storage/function-call-5068727344322754251.json', 'var_function-call-11093841680110614577': [{'cpc_group_4': 'B41F', 'best_year': 2007}, {'cpc_group_4': 'B60K', 'best_year': 2013}, {'cpc_group_4': 'B60R', 'best_year': 2018}, {'cpc_group_4': 'B60S', 'best_year': 2016}, {'cpc_group_4': 'B60W', 'best_year': 2013}, {'cpc_group_4': 'B64D', 'best_year': 2018}, {'cpc_group_4': 'B66C', 'best_year': 2016}, {'cpc_group_4': 'C04B', 'best_year': 2015}, {'cpc_group_4': 'C09K', 'best_year': 2015}, {'cpc_group_4': 'E02F', 'best_year': 2012}, {'cpc_group_4': 'F02N', 'best_year': 2013}, {'cpc_group_4': 'F41H', 'best_year': 2012}, {'cpc_group_4': 'F42B', 'best_year': 2012}, {'cpc_group_4': 'H01R', 'best_year': 2018}, {'cpc_group_4': 'Y02T', 'best_year': 2013}], 'var_function-call-15794588859671135835': 'file_storage/function-call-15794588859671135835.json', 'var_function-call-7985360290914312870': [{'cpc_group_4': 'B41F', 'best_year': 2007, 'max_ema': 3.0}, {'cpc_group_4': 'B60K', 'best_year': 2013, 'max_ema': 1.0}, {'cpc_group_4': 'B60R', 'best_year': 2018, 'max_ema': 1.0}, {'cpc_group_4': 'B60S', 'best_year': 2016, 'max_ema': 1.0}, {'cpc_group_4': 'B60W', 'best_year': 2013, 'max_ema': 1.0}, {'cpc_group_4': 'B64D', 'best_year': 2018, 'max_ema': 1.0}, {'cpc_group_4': 'B66C', 'best_year': 2016, 'max_ema': 1.0}, {'cpc_group_4': 'C04B', 'best_year': 2015, 'max_ema': 45.0}, {'cpc_group_4': 'C09K', 'best_year': 2015, 'max_ema': 2.0}, {'cpc_group_4': 'E02F', 'best_year': 2012, 'max_ema': 5.0}, {'cpc_group_4': 'F02N', 'best_year': 2013, 'max_ema': 7.0}, {'cpc_group_4': 'F41H', 'best_year': 2012, 'max_ema': 2.0}, {'cpc_group_4': 'F42B', 'best_year': 2012, 'max_ema': 2.0}, {'cpc_group_4': 'H01R', 'best_year': 2018, 'max_ema': 6.0}, {'cpc_group_4': 'Y02T', 'best_year': 2013, 'max_ema': 2.0}], 'var_function-call-14655044256450552688': [], 'var_function-call-7971683790454558197': [], 'var_function-call-4188447218076284597': [], 'var_function-call-16531042350842776160': 'file_storage/function-call-16531042350842776160.json', 'var_function-call-4936180994424312443': [], 'var_function-call-11275391057877533887': [], 'var_function-call-8813159367841732341': [], 'var_function-call-12758969213205302255': [], 'var_function-call-12880038949360923757': 'file_storage/function-call-12880038949360923757.json', 'var_function-call-6613148521276364075': [], 'var_function-call-11731273159119014989': 'file_storage/function-call-11731273159119014989.json', 'var_function-call-17101546386702363979': [], 'var_function-call-6553186611529925794': 'file_storage/function-call-6553186611529925794.json', 'var_function-call-5794199066746412496': [], 'var_function-call-2955801480948424602': [], 'var_function-call-16416045839829885028': 'file_storage/function-call-16416045839829885028.json', 'var_function-call-6993928978843861115': [], 'var_function-call-9351177106290979055': [], 'var_function-call-14745830415751959940': 'file_storage/function-call-14745830415751959940.json', 'var_function-call-17704387879430972464': []}

exec(code, env_args)
