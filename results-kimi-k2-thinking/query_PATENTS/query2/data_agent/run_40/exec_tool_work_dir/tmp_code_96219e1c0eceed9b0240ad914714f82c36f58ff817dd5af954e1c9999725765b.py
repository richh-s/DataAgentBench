code = """import json
import re
from collections import defaultdict

# Load all German patents
all_patents_path = locals()['var_functions.query_db:62']
with open(all_patents_path, 'r') as f:
    all_german_patents = json.load(f)

# Build historical counts for CPC level 4 groups
cpc_year_counts = defaultdict(lambda: defaultdict(int))

for patent in all_german_patents:
    grant_date = patent.get('grant_date', '')
    if not grant_date:
        continue
    
    year_match = re.search(r'(19\d{2}|20\d{2}|21\d{2})', grant_date)
    if not year_match:
        continue
    year = int(year_match.group(1))
    
    cpc_field = patent.get('cpc', '[]')
    if cpc_field:
        try:
            cpc_list = json.loads(cpc_field)
            for cpc_item in cpc_list:
                code = cpc_item.get('code', '')
                if code and '/' in code:
                    main_group = code.split('/')[0]
                    if len(main_group) >= 4:
                        level4 = main_group[:4]
                        cpc_year_counts[level4][year] += 1
        except:
            pass

# Calculate EMA for each CPC group (smoothing factor = 0.1)
cpc_ema_best = []
for level4, year_counts in cpc_year_counts.items():
    if len(year_counts) >= 2:
        # Sort years
        sorted_years = sorted(year_counts.keys())
        ema_values = {}
        
        # Initial EMA
        first_year = sorted_years[0]
        ema_prev = year_counts[first_year]
        ema_values[first_year] = ema_prev
        
        # Calculate EMA for each subsequent year
        for year in sorted_years[1:]:
            count = year_counts[year]
            ema_current = 0.1 * count + 0.9 * ema_prev
            ema_values[year] = ema_current
            ema_prev = ema_current
        
        # Find best year (highest EMA)
        best_year = max(ema_values.keys(), key=lambda y: ema_values[y])
        best_ema = ema_values[best_year]
        
        # Only include if best year is 2019 or later
        if best_year >= 2019:
            cpc_ema_best.append({
                'cpc_group': level4,
                'best_year': best_year,
                'best_ema': best_ema,
                'total_years': len(sorted_years)
            })

# Sort by best EMA value
sorted_results = sorted(cpc_ema_best, key=lambda x: x['best_ema'], reverse=True)

result = {
    'top_cpc_groups': sorted_results[:15]
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'applicationReferences': '[]', 'breakdownCode': 'False', 'childGroups': '[]', 'children': '[\n  "B04B",\n  "B04C"\n]', 'dateRevised': '20190501.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'None', 'level': '4.0', 'limitingReferences': '[]', 'notAllocatable': 'True', 'parents': '[\n  "B"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'B04', 'synonyms': '[]', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'titlePart': '[\n  "CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'False', 'childGroups': '[]', 'children': '[\n  "B23B",\n  "B23C",\n  "B23D",\n  "B23F",\n  "B23G",\n  "B23H",\n  "B23K",\n  "B23P",\n  "B23Q"\n]', 'dateRevised': '20190501.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'None', 'level': '4.0', 'limitingReferences': '[]', 'notAllocatable': 'True', 'parents': '[\n  "B"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'B23', 'synonyms': '[]', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'titlePart': '[\n  "MACHINE TOOLS",\n  "METAL-WORKING NOT OTHERWISE PROVIDED FOR"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'False', 'childGroups': '[]', 'children': '[\n  "B30B"\n]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'None', 'level': '4.0', 'limitingReferences': '[]', 'notAllocatable': 'True', 'parents': '[\n  "B"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'B30', 'synonyms': '[]', 'titleFull': 'PRESSES', 'titlePart': '[\n  "PRESSES"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'False', 'childGroups': '[]', 'children': '[\n  "B21B",\n  "B21C",\n  "B21D",\n  "B21F",\n  "B21G",\n  "B21H",\n  "B21J",\n  "B21K",\n  "B21L"\n]', 'dateRevised': '20190501.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'None', 'level': '4.0', 'limitingReferences': '[]', 'notAllocatable': 'True', 'parents': '[\n  "B"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'B21', 'synonyms': '[]', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'titlePart': '[\n  "MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL",\n  "PUNCHING METAL"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'False', 'childGroups': '[]', 'children': '[\n  "B25B",\n  "B25C",\n  "B25D",\n  "B25F",\n  "B25G",\n  "B25H",\n  "B25J"\n]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'None', 'level': '4.0', 'limitingReferences': '[]', 'notAllocatable': 'True', 'parents': '[\n  "B"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'B25', 'synonyms': '[]', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'titlePart': '[\n  "HAND TOOLS",\n  "PORTABLE POWER-DRIVEN TOOLS",\n  "MANIPULATORS"\n]'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:22': [{'grant_year': ' 1st'}, {'grant_year': ' 2nd'}, {'grant_year': ' 3rd'}, {'grant_year': ' 4th'}, {'grant_year': ' 5th'}, {'grant_year': ' 6th'}, {'grant_year': ' 7th'}, {'grant_year': ' 8th'}, {'grant_year': ' 9th'}, {'grant_year': '10th'}, {'grant_year': '11th'}, {'grant_year': '12th'}, {'grant_year': '13th'}, {'grant_year': '14th'}, {'grant_year': '15th'}, {'grant_year': '16th'}, {'grant_year': '17th'}, {'grant_year': '1837'}, {'grant_year': '1839'}, {'grant_year': '1841'}, {'grant_year': '1842'}, {'grant_year': '1843'}, {'grant_year': '1844'}, {'grant_year': '1845'}, {'grant_year': '1846'}, {'grant_year': '1847'}, {'grant_year': '1848'}, {'grant_year': '1849'}, {'grant_year': '1850'}, {'grant_year': '1851'}, {'grant_year': '1853'}, {'grant_year': '1854'}, {'grant_year': '1855'}, {'grant_year': '1856'}, {'grant_year': '1857'}, {'grant_year': '1858'}, {'grant_year': '1859'}, {'grant_year': '1860'}, {'grant_year': '1861'}, {'grant_year': '1862'}, {'grant_year': '1863'}, {'grant_year': '1864'}, {'grant_year': '1865'}, {'grant_year': '1866'}, {'grant_year': '1867'}, {'grant_year': '1868'}, {'grant_year': '1869'}, {'grant_year': '1870'}, {'grant_year': '1871'}, {'grant_year': '1872'}, {'grant_year': '1873'}, {'grant_year': '1874'}, {'grant_year': '1875'}, {'grant_year': '1876'}, {'grant_year': '1877'}, {'grant_year': '1878'}, {'grant_year': '1879'}, {'grant_year': '1880'}, {'grant_year': '1881'}, {'grant_year': '1882'}, {'grant_year': '1883'}, {'grant_year': '1884'}, {'grant_year': '1885'}, {'grant_year': '1886'}, {'grant_year': '1887'}, {'grant_year': '1888'}, {'grant_year': '1889'}, {'grant_year': '1890'}, {'grant_year': '1891'}, {'grant_year': '1892'}, {'grant_year': '1893'}, {'grant_year': '1894'}, {'grant_year': '1895'}, {'grant_year': '1896'}, {'grant_year': '1897'}, {'grant_year': '1898'}, {'grant_year': '1899'}, {'grant_year': '18th'}, {'grant_year': '1900'}, {'grant_year': '1901'}, {'grant_year': '1902'}, {'grant_year': '1903'}, {'grant_year': '1904'}, {'grant_year': '1905'}, {'grant_year': '1906'}, {'grant_year': '1907'}, {'grant_year': '1908'}, {'grant_year': '1909'}, {'grant_year': '1910'}, {'grant_year': '1911'}, {'grant_year': '1912'}, {'grant_year': '1913'}, {'grant_year': '1914'}, {'grant_year': '1915'}, {'grant_year': '1916'}, {'grant_year': '1917'}, {'grant_year': '1918'}, {'grant_year': '1919'}, {'grant_year': '1920'}, {'grant_year': '1921'}, {'grant_year': '1922'}, {'grant_year': '1923'}, {'grant_year': '1924'}, {'grant_year': '1925'}, {'grant_year': '1926'}, {'grant_year': '1927'}, {'grant_year': '1928'}, {'grant_year': '1929'}, {'grant_year': '1930'}, {'grant_year': '1931'}, {'grant_year': '1932'}, {'grant_year': '1933'}, {'grant_year': '1934'}, {'grant_year': '1935'}, {'grant_year': '1936'}, {'grant_year': '1937'}, {'grant_year': '1938'}, {'grant_year': '1939'}, {'grant_year': '1940'}, {'grant_year': '1941'}, {'grant_year': '1942'}, {'grant_year': '1943'}, {'grant_year': '1944'}, {'grant_year': '1945'}, {'grant_year': '1946'}, {'grant_year': '1947'}, {'grant_year': '1948'}, {'grant_year': '1949'}, {'grant_year': '1950'}, {'grant_year': '1951'}, {'grant_year': '1952'}, {'grant_year': '1953'}, {'grant_year': '1954'}, {'grant_year': '1955'}, {'grant_year': '1956'}, {'grant_year': '1957'}, {'grant_year': '1958'}, {'grant_year': '1959'}, {'grant_year': '1960'}, {'grant_year': '1961'}, {'grant_year': '1962'}, {'grant_year': '1963'}, {'grant_year': '1964'}, {'grant_year': '1965'}, {'grant_year': '1966'}, {'grant_year': '1967'}, {'grant_year': '1968'}, {'grant_year': '1969'}, {'grant_year': '1970'}, {'grant_year': '1971'}, {'grant_year': '1972'}, {'grant_year': '1973'}, {'grant_year': '1974'}, {'grant_year': '1975'}, {'grant_year': '1976'}, {'grant_year': '1977'}, {'grant_year': '1978'}, {'grant_year': '1979'}, {'grant_year': '1980'}, {'grant_year': '1981'}, {'grant_year': '1982'}, {'grant_year': '1983'}, {'grant_year': '1984'}, {'grant_year': '1985'}, {'grant_year': '1986'}, {'grant_year': '1987'}, {'grant_year': '1988'}, {'grant_year': '1989'}, {'grant_year': '1990'}, {'grant_year': '1991'}, {'grant_year': '1992'}, {'grant_year': '1993'}, {'grant_year': '1994'}, {'grant_year': '1995'}, {'grant_year': '1996'}, {'grant_year': '1997'}, {'grant_year': '1998'}, {'grant_year': '1999'}, {'grant_year': '19th'}, {'grant_year': '2000'}, {'grant_year': '2001'}, {'grant_year': '2002'}, {'grant_year': '2003'}, {'grant_year': '2004'}, {'grant_year': '2005'}, {'grant_year': '2006'}, {'grant_year': '2007'}, {'grant_year': '2008'}, {'grant_year': '2009'}, {'grant_year': '2010'}, {'grant_year': '2011'}, {'grant_year': '2012'}, {'grant_year': '2013'}, {'grant_year': '2014'}, {'grant_year': '2015'}, {'grant_year': '2016'}, {'grant_year': '2017'}, {'grant_year': '2018'}, {'grant_year': '2019'}, {'grant_year': '2020'}, {'grant_year': '2021'}, {'grant_year': '2022'}, {'grant_year': '2023'}, {'grant_year': '2024'}, {'grant_year': '20th'}, {'grant_year': '21st'}, {'grant_year': '22nd'}, {'grant_year': '23rd'}, {'grant_year': '24th'}, {'grant_year': '25th'}, {'grant_year': '26th'}, {'grant_year': '27th'}, {'grant_year': '28th'}, {'grant_year': '29th'}, {'grant_year': '30th'}, {'grant_year': '31st'}, {'grant_year': 'Date'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:42': {'count': 25}, 'var_functions.execute_python:46': {'status': 'loaded', 'count': 25}, 'var_functions.execute_python:48': {'cpc_groups': [['C04B2235', 32], ['H04W52', 12], ['C04B35', 12], ['H04L1', 10], ['H01J49', 10], ['H04W72', 9], ['B29C2049', 9], ['F02M59', 8], ['F17C2205', 8], ['F17C2250', 8]], 'total_cpc_groups': 93}, 'var_functions.query_db:52': [], 'var_functions.execute_python:54': {'level4_groups': [['C04B', 45], ['F17C', 30], ['H04W', 22], ['B29C', 19], ['H04L', 14], ['G02B', 12], ['F02M', 11], ['H01J', 10], ['F02D', 8], ['F02N', 7], ['E02F', 6], ['A61F', 6], ['F23L', 6], ['H01R', 6], ['H02J', 6]], 'main_groups': [['C04B2235', 32], ['H04W52', 12], ['C04B35', 12], ['H04L1', 10], ['H01J49', 10], ['H04W72', 9], ['B29C2049', 9], ['F02M59', 8], ['F17C2205', 8], ['F17C2250', 8], ['F02D41', 6], ['A61F5', 6], ['F17C2201', 6], ['B29C49', 5], ['G02B15', 5]], 'total_level4': 52, 'total_main': 93}, 'var_functions.query_db:56': 'file_storage/functions.query_db:56.json', 'var_functions.query_db:58': [], 'var_functions.execute_python:60': {'total_patents': 25, 'cpc_level4_codes': ['F16H', 'H01H', 'F41H', 'F23L', 'B60R', 'F42B', 'G01D', 'F16K', 'F02D', 'H04L', 'H01R', 'H01F', 'H02J', 'G01N', 'F17C', 'H04W', 'E05B', 'B29C', 'G07C', 'A43B', 'B60K', 'F02M', 'Y02D', 'G02B', 'F23N', 'B29D', 'C04B', 'F24B', 'H01J', 'B64D', 'A61B', 'B60W', 'Y10T', 'F02N', 'B66C', 'Y02E', 'A61L', 'G01F', 'G05D', 'F02P', 'A21C', 'B23K', 'B63B', 'A61F', 'B60S', 'F04B', 'Y02T', 'C09K', 'E02F', 'A47J', 'B41F', 'F23B']}, 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json', 'var_functions.execute_python:66': {'total_german_patents': 11765, 'cpc_groups_2019_h2': 82, 'relevant_cpcs_count': 82}}

exec(code, env_args)
