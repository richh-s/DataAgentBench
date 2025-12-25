code = """import json
import re
import pandas as pd
from datetime import datetime

# Load data
with open(locals()['var_function-call-14453105091914346968'], 'r') as f:
    data = json.load(f)

# Helper to parse dates
month_map = {
    'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
    'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
}

def parse_date(date_str):
    if not date_str:
        return None
    date_str = date_str.lower()
    # Extract year
    year_match = re.search(r'\d{4}', date_str)
    if not year_match:
        return None
    year = int(year_match.group(0))
    
    # Extract month
    month = 1 # Default
    for m_str, m_int in month_map.items():
        if m_str in date_str:
            month = m_int
            break
    
    # Extract day (optional, but good for filtering 2nd half)
    # Looking for digits that are not the year
    # This is tricky. simpler to just check month for 2nd half.
    # But day is needed for exact "July 1st" boundary.
    # regex for day: digit followed by st, nd, rd, th or just space/punctuation, not part of year
    # Simplification: if month > 7, it's 2nd half. If month == 7, need day.
    # If month < 7, not 2nd half.
    # Let's try to find a day.
    day = 1
    # Remove year from string to avoid confusion
    rem_str = date_str.replace(str(year), '')
    day_match = re.search(r'(\d{1,2})(st|nd|rd|th)?', rem_str)
    if day_match:
        day = int(day_match.group(1))
        
    return datetime(year, month, day)

# Step 1: Filter patents granted in 2nd half of 2019 (July 1 - Dec 31)
# And extract Target CPCs
target_cpcs = set()
start_date = datetime(2019, 7, 1)
end_date = datetime(2019, 12, 31)

filtered_patents = []

for record in data:
    g_date = parse_date(record.get('grant_date', ''))
    if g_date and start_date <= g_date <= end_date:
        # Check for Germany in Patents_info?
        # The query already filtered for "Germany" in SQL.
        # But let's double check if Patents_info indicates Germany context to be safe?
        # The SQL query was: Patents_info LIKE '%Germany%' OR ...
        # So all records here are relevant to Germany.
        
        # Extract CPCs
        cpc_json = record.get('cpc', '[]')
        try:
            cpcs = json.loads(cpc_json)
            for cpc in cpcs:
                code = cpc.get('code', '')
                if len(code) >= 3:
                    level4 = code[:3] # First 3 chars
                    target_cpcs.add(level4)
        except:
            pass

# Step 2: Build filing history for Target CPCs using ALL data
# We need counts per year for each target_cpc.
filing_history = {cpc: {} for cpc in target_cpcs} # {cpc: {year: count}}

for record in data:
    f_date = parse_date(record.get('filing_date', ''))
    if f_date:
        year = f_date.year
        cpc_json = record.get('cpc', '[]')
        try:
            cpcs = json.loads(cpc_json)
            # A patent might have multiple codes.
            # If a patent has code C01B and C01C, it counts for both C01 (if C01 is target).
            # But duplicate codes for same level 4 group in one patent should count as 1?
            # Usually "filings" refers to number of patents filed.
            # So if a patent falls into C01 category, it contributes 1 to C01 count for that year.
            
            patent_cats = set()
            for cpc in cpcs:
                code = cpc.get('code', '')
                if len(code) >= 3:
                    level4 = code[:3]
                    if level4 in target_cpcs:
                        patent_cats.add(level4)
            
            for cat in patent_cats:
                filing_history[cat][year] = filing_history[cat].get(year, 0) + 1
        except:
            pass

# Step 3: Calculate EMA
results = []
for cpc, history in filing_history.items():
    if not history:
        continue
    
    # Create continuous year range
    min_year = min(history.keys())
    max_year = max(history.keys())
    
    # Create DataFrame
    years = range(min_year, max_year + 1)
    counts = [history.get(y, 0) for y in years]
    df = pd.DataFrame({'year': years, 'count': counts})
    
    # Calculate EMA
    # smoothing factor 0.1
    df['ema'] = df['count'].ewm(alpha=0.1, adjust=False).mean()
    
    # Find max EMA
    best_row = df.loc[df['ema'].idxmax()]
    best_year = int(best_row['year'])
    max_ema = best_row['ema']
    
    results.append({
        'cpc_code': cpc,
        'best_year': best_year,
        'max_ema': max_ema
    })

# Sort by EMA descending (optional, or just return all)
results.sort(key=lambda x: x['max_ema'], reverse=True)

# Output intermediate result to get titles later
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-14016306173097755035': 'file_storage/function-call-14016306173097755035.json', 'var_function-call-14016306173097755288': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-3425986448742959405': [{'symbol': 'C01', 'level': '4.0', 'titleFull': 'INORGANIC CHEMISTRY'}, {'symbol': 'C01B', 'level': '5.0', 'titleFull': 'NON-METALLIC ELEMENTS; COMPOUNDS THEREOF; METALLOIDS OR COMPOUNDS THEREOF NOT COVERED BY SUBCLASS C01C'}, {'symbol': 'C01B33/00', 'level': '7.0', 'titleFull': 'Silicon; Compounds thereof'}], 'var_function-call-3595820558278827425': [{'COUNT(*)': '55'}], 'var_function-call-14505097301841626708': [{'COUNT(*)': '12225'}], 'var_function-call-14453105091914346968': 'file_storage/function-call-14453105091914346968.json'}

exec(code, env_args)
