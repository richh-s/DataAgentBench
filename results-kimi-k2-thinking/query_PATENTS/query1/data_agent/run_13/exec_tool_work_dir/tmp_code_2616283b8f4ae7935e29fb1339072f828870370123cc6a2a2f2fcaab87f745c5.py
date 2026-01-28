code = """import json

# Load the data files
with open(locals()['var_functions.query_db:2'], 'r') as f:
    patent_data = json.load(f)

# Load CPC level 5 symbols
with open(locals()['var_functions.query_db:3'], 'r') as f:
    cpc_level5_data = json.load(f)

# Count records by year
import re
year_counts = {}
for record in patent_data:
    pub_date = record.get('publication_date', '')
    if pub_date:
        match = re.search(r'(\d{4})', str(pub_date))
        if match:
            year = int(match.group(1))
            year_counts[year] = year_counts.get(year, 0) + 1

# Sample a few records to see CPC structure
sample_cpc = []
if patent_data and len(patent_data) > 0:
    for i in range(min(3, len(patent_data))):
        cpc_field = patent_data[i].get('cpc', '')
        sample_cpc.append({
            'record': i,
            'cpc_type': str(type(cpc_field)),
            'cpc_preview': str(cpc_field)[:200] if cpc_field else 'empty'
        })

result = {
    'patent_records_total': len(patent_data),
    'records_by_year': year_counts,
    'cpc_level5_count': len(cpc_level5_data),
    'cpc_samples': sample_cpc
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json', 'var_functions.execute_python:18': [], 'var_functions.execute_python:20': {'cpc_symbols_sample': ['A01H', 'A01F', 'A01C', 'A01G', 'A23J', 'A01N', 'A01P', 'A01D', 'A01L', 'A01K', 'A01M', 'A01J', 'A01B', 'A21D', 'A21C', 'A21B', 'A22B', 'A22C', 'A23P', 'A23C'], 'patent_cpc_samples': [], 'available_years': [1837, 1839, 1841, 1842, 1843, 1844, 1845, 1846, 1847, 1848, 1849, 1850, 1851, 1852, 1853, 1854, 1855, 1856, 1857, 1858, 1859, 1860, 1861, 1862, 1863, 1864, 1865, 1866, 1867, 1868, 1869, 1870, 1871, 1872, 1873, 1874, 1875, 1876, 1877, 1878, 1879, 1880, 1881, 1882, 1883, 1884, 1885, 1886, 1887, 1888, 1889, 1890, 1891, 1892, 1893, 1894, 1895, 1896, 1897, 1898, 1899, 1900, 1901, 1902, 1903, 1904, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1916, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1926, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939, 1940, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]}, 'var_functions.query_db:22': [{'symbol': 'A01H'}, {'symbol': 'A01F'}, {'symbol': 'A01C'}, {'symbol': 'A01G'}, {'symbol': 'A23J'}, {'symbol': 'A01N'}, {'symbol': 'A01P'}, {'symbol': 'A01D'}, {'symbol': 'A01L'}, {'symbol': 'A01K'}], 'var_functions.list_db:24': ['cpc_definition']}

exec(code, env_args)
