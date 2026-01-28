code = """import json
import re

# Load UC publication numbers from earlier analysis (using key from execute_python result)
uc_cpc_data = locals()['var_functions.query_db:46']
uc_pub_numbers = set(uc_cpc_data['uc_publication_numbers'])

# Load sample patent data to find citations
data_file = locals()['var_functions.query_db:48']
with open(data_file, 'r') as f:
    patents_data = json.load(f)

# Find patents that cite UC patents and get their assignees
citing_assignees_map = {}  # assignee -> set of UC patents they cite
uc_citation_map = {}  # cited_uc_patent -> list of citing assignees

for record in patents_data:
    patents_info = record.get('Patents_info', '')
    citation_data = record.get('citation', '')
    
    if citation_data:
        try:
            citations = json.loads(citation_data)
            # Check if any citation is a UC patent
            for citation in citations:
                pub_num = citation.get('publication_number', '')
                if pub_num in uc_pub_numbers:
                    # This patent cites a UC patent - extract assignee
                    assignee_match = re.search(r'^([A-Z][^,]+?) holds|^([A-Z][^,]+?) is|^In [A-Z]{2}, the (?:application|patent filing) [^,]+ (?:is assigned to|owned by|belongs to) ([A-Z][^,\.]+)', patents_info)
                    
                    if assignee_match:
                        # Get the first matching group
                        assignee = next((g for g in assignee_match.groups() if g), '').strip()
                        
                        # Skip UNIV CALIFORNIA
                        if assignee and 'UNIV CALIFORNIA' not in assignee.upper() and 'UNIVERSITY OF CALIFORNIA' not in assignee.upper():
                            # Add to assignee map
                            if assignee not in citing_assignees_map:
                                citing_assignees_map[assignee] = set()
                            citing_assignees_map[assignee].add(pub_num)
                            
                            # Add to UC citation map
                            if pub_num not in uc_citation_map:
                                uc_citation_map[pub_num] = []
                            uc_citation_map[pub_num].append(assignee)
        except:
            pass

# Count citations per assignee
assignee_citation_counts = {assignee: len(pats) for assignee, pats in citing_assignees_map.items()}

result = {
    'total_citations_found': sum(len(v) for v in uc_citation_map.values()),
    'unique_citing_assignees': len(citing_assignees_map),
    'top_citing_assignees': dict(sorted(assignee_citation_counts.items(), key=lambda x: x[1], reverse=True)[:20]),
    'uc_citation_map_sample': {k: uc_citation_map[k][:5] for k in list(uc_citation_map.keys())[:3]}
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:12': {'status': 'no_valid_data', 'summary': {}}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:18': [{'symbol': 'A01K2227/108', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'titleFull': 'Ovine'}], 'var_functions.query_db:24': [{'cid': '0', 'name': 'Patents_info', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'kind_code', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'application_kind', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'pct_number', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '4', 'name': 'family_id', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '5', 'name': 'title_localized', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '6', 'name': 'abstract_localized', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '7', 'name': 'claims_localized_html', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '8', 'name': 'description_localized_html', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '9', 'name': 'publication_date', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '10', 'name': 'filing_date', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '11', 'name': 'grant_date', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '12', 'name': 'priority_date', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '13', 'name': 'priority_claim', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '14', 'name': 'inventor_harmonized', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '15', 'name': 'examiner', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '16', 'name': 'uspc', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '17', 'name': 'ipc', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '18', 'name': 'cpc', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '19', 'name': 'citation', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '20', 'name': 'parent', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '21', 'name': 'child', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '22', 'name': 'entity_status', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '23', 'name': 'art_unit', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:32': {'type': "<class 'str'>", 'is_list': True, 'record_count': 169}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:37': 'file_storage/functions.query_db:37.json', 'var_functions.execute_python:38': {'total_uc_patents': 169, 'uc_publication_numbers': ['US-6750960-B2', 'US-11667770-B2', 'US-10744347-B2', 'US-11607427-B2', 'EP-4284234-A1', 'US-2020283856-A1', 'US-10900049-B2', 'US-2017087258-A1', 'AU-2007297661-A1', 'US-11014955-B2', 'WO-2024050335-A2', 'WO-2018152537-A1', 'AU-2001296493-B2', 'US-7052856-B2', 'US-6767662-B2', 'WO-2024044766-A3', 'WO-2020096950-A1', 'CA-3161617-A1', 'US-2023171142-A1', 'US-2021282642-A1'], 'total_unique_pub_numbers': 124}, 'var_functions.execute_python:37': {'uc_patents_count': 169, 'uc_pub_numbers_count': 124, 'sample_uc_pub_numbers': ['WO-2023225482-A3', 'WO-2019173834-A1', 'AU-2002254753-B2', 'US-2017087258-A1', 'WO-2021102420-A1', 'US-11667770-B2', 'PE-20130764-A1', 'WO-2024050335-A2', 'US-11960018-B2', 'WO-2012158833-A3']}, 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.execute_python:43': {'uc_patents_found': 10, 'uc_publication_numbers': 8, 'sample_mapping': {'US-2022074631-A1': ['F25B21/00', 'F28D15/00'], 'US-11421276-B2': ['C12Q1/6883'], 'AU-2019275518-B2': ['A61K9/007', 'A61K31/357', 'A61K31/08', 'A61K31/34', 'A61M16/01', 'A61P23/00', 'A61K31/351', 'A61P11/00', 'A61P43/00', 'A61D7/04', 'A61K31/015', 'A61K31/341', 'A61P25/20', 'A61K31/045', 'A61K31/02', 'A61K31/025']}}, 'var_functions.execute_python:46': {'uc_publication_numbers': ['AU-2019275518-B2', 'AU-2017356943-A1', 'US-2022074631-A1', 'AU-2003247814-A1', 'US-11421276-B2', 'US-2017194630-A1', 'US-2017281687-A1', 'EP-1224461-B1'], 'uc_cpc_map': {'US-2022074631-A1': ['F25B21/00', 'F28D15/00'], 'US-11421276-B2': ['C12Q1/6883'], 'AU-2019275518-B2': ['A61K31/341', 'A61K9/007', 'A61K31/34', 'A61K31/015', 'A61K31/02', 'A61P25/20', 'A61K31/045', 'A61K31/08', 'A61D7/04', 'A61K31/351', 'A61K31/357', 'A61K31/025', 'A61P43/00', 'A61M16/01', 'A61P11/00', 'A61P23/00'], 'US-2017194630-A1': ['H01M4/0469', 'H01M4/0483', 'H01M4/625', 'H01M4/0471', 'H01M4/382', 'H01M4/134', 'H01M4/0492', 'H01M4/386', 'H01M10/0525', 'H01M4/74', 'H01M4/366', 'H01M10/0569', 'H01M4/1395'], 'US-2017281687-A1': ['A61K31/52', 'A61K35/28', 'A61K31/522'], 'EP-1224461-B1': ['A61K41/0057', 'A61K51/1018', 'A61P9/10', 'G01N33/92', 'A61K49/227', 'C07K16/18'], 'AU-2003247814-A1': ['A61H9/005'], 'AU-2017356943-A1': ['C07C253/30', 'C07C255/34', 'C07C253/34', 'C07B59/001']}, 'total_uc_pubs': 8}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json'}

exec(code, env_args)
