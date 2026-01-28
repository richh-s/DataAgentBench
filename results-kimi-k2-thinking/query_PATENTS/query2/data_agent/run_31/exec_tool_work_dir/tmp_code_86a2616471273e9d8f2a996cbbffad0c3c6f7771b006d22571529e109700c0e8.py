code = """import json
import re
from collections import defaultdict, Counter

# First, filter for patents granted in H2 2019 (July-December)
result_file = locals()['var_functions.query_db:17']
with open(result_file, 'r') as f:
    german_patents = json.load(f)

# Extract H2 2019 patents and their CPC level 4 codes
h2_2019_patents = []
h2_2019_cpc_groups = set()

year_pattern = re.compile(r'(\d{4})')
month_pattern = re.compile(r'(January|February|March|April|May|June|July|August|September|October|November|December)', re.IGNORECASE)

for patent in german_patents:
    try:
        grant_date = patent['grant_date']
        
        # Check if it's 2019
        year_match = year_pattern.search(grant_date)
        if not year_match or int(year_match.group(1)) != 2019:
            continue
            
        # Check if it's H2 (July-December)
        month_match = month_pattern.search(grant_date)
        if not month_match:
            continue
            
        month = month_match.group(1).lower()
        if month not in ['july', 'august', 'september', 'october', 'november', 'december']:
            continue
        
        h2_2019_patents.append(patent)
        
        # Extract CPC codes for this patent
        cpc_list = json.loads(patent['cpc'])
        for cpc in cpc_list:
            code = cpc['code']
            if '/' not in code:
                continue
            
            main_part, subgroup = code.split('/')
            section = main_part[0]
            class_num = main_part[1:3]
            subclass = main_part[3] if len(main_part) > 3 else ''
            
            if len(main_part) > 4:
                group_digits = main_part[4:]
                level4_code = f"{section}{class_num}{subclass}{group_digits}"
                h2_2019_cpc_groups.add(level4_code)
    except:
        continue

print(f"__RESULT__:")
print(json.dumps({
    "h2_2019_patents": len(h2_2019_patents),
    "unique_cpc_level4_groups_in_h2_2019": len(h2_2019_cpc_groups),
    "sample_cpc_groups": list(h2_2019_cpc_groups)[:20]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'total_patents': 18, 'first_patent': {'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'cpc': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F21/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'dated 21st November 2019'}, 'sample_cpc': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"'}, 'var_functions.execute_python:14': {'total_level4_codes': 219, 'unique_level4_codes': 69, 'top_level4_codes': {'C04B2235': 32, 'H04W52': 12, 'C04B35': 12, 'H04L1': 10, 'H04W72': 9, 'B29C2049': 9, 'F02M59': 8, 'F02D41': 6, 'A61F5': 6, 'B29C49': 5}, 'all_level4_codes': ['B41F21', 'B41F22', 'F02D41', 'F02M65', 'F02M59', 'F02M55', 'F04B53', 'G01D11', 'B23K1', 'B63B21', 'H04W72', 'H04L5', 'H04L1', 'H04W52', 'H04W76', 'Y02D30', 'B66C23', 'E02F9', 'B60S9', 'F02D15', 'F02D13', 'Y02T10', 'A61F5', 'A43B17', 'A43B7', 'A43B13', 'F24B5', 'F23L15', 'F23L1', 'F23B60', 'F23B50', 'F23N1', 'Y02E20', 'H01R35', 'B64D11', 'H01R2201', 'H01R24', 'H01R13', 'B60R16', 'F02N2200', 'F02N2300', 'F02N11', 'B60K6', 'B60W30', 'C04B2235', 'C04B35', 'C09K11', 'C04B40', 'B29C49', 'B29C2049', 'B29C2949', 'G02B15', 'A61B1', 'G02B13', 'G02B23', 'Y10T70', 'G07C9', 'B29C2045', 'B29D99', 'H01H9', 'B29C45', 'H01H2009', 'E05B19', 'F16H37', 'F16H2200', 'F16H3', 'E02F3', 'F42B3', 'F41H11']}, 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json', 'var_functions.execute_python:18': {'total_patents_processed': 510, 'cpc_level4_groups': 1038, 'year_range': '2010 - 2019', 'sample_cpc_groups': ['B26B5', 'B64G1', 'F16C33', 'F16C2326', 'F16C19', 'F16C32', 'G01D5', 'B60N3', 'B60N2', 'F41H7'], 'sample_yearly_counts': {'B26B5': {'2010': 4}, 'B64G1': {'2016': 6}, 'F16C33': {'2016': 2, '2014': 2, '2010': 2, '2019': 3, '2013': 9}}}}

exec(code, env_args)
