code = """import json
import re
import pandas as pd

with open(locals()['var_function-call-6414003164698615798'], 'r') as f:
    data = json.load(f)

print("Total records:", len(data))

# Check DE matches
de_matches = []
for row in data:
    p_info = row.get('Patents_info', '')
    if re.search(r'\bDE[- ]', p_info) or "from DE" in p_info or "In DE" in p_info:
        de_matches.append(row)

print("DE matches:", len(de_matches))
if de_matches:
    print("Sample DE Patents_info:", de_matches[0]['Patents_info'])
    print("Sample DE Grant Date:", de_matches[0]['grant_date'])

# Test Date Parser on Sample
def parse_date(date_str):
    try:
        clean = re.sub(r'(dated|on|the|of|,)', '', date_str, flags=re.IGNORECASE)
        clean = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', clean)
        clean = " ".join(clean.split())
        return pd.to_datetime(clean)
    except:
        return None

if de_matches:
    print("Parsed Date:", parse_date(de_matches[0]['grant_date']))

# Check if any DE match is in H2 2019
count_h2_2019 = 0
for row in de_matches:
    d = parse_date(row.get('grant_date', ''))
    if d and d.year == 2019 and d.month >= 7:
        count_h2_2019 += 1

print("DE Matches in H2 2019:", count_h2_2019)

print("__RESULT__:")
print("done")"""

env_args = {'var_function-call-1868465921641692363': 'file_storage/function-call-1868465921641692363.json', 'var_function-call-6414003164698615067': [{'symbol': 'A01K2227/108', 'level': '9.0', 'titleFull': 'Swine'}], 'var_function-call-6414003164698615798': 'file_storage/function-call-6414003164698615798.json', 'var_function-call-4244802832919163477': [{'symbol': 'A', 'level': '2.0', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'A01', 'level': '4.0', 'titleFull': 'AGRICULTURE; FORESTRY; ANIMAL HUSBANDRY; HUNTING; TRAPPING; FISHING'}, {'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'G06F', 'level': '5.0', 'titleFull': 'ELECTRIC DIGITAL DATA PROCESSING'}, {'symbol': 'A01B1/00', 'level': '7.0', 'titleFull': 'Hand tools'}, {'symbol': 'G06F9/00', 'level': '7.0', 'titleFull': 'Arrangements for program control, e.g. control units'}], 'var_function-call-14093412893191991109': [], 'var_function-call-8691657811473980173': []}

exec(code, env_args)
