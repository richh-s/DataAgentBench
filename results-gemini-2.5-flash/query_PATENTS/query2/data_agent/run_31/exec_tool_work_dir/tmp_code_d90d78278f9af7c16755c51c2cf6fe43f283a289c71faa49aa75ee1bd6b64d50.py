code = """import json
import pandas as pd
from datetime import datetime
import re

# Load the full result from the file
with open(locals()['var_function-call-13693480272750509533'], 'r') as f:
    publication_data = json.load(f)

df = pd.DataFrame(publication_data)

# Function to parse natural language dates more robustly
def parse_date(date_str):
    if pd.isna(date_str) or not isinstance(date_str, str):
        return None
    date_str = date_str.replace("th", "").replace("nd", "").replace("rd", "").replace("st", "").replace("dated ", "").strip()
    try:
        return pd.to_datetime(date_str, format='%B %d, %Y', errors='coerce')
    except ValueError:
        pass
    try:
        return pd.to_datetime(date_str, format='%b %d, %Y', errors='coerce')
    except ValueError:
        pass
    try:
        # For "5th March 2019" type formats
        return pd.to_datetime(date_str, format='%d %B %Y', errors='coerce')
    except ValueError:
        pass
    try:
        # For "March the 18th, 2019" type formats, try removing "the"
        return pd.to_datetime(date_str.replace(" the ", " "), format='%B %d, %Y', errors='coerce')
    except ValueError:
        pass
    # Fallback to general parser, which might handle more cases but can be less strict
    return pd.to_datetime(date_str, errors='coerce')

# Function to extract country code from Patents_info
def extract_country_code(patents_info):
    if pd.isna(patents_info) or not isinstance(patents_info, str):
        return None
    if "Germany" in patents_info or re.search(r'country_code\s+DE', patents_info):
        return "DE"
    elif "US patent application" in patents_info or re.search(r'country_code\s+US', patents_info):
        return "US"
    # A more general regex to find two-letter country codes preceded by 'ID ' or 'country_code '
    match = re.search(r'(?:ID\s+|country_code\s+)([A-Z]{2})', patents_info)
    if match:
        return match.group(1)
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
        if '/' in code:
            parts = code.split('/')
            main_group = parts[0].strip()
            sub_group_digits = parts[1].strip()
            # Level 4 is usually up to the 2 digits after the slash, if more exist
            if len(sub_group_digits) >= 2:
                level4_codes.append(f"{main_group}/{sub_group_digits[:2]}")
            else:
                level4_codes.append(code) # if less than 2 digits after /, use as is
        else:
            # If no slash, consider the code as is for level 4. This is a heuristic.
            level4_codes.append(code)
    return level4_codes

filtered_df['level4_cpc_list'] = filtered_df['cpc'].apply(extract_level4_cpc)
exploded_df = filtered_df.explode('level4_cpc_list')

# Remove any rows where level4_cpc_list or filing_year is None after explode
exploded_df.dropna(subset=['level4_cpc_list', 'filing_year'], inplace=True)
exploded_df['filing_year'] = exploded_df['filing_year'].astype(int)

# Group by CPC group and filing year to count patent filings
filings_count = exploded_df.groupby(['level4_cpc_list', 'filing_year']).size().reset_index(name='filings')

# Calculate Exponential Moving Average (EMA) for each CPC group
def calculate_ema(group):
    group = group.sort_values(by='filing_year')
    # Smoothing factor 0.1, alpha = 0.1
    group['ema'] = group['filings'].ewm(alpha=0.1, adjust=False).mean()
    return group

# Apply EMA calculation. Use group_keys=False to prevent 'level4_cpc_list' from becoming an index level
ema_df_temp = filings_count.groupby('level4_cpc_list', group_keys=False).apply(calculate_ema)

# Find the best year (highest EMA) for each CPC group.
# Reset index to ensure 'level4_cpc_list' is a column for idxmax and loc operations.
ema_df_temp = ema_df_temp.reset_index(drop=True)
best_year_cpc = ema_df_temp.loc[ema_df_temp.groupby('level4_cpc_list')['ema'].idxmax()]

# Select relevant columns
result_df = best_year_cpc[['level4_cpc_list', 'filing_year', 'ema']].rename(columns={
    'level4_cpc_list': 'cpc_group_code',
    'filing_year': 'best_year',
    'ema': 'highest_ema'
})

result_json = result_df.to_json(orient='records')

print("__RESULT__:")
print(result_json)"""

env_args = {'var_function-call-13693480272750509533': 'file_storage/function-call-13693480272750509533.json', 'var_function-call-11158641396443767350': [{'cpc_group_code': 'A43B13/2', 'best_year': 2016.0, 'highest_ema': 1.0}, {'cpc_group_code': 'A43B17/', 'best_year': 2016.0, 'highest_ema': 2.0}, {'cpc_group_code': 'A43B7/', 'best_year': 2016.0, 'highest_ema': 2.0}, {'cpc_group_code': 'A61F5/', 'best_year': 2016.0, 'highest_ema': 2.0}, {'cpc_group_code': 'A61F5/01', 'best_year': 2016.0, 'highest_ema': 4.0}, {'cpc_group_code': 'B60K6/4', 'best_year': 2013.0, 'highest_ema': 1.0}, {'cpc_group_code': 'B60W30/1', 'best_year': 2013.0, 'highest_ema': 1.0}, {'cpc_group_code': 'F02N11/', 'best_year': 2013.0, 'highest_ema': 1.0}, {'cpc_group_code': 'F02N11/0', 'best_year': 2013.0, 'highest_ema': 1.0}, {'cpc_group_code': 'F02N11/08', 'best_year': 2013.0, 'highest_ema': 1.0}, {'cpc_group_code': 'F02N2200/0', 'best_year': 2013.0, 'highest_ema': 2.0}, {'cpc_group_code': 'F02N2300/20', 'best_year': 2013.0, 'highest_ema': 2.0}, {'cpc_group_code': 'F02P15/', 'best_year': 2011.0, 'highest_ema': 2.0}, {'cpc_group_code': 'F02P3/', 'best_year': 2011.0, 'highest_ema': 2.0}, {'cpc_group_code': 'H01F27/', 'best_year': 2011.0, 'highest_ema': 2.0}, {'cpc_group_code': 'H01F38/', 'best_year': 2011.0, 'highest_ema': 2.0}, {'cpc_group_code': 'Y02T10/', 'best_year': 2013.0, 'highest_ema': 2.0}], 'var_function-call-11165716241033857098': ['cpc_definition'], 'var_function-call-16529514565601507171': "'A43B13/2', 'A43B17/', 'A43B7/', 'A61F5/', 'A61F5/01', 'B60K6/4', 'B60W30/1', 'F02N11/', 'F02N11/0', 'F02N11/08', 'F02N2200/0', 'F02N2300/20', 'F02P15/', 'F02P3/', 'H01F27/', 'H01F38/', 'Y02T10/'", 'var_function-call-15219561017373187378': [{'symbol': 'A61F5/01', 'titleFull': 'Orthopaedic devices, e.g. splints, casts or braces'}, {'symbol': 'F02N11/08', 'titleFull': 'Circuits or control means specially adapted for starting of engines'}, {'symbol': 'F02N2300/20', 'titleFull': 'Control related aspects of engine starting characterised by the control method'}]}

exec(code, env_args)
