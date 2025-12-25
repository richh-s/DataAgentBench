code = """import json
import pandas as pd
import re

# Load the full result from the file
with open(locals()['var_function-call-12637477994751349657'], 'r') as f:
    data = json.load(f)

records = data['query_db_response']['results']

all_cpc_data = []

for record in records:
    cpc_codes_str = record.get('cpc')
    filing_date_str = record.get('filing_date')

    filing_year = None
    if filing_date_str:
        # Extract year from natural language date string
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
            # Handle cases where cpc_codes_str is not a valid JSON
            pass

df_cpc = pd.DataFrame(all_cpc_data)

# Extract level 5 CPC group codes (e.g., A61K 31/00 becomes A61K31/000, A61K 31/00A)
# A level 5 CPC code has a format like 'SECTIONNN/NNAA' where 'SECTION' is A-H, 'NN' is group, 'NNN' is subgroup, 'NN' is further subgroup and 'AA' are two letters.
# Simpler approach: split by '/' and then take the first 4 characters and the part after the '/'
# The general format for CPC is Section (1 letter) + Class (2 digits) + Subclass (1 letter) + Main Group (1-3 digits) + Subgroup (0-5 digits or letters).
# A level 5 CPC is defined in the CPCDefinition_database by the 'level' column.
# For now, let's extract the full CPC code and then filter by level using the CPCDefinition_database in the next step.
# The `symbol` in `cpc_definition` table corresponds to the full CPC code.

# We need to filter for level 5 CPC codes.
# For now, let's just count all CPC codes by year.
cpc_counts_per_year = df_cpc.groupby(['cpc_code', 'filing_year']).size().reset_index(name='patent_count')

# Pivot the table to have years as columns and cpc_code as index
pivot_table = cpc_counts_per_year.pivot(index='cpc_code', columns='filing_year', values='patent_count').fillna(0)

# Calculate EMA for each CPC code
alpha = 0.2
ema_data = {}
for cpc_code in pivot_table.index:
    series = pivot_table.loc[cpc_code]
    ema_values = []
    current_ema = 0
    for year in sorted(series.index):
        if year <= 2022: # Only consider years up to 2022 for EMA calculation
            current_ema = (series[year] * alpha) + (current_ema * (1 - alpha))
            ema_values.append({'year': year, 'ema': current_ema})
    ema_data[cpc_code] = ema_values

# Find the best year (highest EMA) for each CPC code, considering only up to 2022
best_year_cpc = []
for cpc_code, emas in ema_data.items():
    if emas: # Check if emas list is not empty
        best_ema_for_cpc = max(emas, key=lambda x: x['ema'])
        if best_ema_for_cpc['year'] == 2022:
            best_year_cpc.append(cpc_code)

print("__RESULT__:")
print(json.dumps(best_year_cpc))"""

env_args = {'var_function-call-12637477994751349657': 'file_storage/function-call-12637477994751349657.json'}

exec(code, env_args)
