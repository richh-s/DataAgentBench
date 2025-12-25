code = """import json
import pandas as pd

file_path = locals()['var_function-call-5336319047275791554']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Extract year from filing_date
def extract_year(date_str):
    try:
        return pd.to_datetime(date_str, errors='coerce').year
    except ValueError:
        try:
            # Handle cases like "dated 5th March 2019"
            year = date_str.strip().split(' ')[-1]
            if year.isdigit():
                return int(year)
            return pd.NA
        except:
            return pd.NA

df['filing_year'] = df['filing_date'].apply(extract_year)
df = df.dropna(subset=['filing_year'])
df['filing_year'] = df['filing_year'].astype(int)

# Extract CPC codes and flatten the list
all_cpc_codes = []
for index, row in df.iterrows():
    try:
        cpc_list = json.loads(row['cpc'])
        for cpc_item in cpc_list:
            code = cpc_item.get('code')
            if code and len(code) >= 5: # Ensure code is at least 5 characters for level 5 analysis later
                all_cpc_codes.append({'cpc_code': code, 'filing_year': row['filing_year']})
    except (json.JSONDecodeError, TypeError):
        continue

cpc_df = pd.DataFrame(all_cpc_codes)

# Filter for CPC codes at level 5 (assuming level 5 means 5 characters, or more complex structure for sub-groups)
# A typical CPC code for level 5 would look like "A61K31/00" or similar, where the first 4 characters are group and then '/' and then sub-group.
# For simplicity and given the nature of the codes, I will consider level 5 as the full code for now.
# However, if 'level' field was directly available in publicationinfo, it would be easier.
# Given the query asks for CPC group codes at level 5, let's assume it refers to the full 'symbol' in CPCDefinition_database where level is 5.
# For now, I'll count based on the full code and later filter using CPCDefinition_database to confirm level 5 codes.

# Count filings per CPC code and year
yearly_filings = cpc_df.groupby(['cpc_code', 'filing_year']).size().reset_index(name='filings')

# Calculate Exponential Moving Average
smoothing_factor = 0.2
yearly_filings_pivot = yearly_filings.pivot_table(index='filing_year', columns='cpc_code', values='filings').fillna(0)

ema_results = {}
for cpc_code in yearly_filings_pivot.columns:
    series = yearly_filings_pivot[cpc_code]
    ema = series.ewm(alpha=smoothing_factor, adjust=False).mean()
    ema_results[cpc_code] = ema

# Find the best year for each CPC code (highest EMA)
best_year_for_cpc = {}
for cpc_code, ema_series in ema_results.items():
    if not ema_series.empty:
        best_year = ema_series.idxmax()
        best_year_for_cpc[cpc_code] = best_year

# Filter for CPC codes whose best year is 2022
cpc_codes_best_in_2022 = [cpc for cpc, year in best_year_for_cpc.items() if year == 2022]

# Now, need to check CPCDefinition_database for level 5 codes.
# This part will be done in the next step, by querying the CPCDefinition_database
# and then filtering the cpc_codes_best_in_2022.

print("__RESULT__:")
print(json.dumps(cpc_codes_best_in_2022))"""

env_args = {'var_function-call-5336319047275791554': 'file_storage/function-call-5336319047275791554.json'}

exec(code, env_args)
