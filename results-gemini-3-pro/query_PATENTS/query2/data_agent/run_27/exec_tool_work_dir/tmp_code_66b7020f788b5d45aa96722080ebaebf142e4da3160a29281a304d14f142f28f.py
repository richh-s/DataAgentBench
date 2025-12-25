code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-15606792083185834976'], 'r') as f:
    data = json.load(f)

# Date parser
month_map = {
    'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
    'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12,
    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12,
    'Sept': 9
}

def parse_date(date_str):
    if not date_str:
        return None
    # Find year (4 digits)
    year_match = re.search(r'\d{4}', date_str)
    if not year_match:
        return None
    year = int(year_match.group(0))
    
    # Find month
    month = None
    for m_name, m_val in month_map.items():
        if m_name in date_str:
            month = m_val
            break
    
    if month is None:
        return None
        
    return pd.Timestamp(year=year, month=month, day=1)

# Process data
valid_records = []
for entry in data:
    # Filter by Grant Date (H2 2019: July to Dec)
    g_date = parse_date(entry.get('grant_date', ''))
    if not g_date:
        continue
    if g_date.year != 2019 or g_date.month < 7:
        continue
        
    # Filter by Germany (already filtered by SQL mostly, but double check)
    # The SQL used LIKE '%DE-%' which is quite specific to German patent numbers.
    # So we assume it's fine.
    
    # Parse Filing Date
    f_date = parse_date(entry.get('filing_date', ''))
    if not f_date:
        continue
    filing_year = f_date.year
    
    # Extract CPCs
    try:
        cpc_list = json.loads(entry.get('cpc', '[]'))
    except:
        continue
        
    cpc_codes = set()
    for cpc in cpc_list:
        code = cpc.get('code', '')
        if len(code) >= 3:
            # Level 4 code (Class)
            l4_code = code[:3]
            cpc_codes.add(l4_code)
            
    for code in cpc_codes:
        valid_records.append({'year': filing_year, 'cpc': code})

df = pd.DataFrame(valid_records)

if df.empty:
    print('__RESULT__:')
    print('[]')
else:
    # Count filings per year per CPC
    counts = df.groupby(['year', 'cpc']).size().reset_index(name='count')
    
    # Pivot to create time series
    # We want a continuous range of years?
    # The EMA depends on history.
    # We should consider all years present in the data.
    pivot_df = counts.pivot(index='year', columns='cpc', values='count').fillna(0)
    
    # Sort index
    pivot_df = pivot_df.sort_index()
    
    # Calculate EMA
    # Pandas ewm: alpha=0.1, adjust=False (matches recursive definition EMA_t = alpha*x + (1-alpha)*EMA_{t-1})
    ema_df = pivot_df.ewm(alpha=0.1, adjust=False).mean()
    
    # Find max CPC for each year
    results = []
    # Identify unique CPCs that are top in any year
    top_cpcs = set()
    
    yearly_winners = []
    for year in ema_df.index:
        # Get the row
        row = ema_df.loc[year]
        # Find max
        best_cpc = row.idxmax()
        max_val = row.max()
        yearly_winners.append({'year': int(year), 'cpc': best_cpc, 'ema': max_val})
        top_cpcs.add(best_cpc)
        
    # For each top CPC, find its best year (max EMA overall)
    cpc_best_years = {}
    for cpc in top_cpcs:
        # Get the series for this CPC
        series = ema_df[cpc]
        best_y = series.idxmax()
        best_v = series.max()
        cpc_best_years[cpc] = int(best_y)
        
    final_output = {
        'yearly_winners': yearly_winners,
        'cpc_best_years': cpc_best_years,
        'unique_cpcs': list(top_cpcs)
    }
    
    print('__RESULT__:')
    print(json.dumps(final_output))"""

env_args = {'var_function-call-1199938574274535269': 'file_storage/function-call-1199938574274535269.json', 'var_function-call-2446296467746717570': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-2588780312602812612': [{'symbol': 'H04L2025/03496', 'level': '16.0'}, {'symbol': 'H04L2025/0349', 'level': '16.0'}, {'symbol': 'H04L2025/03503', 'level': '16.0'}, {'symbol': 'H04Q2213/161', 'level': '8.0'}, {'symbol': 'H04Q2213/281', 'level': '8.0'}, {'symbol': 'H04Q2213/292', 'level': '8.0'}, {'symbol': 'H04', 'level': '4.0'}, {'symbol': 'H04Q2213/296', 'level': '8.0'}, {'symbol': 'H04Q2213/299', 'level': '8.0'}, {'symbol': 'H04Q2213/34', 'level': '8.0'}], 'var_function-call-1690403253581886321': [{'symbol': 'H04W', 'level': '5.0'}], 'var_function-call-3298910611970813522': [{'len': '3', 'cnt': '137'}], 'var_function-call-7172290236493635481': [{'Patents_info': 'In AT, the patent filing (application no. AT-52022-U) is assigned to ST Extruded Products Germany GmbH and has publication no. AT-17758-U1.', 'cpc': '[\n  {\n    "code": "E06B1/702",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'Application (no. AU-2006246481-A) from AU, belonging to KAO GERMANY GMBH, with pub. number AU-2006246481-B2.', 'cpc': '[\n  {\n    "code": "A61Q5/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K8/355",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61Q5/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K8/355",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'TRELLEBORG AUTOMOTIVE GERMANY holds the PL patent application (number PL-07728345-T), with publication no. PL-2010798-T3.', 'cpc': '[\n  {\n    "code": "F16F13/14",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16F13/20",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16F13/14",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16F13/20",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DE application (number DE-102008034343-A) is assigned to CONTINENTAL MECH COMPONENTS GERMANY GMBH and has pub. number DE-102008034343-B4.', 'cpc': '[\n  {\n    "code": "F01D25/16",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02C6/12",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F05D2220/40",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02B37/18",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F01D25/12",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F05D2240/51",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F05D2260/232",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02T10/12",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'Patents_info': 'In EP, the application (ID EP-18829350-A) is belonging to MEYER BURGER GERMANY GMBH and has pub. number EP-3729486-C0.', 'cpc': '[\n  {\n    "code": "H01J37/32724",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01J37/32522",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01J37/32724",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01J37/32522",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02E60/10",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01J37/32724",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01J37/32522",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01L23/427",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_function-call-15606792083185834976': 'file_storage/function-call-15606792083185834976.json'}

exec(code, env_args)
