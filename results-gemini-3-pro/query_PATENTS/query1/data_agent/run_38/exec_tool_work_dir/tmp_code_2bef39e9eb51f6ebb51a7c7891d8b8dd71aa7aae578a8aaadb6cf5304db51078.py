code = """import json
import re
import pandas as pd

try:
    with open(locals()['var_function-call-11252670295542494115'], 'r') as f:
        level5_data = json.load(f)
    level5_codes = set(item['symbol'] for item in level5_data)
    print(f"Loaded {len(level5_codes)} Level 5 codes.")

    with open(locals()['var_function-call-2797324583492744393'], 'r') as f:
        filings_data = json.load(f)
    print(f"Loaded {len(filings_data)} filing records.")

    def extract_year(date_str):
        if not date_str:
            return None
        match = re.search(r'\b(19|20)\d{2}\b', str(date_str))
        if match:
            return int(match.group(0))
        return None

    records = []

    for entry in filings_data:
        year = extract_year(entry.get('filing_date'))
        if year is None:
            continue
        
        cpc_json = entry.get('cpc')
        if not cpc_json:
            continue
        
        try:
            # cpc field might be a string (JSON) or already a list if the tool handled it? 
            # The preview showed it as a string: "cpc": "[\n ... ]"
            if isinstance(cpc_json, str):
                cpc_list = json.loads(cpc_json)
            else:
                cpc_list = cpc_json
        except Exception as e:
            continue
            
        seen_codes = set()
        for cpc_item in cpc_list:
            if not isinstance(cpc_item, dict):
                continue
            code = cpc_item.get('code', '')
            if len(code) >= 4:
                subclass = code[:4]
                if subclass in level5_codes:
                    seen_codes.add(subclass)
        
        for c in seen_codes:
            records.append({'year': year, 'code': c})

    print(f"Extracted {len(records)} records.")
    
    if not records:
        print("__RESULT__:")
        print("[]")
    else:
        df = pd.DataFrame(records)
        print("DataFrame head:")
        print(df.head())
        
        counts = df.groupby(['code', 'year']).size().reset_index(name='count')
        
        min_year = counts['year'].min()
        max_year = counts['year'].max()
        all_years = range(min_year, max_year + 1)
        
        codes = counts['code'].unique()
        results = []
        
        for code in codes:
            # Reindex to handle missing years with 0
            code_data = counts[counts['code'] == code].set_index('year').reindex(all_years, fill_value=0)
            
            # EMA
            code_data['ema'] = code_data['count'].ewm(alpha=0.2, adjust=False).mean()
            
            best_year = code_data['ema'].idxmax()
            
            if best_year == 2022:
                results.append(code)
        
        results.sort()
        print("__RESULT__:")
        print(json.dumps(results))

except Exception as e:
    print(f"Error: {e}")"""

env_args = {'var_function-call-11252670295542494115': 'file_storage/function-call-11252670295542494115.json', 'var_function-call-11252670295542493418': 'file_storage/function-call-11252670295542493418.json', 'var_function-call-1816704933838744903': [{'count(*)': '277813'}], 'var_function-call-3705720165070456970': [{'level': '4.0', 'symbol': 'B04', 'parents': '[\n  "B"\n]'}, {'level': '4.0', 'symbol': 'B23', 'parents': '[\n  "B"\n]'}, {'level': '4.0', 'symbol': 'B30', 'parents': '[\n  "B"\n]'}, {'level': '4.0', 'symbol': 'B21', 'parents': '[\n  "B"\n]'}, {'level': '4.0', 'symbol': 'B25', 'parents': '[\n  "B"\n]'}], 'var_function-call-2797324583492744393': 'file_storage/function-call-2797324583492744393.json'}

exec(code, env_args)
