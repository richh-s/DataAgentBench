code = """import json
import re
from collections import defaultdict

# Load data
with open(locals()['var_function-call-4974488808225168135'], 'r') as f:
    patents = json.load(f)

with open(locals()['var_function-call-4381654191407381320'], 'r') as f:
    titles_list = json.load(f)

# Map symbol to title
cpc_titles = {item['symbol']: item['titleFull'] for item in titles_list}

# Helper to parse date
def parse_year(date_str):
    # Formats: "14th Mar 2019", "Mar 19th, 2019", "2019 on Jul 12th", "2019, June 17th", "dated 5th March 2019", "March the 18th, 2019"
    # Just extract 4 digits
    match = re.search(r'\b(19|20)\d{2}\b', date_str)
    if match:
        return int(match.group(0))
    return None

def parse_date_struct(date_str):
    # Need to determine month and day for filtering H2 2019 (July-Dec)
    # Extract year, month
    # Simplification: Convert to YYYYMMDD string for comparison
    # Regex for months
    months = {
        'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
        'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12,
        'January': 1, 'February': 2, 'March': 3, 'April': 4, 'June': 6,
        'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12
    }
    
    try:
        y_match = re.search(r'\b(2019)\b', date_str)
        if not y_match:
            return None # Not 2019
        
        # Find month
        month = None
        for m_str, m_int in months.items():
            if m_str in date_str:
                month = m_int
                break
        
        if month is None:
            return None
            
        return month # Return month number
    except:
        return None

# Filter patents
filtered_patents = []
for p in patents:
    # 1. Check Grant Date (H2 2019)
    g_date = p.get('grant_date', '')
    if not g_date:
        continue
    
    month = parse_date_struct(g_date)
    if month is None or month < 7:
        continue
        
    # 2. Check Country (Germany)
    p_info = p.get('Patents_info', '')
    # Check for DE publication or application
    # Regex: "publication (no.|number) DE-" or "application (no.|number|ID) DE-"
    # Or just "DE-" followed by digits
    if "DE-" in p_info:
        # Verify it's not part of something else like "CODE-123"
        # Check specific patterns
        if (re.search(r'publication (no\.|number)\s*DE-', p_info, re.IGNORECASE) or 
            re.search(r'application (no\.|number|ID)\s*DE-', p_info, re.IGNORECASE) or
            re.search(r'publication number\s*[A-Z]{2}-', p_info) and "DE-" in p_info): # Fallback
             pass
        else:
             # Look for "from DE" or "In DE"
             if not (re.search(r'\bfrom DE\b', p_info) or re.search(r'\bIn DE\b', p_info)):
                 continue
    else:
        continue

    # 3. Get Filing Year
    f_date = p.get('filing_date', '')
    f_year = parse_year(f_date)
    if not f_year:
        continue
        
    filtered_patents.append({
        'filing_year': f_year,
        'cpc_raw': p.get('cpc', '[]')
    })

print(f"Filtered patents count: {len(filtered_patents)}")

# Process CPCs and calculate EMA
group_counts = defaultdict(lambda: defaultdict(int)) # code -> year -> count
group_years = defaultdict(set) # code -> years

for p in filtered_patents:
    f_year = p['filing_year']
    try:
        cpc_list = json.loads(p['cpc_raw'])
    except:
        continue
        
    unique_codes = set()
    for item in cpc_list:
        code = item.get('code', '')
        # Level 4 is Class (3 chars, e.g. H01)
        if len(code) >= 3:
            l4_code = code[:3]
            unique_codes.add(l4_code)
    
    for code in unique_codes:
        group_counts[code][f_year] += 1
        group_years[code].add(f_year)

# Calculate EMA
results = []
alpha = 0.1

for code, counts in group_counts.items():
    years = sorted(list(group_years[code]))
    if not years:
        continue
        
    min_year = min(years)
    max_year = max(years)
    
    # Create continuous timeline? 
    # Or just observed years?
    # "exponential moving average of patent filings EACH YEAR"
    # Usually implies a time series. I will fill missing years with 0 from min to max.
    
    timeline = range(min_year, max_year + 1)
    ema = 0
    max_ema = -1
    best_year = -1
    
    first = True
    for y in timeline:
        cnt = counts.get(y, 0)
        if first:
            ema = cnt
            first = False
        else:
            ema = alpha * cnt + (1 - alpha) * ema
        
        if ema > max_ema:
            max_ema = ema
            best_year = y
            
    results.append({
        'code': code,
        'max_ema': max_ema,
        'best_year': best_year,
        'title': cpc_titles.get(code, "Unknown")
    })

# Sort by Max EMA
results.sort(key=lambda x: x['max_ema'], reverse=True)

# Top results
top_results = results[:10] # Top 10

print("__RESULT__:")
print(json.dumps(top_results))"""

env_args = {'var_function-call-543765259574918097': 'file_storage/function-call-543765259574918097.json', 'var_function-call-4974488808225165482': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-4974488808225168135': 'file_storage/function-call-4974488808225168135.json', 'var_function-call-15178168180992510459': [{'symbol': 'H', 'level': '2.0', 'titleFull': 'ELECTRICITY'}, {'symbol': 'H01', 'level': '4.0', 'titleFull': 'ELECTRIC ELEMENTS'}, {'symbol': 'H01L', 'level': '5.0', 'titleFull': 'SEMICONDUCTOR DEVICES NOT COVERED BY CLASS H10'}, {'symbol': 'H01L21/00', 'level': '7.0', 'titleFull': 'Processes or apparatus adapted for the manufacture or treatment of semiconductor or solid state devices or of parts thereof'}], 'var_function-call-4381654191407381320': 'file_storage/function-call-4381654191407381320.json'}

exec(code, env_args)
