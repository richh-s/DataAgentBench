code = """import json
import re
from collections import defaultdict

key1 = 'var_function-call-14088919373237144211'
key2 = 'var_function-call-14088919373237143530'

with open(locals()[key1], 'r') as f:
    l5 = json.load(f)
valid_level5 = set(x['symbol'] for x in l5)

with open(locals()[key2], 'r') as f:
    pat = json.load(f)

filings = defaultdict(lambda: defaultdict(int))
all_years = set()
year_pattern = re.compile(r'(19|20)\d{2}')

for row in pat:
    fdate = row.get('filing_date', '')
    match = year_pattern.search(fdate)
    if not match:
        continue
    year = int(match.group(0))
    if year < 1900 or year > 2024:
        continue
    all_years.add(year)
    
    cpc_str = row.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
        
    patent_codes = set()
    for entry in cpc_list:
        code = entry.get('code', '')
        if len(code) >= 4:
            sub = code[:4]
            if sub in valid_level5:
                patent_codes.add(sub)
    
    for code in patent_codes:
        filings[code][year] += 1

if not filings:
    print("__RESULT__:")
    print(json.dumps("No filings"))
    exit()

min_year = min(all_years)
max_year = max(all_years)
alpha = 0.2

result_codes = []

# Collect stats for debug if needed
stats = []

for code, counts in filings.items():
    current_ema = float(counts[min_year])
    max_ema = current_ema
    best_year = min_year
    
    # Iterate ALL years from min to max to ensure continuity
    # Even if counts[y] is 0
    for y in range(min_year + 1, max_year + 1):
        count = counts[y] # defaultdict returns 0 if missing
        current_ema = alpha * count + (1 - alpha) * current_ema
        
        # Check max
        if current_ema >= max_ema: # Using >= to capture 2022 if it ties or peaks
            max_ema = current_ema
            best_year = y
            
    if best_year == 2022:
        result_codes.append(code)
    
    # Store stats for top check
    stats.append((code, best_year, max_ema))

print("__RESULT__:")
print(json.dumps(result_codes))"""

env_args = {'var_function-call-12010284986386434738': 'file_storage/function-call-12010284986386434738.json', 'var_function-call-12010284986386434717': [{'symbol': 'A01H'}, {'symbol': 'A01F'}, {'symbol': 'A01C'}, {'symbol': 'A01G'}, {'symbol': 'A23J'}], 'var_function-call-7040256387500827623': [{'count(*)': '277813'}], 'var_function-call-5357179191043032962': [{'symbol': 'C01B33/00', 'level': '7.0', 'titleFull': 'Silicon; Compounds thereof'}, {'symbol': 'H01M10/0565', 'level': '11.0', 'titleFull': 'Polymeric materials, e.g. gel-type or solid-type'}, {'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}], 'var_function-call-2320558758355266598': [{'len': '4', 'count': '677'}], 'var_function-call-14088919373237144211': 'file_storage/function-call-14088919373237144211.json', 'var_function-call-14088919373237143530': 'file_storage/function-call-14088919373237143530.json', 'var_function-call-9751743124835996596': [], 'var_function-call-17846582241492215229': [], 'var_function-call-836893753941726447': {'sample_date_0': 'dated 5th March 2019', 'match_0': '2019', 'total_matches': 273258, 'total_rows': 277813}, 'var_function-call-6350488773007751466': {'2019': 11208, '2020': 11377, '2021': 13246, '2022': 11966, '2023': 6272, '2004': 5361, '1978': 1416, '1985': 1694, '2003': 5160, '1987': 1756, '2005': 5817, '2006': 6087, '2007': 6051, '2009': 5973, '2015': 9324, '2000': 3784, '2001': 4284, '2002': 4376, '1996': 2817, '2011': 5975, '2008': 6206, '2010': 5912, '2012': 6169, '2013': 6936, '2016': 14776, '2017': 16009, '2018': 17108, '1973': 1382, '1994': 2265, '2014': 8056, '1988': 1961, '1990': 2018, '1995': 2449, '1997': 3073, '1976': 1368, '1977': 1379, '1979': 1449, '1981': 1854, '1982': 1752, '1999': 3439, '1998': 2993, '1964': 648, '1965': 721, '1967': 753, '1969': 1012, '1970': 967, '1972': 1187, '1974': 1430, '1975': 1501, '1986': 1767, '1992': 1995, '1983': 1907, '1984': 1874, '1989': 1889, '1993': 2054, '1980': 1566, '1991': 1877, '1968': 811, '1971': 1044, '2024': 641, '1962': 501, '1952': 327, '1966': 751, '1955': 421, '1959': 450, '1960': 438, '1961': 459, '1909': 78, '1963': 494, '1919': 116, '1920': 144, '1921': 187, '1922': 141, '1958': 423, '1943': 258, '1918': 63, '1932': 182, '1929': 201, '1942': 199, '1957': 417, '1947': 296, '1931': 209, '1928': 193, '1940': 271, '1927': 164, '1937': 266, '1941': 273, '1933': 185, '1915': 118, '1948': 262, '1935': 272, '1923': 145, '1924': 149, '1925': 169, '1930': 208, '1934': 254, '1938': 328, '1939': 293, '1936': 294, '1944': 237, '1946': 283, '1949': 293, '1950': 307, '1951': 297, '1953': 307, '1954': 407, '1956': 448, '1907': 102, '1912': 194, '1914': 130, '1916': 110, '1917': 87, '1945': 243, '1926': 181, '1910': 75, '1911': 149, '1913': 194, '1904': 64, '1906': 103, '1903': 51, '1908': 82, '1905': 68, '1901': 26, '1900': 34, '1902': 45}, 'var_function-call-8244782883574280520': {'status': 'No filings found matching Level 5 codes'}, 'var_function-call-14439990027404049667': 'Done', 'var_function-call-17469819292461381226': {'l5_sample': ['B63C', 'B61G', 'B66D', 'A99Z', 'C25B'], 'l5_count': 677, 'extracted_sample': ['C01B33/00', 'C01B35/00', 'H01M10/0565', 'H01M10/0562', 'C01G45/006', 'H01M10/0566', 'H01M10/052', 'C01P2002/76', 'C01G45/006', 'Y02E60/10'], 'matches_sample': [['C01B33/00', 'C01B'], ['C01B35/00', 'C01B'], ['H01M10/0565', 'H01M'], ['H01M10/0562', 'H01M'], ['C01G45/006', 'C01G']], 'matches_count': 555}, 'var_function-call-9494929963714392957': {'status': 'Empty filings', 'processed': 277813, 'matched': 0}, 'var_function-call-962936276071937748': 'Done', 'var_function-call-11965194435214804686': {'l5_count': 677, 'pat_count': 277813, 'first_match': 'No match found'}, 'var_function-call-11249045856800404113': {'index_0_subs': ['C01B', 'C01B', 'H01M', 'H01M', 'C01G', 'H01M', 'H01M', 'C01P', 'C01G', 'Y02E', 'C01P', 'H01M', 'H01M', 'H01M', 'H01M', 'H01M', 'C01B', 'H01M', 'H01M', 'H01M', 'H01M', 'C01B', 'H01M', 'H01M', 'C01B', 'H01M', 'C01B', 'C01P', 'H01M', 'H01M', 'H01M', 'H01M', 'H01M', 'H01M', 'H01M', 'H01M', 'H01M', 'C01G'], 'checks': {'C01B': True, 'H01M': True, 'C01G': True, 'C01P': True, 'Y02E': True}, 'C01B_in_set': True, 'sample_l5': ['B63G', 'F01K', 'B05C', 'B65G', 'G07C']}}

exec(code, env_args)
