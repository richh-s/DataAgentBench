code = """import json
import re
import pandas as pd

file_path = locals()['var_function-call-6422516106666611400']
with open(file_path, 'r') as f:
    data = json.load(f)

records = []
# Find any 4 digits
year_pattern = re.compile(r'\d{4}')

for row in data:
    f_date = row.get('filing_date')
    cpc_json = row.get('cpc')
    
    if not f_date or not cpc_json:
        continue
        
    # Extract Year
    matches = year_pattern.findall(f_date)
    year = None
    for m in matches:
        y = int(m)
        if 1900 <= y <= 2025: # Reasonable range
            year = y
            break
            
    if year is None:
        continue
    
    # Extract CPC codes
    try:
        cpc_list = json.loads(cpc_json)
    except:
        continue
        
    if not isinstance(cpc_list, list):
        continue
        
    subclasses = set()
    for item in cpc_list:
        code = item.get('code', '')
        # Subclass is first 4 chars, e.g., A01B
        if len(code) >= 4:
            subclasses.add(code[:4])
            
    for sc in subclasses:
        records.append({'subclass': sc, 'year': year})

df = pd.DataFrame(records)

if df.empty:
    print("__RESULT__:")
    print("[]")
else:
    # Group and aggregate
    counts = df.groupby(['subclass', 'year']).size().reset_index(name='count')
    
    min_year = counts['year'].min()
    max_year = counts['year'].max()
    all_years = range(min_year, max_year + 1)
    
    pivot_df = counts.pivot(index='year', columns='subclass', values='count').fillna(0).reindex(all_years, fill_value=0)
    
    ema_df = pivot_df.ewm(alpha=0.2, adjust=False).mean()
    
    # Best year
    best_years = ema_df.idxmax()
    
    # Filter best year == 2022
    target_subclasses = best_years[best_years == 2022].index.tolist()
    
    # Sort for consistency
    target_subclasses.sort()
    
    print("__RESULT__:")
    print(json.dumps(target_subclasses))"""

env_args = {'var_function-call-6487159229108555457': 'file_storage/function-call-6487159229108555457.json', 'var_function-call-6487159229108553280': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}], 'var_function-call-4451239759330927851': [{'symbol': 'A01B1/00', 'level': '7.0'}, {'symbol': 'A', 'level': '2.0'}, {'symbol': 'A01', 'level': '4.0'}, {'symbol': 'A01B', 'level': '5.0'}], 'var_function-call-3552584556167493191': [{'count(*)': '277813'}], 'var_function-call-16984543996015765041': [], 'var_function-call-6422516106666611400': 'file_storage/function-call-6422516106666611400.json', 'var_function-call-2770072839738424115': [], 'var_function-call-12092359954613502708': {'stats': 'Empty', 'sample_dates': [['dated 5th March 2019', None], ['March the 18th, 2019', None], ['29th March 2019', None], ['on March 29th, 2019', None], ['2nd April 2019', None]]}}

exec(code, env_args)
