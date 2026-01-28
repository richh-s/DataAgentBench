code = """import json
import pandas as pd

file_path = var_functions.query_db:2

if isinstance(file_path, str):
    with open(file_path, 'r') as f:
        patents_data = json.load(f)
else:
    patents_data = file_path

df = pd.DataFrame(patents_data)

print('Total patents loaded:', len(df))
print('Columns:', list(df.columns))

# Filter for Germany patents with DE-xxxxx format
def is_germany(patents_info):
    if not patents_info:
        return False
    return 'DE-' in str(patents_info)

df['is_germany'] = df['Patents_info'].apply(is_germany)

# Parse grant dates - handle various formats
def extract_yeargrant(date_str):
    if not date_str:
        return None
    try:
        parts = str(date_str).split()
        for part in parts:
            if part.isdigit() and len(part) == 4:
                return int(part)
        return None
    except:
        return None

df['grant_year'] = df['grant_date'].apply(extract_yeargrant)

# Filter for 2019 Germany patents
germany_2019 = df[(df['is_germany']) & (df['grant_year'] == 2019)]

print('Germany patents in 2019:', len(germany_2019))

# Check grant dates for second half of 2019
def get_month(date_str):
    if not date_str:
        return None
    str_date = str(date_str).lower()
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    for i, month in enumerate(months, 1):
        if month in str_date:
            return i
    return None

germany_2019['grant_month'] = germany_2019['grant_date'].apply(get_month)
germany_2019_second_half = germany_2019[germany_2019['grant_month'] >= 7]

print('Germany patents (second half 2019):', len(germany_2019_second_half))

if len(germany_2019_second_half) > 0:
    print('Sample grant dates:')
    for date in germany_2019_second_half['grant_date'].head(10):
        print('  ', date)
    
    print('\nSample CPC data:')
    for cpc in germany_2019_second_half['cpc'].head(3):
        print('  ', cpc)

result_data = {
    'total_patents': len(df),
    'germany_2019_patents': len(germany_2019),
    'germany_2019_second_half': len(germany_2019_second_half),
    'sample_dates': germany_2019_second_half['grant_date'].head(5).tolist() if len(germany_2019_second_half) > 0 else []
}

print('__RESULT__:')
print(json.dumps(result_data))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
