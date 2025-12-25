code = """import json
import pandas as pd

# Load the data from the JSON file
with open(locals()['var_function-call-13877299948745859293'], 'r') as f:
    data = json.load(f)

processed_data = []
for record in data:
    cpc_codes_str = record.get("cpc")
    filing_date_str = record.get("filing_date")

    if cpc_codes_str and filing_date_str:
        try:
            cpc_codes = json.loads(cpc_codes_str)
            # Extract year from filing_date_str (e.g., "dated 5th March 2019" -> 2019)
            filing_year = None
            for part in filing_date_str.split():
                if part.isdigit() and len(part) == 4:
                    filing_year = int(part)
                    break

            if filing_year:
                for cpc_item in cpc_codes:
                    cpc_code = cpc_item.get("code")
                    if cpc_code:
                        processed_data.append({"cpc_code": cpc_code, "filing_year": filing_year})
        except json.JSONDecodeError:
            # Handle cases where cpc_codes_str is not valid JSON
            continue

df_filings = pd.DataFrame(processed_data)

# Filter for years up to 2022 for EMA calculation
df_filings = df_filings[df_filings['filing_year'] <= 2022]

# Group by cpc_code and filing_year to count patents
patent_counts = df_filings.groupby(['cpc_code', 'filing_year']).size().reset_index(name='patent_count')

# Get all unique CPC codes and all years to ensure all combinations exist for EMA calculation
all_cpc_codes = patent_counts['cpc_code'].unique()
all_years = range(patent_counts['filing_year'].min(), patent_counts['filing_year'].max() + 1)

# Create a complete dataframe with all CPC codes and years, filling missing counts with 0
full_index = pd.MultiIndex.from_product([all_cpc_codes, all_years], names=['cpc_code', 'filing_year'])
patent_counts_full = patent_counts.set_index(['cpc_code', 'filing_year']).reindex(full_index, fill_value=0).reset_index()

# Calculate EMA
smoothing_factor = 0.2
ema_results = []
for cpc_code in all_cpc_codes:
    cpc_data = patent_counts_full[patent_counts_full['cpc_code'] == cpc_code].sort_values(by='filing_year')
    cpc_data['ema'] = cpc_data['patent_count'].ewm(alpha=smoothing_factor, adjust=False).mean()
    ema_results.append(cpc_data)

ema_df = pd.concat(ema_results)

# Find the year with the highest EMA for each CPC code
best_ema_year = ema_df.loc[ema_df.groupby('cpc_code')['ema'].idxmax()]

# Filter for CPC codes whose best year is 2022
cpc_best_in_2022 = best_ema_year[best_ema_year['filing_year'] == 2022]['cpc_code'].tolist()

print("__RESULT__:")
print(json.dumps(cpc_best_in_2022))"""

env_args = {'var_function-call-13877299948745859293': 'file_storage/function-call-13877299948745859293.json'}

exec(code, env_args)
