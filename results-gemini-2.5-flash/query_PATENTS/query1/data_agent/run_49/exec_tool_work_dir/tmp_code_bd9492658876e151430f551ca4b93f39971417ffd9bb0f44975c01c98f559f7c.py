code = """import pandas as pd
import json
import re

# Read the large JSON file
with open(locals()['var_function-call-6040878569849289475'], 'r') as f:
    data = json.load(f)

# Create a list to store parsed data
parsed_data = []

for record in data:
    cpc_str = record.get('cpc')
    filing_date_str = record.get('filing_date')

    if cpc_str and filing_date_str:
        try:
            # Extract year from filing_date
            year_match = re.search(r'\\d{4}', filing_date_str)
            filing_year = int(year_match.group(0)) if year_match else None

            # Parse CPC codes
            cpc_list = json.loads(cpc_str)
            for cpc_item in cpc_list:
                cpc_code = cpc_item.get('code')
                if cpc_code and filing_year:
                    # Filter for level 5 CPC codes (assuming level 5 means 5 parts, e.g., A61B5/0000)
                    # A more robust way would be to join with CPCDefinition_database, but for now,
                    # we'll assume a pattern or length for level 5.
                    # The prompt specified "CPC group codes at level 5".
                    # CPC codes generally have this format: Section (1 letter) + Class (2 digits) + Subclass (1 letter) + Main Group (1-3 digits) / Subgroup (2-6 digits)
                    # For level 5, it implies a certain length or structure.
                    # Based on examples, level 5 codes seem to be of the form A01B 1/0000 (with 4 digits after slash)
                    # The instruction says "CPC group codes at level 5", which is ambiguous.
                    # Let's assume a level 5 CPC code has a format like 'A01B 1/0000' and extract it if the length of the string after '/' is 4.
                    # If there's no '/', we can't determine the level from the code itself.
                    # Let's simplify and extract the prefix before '/' if it exists, otherwise use the whole code,
                    # and then rely on the CPCDefinition_database for level information in a later step if needed.

                    # Let's extract the full CPC code and then in the next step, filter for level 5 CPC codes by joining with CPCDefinition_database.
                    # This step focuses on cleaning and extracting year and full CPC code.
                    parsed_data.append({'cpc_code_full': cpc_code, 'filing_year': filing_year})
        except (json.JSONDecodeError, ValueError) as e:
            # Handle cases where cpc_str is not valid JSON or date parsing fails
            continue

df_filings = pd.DataFrame(parsed_data)

# Aggregate filings by cpc_code_full and filing_year
filings_count = df_filings.groupby(['cpc_code_full', 'filing_year']).size().reset_index(name='filings')

# Calculate EMA (Exponential Moving Average) for each CPC code
smoothing_factor = 0.2
alpha = smoothing_factor

# Sort by cpc_code_full and filing_year for correct EMA calculation
filings_count = filings_count.sort_values(by=['cpc_code_full', 'filing_year'])

# Initialize EMA column
ema_results = []
for cpc_code, group in filings_count.groupby('cpc_code_full'):
    ema_values = []
    if not group.empty:
        # Sort the group by filing_year for correct EMA calculation
        group = group.sort_values(by='filing_year').copy() # Use .copy() to avoid SettingWithCopyWarning
        
        # Initial EMA is the first filing count
        prev_ema = group['filings'].iloc[0]
        ema_values.append(prev_ema)

        for i in range(1, len(group)):
            current_filings = group['filings'].iloc[i]
            current_ema = alpha * current_filings + (1 - alpha) * prev_ema
            ema_values.append(current_ema)
            prev_ema = current_ema
    
    group.loc[:, 'ema'] = ema_values # Use .loc for explicit assignment
    ema_results.append(group)

if ema_results:
    ema_df = pd.concat(ema_results)
else:
    ema_df = pd.DataFrame(columns=['cpc_code_full', 'filing_year', 'filings', 'ema'])

# Find the best year for each CPC code based on EMA
# Get the index of the max EMA for each cpc_code_full
idx = ema_df.groupby('cpc_code_full')['ema'].idxmax()
best_year_ema = ema_df.loc[idx]

# Filter for CPC codes whose best year is 2022
cpc_codes_2022_best = best_year_ema[best_year_ema['filing_year'] == 2022]['cpc_code_full'].tolist()

print('__RESULT__:')
print(json.dumps(cpc_codes_2022_best))"""

env_args = {'var_function-call-6040878569849289475': 'file_storage/function-call-6040878569849289475.json'}

exec(code, env_args)
