code = """import json
import pandas as pd
from datetime import datetime

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
        if "January" in date_str or "February" in date_str or "March" in date_str or \
           "April" in date_str or "May" in date_str or "June" in date_str or \
           "July" in date_str or "August" in date_str or "September" in date_str or \
           "October" in date_str or "November" in date_str or "December" in date_str:
            return datetime.strptime(date_str.replace("th", "").replace("nd", "").replace("rd", "").replace("st", "").replace("dated ", ""), "%B %d, %Y")
        elif "Jan" in date_str or "Feb" in date_str or "Mar" in date_str or \
             "Apr" in date_str or "May" in date_str or "Jun" in date_str or \
             "Jul" in date_str or "Aug" in date_str or "Sep" in date_str or \
             "Oct" in date_str or "Nov" in date_str or "Dec" in date_str:
            return datetime.strptime(date_str.replace("th", "").replace("nd", "").replace("rd", "").replace("st", "").replace("dated ", ""), "%b %d, %Y")
        elif "of" in date_str:
            parts = date_str.replace("th", "").replace("nd", "").replace("rd", "").replace("st", "").replace("dated ", "").split(" of ")
            if len(parts) == 2: # "day of Month Year"
                return datetime.strptime(f"{parts[0]} {parts[1]}", "%d %B %Y")
            elif len(parts) == 3: # "Month the day of Year"
                return datetime.strptime(f"{parts[1]} {parts[0]} {parts[2]}", "%d %B %Y")


        return pd.to_datetime(date_str, errors='coerce')
    except ValueError:
        return None

# Function to extract country code from Patents_info
def extract_country_code(patents_info):
    if pd.isna(patents_info) or not isinstance(patents_info, str):
        return None
    if "Germany" in patents_info:
        return "DE"
    elif "US patent application (ID US" in patents_info:
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

# Extract CPC codes at level 4. A Level 4 CPC code typically means the main group.
# For example, for "H01M10/0565", the level 4 would be "H01M10/05".
# We will extract the part before the last two digits after the "/" if present, or the full code if shorter.
# This heuristic assumes that standard CPC groups are typically 4 characters followed by numbers and then a slash followed by more numbers.
# e.g., A61K 31/00. Here, A61K31/00 would be a level 4 group.
# The prompt asks for "CPC group at level 4". Let's assume that means the main group code before the final two digits of the subgroup.

def extract_level4_cpc(cpc_json):
    if pd.isna(cpc_json) or not isinstance(cpc_json, str):
        return []
    cpc_list = json.loads(cpc_json)
    level4_codes = []
    for cpc_entry in cpc_list:
        code = cpc_entry['code']
        # Heuristic for Level 4: take up to the first 4 characters and then if there's a '/' after that, take up to the first two digits after the '/'
        # e.g. H01M10/0565 -> H01M10/05
        #      C01B33/00 -> C01B33/00
        match = re.match(r"^([A-Z]\d{2}[A-Z]\d{0,3})(?:/(\d{2}))?", code)
        if match:
            base_code = match.group(1)
            subgroup_digits = match.group(2)
            if subgroup_digits:
                level4_codes.append(f"{base_code}/{subgroup_digits}")
            else:
                level4_codes.append(base_code)
        else:
            # Fallback for codes that don't match the heuristic, try to get the first part up to a / or just the code if no /
            if '/' in code:
                parts = code.split('/')
                if len(parts) > 1 and len(parts[1]) > 2:
                    level4_codes.append(f"{parts[0]}/{parts[1][:2]}")
                else:
                    level4_codes.append(code)
            else:
                level4_codes.append(code)

    return level4_codes

import re
filtered_df['level4_cpc_list'] = filtered_df['cpc'].apply(extract_level4_cpc)
exploded_df = filtered_df.explode('level4_cpc_list')

# Group by CPC group and filing year to count patent filings
filings_count = exploded_df.groupby(['level4_cpc_list', 'filing_year']).size().reset_index(name='filings')

# Calculate Exponential Moving Average (EMA) for each CPC group
def calculate_ema(group):
    # Sort by filing_year to ensure correct EMA calculation
    group = group.sort_values(by='filing_year')
    group['ema'] = group['filings'].ewm(span=1/(0.1/2 - 0.5), adjust=False).mean() # Smoothing factor 0.1, alpha = 0.1
    return group

ema_df = filings_count.groupby('level4_cpc_list').apply(calculate_ema)

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
