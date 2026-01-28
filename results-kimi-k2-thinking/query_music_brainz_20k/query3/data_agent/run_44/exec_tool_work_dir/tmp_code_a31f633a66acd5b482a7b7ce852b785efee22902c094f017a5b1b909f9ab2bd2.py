code = """import json
import pandas as pd
import re

# Load full data
tracks_file_path = locals()['var_functions.query_db:14']
with open(tracks_file_path, 'r') as f:
    tracks = json.load(f)

sales_file_path = locals()['var_functions.query_db:18']
with open(sales_file_path, 'r') as f:
    sales = json.load(f)

# Create DataFrames
df_tracks = pd.DataFrame(tracks)
df_sales = pd.DataFrame(sales)

# Convert revenue and units to numeric
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])
df_sales['total_units'] = pd.to_numeric(df_sales['total_units'])

# Normalization functions
def clean_text(text):
    if not text or text in ['None', '[unknown]', '   ', '']:
        return ''
    text = str(text).lower().strip()
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text.strip()

def extract_title(title):
    if not title or title == 'None':
        return ''
    title = str(title).lower().strip()
    title = re.sub(r'^\d+-\s*', '', title)
    title = re.sub(r'\s*\([^)]*\)\s*$', '', title)
    title = re.sub(r'\s*\[[^\]]*\]\s*$', '', title)
    title = re.sub(r'\s*-\s*.*$', '', title)
    title = re.sub(r'\s+', ' ', title)
    title = re.sub(r'[^a-z0-9\s]', '', text)
    return title.strip()

def normalize_year(year):
    if not year or year == 'None':
        return None
    year = str(year).strip()
    match = re.search(r'(\d{4})', year)
    if match:
        return int(match.group(1))
    match = re.search(r'(\d{2})', year)
    if match:
        year_num = int(match.group(1))
        return 1900 + year_num if year_num >= 50 else 2000 + year_num
    return None

# Apply normalization
df_tracks['clean_title'] = df_tracks['title'].apply(lambda x: extract_title(str(x)))
df_tracks['clean_artist'] = df_tracks['artist'].apply(lambda x: clean_text(str(x)))
df_tracks['clean_album'] = df_tracks['album'].apply(lambda x: clean_text(str(x)))
df_tracks['norm_year'] = df_tracks['year'].apply(normalize_year)

# Filter
df_tracks_filtered = df_tracks[
    (df_tracks['clean_title'] != '') | 
    (df_tracks['clean_artist'] != '')
].copy()

# Merge with sales
df_merged = df_tracks_filtered.merge(df_sales, on='track_id', how='inner')

result = {
    'tracks_with_sales': len(df_merged),
    'total_revenue': float(df_merged['total_revenue'].sum()),
    'top_tracks': df_merged.nlargest(10, 'total_revenue')[['track_id', 'title', 'artist', 'total_revenue', 'total_units']].to_dict('records')
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:2': ['sales'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'track_id': '14719', 'total_revenue': '2522.82', 'total_units': '2109.0'}, {'track_id': '5124', 'total_revenue': '2503.1899999999996', 'total_units': '2216.0'}, {'track_id': '1344', 'total_revenue': '2500.72', 'total_units': '2186.0'}, {'track_id': '6725', 'total_revenue': '2489.81', 'total_units': '2050.0'}, {'track_id': '10377', 'total_revenue': '2466.71', 'total_units': '2263.0'}, {'track_id': '5050', 'total_revenue': '2466.3100000000004', 'total_units': '2063.0'}, {'track_id': '6667', 'total_revenue': '2452.7000000000003', 'total_units': '2182.0'}, {'track_id': '7245', 'total_revenue': '2436.9700000000003', 'total_units': '2086.0'}, {'track_id': '11641', 'total_revenue': '2428.2200000000003', 'total_units': '2136.0'}, {'track_id': '964', 'total_revenue': '2425.61', 'total_units': '2194.0'}, {'track_id': '12984', 'total_revenue': '2401.71', 'total_units': '2018.0'}, {'track_id': '6208', 'total_revenue': '2385.0299999999997', 'total_units': '2035.0'}, {'track_id': '666', 'total_revenue': '2382.74', 'total_units': '2077.0'}, {'track_id': '12620', 'total_revenue': '2377.59', 'total_units': '2119.0'}, {'track_id': '19232', 'total_revenue': '2368.7499999999995', 'total_units': '2059.0'}, {'track_id': '17757', 'total_revenue': '2365.59', 'total_units': '2144.0'}, {'track_id': '3462', 'total_revenue': '2359.23', 'total_units': '2104.0'}, {'track_id': '9639', 'total_revenue': '2351.68', 'total_units': '1919.0'}, {'track_id': '18760', 'total_revenue': '2349.33', 'total_units': '1939.0'}, {'track_id': '2516', 'total_revenue': '2346.18', 'total_units': '1899.0'}, {'track_id': '6326', 'total_revenue': '2331.91', 'total_units': '1944.0'}, {'track_id': '5836', 'total_revenue': '2321.31', 'total_units': '1860.0'}, {'track_id': '9988', 'total_revenue': '2317.41', 'total_units': '1954.0'}, {'track_id': '18508', 'total_revenue': '2308.44', 'total_units': '1928.0'}, {'track_id': '10760', 'total_revenue': '2293.1099999999997', 'total_units': '2015.0'}, {'track_id': '9002', 'total_revenue': '2288.23', 'total_units': '1913.0'}, {'track_id': '14169', 'total_revenue': '2281.23', 'total_units': '1888.0'}, {'track_id': '9649', 'total_revenue': '2276.7200000000003', 'total_units': '1893.0'}, {'track_id': '10856', 'total_revenue': '2275.85', 'total_units': '1963.0'}, {'track_id': '7422', 'total_revenue': '2275.04', 'total_units': '2029.0'}, {'track_id': '8705', 'total_revenue': '2273.46', 'total_units': '1919.0'}, {'track_id': '5933', 'total_revenue': '2271.62', 'total_units': '1900.0'}, {'track_id': '5809', 'total_revenue': '2269.24', 'total_units': '2018.0'}, {'track_id': '16084', 'total_revenue': '2259.8599999999997', 'total_units': '2028.0'}, {'track_id': '9652', 'total_revenue': '2251.2200000000003', 'total_units': '2008.0'}, {'track_id': '3412', 'total_revenue': '2250.04', 'total_units': '1850.0'}, {'track_id': '15664', 'total_revenue': '2249.3900000000003', 'total_units': '1950.0'}, {'track_id': '12207', 'total_revenue': '2248.7200000000003', 'total_units': '1897.0'}, {'track_id': '5467', 'total_revenue': '2246.94', 'total_units': '2063.0'}, {'track_id': '13102', 'total_revenue': '2244.51', 'total_units': '1907.0'}, {'track_id': '4145', 'total_revenue': '2243.27', 'total_units': '1983.0'}, {'track_id': '13132', 'total_revenue': '2238.21', 'total_units': '1972.0'}, {'track_id': '13211', 'total_revenue': '2233.62', 'total_units': '1852.0'}, {'track_id': '2244', 'total_revenue': '2230.04', 'total_units': '1926.0'}, {'track_id': '18846', 'total_revenue': '2227.95', 'total_units': '1914.0'}, {'track_id': '2029', 'total_revenue': '2226.42', 'total_units': '1884.0'}, {'track_id': '3488', 'total_revenue': '2222.25', 'total_units': '1879.0'}, {'track_id': '17669', 'total_revenue': '2212.4700000000003', 'total_units': '1842.0'}, {'track_id': '12969', 'total_revenue': '2211.97', 'total_units': '1900.0'}, {'track_id': '12551', 'total_revenue': '2210.78', 'total_units': '1925.0'}, {'track_id': '7425', 'total_revenue': '2208.98', 'total_units': '1749.0'}, {'track_id': '17840', 'total_revenue': '2208.67', 'total_units': '1882.0'}, {'track_id': '284', 'total_revenue': '2203.46', 'total_units': '1858.0'}, {'track_id': '8338', 'total_revenue': '2201.58', 'total_units': '1858.0'}, {'track_id': '17958', 'total_revenue': '2200.09', 'total_units': '1857.0'}, {'track_id': '4528', 'total_revenue': '2197.84', 'total_units': '1864.0'}, {'track_id': '7864', 'total_revenue': '2197.7', 'total_units': '1906.0'}, {'track_id': '1820', 'total_revenue': '2196.76', 'total_units': '1983.0'}, {'track_id': '14830', 'total_revenue': '2188.8900000000003', 'total_units': '1989.0'}, {'track_id': '1357', 'total_revenue': '2183.4399999999996', 'total_units': '1838.0'}, {'track_id': '4330', 'total_revenue': '2181.13', 'total_units': '1964.0'}, {'track_id': '16180', 'total_revenue': '2177.7200000000003', 'total_units': '1920.0'}, {'track_id': '15802', 'total_revenue': '2176.8100000000004', 'total_units': '1836.0'}, {'track_id': '7120', 'total_revenue': '2172.4100000000003', 'total_units': '1835.0'}, {'track_id': '5995', 'total_revenue': '2171.1800000000003', 'total_units': '1986.0'}, {'track_id': '7178', 'total_revenue': '2170.29', 'total_units': '1883.0'}, {'track_id': '2654', 'total_revenue': '2169.67', 'total_units': '1885.0'}, {'track_id': '8877', 'total_revenue': '2169.1800000000003', 'total_units': '1887.0'}, {'track_id': '10923', 'total_revenue': '2168.92', 'total_units': '1814.0'}, {'track_id': '13038', 'total_revenue': '2165.17', 'total_units': '1792.0'}, {'track_id': '18874', 'total_revenue': '2164.2999999999997', 'total_units': '1884.0'}, {'track_id': '14686', 'total_revenue': '2163.69', 'total_units': '1882.0'}, {'track_id': '6829', 'total_revenue': '2162.79', 'total_units': '1936.0'}, {'track_id': '17414', 'total_revenue': '2162.06', 'total_units': '1787.0'}, {'track_id': '11425', 'total_revenue': '2161.0299999999997', 'total_units': '1864.0'}, {'track_id': '16618', 'total_revenue': '2160.98', 'total_units': '1845.0'}, {'track_id': '740', 'total_revenue': '2160.0299999999997', 'total_units': '1828.0'}, {'track_id': '7913', 'total_revenue': '2157.08', 'total_units': '1799.0'}, {'track_id': '17585', 'total_revenue': '2156.37', 'total_units': '1836.0'}, {'track_id': '16942', 'total_revenue': '2151.18', 'total_units': '1800.0'}, {'track_id': '15728', 'total_revenue': '2150.2099999999996', 'total_units': '1842.0'}, {'track_id': '5848', 'total_revenue': '2148.29', 'total_units': '1886.0'}, {'track_id': '12899', 'total_revenue': '2147.31', 'total_units': '1851.0'}, {'track_id': '15030', 'total_revenue': '2144.44', 'total_units': '1798.0'}, {'track_id': '16397', 'total_revenue': '2142.59', 'total_units': '1871.0'}, {'track_id': '8829', 'total_revenue': '2142.48', 'total_units': '1804.0'}, {'track_id': '15697', 'total_revenue': '2138.55', 'total_units': '1828.0'}, {'track_id': '11483', 'total_revenue': '2137.93', 'total_units': '1783.0'}, {'track_id': '348', 'total_revenue': '2137.29', 'total_units': '1797.0'}, {'track_id': '3738', 'total_revenue': '2133.81', 'total_units': '1821.0'}, {'track_id': '6077', 'total_revenue': '2133.03', 'total_units': '1919.0'}, {'track_id': '12178', 'total_revenue': '2131.18', 'total_units': '1887.0'}, {'track_id': '3886', 'total_revenue': '2130.43', 'total_units': '1780.0'}, {'track_id': '11280', 'total_revenue': '2129.8199999999997', 'total_units': '1867.0'}, {'track_id': '17450', 'total_revenue': '2128.47', 'total_units': '1834.0'}, {'track_id': '3224', 'total_revenue': '2127.63', 'total_units': '1914.0'}, {'track_id': '8941', 'total_revenue': '2124.15', 'total_units': '1807.0'}, {'track_id': '5379', 'total_revenue': '2123.83', 'total_units': '1785.0'}, {'track_id': '8324', 'total_revenue': '2122.5299999999997', 'total_units': '1753.0'}, {'track_id': '6015', 'total_revenue': '2122.5099999999998', 'total_units': '1854.0'}], 'var_functions.query_db:8': [{'track_id': '14719', 'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?", 'year': '2009', 'length': '223000', 'language': 'German'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'num_tracks': 19375, 'num_sales_records': 100, 'top_sales_preview': [{'track_id': '14719', 'total_revenue': '2522.82', 'total_units': '2109.0'}, {'track_id': '5124', 'total_revenue': '2503.1899999999996', 'total_units': '2216.0'}, {'track_id': '1344', 'total_revenue': '2500.72', 'total_units': '2186.0'}, {'track_id': '6725', 'total_revenue': '2489.81', 'total_units': '2050.0'}, {'track_id': '10377', 'total_revenue': '2466.71', 'total_units': '2263.0'}]}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:22': {'original_tracks': 19375, 'filtered_tracks': 19369, 'sales_records': 19375, 'sample_normalized': [{'track_id': '1', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'norm_title': 'daniel balavoine', 'artist': 'None', 'norm_artist': ''}, {'track_id': '2', 'title': '007', 'norm_title': '007', 'artist': '[unknown]', 'norm_artist': ''}, {'track_id': '3', 'title': 'Action PAINTING! - Mustard Gas', 'norm_title': 'action painting!', 'artist': 'None', 'norm_artist': ''}, {'track_id': '4', 'title': 'Your Grace', 'norm_title': 'your grace', 'artist': 'Kathy Troccoli', 'norm_artist': 'kathy troccoli'}, {'track_id': '5', 'title': "Well You Needn't", 'norm_title': "well you needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'norm_artist': 'ernie stadler jazz quintet'}, {'track_id': '6', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'norm_title': 'try (acoustic)', 'artist': 'Neil Young', 'norm_artist': 'neil young'}, {'track_id': '7', 'title': 'Bruce Maginnis - Sttreet Hype', 'norm_title': 'bruce maginnis', 'artist': 'None', 'norm_artist': ''}, {'track_id': '8', 'title': 'Luce Dufault - Ballade à donner', 'norm_title': 'luce dufault', 'artist': 'None', 'norm_artist': ''}, {'track_id': '9', 'title': "Just Like Tom Thumb's Blues (live)", 'norm_title': "just like tom thumb's blues", 'artist': 'Wendy Saddington', 'norm_artist': 'wendy saddington'}, {'track_id': '10', 'title': 'Στα καμένα', 'norm_title': '', 'artist': 'Λαυρέντης Μαχαιρίίτσας', 'norm_artist': 'λαυρέντης μαχαιρίίτσας'}]}}

exec(code, env_args)
