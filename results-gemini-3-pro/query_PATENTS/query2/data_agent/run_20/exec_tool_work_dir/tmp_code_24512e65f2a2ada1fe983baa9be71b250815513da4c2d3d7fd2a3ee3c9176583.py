code = """import json
import pandas as pd
import re
import datetime

# Load data
with open(locals()['var_function-call-5077132125135892078'], 'r') as f:
    data = json.load(f)

# Date cleaning function
def parse_date(date_str):
    if not date_str:
        return None
    # Remove ordinal suffixes and filler words
    s = date_str.lower()
    s = re.sub(r'(st|nd|rd|th)', '', s)
    s = re.sub(r'\b(on|dated|of|the)\b', '', s)
    s = re.sub(r'[,]', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    try:
        return pd.to_datetime(s)
    except:
        return None

# Process records
records = []
for entry in data:
    g_date = parse_date(entry.get('grant_date'))
    f_date = parse_date(entry.get('filing_date'))
    
    # Filter Grant Date: 2019 H2 (July 1 - Dec 31)
    if g_date is None:
        continue
    if not (datetime.datetime(2019, 7, 1) <= g_date <= datetime.datetime(2019, 12, 31)):
        continue
    
    # Check Country (already filtered by SQL but double check)
    if 'DE patent filing' not in entry.get('Patents_info', ''):
        continue

    # Extract Filing Year
    if f_date is None:
        continue
    year = f_date.year
    
    # Extract CPC Level 4
    cpc_json = entry.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_json)
    except:
        continue
        
    codes = set()
    for item in cpc_list:
        code = item.get('code', '')
        if len(code) >= 3:
            # Level 4 is usually the first 3 chars (e.g. A23) based on previous check
            l4_code = code[:3]
            codes.add(l4_code)
    
    for code in codes:
        records.append({'cpc': code, 'year': year})

# Create DataFrame
df = pd.DataFrame(records)

if df.empty:
    print("__RESULT__:")
    print(json.dumps([]))
else:
    # Group by CPC and Year
    counts = df.groupby(['cpc', 'year']).size().reset_index(name='count')
    
    # Calculate EMA
    # We need a continuous range of years for each CPC to properly calculate EMA?
    # Or just iterate through the sorted existing years?
    # EMA is time-dependent. Gaps should probably be treated as 0.
    # Let's pivot to fill gaps.
    pivot = counts.pivot(index='year', columns='cpc', values='count').fillna(0)
    
    # Sort years
    pivot = pivot.sort_index()
    
    ema_results = {} # cpc -> {'max_ema': val, 'best_year': y}
    
    alpha = 0.1
    
    for col in pivot.columns:
        series = pivot[col]
        # Calculate EMA
        # Start EMA with the first value? Or 0?
        # Usually EMA starts with the first observation.
        # But if the series starts with 0s?
        # Let's iterate.
        ema = 0
        max_ema = -1
        best_year = None
        
        # We should start calculation from the first year in the pivot?
        # Yes.
        for year, val in series.items():
            # For the very first point of the series (globally), usually EMA_0 = val_0
            # But here we iterate through the dataframe index.
            # Let's assume EMA initialized at 0 before the first year of data? 
            # Or EMA_t = alpha*val + (1-alpha)*prev_EMA.
            # If prev_EMA is not set, set it to val?
            # Standard pandas ewm: adjust=False means y0=x0?
            pass
            
        # Using pandas ewm
        # min_periods=0?
        # adjust=False: y_t = (1-alpha)y_{t-1} + alpha*x_t. 
        # This matches the user formula `EMA_t = 0.1 * Count + (1-0.1) * EMA_{t-1}` implies alpha=0.1.
        # But pandas ewm definition for alpha: y_t = (1-alpha)y_{t-1} + alpha*x_t.
        # So pandas alpha=0.1 matches.
        
        ema_series = series.ewm(alpha=0.1, adjust=False).mean()
        
        # Find max
        mx = ema_series.max()
        idxmax = ema_series.idxmax()
        
        ema_results[col] = {'max_ema': mx, 'best_year': int(idxmax)}

    # Sort by max_ema
    sorted_res = sorted(ema_results.items(), key=lambda x: x[1]['max_ema'], reverse=True)
    
    # Top 10
    top_10 = sorted_res[:10]
    
    # Prepare output list of codes to query
    output = []
    for cpc, info in top_10:
        output.append({'cpc': cpc, 'best_year': info['best_year'], 'max_ema': info['max_ema']})
        
    print("__RESULT__:")
    print(json.dumps(output))"""

env_args = {'var_function-call-4980740479115432120': 'file_storage/function-call-4980740479115432120.json', 'var_function-call-885587414874800350': [{'Patents_info': 'VITTORI GIANFRANCO DE holds the FR patent filing (app. number FR-7811408-A), with publication number FR-2388575-B3.'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.'}, {'Patents_info': 'MITUTOYO CORP holds the DE patent filing (app. number DE-10037981-A), with pub. number DE-10037981-B4.'}], 'var_function-call-885587414874803867': [{'symbol': 'A01K2227/108', 'level': '9.0', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'level': '9.0', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'level': '9.0', 'titleFull': 'Bovine'}], 'var_function-call-4189893605340898872': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-4189893605340900237': 'file_storage/function-call-4189893605340900237.json', 'var_function-call-13165109459917276818': [{'symbol': 'A', 'level': '2.0', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'A23', 'level': '4.0', 'titleFull': 'FOODS OR FOODSTUFFS; TREATMENT THEREOF, NOT COVERED BY OTHER CLASSES'}, {'symbol': 'A23N', 'level': '5.0', 'titleFull': 'MACHINES OR APPARATUS FOR TREATING HARVESTED FRUIT, VEGETABLES OR FLOWER BULBS IN BULK, NOT OTHERWISE PROVIDED FOR; PEELING VEGETABLES OR FRUIT IN BULK; APPARATUS FOR PREPARING ANIMAL FEEDING- STUFFS'}, {'symbol': 'A23N12/00', 'level': '7.0', 'titleFull': 'Machines for cleaning, blanching, drying or roasting fruits or vegetables, e.g. coffee, cocoa, nuts'}, {'symbol': 'A23N12/10', 'level': '9.0', 'titleFull': 'Rotary roasters'}], 'var_function-call-5077132125135892078': 'file_storage/function-call-5077132125135892078.json'}

exec(code, env_args)
