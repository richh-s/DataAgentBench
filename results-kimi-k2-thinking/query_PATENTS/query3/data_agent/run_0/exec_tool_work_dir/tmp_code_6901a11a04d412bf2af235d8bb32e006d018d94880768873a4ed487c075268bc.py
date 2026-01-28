code = """import json

# Load the assignee CPC codes
result_file = locals()['var_functions.execute_python:30']
with open(result_file, 'r') as f:
    results = json.load(f)

assignee_cpc_codes = results.get('assignee_cpc_codes', {})

# Load CPC definitions
cpc_def_file = locals()['var_functions.query_db:38']
with open(cpc_def_file, 'r') as f:
    cpc_defs = json.load(f)

# Create CPC code to title mapping
cpc_title_map = {}
for row in cpc_defs:
    symbol = row.get('symbol', '')
    title = row.get('titleFull', '')
    if symbol and title:
        cpc_title_map[symbol] = title

# Sample the data
sample_assignee = list(assignee_cpc_codes.keys())[0]
sample_cpc = assignee_cpc_codes[sample_assignee][:3]

print('__RESULT__:')
print(json.dumps({
    'total_assignees': len(assignee_cpc_codes),
    'sample_assignee': sample_assignee,
    'sample_cpc_codes': sample_cpc,
    'sample_cpc_titles': [cpc_title_map.get(code, 'Title not found') for code in sample_cpc][:3]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'total_records': 169, 'total_citations': 1308, 'sample': [{'publication_number': 'US-4599677-A', 'source_patent': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'publication_number': 'US-2015129765-A1', 'source_patent': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'publication_number': 'FR-3105380-A1', 'source_patent': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'publication_number': 'US-11466906-B2', 'source_patent': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'publication_number': 'US-2001053519-A1', 'source_patent': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}]}, 'var_functions.execute_python:10': {'total_cited_publications': 1112, 'sample_pubs': ['WO-2013025632-A1', 'US-2020023209-A1', 'US-6200265-B1', 'EP-2694154-A1', 'US-9974593-B2', 'US-5366770-A', 'US-8865406-B2', 'US-2006105322-A1', 'US-7757565-B2', 'US-2014356956-A1', 'JP-H11261169-A', 'US-2016242650-A1', 'US-2014356867-A1', 'WO-2014093712-A1', 'US-8080523-B2', 'WO-2013169802-A1', 'WO-2010144578-A2', 'EP-2515996-A2', 'US-2011281288-A1', 'US-2012065087-A1']}, 'var_functions.execute_python:12': {'message': 'Created cited_pubs.json with all cited publication numbers', 'count': 1112}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'total_patents': 277813, 'total_uc_cited_pubs': 1112, 'sample_uc_cited': ['US-2014170753-A1', 'US-2003222263-A1', 'FR-1447611-A', 'US-5710621-A', 'US-5019504-A', 'US-5125736-A', 'US-4911920-A', 'US-6303344-B1', 'US-9057109-B2', 'US-5532071-A']}, 'var_functions.execute_python:24': {'total_patents_loaded': 277813, 'total_uc_cited_pubs': 1112, 'sample_uc_cited': ['US-2016000590-A1', 'WO-9213961-A1', 'US-9587252-B2', 'EP-2764103-A2', 'US-6461870-B2', 'US-2005238577-A1', 'US-6492160-B1', 'EP-2928557-A2', 'US-2015291961-A1', 'US-8618096-B2']}, 'var_functions.execute_python:26': {'uc_cited_pubs_count': 1112, 'sample_cited': ['US-2005147558-A1', 'US-2011300538-A1', 'US-2013062527-A1', 'US-2012316076-A1', 'US-7135709-B1', 'US-2015240261-A1', 'US-6492160-B1', 'WO-2014039872-A1', 'US-5895223-A', 'WO-2008016345-A2']}, 'var_functions.execute_python:28': {'total_patents_to_search': 277813, 'total_uc_cited_pubs': 1112}, 'var_functions.execute_python:30': 'file_storage/functions.execute_python:30.json', 'var_functions.list_db:32': ['cpc_definition'], 'var_functions.execute_python:34': {'total_assignees_with_cpc': 55, 'total_unique_cpc_codes': 662, 'sample_assignees': ['BIONIME CORP', 'LG INNOTEK CO LTD', 'CIBUS US LLC', 'ASCENSIA DIABETES CARE HOLDINGS AG', 'SLT TECH INC'], 'sample_cpc_codes': ['A61P31/12', 'C12N5/04', 'C12N15/102', 'C08G2261/1424', 'C07K14/51', 'B01J2219/00599', 'G01N2035/1048', 'G01N21/6456', 'Y10S438/977', 'C12N9/2408']}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)
