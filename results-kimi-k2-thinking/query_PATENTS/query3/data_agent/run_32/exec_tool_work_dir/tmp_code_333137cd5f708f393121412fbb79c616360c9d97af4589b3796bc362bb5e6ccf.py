code = """import json
import re

# Load UC patents data
uc_file = locals()['var_functions.query_db:60']
with open(uc_file, 'r') as f:
    uc_patents = json.load(f)

# Build comprehensive mapping of UC publication numbers to CPC subclasses
uc_pub_to_cpc_map = {}
uc_pub_numbers = set()

for record in uc_patents[:100]:  # Process first 100 for practical purposes
    patents_info = record.get('Patents_info', '')
    cpc_data = record.get('cpc', '')
    
    # Extract publication numbers
    pub_matches = re.findall(r'([A-Z]{2}-\d+-[A-Z]\d+)', patents_info)
    if pub_matches:
        for pub_num in pub_matches:
            uc_pub_numbers.add(pub_num)
            
            # Extract primary CPC codes for this patent
            primary_cpcs = []
            if cpc_data:
                try:
                    cpc_list = json.loads(cpc_data)
                    for cpc_item in cpc_list:
                        if cpc_item.get('inventive') or cpc_item.get('first'):
                            code = cpc_item.get('code')
                            if code:
                                primary_cpcs.append(code)
                except:
                    pass
            
            if pub_num not in uc_pub_to_cpc_map:
                uc_pub_to_cpc_map[pub_num] = set()
            uc_pub_to_cpc_map[pub_num].update(primary_cpcs)

# Based on the data pattern, let's identify the top UC patents and their CPCs
uc_patent_summary = []
for pub_num, cpc_set in list(uc_pub_to_cpc_map.items())[:20]:
    uc_patent_summary.append({
        'publication_number': pub_num,
        'primary_cpc_subclasses': list(cpc_set)[:10]  # Limit to top 10 per patent
    })

result_info = {
    'total_uc_patents_analyzed': len(uc_pub_to_cpc_map),
    'uc_patents_with_cpc': uc_patent_summary,
    'total_unique_cpc_codes': sum(len(cpc_set) for cpc_set in uc_pub_to_cpc_map.values()),
    'methodology': 'Analysis of UNIV CALIFORNIA patents and their primary CPC classifications'
}

print('__RESULT__:')
print(json.dumps(result_info))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:12': {'status': 'no_valid_data', 'summary': {}}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:18': [{'symbol': 'A01K2227/108', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'titleFull': 'Ovine'}], 'var_functions.query_db:24': [{'cid': '0', 'name': 'Patents_info', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'kind_code', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'application_kind', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'pct_number', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '4', 'name': 'family_id', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '5', 'name': 'title_localized', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '6', 'name': 'abstract_localized', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '7', 'name': 'claims_localized_html', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '8', 'name': 'description_localized_html', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '9', 'name': 'publication_date', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '10', 'name': 'filing_date', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '11', 'name': 'grant_date', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '12', 'name': 'priority_date', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '13', 'name': 'priority_claim', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '14', 'name': 'inventor_harmonized', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '15', 'name': 'examiner', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '16', 'name': 'uspc', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '17', 'name': 'ipc', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '18', 'name': 'cpc', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '19', 'name': 'citation', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '20', 'name': 'parent', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '21', 'name': 'child', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '22', 'name': 'entity_status', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '23', 'name': 'art_unit', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:32': {'type': "<class 'str'>", 'is_list': True, 'record_count': 169}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:37': 'file_storage/functions.query_db:37.json', 'var_functions.execute_python:38': {'total_uc_patents': 169, 'uc_publication_numbers': ['US-6750960-B2', 'US-11667770-B2', 'US-10744347-B2', 'US-11607427-B2', 'EP-4284234-A1', 'US-2020283856-A1', 'US-10900049-B2', 'US-2017087258-A1', 'AU-2007297661-A1', 'US-11014955-B2', 'WO-2024050335-A2', 'WO-2018152537-A1', 'AU-2001296493-B2', 'US-7052856-B2', 'US-6767662-B2', 'WO-2024044766-A3', 'WO-2020096950-A1', 'CA-3161617-A1', 'US-2023171142-A1', 'US-2021282642-A1'], 'total_unique_pub_numbers': 124}, 'var_functions.execute_python:37': {'uc_patents_count': 169, 'uc_pub_numbers_count': 124, 'sample_uc_pub_numbers': ['WO-2023225482-A3', 'WO-2019173834-A1', 'AU-2002254753-B2', 'US-2017087258-A1', 'WO-2021102420-A1', 'US-11667770-B2', 'PE-20130764-A1', 'WO-2024050335-A2', 'US-11960018-B2', 'WO-2012158833-A3']}, 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.execute_python:43': {'uc_patents_found': 10, 'uc_publication_numbers': 8, 'sample_mapping': {'US-2022074631-A1': ['F25B21/00', 'F28D15/00'], 'US-11421276-B2': ['C12Q1/6883'], 'AU-2019275518-B2': ['A61K9/007', 'A61K31/357', 'A61K31/08', 'A61K31/34', 'A61M16/01', 'A61P23/00', 'A61K31/351', 'A61P11/00', 'A61P43/00', 'A61D7/04', 'A61K31/015', 'A61K31/341', 'A61P25/20', 'A61K31/045', 'A61K31/02', 'A61K31/025']}}, 'var_functions.execute_python:46': {'uc_publication_numbers': ['AU-2019275518-B2', 'AU-2017356943-A1', 'US-2022074631-A1', 'AU-2003247814-A1', 'US-11421276-B2', 'US-2017194630-A1', 'US-2017281687-A1', 'EP-1224461-B1'], 'uc_cpc_map': {'US-2022074631-A1': ['F25B21/00', 'F28D15/00'], 'US-11421276-B2': ['C12Q1/6883'], 'AU-2019275518-B2': ['A61K31/341', 'A61K9/007', 'A61K31/34', 'A61K31/015', 'A61K31/02', 'A61P25/20', 'A61K31/045', 'A61K31/08', 'A61D7/04', 'A61K31/351', 'A61K31/357', 'A61K31/025', 'A61P43/00', 'A61M16/01', 'A61P11/00', 'A61P23/00'], 'US-2017194630-A1': ['H01M4/0469', 'H01M4/0483', 'H01M4/625', 'H01M4/0471', 'H01M4/382', 'H01M4/134', 'H01M4/0492', 'H01M4/386', 'H01M10/0525', 'H01M4/74', 'H01M4/366', 'H01M10/0569', 'H01M4/1395'], 'US-2017281687-A1': ['A61K31/52', 'A61K35/28', 'A61K31/522'], 'EP-1224461-B1': ['A61K41/0057', 'A61K51/1018', 'A61P9/10', 'G01N33/92', 'A61K49/227', 'C07K16/18'], 'AU-2003247814-A1': ['A61H9/005'], 'AU-2017356943-A1': ['C07C253/30', 'C07C255/34', 'C07C253/34', 'C07B59/001']}, 'total_uc_pubs': 8}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:54': {'uc_patents_sample': ['AU-2019275518-B2', 'US-2017194630-A1', 'US-11421276-B2', 'US-2017281687-A1', 'AU-2003247814-A1', 'EP-1224461-B1', 'AU-2017356943-A1', 'US-2022074631-A1'], 'citations_found': 0, 'uc_cited_sample': [], 'top_assignees': {}}, 'var_functions.query_db:56': 'file_storage/functions.query_db:56.json', 'var_functions.query_db:58': [], 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:62': [], 'var_functions.execute_python:64': {'uc_patents_processed': 40, 'sample_uc_patents': ['HK-1052178-A1', 'WO-2023239670-A1', 'US-2018080022-A1', 'WO-2017214343-A1', 'US-10765865-B2', 'EP-3668487-A4', 'US-2018243924-A1', 'US-2020025859-A1', 'US-11014955-B2', 'AU-2003297741-A1'], 'sample_cpc_mapping': {'HK-1052178-A1': ['A01N43/50', 'C08F26/06', 'C08L51/003', 'C07D235/02', 'C08F289/00', 'C09J151/04', 'C08L51/08', 'C08L51/04', 'C08F291/00', 'A01N59/00', 'C08F265/04', 'C09J151/003', 'C08F271/02', 'C09J151/02', 'C08L51/02', 'C07D233/74', 'C07D251/34', 'C08F253/00', 'C09J151/08', 'A61K31/77', 'C08F8/30', 'C08F251/02'], 'WO-2023239670-A1': ['A61N7/00', 'A61N1/3606', 'A61N1/36071', 'A61N1/36021'], 'US-2018080022-A1': ['A61K31/70', 'C07H21/02', 'C12N15/1132', 'C12N15/113', 'C12Q1/08', 'C12N15/111', 'C07H21/04'], 'WO-2017214343-A1': ['A61K47/52', 'A61K47/6943', 'A61K31/606', 'A61K47/18', 'A61P1/00'], 'US-10765865-B2': ['A61B6/4258', 'A61N1/37205', 'A61B5/389', 'A61B5/279', 'G01N27/327', 'A61B8/4483', 'A61B5/296', 'A61B5/076', 'A61B8/085', 'A61N1/36135', 'A61B5/686', 'A61B8/48', 'A61N1/3787', 'A61N7/02', 'A61N1/372', 'A61B8/0875', 'B06B1/06', 'A61B8/0808', 'A61B5/0031', 'A61N1/0534', 'A61N1/3605']}}}

exec(code, env_args)
