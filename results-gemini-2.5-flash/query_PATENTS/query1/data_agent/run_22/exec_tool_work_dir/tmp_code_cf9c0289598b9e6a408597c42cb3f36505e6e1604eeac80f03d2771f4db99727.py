code = """import pandas as pd
import json
import re

# Load patent publication data
with open(locals()['var_function-call-2018874257286241520'], 'r') as f:
    publication_data = json.load(f)

publications_df = pd.DataFrame(publication_data)

# Extract year from 'filing_date'
def extract_year(date_string):
    if isinstance(date_string, str):
        match = re.search(r'\b(\d{4})\b', date_string)
        if match:
            return int(match.group(1))
    return None

publications_df['filing_year'] = publications_df['filing_date'].apply(extract_year)

# Debug 1: Check columns after filing_year creation
# print('__RESULT__:')
# print(json.dumps({'step': 'after_filing_year_creation', 'columns': publications_df.columns.tolist()}))

# Filter out rows with invalid filing years and convert to int
publications_df = publications_df.dropna(subset=['filing_year'])
publications_df['filing_year'] = publications_df['filing_year'].astype(int)

# Debug 2: Check columns after dropna and astype(int)
# print('__RESULT__:')
# print(json.dumps({'step': 'after_dropna_astype', 'columns': publications_df.columns.tolist()}))

# Process CPC codes and explode into separate rows
all_cpc_filings = []
for _, row in publications_df.iterrows():
    try:
        if isinstance(row['cpc'], str):
            cpc_list = json.loads(row['cpc'])
            for cpc_item in cpc_list:
                all_cpc_filings.append({'cpc_code': cpc_item['code'], 'filing_year': row['filing_year']})
    except (json.JSONDecodeError, TypeError):
        continue

cpc_filings_df = pd.DataFrame(all_cpc_filings)

# Debug 3: Check columns after cpc_filings_df creation
# print('__RESULT__:')
# print(json.dumps({'step': 'after_cpc_filings_df_creation', 'columns': cpc_filings_df.columns.tolist()}))

# Filter for years up to 2022 (inclusive)
cpc_filings_df = cpc_filings_df[cpc_filings_df['filing_year'] <= 2022]

# Group by cpc_code and filing_year to count patents
patent_counts = cpc_filings_df.groupby(['cpc_code', 'filing_year']).size().reset_index(name='patent_count')

# Debug 4: Check columns after patent_counts creation
# print('__RESULT__:')
# print(json.dumps({'step': 'after_patent_counts_creation', 'columns': patent_counts.columns.tolist()}))

# Calculate Exponential Moving Average (EMA)
smoothing_factor = 0.2
ema_results = []

for cpc_code in patent_counts['cpc_code'].unique():
    cpc_data = patent_counts[patent_counts['cpc_code'] == cpc_code].sort_values(by='filing_year')
    
    if not cpc_data.empty:
        ema = cpc_data.iloc[0]['patent_count']
        ema_results.append({'cpc_code': cpc_code, 'filing_year': cpc_data.iloc[0]['filing_year'], 'ema': ema})

        for i in range(1, len(cpc_data)):
            current_patent_count = cpc_data.iloc[i]['patent_count']
            ema = (current_patent_count * smoothing_factor) + (ema * (1 - smoothing_factor))
            ema_results.append({'cpc_code': cpc_code, 'filing_year': cpc_data.iloc[i]['filing_year'], 'ema': ema})

ema_df = pd.DataFrame(ema_results)

# Find the best year for each CPC code (highest EMA)
best_year_cpc = ema_df.loc[ema_df.groupby('cpc_code')['ema'].idxmax()]

# Filter for best year being 2022
cpc_best_year_2022 = best_year_cpc[best_year_cpc['filing_year'] == 2022]['cpc_code'].unique().tolist()

# Load level 5 CPC codes from CPCDefinition_database
with open(locals()['var_function-call-5891838390981204155'], 'r') as f:
    level_5_cpc_data = json.load(f)

level_5_cpc_symbols = {item['symbol'] for item in level_5_cpc_data}

# Filter for CPC codes that are also at level 5
final_cpc_codes = [code for code in cpc_best_year_2022 if code in level_5_cpc_symbols]

print('__RESULT__:')
print(json.dumps(final_cpc_codes))"""

env_args = {'var_function-call-2018874257286241520': 'file_storage/function-call-2018874257286241520.json', 'var_function-call-10242324406622312450': ['cpc_definition'], 'var_function-call-13458682655913919725': 'file_storage/function-call-13458682655913919725.json', 'var_function-call-5891838390981204155': 'file_storage/function-call-5891838390981204155.json', 'var_function-call-5313532908811152240': {'filing_date_head': ['dated 5th March 2019', 'March the 18th, 2019', '29th March 2019', 'on March 29th, 2019', '2nd April 2019'], 'filing_year_head': [2019.0, 2019.0, 2019.0, 2019.0, 2019.0], 'publications_df_shape_before_dropna': [277813, 3], 'filing_year_value_counts_before_dropna': {'2018.0': 17108, '2017.0': 16009, '2016.0': 14776, '2021.0': 13246, '2022.0': 11966, '2020.0': 11377, '2019.0': 11208, '2015.0': 9324, '2014.0': 8056, '2013.0': 6936, '2023.0': 6272, '2008.0': 6206, '2012.0': 6169, '2006.0': 6087, '2007.0': 6051, '2011.0': 5975, '2009.0': 5973, '2010.0': 5912, '2005.0': 5817, '2004.0': 5361, '2003.0': 5160, 'NaN': 4449, '2002.0': 4376, '2001.0': 4284, '2000.0': 3784, '1999.0': 3439, '1997.0': 3073, '1998.0': 2993, '1996.0': 2817, '1995.0': 2449, '1994.0': 2265, '1993.0': 2054, '1990.0': 2018, '1992.0': 1995, '1988.0': 1961, '1983.0': 1907, '1989.0': 1889, '1991.0': 1877, '1984.0': 1874, '1981.0': 1854, '1986.0': 1767, '1987.0': 1756, '1982.0': 1752, '1985.0': 1694, '1980.0': 1566, '1975.0': 1501, '1979.0': 1449, '1974.0': 1430, '1978.0': 1416, '1973.0': 1382, '1977.0': 1379, '1976.0': 1368, '1972.0': 1187, '1971.0': 1044, '1969.0': 1012, '1970.0': 967, '1968.0': 811, '1967.0': 753, '1966.0': 751, '1965.0': 721, '1964.0': 648, '2024.0': 641, '1962.0': 501, '1963.0': 494, '1961.0': 459, '1959.0': 450, '1956.0': 448, '1960.0': 438, '1958.0': 423, '1955.0': 421, '1957.0': 417, '1954.0': 407, '1938.0': 328, '1952.0': 327, '1950.0': 307, '1953.0': 307, '1951.0': 297, '1947.0': 296, '1936.0': 294, '1939.0': 293, '1949.0': 293, '1946.0': 283, '1941.0': 273, '1935.0': 272, '1940.0': 271, '1937.0': 266, '1948.0': 262, '1943.0': 258, '1934.0': 254, '1945.0': 243, '1944.0': 237, '1931.0': 209, '1930.0': 208, '1929.0': 201, '1942.0': 199, '1913.0': 194, '1912.0': 194, '1928.0': 193, '1921.0': 187, '1933.0': 185, '1932.0': 182, '1926.0': 181, '1925.0': 169, '1927.0': 164, '1911.0': 149, '1924.0': 149, '1923.0': 145, '1920.0': 144, '1922.0': 141, '1914.0': 130, '1915.0': 118, '1919.0': 116, '1916.0': 110, '1906.0': 103, '1907.0': 102, '1917.0': 87, '1908.0': 82, '1909.0': 78, '1910.0': 75, '1905.0': 68, '1904.0': 64, '1918.0': 63, '1899.0': 56, '1903.0': 51, '1902.0': 45, '1900.0': 34, '1901.0': 26, '1898.0': 12, '1897.0': 7, '1894.0': 6, '1896.0': 4, '1895.0': 3, '1885.0': 3, '1892.0': 2, '1891.0': 2, '1889.0': 2, '1882.0': 1, '1883.0': 1, '1893.0': 1, '1887.0': 1, '1880.0': 1, '1881.0': 1, '1890.0': 1, '1877.0': 1, '1888.0': 1}}}

exec(code, env_args)
