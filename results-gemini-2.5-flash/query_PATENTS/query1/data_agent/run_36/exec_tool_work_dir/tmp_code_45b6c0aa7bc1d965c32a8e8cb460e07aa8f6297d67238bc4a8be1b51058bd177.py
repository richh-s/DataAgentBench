code = """import pandas as pd
import json

# Load the full result from the file
with open(locals()['var_function-call-9977547959283513273'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Extract year from filing_date and handle potential errors
def extract_year(date_str):
    if pd.isna(date_str) or not isinstance(date_str, str):
        return None
    try:
        # Common date formats to try to extract the year
        for fmt in ["%B %dth, %Y", "%B the %dth, %Y", "%Y", "%d %B %Y", "%B %d, %Y"]:
            if "th" in date_str:
                date_str = date_str.replace("th", "").replace("st", "").replace("nd", "").replace("rd", "")
            elif "dated" in date_str:
                date_str = date_str.replace("dated", "").strip()
            
            try:
                return pd.to_datetime(date_str, format=fmt, errors='coerce').year
            except ValueError:
                pass
        # Fallback for simpler year extraction if direct parsing fails
        year_match = pd.to_numeric(date_str, errors='coerce')
        if not pd.isna(year_match):
            return int(year_match)
        return None
    except:
        return None

df['filing_year'] = df['filing_date'].apply(extract_year)

# Filter out rows with invalid years
df = df.dropna(subset=['filing_year'])
df['filing_year'] = df['filing_year'].astype(int)

# Extract CPC codes and flatten the list
cpc_data = []
for _, row in df.iterrows():
    try:
        cpc_list = json.loads(row['cpc'])
        for cpc_item in cpc_list:
            cpc_data.append({'cpc_code': cpc_item['code'], 'filing_year': row['filing_year']})
    except (json.JSONDecodeError, TypeError):
        continue

cpc_df = pd.DataFrame(cpc_data)

# Count patent filings per CPC code and year
filings_by_cpc_year = cpc_df.groupby(['cpc_code', 'filing_year']).size().reset_index(name='patent_count')

# Filter for years up to 2022 and sort by year for EMA calculation
filings_by_cpc_year = filings_by_cpc_year[filings_by_cpc_year['filing_year'] <= 2022]
filings_by_cpc_year = filings_by_cpc_year.sort_values(by=['cpc_code', 'filing_year'])

# Calculate EMA (smoothing factor 0.2)
alpha = 0.2
ema_results = []
for cpc_code, group in filings_by_cpc_year.groupby('cpc_code'):
    # Create a full range of years for this CPC code to ensure all years are present
    min_year = group['filing_year'].min()
    max_year = group['filing_year'].max()
    full_years_range = pd.DataFrame({'filing_year': range(min_year, max_year + 1)})
    
    # Merge with the existing group to get 0 for years with no filings
    group_full_years = pd.merge(full_years_range, group, on='filing_year', how='left').fillna(0)
    group_full_years['cpc_code'] = cpc_code # Ensure cpc_code is present after merge
    
    group_full_years = group_full_years.sort_values(by='filing_year')
    group_full_years['ema'] = group_full_years['patent_count'].ewm(alpha=alpha, adjust=False).mean()
    ema_results.append(group_full_years)

ema_df = pd.concat(ema_results)

# Find the year with the highest EMA for each CPC code
idx_max_ema = ema_df.groupby('cpc_code')['ema'].idxmax()
best_year_cpc = ema_df.loc[idx_max_ema]

# Filter for best year 2022
cpc_best_year_2022 = best_year_cpc[best_year_cpc['filing_year'] == 2022]['cpc_code'].tolist()

# Filter for CPC group codes at level 5
cpc_level_5 = [cpc_code for cpc_code in cpc_best_year_2022 if len(cpc_code) >= 5 and cpc_code[4].isdigit()]


print("__RESULT__:")
print(json.dumps(cpc_level_5))"""

env_args = {'var_function-call-9977547959283513273': 'file_storage/function-call-9977547959283513273.json'}

exec(code, env_args)
