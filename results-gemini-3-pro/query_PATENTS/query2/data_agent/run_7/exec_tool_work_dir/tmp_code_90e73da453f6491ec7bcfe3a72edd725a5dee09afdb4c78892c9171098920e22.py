code = """import json
import pandas as pd
import re
from datetime import datetime

file_path = locals()['var_function-call-5965053505380751305']
with open(file_path, 'r') as f:
    data = json.load(f)

def parse_date(date_str):
    if not date_str: return None
    # Manual cleanup
    # Remove stopwords
    stopwords = {'dated', 'on', 'the', 'of'}
    parts = date_str.replace(',', ' ').split()
    cleaned_parts = [p for p in parts if p.lower() not in stopwords]
    clean = ' '.join(cleaned_parts)
    
    # Remove ordinals: 12th -> 12
    # simple regex with correct backref
    clean = re.sub(r'(\d+)(st|nd|rd|th)', r'\g<1>', clean, flags=re.IGNORECASE)
    
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

filtered_filings = []

for entry in data:
    # 1. Filter Country: Germany
    p_info = entry.get('Patents_info', '')
    if 'DE-' not in p_info and 'Germany' not in p_info and 'DE' not in p_info.split():
        continue
    
    # 2. Filter Grant Date: H2 2019
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
    # Class is first 3 chars (e.g. C01)
    cpc_json = entry.get('cpc', '[]')
    try:
        cpcs = json.loads(cpc_json)
    except:
        continue
        
    classes = set()
    for c in cpcs:
        code = c.get('code', '')
        if len(code) >= 3:
            classes.add(code[:3])
            
    for cls in classes:
        filtered_filings.append({'year': year, 'cpc': cls})

df = pd.DataFrame(filtered_filings)

if df.empty:
    print('__RESULT__:')
    print('[]')
else:
    # EMA Calculation
    # We need to cover the range of years present in the filtered set?
    # Or should we look at the entire history if available?
    # The query implies "highest ... each year"
    # I'll use the range of filing years found in the dataset.
    
    min_year = int(df['year'].min())
    max_year = int(df['year'].max())
    all_years = range(min_year, max_year + 1)
    
    # Count filings
    counts = df.groupby(['cpc', 'year']).size().reset_index(name='count')
    
    ema_data = []
    
    unique_cpcs = df['cpc'].unique()
    
    for cpc in unique_cpcs:
        cpc_counts = counts[counts['cpc'] == cpc].set_index('year')['count']
        
        ema = 0
        first = True
        
        # We iterate through all years to maintain EMA state
        # Assume 0 count for missing years
        cpc_series = []
        for y in all_years:
            val = cpc_counts.get(y, 0)
            if first:
                # Initialize EMA with first value (even if 0)
                ema = val
                first = False
            else:
                ema = 0.1 * val + 0.9 * ema
            
            cpc_series.append({'year': y, 'cpc': cpc, 'ema': ema})
        
        ema_data.extend(cpc_series)
        
    ema_df = pd.DataFrame(ema_data)
    
    # Find winner for each year
    # "highest ... each year"
    winners = {} # cpc -> best_year (personal)
    
    for y in all_years:
        year_slice = ema_df[ema_df['year'] == y]
        if year_slice.empty: continue
        
        # Max EMA in this year
        max_val = year_slice['ema'].max()
        if max_val == 0: continue # Ignore 0s
        
        # Get CPCs with this max
        top_cpcs = year_slice[year_slice['ema'] == max_val]['cpc'].tolist()
        
        for tc in top_cpcs:
            if tc not in winners:
                winners[tc] = None # Will find best year later
                
    # Now for each winner, find their personal best year (max EMA)
    final_list = []
    for w in winners.keys():
        w_df = ema_df[ema_df['cpc'] == w]
        best_row = w_df.loc[w_df['ema'].idxmax()]
        final_list.append({
            'cpc_group_code': w,
            'best_year': int(best_row['year']),
            'max_ema': float(best_row['ema'])
        })
        
    print('__RESULT__:')
    print(json.dumps(final_list))"""

env_args = {'var_function-call-18028440708686650123': [{'symbol': 'A01K2227/108', 'level': '9.0', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'level': '9.0', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'level': '9.0', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'level': '9.0', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'level': '9.0', 'titleFull': 'Ovine'}], 'var_function-call-14121556978734837448': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-9930715917777594238': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}], 'var_function-call-6217904583302428661': 'file_storage/function-call-6217904583302428661.json', 'var_function-call-14928006443128475187': [{'symbol': 'C01B', 'level': '5.0', 'titleFull': 'NON-METALLIC ELEMENTS; COMPOUNDS THEREOF; METALLOIDS OR COMPOUNDS THEREOF NOT COVERED BY SUBCLASS C01C'}], 'var_function-call-372215383101891581': [{'symbol': 'C01', 'level': '4.0', 'titleFull': 'INORGANIC CHEMISTRY'}], 'var_function-call-5965053505380751305': 'file_storage/function-call-5965053505380751305.json', 'var_function-call-14590075051570926846': [], 'var_function-call-9474592491575834864': {'total': 4833, 'german_count': 70, 'h2_2019_count': 0, 'both_count': 0, 'sample_dates': ['14th Mar 2019', 'Mar 19th, 2019', 'Mar 12th, 2019', '2019 on Jul 12th', 'on March 14th, 2019']}, 'var_function-call-15869300767040837747': {'2019 on Jul 12th': 'Failed: 2019 on Jul \x01', '14th Mar 2019': 'Failed: \x01 Mar 2019', 'Mar 19th, 2019': 'Failed: Mar \x01 2019', 'dated 6th October 2020': 'Failed: dated \x01 October 2020', '21st of September, 2021': 'Failed: \x01 of September 2021'}}

exec(code, env_args)
