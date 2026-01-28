code = """import json, re
from collections import defaultdict, Counter

# Load CPC level 5 codes
cpc5_file = locals()['var_functions.query_db:20']
with open(cpc5_file, 'r') as f:
    cpc5_data = json.load(f)

cpc_level5_set = set(entry['symbol'] for entry in cpc5_data)

# Parse patents - create yearly counts for level 5 CPC codes
patents_by_year = defaultdict(Counter)
years = set()

with open(locals()['var_functions.query_db:24'], 'r') as f:
    publications = json.load(f)
    for record in publications:
        # Extract year
        pub_date = record['publication_date']
        year_match = re.search(r'\d{4}', pub_date)
        if not year_match:
            continue
        year = int(year_match.group())
        years.add(year)
        
        # Parse CPC codes
        try:
            cpc_list = json.loads(record['cpc'])
            for cpc_entry in cpc_list:
                cpc_code = cpc_entry['code']
                # Keep full CPC code (level 5)
                patents_by_year[year][cpc_code] += 1
        except:
            continue

# Sort years chronologically
sorted_years = sorted(years)

# Calculate exponential moving average for each CPC code at level 5
smoothing_factor = 0.2
cpc_ema_by_year = defaultdict(list)  # {cpc: [(year, ema)]}

# First, identify all level 5 CPC codes that appear in the data
all_cpc_codes = set()
for year_counts in patents_by_year.values():
    all_cpc_codes.update(year_counts.keys())

# Filter to only level 5 CPC codes (those in cpc_level5_set)
level5_cpc_codes = [code for code in all_cpc_codes if code in cpc_level5_set]

# Calculate EMA for each level 5 CPC code
for cpc_code in level5_cpc_codes:
    prev_ema = None
    for year in sorted_years:
        count = patents_by_year[year].get(cpc_code, 0)
        if prev_ema is None:
            ema = count
        else:
            ema = (count * smoothing_factor) + (prev_ema * (1 - smoothing_factor))
        cpc_ema_by_year[cpc_code].append((year, ema))
        prev_ema = ema

# Find the year with highest EMA for each CPC code at level 5
cpc_best_year = {}
for cpc_code, ema_series in cpc_ema_by_year.items():
    if ema_series:
        best_year, best_ema = max(ema_series, key=lambda x: x[1])
        cpc_best_year[cpc_code] = {
            'best_year': best_year,
            'best_ema': best_ema,
            'ema_series': ema_series
        }

# Filter for CPC codes whose best year is 2022
cpc_best_2022 = [cpc_code for cpc_code, data in cpc_best_year.items() if data['best_year'] == 2022]

# Count these CPC codes
count_2022 = len(cpc_best_2022)

print('__RESULT__:')
print(json.dumps({
    'total_cpc_level5_codes': len(cpc_level5_set),
    'level5_cpc_in_data': len(level5_cpc_codes),
    'cpc_codes_best_year_2022_count': count_2022,
    'cpc_codes_best_year_2022_sample': cpc_best_2022[:20] if count_2022 > 0 else []
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:14': {'total_records': 277813, 'years_available': ['1837', '1839', '1841', '1842', '1843', '1844', '1845', '1846', '1847', '1848', '1849', '1850', '1851', '1852', '1853', '1854', '1855', '1856', '1857', '1858', '1859', '1860', '1861', '1862', '1863', '1864', '1865', '1866', '1867', '1868', '1869', '1870', '1871', '1872', '1873', '1874', '1875', '1876', '1877', '1878', '1879', '1880', '1881', '1882', '1883', '1884', '1885', '1886', '1887', '1888', '1889', '1890', '1891', '1892', '1893', '1894', '1895', '1896', '1897', '1898', '1899', '1900', '1901', '1902', '1903', '1904', '1905', '1906', '1907', '1908', '1909', '1910', '1911', '1912', '1913', '1914', '1915', '1916', '1917', '1918', '1919', '1920', '1921', '1922', '1923', '1924', '1925', '1926', '1927', '1928', '1929', '1930', '1931', '1932', '1933', '1934', '1935', '1936', '1937', '1938', '1939', '1940', '1941', '1942', '1943', '1944', '1945', '1946', '1947', '1948', '1949', '1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'], 'total_cpc_codes': 175852}, 'var_functions.list_db:16': ['cpc_definition'], 'var_functions.query_db:18': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}, {'symbol': 'A01N', 'level': '5.0', 'titleFull': 'PRESERVATION OF BODIES OF HUMANS OR ANIMALS OR PLANTS OR PARTS THEREOF; BIOCIDES, e.g. AS DISINFECTANTS, AS PESTICIDES OR AS HERBICIDES; PEST REPELLANTS OR ATTRACTANTS; PLANT GROWTH REGULATORS'}, {'symbol': 'A01P', 'level': '5.0', 'titleFull': 'BIOCIDAL, PEST REPELLANT, PEST ATTRACTANT OR PLANT GROWTH REGULATORY ACTIVITY OF CHEMICAL COMPOUNDS OR PREPARATIONS'}, {'symbol': 'A01D', 'level': '5.0', 'titleFull': 'HARVESTING; MOWING'}, {'symbol': 'A01L', 'level': '5.0', 'titleFull': 'SHOEING OF ANIMALS'}, {'symbol': 'A01K', 'level': '5.0', 'titleFull': 'ANIMAL HUSBANDRY; AVICULTURE; APICULTURE; PISCICULTURE; FISHING; REARING OR BREEDING ANIMALS, NOT OTHERWISE PROVIDED FOR; NEW BREEDS OF ANIMALS'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
