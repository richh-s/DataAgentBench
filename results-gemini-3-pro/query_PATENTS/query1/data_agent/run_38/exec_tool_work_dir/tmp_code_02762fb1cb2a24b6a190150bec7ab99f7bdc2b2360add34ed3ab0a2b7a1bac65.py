code = """import json
import re
import pandas as pd

try:
    with open(locals()['var_function-call-11252670295542494115'], 'r') as f:
        level5_data = json.load(f)
    level5_codes = set(item['symbol'] for item in level5_data)

    with open(locals()['var_function-call-2797324583492744393'], 'r') as f:
        filings_data = json.load(f)

    def extract_year(date_str):
        if not date_str:
            return None
        matches = re.findall(r'(19\d{2}|20\d{2})', str(date_str))
        if matches:
            return int(matches[0])
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
            if isinstance(cpc_json, str):
                cpc_list = json.loads(cpc_json)
            else:
                cpc_list = cpc_json
        except:
            continue
            
        seen_codes = set()
        if isinstance(cpc_list, list):
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

    if not records:
        print("__RESULT__:")
        print("[]")
    else:
        df = pd.DataFrame(records)
        counts = df.groupby(['code', 'year']).size().reset_index(name='count')
        
        min_year = counts['year'].min()
        max_year = counts['year'].max()
        all_years = range(min_year, max_year + 1)
        
        codes = counts['code'].unique()
        results = []
        
        for code in codes:
            code_data = counts[counts['code'] == code].set_index('year').reindex(all_years, fill_value=0)
            code_data['ema'] = code_data['count'].ewm(alpha=0.2, adjust=False).mean()
            best_year = code_data['ema'].idxmax()
            
            if best_year == 2022:
                results.append(code)
        
        results.sort()
        print("__RESULT__:")
        print(json.dumps(results))

except Exception as e:
    print(f"Error: {e}")"""

env_args = {'var_function-call-11252670295542494115': 'file_storage/function-call-11252670295542494115.json', 'var_function-call-11252670295542493418': 'file_storage/function-call-11252670295542493418.json', 'var_function-call-1816704933838744903': [{'count(*)': '277813'}], 'var_function-call-3705720165070456970': [{'level': '4.0', 'symbol': 'B04', 'parents': '[\n  "B"\n]'}, {'level': '4.0', 'symbol': 'B23', 'parents': '[\n  "B"\n]'}, {'level': '4.0', 'symbol': 'B30', 'parents': '[\n  "B"\n]'}, {'level': '4.0', 'symbol': 'B21', 'parents': '[\n  "B"\n]'}, {'level': '4.0', 'symbol': 'B25', 'parents': '[\n  "B"\n]'}], 'var_function-call-2797324583492744393': 'file_storage/function-call-2797324583492744393.json', 'var_function-call-4024176117624834020': [], 'var_function-call-7163784566198070492': {}, 'var_function-call-6373114007726782950': [], 'var_function-call-17660063591044548463': {'2021': 13246, '2022': 11966}, 'var_function-call-338884460349392285': ['Feb 28th, 2022', 'dated 9th March 2022', 'May the 5th, 2022', '29th July 2022', '2022, June 21st'], 'var_function-call-12717044168953259214': ['[\n  {\n    "code": "F16L39/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B01L2200/027",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F16L37/56",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F16L2201/40",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "B01L3/5635",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16L39/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16L37/56",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F16L39/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "B01L2200/027",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "B01L2200/0689",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "B01L2300/0832",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F16L2201/40",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "B01L2200/027",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F16L37/56",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]', '[\n  {\n    "code": "G05D1/0272",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G05D1/0212",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G05D1/0287",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G05D2201/0216",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "G05D1/024",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G05D1/0297",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G05D1/644",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G05D1/0219",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06Q10/047",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B25J13/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G05D1/0272",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G05D1/646",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G05D1/247",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G05D1/69",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G05D1/692",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]', '[\n  {\n    "code": "H02M3/1582",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M8/04567",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M8/04626",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M8/04947",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H02M1/009",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2008/1293",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H02M3/1582",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H02M1/009",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H02M3/1582",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H02M1/009",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02E60/50",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H02M3/1582",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H02M3/33584",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M8/12",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2008/1293",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02E60/50",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M8/04567",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M8/04626",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M8/04947",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2008/1293",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H02M1/009",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'], 'var_function-call-13232737956034933844': {'Feb 28th, 2022': 2022, 'dated 9th March 2022': 2022, 'May the 5th, 2022': 2022, '29th July 2022': 2022, '2022, June 21st': 2022}, 'var_function-call-3509659098298258383': ['A41D', 'A41C', 'A41H', 'A42B', 'A42C', 'A43B', 'A43C', 'A43D', 'A44D', 'A44B']}

exec(code, env_args)
