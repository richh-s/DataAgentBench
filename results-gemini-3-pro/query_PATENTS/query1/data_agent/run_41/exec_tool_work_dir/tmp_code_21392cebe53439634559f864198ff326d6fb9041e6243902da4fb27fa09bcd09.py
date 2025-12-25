code = """import json
import re
from collections import defaultdict

key1 = 'var_function-call-14088919373237144211'
key2 = 'var_function-call-14088919373237143530'

with open(locals()[key1], 'r') as f:
    level5_data = json.load(f)
    valid_level5 = set(item['symbol'] for item in level5_data)

with open(locals()[key2], 'r') as f:
    patent_data = json.load(f)

filings = defaultdict(lambda: defaultdict(int))
all_years = set()
year_pattern = re.compile(r'\b(19|20)\d{2}\b')

for row in patent_data:
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
            subclass = code[:4]
            if subclass in valid_level5:
                patent_codes.add(subclass)
    
    for code in patent_codes:
        filings[code][year] += 1

if not filings:
    print("__RESULT__:")
    print(json.dumps({"status": "No filings found matching Level 5 codes"}))
    exit()

min_year = min(all_years)
max_year = max(all_years)
alpha = 0.2

best_years_counts = defaultdict(int)
code_stats = []

for code in filings:
    counts = filings[code]
    current_ema = float(counts[min_year])
    max_ema = current_ema
    best_year = min_year
    
    # Re-calculate EMA
    for y in range(min_year + 1, max_year + 1):
        count = counts[y]
        current_ema = alpha * count + (1 - alpha) * current_ema
        if current_ema > max_ema: # Strict inequality
            max_ema = current_ema
            best_year = y
        elif current_ema == max_ema:
            # If tie, prefer later year?
            best_year = y

    best_years_counts[best_year] += 1
    code_stats.append({
        "code": code,
        "best_year": best_year,
        "max_ema": max_ema,
        "total_filings": sum(counts.values())
    })

# Sort by max_ema descending
code_stats.sort(key=lambda x: x['max_ema'], reverse=True)

print("__RESULT__:")
print(json.dumps({
    "best_years_distribution": best_years_counts,
    "top_5_codes": code_stats[:5],
    "level5_count": len(valid_level5),
    "codes_found_in_data": len(filings)
}))"""

env_args = {'var_function-call-12010284986386434738': 'file_storage/function-call-12010284986386434738.json', 'var_function-call-12010284986386434717': [{'symbol': 'A01H'}, {'symbol': 'A01F'}, {'symbol': 'A01C'}, {'symbol': 'A01G'}, {'symbol': 'A23J'}], 'var_function-call-7040256387500827623': [{'count(*)': '277813'}], 'var_function-call-5357179191043032962': [{'symbol': 'C01B33/00', 'level': '7.0', 'titleFull': 'Silicon; Compounds thereof'}, {'symbol': 'H01M10/0565', 'level': '11.0', 'titleFull': 'Polymeric materials, e.g. gel-type or solid-type'}, {'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}], 'var_function-call-2320558758355266598': [{'len': '4', 'count': '677'}], 'var_function-call-14088919373237144211': 'file_storage/function-call-14088919373237144211.json', 'var_function-call-14088919373237143530': 'file_storage/function-call-14088919373237143530.json', 'var_function-call-9751743124835996596': [], 'var_function-call-17846582241492215229': [], 'var_function-call-836893753941726447': {'sample_date_0': 'dated 5th March 2019', 'match_0': '2019', 'total_matches': 273258, 'total_rows': 277813}, 'var_function-call-6350488773007751466': {'2019': 11208, '2020': 11377, '2021': 13246, '2022': 11966, '2023': 6272, '2004': 5361, '1978': 1416, '1985': 1694, '2003': 5160, '1987': 1756, '2005': 5817, '2006': 6087, '2007': 6051, '2009': 5973, '2015': 9324, '2000': 3784, '2001': 4284, '2002': 4376, '1996': 2817, '2011': 5975, '2008': 6206, '2010': 5912, '2012': 6169, '2013': 6936, '2016': 14776, '2017': 16009, '2018': 17108, '1973': 1382, '1994': 2265, '2014': 8056, '1988': 1961, '1990': 2018, '1995': 2449, '1997': 3073, '1976': 1368, '1977': 1379, '1979': 1449, '1981': 1854, '1982': 1752, '1999': 3439, '1998': 2993, '1964': 648, '1965': 721, '1967': 753, '1969': 1012, '1970': 967, '1972': 1187, '1974': 1430, '1975': 1501, '1986': 1767, '1992': 1995, '1983': 1907, '1984': 1874, '1989': 1889, '1993': 2054, '1980': 1566, '1991': 1877, '1968': 811, '1971': 1044, '2024': 641, '1962': 501, '1952': 327, '1966': 751, '1955': 421, '1959': 450, '1960': 438, '1961': 459, '1909': 78, '1963': 494, '1919': 116, '1920': 144, '1921': 187, '1922': 141, '1958': 423, '1943': 258, '1918': 63, '1932': 182, '1929': 201, '1942': 199, '1957': 417, '1947': 296, '1931': 209, '1928': 193, '1940': 271, '1927': 164, '1937': 266, '1941': 273, '1933': 185, '1915': 118, '1948': 262, '1935': 272, '1923': 145, '1924': 149, '1925': 169, '1930': 208, '1934': 254, '1938': 328, '1939': 293, '1936': 294, '1944': 237, '1946': 283, '1949': 293, '1950': 307, '1951': 297, '1953': 307, '1954': 407, '1956': 448, '1907': 102, '1912': 194, '1914': 130, '1916': 110, '1917': 87, '1945': 243, '1926': 181, '1910': 75, '1911': 149, '1913': 194, '1904': 64, '1906': 103, '1903': 51, '1908': 82, '1905': 68, '1901': 26, '1900': 34, '1902': 45}}

exec(code, env_args)
