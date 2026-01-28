code = """import json, re
from collections import defaultdict, Counter

# Load data
pub_file = locals()['var_functions.query_db:24']
cpc5_file = locals()['var_functions.query_db:20']

# Load CPC level 5 codes
with open(cpc5_file, 'r') as f:
    cpc5_data = json.load(f)

cpc5_set = set(entry['symbol'] for entry in cpc5_data)

# Create mapping from full CPC to level 5
# CPC format: Section (1 char) + Class (2 digits) + Subclass (1 letter) + Group (1-3 digits) + / + Subgroup (1-6 digits)
# Level 5 is the full code, but for grouping we need to extract the appropriate level
def get_cpc_level_5(cpc_full_code):
    """Extract level 5 CPC code (format: A01B02/34)"""
    # Remove any spaces
    code = cpc_full_code.strip()
    
    # Find the slash position
    slash_pos = code.find('/')
    if slash_pos == -1:
        return code  # No slash, return as is
    
    # Get the part before and after slash
    before_slash = code[:slash_pos]
    after_slash = code[slash_pos+1:]
    
    # Level 1: Section (1 char)
    # Level 2: Section + Class (1+2 = 3 chars)
    # Level 3: Section + Class + Subclass (1+2+1 = 4 chars)
    # Level 4: Section + Class + Subclass + Group (1+2+1+1-3 = 4-7 chars)
    # Level 5: Full code with subgroup (full code)
    
    # So level 5 is the complete code
    return code

# Parse patents and count by year and CPC
patents_by_year_cpc = defaultdict(Counter)
years = set()
cpc5_frequencies = defaultdict(Counter)

count_total = 0
count_cpc5 = 0

with open(pub_file, 'r') as f:
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
                full_code = cpc_entry['code']
                level5_code = get_cpc_level_5(full_code)
                
                # Count the patent for this CPC code
                patents_by_year_cpc[year][level5_code] += 1
                
                # Track if this is a level 5 CPC
                if level5_code in cpc5_set:
                    cpc5_frequencies[year][level5_code] += 1
                    count_cpc5 += 1
                    
                count_total += 1
        except:
            continue

# Sort years
sorted_years = sorted(years)

print(f"__RESULT__: Processed {count_total} CPC entries, {count_cpc5} are level 5")
print(json.dumps({
    "years_range": [min(sorted_years), max(sorted_years)],
    "total_patents_with_cpc": sum(sum(year_counts.values()) for year_counts in patents_by_year_cpc.values()),
    "level5_cpc_codes_count": len(cpc5_set),
    "level5_cpc_patents_count": sum(sum(year_counts.values()) for year_counts in cpc5_frequencies.values())
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:14': {'total_records': 277813, 'years_available': ['1837', '1839', '1841', '1842', '1843', '1844', '1845', '1846', '1847', '1848', '1849', '1850', '1851', '1852', '1853', '1854', '1855', '1856', '1857', '1858', '1859', '1860', '1861', '1862', '1863', '1864', '1865', '1866', '1867', '1868', '1869', '1870', '1871', '1872', '1873', '1874', '1875', '1876', '1877', '1878', '1879', '1880', '1881', '1882', '1883', '1884', '1885', '1886', '1887', '1888', '1889', '1890', '1891', '1892', '1893', '1894', '1895', '1896', '1897', '1898', '1899', '1900', '1901', '1902', '1903', '1904', '1905', '1906', '1907', '1908', '1909', '1910', '1911', '1912', '1913', '1914', '1915', '1916', '1917', '1918', '1919', '1920', '1921', '1922', '1923', '1924', '1925', '1926', '1927', '1928', '1929', '1930', '1931', '1932', '1933', '1934', '1935', '1936', '1937', '1938', '1939', '1940', '1941', '1942', '1943', '1944', '1945', '1946', '1947', '1948', '1949', '1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'], 'total_cpc_codes': 175852}, 'var_functions.list_db:16': ['cpc_definition'], 'var_functions.query_db:18': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}, {'symbol': 'A01N', 'level': '5.0', 'titleFull': 'PRESERVATION OF BODIES OF HUMANS OR ANIMALS OR PLANTS OR PARTS THEREOF; BIOCIDES, e.g. AS DISINFECTANTS, AS PESTICIDES OR AS HERBICIDES; PEST REPELLANTS OR ATTRACTANTS; PLANT GROWTH REGULATORS'}, {'symbol': 'A01P', 'level': '5.0', 'titleFull': 'BIOCIDAL, PEST REPELLANT, PEST ATTRACTANT OR PLANT GROWTH REGULATORY ACTIVITY OF CHEMICAL COMPOUNDS OR PREPARATIONS'}, {'symbol': 'A01D', 'level': '5.0', 'titleFull': 'HARVESTING; MOWING'}, {'symbol': 'A01L', 'level': '5.0', 'titleFull': 'SHOEING OF ANIMALS'}, {'symbol': 'A01K', 'level': '5.0', 'titleFull': 'ANIMAL HUSBANDRY; AVICULTURE; APICULTURE; PISCICULTURE; FISHING; REARING OR BREEDING ANIMALS, NOT OTHERWISE PROVIDED FOR; NEW BREEDS OF ANIMALS'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
