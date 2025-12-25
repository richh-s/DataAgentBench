code = """import json
import pandas as pd

# Load the data from the file
with open(locals()['var_function-call-683253105236185108'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Extract year from filing_date
def extract_year(date_str):
    if pd.isna(date_str): # Handle missing values
        return None
    try:
        # Attempt to parse common date formats
        date_str = str(date_str).lower()
        if "january" in date_str: return int(date_str.split("january")[1].strip())
        if "february" in date_str: return int(date_str.split("february")[1].strip())
        if "march" in date_str: return int(date_str.split("march")[1].strip())
        if "april" in date_str: return int(date_str.split("april")[1].strip())
        if "may" in date_str: return int(date_str.split("may")[1].strip())
        if "june" in date_str: return int(date_str.split("june")[1].strip())
        if "july" in date_str: return int(date_str.split("july")[1].strip())
        if "august" in date_str: return int(date_str.split("august")[1].strip())
        if "september" in date_str: return int(date_str.split("september")[1].strip())
        if "october" in date_str: return int(date_str.split("october")[1].strip())
        if "november" in date_str: return int(date_str.split("november")[1].strip())
        if "december" in date_str: return int(date_str.split("december")[1].strip())
        
        # Fallback for "dated Xth Month YYYY" or similar patterns
        words = date_str.split()
        for word in reversed(words):
            if word.isdigit() and len(word) == 4:
                return int(word)
    except:
        pass
    return None

df['filing_year'] = df['filing_date'].apply(extract_year)

# Extract CPC codes at level 5
def extract_level_5_cpc(cpc_json):
    codes = []
    if pd.isna(cpc_json): # Handle missing values
        return codes
    try:
        cpc_list = json.loads(cpc_json)
        for cpc_entry in cpc_list:
            code = cpc_entry.get('code')
            if code and len(code) == 11 and code[4].isalpha() and code[5:].isdigit():  # Basic check for level 5: X000X00/00
                 codes.append(code)
    except json.JSONDecodeError:
        pass
    return codes

df['cpc_codes'] = df['cpc'].apply(extract_level_5_cpc)

# Explode the DataFrame to have one CPC code per row
df_exploded = df.explode('cpc_codes')

# Filter out rows with missing year or cpc_code
df_filtered = df_exploded.dropna(subset=['filing_year', 'cpc_codes'])

# Convert filing_year to integer
df_filtered['filing_year'] = df_filtered['filing_year'].astype(int)

# Calculate annual filings for each CPC code
annual_filings = df_filtered.groupby(['cpc_codes', 'filing_year']).size().reset_index(name='filings')

# Sort by year for EMA calculation
annual_filings_sorted = annual_filings.sort_values(by=['cpc_codes', 'filing_year'])

# Calculate Exponential Moving Average (EMA)
def calculate_ema(group, span=5, smoothing_factor=0.2):
    # Adjust span based on smoothing factor for pandas ewm function
    # For a given smoothing factor alpha, span = 2/alpha - 1
    # span = 2/0.2 - 1 = 10 - 1 = 9
    return group['filings'].ewm(span=9, adjust=False).mean()

ema_filings = annual_filings_sorted.groupby('cpc_codes').apply(calculate_ema).reset_index(name='ema')
ema_filings['filing_year'] = annual_filings_sorted['filing_year']

# Find the best year (highest EMA) for each CPC code
best_year_ema = ema_filings.loc[ema_filings.groupby('cpc_codes')['ema'].idxmax()]

# Filter for best year 2022
cpc_codes_2022 = best_year_ema[best_year_ema['filing_year'] == 2022]['cpc_codes'].tolist()

print('__RESULT__:')
print(json.dumps(cpc_codes_2022))"""

env_args = {'var_function-call-8435232577099967648': ['publicationinfo'], 'var_function-call-683253105236185108': 'file_storage/function-call-683253105236185108.json'}

exec(code, env_args)
