code = """import pandas as pd
import json
import re

raw_data = pd.read_json(locals()['var_function-call-9272648693801938418'])

def parse_date(date_str):
    if not isinstance(date_str, str): return None
    match_month = re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)', date_str, re.IGNORECASE)
    month_map = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6, 'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12}
    month = month_map[match_month.group(0).lower()] if match_month else None

    match_year = re.search(r'\d{4}', date_str)
    year = int(match_year.group(0)) if match_year else None
    return year, month

def get_country_code(patents_info_str):
    if not isinstance(patents_info_str, str): return None
    match = re.search(r'"country_code":\s*"([A-Z]{2})"', patents_info_str)
    return match.group(1) if match else None

# Filter for patents granted in Germany in the second half of 2019
filtered_patents = []
for _, row in raw_data.iterrows():
    grant_year, grant_month = parse_date(row['grant_date'])
    country_code = get_country_code(row['Patents_info'])

    if grant_year == 2019 and grant_month and grant_month >= 7 and country_code == 'DE':
        filing_year, _ = parse_date(row['filing_date'])
        if filing_year:
            # Extract CPC codes at level 4
            cpc_codes = []
            try:
                cpc_data = json.loads(row['cpc'])
                for cpc_entry in cpc_data:
                    code = cpc_entry.get('code')
                    if code and len(code) >= 4:  # CPC group at level 4
                        cpc_codes.append(code[:4])
            except json.JSONDecodeError:
                pass # Handle cases where CPC is not valid JSON
            
            for cpc_code in set(cpc_codes):
                filtered_patents.append({'cpc_group': cpc_code, 'filing_year': filing_year})


# Create a DataFrame for EMA calculation
pdf_filtered = pd.DataFrame(filtered_patents)

# Calculate yearly filings for each CPC group
yearly_filings = pdf_filtered.groupby(['cpc_group', 'filing_year']).size().unstack(fill_value=0)

# Calculate EMA for each CPC group
smoothing_factor = 0.1
ema_results = []
for cpc_group, filings in yearly_filings.iterrows():
    ema = pd.Series(filings).ewm(alpha=smoothing_factor, adjust=False).mean()
    best_year = ema.idxmax()
    highest_ema = ema.max()
    ema_results.append({'cpc_group': cpc_group, 'best_year': int(best_year), 'highest_ema': highest_ema})

# Sort by highest EMA
ema_df = pd.DataFrame(ema_results).sort_values(by='highest_ema', ascending=False)

print("__RESULT__:")
print(ema_df.to_json(orient='records'))"""

env_args = {'var_function-call-4974102629247983957': ['publicationinfo'], 'var_function-call-15607172090208474855': [], 'var_function-call-9272648693801938418': 'file_storage/function-call-9272648693801938418.json'}

exec(code, env_args)
