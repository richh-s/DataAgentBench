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

all_cpc_filings = []
# Process only patents with filing_year <= 2022
for index, row in data[data['filing_year'] <= 2022].iterrows(): # Filter early
    cpc_list_str = row['cpc']
    filing_year = row['filing_year']
    if pd.isna(cpc_list_str) or filing_year is None:
        continue
    try:
        cpc_list = json.loads(cpc_list_str)
        for cpc_item in cpc_list:
            if 'code' in cpc_item:
                cpc_code_full = cpc_item['code']
                # Optimized mapping: Try to find longest matching prefix from level5_symbols
                mapped_level5_code = None
                for level5_sym in level5_symbols: # Iterate sorted (longest first)
                    if cpc_code_full.startswith(level5_sym):
                        mapped_level5_code = level5_sym
                        break # Found the most specific level 5 prefix
                if mapped_level5_code:
                    all_cpc_filings.append({'cpc_code': mapped_level5_code, 'filing_year': filing_year})
    except json.JSONDecodeError:
        continue

cpc_filings_df = pd.DataFrame(all_cpc_filings)

# Calculate annual filings for each mapped CPC code
annual_filings = cpc_filings_df.groupby(['cpc_code', 'filing_year']).size().reset_index(name='patent_count')

# Prepare for EMA calculation: Pivot to get years as columns, then unpivot after filling missing years
min_year = annual_filings['filing_year'].min() if not annual_filings.empty else 2022
all_years = range(min_year, 2023) # Ensure years up to 2022 are included
pivoted_filings = annual_filings.pivot_table(index='cpc_code', columns='filing_year', values='patent_count').fillna(0)
# Fill missing columns for years that might not have data for any CPC code
pivoted_filings = pivoted_filings.reindex(columns=all_years, fill_value=0)


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
