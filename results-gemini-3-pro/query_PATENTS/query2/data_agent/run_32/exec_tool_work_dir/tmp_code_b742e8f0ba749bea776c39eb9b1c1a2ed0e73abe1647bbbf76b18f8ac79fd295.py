code = """import json
import pandas as pd

# Load files
cpc_def_path = locals()['var_function-call-11140997319825556287']
patents_path = locals()['var_function-call-11140997319825559318']

with open(cpc_def_path, 'r') as f:
    cpc_defs = json.load(f)
cpc_titles = {item['symbol']: item['titleFull'] for item in cpc_defs}

with open(patents_path, 'r') as f:
    patents = json.load(f)

processed_data = []
debug_counts = {"total": len(patents), "germany_match": 0, "date_match": 0}

for p in patents:
    # Broad Germany Filter
    p_info = p.get('Patents_info', '').lower()
    # Check for "germany", "from de", " de ", "de-"
    if "germany" in p_info or "from de" in p_info or " de " in p_info or "de-" in p_info:
        debug_counts["germany_match"] += 1
    else:
        continue
        
    # Date Filter
    g_date_str = p.get('grant_date', '')
    try:
        g_date = pd.to_datetime(g_date_str)
        if (pd.Timestamp('2019-07-01') <= g_date <= pd.Timestamp('2019-12-31')):
            debug_counts["date_match"] += 1
        else:
            continue
    except:
        continue

    # Filing Year
    f_date_str = p.get('filing_date', '')
    try:
        f_date = pd.to_datetime(f_date_str)
        f_year = f_date.year
    except:
        continue

    # CPC
    cpc_json = p.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_json)
        codes = set()
        for item in cpc_list:
            code = item.get('code', '')
            if len(code) >= 3:
                codes.add(code[:3]) # Level 4 (Class)
        
        for code in codes:
            processed_data.append({'cpc': code, 'year': f_year})
    except:
        continue

df = pd.DataFrame(processed_data)

results_list = []
if not df.empty:
    cpc_groups = df.groupby('cpc')
    for cpc, group in cpc_groups:
        counts = group['year'].value_counts().sort_index()
        if counts.empty: continue
        
        min_year = counts.index.min()
        max_year = counts.index.max()
        full_range = range(min_year, max_year + 1)
        counts = counts.reindex(full_range, fill_value=0)
        
        ema = counts.ewm(alpha=0.1, adjust=False).mean()
        
        results_list.append({
            'cpc_code': cpc,
            'title': cpc_titles.get(cpc, "Unknown Title"),
            'max_ema': round(ema.max(), 2),
            'best_year': int(ema.idxmax())
        })

    results_list.sort(key=lambda x: x['max_ema'], reverse=True)

# Output with debug info to understand if data volume is the issue
output = {
    "debug": debug_counts,
    "top_results": results_list[:5]
}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_function-call-13481503473468098040': 'file_storage/function-call-13481503473468098040.json', 'var_function-call-15031019168239807513': ['cpc_definition'], 'var_function-call-15031019168239805256': [{'Patents_info': 'In AT, the patent filing (application no. AT-52022-U) is assigned to ST Extruded Products Germany GmbH and has publication no. AT-17758-U1.', 'filing_date': 'dated 26th January 2022', 'grant_date': 'None Date', 'cpc': '[\n  {\n    "code": "E06B1/702",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'Application (no. AU-2006246481-A) from AU, belonging to KAO GERMANY GMBH, with pub. number AU-2006246481-B2.', 'filing_date': 'November the 30th, 2006', 'grant_date': 'September the 6th, 2012', 'cpc': '[\n  {\n    "code": "A61Q5/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K8/355",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61Q5/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K8/355",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'TRELLEBORG AUTOMOTIVE GERMANY holds the PL patent application (number PL-07728345-T), with publication no. PL-2010798-T3.', 'filing_date': '2007 on Apr 20th', 'grant_date': 'None Date', 'cpc': '[\n  {\n    "code": "F16F13/14",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16F13/20",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16F13/14",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16F13/20",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_function-call-11140997319825556287': 'file_storage/function-call-11140997319825556287.json', 'var_function-call-11140997319825559318': 'file_storage/function-call-11140997319825559318.json', 'var_function-call-18035538944869836830': [{'symbol': 'H04', 'level': '4.0', 'titleFull': 'ELECTRIC COMMUNICATION TECHNIQUE'}, {'symbol': 'H04W72/04', 'level': '8.0', 'titleFull': 'Wireless resource allocation'}, {'symbol': 'H04W', 'level': '5.0', 'titleFull': 'WIRELESS COMMUNICATION NETWORKS'}], 'var_function-call-1325232302467222021': [{'cpc_code': 'A61', 'title': 'MEDICAL OR VETERINARY SCIENCE; HYGIENE', 'max_ema': 2.0, 'best_year': 2016}, {'cpc_code': 'G01', 'title': 'MEASURING; TESTING', 'max_ema': 1.1, 'best_year': 2018}, {'cpc_code': 'A21', 'title': 'BAKING; EDIBLE DOUGHS', 'max_ema': 1.0, 'best_year': 2015}, {'cpc_code': 'A43', 'title': 'FOOTWEAR', 'max_ema': 1.0, 'best_year': 2016}, {'cpc_code': 'A47', 'title': 'FURNITURE; DOMESTIC ARTICLES OR APPLIANCES; COFFEE MILLS; SPICE MILLS; SUCTION CLEANERS IN GENERAL', 'max_ema': 1.0, 'best_year': 2015}, {'cpc_code': 'B29', 'title': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL', 'max_ema': 1.0, 'best_year': 2007}, {'cpc_code': 'B60', 'title': 'VEHICLES IN GENERAL', 'max_ema': 1.0, 'best_year': 2013}, {'cpc_code': 'B62', 'title': 'LAND VEHICLES FOR TRAVELLING OTHERWISE THAN ON RAILS', 'max_ema': 1.0, 'best_year': 2010}, {'cpc_code': 'B63', 'title': 'SHIPS OR OTHER WATERBORNE VESSELS; RELATED EQUIPMENT', 'max_ema': 1.0, 'best_year': 2014}, {'cpc_code': 'B64', 'title': 'AIRCRAFT; AVIATION; COSMONAUTICS', 'max_ema': 1.0, 'best_year': 2018}]}

exec(code, env_args)
