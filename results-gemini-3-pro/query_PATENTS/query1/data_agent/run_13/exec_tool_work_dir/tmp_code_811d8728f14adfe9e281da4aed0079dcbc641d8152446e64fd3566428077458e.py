code = """import json
import pandas as pd
import re

# Load patent data
with open(locals()['var_function-call-10323089701006148132'], 'r') as f:
    data = json.load(f)

# Load Level 5 symbols
with open(locals()['var_function-call-8221742485339181695'], 'r') as f:
    level5_data = json.load(f)
    level5_symbols = set(item['symbol'] for item in level5_data)

# Process data
records = []
for entry in data:
    f_date = entry.get('filing_date', '')
    cpc_json = entry.get('cpc', '[]')
    
    # Extract year
    match = re.search(r'(19|20)\d{2}', f_date)
    if match:
        year = int(match.group(0))
    else:
        continue
    
    # Parse CPC
    try:
        cpc_list = json.loads(cpc_json)
        # Extract codes and truncate to 4 chars (Level 5)
        codes = [item['code'][:4] for item in cpc_list if 'code' in item and len(item['code']) >= 4]
        for code in codes:
            # Only consider codes that are actually in the level 5 list (valid subclasses)
            if code in level5_symbols:
                records.append({'year': year, 'cpc': code})
    except:
        continue

df = pd.DataFrame(records)

if not df.empty:
    # Count per year per CPC (Level 5)
    counts = df.groupby(['cpc', 'year']).size().reset_index(name='count')
    
    # Get full range of years
    min_year = df['year'].min()
    max_year = df['year'].max()
    all_years = range(min_year, max_year + 1)
    
    # Pivot
    pivot_df = counts.pivot(index='cpc', columns='year', values='count').fillna(0)
    pivot_df = pivot_df.reindex(columns=all_years, fill_value=0)
    
    # Calculate EMA
    # alpha = 0.2
    # DataFrame.ewm(alpha=0.2, adjust=False).mean()
    ema_df = pivot_df.T.ewm(alpha=0.2, adjust=False).mean().T
    
    # Find best year
    best_years = ema_df.idxmax(axis=1)
    
    # Filter for best year == 2022
    target_cpc = best_years[best_years == 2022].index.tolist()
    
    print("__RESULT__:")
    print(json.dumps(target_cpc))
else:
    print("__RESULT__:")
    print("[]")"""

env_args = {'var_function-call-15599228345113843070': 'file_storage/function-call-15599228345113843070.json', 'var_function-call-10323089701006148132': 'file_storage/function-call-10323089701006148132.json', 'var_function-call-17650219595098056405': 'file_storage/function-call-17650219595098056405.json', 'var_function-call-8221742485339181695': 'file_storage/function-call-8221742485339181695.json', 'var_function-call-6913022513822000697': [{'level': '2.0', 'example': 'A'}, {'level': '4.0', 'example': 'A01'}, {'level': '5.0', 'example': 'A01B'}, {'level': '7.0', 'example': 'A01B1/00'}, {'level': '8.0', 'example': 'A01B1/02'}, {'level': '9.0', 'example': 'A01B1/022'}, {'level': '10.0', 'example': 'A01B1/225'}, {'level': '11.0', 'example': 'A01B3/421'}, {'level': '12.0', 'example': 'A01B3/4215'}, {'level': '13.0', 'example': 'A01D2034/6843'}, {'level': '14.0', 'example': 'A01D2034/6825'}, {'level': '15.0', 'example': 'A47J31/4446'}, {'level': '16.0', 'example': 'A61B17/7028'}, {'level': '17.0', 'example': 'A61K47/6823'}, {'level': '18.0', 'example': 'G01N2333/96444'}, {'level': '19.0', 'example': 'H01L21/32137'}]}

exec(code, env_args)
