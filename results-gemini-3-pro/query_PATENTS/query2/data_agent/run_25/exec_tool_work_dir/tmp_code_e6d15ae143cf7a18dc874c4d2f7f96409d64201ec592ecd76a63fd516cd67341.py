code = """import re
import json

dates = ["14th Mar 2019", "2019 on Jul 12th", "on October 31st, 2019", "on November 5th, 2019", "8th Jan 2019"]

def parse_date(date_str):
    if not isinstance(date_str, str): return "NotStr", None
    y_match = re.search(r'\b(19|20)\d{2}\b', date_str)
    if not y_match: return "NoMatch", None
    year = int(y_match.group(0))
    return year, None

results = []
for d in dates:
    results.append(parse_date(d))

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-16594278227079316675': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-16594278227079319092': 'file_storage/function-call-16594278227079319092.json', 'var_function-call-6081656753288550270': [{'level': '2.0', 'symbol': 'A', 'titleFull': 'HUMAN NECESSITIES'}, {'level': '4.0', 'symbol': 'A01', 'titleFull': 'AGRICULTURE; FORESTRY; ANIMAL HUSBANDRY; HUNTING; TRAPPING; FISHING'}, {'level': '4.0', 'symbol': 'A21', 'titleFull': 'BAKING; EDIBLE DOUGHS'}, {'level': '4.0', 'symbol': 'A22', 'titleFull': 'BUTCHERING; MEAT TREATMENT; PROCESSING POULTRY OR FISH'}, {'level': '4.0', 'symbol': 'A23', 'titleFull': 'FOODS OR FOODSTUFFS; TREATMENT THEREOF, NOT COVERED BY OTHER CLASSES'}, {'level': '4.0', 'symbol': 'A24', 'titleFull': "TOBACCO; CIGARS; CIGARETTES; SIMULATED SMOKING DEVICES; SMOKERS' REQUISITES"}, {'level': '4.0', 'symbol': 'A41', 'titleFull': 'WEARING APPAREL'}, {'level': '4.0', 'symbol': 'A42', 'titleFull': 'HEADWEAR'}, {'level': '4.0', 'symbol': 'A43', 'titleFull': 'FOOTWEAR'}, {'level': '4.0', 'symbol': 'A44', 'titleFull': 'HABERDASHERY; JEWELLERY'}, {'level': '4.0', 'symbol': 'A45', 'titleFull': 'HAND OR TRAVELLING ARTICLES'}, {'level': '4.0', 'symbol': 'A46', 'titleFull': 'BRUSHWARE'}, {'level': '4.0', 'symbol': 'A47', 'titleFull': 'FURNITURE; DOMESTIC ARTICLES OR APPLIANCES; COFFEE MILLS; SPICE MILLS; SUCTION CLEANERS IN GENERAL'}, {'level': '4.0', 'symbol': 'A61', 'titleFull': 'MEDICAL OR VETERINARY SCIENCE; HYGIENE'}, {'level': '4.0', 'symbol': 'A62', 'titleFull': 'LIFE-SAVING; FIRE-FIGHTING'}, {'level': '4.0', 'symbol': 'A63', 'titleFull': 'SPORTS; GAMES; AMUSEMENTS'}, {'level': '4.0', 'symbol': 'A99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION'}, {'level': '5.0', 'symbol': 'A01B', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'level': '5.0', 'symbol': 'A01C', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'level': '5.0', 'symbol': 'A01D', 'titleFull': 'HARVESTING; MOWING'}], 'var_function-call-5448675020633306303': 'file_storage/function-call-5448675020633306303.json', 'var_function-call-3965758477070812416': 'file_storage/function-call-3965758477070812416.json', 'var_function-call-14751869824581945649': [], 'var_function-call-4071173780002865268': {'total': 216, 'cnt_2019': 0, 'cnt_h2': 0, 'cnt_both': 0, 'samples': []}, 'var_function-call-16385586842686664976': ['14th Mar 2019', '2019 on Jul 12th', 'on October 31st, 2019', 'on November 5th, 2019', '8th Jan 2019', 'dated 8th October 2019', 'July the 9th, 2019', 'August the 6th, 2019', 'Apr 2nd, 2019', 'dated 21st November 2019']}

exec(code, env_args)
