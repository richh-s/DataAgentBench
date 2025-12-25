code = """import json
import pandas as pd
from datetime import datetime

# Load results
with open(locals()['var_function-call-9850245990308066574'], 'r') as f:
    patents = json.load(f)

with open(locals()['var_function-call-9850245990308067851'], 'r') as f:
    cpc_defs_list = json.load(f)

# Create CPC title map
cpc_titles = {item['symbol']: item['titleFull'] for item in cpc_defs_list}

# Date parsing helper
def parse_date(date_str):
    if not date_str:
        return None
    # Clean string
    date_str = date_str.lower().replace("dated", "").replace("on", "").replace("of", "").replace(",", "").replace(".", "").strip()
    # Handle ordinals (1st, 2nd, 3rd, 4th)
    for ord_suffix in ["st", "nd", "rd", "th"]:
        if ord_suffix in date_str:
            # removing suffix might be tricky if it's part of month name (unlikely for st, nd, rd, th)
            # regex would be better but keeping it simple
            # Usually format is "3rd August 2021" -> "3 August 2021"
            # But "August" contains "st"? No. "August" has "st". Wait.
            # "1st" -> "1"
            import re
            date_str = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', date_str)
            break
    
    formats = [
        "%d %B %Y", "%B %d %Y", "%Y %B %d",
        "%d %b %Y", "%b %d %Y",
        "%Y-%m-%d"
    ]
    
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    return None

def parse_filing_year(date_str):
    dt = parse_date(date_str)
    if dt:
        return dt.year
    return None

def is_h2_2019(date_str):
    dt = parse_date(date_str)
    if dt:
        if dt.year == 2019 and dt.month >= 7:
            return True
    return False

# Filter and Process
filtered_patents = []
for p in patents:
    # Filter grant date H2 2019
    if not is_h2_2019(p.get('grant_date')):
        continue
    
    # Filter Germany (already done by SQL mostly, but double check country code if possible, or trust SQL)
    # SQL: Patents_info LIKE '%DE-%' OR Patents_info LIKE '%Germany%'
    # We proceed with this set.
    
    # Get Filing Year
    f_year = parse_filing_year(p.get('filing_date'))
    if not f_year:
        continue
        
    # Get CPCs (Level 4 -> first 3 chars)
    cpc_json = p.get('cpc')
    if not cpc_json:
        continue
    try:
        cpcs = json.loads(cpc_json)
    except:
        continue
        
    codes = set()
    for c in cpcs:
        code = c.get('code', '')
        if len(code) >= 3:
            level4 = code[:3]
            codes.add(level4)
    
    for code in codes:
        filtered_patents.append({'year': f_year, 'code': code})

# Aggregate filings
df = pd.DataFrame(filtered_patents)
if df.empty:
    print("__RESULT__:")
    print(json.dumps([]))
else:
    counts = df.groupby(['code', 'year']).size().reset_index(name='count')

    # Create full year range for each code
    min_year = counts['year'].min()
    max_year = counts['year'].max()
    all_years = range(min_year, max_year + 1)
    
    # Pivot to fill missing years with 0
    pivot = counts.pivot(index='code', columns='year', values='count').fillna(0)
    pivot = pivot.reindex(columns=all_years, fill_value=0)
    
    # Calculate EMA
    # Formula: EMA_t = alpha * Count_t + (1-alpha) * EMA_{t-1}
    # Initial EMA: We can start with the first value.
    alpha = 0.1
    ema_df = pivot.copy()
    
    # Initialize first column
    # Usually EMA is calculated recursively.
    # Pandas ewm function: adjust=False implies the recursive formula.
    ema_df = pivot.T.ewm(alpha=alpha, adjust=False).mean().T

    # Find Top Areas
    # "Find the CPC technology areas ... with the highest EMA each year"
    # For each year, find the code with max EMA.
    
    winners = {} # year -> {code, ema}
    
    for year in all_years:
        # Get max EMA for this year
        max_val = ema_df[year].max()
        # Get code(s) with this max
        top_codes = ema_df[ema_df[year] == max_val].index.tolist()
        
        winners[year] = []
        for c in top_codes:
            winners[year].append({'code': c, 'ema': max_val})

    # "Include the full title, CPC group code, and the best year for each CPC group"
    # Collect unique codes from the winners
    unique_codes = set()
    for year, items in winners.items():
        for item in items:
            unique_codes.add(item['code'])
            
    results = []
    for code in unique_codes:
        # Find best year for this code (max EMA year)
        # We look at the entire ema_df for this code
        code_series = ema_df.loc[code]
        best_year = code_series.idxmax()
        max_ema = code_series.max()
        
        title = cpc_titles.get(code, "N/A")
        
        results.append({
            "CPC Group Code": code,
            "Title": title,
            "Best Year": int(best_year),
            "Max EMA": float(max_ema) # optional, for checking
        })

    # Sort results? Maybe by Best Year or Code?
    # Query doesn't specify sort order.
    results.sort(key=lambda x: x['CPC Group Code'])
    
    print("__RESULT__:")
    print(json.dumps(results))"""

env_args = {'var_function-call-13186560279327223649': 'file_storage/function-call-13186560279327223649.json', 'var_function-call-13186560279327220156': [{'symbol': 'A01K2227/108', 'level': '9.0', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'level': '9.0', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'level': '9.0', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'level': '9.0', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'level': '9.0', 'titleFull': 'Ovine'}], 'var_function-call-14970819546333422104': [{'symbol': 'C', 'level': '2.0', 'titleFull': 'CHEMISTRY; METALLURGY'}, {'symbol': 'C01', 'level': '4.0', 'titleFull': 'INORGANIC CHEMISTRY'}, {'symbol': 'C01B', 'level': '5.0', 'titleFull': 'NON-METALLIC ELEMENTS; COMPOUNDS THEREOF; METALLOIDS OR COMPOUNDS THEREOF NOT COVERED BY SUBCLASS C01C'}, {'symbol': 'C01B33/00', 'level': '7.0', 'titleFull': 'Silicon; Compounds thereof'}], 'var_function-call-14970819546333424263': [{'Patents_info': 'VITTORI GIANFRANCO DE holds the FR patent filing (app. number FR-7811408-A), with publication number FR-2388575-B3.'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.'}, {'Patents_info': 'MITUTOYO CORP holds the DE patent filing (app. number DE-10037981-A), with pub. number DE-10037981-B4.'}], 'var_function-call-445264303235556503': [{'level': '4.0', 'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'level': '4.0', 'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'level': '4.0', 'symbol': 'B30', 'titleFull': 'PRESSES'}, {'level': '4.0', 'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'level': '4.0', 'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}, {'level': '4.0', 'symbol': 'B99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION'}, {'level': '4.0', 'symbol': 'B29', 'titleFull': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL'}, {'level': '4.0', 'symbol': 'B33', 'titleFull': 'ADDITIVE MANUFACTURING TECHNOLOGY'}, {'level': '4.0', 'symbol': 'C22', 'titleFull': 'METALLURGY; FERROUS OR NON-FERROUS ALLOYS; TREATMENT OF ALLOYS OR NON-FERROUS METALS'}, {'level': '4.0', 'symbol': 'D99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION'}], 'var_function-call-9850245990308066574': 'file_storage/function-call-9850245990308066574.json', 'var_function-call-9850245990308067851': 'file_storage/function-call-9850245990308067851.json'}

exec(code, env_args)
