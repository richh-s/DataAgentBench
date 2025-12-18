code = """import pandas as pd
import json
import re

# Load publicationinfo data
data = pd.read_json(locals()['var_function-call-9499660023967929457'])

# Load cpc_definition data for level 5 symbols
with open(locals()['var_function-call-4508705775201837439'], 'r') as f:
    cpc_level5_data = json.load(f)
cpc_level5_df = pd.DataFrame(cpc_level5_data)
cpc_level5_df['level'] = pd.to_numeric(cpc_level5_df['level'])
level5_symbols = sorted(cpc_level5_df[cpc_level5_df['level'] == 5.0]['symbol'].tolist(), key=len, reverse=True)

def parse_year(date_str):
    if isinstance(date_str, str):
        match = re.search(r'\\d{4}', date_str)
        if match:
            return int(match.group(0))
    return None

data['filing_year'] = data['filing_date'].apply(parse_year)

# Function to map detailed CPC code to its level 5 group
def map_to_level5_cpc(cpc_code, level5_symbols):
    for symbol in level5_symbols:
        if cpc_code.startswith(symbol):
            return symbol
    return None

all_cpc_filings = []
for index, row in data.iterrows():
    cpc_list_str = row['cpc']
    filing_year = row['filing_year']
    if pd.isna(cpc_list_str) or filing_year is None:
        continue
    try:
        cpc_list = json.loads(cpc_list_str)
        for cpc_item in cpc_list:
            if 'code' in cpc_item:
                level5_mapped_code = map_to_level5_cpc(cpc_item['code'], level5_symbols)
                if level5_mapped_code:
                    all_cpc_filings.append({'cpc_code': level5_mapped_code, 'filing_year': filing_year})
    except json.JSONDecodeError:
        continue

cpc_filings_df = pd.DataFrame(all_cpc_filings)

# Filter for years up to 2022
cpc_filings_df = cpc_filings_df[cpc_filings_df['filing_year'] <= 2022]

# Calculate annual filings for each mapped CPC code
annual_filings = cpc_filings_df.groupby(['cpc_code', 'filing_year']).size().reset_index(name='patent_count')

# Prepare for EMA calculation: Pivot to get years as columns, then unpivot after filling missing years
pivoted_filings = annual_filings.pivot_table(index='cpc_code', columns='filing_year', values='patent_count').fillna(0)

# Calculate EMA
smoothing_factor = 0.2
ema_df = pivoted_filings.ewm(alpha=smoothing_factor, axis=1, adjust=False).mean()

# Find the best year for each CPC code based on EMA
best_year_series = ema_df.idxmax(axis=1)

# Filter for CPC codes whose best year is 2022
cpc_best_in_2022_ema = best_year_series[best_year_series == 2022].index.tolist()

print("__RESULT__:")
print(json.dumps(cpc_best_in_2022_ema))"""

env_args = {'var_function-call-14696505315028543546': 'file_storage/function-call-14696505315028543546.json', 'var_function-call-9499660023967929457': 'file_storage/function-call-9499660023967929457.json', 'var_function-call-17851144477517317510': 'file_storage/function-call-17851144477517317510.json', 'var_function-call-4508705775201837439': 'file_storage/function-call-4508705775201837439.json', 'var_function-call-16860636197230919779': []}

exec(code, env_args)
