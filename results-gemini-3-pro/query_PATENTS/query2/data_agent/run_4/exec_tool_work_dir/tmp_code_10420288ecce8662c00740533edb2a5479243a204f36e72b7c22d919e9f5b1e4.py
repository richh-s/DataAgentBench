code = """import json
import pandas as pd
import re

patents_path = locals()['var_function-call-16435967301398580660']
with open(patents_path, 'r') as f:
    patents = json.load(f)

de_pattern = re.compile(r'\bfrom DE\b|\bDE-\d+')

count_total = len(patents)
count_de = 0
count_date = 0
count_h2_2019 = 0

def parse_date(date_str):
    clean = re.sub(r'(st|nd|rd|th|on|dated|,|of|the)', '', date_str)
    # "14 Mar 2019"
    # "2019  Jul 12"
    try:
        return pd.to_datetime(clean).date()
    except:
        return None

sample_dates = []

for p in patents[:1000]:
    matches_de = bool(de_pattern.search(p.get('Patents_info', '')))
    if matches_de:
        count_de += 1
    
    g_str = p.get('grant_date', '')
    g_date = parse_date(g_str)
    if g_date:
        count_date += 1
        if g_date.year == 2019 and g_date.month >= 7:
            count_h2_2019 += 1
    else:
        if matches_de and len(sample_dates) < 5:
            sample_dates.append(g_str)

print("__RESULT__:")
print(json.dumps({
    "total": count_total,
    "matches_de": count_de,
    "parsed_dates_in_subset": count_date,
    "h2_2019": count_h2_2019,
    "failed_dates": sample_dates
}))"""

env_args = {'var_function-call-9027804141299956237': ['publicationinfo'], 'var_function-call-9027804141299956054': ['cpc_definition'], 'var_function-call-13891800015006892835': 'file_storage/function-call-13891800015006892835.json', 'var_function-call-13748478948310889332': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0'}], 'var_function-call-6605672204215736455': [{'symbol': 'B', 'level': '2.0'}, {'symbol': 'H', 'level': '2.0'}, {'symbol': 'Y', 'level': '2.0'}, {'symbol': 'D', 'level': '2.0'}, {'symbol': 'F', 'level': '2.0'}, {'symbol': 'E', 'level': '2.0'}, {'symbol': 'C', 'level': '2.0'}, {'symbol': 'G', 'level': '2.0'}, {'symbol': 'A', 'level': '2.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}], 'var_function-call-8398798029853849913': [], 'var_function-call-7499511620997998355': [{'level': '2.0'}, {'level': '4.0'}, {'level': '5.0'}, {'level': '7.0'}, {'level': '8.0'}, {'level': '9.0'}, {'level': '10.0'}, {'level': '11.0'}, {'level': '12.0'}, {'level': '13.0'}, {'level': '14.0'}, {'level': '15.0'}, {'level': '16.0'}, {'level': '17.0'}, {'level': '18.0'}, {'level': '19.0'}], 'var_function-call-3699617742520592814': [{'symbol': 'C01', 'titleFull': 'INORGANIC CHEMISTRY'}], 'var_function-call-16435967301398580660': 'file_storage/function-call-16435967301398580660.json', 'var_function-call-11235697834189481417': [{'symbol': 'A01', 'len': '3'}, {'symbol': 'A21', 'len': '3'}, {'symbol': 'A22', 'len': '3'}, {'symbol': 'A23', 'len': '3'}, {'symbol': 'A24', 'len': '3'}, {'symbol': 'A41', 'len': '3'}, {'symbol': 'A42', 'len': '3'}, {'symbol': 'A43', 'len': '3'}, {'symbol': 'A44', 'len': '3'}, {'symbol': 'A45', 'len': '3'}], 'var_function-call-12448420585321566256': [], 'var_function-call-5294950170102655327': 'file_storage/function-call-5294950170102655327.json', 'var_function-call-4570370100524341779': []}

exec(code, env_args)
