code = """import pandas as pd
import json
import re

# Load data from the storage
data = pd.read_json(locals()['var_function-call-625402063173939593'])

# Process cpc and filing_date
all_cpc_data = []
for index, row in data.iterrows():
    try:
        cpc_list = json.loads(row['cpc'])
        filing_date_str = row['filing_date']

        # Extract year from filing_date using regex
        year_match = re.search(r'\d{4}', filing_date_str)
        year = int(year_match.group(0)) if year_match else None

        if year:
            for cpc_item in cpc_list:
                cpc_code = cpc_item.get('code')
                if cpc_code and len(cpc_code) >= 5: # Ensure it's at least level 5
                    all_cpc_data.append({'cpc_code': cpc_code, 'year': year})
    except (json.JSONDecodeError, TypeError):
        # Handle cases where cpc is not a valid JSON or other parsing errors
        continue

cpc_df = pd.DataFrame(all_cpc_data)

# Filter for level 5 CPC codes (assuming level 5 means 5 characters long and then further alphanumeric characters)
# CPC codes at level 5 typically have a structure like 'A01B 1/00' or 'A01B1/00'
# The problem asks for "CPC group codes at level 5". Let's assume this means the full CPC code up to level 5.
# For example, if a code is 'A01B 1/00', then 'A01B1/00' is a level 5 code.
# The codes in the dataset are like 'C01B33/00' or 'H01M10/0565'.
# I'll consider the group code at level 5 to be the part before the last '/' if there is one,
# or the whole code if there isn't one and it matches the typical level 5 structure (e.g. A01B1/00).
# Based on the prompt, "CPC group codes at level 5", it usually refers to the 5-character group (e.g., A01B).
# However, the example CPC codes from the database like "C01B33/00" suggest a longer format.
# Let's re-evaluate the "level 5" requirement.
# Given a CPC code like C01B33/00, the group code is C01B. The subgroup is 33/00.
# Level 1: C
# Level 2: C01
# Level 3: C01B
# Level 4: C01B33
# Level 5: C01B33/00
# So I should consider the full code from the database.
# Let's count filings per cpc code per year
filings_per_cpc_year = cpc_df.groupby(['cpc_code', 'year']).size().reset_index(name='filings')

# Calculate EMA
smoothing_factor = 0.2
ema_data = []

# Sort by cpc_code and year to ensure correct EMA calculation
filings_per_cpc_year = filings_per_cpc_year.sort_values(by=['cpc_code', 'year'])

for cpc_code in filings_per_cpc_year['cpc_code'].unique():
    cpc_group_data = filings_per_cpc_year[filings_per_cpc_year['cpc_code'] == cpc_code].copy()
    cpc_group_data['ema'] = cpc_group_data['filings'].ewm(alpha=smoothing_factor, adjust=False).mean()
    ema_data.append(cpc_group_data)

if ema_data:
    ema_df = pd.concat(ema_data)

    # Find the best year for each cpc_code
    idx_max_ema = ema_df.groupby('cpc_code')['ema'].idxmax()
    best_year_cpc = ema_df.loc[idx_max_ema]

    # Filter for cpc_codes whose best year is 2022
    best_in_2022 = best_year_cpc[best_year_cpc['year'] == 2022]

    # Extract the CPC group codes
    # From the prompt "return only the CPC group codes at level 5".
    # I should get the full CPC codes identified as Level 5 from the cpc_definition table later.
    # For now, I'll keep the full code and then filter by level 5 using the definition database.
    result_cpc_codes = best_in_2022['cpc_code'].tolist()
else:
    result_cpc_codes = []

print('__RESULT__:')
print(json.dumps(result_cpc_codes))"""

env_args = {'var_function-call-625402063173939593': 'file_storage/function-call-625402063173939593.json'}

exec(code, env_args)
