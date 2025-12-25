code = """import json
import re

with open(locals()['var_function-call-11543888931216263098'], 'r') as f:
    data = json.load(f)

print(f"Total records: {len(data)}")

def parse_date_to_year_month(date_str):
    months = {
        'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6,
        'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12,
        'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'jun': 6, 'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
    }
    date_str = date_str.lower()
    year_match = re.search(r'\b(19|20)\d{2}\b', date_str)
    if not year_match:
        return None, None
    year = int(year_match.group(0))
    month = None
    for m_name, m_num in months.items():
        if m_name in date_str:
            month = m_num
            break
    return year, month

# Debug first 5
for i, record in enumerate(data[:5]):
    g_date = record.get('grant_date', '')
    g_year, g_month = parse_date_to_year_month(g_date)
    f_date = record.get('filing_date', '')
    f_year, f_month = parse_date_to_year_month(f_date)
    cpc_raw = record.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_raw)
        cpc_count = len(cpc_list)
    except:
        cpc_count = "Error"
    
    print(f"Rec {i}: Grant: {g_date} -> ({g_year}, {g_month}); Filing: {f_date} -> ({f_year}); CPC Items: {cpc_count}")

# Check filter counts
count_grant = 0
count_de = 0
count_filing = 0
count_cpc = 0

for record in data:
    g_date = record.get('grant_date', '')
    g_year, g_month = parse_date_to_year_month(g_date)
    if g_year == 2019 and g_month is not None and g_month >= 7:
        count_grant += 1
        if 'DE' in record.get('Patents_info', ''):
            count_de += 1
            if parse_date_to_year_month(record.get('filing_date', ''))[0] is not None:
                count_filing += 1
                try:
                    c = json.loads(record.get('cpc', '[]'))
                    if c: count_cpc += 1
                except: pass

print(f"Passed Grant Filter: {count_grant}")
print(f"Passed DE Filter: {count_de}")
print(f"Passed Filing Date: {count_filing}")
print(f"Passed CPC: {count_cpc}")

print("__RESULT__:")
print("done")"""

env_args = {'var_function-call-4774163761277503972': 'file_storage/function-call-4774163761277503972.json', 'var_function-call-12755170999949966242': ['publicationinfo'], 'var_function-call-17983425627878789748': [{'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.'}, {'Patents_info': 'In DE, the patent application (no. DE-10130631-A) is owned by SCHNEIDER SIEGHARD and has publication number DE-10130631-B4.'}, {'Patents_info': 'The DE patent application (no. DE-10134061-A) is belonging to MOSMATIC AG NECKER and has publication number DE-10134061-B4.'}, {'Patents_info': 'In DE, the patent application (no. DE-10147111-A) is belonging to VISTEON GLOBAL TECH INC and has publication number DE-10147111-B4.'}], 'var_function-call-3520023833909275240': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-14298847436406348240': 'file_storage/function-call-14298847436406348240.json', 'var_function-call-17296021972275604149': [{'symbol': 'B', 'level': '2.0', 'titleFull': 'PERFORMING OPERATIONS; TRANSPORTING'}, {'symbol': 'B04B', 'level': '5.0', 'titleFull': 'CENTRIFUGES'}, {'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}], 'var_function-call-11543888931216263098': 'file_storage/function-call-11543888931216263098.json', 'var_function-call-16387991390808413708': 'file_storage/function-call-16387991390808413708.json', 'var_function-call-1586333864231123704': []}

exec(code, env_args)
