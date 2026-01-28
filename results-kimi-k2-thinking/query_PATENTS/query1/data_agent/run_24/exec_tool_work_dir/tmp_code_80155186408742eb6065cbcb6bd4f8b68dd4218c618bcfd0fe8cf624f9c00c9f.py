code = """import json

# Read the full result from the stored file
result_file_path = locals()['var_functions.execute_python:24']

with open(result_file_path, 'r') as f:
    result_data = json.load(f)

# Extract the list of CPC codes
cpc_codes = result_data['all_codes']

print(f"Number of CPC codes to return: {len(cpc_codes)}")
print(f"First 10 codes: {cpc_codes[:10]}")

# Return just the list of codes
print('__RESULT__:')
print(json.dumps(cpc_codes))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:8': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_publications': 277813, 'invalid_dates': 139721, 'valid_entries': 1333969, 'unique_cpc_codes': 143452, 'years': [1837, 1839, 1841, 1842, 1844, 1846, 1847, 1848, 1849, 1850, 1851, 1852, 1853, 1856, 1857, 1858, 1859, 1860, 1861, 1862, 1863, 1864, 1865, 1866, 1867, 1868, 1869, 1870, 1871, 1872, 1873, 1874, 1875, 1876, 1877, 1878, 1879, 1880, 1881, 1882, 1883, 1884, 1885, 1886, 1887, 1888, 1889, 1890, 1891, 1892, 1893, 1894, 1895, 1896, 1897, 1898, 1899, 1900, 1901, 1902, 1903, 1904, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1916, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1926, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939, 1940, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024], 'min_year': 1837, 'max_year': 2024}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'total_cpc_codes': 143452, 'codes_best_2022': 12035, 'sample_codes': ['G11B3/5845', 'H03M1/0854', 'A61K2800/546', 'H01L24/29', 'B65B19/223', 'D07B1/062', 'B29D29/00', 'C04B14/10', 'A47C7/16', 'B62D55/062', 'B05D7/544', 'A61C11/00', 'Y10T137/402', 'H10B12/37', 'H02G7/18', 'G06F2209/5022', 'C22C1/1068', 'B60L15/42', 'B32B5/10', 'G11C7/1069'], 'format_distribution': {'subgroup': 100}, 'sample_level5_matches': [], 'level5_symbols_count': 677, 'years_count': 182, 'min_year': 1837, 'max_year': 2024}, 'var_functions.execute_python:22': 'file_storage/functions.execute_python:22.json', 'var_functions.execute_python:24': 'file_storage/functions.execute_python:24.json'}

exec(code, env_args)
