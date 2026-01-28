code = """import json
import re

# Load UC patents map (pub_num -> CPC codes)
uc_path = locals()['var_functions.query_db:38']
with open(uc_path, 'r') as f:
    uc_data = json.load(f)

uc_patents_map = {}
for patent in uc_data:
    patents_info = patent['Patents_info']
    pub_match = re.search(r'pub[^\\w]*number[^\\w]*([A-Z]{2}-[^-]+-[A-Z][0-9])', patents_info, re.IGNORECASE)
    if pub_match:
        pub_num = pub_match.group(1)
        try:
            cpc_data = json.loads(patent['cpc'])
            cpc_codes = list(set([cpc['code'] for cpc in cpc_data if 'code' in cpc]))
            uc_patents_map[pub_num] = cpc_codes
        except:
            uc_patents_map[pub_num] = []

print('UC patents loaded: ' + str(len(uc_patents_map)))

# Load CPC definitions
cpc_def_path = locals()['var_functions.query_db:28']
with open(cpc_def_path, 'r') as f:
    cpc_defs = json.load(f)

cpc_title_map = {}
for item in cpc_defs:
    cpc_title_map[item['symbol']] = item['titleFull']

print('CPC title map loaded: ' + str(len(cpc_title_map)))

# Strategy: We need to find all patents that cite UC patents in their citation field
# Since the dataset is large, let's build a comprehensive but efficient query

uc_pub_numbers = list(uc_patents_map.keys())
print('UC publication numbers to search for: ' + str(len(uc_pub_numbers)))

# Build query patterns for a sample first
sample_patterns = uc_pub_numbers[:3]
print('Sample patterns to test: ' + str(sample_patterns))

# We'll use these patterns to search for citing patents
result = {
    'uc_patents_count': len(uc_patents_map),
    'sample_cpc': uc_patents_map.get('US-2022074631-A1', [])[:5],
    'cpc_titles_sample': {
        'F28D15/00': cpc_title_map.get('F28D15/00', 'Not found')[:50],
        'F25B21/00': cpc_title_map.get('F25B21/00', 'Not found')[:50]
    },
    'patterns': sample_patterns
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': [{'total': '169'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:22': {'status': 'success', 'count': 87}, 'var_functions.execute_python:24': 'file_storage/functions.execute_python:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:32': {'uc_patents_count': 87, 'uc_pub_numbers_count': 26, 'uc_pub_numbers': ['WO-2021102420-A1', 'US-11546022-B2', 'US-6767662-B2', 'US-6750960-B2', 'US-2006292670-A1', 'WO-2018026404-A3', 'AU-2019275518-B2', 'WO-2024112568-A1', 'US-2022074631-A1', 'WO-2012162563-A2', 'WO-2024044766-A3', 'WO-2023225482-A3', 'WO-2017214343-A1', 'US-2018243924-A1', 'US-2017145219-A1', 'US-11376346-B2', 'US-2017281687-A1', 'EP-0826155-A4', 'US-2006051790-A1', 'AU-2010214112-B2', 'EP-1212462-A1', 'US-9061071-B2', 'WO-2010045542-A3', 'US-11667770-B2', 'AU-2015364602-B2', 'US-2019328740-A1'], 'uc_cpc_sample': {'US-2022074631-A1': ['Y02B30/00', 'F25B2321/001', 'F25B21/00', 'F28D15/00', 'F25B21/00', 'F25B2321/001', 'F25B2321/001', 'F28D15/00', 'F25B21/00'], 'AU-2019275518-B2': ['A61K31/357', 'A61K31/34', 'A61K31/08', 'A61D7/04', 'A61K31/025', 'A61K31/357', 'A61P43/00', 'A61P25/20', 'A61K31/045', 'A61K31/02', 'A61P23/00', 'A61K9/007', 'A61K31/341', 'A61M16/01', 'A61D7/04', 'A61K31/351', 'A61K31/351', 'A61K31/34', 'A61K31/08', 'A61K31/025', 'A61P43/00', 'A61K31/02', 'A61K31/045', 'A61P11/00', 'A61K31/357', 'A61P23/00', 'A61P25/20', 'A61M16/01', 'A61K31/357', 'A61P11/00', 'A61K9/007', 'A61K31/025', 'A61K31/015', 'A61K31/341', 'A61K31/025', 'A61K31/045', 'A61K31/341', 'A61K31/351', 'A61K31/357', 'A61K31/08', 'A61K9/007', 'A61P23/00', 'A61K31/34', 'A61K31/015'], 'US-2017281687-A1': ['A61K31/52', 'A61K2035/124', 'A61K31/522', 'A61K35/28', 'A61K35/28', 'A61K31/522', 'C12N2510/00', 'A61K2035/124', 'A61K31/52', 'A61K2035/124', 'A61K35/28']}}, 'var_functions.query_db:34': [{'count': '277644'}], 'var_functions.execute_python:36': {'uc_patents_count': 26, 'sample': {'US-2022074631-A1': ['Y02B30/00', 'F25B2321/001', 'F25B21/00'], 'AU-2019275518-B2': ['A61K31/357', 'A61K31/34', 'A61K31/08'], 'US-2017281687-A1': ['A61K31/52', 'A61K2035/124', 'A61K31/522']}}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': [], 'var_functions.execute_python:42': {'uc_patents_total': 169, 'uc_pub_numbers': 43, 'sample_uc_cpc': {'US-2022074631-A1': ['F28D15/00', 'Y02B30/00', 'F25B2321/001'], 'AU-2019275518-B2': ['A61K31/045', 'A61M16/01', 'A61K9/007'], 'US-2017281687-A1': ['A61K2035/124', 'A61K35/28', 'A61K31/522']}}, 'var_functions.query_db:44': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'}, {'Patents_info': 'MEAD JOHNSON NUTRITION CO holds the US patent application (no. US-201916377667-A), with publication number US-10933114-B2.'}, {'Patents_info': 'WATERS TECHNOLOGIES CORP holds the US application (no. US-201916384272-A), with pub. number US-11169125-B2.'}, {'Patents_info': 'The US patent application (no. US-201916389545-A) is assigned to MODERNATX INC and has pub. number US-10695419-B2.'}, {'Patents_info': 'Patent application (ID US-201916393628-A) from US, owned by YOBS TECH INC, with publication no. US-10950222-B2.'}, {'Patents_info': 'The US patent filing (application number US-201916395813-A) is owned by HONDA MOTOR CO LTD and has publication number US-11168653-B2.'}], 'var_functions.execute_python:45': {'uc_pub_count': 43, 'sample_pattern': "'%CA-2298540-A1%' OR citation LIKE '%US-9061071-B2%' OR citation LIKE '%WO-2012162563-A2%' OR citati"}, 'var_functions.execute_python:48': {'uc_patents_count': 43, 'query_conditions': 43, 'query_preview': "SELECT Patents_info, citation FROM publicationinfo WHERE citation LIKE '%US-2022074631-A1%' OR citation LIKE '%AU-2019275518-B2%' OR citation LIKE '%US-2017281687-A1%' OR citation LIKE '%US-9061071-B2"}, 'var_functions.query_db:50': [], 'var_functions.execute_python:52': {'uc_patents_count': 43, 'uc_pub_numbers': ['US-11376346-B2', 'WO-2024044766-A3', 'US-2023279470-A1', 'US-2023155090-A1', 'AU-2008349842-A1', 'US-6767662-B2', 'AU-2019275518-B2', 'CA-2298540-A1', 'US-2020025859-A1', 'US-2018243924-A1']}, 'var_functions.execute_python:54': {'patterns': ['US-2022074631-A1', 'AU-2019275518-B2', 'US-2017281687-A1', 'US-9061071-B2', 'EP-0826155-A4', 'WO-2021102420-A1', 'WO-2012162563-A2', 'US-11376346-B2', 'US-2017145219-A1', 'CA-2298540-A1'], 'count': 43}, 'var_functions.execute_python:56': {'uc_patents_count': 43, 'sample_uc_cpc': {'US-2022074631-A1': ['F25B21/00', 'Y02B30/00', 'F28D15/00'], 'AU-2019275518-B2': ['A61P23/00', 'A61K31/015', 'A61K31/08'], 'US-2017281687-A1': ['A61K31/52', 'C12N2510/00', 'A61K2035/124']}, 'uc_pub_numbers_sample': ['US-2022074631-A1', 'AU-2019275518-B2', 'US-2017281687-A1', 'US-9061071-B2', 'EP-0826155-A4', 'WO-2021102420-A1', 'WO-2012162563-A2', 'US-11376346-B2', 'US-2017145219-A1', 'CA-2298540-A1']}, 'var_functions.execute_python:58': {'cpc_definitions_count': 260808, 'cpc_title_map_size': 260808, 'sample_titles': {'A01K2227/108': 'Swine', 'A01K2227/105': 'Murine', 'A01K2227/101': 'Bovine'}}, 'var_functions.execute_python:60': {'status': 'ready_to_query', 'uc_patents_count': 43, 'uc_pub_numbers': ['US-2022074631-A1', 'AU-2019275518-B2', 'US-2017281687-A1', 'US-9061071-B2', 'EP-0826155-A4', 'WO-2021102420-A1', 'WO-2012162563-A2', 'US-11376346-B2', 'US-2017145219-A1', 'CA-2298540-A1', 'US-2021000566-A1', 'US-2006051790-A1', 'US-2023171142-A1', 'WO-2018026404-A3', 'US-2006292670-A1', 'US-2021101879-A1', 'US-2023321419-A1', 'AU-2003297741-A1', 'WO-2017214343-A1', 'US-11667770-B2', 'US-6750960-B2', 'US-2020025859-A1', 'EP-1212462-A1', 'US-2023279470-A1', 'AU-2008349842-A1', 'EP-4284234-A1', 'WO-2020055916-A9', 'US-6767662-B2', 'AU-2015364602-B2', 'IL-244029-A0', 'AU-2010214112-B2', 'US-2019328740-A1', 'US-2022018060-A1', 'WO-2023225482-A3', 'WO-2024044766-A3', 'AU-2007297661-A1', 'WO-2024112568-A1', 'CA-2550552-A1', 'US-11546022-B2', 'US-2023155090-A1', 'WO-2010045542-A3', 'HK-1250569-A1', 'US-2018243924-A1']}, 'var_functions.execute_python:64': {'uc_patents': 43, 'cpc_defs': 260808, 'sample_codes': {'US-2022074631-A1': ['F28D15/00', 'F25B21/00'], 'AU-2019275518-B2': ['A61P23/00', 'A61K31/02'], 'US-2017281687-A1': ['A61K2035/124', 'C12N2510/00']}}, 'var_functions.execute_python:68': {'loaded': True, 'sample_size': 1}, 'var_functions.execute_python:70': {'uc_patents_count': 43, 'sample_uc_cpc': {'US-2022074631-A1': ['F28D15/00', 'F25B2321/001', 'F25B21/00'], 'AU-2019275518-B2': ['A61K31/351', 'A61K31/341', 'A61K31/34']}, 'cpc_titles_sample': {'F25B21/00': 'Machines, plants or systems, using electric or magnetic effe', 'A61K31/357': 'Heterocyclic compounds having oxygen as the only ring hetero'}}}

exec(code, env_args)
