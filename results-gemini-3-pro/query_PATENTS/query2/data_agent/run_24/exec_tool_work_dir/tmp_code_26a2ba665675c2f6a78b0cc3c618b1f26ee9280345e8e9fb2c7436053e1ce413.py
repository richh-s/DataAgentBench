code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-4816384186624279514'], 'r') as f:
    data = json.load(f)

print(f"Total records loaded: {len(data)}")

# Helper for date parsing
def parse_date(d_str):
    if not d_str:
        return None
    # Remove ordinal suffixes and common filler words
    clean = re.sub(r'\b(?:dated|on|of|the)\b', ' ', d_str, flags=re.IGNORECASE)
    clean = re.sub(r'(\d+)(?:st|nd|rd|th)\b', r'\1', clean, flags=re.IGNORECASE)
    clean = re.sub(r',', ' ', clean)
    clean = " ".join(clean.split())
    try:
        return pd.to_datetime(clean)
    except:
        return None

parsed_count = 0
in_range_count = 0
start_date = pd.Timestamp("2019-07-01")
end_date = pd.Timestamp("2019-12-31")

sample_parsed = []

for p in data[:100]:
    g_str = p.get('grant_date')
    d = parse_date(g_str)
    sample_parsed.append((g_str, str(d)))

for p in data:
    d = parse_date(p.get('grant_date'))
    if d:
        parsed_count += 1
        if start_date <= d <= end_date:
            in_range_count += 1

print(f"Parsed dates: {parsed_count}")
print(f"In range (2H 2019): {in_range_count}")
print("Sample parsed:")
print(json.dumps(sample_parsed[:10]))
print("__RESULT__:")
print(json.dumps("done"))"""

env_args = {'var_function-call-6891204174619872190': 'file_storage/function-call-6891204174619872190.json', 'var_function-call-6891204174619871375': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}, {'symbol': 'B99', 'level': '4.0', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION'}, {'symbol': 'B29', 'level': '4.0', 'titleFull': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL'}, {'symbol': 'B33', 'level': '4.0', 'titleFull': 'ADDITIVE MANUFACTURING TECHNOLOGY'}, {'symbol': 'C22', 'level': '4.0', 'titleFull': 'METALLURGY; FERROUS OR NON-FERROUS ALLOYS; TREATMENT OF ALLOYS OR NON-FERROUS METALS'}, {'symbol': 'D99', 'level': '4.0', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION'}], 'var_function-call-11482570988184779997': [{'symbol': 'A', 'level': '2.0', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'A01', 'level': '4.0', 'titleFull': 'AGRICULTURE; FORESTRY; ANIMAL HUSBANDRY; HUNTING; TRAPPING; FISHING'}, {'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'A01B1/00', 'level': '7.0', 'titleFull': 'Hand tools'}], 'var_function-call-11482570988184779666': [{'Patents_info': 'VITTORI GIANFRANCO DE holds the FR patent filing (app. number FR-7811408-A), with publication number FR-2388575-B3.', 'grant_date': '1980 on Nov 14th'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.', 'grant_date': '2006 on Apr 27th'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.', 'grant_date': 'Nov 29th, 2007'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.', 'grant_date': '2009, January 29th'}, {'Patents_info': 'MITUTOYO CORP holds the DE patent filing (app. number DE-10037981-A), with pub. number DE-10037981-B4.', 'grant_date': '19th of October, 2017'}], 'var_function-call-4816384186624279514': 'file_storage/function-call-4816384186624279514.json', 'var_function-call-841467299861445762': [{'cpc_group': 'A61', 'best_year': 2016, 'max_ema': 0.1}, {'cpc_group': 'B29', 'best_year': 2007, 'max_ema': 1.0}, {'cpc_group': 'G02', 'best_year': 2016, 'max_ema': 0.1}]}

exec(code, env_args)
