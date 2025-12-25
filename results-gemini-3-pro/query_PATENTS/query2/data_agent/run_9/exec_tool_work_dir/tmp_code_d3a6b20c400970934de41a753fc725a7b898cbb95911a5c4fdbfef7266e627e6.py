code = """import json
import pandas as pd
import dateutil.parser

# Load patent data
file_path_patents = locals()['var_function-call-9056115891715311579']
with open(file_path_patents, 'r') as f:
    patents = json.load(f)

# Load CPC definitions
file_path_defs = locals()['var_function-call-3105256378493119945']
with open(file_path_defs, 'r') as f:
    cpc_defs = json.load(f)

cpc_map = {item['symbol']: item['titleFull'] for item in cpc_defs}

# Filter patents granted in H2 2019
filtered_patents = []
for p in patents:
    g_date_str = p.get('grant_date')
    if not g_date_str:
        continue
    try:
        g_date = dateutil.parser.parse(g_date_str)
        if 2019 == g_date.year and g_date.month >= 7:
            filtered_patents.append(p)
    except:
        continue

# Extract (CPC, Filing Year)
data = []
for p in filtered_patents:
    f_date_str = p.get('filing_date')
    if not f_date_str:
        continue
    try:
        f_year = dateutil.parser.parse(f_date_str).year
    except:
        continue
    
    cpc_json = p.get('cpc')
    if not cpc_json:
        continue
    try:
        cpc_list = json.loads(cpc_json)
        # Extract unique level 4 codes for this patent
        codes = set()
        for c in cpc_list:
            code = c.get('code', '')
            # Level 4 is usually first 3 chars, e.g., A01
            if len(code) >= 3:
                codes.add(code[:3])
        
        for code in codes:
            data.append({'cpc': code, 'year': f_year})
    except:
        continue

df = pd.DataFrame(data)

if df.empty:
    print('__RESULT__:')
    print(json.dumps([]))
else:
    # Count filings per CPC per year
    counts = df.groupby(['cpc', 'year']).size().reset_index(name='count')
    
    # Global year range
    min_year = df['year'].min()
    max_year = df['year'].max()
    all_years = list(range(min_year, max_year + 1))
    
    results = []
    
    for cpc_code, group in counts.groupby('cpc'):
        # Reindex to full year range
        g = group.set_index('year').reindex(all_years, fill_value=0).sort_index()
        
        # Calculate EMA
        # alpha=0.1
        # Initial value: first observation? Or 0?
        # ewm(adjust=False) uses the first value as the starting EMA.
        # This is reasonable.
        g['ema'] = g['count'].ewm(alpha=0.1, adjust=False).mean()
        
        best_year = g['ema'].idxmax()
        max_ema = g['ema'].max()
        
        title = cpc_map.get(cpc_code, "Unknown")
        
        results.append({
            'cpc_group': cpc_code,
            'full_title': title,
            'best_year': int(best_year),
            'max_ema': float(max_ema)
        })
    
    # Sort by max_ema desc
    results.sort(key=lambda x: x['max_ema'], reverse=True)
    
    print('__RESULT__:')
    print(json.dumps(results[:5]))"""

env_args = {'var_function-call-3211025022715469786': 'file_storage/function-call-3211025022715469786.json', 'var_function-call-13844795097354421459': [{'priority_claim': '[\n  {\n    "application_number": "JP-2016234666-A",\n    "category": "",\n    "filing_date": 20161202,\n    "npl_text": "",\n    "publication_number": "",\n    "type": ""\n  },\n  {\n    "application_number": "JP-2017026210-W",\n    "category": "",\n    "filing_date": 20170720,\n    "npl_text": "",\n    "publication_number": "",\n    "type": ""\n  }\n]'}, {'priority_claim': '[\n  {\n    "application_number": "EP-18000267-A",\n    "category": "",\n    "filing_date": 20180319,\n    "npl_text": "",\n    "publication_number": "",\n    "type": ""\n  }\n]'}, {'priority_claim': '[\n  {\n    "application_number": "US-201916369247-A",\n    "category": "",\n    "filing_date": 20190329,\n    "npl_text": "",\n    "publication_number": "",\n    "type": ""\n  }\n]'}, {'priority_claim': '[\n  {\n    "application_number": "US-201862625150-P",\n    "category": "",\n    "filing_date": 20180201,\n    "npl_text": "",\n    "publication_number": "",\n    "type": ""\n  },\n  {\n    "application_number": "US-2019016351-W",\n    "category": "",\n    "filing_date": 20190201,\n    "npl_text": "",\n    "publication_number": "",\n    "type": ""\n  },\n  {\n    "application_number": "US-201916369879-A",\n    "category": "",\n    "filing_date": 20190329,\n    "npl_text": "",\n    "publication_number": "",\n    "type": ""\n  }\n]'}, {'priority_claim': '[\n  {\n    "application_number": "IN-201821024002-A",\n    "category": "",\n    "filing_date": 20180627,\n    "npl_text": "",\n    "publication_number": "",\n    "type": ""\n  }\n]'}], 'var_function-call-9056115891715311579': 'file_storage/function-call-9056115891715311579.json', 'var_function-call-14991466691147468904': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-13095999218052369809': [{'symbol': 'A', 'level': '2.0'}, {'symbol': 'A01', 'level': '4.0'}, {'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01B1/00', 'level': '7.0'}], 'var_function-call-3105256378493119945': 'file_storage/function-call-3105256378493119945.json'}

exec(code, env_args)
