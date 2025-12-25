code = """import pandas as pd
import json
import re

# Load data from the storage
data_path = locals()['var_function-call-625402063173939593']
with open(data_path, 'r') as f:
    raw_data = json.load(f)

# Prepare data for DataFrame
all_cpc_data = []
for row in raw_data:
    try:
        cpc_list = json.loads(row['cpc'])
        filing_date_str = row['filing_date']

        # Extract year from filing_date using regex
        year_match = re.search(r'\d{4}', filing_date_str)
        year = int(year_match.group(0)) if year_match else None

        if year:
            for cpc_item in cpc_list:
                cpc_code = cpc_item.get('code')
                if cpc_code: # No length filtering yet, will filter by level from definition DB
                    all_cpc_data.append({'cpc_code': cpc_code, 'year': year})
    except (json.JSONDecodeError, TypeError):
        continue

cpc_df = pd.DataFrame(all_cpc_data)

# Count filings per cpc code per year
filings_per_cpc_year = cpc_df.groupby(['cpc_code', 'year']).size().reset_index(name='filings')

# Sort by cpc_code and year for correct EMA calculation
filings_per_cpc_year = filings_per_cpc_year.sort_values(by=['cpc_code', 'year'])

smoothing_factor = 0.2

# Calculate EMA using transform for efficiency
filings_per_cpc_year['ema'] = filings_per_cpc_year.groupby('cpc_code')['filings'].transform(lambda x: x.ewm(alpha=smoothing_factor, adjust=False).mean())

# Find the best year for each cpc_code
idx_max_ema = filings_per_cpc_year.groupby('cpc_code')['ema'].idxmax()
best_year_cpc = filings_per_cpc_year.loc[idx_max_ema]

# Filter for cpc_codes whose best year is 2022
best_in_2022 = best_year_cpc[best_year_cpc['year'] == 2022]

result_cpc_codes = best_in_2022['cpc_code'].tolist()

print('__RESULT__:')
print(json.dumps(result_cpc_codes))"""

env_args = {'var_function-call-625402063173939593': 'file_storage/function-call-625402063173939593.json', 'var_function-call-10429486680241137385': ['cpc_definition']}

exec(code, env_args)
