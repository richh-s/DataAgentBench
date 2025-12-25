code = """import json
import pandas as pd

# Load the patent data from the file
with open(locals()['var_function-call-683253105236185108'], 'r') as f:
    patent_data = json.load(f)
patent_df = pd.DataFrame(patent_data)

# Load the level 5 CPC symbols from the file
with open(locals()['var_function-call-4047116028136980807'], 'r') as f:
    level_5_cpc_data = json.load(f)
level_5_cpc_symbols = {entry['symbol'] for entry in level_5_cpc_data}

# Extract year from filing_date
def extract_year(date_str):
    if pd.isna(date_str):
        return None
    try:
        date_str = str(date_str).lower()
        # Improved year extraction for common formats
        for month in ["january", "february", "march", "april", "may", "june", 
                      "july", "august", "september", "october", "november", "december"]:
            if month in date_str:
                parts = date_str.split(month)
                if len(parts) > 1 and parts[1].strip().isdigit() and len(parts[1].strip()) == 4:
                    return int(parts[1].strip())
        
        words = date_str.split()
        for word in reversed(words):
            if word.isdigit() and len(word) == 4:
                return int(word)
    except:
        pass
    return None

patent_df['filing_year'] = patent_df['filing_date'].apply(extract_year)

# Extract CPC codes and filter to level 5 using the provided list
def extract_and_filter_level_5_cpc(cpc_json, level_5_symbols):
    codes = []
    if pd.isna(cpc_json):
        return codes
    try:
        cpc_list = json.loads(cpc_json)
        for cpc_entry in cpc_list:
            code = cpc_entry.get('code')
            if code and code in level_5_symbols:
                 codes.append(code)
    except json.JSONDecodeError:
        pass
    return codes

patent_df['cpc_codes'] = patent_df['cpc'].apply(lambda x: extract_and_filter_level_5_cpc(x, level_5_cpc_symbols))

# Explode the DataFrame to have one CPC code per row
df_exploded = patent_df.explode('cpc_codes')

# Filter out rows with missing year or cpc_code
df_filtered = df_exploded.dropna(subset=['filing_year', 'cpc_codes'])

# Convert filing_year to integer
df_filtered['filing_year'] = df_filtered['filing_year'].astype(int)

# Calculate annual filings for each CPC code
annual_filings = df_filtered.groupby(['cpc_codes', 'filing_year']).size().reset_index()
annual_filings.columns = ['cpc_codes', 'filing_year', 'filings'] # Manually assign column names

# Sort by year for EMA calculation
annual_filings_sorted = annual_filings.sort_values(by=['cpc_codes', 'filing_year'])

# Calculate Exponential Moving Average (EMA)
def calculate_ema(group, smoothing_factor=0.2):
    span = 2 / smoothing_factor - 1
    return group['filings'].ewm(span=span, adjust=False).mean()

ema_filings = annual_filings_sorted.groupby('cpc_codes').apply(calculate_ema).reset_index()
ema_filings.columns = ['cpc_codes', 'ema'] # Manually assign column names

# Merge EMA with annual_filings to get the filing_year back for each EMA value
ema_filings = pd.merge(ema_filings, annual_filings_sorted[['cpc_codes', 'filing_year']], 
                       left_index=True, right_index=True, how='left')

# Find the best year (highest EMA) for each CPC code
best_year_ema = ema_filings.loc[ema_filings.groupby('cpc_codes')['ema'].idxmax()]

# Filter for best year 2022
cpc_codes_2022 = best_year_ema[best_year_ema['filing_year'] == 2022]['cpc_codes'].tolist()

print('__RESULT__:')
print(json.dumps(cpc_codes_2022))"""

env_args = {'var_function-call-8435232577099967648': ['publicationinfo'], 'var_function-call-683253105236185108': 'file_storage/function-call-683253105236185108.json', 'var_function-call-15005703462702372622': 'file_storage/function-call-15005703462702372622.json', 'var_function-call-4047116028136980807': 'file_storage/function-call-4047116028136980807.json'}

exec(code, env_args)
