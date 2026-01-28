code = """import json
import re
from collections import defaultdict

# Get the stored file path
file_path = locals()['var_functions.query_db:50']

# Load full data
with open(file_path, 'r') as f:
    publications = json.load(f)

print('Processing ' + str(len(publications)) + ' publications...')

# Data structures for analysis
year_cpc_counts = defaultdict(lambda: defaultdict(int))
cpc_year_counts = defaultdict(lambda: defaultdict(int))
all_years = set()

# Process publications
for i, pub in enumerate(publications):
    if i % 50000 == 0:
        print('Processed ' + str(i) + ' records...')
    
    # Extract year
    date_str = pub.get('publication_date', '')
    year_match = re.search(r'(\d{4})', date_str)
    if not year_match:
        continue
    
    year = int(year_match.group(1))
    all_years.add(year)
    
    # Parse CPC codes
    cpc_str = pub.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str)
        for item in cpc_list:
            code = item.get('code', '')
            if code:
                # Get level 5 code (first 5 chars of main class)
                main_class = code.split('/')[0]
                if len(main_class) >= 5:
                    level5_code = main_class[:5]
                    year_cpc_counts[year][level5_code] += 1
                    cpc_year_counts[level5_code][year] += 1
    except:
        continue

print('Data spans years ' + str(min(all_years)) + ' to ' + str(max(all_years)))
print('Found ' + str(len(cpc_year_counts)) + ' unique level 5 CPC codes')

# Calculate EMA for each CPC code
alpha = 0.2
results = []
year_range = range(min(all_years), max(all_years) + 1)

for cpc_code in cpc_year_counts:
    counts = cpc_year_counts[cpc_code]
    
    # Calculate EMA across years
    time_series = []
    ema_prev = None
    
    for year in year_range:
        count = counts.get(year, 0)
        
        if ema_prev is None:
            ema = float(count)
        else:
            ema = alpha * count + (1 - alpha) * ema_prev
        
        ema_prev = ema
        time_series.append((year, ema))
    
    # Find year with highest EMA
    if time_series:
        best_year, best_ema = max(time_series, key=lambda x: x[1])
        
        # Filter for best year = 2022
        if best_year == 2022:
            results.append({
                'cpc_code': cpc_code,
                'best_ema': best_ema
            })

# Sort by EMA descending
results_sorted = sorted(results, key=lambda x: x['best_ema'], reverse=True)

# Get all codes
all_codes = [r['cpc_code'] for r in results_sorted]

print('Found ' + str(len(all_codes)) + ' CPC level 5 codes with peak EMA in 2022')

# Return all codes
final_result = json.dumps(all_codes)
print('__RESULT__:')
print(final_result)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': [{'count': '277813'}], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': [{'publication_date': 'on March 15th, 2022'}, {'publication_date': '25th Jan 2022'}, {'publication_date': 'April 19th, 2022'}, {'publication_date': '28th June 2022'}, {'publication_date': '25th October 2022'}], 'var_functions.execute_python:44': ['H01L2', 'A61K3', 'G06F1', 'G06F3', 'H04L6', 'H04N2', 'A61B5', 'A61B2', 'G01N2', 'A61P3', 'A61B1', 'A61K4', 'H04W7', 'A61K9', 'G01N3', 'H04L4', 'H04W4', 'C04B2', 'H04L1', 'A61P2', 'B29C6', 'H01L3', 'C22C3', 'A61L2', 'C12N1', 'G02B2', 'B29C4', 'G06Q2', 'C08F2', 'H04L9', 'C07C2', 'H01R1', 'G03F7', 'G11C1', 'B01L2', 'B01J3', 'C02F1', 'B23K2', 'H01M8', 'C09D1', 'C12Q1', 'F17C2', 'B60R2', 'A61H2', 'C01P2', 'B01D5', 'E21B4', 'H01Q1', 'C04B3', 'B22F1', 'G05B1', 'C09K1', 'C12N9', 'A61B3', 'H04N5', 'G02B1', 'F04D2', 'C08K3', 'C12Q2', 'G01N1', 'B01F2', 'B60R1', 'A61B8', 'H01S5', 'B60L2', 'H04R2', 'B05B1', 'F25B2', 'H01F2', 'A47L1', 'C08G7', 'B25J1', 'H03M1', 'B60W1', 'A47J3', 'B23K3', 'C21D8', 'Y02T9', 'G06K1', 'H04N7', 'C09D7', 'C10G2', 'B01L3', 'G11C2', 'D06M1', 'F16C3', 'C08J5', 'F16K3', 'B60H1', 'F15B2', 'F16C2', 'D06F3', 'B65G4', 'E02F9', 'B01F3', 'B01D3', 'E21B3', 'H01L5', 'B65G1', 'C12M2', 'A43B1', 'G01B1', 'C07C3', 'H02M7', 'G03B2', 'A61B9', 'H01R4', 'G01F1', 'E04F1', 'E04B1', 'G11C7', 'G06K7', 'F25B4', 'B01J1', 'H01G1', 'G01M1', 'B22F2', 'B60T1', 'F16C1', 'C12Y3', 'B08B1', 'G03B1', 'B29C3', 'F16J1', 'H04N9', 'H02K7', 'A61P7', 'B23K9', 'C21D2', 'C07C6', 'A61C1', 'C09J7', 'H10N7', 'B65D7', 'C22C1', 'F16F1', 'C30B2', 'G02B7', 'A23L1', 'C09K8', 'C04B4', 'F26B2', 'B64D2', 'F16L5', 'B22D1', 'C22C2', 'B60Q1', 'A41D1', 'F15B1', 'E21B2', 'C10L2', 'C07D5', 'B64U2', 'C07H1', 'E04B2', 'F04B3', 'B23K1', 'B02C1', 'B23Q1', 'B05C1', 'G01J5', 'B65D4', 'A45D2', 'G01L1', 'B60T8', 'B64C1', 'H04R3', 'H01B7', 'B60L1', 'G01D5', 'C08L9', 'C12M4', 'B02C2', 'B64D1', 'C07K7', 'A61L1', 'G01R2', 'H02G3', 'B07B1', 'H05B6', 'E04H1', 'H01F4', 'F16B2', 'C07K5', 'C08L1', 'C10J2', 'B08B3', 'B60T2', 'A61G1', 'E05F1', 'B60G1', 'G01F2', 'G02C7', 'F02B3', 'A01K1', 'B82Y3', 'F21W2', 'B64C3', 'B82Y4', 'G01C1', 'C11D7', 'C21D6', 'A61L9', 'C04B1', 'B66C1', 'C03B3', 'F17C1', 'A23K5', 'G03F1', 'B22F3', 'E05B8', 'A61K5', 'A61H3', 'B25B2', 'C12Y1', 'G01J2', 'A41D2', 'B60B2', 'D06M2', 'G01V2', 'H04W9', 'F16K2', 'A47G2', 'B05D1', 'H04S2', 'C10G4', 'D01D5', 'H01Q9', 'C08K7', 'F04B5', 'G16B2', 'B60H2', 'F16B1', 'G21C1', 'G11C5', 'B62K2', 'B24B5', 'B05D7', 'F16B3', 'H10B6', 'H01B3', 'B65H7', 'B07C5', 'F16H1', 'G06F7', 'B01J4', 'H02S2', 'G01B2', 'Y02E2', 'B64D4', 'G06N7', 'B41J3', 'A43B2', 'A47C7', 'F25B1', 'G09B1', 'E05B1', 'H01Q5', 'E21B7', 'G10H2', 'G01V3', 'H01F3', 'F23D1', 'C01B1', 'B60B3', 'E01C1', 'C10G1', 'A47C2', 'C05F1', 'H01L4', 'G01L5', 'A47B9', 'A61G2', 'D07B2', 'B61L2', 'B05D2', 'C12N7', 'E04D1', 'D02G3', 'G01G1', 'F16B5', 'B25B1', 'A61C8', 'A01D3', 'G01P1', 'B65F1', 'H01H9', 'G07D7', 'A01G3', 'F16H4', 'G16B4', 'B60T7', 'E05B7', 'B33Y4', 'A41D3', 'B60Q3', 'B05C5', 'H02P6', 'B06B1', 'H04S7', 'C07H2', 'B64U5', 'C12M3', 'G09B5', 'G07G1', 'H05B1', 'B81C1', 'D01F6', 'A47B8', 'H04R5', 'B65D6', 'A61K6', 'B21J1', 'F01M1', 'G16B3', 'E03F5', 'B62J4', 'G11C8', 'H02N2', 'A01C1', 'C10G6', 'H03K5', 'A45F2', 'B26B1', 'H04Q9', 'A01G7', 'E21D1', 'G01B7', 'H02K4', 'E01B2', 'Y04S4', 'C11D2', 'A01M2', 'A47G1', 'B62B5', 'F03D8', 'D06N2', 'E01D1', 'B64F5', 'A01B6', 'C23C8', 'A01N1', 'B62B3', 'F02C3', 'F16D5', 'B01L7', 'F24F7', 'D01F1', 'F01M2', 'B66B2', 'B64U3', 'B60C9', 'A23F5', 'A45F3', 'A43B3', 'G09F3', 'G01D1', 'C21C7', 'E01D2', 'B24D1', 'F23G2', 'B30B9', 'A23G1', 'B43K2', 'B61L1', 'A01B7', 'C03B5', 'B24B1', 'C09C3', 'B28D5', 'F02B6', 'B60J7', 'B66D1', 'B01L9', 'E21D9', 'E04C3', 'B65B7', 'G02C1', 'F02C6', 'E02B1', 'B82Y5', 'B02C4', 'B41F3', 'A23B4', 'B22F7', 'F16B7', 'A47C3', 'A41C3', 'B28B7', 'C01G3', 'C01D1', 'F21V9', 'F16L4', 'C30B3', 'G16B5', 'A44C5', 'B05B5', 'G01P3', 'C12M1', 'B62J1', 'A01K5', 'B60N3', 'B65C9', 'B66F7', 'A23K4', 'A63F9', 'A23P2', 'H02M5', 'B01D9', 'G06K2', 'A47B4', 'G08B7', 'A61H7', 'C03C4', 'G07B1', 'A61B4', 'B60G7', 'D07B1', 'A41B1', 'C09B5', 'D01F8', 'G21K1', 'B26D3', 'H01G2', 'A41B2', 'G09B9', 'A01K3', 'H02S1', 'E04H6', 'B62B7', 'G04B3', 'C22C4', 'G01P2', 'F02F3', 'F04F5', 'A47F5', 'E01F9', 'B60K7', 'A45F5', 'A47F1', 'Y04S3', 'C04B7', 'F21S9', 'F01C2', 'B44C1', 'B28D1', 'F23G7', 'Y02T7', 'B61F5', 'C12Y5', 'A01H4', 'C09J4', 'A01B4', 'C12P3', 'G01V8', 'G09B7', 'B31F1', 'F17C5', 'F27B9', 'G01N9', 'C01C1', 'H02P1', 'F04B9', 'D01D1', 'H01B9', 'F17D1', 'C09D2', 'C09B1', 'E02B7', 'E03B3', 'G01C3', 'G07C1', 'B21F1', 'B28D7', 'F24S3', 'E05B3', 'G01P5', 'A47B5', 'A47B3', 'B64B1', 'E03F1', 'A61J9', 'A01F2', 'F41H1', 'F24T1', 'A61Q7', 'G21F5', 'F01N5', 'B62J9', 'B60S3', 'H01F5', 'G04B4', 'F17C9', 'E03C2', 'Y04S5', 'H02P7', 'A47B7', 'B05C9', 'A61D7', 'B06B2', 'B66B9', 'B43L1', 'E05D2', 'E04D2', 'B66F3', 'B27K2', 'B27D1', 'C08H6', 'G08B6', 'C05C9', 'H10B2', 'F24S5', 'F01K7', 'B60R3', 'G01D3', 'G21K5', 'G05G9', 'C06B2', 'F17C7', 'B66C9', 'G05D3', 'B27M3', 'C07F3', 'B62D4', 'C30B7', 'E05B5', 'A01D7', 'H05H7', 'C25D9', 'B27G1', 'C23G3', 'A41B9', 'B66B3', 'D21B1', 'F28G1', 'B07C2', 'B61K9', 'B29D7', 'B23D2', 'C09K9', 'B02C7', 'G10C3', 'G01N5', 'B03B5', 'C07J6', 'G07D5', 'B64C5', 'B60G9', 'B44F9', 'B09C2', 'E04B7', 'F24S6', 'E21C4', 'F27D7', 'D02G1', 'B01F7', 'B61B3', 'B23F1', 'F41J5', 'B61L5', 'B07B4', 'B67B7', 'C12C7', 'B07B9', 'F25B7', 'A43D8', 'B24C7', 'C07G1', 'H02B3', 'G21C9', 'B44F1', 'A41H3', 'B22C2', 'B64D9', 'E04H2', 'D04C1', 'A43C7', 'A45D6', 'F24V3', 'A21B3', 'B60L8', 'F41A5', 'F16M7', 'D07B7', 'B61G9', 'B02B3', 'G01J4', 'F02C1', 'H03G9', 'B64U6', 'B27C5', 'C23F2', 'A41G3', 'C06B3', 'B03C5', 'B25B7', 'A45D7', 'G04D3', 'F23Q3', 'F24T2', 'A23Y2', 'B23H2', 'B60Q7', 'B62J7', 'H03L2', 'G07G5', 'B64C7', 'F01M9', 'B66D2', 'B60S9', 'B60M3', 'C05C5', 'B21H1', 'B60B5', 'B66C3', 'A61D3', 'B62D9', 'A41C5', 'G10D7', 'A21B5', 'B81B1', 'B03B1', 'B61G1', 'G21H1', 'B61G3', 'F16M5', 'F23G1', 'B27G3', 'B42C5', 'B42C7', 'B23C9', 'B81C3', 'B07C1', 'H05H9', 'B25F3', 'D06B9', 'B64F3', 'C09B7', 'B66C7', 'G10G1', 'B81B5', 'G10C1', 'B21L1', 'F42C7', 'B31C1', 'C04B5', 'B61H9', 'E01F5', 'A62B5', 'C12P9', 'H05F7', 'G08G7', 'G10G7', 'F26B7', 'A63G4', 'H02H6', 'B63G1', 'F41H9', 'F03B7', 'G21K7', 'B61D9', 'E04D7', 'B42F9', 'F28G2', 'C12L3', 'F01P9', 'E01B5', 'G01P7', 'G12B5', 'B27H1', 'B64G4', 'C12C2', 'B31C5', 'B31C9', 'G01H7', 'F41B7', 'E21D5', 'E21F3', 'A23N2', 'G21H3', 'E21D8', 'A22B2', 'A63K1'], 'var_functions.execute_python:46': ['H01L2', 'A61K3', 'G06F1', 'G06F3', 'H04L6', 'H04N2', 'A61B5', 'A61B2', 'G01N2', 'A61P3', 'A61B1', 'A61K4', 'H04W7', 'A61K9', 'G01N3', 'H04L4', 'H04W4', 'C04B2', 'H04L1', 'A61P2', 'B29C6', 'H01L3', 'C22C3', 'A61L2', 'C12N1', 'G02B2', 'B29C4', 'G06Q2', 'C08F2', 'H04L9', 'C07C2', 'H01R1', 'G03F7', 'G11C1', 'B01L2', 'B01J3', 'C02F1', 'B23K2', 'H01M8', 'C09D1', 'C12Q1', 'F17C2', 'B60R2', 'A61H2', 'C01P2', 'B01D5', 'E21B4', 'H01Q1', 'C04B3', 'B22F1', 'G05B1', 'C09K1', 'C12N9', 'A61B3', 'H04N5', 'G02B1', 'F04D2', 'C08K3', 'C12Q2', 'G01N1', 'B01F2', 'B60R1', 'A61B8', 'H01S5', 'B60L2', 'H04R2', 'B05B1', 'F25B2', 'H01F2', 'A47L1', 'C08G7', 'B25J1', 'H03M1', 'B60W1', 'A47J3', 'B23K3', 'C21D8', 'Y02T9', 'G06K1', 'H04N7', 'C09D7', 'C10G2', 'B01L3', 'G11C2', 'D06M1', 'F16C3', 'C08J5', 'F16K3', 'B60H1', 'F15B2', 'F16C2', 'D06F3', 'B65G4', 'E02F9', 'B01F3', 'B01D3', 'E21B3', 'H01L5', 'B65G1', 'C12M2', 'A43B1', 'G01B1', 'C07C3', 'H02M7', 'G03B2', 'A61B9', 'H01R4', 'G01F1', 'E04F1', 'E04B1', 'G11C7', 'G06K7', 'F25B4', 'B01J1', 'H01G1', 'G01M1', 'B22F2', 'B60T1', 'F16C1', 'C12Y3', 'B08B1', 'G03B1', 'B29C3', 'F16J1', 'H04N9', 'H02K7', 'A61P7', 'B23K9', 'C21D2', 'C07C6', 'A61C1', 'C09J7', 'H10N7', 'B65D7', 'C22C1', 'F16F1', 'C30B2', 'G02B7', 'A23L1', 'C09K8', 'C04B4', 'F26B2', 'B64D2', 'F16L5', 'B22D1', 'C22C2', 'B60Q1', 'A41D1', 'F15B1', 'E21B2', 'C10L2', 'C07D5', 'B64U2', 'C07H1', 'E04B2', 'F04B3', 'B23K1', 'B02C1', 'B23Q1', 'B05C1', 'G01J5', 'B65D4', 'A45D2', 'G01L1', 'B60T8', 'B64C1', 'H04R3', 'H01B7', 'B60L1', 'G01D5', 'C08L9', 'C12M4', 'B02C2', 'B64D1', 'C07K7', 'A61L1', 'G01R2', 'H02G3', 'B07B1', 'H05B6', 'E04H1', 'H01F4', 'F16B2', 'C07K5', 'C08L1', 'C10J2', 'B08B3', 'B60T2', 'A61G1', 'E05F1', 'B60G1', 'G01F2', 'G02C7', 'F02B3', 'A01K1', 'B82Y3', 'F21W2', 'B64C3', 'B82Y4', 'G01C1', 'C11D7', 'C21D6', 'A61L9', 'C04B1', 'B66C1', 'C03B3', 'F17C1', 'A23K5', 'G03F1', 'B22F3', 'E05B8', 'A61K5', 'A61H3', 'B25B2', 'C12Y1', 'G01J2', 'A41D2', 'B60B2', 'D06M2', 'G01V2', 'H04W9', 'F16K2', 'A47G2', 'B05D1', 'H04S2', 'C10G4', 'D01D5', 'H01Q9', 'C08K7', 'F04B5', 'G16B2', 'B60H2', 'F16B1', 'G21C1', 'G11C5', 'B62K2', 'B24B5', 'B05D7', 'F16B3', 'H10B6', 'H01B3', 'B65H7', 'B07C5', 'F16H1', 'G06F7', 'B01J4', 'H02S2', 'G01B2', 'Y02E2', 'B64D4', 'G06N7', 'B41J3', 'A43B2', 'A47C7', 'F25B1', 'G09B1', 'E05B1', 'H01Q5', 'E21B7', 'G10H2', 'G01V3', 'H01F3', 'F23D1', 'C01B1', 'B60B3', 'E01C1', 'C10G1', 'A47C2', 'C05F1', 'H01L4', 'G01L5', 'A47B9', 'A61G2', 'D07B2', 'B61L2', 'B05D2', 'C12N7', 'E04D1', 'D02G3', 'G01G1', 'F16B5', 'B25B1', 'A61C8', 'A01D3', 'G01P1', 'B65F1', 'H01H9', 'G07D7', 'A01G3', 'F16H4', 'G16B4', 'B60T7', 'E05B7', 'B33Y4', 'A41D3', 'B60Q3', 'B05C5', 'H02P6', 'B06B1', 'H04S7', 'C07H2', 'B64U5', 'C12M3', 'G09B5', 'G07G1', 'H05B1', 'B81C1', 'D01F6', 'A47B8', 'H04R5', 'B65D6', 'A61K6', 'B21J1', 'F01M1', 'G16B3', 'E03F5', 'B62J4', 'G11C8', 'H02N2', 'A01C1', 'C10G6', 'H03K5', 'A45F2', 'B26B1', 'H04Q9', 'A01G7', 'E21D1', 'G01B7', 'H02K4', 'E01B2', 'Y04S4', 'C11D2', 'A01M2', 'A47G1', 'B62B5', 'F03D8', 'D06N2', 'E01D1', 'B64F5', 'A01B6', 'C23C8', 'A01N1', 'B62B3', 'F02C3', 'F16D5', 'B01L7', 'F24F7', 'D01F1', 'F01M2', 'B66B2', 'B64U3', 'B60C9', 'A23F5', 'A45F3', 'A43B3', 'G09F3', 'G01D1', 'C21C7', 'E01D2', 'B24D1', 'F23G2', 'B30B9', 'A23G1', 'B43K2', 'B61L1', 'A01B7', 'C03B5', 'B24B1', 'C09C3', 'B28D5', 'F02B6', 'B60J7', 'B66D1', 'B01L9', 'E21D9', 'E04C3', 'B65B7', 'G02C1', 'F02C6', 'E02B1', 'B82Y5', 'B02C4', 'B41F3', 'A23B4', 'B22F7', 'F16B7', 'A47C3', 'A41C3', 'B28B7', 'C01G3', 'C01D1', 'F21V9', 'F16L4', 'C30B3', 'G16B5', 'A44C5', 'B05B5', 'G01P3', 'C12M1', 'B62J1', 'A01K5', 'B60N3', 'B65C9', 'B66F7', 'A23K4', 'A63F9', 'A23P2', 'H02M5', 'B01D9', 'G06K2', 'A47B4', 'G08B7', 'A61H7', 'C03C4', 'G07B1', 'A61B4', 'B60G7', 'D07B1', 'A41B1', 'C09B5', 'D01F8', 'G21K1', 'B26D3', 'H01G2', 'A41B2', 'G09B9', 'A01K3', 'H02S1', 'E04H6', 'B62B7', 'G04B3', 'C22C4', 'G01P2', 'F02F3', 'F04F5', 'A47F5', 'E01F9', 'B60K7', 'A45F5', 'A47F1', 'Y04S3', 'C04B7', 'F21S9', 'F01C2', 'B44C1', 'B28D1', 'F23G7', 'Y02T7', 'B61F5', 'C12Y5', 'A01H4', 'C09J4', 'A01B4', 'C12P3', 'G01V8', 'G09B7', 'B31F1', 'F17C5', 'F27B9', 'G01N9', 'C01C1', 'H02P1', 'F04B9', 'D01D1', 'H01B9', 'F17D1', 'C09D2', 'C09B1', 'E02B7', 'E03B3', 'G01C3', 'G07C1', 'B21F1', 'B28D7', 'F24S3', 'E05B3', 'G01P5', 'A47B5', 'A47B3', 'B64B1', 'E03F1', 'A61J9', 'A01F2', 'F41H1', 'F24T1', 'A61Q7', 'G21F5', 'F01N5', 'B62J9', 'B60S3', 'H01F5', 'G04B4', 'F17C9', 'E03C2', 'Y04S5', 'H02P7', 'A47B7', 'B05C9', 'A61D7', 'B06B2', 'B66B9', 'B43L1', 'E05D2', 'E04D2', 'B66F3', 'B27K2', 'B27D1', 'C08H6', 'G08B6', 'C05C9', 'H10B2', 'F24S5', 'F01K7', 'B60R3', 'G01D3', 'G21K5', 'G05G9', 'C06B2', 'F17C7', 'B66C9', 'G05D3', 'B27M3', 'C07F3', 'B62D4', 'C30B7', 'E05B5', 'A01D7', 'H05H7', 'C25D9', 'B27G1', 'C23G3', 'A41B9', 'B66B3', 'D21B1', 'F28G1', 'B07C2', 'B61K9', 'B29D7', 'B23D2', 'C09K9', 'B02C7', 'G10C3', 'G01N5', 'B03B5', 'C07J6', 'G07D5', 'B64C5', 'B60G9', 'B44F9', 'B09C2', 'E04B7', 'F24S6', 'E21C4', 'F27D7', 'D02G1', 'B01F7', 'B61B3', 'B23F1', 'F41J5', 'B61L5', 'B07B4', 'B67B7', 'C12C7', 'B07B9', 'F25B7', 'A43D8', 'B24C7', 'C07G1', 'H02B3', 'G21C9', 'B44F1', 'A41H3', 'B22C2', 'B64D9', 'E04H2', 'D04C1', 'A43C7', 'A45D6', 'F24V3', 'A21B3', 'B60L8', 'F41A5', 'F16M7', 'D07B7', 'B61G9', 'B02B3', 'G01J4', 'F02C1', 'H03G9', 'B64U6', 'B27C5', 'C23F2', 'A41G3', 'C06B3', 'B03C5', 'B25B7', 'A45D7', 'G04D3', 'F23Q3', 'F24T2', 'A23Y2', 'B23H2', 'B60Q7', 'B62J7', 'H03L2', 'G07G5', 'B64C7', 'F01M9', 'B66D2', 'B60S9', 'B60M3', 'C05C5', 'B21H1', 'B60B5', 'B66C3', 'A61D3', 'B62D9', 'A41C5', 'G10D7', 'A21B5', 'B81B1', 'B03B1', 'B61G1', 'G21H1', 'B61G3', 'F16M5', 'F23G1', 'B27G3', 'B42C5', 'B42C7', 'B23C9', 'B81C3', 'B07C1', 'H05H9', 'B25F3', 'D06B9', 'B64F3', 'C09B7', 'B66C7', 'G10G1', 'B81B5', 'G10C1', 'B21L1', 'F42C7', 'B31C1', 'C04B5', 'B61H9', 'E01F5', 'A62B5', 'C12P9', 'H05F7', 'G08G7', 'G10G7', 'F26B7', 'A63G4', 'H02H6', 'B63G1', 'F41H9', 'F03B7', 'G21K7', 'B61D9', 'E04D7', 'B42F9', 'F28G2', 'C12L3', 'F01P9', 'E01B5', 'G01P7', 'G12B5', 'B27H1', 'B64G4', 'C12C2', 'B31C5', 'B31C9', 'G01H7', 'F41B7', 'E21D5', 'E21F3', 'A23N2', 'G21H3', 'E21D8', 'A22B2', 'A63K1'], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json'}

exec(code, env_args)
