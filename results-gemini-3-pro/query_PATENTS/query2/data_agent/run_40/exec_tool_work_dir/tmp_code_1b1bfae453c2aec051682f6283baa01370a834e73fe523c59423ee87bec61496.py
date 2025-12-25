code = """import json
import re

# Load data
with open(locals()['var_function-call-11028473770034293792'], 'r') as f:
    patents = json.load(f)

with open(locals()['var_function-call-16227549085271069806'], 'r') as f:
    cpc_defs = json.load(f)

cpc_map = {item['symbol']: item['titleFull'] for item in cpc_defs}

# Filter patents
filtered_patents = []
h2_months = ['july', 'august', 'september', 'october', 'november', 'december']

for p in patents:
    p_info = p.get('Patents_info', '')
    if 'DE-' not in p_info:
        continue
    
    g_date = p.get('grant_date', '').lower()
    if '2019' not in g_date:
        continue
    
    # Check H2
    is_h2 = any(m in g_date for m in h2_months)
    if not is_h2:
        continue
        
    filtered_patents.append(p)

# Process filings
# Structure: {cpc_code: {year: count}}
filings = {}

for p in filtered_patents:
    # Get filing year
    f_date = p.get('filing_date', '')
    y_match = re.search(r'\d{4}', f_date)
    if not y_match:
        continue
    year = int(y_match.group(0))
    
    # Get CPC codes (Level 4 Class)
    cpc_json = p.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_json)
    except:
        continue
        
    # Extract codes
    codes = set()
    for item in cpc_list:
        code = item.get('code', '')
        if len(code) >= 3:
            class_code = code[:3] # Level 4 in DB is 3 chars (e.g. H04)
            # Ensure it is a valid class code format (Letter + 2 digits)
            # Some codes might be different? 
            # Standard CPC class is 1 letter + 2 digits (e.g. A01).
            # If code is like Y02E... Y02 is class.
            codes.add(class_code)
            
    for c in codes:
        if c not in filings:
            filings[c] = {}
        filings[c][year] = filings[c].get(year, 0) + 1

# Calculate EMA
alpha = 0.1
results = []

for cpc, year_counts in filings.items():
    if not year_counts:
        continue
        
    years = sorted(year_counts.keys())
    if not years:
        continue
        
    min_year = years[0]
    max_year = years[-1]
    
    ema = year_counts[min_year] # Initialize with first observation
    best_ema = ema
    best_year = min_year
    
    # Iterate from min_year + 1 to max_year
    current_year = min_year + 1
    while current_year <= max_year:
        count = year_counts.get(current_year, 0)
        ema = alpha * count + (1 - alpha) * ema
        
        if ema > best_ema:
            best_ema = ema
            best_year = current_year
        
        current_year += 1
        
    results.append({
        "CPC Group Code": cpc,
        "Full Title": cpc_map.get(cpc, "N/A"),
        "Best Year": best_year,
        "Max EMA": best_ema
    })

# Sort by Max EMA
results.sort(key=lambda x: x['Max EMA'], reverse=True)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-6900902718383097330': 'file_storage/function-call-6900902718383097330.json', 'var_function-call-1392774076745660439': [{'Patents_info': 'Patent application (number DE-10317286-A) from DE, belonging to NICOLAY VERWALTUNGS GMBH, with publication no. DE-10317286-B3.'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.'}, {'Patents_info': 'In DE, the patent filing (application no. DE-102009032362-A) is owned by MARTOR KG and has pub. number DE-102009032362-B3.'}], 'var_function-call-3593124933623607429': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-7323997037308630728': [{'symbol': 'B', 'level': '2.0', 'titleFull': 'PERFORMING OPERATIONS; TRANSPORTING'}, {'symbol': 'H', 'level': '2.0', 'titleFull': 'ELECTRICITY'}, {'symbol': 'Y', 'level': '2.0', 'titleFull': 'GENERAL TAGGING OF NEW TECHNOLOGICAL DEVELOPMENTS; GENERAL TAGGING OF CROSS-SECTIONAL TECHNOLOGIES SPANNING OVER SEVERAL SECTIONS OF THE IPC; TECHNICAL SUBJECTS COVERED BY FORMER USPC CROSS-REFERENCE ART COLLECTIONS [XRACs] AND DIGESTS'}, {'symbol': 'D', 'level': '2.0', 'titleFull': 'TEXTILES; PAPER'}, {'symbol': 'F', 'level': '2.0', 'titleFull': 'MECHANICAL ENGINEERING; LIGHTING; HEATING; WEAPONS; BLASTING'}, {'symbol': 'E', 'level': '2.0', 'titleFull': 'FIXED CONSTRUCTIONS'}, {'symbol': 'C', 'level': '2.0', 'titleFull': 'CHEMISTRY; METALLURGY'}, {'symbol': 'G', 'level': '2.0', 'titleFull': 'PHYSICS'}, {'symbol': 'A', 'level': '2.0', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}, {'symbol': 'A01N', 'level': '5.0', 'titleFull': 'PRESERVATION OF BODIES OF HUMANS OR ANIMALS OR PLANTS OR PARTS THEREOF; BIOCIDES, e.g. AS DISINFECTANTS, AS PESTICIDES OR AS HERBICIDES; PEST REPELLANTS OR ATTRACTANTS; PLANT GROWTH REGULATORS'}, {'symbol': 'A01P', 'level': '5.0', 'titleFull': 'BIOCIDAL, PEST REPELLANT, PEST ATTRACTANT OR PLANT GROWTH REGULATORY ACTIVITY OF CHEMICAL COMPOUNDS OR PREPARATIONS'}, {'symbol': 'A01D', 'level': '5.0', 'titleFull': 'HARVESTING; MOWING'}, {'symbol': 'A01L', 'level': '5.0', 'titleFull': 'SHOEING OF ANIMALS'}, {'symbol': 'A01K', 'level': '5.0', 'titleFull': 'ANIMAL HUSBANDRY; AVICULTURE; APICULTURE; PISCICULTURE; FISHING; REARING OR BREEDING ANIMALS, NOT OTHERWISE PROVIDED FOR; NEW BREEDS OF ANIMALS'}, {'symbol': 'A01M', 'level': '5.0', 'titleFull': 'CATCHING, TRAPPING OR SCARING OF ANIMALS; APPARATUS FOR THE DESTRUCTION OF NOXIOUS ANIMALS OR NOXIOUS PLANTS'}], 'var_function-call-10208193421792653251': [], 'var_function-call-12206349714140732509': [{'symbol': 'C13B50/00', 'level': '7.0', 'titleFull': 'Sugar products, e.g. powdered, lump or liquid sugar; Working-up of sugar'}, {'symbol': 'C13B40/00', 'level': '7.0', 'titleFull': 'Drying sugar'}, {'symbol': 'C13B99/00', 'level': '7.0', 'titleFull': 'Subject matter not provided for in other groups of this subclass'}, {'symbol': 'C13B45/00', 'level': '7.0', 'titleFull': 'Cutting machines specially adapted for sugar'}, {'symbol': 'C21B3/00', 'level': '7.0', 'titleFull': 'General features in the manufacture of pig-iron'}], 'var_function-call-1615368643440033364': [{'symbol': 'H04L', 'level': '5.0', 'titleFull': 'TRANSMISSION OF DIGITAL INFORMATION, e.g. TELEGRAPHIC COMMUNICATION'}, {'symbol': 'H04', 'level': '4.0', 'titleFull': 'ELECTRIC COMMUNICATION TECHNIQUE'}], 'var_function-call-6132027812850368290': [{'COUNT(*)': '68'}], 'var_function-call-7533784351661024707': [{'COUNT(*)': '4833'}], 'var_function-call-11028473770034293792': 'file_storage/function-call-11028473770034293792.json', 'var_function-call-16227549085271069806': 'file_storage/function-call-16227549085271069806.json'}

exec(code, env_args)
