code = """import json
import pandas as pd
import re

# Load CPC Definitions (Level 4)
cpc_def_path = locals()['var_function-call-11140997319825556287']
with open(cpc_def_path, 'r') as f:
    cpc_defs = json.load(f)
    
# Create a dictionary for CPC Title lookup
cpc_titles = {item['symbol']: item['titleFull'] for item in cpc_defs}

# Load Patent Data
patents_path = locals()['var_function-call-11140997319825559318']
with open(patents_path, 'r') as f:
    patents = json.load(f)

print(f"Total patents loaded: {len(patents)}")

# Filter and Process Patents
processed_data = []

for p in patents:
    # 1. Filter for Germany
    # Checking for "from DE" or "DE-" in Patents_info as a proxy for German jurisdiction
    p_info = p.get('Patents_info', '')
    if "from DE" not in p_info and "DE-" not in p_info:
        continue
        
    # 2. Filter Grant Date (H2 2019: July 1 - Dec 31)
    g_date_str = p.get('grant_date', '')
    try:
        g_date = pd.to_datetime(g_date_str)
        if not (pd.Timestamp('2019-07-01') <= g_date <= pd.Timestamp('2019-12-31')):
            continue
    except:
        continue
        
    # 3. Extract Filing Year
    f_date_str = p.get('filing_date', '')
    try:
        f_date = pd.to_datetime(f_date_str)
        f_year = f_date.year
    except:
        continue
        
    # 4. Extract CPC Level 4 (Class - first 3 chars)
    cpc_json = p.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_json)
        # Get unique Level 4 codes for this patent
        codes = set()
        for item in cpc_list:
            code = item.get('code', '')
            if len(code) >= 3:
                codes.add(code[:3])
        
        for code in codes:
            processed_data.append({'cpc': code, 'year': f_year})
            
    except:
        continue

df = pd.DataFrame(processed_data)
print(f"Filtered rows (cpc-year pairs): {len(df)}")

if len(df) == 0:
    print("__RESULT__:")
    print("[]")
else:
    # Calculate EMA per CPC
    results = []
    
    # Get range of years to ensure continuity? 
    # The EMA should be calculated on the sequence of years available or continuous?
    # Usually EMA is time-series. We should fill missing years with 0 if we want a true timeline, 
    # or just use the years present?
    # "EMA of patent filings each year" implies a time series.
    # I will construct a full range of years from min to max for each CPC.
    
    # Group by CPC
    cpc_groups = df.groupby('cpc')
    
    for cpc, group in cpc_groups:
        # Count filings per year
        counts = group['year'].value_counts().sort_index()
        
        if counts.empty:
            continue
            
        min_year = counts.index.min()
        max_year = counts.index.max()
        
        # Reindex to fill missing years with 0
        full_range = range(min_year, max_year + 1)
        counts = counts.reindex(full_range, fill_value=0)
        
        # Calculate EMA
        # Pandas ewm: alpha=0.1, adjust=False (matches typical recursive definition)
        # adjust=False: y_t = (1-alpha)*y_{t-1} + alpha*x_t
        # Note: The user said "smoothing factor 0.1". 
        # Pandas ewm(alpha=0.1).mean() calculates this.
        ema = counts.ewm(alpha=0.1, adjust=False).mean()
        
        # Find Max EMA and Best Year
        max_ema = ema.max()
        best_year = ema.idxmax()
        
        results.append({
            'cpc_code': cpc,
            'title': cpc_titles.get(cpc, "Unknown Title"),
            'max_ema': max_ema,
            'best_year': int(best_year)
        })
        
    # Sort by max_ema descending
    results.sort(key=lambda x: x['max_ema'], reverse=True)
    
    # Take top 10 for display
    top_results = results[:10]
    
    print("__RESULT__:")
    print(json.dumps(top_results))"""

env_args = {'var_function-call-13481503473468098040': 'file_storage/function-call-13481503473468098040.json', 'var_function-call-15031019168239807513': ['cpc_definition'], 'var_function-call-15031019168239805256': [{'Patents_info': 'In AT, the patent filing (application no. AT-52022-U) is assigned to ST Extruded Products Germany GmbH and has publication no. AT-17758-U1.', 'filing_date': 'dated 26th January 2022', 'grant_date': 'None Date', 'cpc': '[\n  {\n    "code": "E06B1/702",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'Application (no. AU-2006246481-A) from AU, belonging to KAO GERMANY GMBH, with pub. number AU-2006246481-B2.', 'filing_date': 'November the 30th, 2006', 'grant_date': 'September the 6th, 2012', 'cpc': '[\n  {\n    "code": "A61Q5/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K8/355",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61Q5/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K8/355",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'TRELLEBORG AUTOMOTIVE GERMANY holds the PL patent application (number PL-07728345-T), with publication no. PL-2010798-T3.', 'filing_date': '2007 on Apr 20th', 'grant_date': 'None Date', 'cpc': '[\n  {\n    "code": "F16F13/14",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16F13/20",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16F13/14",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16F13/20",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_function-call-11140997319825556287': 'file_storage/function-call-11140997319825556287.json', 'var_function-call-11140997319825559318': 'file_storage/function-call-11140997319825559318.json', 'var_function-call-18035538944869836830': [{'symbol': 'H04', 'level': '4.0', 'titleFull': 'ELECTRIC COMMUNICATION TECHNIQUE'}, {'symbol': 'H04W72/04', 'level': '8.0', 'titleFull': 'Wireless resource allocation'}, {'symbol': 'H04W', 'level': '5.0', 'titleFull': 'WIRELESS COMMUNICATION NETWORKS'}]}

exec(code, env_args)
