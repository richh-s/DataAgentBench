code = """import json
import re

# Load data
with open(locals()['var_function-call-11543888931216263098'], 'r') as f:
    data = json.load(f)

# Load titles
with open(locals()['var_function-call-16387991390808413708'], 'r') as f:
    titles_list = json.load(f)

titles_map = {item['symbol']: item['titleFull'] for item in titles_list}

def parse_date_to_year_month(date_str):
    # Extracts year and month from strings like "3rd August 2021", "dated 5th March 2019", "2013, June 17th"
    # Mapping months
    months = {
        'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6,
        'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12,
        'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'jun': 6, 'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
    }
    
    date_str = date_str.lower()
    
    # Find year (4 digits)
    year_match = re.search(r'\b(19|20)\d{2}\b', date_str)
    if not year_match:
        return None, None
    year = int(year_match.group(0))
    
    # Find month
    month = None
    for m_name, m_num in months.items():
        if m_name in date_str:
            month = m_num
            break
            
    return year, month

def get_filing_year(date_str):
    y, m = parse_date_to_year_month(date_str)
    return y

# Filter and aggregate
filings = {} # class -> {year: count}

for record in data:
    # Filter grant date: H2 2019
    g_date = record.get('grant_date', '')
    g_year, g_month = parse_date_to_year_month(g_date)
    
    if g_year != 2019 or g_month is None or g_month < 7:
        continue
        
    # Check for Germany in Patents_info if not filtered by query
    # The query already filtered for "publication number DE", so we assume these are DE.
    # Just in case, let's verify if "DE" is in Patents_info
    if 'DE' not in record.get('Patents_info', ''):
        continue

    # Filing Year
    f_year = get_filing_year(record.get('filing_date', ''))
    if f_year is None:
        continue
        
    # Extract CPC Classes
    cpc_json = record.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_json)
    except:
        continue
        
    seen_classes = set()
    for item in cpc_list:
        code = item.get('code', '')
        if len(code) >= 3:
            cls = code[:3] # Level 4 class (e.g. C01)
            # Verify if it is a valid class format (Letter + 2 digits)?
            # Or just use the first 3 chars as per CPC structure.
            # Most are like [A-H][0-9]{2}.
            if re.match(r'^[A-H]\d{2}$', cls):
                 seen_classes.add(cls)
    
    for cls in seen_classes:
        if cls not in filings:
            filings[cls] = {}
        filings[cls][f_year] = filings[cls].get(f_year, 0) + 1

# Calculate EMA
results = []
alpha = 0.1

for cls, year_counts in filings.items():
    if not year_counts:
        continue
        
    years = sorted(year_counts.keys())
    min_year = years[0]
    max_year = years[-1]
    
    ema = 0
    best_ema = -1.0
    best_year = None
    
    # Iterate through all years in range
    # Note: "highest EMA each year" could mean calculating for each year. 
    # But usually EMA is recursive.
    # Initial EMA: usually first observation.
    
    # Let's start from the first year with data.
    ema = year_counts[min_year]
    if ema > best_ema:
        best_ema = ema
        best_year = min_year
        
    for y in range(min_year + 1, max_year + 1):
        count = year_counts.get(y, 0)
        ema = (count * alpha) + (ema * (1 - alpha))
        if ema > best_ema:
            best_ema = ema
            best_year = y
            
    results.append({
        "class": cls,
        "title": titles_map.get(cls, "N/A"),
        "best_year": best_year,
        "max_ema": best_ema
    })

# Sort by max_ema
results.sort(key=lambda x: x['max_ema'], reverse=True)

# Top 10
top_results = results[:10]

print("__RESULT__:")
print(json.dumps(top_results))"""

env_args = {'var_function-call-4774163761277503972': 'file_storage/function-call-4774163761277503972.json', 'var_function-call-12755170999949966242': ['publicationinfo'], 'var_function-call-17983425627878789748': [{'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.'}, {'Patents_info': 'In DE, the patent application (no. DE-10130631-A) is owned by SCHNEIDER SIEGHARD and has publication number DE-10130631-B4.'}, {'Patents_info': 'The DE patent application (no. DE-10134061-A) is belonging to MOSMATIC AG NECKER and has publication number DE-10134061-B4.'}, {'Patents_info': 'In DE, the patent application (no. DE-10147111-A) is belonging to VISTEON GLOBAL TECH INC and has publication number DE-10147111-B4.'}], 'var_function-call-3520023833909275240': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-14298847436406348240': 'file_storage/function-call-14298847436406348240.json', 'var_function-call-17296021972275604149': [{'symbol': 'B', 'level': '2.0', 'titleFull': 'PERFORMING OPERATIONS; TRANSPORTING'}, {'symbol': 'B04B', 'level': '5.0', 'titleFull': 'CENTRIFUGES'}, {'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}], 'var_function-call-11543888931216263098': 'file_storage/function-call-11543888931216263098.json', 'var_function-call-16387991390808413708': 'file_storage/function-call-16387991390808413708.json'}

exec(code, env_args)
