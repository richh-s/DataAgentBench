code = """import pandas as pd
import json
import re

# Load data
with open(locals()['var_function-call-5473606879443203054'], 'r') as f:
    data = json.load(f)

# Date parser
def parse_date(date_str):
    # Map month names
    months = {
        'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6,
        'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12,
        'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
        'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
    }
    
    if not date_str:
        return None
        
    s = date_str.lower()
    # Remove suffixes
    s = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', s)
    # Remove filler words
    s = re.sub(r'\b(dated|on|the|of)\b', ' ', s)
    # Replace commas with space
    s = s.replace(',', ' ')
    
    parts = s.split()
    
    y, m, d = None, None, None
    
    # Find Year (4 digits)
    for i, p in enumerate(parts):
        if p.isdigit() and len(p) == 4:
            y = int(p)
            parts.pop(i)
            break
            
    if y is None: return None
    
    # Find Month
    for i, p in enumerate(parts):
        if p in months:
            m = months[p]
            parts.pop(i)
            break
            
    if m is None: return None
    
    # Find Day
    for p in parts:
        if p.isdigit():
            d = int(p)
            break
            
    if y and m and d:
        try:
            return pd.Timestamp(year=y, month=m, day=d)
        except:
            return None
    return None

# Filter and Process
counts = {}

for row in data:
    g_date = parse_date(row.get('grant_date'))
    # Filter Grant Date: H2 2019
    if g_date and g_date >= pd.Timestamp('2019-07-01') and g_date <= pd.Timestamp('2019-12-31'):
        f_date = parse_date(row.get('filing_date'))
        if f_date:
            y = f_date.year
            try:
                cpcs = json.loads(row.get('cpc', '[]'))
            except:
                continue
            
            # Extract Level 4 codes (Classes)
            # Level 4 is 3 chars (e.g., A23)
            classes = set()
            for c in cpcs:
                code = c.get('code', '')
                if len(code) >= 3:
                    cls = code[:3]
                    classes.add(cls)
            
            for cls in classes:
                if cls not in counts:
                    counts[cls] = {}
                counts[cls][y] = counts[cls].get(y, 0) + 1

# Calculate EMA
results = []
alpha = 0.1

for cls, year_counts in counts.items():
    if not year_counts:
        continue
        
    min_year = min(year_counts.keys())
    max_year = max(year_counts.keys())
    years = sorted(range(min_year, max_year + 1))
    
    ema = 0
    best_ema = -1.0
    best_year = None
    
    first = True
    for y in years:
        cnt = year_counts.get(y, 0)
        if first:
            ema = cnt
            first = False
        else:
            ema = alpha * cnt + (1 - alpha) * ema
            
        if ema > best_ema:
            best_ema = ema
            best_year = y
            
    results.append({
        'symbol': cls,
        'best_year': best_year,
        'max_ema': round(best_ema, 4)
    })

# Sort by Max EMA
results.sort(key=lambda x: x['max_ema'], reverse=True)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-8608372227863674582': 'file_storage/function-call-8608372227863674582.json', 'var_function-call-15024124238442063674': [{'Patents_info': 'VITTORI GIANFRANCO DE holds the FR patent filing (app. number FR-7811408-A), with publication number FR-2388575-B3.', 'grant_date': '1980 on Nov 14th'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.', 'grant_date': '2006 on Apr 27th'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.', 'grant_date': 'Nov 29th, 2007'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.', 'grant_date': '2009, January 29th'}, {'Patents_info': 'MITUTOYO CORP holds the DE patent filing (app. number DE-10037981-A), with pub. number DE-10037981-B4.', 'grant_date': '19th of October, 2017'}], 'var_function-call-5473606879443203054': 'file_storage/function-call-5473606879443203054.json', 'var_function-call-2708646517238800899': [{'symbol': 'A23N4/085', 'level': '10.0', 'titleFull': 'Machines for stoning fruit or removing seed-containing sections from fruit, characterised by their stoning or removing device for stoning fruit for dates, olives or the like oblong fruits for olives'}, {'symbol': 'A23N12/125', 'level': '10.0', 'titleFull': 'Accessories or details'}, {'symbol': 'A23N7/026', 'level': '10.0', 'titleFull': 'Peeling machines therefor with rotary fruit holding spindles and fixed or movable peeler blades'}, {'symbol': 'A23N12/026', 'level': '10.0', 'titleFull': 'Stone-gatherers or cleaning devices for the washing machines'}, {'symbol': 'A23N', 'level': '5.0', 'titleFull': 'MACHINES OR APPARATUS FOR TREATING HARVESTED FRUIT, VEGETABLES OR FLOWER BULBS IN BULK, NOT OTHERWISE PROVIDED FOR; PEELING VEGETABLES OR FRUIT IN BULK; APPARATUS FOR PREPARING ANIMAL FEEDING- STUFFS'}, {'symbol': 'A23N12/00', 'level': '7.0', 'titleFull': 'Machines for cleaning, blanching, drying or roasting fruits or vegetables, e.g. coffee, cocoa, nuts'}, {'symbol': 'A23N1/00', 'level': '7.0', 'titleFull': 'Machines or apparatus for extracting juice'}, {'symbol': 'A23N3/00', 'level': '7.0', 'titleFull': 'Machines for coring or stoning fruit, characterised by their feeding device'}, {'symbol': 'A23N7/00', 'level': '7.0', 'titleFull': 'Peeling vegetables or fruit'}, {'symbol': 'A23N11/00', 'level': '7.0', 'titleFull': 'Removing pith from stems'}], 'var_function-call-8672725961208045102': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}, {'symbol': 'B99', 'level': '4.0', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION'}, {'symbol': 'B29', 'level': '4.0', 'titleFull': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL'}, {'symbol': 'B33', 'level': '4.0', 'titleFull': 'ADDITIVE MANUFACTURING TECHNOLOGY'}, {'symbol': 'C22', 'level': '4.0', 'titleFull': 'METALLURGY; FERROUS OR NON-FERROUS ALLOYS; TREATMENT OF ALLOYS OR NON-FERROUS METALS'}, {'symbol': 'D99', 'level': '4.0', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION'}], 'var_function-call-16602253025004067718': [{'symbol': 'A', 'level': '2.0', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'A23', 'level': '4.0', 'titleFull': 'FOODS OR FOODSTUFFS; TREATMENT THEREOF, NOT COVERED BY OTHER CLASSES'}, {'symbol': 'A23N', 'level': '5.0', 'titleFull': 'MACHINES OR APPARATUS FOR TREATING HARVESTED FRUIT, VEGETABLES OR FLOWER BULBS IN BULK, NOT OTHERWISE PROVIDED FOR; PEELING VEGETABLES OR FRUIT IN BULK; APPARATUS FOR PREPARING ANIMAL FEEDING- STUFFS'}]}

exec(code, env_args)
