code = """import json
import re
import collections

file_path = locals()['var_function-call-8681905934765234662']
year_pattern = re.compile(r'(19|20)\d{2}')

def extract_year(date_str):
    if not date_str:
        return None
    match = year_pattern.search(date_str)
    if match:
        return int(match.group(0))
    return None

unique_filings = set()
with open(file_path, 'r') as f:
    data = json.load(f)

for row in data:
    subclass = row.get('subclass')
    date_str = row.get('filing_date')
    rowid = row.get('rowid')
    if subclass and date_str and rowid:
        year = extract_year(date_str)
        if year:
            unique_filings.add((rowid, subclass, year))

counts = collections.defaultdict(lambda: collections.defaultdict(int))
for _, subclass, year in unique_filings:
    counts[subclass][year] += 1

all_years = {y for r, s, y in unique_filings}
if not all_years:
    print("__RESULT__:")
    print("[]")
    exit()

global_max_year = max(all_years)
# Assuming the user considers "best year 2022" relative to the available history.
# If global max is < 2022, return empty.
if global_max_year < 2022:
    # If the data doesn't reach 2022, we can't say 2022 is the best year (unless we project, which we shouldn't).
    # But let's check what the global max is first.
    pass

result_subclasses = []
alpha = 0.2

for subclass in counts:
    # Get range for this subclass
    sub_years = sorted(counts[subclass].keys())
    start_year = sub_years[0]
    
    # Calculate EMA
    ema_values = {}
    curr = None
    
    # We iterate from start_year to global_max_year
    # This handles years with 0 filings by carrying over the decay
    for y in range(start_year, global_max_year + 1):
        c = counts[subclass].get(y, 0)
        if curr is None:
            curr = c
        else:
            curr = alpha * c + (1 - alpha) * curr
        ema_values[y] = curr
            
    # Find best year
    best_y = max(ema_values, key=ema_values.get)
    
    if best_y == 2022:
        result_subclasses.append(subclass)

print("__RESULT__:")
print(json.dumps(result_subclasses))"""

env_args = {'var_function-call-5009087051122217178': 'file_storage/function-call-5009087051122217178.json', 'var_function-call-5009087051122218151': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}], 'var_function-call-16623960229057700922': [{'level': '2.0', 'symbol': 'A', 'titleFull': 'HUMAN NECESSITIES'}, {'level': '2.0', 'symbol': 'B', 'titleFull': 'PERFORMING OPERATIONS; TRANSPORTING'}, {'level': '2.0', 'symbol': 'C', 'titleFull': 'CHEMISTRY; METALLURGY'}, {'level': '2.0', 'symbol': 'D', 'titleFull': 'TEXTILES; PAPER'}, {'level': '2.0', 'symbol': 'E', 'titleFull': 'FIXED CONSTRUCTIONS'}, {'level': '2.0', 'symbol': 'F', 'titleFull': 'MECHANICAL ENGINEERING; LIGHTING; HEATING; WEAPONS; BLASTING'}, {'level': '2.0', 'symbol': 'G', 'titleFull': 'PHYSICS'}, {'level': '2.0', 'symbol': 'H', 'titleFull': 'ELECTRICITY'}, {'level': '2.0', 'symbol': 'Y', 'titleFull': 'GENERAL TAGGING OF NEW TECHNOLOGICAL DEVELOPMENTS; GENERAL TAGGING OF CROSS-SECTIONAL TECHNOLOGIES SPANNING OVER SEVERAL SECTIONS OF THE IPC; TECHNICAL SUBJECTS COVERED BY FORMER USPC CROSS-REFERENCE ART COLLECTIONS [XRACs] AND DIGESTS'}, {'level': '4.0', 'symbol': 'A01', 'titleFull': 'AGRICULTURE; FORESTRY; ANIMAL HUSBANDRY; HUNTING; TRAPPING; FISHING'}, {'level': '4.0', 'symbol': 'A21', 'titleFull': 'BAKING; EDIBLE DOUGHS'}, {'level': '4.0', 'symbol': 'A22', 'titleFull': 'BUTCHERING; MEAT TREATMENT; PROCESSING POULTRY OR FISH'}, {'level': '4.0', 'symbol': 'A23', 'titleFull': 'FOODS OR FOODSTUFFS; TREATMENT THEREOF, NOT COVERED BY OTHER CLASSES'}, {'level': '4.0', 'symbol': 'A24', 'titleFull': "TOBACCO; CIGARS; CIGARETTES; SIMULATED SMOKING DEVICES; SMOKERS' REQUISITES"}, {'level': '4.0', 'symbol': 'A41', 'titleFull': 'WEARING APPAREL'}, {'level': '4.0', 'symbol': 'A42', 'titleFull': 'HEADWEAR'}, {'level': '4.0', 'symbol': 'A43', 'titleFull': 'FOOTWEAR'}, {'level': '4.0', 'symbol': 'A44', 'titleFull': 'HABERDASHERY; JEWELLERY'}, {'level': '4.0', 'symbol': 'A45', 'titleFull': 'HAND OR TRAVELLING ARTICLES'}, {'level': '4.0', 'symbol': 'A46', 'titleFull': 'BRUSHWARE'}], 'var_function-call-3772922055312996325': [{'level': '5.0', 'symbol': 'A62B'}, {'level': '5.0', 'symbol': 'A63G'}, {'level': '5.0', 'symbol': 'A63K'}, {'level': '5.0', 'symbol': 'A63B'}, {'level': '7.0', 'symbol': 'C13B50/00'}, {'level': '5.0', 'symbol': 'A63J'}, {'level': '5.0', 'symbol': 'A63C'}, {'level': '5.0', 'symbol': 'A63D'}, {'level': '5.0', 'symbol': 'A63F'}, {'level': '5.0', 'symbol': 'C25D'}, {'level': '5.0', 'symbol': 'A63H'}, {'level': '5.0', 'symbol': 'A99Z'}, {'level': '5.0', 'symbol': 'B01J'}, {'level': '5.0', 'symbol': 'B01B'}, {'level': '5.0', 'symbol': 'B01D'}, {'level': '5.0', 'symbol': 'B01L'}, {'level': '7.0', 'symbol': 'C13B40/00'}, {'level': '5.0', 'symbol': 'B01F'}, {'level': '5.0', 'symbol': 'B02C'}, {'level': '5.0', 'symbol': 'B02B'}], 'var_function-call-3504814913014613088': [{'COUNT(*)': '277813'}], 'var_function-call-7539642581129498440': [{'code': 'C01B33/00', 'filing_date': 'dated 5th March 2019'}, {'code': 'C01B35/00', 'filing_date': 'dated 5th March 2019'}, {'code': 'H01M10/0565', 'filing_date': 'dated 5th March 2019'}, {'code': 'H01M10/0562', 'filing_date': 'dated 5th March 2019'}, {'code': 'C01G45/006', 'filing_date': 'dated 5th March 2019'}, {'code': 'H01M10/0566', 'filing_date': 'dated 5th March 2019'}, {'code': 'H01M10/052', 'filing_date': 'dated 5th March 2019'}, {'code': 'C01P2002/76', 'filing_date': 'dated 5th March 2019'}, {'code': 'C01G45/006', 'filing_date': 'dated 5th March 2019'}, {'code': 'Y02E60/10', 'filing_date': 'dated 5th March 2019'}], 'var_function-call-17371980369775714343': [{'len': '4', 'cnt': '677'}], 'var_function-call-8681905934765234662': 'file_storage/function-call-8681905934765234662.json', 'var_function-call-9855483480759291362': [], 'var_function-call-16594887014080317566': {'error': 'No years found'}, 'var_function-call-103896030704302249': '[\n  {\n    "rowid": "1",\n    "subclass": "C01B",\n    "filing_date": "dated 5th March 2019"\n  },\n  {\n    "rowid": "1",\n    "subclass": "C01B",\n    "filing_date": "dated 5th March 2019"\n  },\n  {\n    "rowid": "1",\n    "subclass": "H01M",\n    "filing_date": "dated 5th March 2019"\n  },\n  {\n    "rowid": "1",\n    "subclass": "H01M",\n    "filing_date": "dated 5th March 2019"\n  },\n  {\n    "rowid": "1",\n    "subclass": "C01G",\n    "filing_date": "dated 5th March 2019"\n  },\n  {\n    "rowid": "1",\n    "subclass": "H01M",\n    "filing_date": "dated 5th March 2019"\n  },\n  {\n    "rowid": "1",\n    "subclass": "H01M",\n    "filing_date": "dated 5th March 2019"\n  },\n  {\n    "rowid": "1",\n    "subclass": "C01P",\n    "filing_date": "dated 5th March 2019"\n  },\n  {\n    "rowid": "1",\n    "subclass": "C01G",\n    "filing_date": "dated 5th March 2019"\n  },\n  {\n    "rowid": "1",\n    "subclass": "Y02E",\n    "filing_date": "dated 5th March 2019"\n  },\n  {\n    "rowid": "1",\n    "subclass": "C01P",\n    "filing_date": "da', 'var_function-call-12307818636556348709': {'match': None}, 'var_function-call-14995663821364844276': {'match': '2019'}}

exec(code, env_args)
