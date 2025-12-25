code = """import json
import pandas as pd
from datetime import datetime
import re

# Load the full result from the file
with open(locals()['var_function-call-13693480272750509533'], 'r') as f:
    publication_data = json.load(f)

df = pd.DataFrame(publication_data)

# Function to parse natural language dates
def parse_date(date_str):
    if pd.isna(date_str) or not isinstance(date_str, str):
        return None
    try:
        # Try a few common formats
        if any(month in date_str for month in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]):
            return datetime.strptime(date_str.replace("th", "").replace("nd", "").replace("rd", "").replace("st", "").replace("dated ", ""), "%B %d, %Y")
        elif any(month in date_str for month in ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]):
            return datetime.strptime(date_str.replace("th", "").replace("nd", "").replace("rd", "").replace("st", "").replace("dated ", ""), "%b %d, %Y")
        elif "of" in date_str:
            parts = date_str.replace("th", "").replace("nd", "").replace("rd", "").replace("st", "").replace("dated ", "").split(" of ")
            if len(parts) == 2: # "day of Month Year"
                return datetime.strptime(f"{parts[0]} {parts[1]}", "%d %B %Y")
            elif len(parts) == 3: # "Month the day of Year"
                # This specific format 'Month the day of Year' is not common and might need adjustment.
                # Let's assume the common case is 'day of Month, Year' or 'Month day, Year'
                return pd.to_datetime(date_str, errors='coerce') # fallback to general parser

        return pd.to_datetime(date_str, errors='coerce')
    except ValueError:
        return None

# Function to extract country code from Patents_info
def extract_country_code(patents_info):
    if pd.isna(patents_info) or not isinstance(patents_info, str):
        return None
    if "Germany" in patents_info or "DE" in patents_info:
        return "DE"
    elif "US patent application (ID US" in patents_info or "US" in patents_info:
        return "US"
    # Add more country extractions as needed, or use regex for robustness
    return None

# Apply date parsing and country extraction
df['grant_date_parsed'] = df['grant_date'].apply(parse_date)
df['filing_year'] = df['filing_date'].apply(lambda x: parse_date(x).year if parse_date(x) else None)
df['country_code'] = df['Patents_info'].apply(extract_country_code)

# Filter for patents granted in Germany in the second half of 2019
filtered_df = df[(df['country_code'] == 'DE') &
                 (df['grant_date_parsed'] >= datetime(2019, 7, 1)) &
                 (df['grant_date_parsed'] <= datetime(2019, 12, 31))].copy()

# Extract CPC codes at level 4
def extract_level4_cpc(cpc_json):
    if pd.isna(cpc_json) or not isinstance(cpc_json, str):
        return []
    try:
        cpc_list = json.loads(cpc_json)
    except json.JSONDecodeError:
        return []
    level4_codes = []
    for cpc_entry in cpc_list:
        code = cpc_entry['code']
        # A Level 4 CPC code typically has the format AXXY Z/NN or AXXY ZN/NN
        # where N is a digit and X,Y,Z are letters/digits.
        # This heuristic attempts to get the part before the last two digits after the '/', if present.
        match = re.match(r"^([A-Z]\d{2}[A-Z][\d/]*?)(?:\d{2})?$", code)
        if match:
            # Try to capture the main group and subgroup without the last two digits after the slash for level 4
            # Example: H01M10/0565 -> H01M10/05
            parts = code.split('/')
            if len(parts) > 1:
                main_group = parts[0]
                sub_group = parts[1]
                if len(sub_group) >= 2:
                    level4_codes.append(f"{main_group}/{sub_group[:-2]}")
                else:
                    level4_codes.append(code) # If subgroup has less than 2 digits, use full code
            else:
                level4_codes.append(code)
        else:
            # Fallback for codes that don't match the heuristic
            if '/' in code:
                parts = code.split('/')
                if len(parts) > 1 and len(parts[1]) > 2:
                    level4_codes.append(f"{parts[0]}/{parts[1][:2]}")
                else:
                    level4_codes.append(code)
            else:
                level4_codes.append(code)

    return level4_codes

filtered_df['level4_cpc_list'] = filtered_df['cpc'].apply(extract_level4_cpc)
exploded_df = filtered_df.explode('level4_cpc_list')

# Group by CPC group and filing year to count patent filings
filings_count = exploded_df.groupby(['level4_cpc_list', 'filing_year']).size().reset_index(name='filings')

# Calculate Exponential Moving Average (EMA) for each CPC group
def calculate_ema(group):
    group = group.sort_values(by='filing_year')
    # Alpha for smoothing factor of 0.1, using adjust=False, so alpha=0.1
    group['ema'] = group['filings'].ewm(alpha=0.1, adjust=False).mean()
    return group

ema_df = filings_count.groupby('level4_cpc_list', group_keys=False).apply(calculate_ema)

# Find the best year (highest EMA) for each CPC group
best_year_cpc = ema_df.loc[ema_df.groupby('level4_cpc_list')['ema'].idxmax()]

# Select relevant columns
result_df = best_year_cpc[['level4_cpc_list', 'filing_year', 'ema']].rename(columns={
    'level4_cpc_list': 'cpc_group_code',
    'filing_year': 'best_year',
    'ema': 'highest_ema'
})

result_json = result_df.to_json(orient='records')

print("__RESULT__:")
print(result_json)"""

env_args = {'var_function-call-13693480272750509533': 'file_storage/function-call-13693480272750509533.json'}

exec(code, env_args)
