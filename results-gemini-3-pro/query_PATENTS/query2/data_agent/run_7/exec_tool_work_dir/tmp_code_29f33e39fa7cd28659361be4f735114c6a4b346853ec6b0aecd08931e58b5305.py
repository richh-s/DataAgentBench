code = """import json
import pandas as pd
import re
from datetime import datetime

# Load data
file_path = locals()['var_function-call-5965053505380751305']
with open(file_path, 'r') as f:
    data = json.load(f)

# Helper to parse natural language date
def parse_date(date_str):
    # Formats seen: "3rd August 2021", "dated 5th March 2019", "March the 18th, 2019", "2013, June 17th"
    # "2019 on Jul 12th", "on December 4th, 2017", "Mar 19th, 2019"
    # Clean string: remove "dated", "on", "the", "of"
    clean = re.sub(r'\b(dated|on|the|of)\b', '', date_str, flags=re.IGNORECASE).strip()
    # Remove ordinal suffixes (st, nd, rd, th) attached to numbers
    clean = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', clean)
    # Normalize spaces
    clean = re.sub(r'\s+', ' ', clean).replace(',', '')
    
    # Try formats
    formats = [
        '%d %B %Y', '%B %d %Y', '%Y %B %d', 
        '%d %b %Y', '%b %d %Y', '%Y %b %d'
    ]
    
    for fmt in formats:
        try:
            return datetime.strptime(clean, fmt)
        except ValueError:
            continue
    return None

# Filter and Process
filtered_filings = []

for entry in data:
    # 1. Filter Country: Germany
    # Check for "DE-" in text, or "from DE"
    p_info = entry.get('Patents_info', '')
    # Check for DE publication number pattern or explicit mention
    if 'DE-' not in p_info and 'Germany' not in p_info:
        continue
    # A bit more robust check: Look for "publication number DE-" or "application (no. DE-..."
    if not re.search(r'(publication|application).*DE-', p_info, re.IGNORECASE):
        # Maybe "from DE" is enough?
        if "from DE" not in p_info:
            continue

    # 2. Filter Grant Date: H2 2019 (July 1 - Dec 31)
    g_date = parse_date(entry.get('grant_date', ''))
    if not g_date:
        continue
    if not (g_date.year == 2019 and g_date.month >= 7):
        continue
        
    # 3. Get Filing Year
    f_date = parse_date(entry.get('filing_date', ''))
    if not f_date:
        continue
    year = f_date.year
    
    # 4. Extract CPC Level 4 (Class)
    cpc_json = entry.get('cpc', '[]')
    try:
        cpcs = json.loads(cpc_json)
    except:
        continue
        
    # Get unique classes for this patent
    classes = set()
    for c in cpcs:
        code = c.get('code', '')
        if len(code) >= 3:
            classes.add(code[:3]) # Class level (e.g. C01)
            
    for cls in classes:
        filtered_filings.append({'year': year, 'cpc': cls})

# DataFrame
df = pd.DataFrame(filtered_filings)

if df.empty:
    print('__RESULT__:')
    print('[]')
else:
    # Count filings per CPC per Year
    counts = df.groupby(['cpc', 'year']).size().reset_index(name='count')
    
    # Create full range of years for each CPC?
    # Or just iterate years present in data?
    # EMA requires sequential updates. If a year is missing, count is 0.
    min_year = df['year'].min()
    max_year = df['year'].max()
    all_years = range(min_year, max_year + 1)
    
    ema_results = []
    
    # Process each CPC
    unique_cpcs = df['cpc'].unique()
    
    for cpc in unique_cpcs:
        cpc_data = counts[counts['cpc'] == cpc].set_index('year')['count']
        
        ema = 0
        first = True
        
        # We need to track best year and EMA history
        cpc_ema_history = []
        
        for y in all_years:
            cnt = cpc_data.get(y, 0)
            if first:
                # Initialize with first count (or 0 if not present?)
                # If we start from min_year of ALL data, we treat prior as 0.
                # Standard EMA: if sequence starts at t=0, EMA_0 = X_0.
                ema = cnt
                first = False
            else:
                ema = 0.1 * cnt + 0.9 * ema
            
            cpc_ema_history.append({'year': y, 'cpc': cpc, 'ema': ema})
            
        ema_results.extend(cpc_ema_history)
        
    ema_df = pd.DataFrame(ema_results)
    
    # Find winner each year
    winners = []
    for y in all_years:
        year_data = ema_df[ema_df['year'] == y]
        if not year_data.empty:
            # Find max EMA
            max_row = year_data.loc[year_data['ema'].idxmax()]
            winners.append(max_row['cpc'])
            
    unique_winners = list(set(winners))
    
    # For each winner, find their Best Year (max EMA)
    final_output = []
    for w in unique_winners:
        w_data = ema_df[ema_df['cpc'] == w]
        best_row = w_data.loc[w_data['ema'].idxmax()]
        final_output.append({
            'cpc_code': w, 
            'best_year': int(best_row['year']), 
            'max_ema': best_row['ema']
        })
        
    print('__RESULT__:')
    print(json.dumps(final_output))"""

env_args = {'var_function-call-18028440708686650123': [{'symbol': 'A01K2227/108', 'level': '9.0', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'level': '9.0', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'level': '9.0', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'level': '9.0', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'level': '9.0', 'titleFull': 'Ovine'}], 'var_function-call-14121556978734837448': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-9930715917777594238': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}], 'var_function-call-6217904583302428661': 'file_storage/function-call-6217904583302428661.json', 'var_function-call-14928006443128475187': [{'symbol': 'C01B', 'level': '5.0', 'titleFull': 'NON-METALLIC ELEMENTS; COMPOUNDS THEREOF; METALLOIDS OR COMPOUNDS THEREOF NOT COVERED BY SUBCLASS C01C'}], 'var_function-call-372215383101891581': [{'symbol': 'C01', 'level': '4.0', 'titleFull': 'INORGANIC CHEMISTRY'}], 'var_function-call-5965053505380751305': 'file_storage/function-call-5965053505380751305.json'}

exec(code, env_args)
