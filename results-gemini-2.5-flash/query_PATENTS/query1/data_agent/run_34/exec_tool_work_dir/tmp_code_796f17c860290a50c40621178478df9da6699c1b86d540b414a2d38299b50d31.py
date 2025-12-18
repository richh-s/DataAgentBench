code = """import json
import pandas as pd

# Load the large JSON data from the file
with open(locals()['var_function-call-17019213161780401760'], 'r') as f:
    data = json.load(f)

# Initialize lists to store parsed data
cpc_codes_list = []
filing_years_list = []

for record in data:
    cpc_str = record['cpc']
    filing_date_str = record['filing_date']

    # Parse CPC codes
    if cpc_str:
        try:
            cpc_entries = json.loads(cpc_str)
            for entry in cpc_entries:
                cpc_codes_list.append(entry['code'])
                # Extract year from filing_date
                if filing_date_str:
                    # Attempt to parse date from various formats
                    try:
                        filing_year = pd.to_datetime(filing_date_str, errors='coerce').year
                        filing_years_list.append(filing_year)
                    except:
                        filing_years_list.append(None) # Append None if parsing fails
                else:
                    filing_years_list.append(None)
        except json.JSONDecodeError:
            # Handle cases where cpc_str is not valid JSON
            filing_years_list.extend([None] * len(cpc_codes_list) - len(filing_years_list)) # Adjust length if CPC parsing failed for this record
            continue
    else:
        filing_years_list.append(None)

# Create a DataFrame
df_filings = pd.DataFrame({'cpc_code': cpc_codes_list, 'filing_year': filing_years_list})

# Drop rows where filing_year is None
df_filings.dropna(subset=['filing_year'], inplace=True)
df_filings['filing_year'] = df_filings['filing_year'].astype(int)

# Filter for years between 1900 and 2023 (to remove unreasonable dates)
df_filings = df_filings[(df_filings['filing_year'] >= 1900) & (df_filings['filing_year'] <= 2023)]

# Count filings per CPC code per year
filings_per_year = df_filings.groupby(['cpc_code', 'filing_year']).size().reset_index(name='filing_count')

# Ensure all years are present for each cpc_code for EMA calculation
all_years = range(filings_per_year['filing_year'].min(), filings_per_year['filing_year'].max() + 1)
all_cpc_codes = filings_per_year['cpc_code'].unique()

multi_index = pd.MultiIndex.from_product([all_cpc_codes, all_years], names=['cpc_code', 'filing_year'])
filings_per_year = filings_per_year.set_index(['cpc_code', 'filing_year']).reindex(multi_index, fill_value=0).reset_index()

# Sort for EMA calculation
filings_per_year = filings_per_year.sort_values(by=['cpc_code', 'filing_year'])

# Calculate EMA (smoothing factor 0.2)
alpha = 0.2
filings_per_year['ema'] = filings_per_year.groupby('cpc_code')['filing_count'].transform(lambda x: x.ewm(alpha=alpha, adjust=False).mean())

# Find the year with the highest EMA for each CPC code
idx_max_ema = filings_per_year.groupby('cpc_code')['ema'].idxmax()
best_year_ema = filings_per_year.loc[idx_max_ema, ['cpc_code', 'filing_year', 'ema']]
best_year_ema = best_year_ema.rename(columns={'filing_year': 'best_ema_year'})

# Filter for CPC codes whose best year is 2022
cpc_best_2022 = best_year_ema[best_year_ema['best_ema_year'] == 2022]['cpc_code'].tolist()

print('__RESULT__:')
print(json.dumps(cpc_best_2022))"""

env_args = {'var_function-call-17019213161780401760': 'file_storage/function-call-17019213161780401760.json'}

exec(code, env_args)
