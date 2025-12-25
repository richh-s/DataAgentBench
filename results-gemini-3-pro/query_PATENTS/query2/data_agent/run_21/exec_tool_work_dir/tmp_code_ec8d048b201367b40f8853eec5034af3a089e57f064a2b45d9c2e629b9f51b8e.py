code = """import json
import pandas as pd
import re
import datetime

# Load data
with open(locals()['var_function-call-511248593719389968'], 'r') as f:
    records = json.load(f)

# Date parser
month_map = {
    'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
    'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
}

def parse_date_str(s):
    if not s:
        return None
    s = s.lower()
    # Extract year
    year_match = re.search(r'\d{4}', s)
    if not year_match:
        return None
    year = int(year_match.group(0))
    
    # Extract month
    month = 0
    for m_name, m_val in month_map.items():
        if m_name in s:
            month = m_val
            break
    if month == 0:
        return None # Can't determine H2 without month
    
    # We don't strictly need day for H2 check if month is known
    # H2 is July (7) to Dec (12).
    return datetime.date(year, month, 1)

def is_h2_2019(d):
    if d is None:
        return False
    return d.year == 2019 and d.month >= 7

# Process
cpc_filing_data = []

for rec in records:
    g_date = parse_date_str(rec['grant_date'])
    if not is_h2_2019(g_date):
        continue
        
    f_date = parse_date_str(rec['filing_date'])
    if not f_date:
        continue
    f_year = f_date.year
    
    # Process CPC
    try:
        cpcs = json.loads(rec['cpc'])
    except:
        continue
        
    # Extract Level 4 codes (first 3 chars)
    # Use a set to avoid double counting same class in one patent?
    # Usually counting "filings" means 1 filing counts for the class.
    # If a patent has multiple codes in A01, it counts as 1 filing for A01.
    
    classes = set()
    for item in cpcs:
        code = item.get('code', '')
        if len(code) >= 3:
            classes.add(code[:3])
            
    for cls in classes:
        cpc_filing_data.append({'code': cls, 'year': f_year})

df = pd.DataFrame(cpc_filing_data)

# Calculate EMA
results = []
alpha = 0.1

if not df.empty:
    # Group by code
    grouped = df.groupby('code')
    
    for code, group_df in grouped:
        # Count filings per year
        yearly_counts = group_df.groupby('year').size().sort_index()
        
        # Reindex to fill missing years?
        # If we want EMA over time, gaps should probably be 0.
        # Range from min year to max year.
        if yearly_counts.empty:
            continue
            
        full_idx = range(yearly_counts.index.min(), yearly_counts.index.max() + 1)
        yearly_counts = yearly_counts.reindex(full_idx, fill_value=0)
        
        # Calculate EMA
        # Pandas ewm: adjust=False corresponds to: y_t = alpha * x_t + (1-alpha) * y_{t-1}
        # But we need to check initialization. 
        # Pandas ewm with adjust=False takes the first value as the starting EMA.
        ema = yearly_counts.ewm(alpha=alpha, adjust=False).mean()
        
        # Find max EMA and corresponding year
        max_ema = ema.max()
        best_year = ema.idxmax()
        
        results.append({
            'symbol': code,
            'max_ema': max_ema,
            'best_year': int(best_year)
        })

# Sort by max_ema desc
results.sort(key=lambda x: x['max_ema'], reverse=True)

# Print result structure
print("__RESULT__:")
print(json.dumps(results[:50])) # Limit to top 50 to avoid huge output"""

env_args = {'var_function-call-7552569785716595056': 'file_storage/function-call-7552569785716595056.json', 'var_function-call-7552569785716594767': [{'symbol': 'A01K2227/108', 'level': '9.0', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'level': '9.0', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'level': '9.0', 'titleFull': 'Bovine'}], 'var_function-call-192039731568297242': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-3194235214395417911': [{'symbol': 'B', 'level': '2.0', 'titleFull': 'PERFORMING OPERATIONS; TRANSPORTING'}, {'symbol': 'H', 'level': '2.0', 'titleFull': 'ELECTRICITY'}, {'symbol': 'Y', 'level': '2.0', 'titleFull': 'GENERAL TAGGING OF NEW TECHNOLOGICAL DEVELOPMENTS; GENERAL TAGGING OF CROSS-SECTIONAL TECHNOLOGIES SPANNING OVER SEVERAL SECTIONS OF THE IPC; TECHNICAL SUBJECTS COVERED BY FORMER USPC CROSS-REFERENCE ART COLLECTIONS [XRACs] AND DIGESTS'}, {'symbol': 'D', 'level': '2.0', 'titleFull': 'TEXTILES; PAPER'}, {'symbol': 'F', 'level': '2.0', 'titleFull': 'MECHANICAL ENGINEERING; LIGHTING; HEATING; WEAPONS; BLASTING'}, {'symbol': 'E', 'level': '2.0', 'titleFull': 'FIXED CONSTRUCTIONS'}, {'symbol': 'C', 'level': '2.0', 'titleFull': 'CHEMISTRY; METALLURGY'}, {'symbol': 'G', 'level': '2.0', 'titleFull': 'PHYSICS'}, {'symbol': 'A', 'level': '2.0', 'titleFull': 'HUMAN NECESSITIES'}], 'var_function-call-15323268024429165824': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}], 'var_function-call-4924233972547621931': [{'level': '2.0', 'cnt': '9'}, {'level': '4.0', 'cnt': '137'}, {'level': '5.0', 'cnt': '677'}, {'level': '7.0', 'cnt': '9816'}, {'level': '8.0', 'cnt': '48384'}, {'level': '9.0', 'cnt': '70250'}, {'level': '10.0', 'cnt': '62585'}, {'level': '11.0', 'cnt': '35084'}, {'level': '12.0', 'cnt': '17632'}, {'level': '13.0', 'cnt': '8015'}, {'level': '14.0', 'cnt': '3649'}, {'level': '15.0', 'cnt': '1521'}, {'level': '16.0', 'cnt': '1223'}, {'level': '17.0', 'cnt': '720'}, {'level': '18.0', 'cnt': '485'}, {'level': '19.0', 'cnt': '621'}], 'var_function-call-511248593719389968': 'file_storage/function-call-511248593719389968.json'}

exec(code, env_args)
