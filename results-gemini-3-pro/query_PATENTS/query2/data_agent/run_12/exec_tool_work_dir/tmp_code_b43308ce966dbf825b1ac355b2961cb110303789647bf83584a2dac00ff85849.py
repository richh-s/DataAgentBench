code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-6414003164698615798'], 'r') as f:
    raw_data = json.load(f)

# Helper to parse date
def parse_date(date_str):
    try:
        # Remove "dated", "on", "the", etc.
        clean = re.sub(r'(dated|on|the|of|,)', '', date_str, flags=re.IGNORECASE)
        clean = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', clean) # 14th -> 14
        clean = " ".join(clean.split())
        return pd.to_datetime(clean)
    except:
        return None

# Filter and Process
filtered_filings = []

for row in raw_data:
    # 1. Filter Country: Germany
    # Check Patents_info for DE
    p_info = row.get('Patents_info', '')
    # Pattern: DE followed by number or space, or "from DE"
    if not (re.search(r'\bDE[- ]', p_info) or re.search(r'\bfrom DE\b', p_info) or re.search(r'\bIn DE\b', p_info) or "Germany" in p_info):
        continue
        
    # 2. Filter Grant Date: H2 2019
    g_date_str = row.get('grant_date', '')
    g_date = parse_date(g_date_str)
    if g_date is None:
        continue
    if not (g_date.year == 2019 and g_date.month >= 7):
        continue
        
    # 3. Get Filing Year
    f_date_str = row.get('filing_date', '')
    f_date = parse_date(f_date_str)
    if f_date is None:
        continue
    f_year = f_date.year
    
    # 4. Extract CPC Level 4 (First 3 chars)
    cpc_json = row.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_json)
        # Extract codes, take first 3 chars
        codes = set()
        for entry in cpc_list:
            code = entry.get('code', '')
            if len(code) >= 3:
                codes.add(code[:3]) # Level 4 (Class)
        
        for c in codes:
            filtered_filings.append({'cpc': c, 'year': f_year})
            
    except:
        continue

df = pd.DataFrame(filtered_filings)

# Calculate EMA
results = []
if not df.empty:
    # Count per CPC per Year
    counts = df.groupby(['cpc', 'year']).size().reset_index(name='count')
    
    # Get range of years
    all_years = range(counts['year'].min(), counts['year'].max() + 1)
    
    unique_cpcs = counts['cpc'].unique()
    
    ema_data = [] # (cpc, year, ema)
    
    for cpc in unique_cpcs:
        cpc_counts = counts[counts['cpc'] == cpc].set_index('year')['count']
        # Reindex to fill missing years with 0
        cpc_series = cpc_counts.reindex(all_years, fill_value=0)
        
        # Calculate EMA
        # First value is just the count
        ema_vals = []
        prev_ema = None
        alpha = 0.1
        
        for y in all_years:
            val = cpc_series[y]
            if prev_ema is None:
                ema = val # Start with first value
            else:
                ema = (val * alpha) + (prev_ema * (1 - alpha))
            ema_vals.append({'cpc': cpc, 'year': y, 'ema': ema})
            prev_ema = ema
            
        ema_data.extend(ema_vals)
        
    ema_df = pd.DataFrame(ema_data)
    
    # Find CPC with Highest EMA each year
    winners = {} # Year -> {cpc, ema}
    for y in all_years:
        year_data = ema_df[ema_df['year'] == y]
        if not year_data.empty:
            top = year_data.sort_values('ema', ascending=False).iloc[0]
            winners[y] = {'cpc': top['cpc'], 'ema': top['ema']}
            
    # Collect unique winner CPCs and their "Best Year" (global max EMA)
    final_cpcs = {}
    winner_codes = set(v['cpc'] for v in winners.values())
    
    for cpc in winner_codes:
        # Get all data for this CPC
        cpc_stats = ema_df[ema_df['cpc'] == cpc]
        # Find best year
        best_stat = cpc_stats.sort_values('ema', ascending=False).iloc[0]
        final_cpcs[cpc] = {
            'cpc': cpc,
            'best_year': int(best_stat['year']),
            'max_ema': float(best_stat['ema'])
        }
        
    print("__RESULT__:")
    print(json.dumps(list(final_cpcs.values())))
else:
    print("__RESULT__:")
    print("[]")"""

env_args = {'var_function-call-1868465921641692363': 'file_storage/function-call-1868465921641692363.json', 'var_function-call-6414003164698615067': [{'symbol': 'A01K2227/108', 'level': '9.0', 'titleFull': 'Swine'}], 'var_function-call-6414003164698615798': 'file_storage/function-call-6414003164698615798.json', 'var_function-call-4244802832919163477': [{'symbol': 'A', 'level': '2.0', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'A01', 'level': '4.0', 'titleFull': 'AGRICULTURE; FORESTRY; ANIMAL HUSBANDRY; HUNTING; TRAPPING; FISHING'}, {'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'G06F', 'level': '5.0', 'titleFull': 'ELECTRIC DIGITAL DATA PROCESSING'}, {'symbol': 'A01B1/00', 'level': '7.0', 'titleFull': 'Hand tools'}, {'symbol': 'G06F9/00', 'level': '7.0', 'titleFull': 'Arrangements for program control, e.g. control units'}], 'var_function-call-14093412893191991109': []}

exec(code, env_args)
