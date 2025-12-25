code = """import json
import re
from collections import defaultdict

file_path = locals()['var_function-call-17297428760481045354']

with open(file_path, 'r') as f:
    data = json.load(f)

def parse_date_get_year_month(d_str):
    if not d_str: return None, None
    d_str = d_str.lower()
    y_matches = re.findall(r'\d{4}', d_str)
    if not y_matches: return None, None
    year = int(y_matches[-1]) 
    months = {
        'january': 1, 'jan': 1, 'february': 2, 'feb': 2, 'march': 3, 'mar': 3,
        'april': 4, 'apr': 4, 'may': 5, 'june': 6, 'jun': 6,
        'july': 7, 'jul': 7, 'august': 8, 'aug': 8, 'september': 9, 'sep': 9, 'sept': 9,
        'october': 10, 'oct': 10, 'november': 11, 'nov': 11, 'december': 12, 'dec': 12
    }
    month = 0
    for m, v in months.items():
        if m in d_str:
            month = v
            break 
    return year, month

filtered_patents = []
for p in data:
    gd = p.get('grant_date', '')
    gy, gm = parse_date_get_year_month(gd)
    if not gy or gy != 2019: continue
    if not gm or gm < 7: continue 
    
    pc = p.get('priority_claim', '[]')
    has_de = False
    try:
        pc_list = json.loads(pc)
        for item in pc_list:
            app_num = item.get('application_number', '')
            if app_num and ('DE' in app_num.upper()): 
                has_de = True
                break
    except:
        pass
    
    if not has_de:
        if 'DE-' in str(pc): has_de = True
    if not has_de: continue

    fd = p.get('filing_date', '')
    fy, fm = parse_date_get_year_month(fd)
    if not fy: continue
    
    cpc_str = p.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str)
        codes = set()
        for item in cpc_list:
            c = item.get('code', '')
            if len(c) >= 3:
                codes.add(c[:3])
        
        if codes:
            filtered_patents.append({'year': fy, 'codes': list(codes)})
    except:
        continue

counts = defaultdict(lambda: defaultdict(int))
years_set = set()
for p in filtered_patents:
    y = p['year']
    years_set.add(y)
    for c in p['codes']:
        counts[c][y] += 1

if not years_set:
    print(json.dumps([]))
else:
    min_y, max_y = min(years_set), max(years_set)
    alpha = 0.1
    
    # Calculate EMA history for all CPCs
    cpc_ema_history = defaultdict(dict)
    
    # Store "Best Year" for each CPC as well (max EMA achieved)
    cpc_best_year = {}
    
    for cpc, year_counts in counts.items():
        prev_ema = None
        max_ema_val = -1
        best_y = -1
        
        # Iterate over full range or just relevant?
        # To compare "each year", we need values for each year.
        # But EMA starts when data starts.
        # I'll calculate from min_y to max_y for all, assuming 0 if no data yet?
        # Or start from the first year the CPC appears?
        # Usually EMA starts at first observation. Before that it is undefined or 0.
        # I'll assume 0 before first observation.
        
        # Better: iterate min_y to max_y.
        for y in range(min_y, max_y + 1):
            cnt = year_counts.get(y, 0)
            if prev_ema is None:
                # If cnt > 0, start. If cnt=0, stay None (or 0).
                if cnt > 0:
                    curr_ema = float(cnt)
                else:
                    curr_ema = 0.0 # No presence yet
            else:
                curr_ema = alpha * cnt + (1 - alpha) * prev_ema
            
            cpc_ema_history[cpc][y] = curr_ema
            prev_ema = curr_ema
            
            if curr_ema > max_ema_val:
                max_ema_val = curr_ema
                best_y = y
                
        cpc_best_year[cpc] = best_y

    # Find winner for each year
    yearly_winners = []
    unique_winning_cpcs = set()
    
    for y in range(min_y, max_y + 1):
        best_cpc = None
        best_val = -1
        for cpc in cpc_ema_history:
            val = cpc_ema_history[cpc].get(y, 0)
            if val > best_val:
                best_val = val
                best_cpc = cpc
        
        if best_cpc and best_val > 0:
            yearly_winners.append({'year': y, 'cpc': best_cpc, 'ema': best_val})
            unique_winning_cpcs.add(best_cpc)

    # Prepare output: List of Unique Winning CPCs with their Best Year
    final_cpcs = []
    for cpc in unique_winning_cpcs:
        final_cpcs.append({
            'cpc': cpc, 
            'best_year': cpc_best_year[cpc]
        })

    print("__RESULT__:")
    print(json.dumps(final_cpcs))"""

env_args = {'var_function-call-17606571022762197169': 'file_storage/function-call-17606571022762197169.json', 'var_function-call-17606571022762197068': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}], 'var_function-call-3388322548671883875': [{'level': '2.0', 'symbol': 'A', 'titleFull': 'HUMAN NECESSITIES'}, {'level': '4.0', 'symbol': 'A01', 'titleFull': 'AGRICULTURE; FORESTRY; ANIMAL HUSBANDRY; HUNTING; TRAPPING; FISHING'}, {'level': '5.0', 'symbol': 'A01B', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'level': '7.0', 'symbol': 'A01B1/00', 'titleFull': 'Hand tools'}], 'var_function-call-3388322548671885256': [{'Patents_info': 'In US, the application (ID US-201916435109-A) is owned by MAHLE INT GMBH and has pub. number US-11130385-B2.', 'priority_claim': '[\n  {\n    "application_number": "DE-102018209169-A",\n    "category": "",\n    "filing_date": 20180608,\n    "npl_text": "",\n    "publication_number": "",\n    "type": ""\n  }\n]'}, {'Patents_info': 'In US, the patent filing (application no. US-201916962508-A) is owned by ZEISS CARL MEDITEC AG and has publication number US-11766171-B2.', 'priority_claim': '[\n  {\n    "application_number": "DE-102018200829-A",\n    "category": "",\n    "filing_date": 20180119,\n    "npl_text": "",\n    "publication_number": "",\n    "type": ""\n  },\n  {\n    "application_number": "EP-2019051090-W",\n    "category": "",\n    "filing_date": 20190117,\n    "npl_text": "",\n    "publication_number": "",\n    "type": ""\n  }\n]'}, {'Patents_info': 'HELLA GMBH & CO KGAA holds the US patent application (number US-202117547981-A), with pub. number US-12062949-B2.', 'priority_claim': '[\n  {\n    "application_number": "DE-102020133073-A",\n    "category": "",\n    "filing_date": 20201211,\n    "npl_text": "",\n    "publication_number": "",\n    "type": ""\n  }\n]'}], 'var_function-call-2592868685032296919': [{'count(*)': '277813'}], 'var_function-call-17297428760481045354': 'file_storage/function-call-17297428760481045354.json', 'var_function-call-12523227780323910395': [{'cpc': 'Y02', 'max_ema': 2.1, 'best_year': 2014}, {'cpc': 'G06', 'max_ema': 2.0, 'best_year': 2014}, {'cpc': 'B24', 'max_ema': 2.0, 'best_year': 2015}, {'cpc': 'B01', 'max_ema': 2.0, 'best_year': 2016}, {'cpc': 'B65', 'max_ema': 2.0, 'best_year': 2016}, {'cpc': 'G01', 'max_ema': 1.3800000000000003, 'best_year': 2016}, {'cpc': 'A47', 'max_ema': 1.3, 'best_year': 2016}, {'cpc': 'H01', 'max_ema': 1.118271, 'best_year': 2018}, {'cpc': 'B60', 'max_ema': 1.1, 'best_year': 2014}, {'cpc': 'A61', 'max_ema': 1.0124410000000001, 'best_year': 2016}], 'var_function-call-14112741153064733929': {'total': 126, 'grant_filter_pass': 66, 'de_filter_pass': 65, 'final_count': 65}, 'var_function-call-14858267732229203468': [{'symbol': 'A61', 'titleFull': 'MEDICAL OR VETERINARY SCIENCE; HYGIENE'}, {'symbol': 'A47', 'titleFull': 'FURNITURE; DOMESTIC ARTICLES OR APPLIANCES; COFFEE MILLS; SPICE MILLS; SUCTION CLEANERS IN GENERAL'}, {'symbol': 'B65', 'titleFull': 'CONVEYING; PACKING; STORING; HANDLING THIN OR FILAMENTARY MATERIAL'}, {'symbol': 'B24', 'titleFull': 'GRINDING; POLISHING'}, {'symbol': 'B01', 'titleFull': 'PHYSICAL OR CHEMICAL PROCESSES OR APPARATUS IN GENERAL'}, {'symbol': 'B60', 'titleFull': 'VEHICLES IN GENERAL'}, {'symbol': 'G06', 'titleFull': 'COMPUTING; CALCULATING OR COUNTING'}, {'symbol': 'G01', 'titleFull': 'MEASURING; TESTING'}, {'symbol': 'H01', 'titleFull': 'ELECTRIC ELEMENTS'}, {'symbol': 'Y02', 'titleFull': 'TECHNOLOGIES OR APPLICATIONS FOR MITIGATION OR ADAPTATION AGAINST CLIMATE CHANGE'}]}

exec(code, env_args)
