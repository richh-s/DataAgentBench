code = """import json
import re
import collections

# Load the large JSON result from the previous query
# var_function-call-8681905934765234662 is the key
file_path = locals()['var_function-call-8681905934765234662']

# Function to extract year
year_pattern = re.compile(r'\b(19\d{2}|20\d{2})\b')
def extract_year(date_str):
    if not date_str:
        return None
    match = year_pattern.search(date_str)
    if match:
        return int(match.group(1))
    return None

# Process data
# We need to count unique filings per subclass per year.
# Structure: Set of (rowid, subclass, year)
unique_filings = set()
subclasses = set()

# Reading the file line by line if it's a JSON list, or loading full json
# The helper returns a valid JSON string (list of dicts).
# If it's huge, json.load might use memory, but 100MB is fine.
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
            subclasses.add(subclass)

# Aggregate counts
# counts[subclass][year] = count
counts = collections.defaultdict(lambda: collections.defaultdict(int))

for _, subclass, year in unique_filings:
    counts[subclass][year] += 1

# Calculate EMA and find best year
alpha = 0.2
result_subclasses = []

# Global max year check to ensure we cover up to 2022 if data exists
all_years = {y for r, s, y in unique_filings}
if not all_years:
    print("__RESULT__:")
    print("[]")
    exit()

global_max_year = max(all_years)
# We need to ensure we evaluate up to at least 2022 if it's in the data.
# If 2022 is not in the data, then "best year is 2022" is impossible unless we assume 0 counts which would decrease EMA.
# Assuming data covers 2022.

for subclass in counts:
    sub_years = sorted(counts[subclass].keys())
    if not sub_years:
        continue
    
    start_year = sub_years[0]
    # We should run EMA up to the last year available for this subclass or global max?
    # Usually "best year" implies comparison against all years the technology is active.
    # If a technology stopped in 2010, its EMA decays. 
    # But if we stop calculating at 2010, the "best year" might be 2010.
    # If we extend to 2022 with 0s, it definitely won't be 2022.
    # However, if the question implies "active" technologies or just mathematical EMA...
    # Let's calculate EMA for the range [start_year, global_max_year].
    # This allows checking if 2022 (if active) is the peak.
    
    # Actually, if the best year is 2022, the EMA at 2022 must be >= EMA at any other year.
    
    ema_values = {}
    current_ema = None
    
    # Iterate from start_year to global_max_year
    for y in range(start_year, global_max_year + 1):
        count = counts[subclass].get(y, 0)
        if current_ema is None:
            current_ema = count
        else:
            current_ema = alpha * count + (1 - alpha) * current_ema
        ema_values[y] = current_ema
        
    # Find year with max EMA
    if not ema_values:
        continue
        
    best_y = max(ema_values, key=ema_values.get)
    
    if best_y == 2022:
        result_subclasses.append(subclass)

# Output result
print("__RESULT__:")
print(json.dumps(result_subclasses))"""

env_args = {'var_function-call-5009087051122217178': 'file_storage/function-call-5009087051122217178.json', 'var_function-call-5009087051122218151': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}], 'var_function-call-16623960229057700922': [{'level': '2.0', 'symbol': 'A', 'titleFull': 'HUMAN NECESSITIES'}, {'level': '2.0', 'symbol': 'B', 'titleFull': 'PERFORMING OPERATIONS; TRANSPORTING'}, {'level': '2.0', 'symbol': 'C', 'titleFull': 'CHEMISTRY; METALLURGY'}, {'level': '2.0', 'symbol': 'D', 'titleFull': 'TEXTILES; PAPER'}, {'level': '2.0', 'symbol': 'E', 'titleFull': 'FIXED CONSTRUCTIONS'}, {'level': '2.0', 'symbol': 'F', 'titleFull': 'MECHANICAL ENGINEERING; LIGHTING; HEATING; WEAPONS; BLASTING'}, {'level': '2.0', 'symbol': 'G', 'titleFull': 'PHYSICS'}, {'level': '2.0', 'symbol': 'H', 'titleFull': 'ELECTRICITY'}, {'level': '2.0', 'symbol': 'Y', 'titleFull': 'GENERAL TAGGING OF NEW TECHNOLOGICAL DEVELOPMENTS; GENERAL TAGGING OF CROSS-SECTIONAL TECHNOLOGIES SPANNING OVER SEVERAL SECTIONS OF THE IPC; TECHNICAL SUBJECTS COVERED BY FORMER USPC CROSS-REFERENCE ART COLLECTIONS [XRACs] AND DIGESTS'}, {'level': '4.0', 'symbol': 'A01', 'titleFull': 'AGRICULTURE; FORESTRY; ANIMAL HUSBANDRY; HUNTING; TRAPPING; FISHING'}, {'level': '4.0', 'symbol': 'A21', 'titleFull': 'BAKING; EDIBLE DOUGHS'}, {'level': '4.0', 'symbol': 'A22', 'titleFull': 'BUTCHERING; MEAT TREATMENT; PROCESSING POULTRY OR FISH'}, {'level': '4.0', 'symbol': 'A23', 'titleFull': 'FOODS OR FOODSTUFFS; TREATMENT THEREOF, NOT COVERED BY OTHER CLASSES'}, {'level': '4.0', 'symbol': 'A24', 'titleFull': "TOBACCO; CIGARS; CIGARETTES; SIMULATED SMOKING DEVICES; SMOKERS' REQUISITES"}, {'level': '4.0', 'symbol': 'A41', 'titleFull': 'WEARING APPAREL'}, {'level': '4.0', 'symbol': 'A42', 'titleFull': 'HEADWEAR'}, {'level': '4.0', 'symbol': 'A43', 'titleFull': 'FOOTWEAR'}, {'level': '4.0', 'symbol': 'A44', 'titleFull': 'HABERDASHERY; JEWELLERY'}, {'level': '4.0', 'symbol': 'A45', 'titleFull': 'HAND OR TRAVELLING ARTICLES'}, {'level': '4.0', 'symbol': 'A46', 'titleFull': 'BRUSHWARE'}], 'var_function-call-3772922055312996325': [{'level': '5.0', 'symbol': 'A62B'}, {'level': '5.0', 'symbol': 'A63G'}, {'level': '5.0', 'symbol': 'A63K'}, {'level': '5.0', 'symbol': 'A63B'}, {'level': '7.0', 'symbol': 'C13B50/00'}, {'level': '5.0', 'symbol': 'A63J'}, {'level': '5.0', 'symbol': 'A63C'}, {'level': '5.0', 'symbol': 'A63D'}, {'level': '5.0', 'symbol': 'A63F'}, {'level': '5.0', 'symbol': 'C25D'}, {'level': '5.0', 'symbol': 'A63H'}, {'level': '5.0', 'symbol': 'A99Z'}, {'level': '5.0', 'symbol': 'B01J'}, {'level': '5.0', 'symbol': 'B01B'}, {'level': '5.0', 'symbol': 'B01D'}, {'level': '5.0', 'symbol': 'B01L'}, {'level': '7.0', 'symbol': 'C13B40/00'}, {'level': '5.0', 'symbol': 'B01F'}, {'level': '5.0', 'symbol': 'B02C'}, {'level': '5.0', 'symbol': 'B02B'}], 'var_function-call-3504814913014613088': [{'COUNT(*)': '277813'}], 'var_function-call-7539642581129498440': [{'code': 'C01B33/00', 'filing_date': 'dated 5th March 2019'}, {'code': 'C01B35/00', 'filing_date': 'dated 5th March 2019'}, {'code': 'H01M10/0565', 'filing_date': 'dated 5th March 2019'}, {'code': 'H01M10/0562', 'filing_date': 'dated 5th March 2019'}, {'code': 'C01G45/006', 'filing_date': 'dated 5th March 2019'}, {'code': 'H01M10/0566', 'filing_date': 'dated 5th March 2019'}, {'code': 'H01M10/052', 'filing_date': 'dated 5th March 2019'}, {'code': 'C01P2002/76', 'filing_date': 'dated 5th March 2019'}, {'code': 'C01G45/006', 'filing_date': 'dated 5th March 2019'}, {'code': 'Y02E60/10', 'filing_date': 'dated 5th March 2019'}], 'var_function-call-17371980369775714343': [{'len': '4', 'cnt': '677'}], 'var_function-call-8681905934765234662': 'file_storage/function-call-8681905934765234662.json'}

exec(code, env_args)
