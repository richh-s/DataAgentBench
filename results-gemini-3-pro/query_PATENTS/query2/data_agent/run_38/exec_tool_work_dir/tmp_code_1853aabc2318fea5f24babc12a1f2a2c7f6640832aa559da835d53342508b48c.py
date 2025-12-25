code = """import json
import re

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

count_total = 0
count_grant_filter = 0
count_de_filter = 0
count_filing_date = 0
count_cpc = 0

filtered_patents = []
for p in data:
    count_total += 1
    
    gd = p.get('grant_date', '')
    gy, gm = parse_date_get_year_month(gd)
    if not gy or gy != 2019: continue
    if not gm or gm < 7: continue 
    count_grant_filter += 1
    
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
    count_de_filter += 1

    fd = p.get('filing_date', '')
    fy, fm = parse_date_get_year_month(fd)
    if not fy: continue
    count_filing_date += 1
    
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
            count_cpc += 1
    except:
        continue

print("__RESULT__:")
print(json.dumps({
    "total": count_total,
    "grant_filter_pass": count_grant_filter,
    "de_filter_pass": count_de_filter,
    "final_count": count_cpc
}))"""

env_args = {'var_function-call-17606571022762197169': 'file_storage/function-call-17606571022762197169.json', 'var_function-call-17606571022762197068': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}], 'var_function-call-3388322548671883875': [{'level': '2.0', 'symbol': 'A', 'titleFull': 'HUMAN NECESSITIES'}, {'level': '4.0', 'symbol': 'A01', 'titleFull': 'AGRICULTURE; FORESTRY; ANIMAL HUSBANDRY; HUNTING; TRAPPING; FISHING'}, {'level': '5.0', 'symbol': 'A01B', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'level': '7.0', 'symbol': 'A01B1/00', 'titleFull': 'Hand tools'}], 'var_function-call-3388322548671885256': [{'Patents_info': 'In US, the application (ID US-201916435109-A) is owned by MAHLE INT GMBH and has pub. number US-11130385-B2.', 'priority_claim': '[\n  {\n    "application_number": "DE-102018209169-A",\n    "category": "",\n    "filing_date": 20180608,\n    "npl_text": "",\n    "publication_number": "",\n    "type": ""\n  }\n]'}, {'Patents_info': 'In US, the patent filing (application no. US-201916962508-A) is owned by ZEISS CARL MEDITEC AG and has publication number US-11766171-B2.', 'priority_claim': '[\n  {\n    "application_number": "DE-102018200829-A",\n    "category": "",\n    "filing_date": 20180119,\n    "npl_text": "",\n    "publication_number": "",\n    "type": ""\n  },\n  {\n    "application_number": "EP-2019051090-W",\n    "category": "",\n    "filing_date": 20190117,\n    "npl_text": "",\n    "publication_number": "",\n    "type": ""\n  }\n]'}, {'Patents_info': 'HELLA GMBH & CO KGAA holds the US patent application (number US-202117547981-A), with pub. number US-12062949-B2.', 'priority_claim': '[\n  {\n    "application_number": "DE-102020133073-A",\n    "category": "",\n    "filing_date": 20201211,\n    "npl_text": "",\n    "publication_number": "",\n    "type": ""\n  }\n]'}], 'var_function-call-2592868685032296919': [{'count(*)': '277813'}], 'var_function-call-17297428760481045354': 'file_storage/function-call-17297428760481045354.json', 'var_function-call-12523227780323910395': [{'cpc': 'Y02', 'max_ema': 2.1, 'best_year': 2014}, {'cpc': 'G06', 'max_ema': 2.0, 'best_year': 2014}, {'cpc': 'B24', 'max_ema': 2.0, 'best_year': 2015}, {'cpc': 'B01', 'max_ema': 2.0, 'best_year': 2016}, {'cpc': 'B65', 'max_ema': 2.0, 'best_year': 2016}, {'cpc': 'G01', 'max_ema': 1.3800000000000003, 'best_year': 2016}, {'cpc': 'A47', 'max_ema': 1.3, 'best_year': 2016}, {'cpc': 'H01', 'max_ema': 1.118271, 'best_year': 2018}, {'cpc': 'B60', 'max_ema': 1.1, 'best_year': 2014}, {'cpc': 'A61', 'max_ema': 1.0124410000000001, 'best_year': 2016}]}

exec(code, env_args)
