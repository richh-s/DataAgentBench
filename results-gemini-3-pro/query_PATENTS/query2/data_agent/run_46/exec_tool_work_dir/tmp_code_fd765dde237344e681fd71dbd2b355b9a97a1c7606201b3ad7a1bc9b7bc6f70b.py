code = """import json
import re
from datetime import datetime

# Load data
with open('var_function-call-9170498149047143143.json', 'r') as f:
    cpc_defs_raw = json.load(f)

with open('var_function-call-1798805734862121225.json', 'r') as f:
    patents_raw = json.load(f)

# Create CPC definition map (symbol -> titleFull)
cpc_map = {item['symbol']: item['titleFull'] for item in cpc_defs_raw}

# Date parsing logic
month_map = {
    'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
    'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12,
    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
}

def parse_date(date_str):
    if not date_str:
        return None
    # Remove ordinal suffixes and filler words
    clean_str = re.sub(r'(st|nd|rd|th)', '', date_str)
    clean_str = re.sub(r'[,]', ' ', clean_str)
    clean_str = re.sub(r'\b(of|on|dated|the)\b', ' ', clean_str, flags=re.IGNORECASE)
    # Normalize spaces
    clean_str = ' '.join(clean_str.split())
    
    # Try to find year, month, day
    # Pattern: Look for 4 digits (year), word (month), 1-2 digits (day)
    # Can be in any order
    try:
        parts = clean_str.split()
        year, month, day = None, None, None
        
        for part in parts:
            if part.isdigit():
                val = int(part)
                if val > 1900 and val < 2100:
                    year = val
                elif 1 <= val <= 31:
                    # Could be day or month number, but month is usually text here.
                    # Assume day if we haven't found day.
                    if day is None:
                        day = val
            elif part.title() in month_map:
                month = month_map[part.title()]
            elif part.title()[:3] in month_map: # Handle abbreviations
                 month = month_map[part.title()[:3]]
        
        if year and month and day:
            return datetime(year, month, day)
    except:
        pass
    return None

# Process patents
valid_patents = []
target_cpc_groups = set()

# First pass: Parse dates and identify target CPC groups from 2H 2019 grants
target_start = datetime(2019, 7, 1)
target_end = datetime(2019, 12, 31)

processed_patents = []

for p in patents_raw:
    g_date = parse_date(p.get('grant_date'))
    f_date = parse_date(p.get('filing_date'))
    
    if not f_date:
        continue # Need filing date for EMA
    
    # Extract CPC classes (Level 4, 3 chars)
    cpc_json = p.get('cpc')
    codes = set()
    if cpc_json:
        try:
            cpc_list = json.loads(cpc_json)
            for item in cpc_list:
                code = item.get('code', '')
                if len(code) >= 3:
                    cls = code[:3]
                    codes.add(cls)
        except:
            pass
            
    processed_patents.append({
        'grant_date': g_date,
        'filing_year': f_date.year,
        'cpc_classes': codes
    })
    
    # Check if granted in 2H 2019
    if g_date and target_start <= g_date <= target_end:
        target_cpc_groups.update(codes)

# Only consider groups that exist in the definition map (Level 4)
# Also filter target_cpc_groups to valid ones (keys in cpc_map)
valid_target_groups = {c for c in target_cpc_groups if c in cpc_map}

# Second pass: Aggregate filings for these groups
# Structure: group -> {year: count}
group_filings = {c: {} for c in valid_target_groups}

for p in processed_patents:
    f_year = p['filing_year']
    for c in p['cpc_classes']:
        if c in group_filings:
            group_filings[c][f_year] = group_filings[c].get(f_year, 0) + 1

# Calculate EMA
results = []
alpha = 0.1

for c, filings in group_filings.items():
    if not filings:
        continue
    
    # Determine year range
    min_year = min(filings.keys())
    max_year = max(filings.keys())
    
    # Create time series
    # We should probably extend range to include all years up to max_year found across all patents?
    # Or just the local range. Local range is safer.
    years = sorted(range(min_year, max_year + 1))
    
    ema = None
    max_ema = -1.0
    best_year = None
    
    for y in years:
        count = filings.get(y, 0)
        if ema is None:
            ema = count
        else:
            ema = alpha * count + (1 - alpha) * ema
        
        if ema > max_ema:
            max_ema = ema
            best_year = y
            
    results.append({
        'CPC group code': c,
        'Full title': cpc_map[c],
        'Best year': best_year,
        'Max EMA': max_ema
    })

# Sort by Max EMA descending
results.sort(key=lambda x: x['Max EMA'], reverse=True)

print("__RESULT__:")
print(json.dumps(results[:10])) # Return top 10"""

env_args = {'var_function-call-10751408209218884262': 'file_storage/function-call-10751408209218884262.json', 'var_function-call-5193732056185576556': [{'Patents_info': 'VITTORI GIANFRANCO DE holds the FR patent filing (app. number FR-7811408-A), with publication number FR-2388575-B3.'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.'}, {'Patents_info': 'MITUTOYO CORP holds the DE patent filing (app. number DE-10037981-A), with pub. number DE-10037981-B4.'}], 'var_function-call-5193732056185577357': [{'symbol': 'A01K2227/108', 'level': '9.0', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'level': '9.0', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'level': '9.0', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'level': '9.0', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'level': '9.0', 'titleFull': 'Ovine'}], 'var_function-call-8094760001745233462': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}, {'symbol': 'B99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION'}, {'symbol': 'B29', 'titleFull': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL'}, {'symbol': 'B33', 'titleFull': 'ADDITIVE MANUFACTURING TECHNOLOGY'}, {'symbol': 'C22', 'titleFull': 'METALLURGY; FERROUS OR NON-FERROUS ALLOYS; TREATMENT OF ALLOYS OR NON-FERROUS METALS'}, {'symbol': 'D99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION'}], 'var_function-call-8094760001745234105': [{'COUNT(*)': '1932'}], 'var_function-call-883454638392512473': [{'symbol': 'A', 'level': '2.0', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'A01', 'level': '4.0', 'titleFull': 'AGRICULTURE; FORESTRY; ANIMAL HUSBANDRY; HUNTING; TRAPPING; FISHING'}, {'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'A01B1/00', 'level': '7.0', 'titleFull': 'Hand tools'}], 'var_function-call-9170498149047143143': 'file_storage/function-call-9170498149047143143.json', 'var_function-call-1798805734862121225': 'file_storage/function-call-1798805734862121225.json'}

exec(code, env_args)
