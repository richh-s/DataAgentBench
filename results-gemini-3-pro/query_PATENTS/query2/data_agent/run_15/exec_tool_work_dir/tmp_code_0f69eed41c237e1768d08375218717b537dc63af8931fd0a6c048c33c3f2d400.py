code = """import json
import pandas as pd
from dateutil import parser
import datetime

# Load data
with open(locals()['var_function-call-14995722181694731292'], 'r') as f:
    patents = json.load(f)
with open(locals()['var_function-call-17555163745562188786'], 'r') as f:
    definitions = json.load(f)

# Definitions map
cpc_titles = {item['symbol']: item['titleFull'] for item in definitions}

target_cpcs = set()
filing_data = []

# Date filtering range
start_date = datetime.datetime(2019, 7, 1)
end_date = datetime.datetime(2019, 12, 31)

for p in patents:
    # Parse grant date
    g_str = p.get('grant_date')
    g_date = None
    if g_str:
        try:
            g_date = parser.parse(g_str)
        except:
            pass
    
    is_target = False
    if g_date and start_date <= g_date <= end_date:
        is_target = True
    
    # Parse filing date
    f_str = p.get('filing_date')
    year = None
    if f_str:
        try:
            f_date = parser.parse(f_str)
            year = f_date.year
        except:
            pass
            
    if year is None:
        continue
    
    # Parse CPC
    try:
        cpcs = json.loads(p.get('cpc', '[]'))
    except:
        continue
        
    p_codes = set()
    for item in cpcs:
        code = item.get('code', '')
        if len(code) >= 3:
            l4 = code[:3]
            # Verify if it is a Level 4 class (in definitions)
            if l4 in cpc_titles:
                p_codes.add(l4)
    
    if is_target:
        target_cpcs.update(p_codes)
    
    for c in p_codes:
        filing_data.append({'year': year, 'cpc': c})

# Filter filing data
filtered_filing_data = [x for x in filing_data if x['cpc'] in target_cpcs]

if not filtered_filing_data:
    print("__RESULT__:")
    print(json.dumps("No data found for the specified criteria."))
else:
    df = pd.DataFrame(filtered_filing_data)
    # Count per year
    counts = df.groupby(['cpc', 'year']).size().reset_index(name='count')
    
    results = []
    alpha = 0.1
    
    for cpc in target_cpcs:
        c_df = counts[counts['cpc'] == cpc].sort_values('year')
        if c_df.empty:
            continue
        
        min_y = int(c_df['year'].min())
        max_y = int(c_df['year'].max())
        all_years = pd.DataFrame({'year': range(min_y, max_y + 1)})
        c_df = pd.merge(all_years, c_df, on='year', how='left').fillna({'count': 0})
        c_df['cpc'] = cpc # Fill cpc column
        
        # Calculate EMA
        ema_values = []
        prev_ema = None
        for cnt in c_df['count']:
            if prev_ema is None:
                ema = float(cnt)
            else:
                ema = alpha * float(cnt) + (1 - alpha) * prev_ema
            ema_values.append(ema)
            prev_ema = ema
        
        c_df['ema'] = ema_values
        
        best_idx = c_df['ema'].idxmax()
        best_row = c_df.loc[best_idx]
        
        results.append({
            'Full Title': cpc_titles.get(cpc),
            'CPC Group Code': cpc,
            'Best Year': int(best_row['year']),
            'Max EMA': best_row['ema']
        })
    
    # Sort
    results.sort(key=lambda x: x['Max EMA'], reverse=True)
    
    print("__RESULT__:")
    print(json.dumps(results, indent=2))"""

env_args = {'var_function-call-214723707077387799': 'file_storage/function-call-214723707077387799.json', 'var_function-call-18252369469336044559': 'file_storage/function-call-18252369469336044559.json', 'var_function-call-9445320778325029841': [{'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.'}, {'Patents_info': 'In DE, the patent application (no. DE-10130631-A) is owned by SCHNEIDER SIEGHARD and has publication number DE-10130631-B4.'}, {'Patents_info': 'The DE patent application (no. DE-10134061-A) is belonging to MOSMATIC AG NECKER and has publication number DE-10134061-B4.'}, {'Patents_info': 'In DE, the patent application (no. DE-10147111-A) is belonging to VISTEON GLOBAL TECH INC and has publication number DE-10147111-B4.'}], 'var_function-call-11463893853230926505': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-1971227252066381487': [{'symbol': 'A', 'level': '2.0'}, {'symbol': 'B', 'level': '2.0'}, {'symbol': 'C', 'level': '2.0'}, {'symbol': 'D', 'level': '2.0'}, {'symbol': 'E', 'level': '2.0'}, {'symbol': 'F', 'level': '2.0'}, {'symbol': 'G', 'level': '2.0'}, {'symbol': 'H', 'level': '2.0'}, {'symbol': 'Y', 'level': '2.0'}, {'symbol': 'A01', 'level': '4.0'}], 'var_function-call-12459689083035061514': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01B59/00', 'level': '7.0'}, {'symbol': 'A01B19/00', 'level': '7.0'}, {'symbol': 'A01B35/00', 'level': '7.0'}, {'symbol': 'A01B13/00', 'level': '7.0'}], 'var_function-call-17555163745562188786': 'file_storage/function-call-17555163745562188786.json', 'var_function-call-14995722181694731292': 'file_storage/function-call-14995722181694731292.json'}

exec(code, env_args)
