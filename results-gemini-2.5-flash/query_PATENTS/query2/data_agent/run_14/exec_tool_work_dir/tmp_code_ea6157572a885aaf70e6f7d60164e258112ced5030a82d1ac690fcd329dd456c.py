code = """import pandas as pd
import json

# Load the large JSON result from the file path
data = pd.read_json(locals()['var_function-call-12286119263325599604'])

def parse_date(date_str):
    if isinstance(date_str, str):
        # Clean the string for parsing
        date_str = date_str.replace("th", "").replace("rd", "").replace("nd", "").replace("st", "").replace("on ", "").replace(",", "")
        try:
            return pd.to_datetime(date_str, format="%B %d %Y", errors='coerce')
        except ValueError:
            try:
                return pd.to_datetime(date_str, format="%d %B %Y", errors='coerce')
            except ValueError:
                try:
                    return pd.to_datetime(date_str, format="%Y %B %d", errors='coerce')
                except ValueError:
                    return pd.to_datetime(date_str, errors='coerce')
    return pd.NaT

data['parsed_grant_date'] = data['grant_date'].apply(parse_date)
data['parsed_filing_date'] = data['filing_date'].apply(parse_date)

# Filter for patents granted in the second half of 2019 and from Germany
filtered_data = data[
    (data['parsed_grant_date'].dt.year == 2019) &
    (data['parsed_grant_date'].dt.month >= 7) &
    (data['Patents_info'].str.contains('from DE', na=False))
]

cpc_filings = []
for _, row in filtered_data.iterrows():
    try:
        cpc_list = json.loads(row['cpc'])
        for cpc_item in cpc_list:
            code = cpc_item['code']
            if len(code) >= 4:
                cpc_group = code[:4]
                filing_year = row['parsed_filing_date'].year
                if not pd.isna(filing_year):
                    cpc_filings.append({'cpc_group': cpc_group, 'filing_year': int(filing_year)})
    except (json.JSONDecodeError, TypeError):
        continue

filings_df = pd.DataFrame(cpc_filings)

# Group by CPC group and filing year to count patents
yearly_filings = filings_df.groupby(['cpc_group', 'filing_year']).size().reset_index(name='count')

# Pivot to have years as columns for easier EMA calculation
# Fill NaNs with 0 to ensure all years have a value for EMA calculation
pivot_df = yearly_filings.pivot(index='cpc_group', columns='filing_year', values='count').fillna(0)

alpha = 0.1
ema_results = []

for cpc_group in pivot_df.index:
    current_ema = 0
    best_year_for_group = None
    highest_ema_for_group = -1

    # Get all years in the pivot table for this cpc_group and sort them
    years_for_group = sorted(pivot_df.columns.intersection(pivot_df.loc[cpc_group].dropna().index).tolist())
    
    # If there are no filings for this group, skip it.
    if not years_for_group:
        continue

    # Initialize current_ema with the first year's value if available
    first_year = years_for_group[0]
    current_ema = pivot_df.loc[cpc_group, first_year]
    highest_ema_for_group = current_ema
    best_year_for_group = first_year

    for year in years_for_group[1:]:
        value = pivot_df.loc[cpc_group, year]
        current_ema = alpha * value + (1 - alpha) * current_ema
        if current_ema > highest_ema_for_group:
            highest_ema_for_group = current_ema
            best_year_for_group = year
    
    # If no valid best year was found, use the first year as a fallback, though this shouldn't happen with the current logic
    if best_year_for_group is not None:
        ema_results.append({
            'cpc_group': cpc_group,
            'best_year': int(best_year_for_group),
            'highest_ema': highest_ema_for_group
        })

best_cpc_df = pd.DataFrame(ema_results).sort_values(by='highest_ema', ascending=False)

print("__RESULT__:")
print(best_cpc_df.to_json(orient='records'))"""

env_args = {'var_function-call-12286119263325599604': 'file_storage/function-call-12286119263325599604.json', 'var_function-call-17238172386859849011': [{'cpc_group': 'A61F', 'best_year': 2016, 'highest_ema': 0.6}, {'cpc_group': 'A43B', 'best_year': 2016, 'highest_ema': 0.5}], 'var_function-call-15995829258352346263': [], 'var_function-call-15786196653833816783': 'file_storage/function-call-15786196653833816783.json', 'var_function-call-2044574974618873207': [], 'var_function-call-6381926105834134672': 'file_storage/function-call-6381926105834134672.json', 'var_function-call-6484813827852245575': 'A61F, A43B', 'var_function-call-8800901605693715834': [], 'var_function-call-2936073602088239421': 'file_storage/function-call-2936073602088239421.json', 'var_function-call-3412235902006546830': 'file_storage/function-call-3412235902006546830.json', 'var_function-call-12997310755155396542': 'file_storage/function-call-12997310755155396542.json'}

exec(code, env_args)
