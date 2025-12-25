code = """import json
import re

with open(locals()['var_function-call-5448675020633306303'], 'r') as f:
    patents = json.load(f)

def parse_date(date_str):
    if not isinstance(date_str, str): return None, None
    y_match = re.search(r'\b(19|20)\d{2}\b', date_str)
    if not y_match: return None, None
    year = int(y_match.group(0))
    
    months = {
        'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
        'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
    }
    month = None
    lower_s = date_str.lower()
    for m_str, m_int in months.items():
        if m_str in lower_s:
            month = m_int
            break
    return year, month

cnt_2019 = 0
cnt_h2 = 0
cnt_both = 0
samples_de_check = []

for p in patents:
    gd = p.get('grant_date', '')
    y, m = parse_date(gd)
    if y == 2019:
        cnt_2019 += 1
        if m and m >= 7:
            cnt_h2 += 1
            info = p.get('Patents_info', '')
            is_de = False
            if re.search(r'\bDE\s*-\s*\d', info): is_de = True
            elif 'from DE' in info: is_de = True
            elif 'Germany' in info: is_de = True
            
            if is_de:
                cnt_both += 1
            
            if len(samples_de_check) < 5:
                samples_de_check.append((info, is_de))

res = {
    "total": len(patents),
    "cnt_2019": cnt_2019,
    "cnt_h2": cnt_h2,
    "cnt_both": cnt_both,
    "samples": samples_de_check
}
print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_function-call-16594278227079316675': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-16594278227079319092': 'file_storage/function-call-16594278227079319092.json', 'var_function-call-6081656753288550270': [{'level': '2.0', 'symbol': 'A', 'titleFull': 'HUMAN NECESSITIES'}, {'level': '4.0', 'symbol': 'A01', 'titleFull': 'AGRICULTURE; FORESTRY; ANIMAL HUSBANDRY; HUNTING; TRAPPING; FISHING'}, {'level': '4.0', 'symbol': 'A21', 'titleFull': 'BAKING; EDIBLE DOUGHS'}, {'level': '4.0', 'symbol': 'A22', 'titleFull': 'BUTCHERING; MEAT TREATMENT; PROCESSING POULTRY OR FISH'}, {'level': '4.0', 'symbol': 'A23', 'titleFull': 'FOODS OR FOODSTUFFS; TREATMENT THEREOF, NOT COVERED BY OTHER CLASSES'}, {'level': '4.0', 'symbol': 'A24', 'titleFull': "TOBACCO; CIGARS; CIGARETTES; SIMULATED SMOKING DEVICES; SMOKERS' REQUISITES"}, {'level': '4.0', 'symbol': 'A41', 'titleFull': 'WEARING APPAREL'}, {'level': '4.0', 'symbol': 'A42', 'titleFull': 'HEADWEAR'}, {'level': '4.0', 'symbol': 'A43', 'titleFull': 'FOOTWEAR'}, {'level': '4.0', 'symbol': 'A44', 'titleFull': 'HABERDASHERY; JEWELLERY'}, {'level': '4.0', 'symbol': 'A45', 'titleFull': 'HAND OR TRAVELLING ARTICLES'}, {'level': '4.0', 'symbol': 'A46', 'titleFull': 'BRUSHWARE'}, {'level': '4.0', 'symbol': 'A47', 'titleFull': 'FURNITURE; DOMESTIC ARTICLES OR APPLIANCES; COFFEE MILLS; SPICE MILLS; SUCTION CLEANERS IN GENERAL'}, {'level': '4.0', 'symbol': 'A61', 'titleFull': 'MEDICAL OR VETERINARY SCIENCE; HYGIENE'}, {'level': '4.0', 'symbol': 'A62', 'titleFull': 'LIFE-SAVING; FIRE-FIGHTING'}, {'level': '4.0', 'symbol': 'A63', 'titleFull': 'SPORTS; GAMES; AMUSEMENTS'}, {'level': '4.0', 'symbol': 'A99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION'}, {'level': '5.0', 'symbol': 'A01B', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'level': '5.0', 'symbol': 'A01C', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'level': '5.0', 'symbol': 'A01D', 'titleFull': 'HARVESTING; MOWING'}], 'var_function-call-5448675020633306303': 'file_storage/function-call-5448675020633306303.json', 'var_function-call-3965758477070812416': 'file_storage/function-call-3965758477070812416.json', 'var_function-call-14751869824581945649': []}

exec(code, env_args)
