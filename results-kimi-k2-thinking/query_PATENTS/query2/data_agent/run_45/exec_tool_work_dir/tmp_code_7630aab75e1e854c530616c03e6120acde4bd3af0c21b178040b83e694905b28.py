code = """import json
import re
from collections import defaultdict

# Load German patents data
file_path = locals()['var_functions.query_db:38']
with open(file_path, 'r') as f:
    german_patents = json.load(f)

print('Loaded', len(german_patents), 'German patents')

# Process to extract CPC codes and filing years
cpc_year_counts = defaultdict(lambda: defaultdict(int))
cpc_full_codes = defaultdict(set)
patent_years = []

for patent in german_patents:
    try:
        # Parse CPC JSON
        cpc_entries = json.loads(patent['cpc'])
        
        # Extract filing year
        filing_date = patent['filing_date']
        year_match = re.search(r'(\d{4})', filing_date)
        
        if year_match:
            filing_year = int(year_match.group(1))
            patent_years.append((filing_year, len(cpc_entries)))
            
            # Process each CPC entry
            for entry in cpc_entries:
                if isinstance(entry, dict) and 'code' in entry:
                    full_code = entry['code']
                    
                    # Extract level 4 code (main group before slash)
                    if '/' in full_code:
                        main_group = full_code.split('/')[0]
                        if len(main_group) >= 4:
                            level4 = main_group
                            cpc_year_counts[level4][filing_year] += 1
                            cpc_full_codes[level4].add(full_code)
    except Exception as e:
        continue

print('Found patents filed in years:', sorted(set(y[0] for y in patent_years)))
print('Total CPC level 4 groups:', len(cpc_year_counts))

# Show distribution
for cpc, years in list(cpc_year_counts.items())[:8]:
    print(f'{cpc}: {dict(years)}')

# Calculate Exponential Moving Average for each CPC group
# We need to consider the historical pattern
result = {
    'cpc_year_counts': {k: dict(v) for k, v in cpc_year_counts.items()},
    'full_codes': {k: list(v) for k, v in cpc_full_codes.items()},
    'filing_years_range': (min(patent_years)[0], max(patent_years)[0]) if patent_years else None,
    'total_patents': len(german_patents)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:20': {'cpc_year_counts': {}, 'cpc_all_codes': {}, 'total_german_patents': 0}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'country_code': 'US'}, {'country_code': 'DE'}, {'country_code': 'CU'}, {'country_code': 'EP'}, {'country_code': 'BR'}, {'country_code': 'AU'}, {'country_code': 'CN'}, {'country_code': 'SE'}, {'country_code': 'NL'}, {'country_code': 'RU'}, {'country_code': 'UA'}, {'country_code': 'DK'}, {'country_code': 'NO'}, {'country_code': 'GB'}, {'country_code': 'HU'}, {'country_code': 'AT'}, {'country_code': 'HR'}, {'country_code': 'ES'}, {'country_code': 'PL'}, {'country_code': 'GR'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:32': {'cpc_year_counts': {}, 'full_codes': {}, 'total_patents': 34}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.execute_python:40': {'cpc_year_counts': {'B41F21': {'2019': 2}, 'B41F22': {'2019': 1}, 'F02D41': {'2019': 9}, 'F02M65': {'2019': 1}, 'F02M59': {'2019': 8}, 'F02M55': {'2019': 2}, 'F04B53': {'2019': 2}, 'G01D11': {'2019': 1}, 'B23K1': {'2019': 1}, 'B63B21': {'2019': 1}, 'H04W72': {'2019': 9}, 'H04L5': {'2019': 4}, 'H04L1': {'2019': 10}, 'H04W52': {'2019': 12}, 'H04W76': {'2019': 1}, 'Y02D30': {'2019': 2}, 'B66C23': {'2019': 1}, 'E02F9': {'2019': 3}, 'B60S9': {'2019': 1}, 'F02D15': {'2019': 1}, 'F02D13': {'2019': 1}, 'Y02T10': {'2019': 4}, 'F16C33': {'2019': 3}, 'A47J37': {'2019': 1}, 'A21C9': {'2019': 1}, 'A61F5': {'2019': 6}, 'A43B17': {'2019': 2}, 'A43B7': {'2019': 2}, 'A43B13': {'2019': 1}, 'F24B5': {'2019': 3}, 'F23L15': {'2019': 3}, 'F23L1': {'2019': 3}, 'F23B60': {'2019': 1}, 'F23B50': {'2019': 3}, 'F23N1': {'2019': 1}, 'Y02E20': {'2019': 1}, 'H01J49': {'2019': 10}, 'G01M1': {'2019': 4}, 'F05D2270': {'2019': 1}, 'F04D29': {'2019': 1}, 'F05D2260': {'2019': 1}, 'F16F15': {'2019': 1}, 'F01D5': {'2019': 2}, 'H01R35': {'2019': 2}, 'B64D11': {'2019': 1}, 'H01R2201': {'2019': 2}, 'H01R24': {'2019': 1}, 'H01R13': {'2019': 1}, 'B60R16': {'2019': 1}, 'H01L23': {'2019': 3}, 'H01L2924': {'2019': 2}, 'H01L25': {'2019': 1}, 'B62D25': {'2019': 1}, 'B62D21': {'2019': 1}, 'F02N2200': {'2019': 2}, 'F02N2300': {'2019': 2}, 'F02N11': {'2019': 3}, 'B60K6': {'2019': 1}, 'B60W30': {'2019': 1}, 'C04B2235': {'2019': 32}, 'C04B35': {'2019': 12}, 'C09K11': {'2019': 2}, 'C04B40': {'2019': 1}, 'B29C49': {'2019': 5}, 'B29C2049': {'2019': 9}, 'B29C2949': {'2019': 1}, 'A61B2090': {'2019': 1}, 'G01N27': {'2019': 1}, 'A61L2': {'2019': 2}, 'A61B90': {'2019': 1}, 'G01N2021': {'2019': 1}, 'G02B5': {'2019': 2}, 'G02B21': {'2019': 4}, 'G02B26': {'2019': 2}, 'H01F27': {'2019': 2}, 'F02P15': {'2019': 2}, 'H01F38': {'2019': 2}, 'F02P3': {'2019': 2}, 'G02B15': {'2019': 5}, 'A61B1': {'2019': 3}, 'G02B13': {'2019': 2}, 'G02B23': {'2019': 5}, 'Y10T70': {'2019': 2}, 'G07C9': {'2019': 2}, 'B29C2045': {'2019': 2}, 'B29D99': {'2019': 1}, 'H01H9': {'2019': 2}, 'B29C45': {'2019': 2}, 'H01H2009': {'2019': 2}, 'E05B19': {'2019': 1}, 'F02D35': {'2019': 3}, 'G01L23': {'2019': 2}, 'F02D2250': {'2019': 1}, 'G01L27': {'2019': 2}, 'F02D2200': {'2019': 1}, 'G01F23': {'2019': 2}, 'F16H37': {'2019': 2}, 'F16H2200': {'2019': 2}, 'F16H3': {'2019': 1}, 'B60K23': {'2019': 1}, 'B60K17': {'2019': 1}, 'F16D2023': {'2019': 1}, 'F16D2011': {'2019': 1}, 'F16D27': {'2019': 1}, 'H02J1': {'2019': 2}, 'H02J7': {'2019': 4}, 'H04L7': {'2019': 2}, 'H03L7': {'2019': 6}, 'B60N2205': {'2019': 1}, 'B60N2': {'2019': 2}, 'E02F3': {'2019': 3}, 'F42B3': {'2019': 2}, 'F41H11': {'2019': 2}, 'G08B19': {'2019': 1}, 'G08B17': {'2019': 1}}, 'cpc_full_codes': {'B41F21': ['B41F21/102', 'B41F21/00'], 'B41F22': ['B41F22/00'], 'F02D41': ['F02D41/00', 'F02D41/222', 'F02D41/20', 'F02D41/009', 'F02D41/0087', 'F02D41/3005'], 'F02M65': ['F02M65/005'], 'F02M59': ['F02M59/06', 'F02M59/368', 'F02M59/102', 'F02M59/44'], 'F02M55': ['F02M55/04'], 'F04B53': ['F04B53/001'], 'G01D11': ['G01D11/24'], 'B23K1': ['B23K1/0016'], 'B63B21': ['B63B21/50'], 'H04W72': ['H04W72/56', 'H04W72/0446', 'H04W72/21'], 'H04L5': ['H04L5/0037', 'H04L5/0007'], 'H04L1': ['H04L1/1861', 'H04L1/1671', 'H04L1/1614', 'H04L1/1822', 'H04L1/1864'], 'H04W52': ['H04W52/0216', 'H04W52/0251', 'H04W52/0261', 'H04W52/0229'], 'H04W76': ['H04W76/28'], 'Y02D30': ['Y02D30/70'], 'B66C23': ['B66C23/80'], 'E02F9': ['E02F9/085', 'E02F9/006'], 'B60S9': ['B60S9/10'], 'F02D15': ['F02D15/00'], 'F02D13': ['F02D13/06'], 'Y02T10': ['Y02T10/40', 'Y02T10/62', 'Y02T10/12'], 'F16C33': ['F16C33/4635', 'F16C33/4676', 'F16C33/4682'], 'A47J37': ['A47J37/01'], 'A21C9': ['A21C9/00'], 'A61F5': ['A61F5/0111', 'A61F5/14', 'A61F5/0127'], 'A43B17': ['A43B17/00'], 'A43B7': ['A43B7/20'], 'A43B13': ['A43B13/223'], 'F24B5': ['F24B5/023'], 'F23L15': ['F23L15/04'], 'F23L1': ['F23L1/00'], 'F23B60': ['F23B60/00'], 'F23B50': ['F23B50/12'], 'F23N1': ['F23N1/027'], 'Y02E20': ['Y02E20/34'], 'H01J49': ['H01J49/4215', 'H01J49/0468', 'H01J49/0431', 'H01J49/164', 'H01J49/0031'], 'G01M1': ['G01M1/24', 'G01M1/28'], 'F05D2270': ['F05D2270/821'], 'F04D29': ['F04D29/662'], 'F05D2260': ['F05D2260/12'], 'F16F15': ['F16F15/322'], 'F01D5': ['F01D5/027'], 'H01R35': ['H01R35/04', 'H01R35/02'], 'B64D11': ['B64D11/0624'], 'H01R2201': ['H01R2201/26'], 'H01R24': ['H01R24/60'], 'H01R13': ['H01R13/633'], 'B60R16': ['B60R16/027'], 'H01L23': ['H01L23/34', 'H01L23/02', 'H01L23/48'], 'H01L2924': ['H01L2924/16195', 'H01L2924/01079'], 'H01L25': ['H01L25/072'], 'B62D25': ['B62D25/04'], 'B62D21': ['B62D21/157'], 'F02N2200': ['F02N2200/022', 'F02N2200/023'], 'F02N2300': ['F02N2300/2002', 'F02N2300/2011'], 'F02N11': ['F02N11/0814', 'F02N11/04', 'F02N11/006'], 'B60K6': ['B60K6/485'], 'B60W30': ['B60W30/194'], 'C04B2235': ['C04B2235/5481', 'C04B2235/3224', 'C04B2235/662', 'C04B2235/3203', 'C04B2235/666', 'C04B2235/72', 'C04B2235/77', 'C04B2235/661', 'C04B2235/6581', 'C04B2235/6565', 'C04B2235/445', 'C04B2235/5436', 'C04B2235/9653', 'C04B2235/3287', 'C04B2235/3229', 'C04B2235/6567'], 'C04B35': ['C04B35/6261', 'C04B35/547', 'C04B35/64', 'C04B35/645', 'C04B35/6455', 'C04B35/5156'], 'C09K11': ['C09K11/7772'], 'C04B40': ['C04B40/0007'], 'B29C49': ['B29C49/58', 'B29C49/06', 'B29C49/42087'], 'B29C2049': ['B29C2049/5868', 'B29C2049/5898', 'B29C2049/5817', 'B29C2049/5893', 'B29C2049/4294'], 'B29C2949': ['B29C2949/0715'], 'A61B2090': ['A61B2090/702'], 'G01N27': ['G01N27/221'], 'A61L2': ['A61L2/26', 'A61L2/28'], 'A61B90': ['A61B90/70'], 'G01N2021': ['G01N2021/6471'], 'G02B5': ['G02B5/20'], 'G02B21': ['G02B21/002', 'G02B21/0048', 'G02B21/0076', 'G02B21/0032'], 'G02B26': ['G02B26/023', 'G02B26/101'], 'H01F27': ['H01F27/33'], 'F02P15': ['F02P15/00'], 'H01F38': ['H01F38/12'], 'F02P3': ['F02P3/02'], 'G02B15': ['G02B15/143507', 'G02B15/15', 'G02B15/167'], 'A61B1': ['A61B1/00', 'A61B1/00188'], 'G02B13': ['G02B13/02', 'G02B13/18'], 'G02B23': ['G02B23/24', 'G02B23/243', 'G02B23/2415', 'G02B23/2438'], 'Y10T70': ['Y10T70/7051'], 'G07C9': ['G07C9/00944'], 'B29C2045': ['B29C2045/5635'], 'B29D99': ['B29D99/006'], 'H01H9': ['H01H9/0235'], 'B29C45': ['B29C45/561'], 'H01H2009': ['H01H2009/183'], 'E05B19': ['E05B19/0088'], 'F02D35': ['F02D35/023', 'F02D35/024'], 'G01L23': ['G01L23/22'], 'F02D2250': ['F02D2250/14'], 'G01L27': ['G01L27/007'], 'F02D2200': ['F02D2200/024'], 'G01F23': ['G01F23/36'], 'F16H37': ['F16H37/042', 'F16H37/046'], 'F16H2200': ['F16H2200/0056', 'F16H2200/0065'], 'F16H3': ['F16H3/006'], 'B60K23': ['B60K23/0808'], 'B60K17': ['B60K17/3462'], 'F16D2023': ['F16D2023/123'], 'F16D2011': ['F16D2011/004'], 'F16D27': ['F16D27/118'], 'H02J1': ['H02J1/10'], 'H02J7': ['H02J7/007182', 'H02J7/34'], 'H04L7': ['H04L7/0054', 'H04L7/0331'], 'H03L7': ['H03L7/091', 'H03L7/1806', 'H03L7/1976'], 'B60N2205': ['B60N2205/30'], 'B60N2': ['B60N2/3013', 'B60N2/3065'], 'E02F3': ['E02F3/96', 'E02F3/7631'], 'F42B3': ['F42B3/006'], 'F41H11': ['F41H11/16'], 'G08B19': ['G08B19/00'], 'G08B17': ['G08B17/00']}, 'total_patents': 34}}

exec(code, env_args)
