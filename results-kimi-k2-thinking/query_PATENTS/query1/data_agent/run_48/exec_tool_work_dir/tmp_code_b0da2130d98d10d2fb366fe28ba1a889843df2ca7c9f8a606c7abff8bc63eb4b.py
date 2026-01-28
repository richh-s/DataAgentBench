code = """import json
import re
import numpy as np
from collections import defaultdict

# Load CPC level 5 symbols
cpc_file = locals()['var_functions.query_db:42']
with open(cpc_file, 'r') as f:
    cpc_data = json.load(f)

cpc_level5_symbols = [item['symbol'] for item in cpc_data]
cpc_level5_set = set(cpc_level5_symbols)

print('Loaded {} CPC level 5 symbols'.format(len(cpc_level5_symbols)))

# Process publications file
publication_file = locals()['var_functions.query_db:12']

# Count by year and CPC code (level 5)
cpc_yearly_counts = defaultdict(lambda: defaultdict(int))
years_seen = set()

# Read publications data
with open(publication_file, 'r') as f:
    publications = json.load(f)
    
print('Processing {} publications'.format(len(publications)))

for pub in publications:
    # Extract year
    date_str = pub.get('publication_date', '')
    year_match = re.search(r'(\d{4})', date_str)
    if not year_match:
        continue
    
    year = int(year_match.group(1))
    years_seen.add(year)
    
    # Parse CPC codes
    cpc_data = pub.get('cpc', '')
    if not cpc_data:
        continue
    
    try:
        cpc_list = json.loads(cpc_data.replace("'", '"'))
    except:
        continue
    
    # Map each CPC code to level 5 and count
    for item in cpc_list:
        full_code = item.get('code', '')
        if not full_code:
            continue
        
        # Find matching level 5 symbol (first 4 characters typically)
        if len(full_code) >= 4:
            potential_symbol = full_code[:4]
            if potential_symbol in cpc_level5_set:
                cpc_yearly_counts[potential_symbol][year] += 1

print('Completed counting')
print('Years in data: {}'.format(sorted(years_seen)))
print('CPC codes with filings: {}'.format(len(cpc_yearly_counts)))

# Save results
with open('/tmp/cpc_yearly.json', 'w') as f:
    json.dump({k: dict(v) for k, v in cpc_yearly_counts.items()}, f)

# Sample output
sample_key = next(iter(cpc_yearly_counts))
result = {
    'total_cpc_codes': len(cpc_yearly_counts),
    'years_range': sorted(years_seen),
    'sample': {sample_key: dict(cpc_yearly_counts[sample_key])}
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:9': ['A01H', 'A01F', 'A01C', 'A01G', 'A23J', 'A01N', 'A01P', 'A01D', 'A01L', 'A01K', 'A01M', 'A01J', 'A01B', 'A21D', 'A21C', 'A21B', 'A22B', 'A22C', 'A23P', 'A23C', 'A23K', 'A23L', 'A23N', 'A23V', 'A23F', 'A23G', 'A23B', 'A23D', 'A24C', 'B21L', 'A24D', 'A24F', 'A24B', 'A41F', 'A41G', 'A41B', 'A47F', 'A41D', 'A41C', 'A41H', 'A42B', 'A42C', 'A43B', 'A43C', 'A43D', 'A44D', 'A44B', 'A44C', 'A45F', 'A45C', 'A45D', 'A45B', 'A46D', 'A46B', 'A47L', 'B22C', 'A47D', 'A47G', 'A47K', 'A47H', 'A47B', 'A47C', 'A47J', 'A61M', 'A61K', 'A61B', 'A61C', 'A61F', 'A61L', 'A61J', 'A61G', 'A61Q', 'A61P', 'B60V', 'A61H', 'A61D', 'A61N', 'A62C', 'A62D', 'A62B', 'A63G', 'A63K', 'A63B', 'A63J', 'A63C', 'A63D', 'A63F', 'C25D', 'A63H', 'A99Z', 'B01J', 'B01B', 'B01D', 'B01L', 'B01F', 'B02C', 'B02B', 'B03B', 'B03D', 'B03C', 'B04B', 'B04C', 'B07B', 'B05B', 'B05C', 'B05D', 'B06B', 'B07C', 'B08B', 'B09C', 'B09B', 'B21D', 'B21C', 'B21J', 'B21H', 'B21K', 'B23D', 'B21F', 'B21B', 'B21G', 'B22D', 'B22F', 'B23Q', 'B23B', 'B23C', 'B23K', 'B27C', 'B23G', 'B23P', 'B23H', 'B23F', 'B27M', 'B24B', 'B24D', 'B24C', 'B25D', 'B25J', 'B25F', 'B25B', 'B25C', 'B25H', 'B25G', 'B26F', 'B26B', 'B26D', 'B27D', 'B27F', 'B27L', 'B27J', 'B27G', 'B27K', 'B62L', 'B27B', 'B27H', 'B27N', 'B28B', 'B28C', 'B28D', 'B29D', 'B29K', 'B29C', 'B29B', 'B29L', 'B30B', 'B31D', 'B31B', 'B64G', 'B31F', 'B31C', 'B32B', 'B33Y', 'B41J', 'B41F', 'B41G', 'B41B', 'B41N', 'B41D', 'B41K', 'B41L', 'B41M', 'B41P', 'B41C', 'B42B', 'B42D', 'B42P', 'B42C', 'B42F', 'B43L', 'B43M', 'B43K', 'B44D', 'B44B', 'B44F', 'B44C', 'B60C', 'B60H', 'B60D', 'B60R', 'B60L', 'B60J', 'B60Y', 'B60W', 'B60N', 'B60Q', 'B60T', 'B60G', 'B60M', 'B60B', 'B60K', 'B60F', 'B60S', 'B60P', 'B61L', 'B61C', 'B61F', 'B61D', 'B61K', 'B61J', 'B61G', 'C40B', 'B61B', 'B61H', 'B62H', 'B62B', 'C99Z', 'B62J', 'B62K', 'B62C', 'B62D', 'B62M', 'B63J', 'B63C', 'B63H', 'C08B', 'B63G', 'B63B', 'B64F', 'B64U', 'B64D', 'B64C', 'B64B', 'B65B', 'B65H', 'B65F', 'B65G', 'B65C', 'B65D', 'B66B', 'B66F', 'B66D', 'B66C', 'B67C', 'B67B', 'B67D', 'B68C', 'B68G', 'B68B', 'B68F', 'B81B', 'B81C', 'B82Y', 'B82B', 'B99Z', 'C01C', 'C01B', 'C01G', 'C01D', 'C01F', 'C01P', 'C02F', 'C03C', 'D03D', 'C03B', 'C04B', 'C05G', 'C05B', 'D06G', 'C05D', 'C05C', 'C05F', 'C06D', 'E03F', 'C06C', 'C06B', 'C06F', 'C07H', 'C07F', 'C07D', 'C07J', 'C07B', 'C07K', 'C07C', 'C07G', 'C08J', 'C08F', 'C08H', 'C08L', 'C08C', 'C08G', 'C08K', 'C09H', 'C09B', 'C09C', 'C09D', 'C09G', 'C09F', 'C09K', 'D02J', 'C09J', 'C10K', 'C10M', 'C10N', 'C10F', 'C10G', 'C10C', 'C10J', 'C10B', 'C10H', 'C10L', 'C11C', 'C11D', 'D03C', 'C11B', 'C12J', 'C12N', 'C12C', 'C12R', 'C12Q', 'C12P', 'C12M', 'C12H', 'C12G', 'C12F', 'C12Y', 'C12L', 'C23G', 'C13K', 'C13B', 'C14C', 'C14B', 'C21B', 'C21D', 'C21C', 'C22F', 'C22C', 'C22B', 'C23C', 'C23F', 'C23D', 'D03J', 'C25C', 'C25B', 'C25F', 'C30B', 'D01H', 'D01G', 'D01B', 'D01D', 'D01F', 'D01C', 'D02H', 'D02G', 'D04D', 'D04C', 'D04B', 'D04G', 'D04H', 'D05D', 'D05B', 'D05C', 'D06Q', 'D06P', 'D06C', 'D06M', 'D06L', 'D06J', 'D06B', 'D06F', 'D06H', 'D06N', 'D07B', 'D10B', 'D21J', 'D21D', 'D21B', 'D21H', 'D21F', 'D21C', 'D21G', 'D99Z', 'E01H', 'E01C', 'E01B', 'E01F', 'E01D', 'E02D', 'E02C', 'E02F', 'E02B', 'E03B', 'E03D', 'E03C', 'E04H', 'E04C', 'E04G', 'E04F', 'E04D', 'E04B', 'F05C', 'E05B', 'E05C', 'E05G', 'E05Y', 'E05F', 'E05D', 'E06C', 'E06B', 'E21C', 'F05D', 'E21F', 'E21B', 'E21D', 'E99Z', 'F01M', 'F01L', 'F01N', 'F01B', 'F01C', 'F05B', 'F01K', 'F01P', 'F01D', 'F02P', 'F02K', 'F02C', 'F02F', 'F02D', 'F02G', 'F02M', 'F02B', 'F02N', 'F16G', 'F03D', 'F03H', 'F03B', 'F03C', 'F03G', 'F04B', 'F04F', 'F04C', 'F04D', 'F21Y', 'F15C', 'F15B', 'F15D', 'F16M', 'F16B', 'F16J', 'F16P', 'F16D', 'F16S', 'F16K', 'F16L', 'F16H', 'F16C', 'F16F', 'F16N', 'F16T', 'F17B', 'F17C', 'F17D', 'F21K', 'F21V', 'F21S', 'F21H', 'F21W', 'F21L', 'F23G', 'F22B', 'F22G', 'F22D', 'F23H', 'F23N', 'F23J', 'F23K', 'F23B', 'F23D', 'F23L', 'F23R', 'F23Q', 'F23C', 'F23M', 'F24T', 'F24S', 'F24F', 'F24H', 'F24V', 'F24D', 'F24C', 'F24B', 'F25C', 'F25B', 'F25J', 'F25D', 'F26B', 'F27M', 'F27D', 'F27B', 'F28C', 'F28F', 'F28B', 'F28D', 'F28G', 'F41F', 'F41A', 'F41C', 'F41G', 'F41J', 'F41H', 'F41B', 'F42D', 'F42B', 'F42C', 'F99Z', 'G01D', 'G01C', 'G01V', 'G01Q', 'G01J', 'G01R', 'G01P', 'G01M', 'G01N', 'G01F', 'G01B', 'G01H', 'H04L', 'G01G', 'G01T', 'G01L', 'G01S', 'G01K', 'G01W', 'G02F', 'G02B', 'G02C', 'G03B', 'G03D', 'G03H', 'G03C', 'G03F', 'G03G', 'G04B', 'G04R', 'G04D', 'G04F', 'G04C', 'G04G', 'G05D', 'G05G', 'G05B', 'G05F', 'G06N', 'G06F', 'G06K', 'G06Q', 'G06E', 'G06M', 'G06V', 'G06J', 'G06G', 'G06C', 'G10K', 'G06T', 'G06D', 'G07D', 'G07C', 'G10F', 'G07F', 'G07G', 'G07B', 'G08C', 'G08G', 'G08B', 'G09D', 'G09G', 'G09B', 'G09F', 'G09C', 'G10B', 'G10G', 'G10H', 'G10C', 'G10D', 'G10L', 'G11B', 'G11C', 'G12B', 'G16H', 'G16C', 'G16Z', 'G16B', 'G16Y', 'G21F', 'G21G', 'G21D', 'G21B', 'G21J', 'H01B', 'G21C', 'G21H', 'G21K', 'G99Z', 'H01Q', 'H01P', 'H01F', 'H01L', 'H01J', 'H01S', 'H01R', 'H01K', 'H01C', 'H02N', 'H01M', 'H01T', 'H01G', 'H01H', 'H03L', 'H02S', 'H02B', 'H02G', 'H02P', 'H02M', 'H02K', 'H02H', 'H02J', 'H03B', 'H03K', 'H03C', 'H03J', 'H03G', 'H03D', 'H03H', 'H03M', 'H03F', 'H04R', 'H04M', 'H04S', 'H04J', 'Y02T', 'Y02C', 'H04H', 'H04T', 'H04K', 'H04N', 'H04W', 'H04Q', 'H04B', 'H05B', 'H05F', 'H05K', 'H05C', 'H05G', 'H05H', 'H10N', 'H10B', 'H10K', 'H99Z', 'Y02E', 'Y02W', 'Y02A', 'Y02D', 'Y02B', 'Y02P', 'Y04S', 'Y10T', 'Y10S'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': [{'COUNT(*)': '277813'}], 'var_functions.execute_python:18': {'total_records': 277813, 'sample_parsed': True}, 'var_functions.query_db:28': [{'year': '2021'}, {'year': '2020'}, {'year': ' 7th'}, {'year': ' 9th'}, {'year': '16th'}, {'year': ' 3rd'}, {'year': '2022'}, {'year': ' 5th'}, {'year': ' 1st'}, {'year': '25th'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
