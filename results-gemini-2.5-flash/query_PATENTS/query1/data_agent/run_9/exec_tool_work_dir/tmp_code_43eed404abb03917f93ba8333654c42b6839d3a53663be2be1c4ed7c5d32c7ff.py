code = """import pandas as pd
import json

# Load the large JSON data from the file
with open(locals()['var_function-call-12031246827532621766'], 'r') as f:
    data = json.load(f)

# Extract relevant information
cpc_data = []
for record in data:
    filing_date_str = record.get('filing_date')
    if filing_date_str:
        try:
            # Extract year from natural language date string
            year = int(filing_date_str.strip().split()[-1])
        except ValueError:
            year = None # Handle cases where year extraction fails
    else:
        year = None

    cpc_list_str = record.get('cpc')
    if cpc_list_str:
        try:
            cpc_entries = json.loads(cpc_list_str)
            for entry in cpc_entries:
                cpc_code = entry.get('code')
                if cpc_code and year:
                    # CPC level 5 format example: A01B 1/00
                    # The requirement states "CPC group codes at level 5"
                    # The symbol in the CPCDefinition_database is of the format 'A01B1/00' without spaces.
                    # So, we need to convert 'A01B 1/00' to 'A01B1/00' and then check its length,
                    # or more reliably, check if it fits the pattern of a level 5 code.
                    # A level 5 code typically has a section, class, subclass, group and subgroup,
                    # like 'A01B1/00' or 'A01B1/00B'
                    # The length of a level 5 code without space can be for example 8 or 9 chars
                    # For example, A01B1/00 is a valid level 5 code in 'cpc_definition' table as 'symbol'.
                    # Let's consider a code at level 5 has a structure like `A01B1/00` where the first 4 chars
                    # are section, class, subclass, main group, then a '/' and then 2 or more digits for subgroup.
                    # A simpler heuristic for level 5: It should contain a '/' and have at least 6 characters after removing spaces
                    
                    if '/' in cpc_code and len(cpc_code.replace(' ', '')) >= 6:
                        cpc_data.append({'cpc_code': cpc_code.replace(' ', ''), 'year': year})
        except json.JSONDecodeError:
            pass # Handle cases where cpc_list_str is not valid JSON

df = pd.DataFrame(cpc_data)

# Count filings per CPC code and year
yearly_filings = df.groupby(['cpc_code', 'year']).size().reset_index(name='filings')

# Calculate EMA for each CPC code
smoothing_factor = 0.2
ema_results = []

for cpc_code in yearly_filings['cpc_code'].unique():
    cpc_df = yearly_filings[yearly_filings['cpc_code'] == cpc_code].sort_values(by='year')
    cpc_df['ema'] = cpc_df['filings'].ewm(alpha=smoothing_factor, adjust=False).mean()
    if not cpc_df.empty:
        ema_results.append(cpc_df)

if ema_results:
    ema_df = pd.concat(ema_results)
else:
    ema_df = pd.DataFrame(columns=['cpc_code', 'year', 'filings', 'ema'])

# Find the best year (highest EMA) for each CPC code
idx = ema_df.groupby('cpc_code')['ema'].idxmax()
best_years_df = ema_df.loc[idx]

# Filter for CPC codes whose best year is 2022
cpc_codes_2022_best = best_years_df[best_years_df['year'] == 2022]['cpc_code'].tolist()

print('__RESULT__:')
print(json.dumps(cpc_codes_2022_best))"""

env_args = {'var_function-call-12031246827532621766': 'file_storage/function-call-12031246827532621766.json'}

exec(code, env_args)
