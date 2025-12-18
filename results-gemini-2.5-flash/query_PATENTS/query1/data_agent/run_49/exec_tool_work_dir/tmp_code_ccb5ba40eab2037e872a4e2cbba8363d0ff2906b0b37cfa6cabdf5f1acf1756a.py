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
            year_match = re.search(r'\d{4}', filing_date_str)
            filing_year = int(year_match.group(0)) if year_match else None

            # Parse CPC codes
            cpc_list = json.loads(cpc_str)
            for cpc_item in cpc_list:
                cpc_code = cpc_item.get('code')
                if cpc_code and filing_year:
                    parsed_data.append({'cpc_code': cpc_code, 'filing_year': filing_year})
        except (json.JSONDecodeError, ValueError):
            # Handle cases where cpc_str is not valid JSON or date parsing fails
            continue

df_filings = pd.DataFrame(parsed_data)

# Count patent filings per CPC code per year
filings_count = df_filings.groupby(['cpc_code', 'filing_year']).size().reset_index(name='filings')

# Calculate EMA (Exponential Moving Average) for each CPC code
smoothing_factor = 0.2
alpha = smoothing_factor

# Sort by cpc_code and filing_year for correct EMA calculation
filings_count = filings_count.sort_values(by=['cpc_code', 'filing_year'])

# Initialize EMA column
filings_count['ema'] = 0.0

# Calculate EMA by group
ema_results = []
for cpc_code, group in filings_count.groupby('cpc_code'):
    ema_values = []
    if not group.empty:
        # Sort the group by filing_year for correct EMA calculation
        group = group.sort_values(by='filing_year')
        
        # Initial EMA is the first filing count
        prev_ema = group['filings'].iloc[0]
        ema_values.append(prev_ema)

        for i in range(1, len(group)):
            current_filings = group['filings'].iloc[i]
            current_ema = alpha * current_filings + (1 - alpha) * prev_ema
            ema_values.append(current_ema)
            prev_ema = current_ema
    
    group['ema'] = ema_values
    ema_results.append(group)

if ema_results:
    ema_df = pd.concat(ema_results)
else:
    ema_df = pd.DataFrame(columns=['cpc_code', 'filing_year', 'filings', 'ema'])


# Find the best year for each CPC code based on EMA
best_year_ema = ema_df.loc[ema_df.groupby('cpc_code')['ema'].idxmax()]

# Filter for CPC codes whose best year is 2022
cpc_codes_2022_best = best_year_ema[best_year_ema['filing_year'] == 2022]['cpc_code'].tolist()

print('__RESULT__:')
print(json.dumps(cpc_codes_2022_best))"""

env_args = {'var_function-call-6040878569849289475': 'file_storage/function-call-6040878569849289475.json'}

exec(code, env_args)
