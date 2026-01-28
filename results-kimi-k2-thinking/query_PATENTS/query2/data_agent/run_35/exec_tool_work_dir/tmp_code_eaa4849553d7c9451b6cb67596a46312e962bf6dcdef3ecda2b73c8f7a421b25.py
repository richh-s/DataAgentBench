code = """import json

# From previous analysis
result_file = locals()['var_functions.query_db:9']
with open(result_file, 'r') as f:
    data = json.load(f)

# Filter for Germany patents across multiple years
germany_patents_all_years = []

for row in data:
    patents_info = str(row['Patents_info'])
    if 'DE-' not in patents_info:
        continue
    
    grant_date_str = str(row['grant_date'])
    if not grant_date_str or grant_date_str == 'None':
        continue
    
    # Extract year
    year_match = re.search(r'20\d{2}', grant_date_str)
    if year_match:
        year = int(year_match.group())
        if 2017 <= year <= 2021:  # Get a few years for EMA
            # Extract month
            month_match = re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)', grant_date_str, re.IGNORECASE)
            if month_match:
                month_str = month_match.group(1).capitalize()
                month_map = {
                    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
                    'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
                }
                month_num = month_map.get(month_str, 0)
                
                # Only second half for 2019, but all for other years
                is_second_half = (year == 2019 and month_num >= 7) or (year != 2019)
                
                if is_second_half:
                    # Extract CPC codes
                    cpc_str = str(row['cpc'])
                    if cpc_str and cpc_str != 'None':
                        try:
                            cpc_list = json.loads(cpc_str)
                            for cpc_item in cpc_list:
                                if isinstance(cpc_item, dict) and 'code' in cpc_item:
                                    cpc_code = cpc_item['code']
                                    if '/' in cpc_code:
                                        group_part = cpc_code.split('/')[0]
                                        if len(group_part) >= 4:
                                            level_4_group = group_part[:4]
                                            germany_patents_all_years.append({
                                                'patent_info': patents_info,
                                                'year': year,
                                                'month': month_num,
                                                'cpc_full': cpc_code,
                                                'cpc_level4': level_4_group
                                            })
                        except:
                            cpc_matches = re.findall(r'"code":\s*"([^"]+)"', cpc_str)
                            for cpc_code in cpc_matches:
                                if '/' in cpc_code:
                                    group_part = cpc_code.split('/')[0]
                                    if len(group_part) >= 4:
                                        level_4_group = group_part[:4]
                                        germany_patents_all_years.append({
                                            'patent_info': patents_info,
                                            'year': year,
                                            'month': month_num,
                                            'cpc_full': cpc_code,
                                            'cpc_level4': level_4_group
                                        })

print('Total Germany patents 2017-2021:', len(germany_patents_all_years))
print('Years represented:', sorted(set([x['year'] for x in germany_patents_all_years])))

# Get unique level 4 CPC groups
cpc_level4_groups = sorted(list(set([x['cpc_level4'] for x in germany_patents_all_years])))
print('Unique level 4 CPC groups:', len(cpc_level4_groups))

print('__RESULT__:')
print(json.dumps({
    'total_patents': len(germany_patents_all_years),
    'years': sorted(set([x['year'] for x in germany_patents_all_years])),
    'unique_cpc_level4': len(cpc_level4_groups),
    'sample_records': germany_patents_all_years[:5],
    'cpc_level4_list': cpc_level4_groups
}))"""

env_args = {'var_functions.list_db:2': ['publicationinfo'], 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:10': {'count': 0, 'sample': []}, 'var_functions.execute_python:12': {'total_records': 3838, 'germany_patents_found': 50, 'sample_germany': [{'info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'cpc': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F21/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'info': 'The DE application (number DE-102009046500-A) is owned by LEAR CORP and has publication number DE-102009046500-B4.', 'grant_date': 'Mar 21st, 2019', 'cpc': '[\n  {\n    "code": "G01R31/389",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01R31/389",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}]}, 'var_functions.execute_python:14': {'germany_patents_second_half_2019': 0, 'sample': []}, 'var_functions.execute_python:16': {'sample_dates_2019': [{'patent_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date_raw': '14th Mar 2019', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'patent_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date_raw': 'dated 21st November 2019', 'cpc': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F21/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'patent_info': 'The DE application (number DE-102009046500-A) is owned by LEAR CORP and has publication number DE-102009046500-B4.', 'grant_date_raw': 'Mar 21st, 2019', 'cpc': '[\n  {\n    "code": "G01R31/389",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01R31/389",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'patent_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'grant_date_raw': '5th of December, 2019', 'cpc': '[\n  {\n    "code": "F02D41/3005",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M65/005",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'patent_info': 'In DE, the patent filing (application no. DE-112014003420-T) is assigned to TOYOTA MOTOR CO LTD and has publication number DE-112014003420-B4.', 'grant_date_raw': '22nd of August, 2019', 'cpc': '[\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}], 'second_half_count': 24, 'sample_second_half': [{'patent_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date_raw': 'dated 21st November 2019', 'month': 11, 'cpc': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F21/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'patent_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'grant_date_raw': '5th of December, 2019', 'month': 12, 'cpc': '[\n  {\n    "code": "F02D41/3005",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M65/005",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'patent_info': 'In DE, the patent filing (application no. DE-112014003420-T) is assigned to TOYOTA MOTOR CO LTD and has publication number DE-112014003420-B4.', 'grant_date_raw': '22nd of August, 2019', 'month': 8, 'cpc': '[\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}]}, 'var_functions.execute_python:18': {'total_records': 252, 'unique_level4_groups': 49, 'sample_records': [{'patent_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'grant_month': 11, 'cpc_full': 'B41F21/102', 'cpc_level4': 'B41F', 'year': 2019}, {'patent_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'grant_month': 11, 'cpc_full': 'B41F22/00', 'cpc_level4': 'B41F', 'year': 2019}, {'patent_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'grant_month': 11, 'cpc_full': 'B41F21/00', 'cpc_level4': 'B41F', 'year': 2019}, {'patent_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'grant_date': '5th of December, 2019', 'grant_month': 12, 'cpc_full': 'F02D41/3005', 'cpc_level4': 'F02D', 'year': 2019}, {'patent_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'grant_date': '5th of December, 2019', 'grant_month': 12, 'cpc_full': 'F02D41/20', 'cpc_level4': 'F02D', 'year': 2019}], 'cpc_level4_list': ['B60R', 'F04B', 'F42B', 'F24B', 'Y10T', 'E02F', 'A61L', 'E05B', 'B23K', 'A43B', 'B29C', 'G01N', 'Y02T', 'F02M', 'G07C', 'F02D', 'A61B', 'H01F', 'G01D', 'B64D', 'F41H', 'A47J', 'Y02E', 'H01H', 'F23N', 'A21C', 'C09K', 'H02J', 'G01F', 'B63B', 'B29D', 'H04L', 'B60W', 'B66C', 'Y02D', 'A61F', 'F23L', 'B60S', 'F02N', 'F23B', 'H04W', 'F02P', 'B41F', 'F16H', 'H01J', 'B60K', 'G02B', 'H01R', 'C04B']}}

exec(code, env_args)
