code = """import pandas as pd
import json
from collections import defaultdict

# Read the full CPC level 5 symbols from the file
with open(locals()['var_function-call-7593497756142369016'], 'r') as f:
    cpc_level_5_data = json.load(f)
cpc_level_5_symbols = {d['symbol'] for d in cpc_level_5_data}

# Read the full publication data from the file
with open(locals()['var_function-call-5378456248397069076'], 'r') as f:
    publication_data = json.load(f)

# Prepare data for processing
filings_by_cpc_year = defaultdict(lambda: defaultdict(int))

# Function to extract year from filing_date
def extract_year(date_str):
    if isinstance(date_str, str):
        for fmt in ["%dth %B %Y", "%d %B %Y", "%B %dth, %Y", "%B %d, %Y", "%Y", "dated %dth %B %Y", "dated %d %B %Y", "March the %dth, %Y", "%Y-%m-%d"]:
            try:
                return pd.to_datetime(date_str.replace("dated ", "").replace("the ", ""), format=fmt, errors='coerce').year
            except ValueError:
                continue
        import re
        match = re.search(r'\b(\d{4})\b', date_str)
        if match:
            return int(match.group(1))
    return None

# Process publication data
for record in publication_data:
    filing_year = extract_year(record.get('filing_date'))
    if filing_year is None or not (2000 <= filing_year <= 2022): 
        continue
    
    cpc_raw = record.get('cpc')
    if cpc_raw:
        try:
            cpc_entries = json.loads(cpc_raw)
            for cpc_entry in cpc_entries:
                cpc_code = cpc_entry.get('code')
                if cpc_code and cpc_code in cpc_level_5_symbols:
                    filings_by_cpc_year[cpc_code][filing_year] += 1
        except json.JSONDecodeError:
            continue

# Determine the overall min year from actual filings for accurate EMA calculation
all_filing_years = []
for cpc_code_data in filings_by_cpc_year.values():
    all_filing_years.extend(cpc_code_data.keys())
min_actual_filing_year = min(all_filing_years) if all_filing_years else 2000

all_years_range = range(min_actual_filing_year, 2023) # Up to and including 2022

# Calculate EMA for each CPC code
alpha = 0.2
ema_results = []

for cpc_code in cpc_level_5_symbols:
    # Create a DataFrame for all relevant years for this CPC code, filling missing with 0
    cpc_df = pd.DataFrame({
        'filing_year': list(all_years_range),
        'cpc_codes': cpc_code,
        'patent_filings': [filings_by_cpc_year[cpc_code].get(year, 0) for year in all_years_range]
    })
    
    cpc_df = cpc_df.sort_values(by='filing_year')
    cpc_df['ema'] = cpc_df['patent_filings'].ewm(alpha=alpha, adjust=False).mean()
    ema_results.append(cpc_df)

df_ema = pd.concat(ema_results)

# Find the year with the highest EMA for each CPC code
df_max_ema_year = df_ema.loc[df_ema.groupby('cpc_codes')['ema'].idxmax()]

# Filter for CPC codes whose best year is 2022
cpc_codes_2022_best_year = df_max_ema_year[df_max_ema_year['filing_year'] == 2022]['cpc_codes'].tolist()

print('__RESULT__:')
print(json.dumps(cpc_codes_2022_best_year))"""

env_args = {'var_function-call-17556746862476761428': 'file_storage/function-call-17556746862476761428.json', 'var_function-call-5378456248397069076': 'file_storage/function-call-5378456248397069076.json', 'var_function-call-7593497756142369016': 'file_storage/function-call-7593497756142369016.json'}

exec(code, env_args)
