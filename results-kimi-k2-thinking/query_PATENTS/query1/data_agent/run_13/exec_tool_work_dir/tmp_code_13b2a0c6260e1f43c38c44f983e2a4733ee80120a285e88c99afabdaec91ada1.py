code = """import json
import ast
import re
from collections import defaultdict, Counter

# Load patent data to analyze CPC structure
patent_file = locals()['var_functions.query_db:2']
with open(patent_file, 'r') as f:
    patent_data = json.load(f)

# Extract CPC codes and analyze prefixes
patent_prefixes = Counter()
patent_full_codes = set()

for record in patent_data[:10000]:  # Sample first 10k records
    cpc_str = record.get('cpc', '')
    if not cpc_str:
        continue
    try:
        cpc_list = ast.literal_eval(cpc_str)
        for cpc_entry in cpc_list:
            if isinstance(cpc_entry, dict) and 'code' in cpc_entry:
                code = cpc_entry['code']
                patent_full_codes.add(code)
                if len(code) >= 4:
                    prefix = code[:4]
                    patent_prefixes[prefix] += 1
    except:
        pass

print("Unique CPC prefixes in patent sample:", len(patent_prefixes))
print("Sample prefixes:", list(patent_prefixes.keys())[:20])
print("Sample full codes:", list(patent_full_codes)[:20])

# Load CPC level 5 symbols
cpc_file = locals()['var_functions.query_db:3']
with open(cpc_file, 'r') as f:
    cpc_level5_data = json.load(f)
cpc_symbols = set(item['symbol'] for item in cpc_level5_data)

print("Level 5 CPC symbols:", len(cpc_symbols))
print("Sample level 5 symbols:", sorted(list(cpc_symbols))[:20])

# Check matches using different prefix lengths
def check_prefix_matches(prefix_length):
    patent_prefixes_n = set(code[:prefix_length] for code in patent_full_codes if len(code) >= prefix_length)
    overlap = cpc_symbols.intersection(patent_prefixes_n)
    return len(overlap), list(overlap)[:10]

for length in [3, 4, 5, 6, 7]:
    count, sample = check_prefix_matches(length)
    print(f"Prefix length {length}: {count} matches, sample: {sample}")

# Check if any level 5 symbols are prefixes of patent CPC codes
def is_prefix_match(cpc_code, level5_symbols):
    for symbol in level5_symbols:
        if cpc_code.startswith(symbol):
            return True, symbol
    return False, None

matches = 0
match_examples = []
for code in list(patent_full_codes)[:1000]:
    is_match, matched_symbol = is_prefix_match(code, cpc_symbols)
    if is_match:
        matches += 1
        if len(match_examples) < 10:
            match_examples.append((code, matched_symbol))

print(f"\nDirect prefix matches in sample: {matches}")
print("Match examples:", match_examples)

# Try matching by taking first part before slash
slash_matches = 0
slash_examples = []
for code in list(patent_full_codes)[:1000]:
    if '/' in code:
        main_group = code.split('/')[0]
        if main_group in cpc_symbols:
            slash_matches += 1
            if len(slash_examples) < 10:
                slash_examples.append(code)

print(f"\nSlash-separated matches: {slash_matches}")
print("Examples:", slash_examples)

print('__RESULT__:')
print(json.dumps({"matches_found": matches > 0}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json', 'var_functions.execute_python:18': [], 'var_functions.execute_python:20': {'cpc_symbols_sample': ['A01H', 'A01F', 'A01C', 'A01G', 'A23J', 'A01N', 'A01P', 'A01D', 'A01L', 'A01K', 'A01M', 'A01J', 'A01B', 'A21D', 'A21C', 'A21B', 'A22B', 'A22C', 'A23P', 'A23C'], 'patent_cpc_samples': [], 'available_years': [1837, 1839, 1841, 1842, 1843, 1844, 1845, 1846, 1847, 1848, 1849, 1850, 1851, 1852, 1853, 1854, 1855, 1856, 1857, 1858, 1859, 1860, 1861, 1862, 1863, 1864, 1865, 1866, 1867, 1868, 1869, 1870, 1871, 1872, 1873, 1874, 1875, 1876, 1877, 1878, 1879, 1880, 1881, 1882, 1883, 1884, 1885, 1886, 1887, 1888, 1889, 1890, 1891, 1892, 1893, 1894, 1895, 1896, 1897, 1898, 1899, 1900, 1901, 1902, 1903, 1904, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1916, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1926, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939, 1940, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]}, 'var_functions.query_db:22': [{'symbol': 'A01H'}, {'symbol': 'A01F'}, {'symbol': 'A01C'}, {'symbol': 'A01G'}, {'symbol': 'A23J'}, {'symbol': 'A01N'}, {'symbol': 'A01P'}, {'symbol': 'A01D'}, {'symbol': 'A01L'}, {'symbol': 'A01K'}], 'var_functions.list_db:24': ['cpc_definition'], 'var_functions.execute_python:28': {'patent_records_total': 277813, 'records_by_year': {'2021': 16079, '2020': 13210, '2023': 14217, '2022': 16012, '2024': 7535, '2007': 5256, '1980': 1352, '1988': 1782, '2004': 4595, '1990': 1851, '2006': 5487, '2009': 6087, '2010': 5890, '2016': 10928, '2017': 13795, '2005': 5070, '2011': 5631, '2012': 5507, '2008': 5705, '2015': 8453, '2013': 5816, '2014': 7171, '2019': 13350, '1975': 1412, '1999': 2963, '2018': 16293, '1989': 1882, '1992': 1823, '1995': 2042, '2002': 3888, '2003': 4003, '1997': 2018, '1998': 2643, '1983': 1673, '1986': 1847, '1982': 1659, '1996': 2171, '2000': 3100, '1974': 1313, '1978': 1339, '1979': 1360, '1985': 1880, '1973': 1224, '1987': 1648, '2001': 3407, '1984': 1716, '1991': 1916, '1993': 1832, '1994': 1965, '1976': 1447, '1977': 1246, '1972': 865, '1971': 915, '1981': 1314, '1967': 676, '1968': 695, '1970': 876, '1955': 266, '1966': 691, '1969': 831, '1957': 416, '1841': 4, '1843': 2, '1960': 473, '1965': 590, '1964': 482, '1963': 415, '1910': 56, '1920': 112, '1921': 121, '1922': 160, '1923': 165, '1961': 457, '1945': 204, '1919': 88, '1933': 187, '1930': 196, '1962': 491, '1943': 207, '1959': 494, '1949': 229, '1932': 235, '1928': 169, '1941': 310, '1937': 271, '1934': 176, '1854': 3, '1915': 151, '1860': 13, '1863': 12, '1865': 12, '1936': 278, '1866': 26, '1918': 91, '1867': 18, '1951': 367, '1938': 273, '1869': 25, '1900': 114, '1924': 153, '1925': 172, '1926': 172, '1927': 167, '1929': 164, '1935': 212, '1939': 303, '1940': 271, '1942': 251, '1944': 229, '1946': 166, '1947': 166, '1948': 184, '1950': 299, '1952': 349, '1954': 315, '1956': 335, '1958': 468, '1908': 97, '1909': 84, '1913': 186, '1914': 266, '1917': 107, '1931': 208, '1870': 34, '1874': 26, '1875': 24, '1876': 28, '1877': 29, '1878': 50, '1879': 71, '1880': 56, '1953': 355, '1881': 69, '1882': 105, '1883': 89, '1884': 88, '1916': 109, '1885': 92, '1886': 86, '1887': 79, '1888': 86, '1889': 91, '1890': 101, '1891': 81, '1892': 102, '1894': 66, '1895': 61, '1896': 46, '1897': 51, '1898': 45, '1899': 44, '1902': 34, '1904': 60, '1912': 101, '1837': 2, '1846': 2, '1849': 1, '1852': 1, '1905': 41, '1906': 62, '1856': 6, '1857': 3, '1858': 16, '1868': 16, '1903': 58, '1907': 118, '1871': 32, '1872': 27, '1873': 22, '1893': 62, '1911': 60, '1859': 15, '1901': 23, '1855': 4, '1847': 2, '1862': 7, '1864': 11, '1850': 2, '1853': 3, '1851': 1, '1861': 11, '1848': 2, '1842': 5, '1845': 1, '1844': 3, '1839': 2}, 'cpc_level5_count': 677, 'cpc_samples': [{'record': 0, 'cpc_type': "<class 'str'>", 'cpc_preview': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"'}, {'record': 1, 'cpc_type': "<class 'str'>", 'cpc_preview': '[\n  {\n    "code": "F16H47/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H37/08",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"'}, {'record': 2, 'cpc_type': "<class 'str'>", 'cpc_preview': '[\n  {\n    "code": "B29C70/48",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C08J5/246",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code":'}]}, 'var_functions.execute_python:32': [], 'var_functions.execute_python:36': [], 'var_functions.execute_python:38': [], 'var_functions.execute_python:42': [], 'var_functions.execute_python:48': [], 'var_functions.execute_python:54': [], 'var_functions.execute_python:56': [], 'var_functions.query_db:58': [{'symbol': 'C13B50/00', 'level': '7.0'}, {'symbol': 'C13B40/00', 'level': '7.0'}, {'symbol': 'C13B99/00', 'level': '7.0'}, {'symbol': 'C13B45/00', 'level': '7.0'}, {'symbol': 'A01B59/00', 'level': '7.0'}, {'symbol': 'H10N89/02', 'level': '8.0'}, {'symbol': 'A01B19/00', 'level': '7.0'}, {'symbol': 'A01B35/00', 'level': '7.0'}, {'symbol': 'C13B25/00', 'level': '7.0'}, {'symbol': 'C13K11/00', 'level': '7.0'}, {'symbol': 'C13K13/00', 'level': '7.0'}, {'symbol': 'C14B21/00', 'level': '7.0'}, {'symbol': 'C14B99/00', 'level': '7.0'}, {'symbol': 'C14B11/00', 'level': '7.0'}, {'symbol': 'C14B15/00', 'level': '7.0'}, {'symbol': 'C14B13/00', 'level': '7.0'}, {'symbol': 'C14B19/00', 'level': '7.0'}, {'symbol': 'F16M11/00', 'level': '7.0'}, {'symbol': 'A01B13/00', 'level': '7.0'}, {'symbol': 'A01B67/00', 'level': '7.0'}], 'var_functions.list_db:60': ['cpc_definition'], 'var_functions.query_db:62': [{'symbol': 'G01J', 'level': '5.0'}, {'symbol': 'G01R', 'level': '5.0'}, {'symbol': 'G01P', 'level': '5.0'}, {'symbol': 'G01M', 'level': '5.0'}, {'symbol': 'G01N', 'level': '5.0'}, {'symbol': 'G01F', 'level': '5.0'}, {'symbol': 'G01B', 'level': '5.0'}, {'symbol': 'G01H', 'level': '5.0'}, {'symbol': 'H04L', 'level': '5.0'}, {'symbol': 'G01G', 'level': '5.0'}, {'symbol': 'G01T', 'level': '5.0'}, {'symbol': 'G01L', 'level': '5.0'}, {'symbol': 'G01S', 'level': '5.0'}, {'symbol': 'G01K', 'level': '5.0'}, {'symbol': 'G01W', 'level': '5.0'}, {'symbol': 'G02F', 'level': '5.0'}, {'symbol': 'G02B', 'level': '5.0'}, {'symbol': 'G02C', 'level': '5.0'}, {'symbol': 'G03B', 'level': '5.0'}, {'symbol': 'G03D', 'level': '5.0'}, {'symbol': 'G03H', 'level': '5.0'}, {'symbol': 'G03C', 'level': '5.0'}, {'symbol': 'G03F', 'level': '5.0'}, {'symbol': 'G03G', 'level': '5.0'}, {'symbol': 'G04B', 'level': '5.0'}, {'symbol': 'G04R', 'level': '5.0'}, {'symbol': 'G04D', 'level': '5.0'}, {'symbol': 'G04F', 'level': '5.0'}, {'symbol': 'G04C', 'level': '5.0'}, {'symbol': 'G04G', 'level': '5.0'}, {'symbol': 'G05D', 'level': '5.0'}, {'symbol': 'G05G', 'level': '5.0'}, {'symbol': 'G05B', 'level': '5.0'}, {'symbol': 'G05F', 'level': '5.0'}, {'symbol': 'G06N', 'level': '5.0'}, {'symbol': 'G06F', 'level': '5.0'}, {'symbol': 'G06K', 'level': '5.0'}, {'symbol': 'G06Q', 'level': '5.0'}, {'symbol': 'G06E', 'level': '5.0'}, {'symbol': 'G06M', 'level': '5.0'}, {'symbol': 'G06V', 'level': '5.0'}, {'symbol': 'G06J', 'level': '5.0'}, {'symbol': 'G06G', 'level': '5.0'}, {'symbol': 'G06C', 'level': '5.0'}, {'symbol': 'G10K', 'level': '5.0'}, {'symbol': 'G06T', 'level': '5.0'}, {'symbol': 'G06D', 'level': '5.0'}, {'symbol': 'G07D', 'level': '5.0'}, {'symbol': 'G07C', 'level': '5.0'}, {'symbol': 'G10F', 'level': '5.0'}], 'var_functions.execute_python:64': [], 'var_functions.execute_python:66': [], 'var_functions.execute_python:70': []}

exec(code, env_args)
