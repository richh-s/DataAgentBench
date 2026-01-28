code = """import json

# Load the CPC data from previous analysis
data_file = locals()['var_functions.query_db:12']
with open(data_file, 'r') as f:
    all_records = json.load(f)

# Extract all unique CPC level 4 codes from German H2 2019 patents
cpc_level4_codes = set()

# Reuse the parsing functions from previous analysis
month_map = {
    'jan': 1, 'january': 1, 'feb': 2, 'february': 2, 'mar': 3, 'march': 3,
    'apr': 4, 'april': 4, 'may': 5, 'jun': 6, 'june': 6,
    'jul': 7, 'july': 7, 'aug': 8, 'august': 8, 'sep': 9, 'september': 9,
    'oct': 10, 'october': 10, 'nov': 11, 'november': 11, 'dec': 12, 'december': 12
}

def get_cpc_level4(code):
    code = code.strip()
    parts = code.split('/')
    if len(parts) >= 1:
        main_group = parts[0]
        if len(main_group) >= 5:
            return main_group
    return None

def parse_grant_date(date_str):
    if not date_str or '2019' not in date_str:
        return None
    for month_abbr, month_num in month_map.items():
        if month_abbr in date_str.lower():
            return month_num, 2019
    return None

def extract_cpc_codes(cpc_str):
    if not cpc_str:
        return []
    try:
        cpc_data = json.loads(cpc_str.strip())
        return [item['code'] for item in cpc_data if isinstance(item, dict) and 'code' in item]
    except:
        return []

def is_german_patent(patents_info):
    if not patents_info:
        return False
    return 'DE-' in patents_info or 'Germany' in patents_info or 'German' in patents_info

# Collect CPC codes from German H2 2019 patents
for record in all_records:
    patents_info = record.get('Patents_info', '')
    grant_date = record.get('grant_date', '')
    cpc_str = record.get('cpc', '')
    
    if not is_german_patent(patents_info):
        continue
    
    date_result = parse_grant_date(grant_date)
    if date_result is None:
        continue
    
    month, year = date_result
    if year != 2019 or month < 7:
        continue
    
    cpc_codes = extract_cpc_codes(cpc_str)
    for code in cpc_codes:
        level4 = get_cpc_level4(code)
        if level4:
            cpc_level4_codes.add(level4)

print(f"Found {len(cpc_level4_codes)} unique CPC level 4 codes")

# Create comma-separated list for SQL query (limit to avoid too long query)
cpc_list = list(cpc_level4_codes)[:100]  # Limit to first 100 to avoid query too long
cpc_in_clause = "', '".join(cpc_list)

print('__RESULT__:')
print(json.dumps({
    'cpc_level4_count': len(cpc_level4_codes),
    'cpc_codes_sample': cpc_list[:20],
    'cpc_in_clause': cpc_in_clause
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'In RU, the patent filing (app. number RU-2017142236-A) is held by Sletov Aleksandr Anatolevich and has publication no. RU-2682615-C1.', 'grant_date': 'Mar 19th, 2019', 'cpc': '[\n  {\n    "code": "A61D1/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/645",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/6425",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/64",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/60",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/58",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The RU patent application (number RU-2018105657-A) is held by OBSHCHESTVO S OGRANICHENNOJ OTVETSTVENNOSTYU VORMKHOLS VNEDRENIE and has publication no. RU-2681783-C1.', 'grant_date': 'Mar 12th, 2019', 'cpc': '[\n  {\n    "code": "E21B33/136",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E21B33/134",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'grant_date': '2019 on Jul 12th', 'cpc': '[\n  {\n    "code": "G01S13/42",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S5/18",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41G3/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41H13/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'Patent application (number RU-2016134259-A) from RU, owned by KVINETIK LTD, with publication number RU-2681957-C2.', 'grant_date': 'on March 14th, 2019', 'cpc': '[\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/37",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DK patent application (number DK-14719221-T) is held by JASKE WOLFGANG and has publication number DK-2965013-T3.', 'grant_date': 'July 8th, 2019', 'cpc': '[\n  {\n    "code": "F25B2339/047",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D17/02",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B2400/061",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02B10/70",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D2200/20",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02B30/52",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D17/0005",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02B30/18",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D2200/123",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DK patent filing (application number DK-14835716-T) is owned by UNIV OSLO HF and has pub. number DK-3069138-T3.', 'grant_date': '8th April 2019', 'cpc': '[\n  {\n    "code": "G01N33/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N33/56977",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N33/56977",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/572",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61K39/39",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N2333/70539",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/55527",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C07K14/70503",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C07K14/70539",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/5158",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61K39/0011",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N33/505",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K39/0011",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/5158",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The RU patent application (ID RU-2018146701-U) is held by [] and has publication no. RU-189707-U1.', 'grant_date': '2019, May 30th', 'cpc': '[\n  {\n    "code": "B60P1/48",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The ES patent application (ID ES-11727548-T) is assigned to LOHR IND and has pub. number ES-2713511-T3.', 'grant_date': '22nd May 2019', 'cpc': '[\n  {\n    "code": "B61D3/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B61D3/182",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B61D3/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B61D3/16",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02T30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'Patents_info': 'In RU, the patent filing (application no. RU-2019124341-U) is owned by [] and has pub. number RU-193787-U1.', 'grant_date': '2019 on Nov 14th', 'cpc': '[\n  {\n    "code": "F16K17/192",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16L43/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_functions.execute_python:10': {'total_records': 10, 'german_h2_2019': 0, 'sample_records': [{'patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019', 'month': 3, 'in_h2_2019': False, 'is_german': True, 'cpc_codes': ['G06F9/45533', 'G06F9/45533']}, {'patents_info': 'In RU, the patent filing (app. number RU-2017142236-A) is held by Sletov Aleksandr Anatolevich and has publication no. RU-2682615-C1.', 'grant_date': 'Mar 19th, 2019', 'month': 3, 'in_h2_2019': False, 'is_german': False, 'cpc_codes': ['A61D1/00', 'A61B17/645', 'A61B17/6425', 'A61B17/64', 'A61B17/60', 'A61B17/58']}, {'patents_info': 'The RU patent application (number RU-2018105657-A) is held by OBSHCHESTVO S OGRANICHENNOJ OTVETSTVENNOSTYU VORMKHOLS VNEDRENIE and has publication no. RU-2681783-C1.', 'grant_date': 'Mar 12th, 2019', 'month': 3, 'in_h2_2019': False, 'is_german': False, 'cpc_codes': ['E21B33/136', 'E21B33/134']}, {'patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'grant_date': '2019 on Jul 12th', 'month': 7, 'in_h2_2019': True, 'is_german': False, 'cpc_codes': ['G01S13/42', 'G01S5/18', 'F41G3/00', 'F41H13/00']}, {'patents_info': 'Patent application (number RU-2016134259-A) from RU, owned by KVINETIK LTD, with publication number RU-2681957-C2.', 'grant_date': 'on March 14th, 2019', 'month': 3, 'in_h2_2019': False, 'is_german': False, 'cpc_codes': ['G01S19/30', 'G01S19/30', 'G01S19/30', 'G01S19/37', 'G01S19/30']}]}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'total_german_h2_2019': 34, 'sample_patents': [{'patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'month': 11, 'cpc_codes': ['B41F21/102', 'B41F22/00', 'B41F21/00']}, {'patents_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'grant_date': '5th of December, 2019', 'month': 12, 'cpc_codes': ['F02D41/3005', 'F02D41/20', 'F02M65/005', 'F02D41/00', 'F02D41/20', 'F02D41/20']}, {'patents_info': 'In DE, the patent filing (application no. DE-112014003420-T) is assigned to TOYOTA MOTOR CO LTD and has publication number DE-112014003420-B4.', 'grant_date': '22nd of August, 2019', 'month': 8, 'cpc_codes': ['F02M59/102', 'F02M55/04', 'F02M55/04', 'F02M59/102', 'F02M59/44', 'F02M59/06', 'F04B53/001', 'F02M59/368', 'F04B53/001', 'F02M59/44', 'F02M59/368', 'F02M59/06']}, {'patents_info': 'In DE, the patent filing (application number DE-102015221196-A) is owned by SCHOTT AG and has pub. number DE-102015221196-B4.', 'grant_date': 'September the 19th, 2019', 'month': 9, 'cpc_codes': ['G01D11/24', 'B23K1/0016']}, {'patents_info': 'The DE application (number DE-102014111322-A) is owned by LEMKE SEBASTIAN and has publication no. DE-102014111322-B4.', 'grant_date': '17th of October, 2019', 'month': 10, 'cpc_codes': ['B63B21/50']}, {'patents_info': 'Application (no. DE-112015005888-T) from DE, belonging to APPLE INC, with publication number DE-112015005888-B4.', 'grant_date': 'August the 29th, 2019', 'month': 8, 'cpc_codes': ['H04W72/21', 'H04W72/56', 'H04W72/21', 'H04W72/56', 'H04W72/56', 'H04W72/21', 'H04L5/0037', 'H04L1/1614', 'H04W52/0261', 'H04W52/0216', 'H04W52/0216', 'H04L1/1822', 'H04W52/0216', 'H04W52/0261', 'H04W52/0229', 'H04W72/0446', 'H04W52/0251', 'H04W72/0446', 'H04W72/0446', 'H04L5/0037', 'H04W52/0261', 'H04L1/1861', 'H04L5/0007', 'H04W52/0251', 'H04W76/28', 'H04W52/0229', 'H04W52/0251', 'H04L1/1864', 'H04L1/1671', 'H04W52/0229', 'H04L5/0007', 'Y02D30/70', 'Y02D30/70', 'H04L1/1822', 'H04L1/1861', 'H04L1/1614', 'H04L1/1864', 'H04L1/1671']}, {'patents_info': 'The DE application (ID DE-102016102746-A) is belonging to HAWE Altenstadt Holding GmbH and has pub. number DE-102016102746-B4.', 'grant_date': 'dated 4th July 2019', 'month': 7, 'cpc_codes': ['B66C23/80', 'E02F9/085', 'B60S9/10']}, {'patents_info': 'The DE patent filing (application no. DE-102018213557-A) is assigned to BAYERISCHE MOTOREN WERKE AG and has publication number DE-102018213557-B3.', 'grant_date': '26th September 2019', 'month': 9, 'cpc_codes': ['F02D41/0087', 'F02D15/00', 'F02D13/06', 'Y02T10/12']}, {'patents_info': 'In DE, the patent application (number DE-102011108701-A) is belonging to SUMITOMO HEAVY INDUSTRIES and has pub. number DE-102011108701-B4.', 'grant_date': '2019, December 24th', 'month': 12, 'cpc_codes': ['F16C33/4676', 'F16C33/4682', 'F16C33/4635']}, {'patents_info': 'The DE application (number DE-102015121777-A) is held by BOHNERTH OTTO and has publication no. DE-102015121777-B4.', 'grant_date': '2nd Oct 2019', 'month': 10, 'cpc_codes': ['A47J37/01', 'A21C9/00']}]}, 'var_functions.execute_python:16': {'german_h2_2019_patents_count': 34, 'cpc_level4_codes_count': 115, 'sample_cpc_data': {'B41F22': {'2019': 1}, 'B41F21': {'2019': 1}, 'F02M65': {'2019': 1}, 'F02D41': {'2019': 3}, 'F02M55': {'2019': 1}, 'F02M59': {'2019': 1}, 'F04B53': {'2019': 1}, 'G01D11': {'2019': 1}, 'B23K1': {'2019': 1}, 'B63B21': {'2019': 1}}, 'all_cpc_codes': ['B41F22', 'B41F21', 'F02M65', 'F02D41', 'F02M55', 'F02M59', 'F04B53', 'G01D11', 'B23K1', 'B63B21', 'H04W76', 'H04L5', 'H04W52', 'Y02D30', 'H04W72', 'H04L1', 'E02F9', 'B60S9', 'B66C23', 'Y02T10', 'F02D13', 'F02D15', 'F16C33', 'A21C9', 'A47J37', 'A43B13', 'A43B7', 'A43B17', 'A61F5', 'F24B5', 'F23L15', 'F23B50', 'Y02E20', 'F23L1', 'F23B60', 'F23N1', 'H01J49', 'G01M1', 'F01D5', 'F05D2260', 'F04D29', 'F16F15', 'F05D2270', 'B64D11', 'H01R13', 'B60R16', 'H01R24', 'H01R35', 'H01R2201', 'H01L23']}}

exec(code, env_args)
