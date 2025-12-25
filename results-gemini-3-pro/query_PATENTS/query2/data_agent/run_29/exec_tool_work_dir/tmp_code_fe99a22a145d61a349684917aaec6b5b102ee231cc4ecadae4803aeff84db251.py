code = """import pandas as pd
import json
import re

# Load Patents
with open(locals()['var_function-call-17191090704288552271'], 'r') as f:
    patents = json.load(f)

# Load Definitions
with open(locals()['var_function-call-2972541637893720550'], 'r') as f:
    definitions = json.load(f)

# Create lookup for definitions
level4_map = {d['symbol']: d['titleFull'] for d in definitions}

# Process Patents
records = []
for p in patents:
    # Check Grant Date: 2nd half of 2019
    g_date = p.get('grant_date', '')
    if not g_date:
        continue
    
    # Check year 2019
    if '2019' not in g_date:
        continue
    
    # Check month (July-Dec)
    g_date_lower = g_date.lower()
    months_h2 = ['july', 'august', 'september', 'october', 'november', 'december', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    is_h2 = any(m in g_date_lower for m in months_h2)
    
    if not is_h2:
        continue

    # Get Filing Year
    f_date = p.get('filing_date', '')
    f_year = None
    years = re.findall(r'\d{4}', f_date)
    if years:
        f_year = int(years[0])
    
    if not f_year:
        continue
        
    # Get CPCs
    try:
        cpc_raw = p.get('cpc', '[]')
        if not cpc_raw:
            cpc_list = []
        else:
            cpc_list = json.loads(cpc_raw)
    except:
        cpc_list = []
        
    seen_symbols = set()
    for item in cpc_list:
        code = item.get('code', '')
        if len(code) >= 3:
            symbol = code[:3]
            if symbol in level4_map:
                seen_symbols.add(symbol)
    
    for s in seen_symbols:
        records.append({'symbol': s, 'filing_year': f_year})

if not records:
    print("__RESULT__:")
    print(json.dumps([]))
else:
    # Aggregate
    df = pd.DataFrame(records)
    counts = df.groupby(['symbol', 'filing_year']).size().reset_index(name='count')

    # Calculate EMA
    results = []
    alpha = 0.1

    for symbol, group in counts.groupby('symbol'):
        group = group.sort_values('filing_year')
        min_year = group['filing_year'].min()
        max_year = group['filing_year'].max()
        
        # Create full range
        all_years = pd.DataFrame({'filing_year': range(min_year, max_year + 1)})
        merged = pd.merge(all_years, group, on='filing_year', how='left').fillna(0)
        
        # Calculate EMA
        # Using pandas ewm with adjust=False matches the standard definition: 
        # EMA_t = alpha * x_t + (1-alpha) * EMA_{t-1}
        merged['ema'] = merged['count'].ewm(alpha=alpha, adjust=False).mean()
        
        # Find best year
        best_row = merged.loc[merged['ema'].idxmax()]
        best_year = int(best_row['filing_year'])
        max_ema = best_row['ema']
        
        results.append({
            'cpc_group_code': symbol,
            'full_title': level4_map[symbol],
            'best_year': best_year,
            'max_ema': max_ema
        })

    # Sort by max_ema descending
    results.sort(key=lambda x: x['max_ema'], reverse=True)

    # Return top results. 
    # If the list is short (<20), return all. Else top 10.
    if len(results) < 20:
        output = results
    else:
        output = results[:10]

    print("__RESULT__:")
    print(json.dumps(output))"""

env_args = {'var_function-call-9660806304682991333': ['publicationinfo'], 'var_function-call-1089113106838788780': 'file_storage/function-call-1089113106838788780.json', 'var_function-call-13127744617519299197': [{'Patents_info': 'Patent application (number DE-10317286-A) from DE, belonging to NICOLAY VERWALTUNGS GMBH, with publication no. DE-10317286-B3.'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.'}, {'Patents_info': 'In DE, the patent filing (application no. DE-102009032362-A) is owned by MARTOR KG and has pub. number DE-102009032362-B3.'}], 'var_function-call-15407584031614680749': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-16490565579124031269': [{'symbol': 'B04', 'level': '4.0'}, {'symbol': 'B04B', 'level': '5.0'}, {'symbol': 'B04C', 'level': '5.0'}, {'symbol': 'B04C11/00', 'level': '7.0'}, {'symbol': 'B04B3/00', 'level': '7.0'}, {'symbol': 'B04B5/00', 'level': '7.0'}, {'symbol': 'B04B15/00', 'level': '7.0'}, {'symbol': 'B04B13/00', 'level': '7.0'}, {'symbol': 'B04B7/00', 'level': '7.0'}, {'symbol': 'B04B9/00', 'level': '7.0'}, {'symbol': 'B04B1/00', 'level': '7.0'}, {'symbol': 'B04B11/00', 'level': '7.0'}, {'symbol': 'B04C9/00', 'level': '7.0'}, {'symbol': 'B04C7/00', 'level': '7.0'}, {'symbol': 'B04C3/00', 'level': '7.0'}, {'symbol': 'B04C5/00', 'level': '7.0'}, {'symbol': 'B04C1/00', 'level': '7.0'}, {'symbol': 'B04B1/04', 'level': '8.0'}, {'symbol': 'B04B1/02', 'level': '8.0'}, {'symbol': 'B04B1/20', 'level': '8.0'}, {'symbol': 'B04B3/04', 'level': '8.0'}, {'symbol': 'B04B3/02', 'level': '8.0'}, {'symbol': 'B04B3/06', 'level': '8.0'}, {'symbol': 'B04B3/08', 'level': '8.0'}, {'symbol': 'B04B5/04', 'level': '8.0'}, {'symbol': 'B04B5/10', 'level': '8.0'}, {'symbol': 'B04B5/08', 'level': '8.0'}, {'symbol': 'B04B5/06', 'level': '8.0'}, {'symbol': 'B04B5/005', 'level': '8.0'}, {'symbol': 'B04B5/02', 'level': '8.0'}, {'symbol': 'B04B2007/005', 'level': '8.0'}, {'symbol': 'B04B7/08', 'level': '8.0'}, {'symbol': 'B04B1/10', 'level': '8.0'}, {'symbol': 'B04B9/08', 'level': '8.0'}, {'symbol': 'B04B9/02', 'level': '8.0'}, {'symbol': 'B04B9/06', 'level': '8.0'}, {'symbol': 'B04B9/12', 'level': '8.0'}, {'symbol': 'B04B9/14', 'level': '8.0'}, {'symbol': 'B04B9/10', 'level': '8.0'}, {'symbol': 'B04C2003/006', 'level': '8.0'}, {'symbol': 'B04C3/06', 'level': '8.0'}, {'symbol': 'B04C3/04', 'level': '8.0'}, {'symbol': 'B04C3/02', 'level': '8.0'}, {'symbol': 'B04C2003/003', 'level': '8.0'}, {'symbol': 'B04C5/20', 'level': '8.0'}, {'symbol': 'B04C5/24', 'level': '8.0'}, {'symbol': 'B04C5/22', 'level': '8.0'}, {'symbol': 'B04C5/14', 'level': '8.0'}, {'symbol': 'B04C5/08', 'level': '8.0'}, {'symbol': 'B04C5/02', 'level': '8.0'}, {'symbol': 'B04C5/12', 'level': '8.0'}, {'symbol': 'B04C2009/005', 'level': '8.0'}, {'symbol': 'B04C2009/008', 'level': '8.0'}, {'symbol': 'B04C2009/004', 'level': '8.0'}, {'symbol': 'B04C2009/001', 'level': '8.0'}, {'symbol': 'B04C2009/002', 'level': '8.0'}, {'symbol': 'B04C2009/007', 'level': '8.0'}, {'symbol': 'B04B7/02', 'level': '8.0'}, {'symbol': 'B04B5/12', 'level': '8.0'}, {'symbol': 'B04B11/04', 'level': '8.0'}, {'symbol': 'B04B11/08', 'level': '8.0'}, {'symbol': 'B04B11/06', 'level': '8.0'}, {'symbol': 'B04B11/02', 'level': '8.0'}, {'symbol': 'B04B13/003', 'level': '8.0'}, {'symbol': 'B04B2013/006', 'level': '8.0'}, {'symbol': 'B04B15/12', 'level': '8.0'}, {'symbol': 'B04B15/06', 'level': '8.0'}, {'symbol': 'B04B15/08', 'level': '8.0'}, {'symbol': 'B04B15/04', 'level': '8.0'}, {'symbol': 'B04B15/10', 'level': '8.0'}, {'symbol': 'B04B15/02', 'level': '8.0'}, {'symbol': 'B04C5/087', 'level': '9.0'}, {'symbol': 'B04B1/06', 'level': '9.0'}, {'symbol': 'B04B1/08', 'level': '9.0'}, {'symbol': 'B04B1/14', 'level': '9.0'}, {'symbol': 'B04B1/12', 'level': '9.0'}, {'symbol': 'B04B2001/2066', 'level': '9.0'}, {'symbol': 'B04B2001/2091', 'level': '9.0'}, {'symbol': 'B04B1/2008', 'level': '9.0'}, {'symbol': 'B04B2001/2058', 'level': '9.0'}, {'symbol': 'B04B2001/2083', 'level': '9.0'}, {'symbol': 'B04B2001/2041', 'level': '9.0'}, {'symbol': 'B04B1/2016', 'level': '9.0'}, {'symbol': 'B04B2001/205', 'level': '9.0'}, {'symbol': 'B04B2001/2075', 'level': '9.0'}, {'symbol': 'B04B2001/2033', 'level': '9.0'}, {'symbol': 'B04B3/025', 'level': '9.0'}, {'symbol': 'B04B5/0442', 'level': '9.0'}, {'symbol': 'B04B5/0407', 'level': '9.0'}, {'symbol': 'B04B2005/105', 'level': '9.0'}, {'symbol': 'B04B2005/125', 'level': '9.0'}, {'symbol': 'B04B7/06', 'level': '9.0'}, {'symbol': 'B04B7/04', 'level': '9.0'}, {'symbol': 'B04B2007/025', 'level': '9.0'}, {'symbol': 'B04B7/12', 'level': '9.0'}, {'symbol': 'B04B7/10', 'level': '9.0'}, {'symbol': 'B04B7/085', 'level': '9.0'}, {'symbol': 'B04B7/18', 'level': '9.0'}, {'symbol': 'B04B9/04', 'level': '9.0'}, {'symbol': 'B04B2009/085', 'level': '9.0'}, {'symbol': 'B04B2009/143', 'level': '9.0'}, {'symbol': 'B04B9/146', 'level': '9.0'}, {'symbol': 'B04C5/04', 'level': '9.0'}, {'symbol': 'B04C5/06', 'level': '9.0'}, {'symbol': 'B04C5/10', 'level': '9.0'}, {'symbol': 'B04C5/085', 'level': '9.0'}, {'symbol': 'B04C5/081', 'level': '9.0'}, {'symbol': 'B04C5/103', 'level': '9.0'}, {'symbol': 'B04C5/107', 'level': '9.0'}, {'symbol': 'B04C5/13', 'level': '9.0'}, {'symbol': 'B04C5/185', 'level': '9.0'}, {'symbol': 'B04C5/15', 'level': '9.0'}, {'symbol': 'B04C5/18', 'level': '9.0'}, {'symbol': 'B04C5/181', 'level': '9.0'}, {'symbol': 'B04C5/16', 'level': '9.0'}, {'symbol': 'B04C5/23', 'level': '9.0'}, {'symbol': 'B04C5/30', 'level': '9.0'}, {'symbol': 'B04C5/28', 'level': '9.0'}, {'symbol': 'B04C5/26', 'level': '9.0'}, {'symbol': 'B04B2011/046', 'level': '9.0'}, {'symbol': 'B04B11/05', 'level': '9.0'}, {'symbol': 'B04B2011/086', 'level': '9.0'}, {'symbol': 'B04B2011/084', 'level': '9.0'}, {'symbol': 'B04B11/082', 'level': '9.0'}, {'symbol': 'B04B2011/088', 'level': '9.0'}, {'symbol': 'B04B11/043', 'level': '9.0'}, {'symbol': 'B04B2007/065', 'level': '10.0'}, {'symbol': 'B04B7/16', 'level': '10.0'}, {'symbol': 'B04B7/14', 'level': '10.0'}, {'symbol': 'B04C2005/133', 'level': '10.0'}, {'symbol': 'B04C2005/136', 'level': '10.0'}, {'symbol': 'B04C5/187', 'level': '10.0'}, {'symbol': 'B04B2001/2025', 'level': '10.0'}, {'symbol': 'B04B2005/0435', 'level': '10.0'}, {'symbol': 'B04B5/0414', 'level': '10.0'}, {'symbol': 'B04B5/0428', 'level': '10.0'}, {'symbol': 'B04B2005/0457', 'level': '10.0'}, {'symbol': 'B04B2005/0471', 'level': '10.0'}, {'symbol': 'B04B2005/0464', 'level': '10.0'}, {'symbol': 'B04B2005/0478', 'level': '10.0'}, {'symbol': 'B04B2005/0492', 'level': '10.0'}, {'symbol': 'B04B2005/0485', 'level': '10.0'}, {'symbol': 'B04B2005/045', 'level': '10.0'}, {'symbol': 'B04B1/16', 'level': '10.0'}, {'symbol': 'B04B1/18', 'level': '11.0'}, {'symbol': 'B04B5/0421', 'level': '11.0'}], 'var_function-call-5803491515521878686': [{'symbol': 'B99'}, {'symbol': 'B29'}, {'symbol': 'B33'}, {'symbol': 'C22'}, {'symbol': 'D99'}, {'symbol': 'F28'}, {'symbol': 'A45'}, {'symbol': 'A24'}, {'symbol': 'A61'}, {'symbol': 'A63'}, {'symbol': 'A22'}, {'symbol': 'A42'}, {'symbol': 'A99'}, {'symbol': 'A43'}, {'symbol': 'A01'}, {'symbol': 'A62'}, {'symbol': 'A23'}, {'symbol': 'A47'}, {'symbol': 'A46'}, {'symbol': 'A44'}], 'var_function-call-17191090704288552271': 'file_storage/function-call-17191090704288552271.json', 'var_function-call-2972541637893720550': 'file_storage/function-call-2972541637893720550.json'}

exec(code, env_args)
