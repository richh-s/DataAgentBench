code = """import json
import glob
import re
from collections import defaultdict

# Find the query result file
json_files = glob.glob('*.json')
query_files = [f for f in json_files if 'query_db' in f]

if not query_files:
    print('ERROR: No data file found')
    result = []
else:
    # Use the most recent query file
    query_file = sorted(query_files)[-1]
    print('Processing file:', query_file)
    
    with open(query_file, 'r') as f:
        data = json.load(f)
    
    print(f'Loaded {len(data)} records')
    
    # Initialize data structures
    cpc_filing_counts = defaultdict(lambda: defaultdict(int))
    cpc_level5_groups = set()
    
    year_pattern = re.compile(r'(\d{4})\s*$')
    
    # Process each record
    valid_records = 0
    for record in data:
        date_str = record.get('publication_date', '')
        year_match = year_pattern.search(date_str)
        
        if not year_match:
            continue
            
        year = int(year_match.group(1))
        if year < 2000 or year > 2030:
            continue
        
        valid_records += 1
        
        # Parse CPC codes
        cpc_str = record.get('cpc', '')
        if not cpc_str:
            continue
        
        try:
            cpc_list = json.loads(cpc_str)
            for item in cpc_list:
                code = item.get('code', '')
                if not code:
                    continue
                
                # Extract level 5 group code
                if '/' in code:
                    group_code = code.split('/')[0]
                else:
                    group_code = code
                
                if len(group_code) >= 4:
                    cpc_level5_groups.add(group_code)
                    cpc_filing_counts[group_code][year] += 1
        except:
            continue
    
    print(f'Processed {valid_records} valid records')
    print(f'Found {len(cpc_level5_groups)} CPC level 5 groups')
    
    # Calculate EMA (alpha=0.2) and find best year for each group
    alpha = 0.2
    groups_with_2022_peak = []
    
    for group_code in cpc_level5_groups:
        year_counts = sorted(cpc_filing_counts[group_code].items())
        if not year_counts:
            continue
        
        ema = year_counts[0][1]
        best_year = year_counts[0][0]
        max_ema = ema
        
        for year, count in year_counts[1:]:
            ema = alpha * count + (1 - alpha) * ema
            if ema > max_ema:
                max_ema = ema
                best_year = year
        
        if best_year == 2022:
            groups_with_2022_peak.append((group_code, max_ema))
    
    # Sort by EMA descending
    groups_with_2022_peak.sort(key=lambda x: x[1], reverse=True)
    
    # Extract CPC codes
    result = [code for code, ema in groups_with_2022_peak]
    
    print(f'CPC groups with peak EMA in 2022: {len(result)}')
    
    if len(groups_with_2022_peak) > 0:
        print('Top results:')
        for i, (code, ema) in enumerate(groups_with_2022_peak[:10]):
            print(f'  {i+1}. {code} (EMA: {ema:.2f})')

# Print result in required format
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}, {'symbol': 'A01N', 'level': '5.0', 'titleFull': 'PRESERVATION OF BODIES OF HUMANS OR ANIMALS OR PLANTS OR PARTS THEREOF; BIOCIDES, e.g. AS DISINFECTANTS, AS PESTICIDES OR AS HERBICIDES; PEST REPELLANTS OR ATTRACTANTS; PLANT GROWTH REGULATORS'}, {'symbol': 'A01P', 'level': '5.0', 'titleFull': 'BIOCIDAL, PEST REPELLANT, PEST ATTRACTANT OR PLANT GROWTH REGULATORY ACTIVITY OF CHEMICAL COMPOUNDS OR PREPARATIONS'}, {'symbol': 'A01D', 'level': '5.0', 'titleFull': 'HARVESTING; MOWING'}, {'symbol': 'A01L', 'level': '5.0', 'titleFull': 'SHOEING OF ANIMALS'}, {'symbol': 'A01K', 'level': '5.0', 'titleFull': 'ANIMAL HUSBANDRY; AVICULTURE; APICULTURE; PISCICULTURE; FISHING; REARING OR BREEDING ANIMALS, NOT OTHERWISE PROVIDED FOR; NEW BREEDS OF ANIMALS'}, {'symbol': 'A01M', 'level': '5.0', 'titleFull': 'CATCHING, TRAPPING OR SCARING OF ANIMALS; APPARATUS FOR THE DESTRUCTION OF NOXIOUS ANIMALS OR NOXIOUS PLANTS'}, {'symbol': 'A01J', 'level': '5.0', 'titleFull': 'MANUFACTURE OF DAIRY PRODUCTS'}, {'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'A21D', 'level': '5.0', 'titleFull': 'TREATMENT, e.g. PRESERVATION, OF FLOUR OR DOUGH, e.g. BY ADDITION OF MATERIALS; BAKING; BAKERY PRODUCTS; PRESERVATION THEREOF'}, {'symbol': 'A21C', 'level': '5.0', 'titleFull': 'MACHINES OR EQUIPMENT FOR MAKING OR PROCESSING DOUGHS; HANDLING BAKED ARTICLES MADE FROM DOUGH'}, {'symbol': 'A21B', 'level': '5.0', 'titleFull': "BAKERS' OVENS; MACHINES OR EQUIPMENT FOR BAKING"}, {'symbol': 'A22B', 'level': '5.0', 'titleFull': 'SLAUGHTERING'}, {'symbol': 'A22C', 'level': '5.0', 'titleFull': 'PROCESSING MEAT, POULTRY, OR FISH'}, {'symbol': 'A23P', 'level': '5.0', 'titleFull': 'SHAPING OR WORKING OF FOODSTUFFS, NOT FULLY COVERED BY A SINGLE OTHER SUBCLASS'}, {'symbol': 'A23C', 'level': '5.0', 'titleFull': 'DAIRY PRODUCTS, e.g. MILK, BUTTER OR CHEESE; MILK OR CHEESE SUBSTITUTES; MAKING THEREOF'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:38': 'file_storage/functions.execute_python:38.json', 'var_functions.execute_python:42': 'file_storage/functions.execute_python:42.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:56': 'file_storage/functions.query_db:56.json', 'var_functions.execute_python:60': [], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.execute_python:74': [], 'var_functions.execute_python:76': [], 'var_functions.query_db:78': [{'year': ' 1st'}, {'year': ' 2nd'}, {'year': ' 3rd'}, {'year': ' 4th'}, {'year': ' 5th'}, {'year': ' 6th'}, {'year': ' 7th'}, {'year': ' 8th'}, {'year': ' 9th'}, {'year': '10th'}, {'year': '11th'}, {'year': '12th'}, {'year': '13th'}, {'year': '14th'}, {'year': '15th'}, {'year': '16th'}, {'year': '17th'}, {'year': '1837'}, {'year': '1839'}, {'year': '1841'}, {'year': '1842'}, {'year': '1843'}, {'year': '1844'}, {'year': '1845'}, {'year': '1846'}, {'year': '1847'}, {'year': '1848'}, {'year': '1849'}, {'year': '1850'}, {'year': '1851'}, {'year': '1852'}, {'year': '1853'}, {'year': '1854'}, {'year': '1855'}, {'year': '1856'}, {'year': '1857'}, {'year': '1858'}, {'year': '1859'}, {'year': '1860'}, {'year': '1861'}, {'year': '1862'}, {'year': '1863'}, {'year': '1864'}, {'year': '1865'}, {'year': '1866'}, {'year': '1867'}, {'year': '1868'}, {'year': '1869'}, {'year': '1870'}, {'year': '1871'}, {'year': '1872'}, {'year': '1873'}, {'year': '1874'}, {'year': '1875'}, {'year': '1876'}, {'year': '1877'}, {'year': '1878'}, {'year': '1879'}, {'year': '1880'}, {'year': '1881'}, {'year': '1882'}, {'year': '1883'}, {'year': '1884'}, {'year': '1885'}, {'year': '1886'}, {'year': '1887'}, {'year': '1888'}, {'year': '1889'}, {'year': '1890'}, {'year': '1891'}, {'year': '1892'}, {'year': '1893'}, {'year': '1894'}, {'year': '1895'}, {'year': '1896'}, {'year': '1897'}, {'year': '1898'}, {'year': '1899'}, {'year': '18th'}, {'year': '1900'}, {'year': '1901'}, {'year': '1902'}, {'year': '1903'}, {'year': '1904'}, {'year': '1905'}, {'year': '1906'}, {'year': '1907'}, {'year': '1908'}, {'year': '1909'}, {'year': '1910'}, {'year': '1911'}, {'year': '1912'}, {'year': '1913'}, {'year': '1914'}, {'year': '1915'}, {'year': '1916'}, {'year': '1917'}, {'year': '1918'}, {'year': '1919'}, {'year': '1920'}, {'year': '1921'}, {'year': '1922'}, {'year': '1923'}, {'year': '1924'}, {'year': '1925'}, {'year': '1926'}, {'year': '1927'}, {'year': '1928'}, {'year': '1929'}, {'year': '1930'}, {'year': '1931'}, {'year': '1932'}, {'year': '1933'}, {'year': '1934'}, {'year': '1935'}, {'year': '1936'}, {'year': '1937'}, {'year': '1938'}, {'year': '1939'}, {'year': '1940'}, {'year': '1941'}, {'year': '1942'}, {'year': '1943'}, {'year': '1944'}, {'year': '1945'}, {'year': '1946'}, {'year': '1947'}, {'year': '1948'}, {'year': '1949'}, {'year': '1950'}, {'year': '1951'}, {'year': '1952'}, {'year': '1953'}, {'year': '1954'}, {'year': '1955'}, {'year': '1956'}, {'year': '1957'}, {'year': '1958'}, {'year': '1959'}, {'year': '1960'}, {'year': '1961'}, {'year': '1962'}, {'year': '1963'}, {'year': '1964'}, {'year': '1965'}, {'year': '1966'}, {'year': '1967'}, {'year': '1968'}, {'year': '1969'}, {'year': '1970'}, {'year': '1971'}, {'year': '1972'}, {'year': '1973'}, {'year': '1974'}, {'year': '1975'}, {'year': '1976'}, {'year': '1977'}, {'year': '1978'}, {'year': '1979'}, {'year': '1980'}, {'year': '1981'}, {'year': '1982'}, {'year': '1983'}, {'year': '1984'}, {'year': '1985'}, {'year': '1986'}, {'year': '1987'}, {'year': '1988'}, {'year': '1989'}, {'year': '1990'}, {'year': '1991'}, {'year': '1992'}, {'year': '1993'}, {'year': '1994'}, {'year': '1995'}, {'year': '1996'}, {'year': '1997'}, {'year': '1998'}, {'year': '1999'}, {'year': '19th'}, {'year': '2000'}, {'year': '2001'}, {'year': '2002'}, {'year': '2003'}, {'year': '2004'}, {'year': '2005'}, {'year': '2006'}, {'year': '2007'}, {'year': '2008'}, {'year': '2009'}, {'year': '2010'}, {'year': '2011'}, {'year': '2012'}, {'year': '2013'}, {'year': '2014'}, {'year': '2015'}, {'year': '2016'}, {'year': '2017'}, {'year': '2018'}, {'year': '2019'}, {'year': '2020'}, {'year': '2021'}, {'year': '2022'}, {'year': '2023'}, {'year': '2024'}, {'year': '20th'}, {'year': '21st'}, {'year': '22nd'}, {'year': '23rd'}, {'year': '24th'}, {'year': '25th'}, {'year': '26th'}, {'year': '27th'}, {'year': '28th'}, {'year': '29th'}, {'year': '30th'}, {'year': '31st'}, {'year': 'Date'}], 'var_functions.query_db:80': 'file_storage/functions.query_db:80.json', 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json', 'var_functions.query_db:86': 'file_storage/functions.query_db:86.json', 'var_functions.execute_python:88': [], 'var_functions.execute_python:90': [], 'var_functions.execute_python:92': []}

exec(code, env_args)
