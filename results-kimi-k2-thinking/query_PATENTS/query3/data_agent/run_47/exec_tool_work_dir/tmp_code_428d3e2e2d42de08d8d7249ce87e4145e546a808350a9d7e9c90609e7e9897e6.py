code = """import json
import re
from collections import defaultdict

# Load California patents and create comprehensive mapping
california_path = locals()['var_functions.query_db:14']
with open(california_path, 'r') as f:
    california_patents = json.load(f)

# Build mapping: CA publication number -> primary CPC codes
ca_pub_to_cpcs = {}
ca_pub_set = set()

for patent in california_patents:
    # Extract publication number
    pub_num = None
    patents_info = patent['Patents_info']
    
    # Try multiple patterns
    patterns = [
        r'pub\. number\s+([A-Z]{2}-[A-Z0-9-]+)',
        r'publication number\s+([A-Z]{2}-[A-Z0-9-]+)',
        r'([A-Z]{2}-[A-Z0-9-]+)[\.,\s]*$'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, patents_info, re.IGNORECASE)
        if match:
            pub_num = match.group(1)
            break
    
    if not pub_num:
        # Fallback: extract application ID pattern
        app_match = re.search(r'([A-Z]{2}-\d{6,}-[A-Z])', patents_info)
        if app_match:
            pub_num = app_match.group(1)
    
    if pub_num:
        # Get primary CPC codes
        primary_cpcs = []
        if patent.get('cpc'):
            try:
                cpc_data = json.loads(patent['cpc']) if isinstance(patent['cpc'], str) else patent['cpc']
                for entry in cpc_data:
                    if isinstance(entry, dict) and entry.get('inventive') and entry.get('first'):
                        code = entry.get('code')
                        if code and '/' in code:
                            primary_cpcs.append(code)
            except:
                pass
        
        ca_pub_to_cpcs[pub_num] = list(set(primary_cpcs)) if primary_cpcs else []
        ca_pub_set.add(pub_num)

# Load a larger sample of patents to find citations
# Let's process all available citation data in chunks
citations_path = locals()['var_functions.query_db:44']
with open(citations_path, 'r') as f:
    patents_with_citations = json.load(f)

# Search for patents that cite California patents
university_pattern = re.compile(r'UNIV CALIFORNIA|UNIVERSITY OF CALIFORNIA', re.IGNORECASE)
citing_assignees_info = defaultdict(lambda: {'cited_pubs': set(), 'cpc_codes': set()})

patents_checked = 0
for patent in patents_with_citations:
    patents_checked += 1
    
    # Skip UNIV CALIFORNIA patents
    if university_pattern.search(patent['Patents_info']):
        continue
    
    # Parse citations
    citations = []
    if patent.get('citation'):
        try:
            citations = json.loads(patent['citation']) if isinstance(patent['citation'], str) else patent['citation']
        except:
            citations = []
    
    # Check if any citation is a CA patent
    for citation in citations:
        if isinstance(citation, dict) and citation.get('publication_number'):
            cited_pub = citation['publication_number']
            if cited_pub in ca_pub_set:
                # Found a citation to CA patent!
                # Extract assignee
                assignee = None
                patent_info = patent['Patents_info']
                
                assignee_patterns = [
                    r'^(\w[^,\.]+?)(?:\s+(?:holds|hold the|is assigned|is owned|belongs to|from US,? owned|from US,? held))',
                    r'(?:assigned to|owned by|belongs to|held by|from US,? owned by|from US,? held by)\s+(\w[^,\.]+?)(?:\s+and has|\s+with pub|\s+,|\s+has|$)',
                ]
                
                for pattern in assignee_patterns:
                    match = re.search(pattern, patent_info, re.IGNORECASE)
                    if match:
                        candidate = match.group(1).strip()
                        if not university_pattern.search(candidate):
                            assignee = candidate
                            break
                
                if assignee and assignee != patent_info:
                    citing_assignees_info[assignee]['cited_pubs'].add(cited_pub)
                    # Add CPC codes from the cited CA patent
                    if cited_pub in ca_pub_to_cpcs and ca_pub_to_cpcs[cited_pub]:
                        citing_assignees_info[assignee]['cpc_codes'].update(ca_pub_to_cpcs[cited_pub])

print('__RESULT__:')
print(json.dumps({
    'patents_checked': patents_checked,
    'ca_publications': len(ca_pub_set),
    'citing_assignees_found': len(citing_assignees_info),
    'sample_assignees': list(citing_assignees_info.keys())[:10] if citing_assignees_info else [],
    'ca_cpc_mappings_count': len(ca_pub_to_cpcs),
    'ready_for_cpc_lookup': len(citing_assignees_info) > 0
}, indent=2, default=str))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:18': {'total_california_patents': 169, 'sample_citations': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4599677-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n   ', 'sample_cpc': '[\n  {\n    "code": "Y02B30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "'}, 'var_functions.query_db:20': [{'symbol': 'A01K2227/108', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'titleFull': 'Ovine'}], 'var_functions.execute_python:22': {'total_california_patents': 169, 'extracted_publication_numbers': ['US-2022074631-A1', 'TW-201925402-A', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'US-9061071-B2', 'EP-0826155-A4', 'RO-70061-A', 'WO-2021102420-A1', 'WO-2012162563-A2']}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'total_california_patents': 169, 'extracted_publication_numbers_count': 114, 'sample_pub_nums': ['US-2017145219-A1', 'WO-2018026404-A3', 'US-11421276-B2', 'US-2019169580-A1', 'CN-101584047-A', 'US-2019328740-A1', 'CA-2283629-C', 'AU-2007297661-A1', 'US-2023279470-A1', 'WO-2023212447-A2']}, 'var_functions.query_db:28': [], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:32': {'patents_with_citations': 5, 'california_pub_nums': 114, 'sample_patent_citation': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, 'var_functions.query_db:34': [], 'var_functions.execute_python:36': {'sample_citation_full': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "JP-H01209663-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "JP-H0737617-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "WO-9744842-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "JP-H09330720-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "JP-H10294100-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "JP-H10302768-A",\n    "type": ""\n  },\n  {\n    "application_n'}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.execute_python:40': {'total_ca_patents': 169, 'unique_pub_nums': 114, 'sample_pub_nums': ['AU-2003247814-A1', 'AU-2003297741-A1', 'AU-2004253879-A1', 'AU-2005269556-A1', 'AU-2007297661-A1', 'AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2017356943-A1', 'AU-2019275518-B2', 'AU-2409401-A', 'AU-2898989-A', 'AU-3353000-A', 'AU-5938296-A', 'AU-6535890-A', 'CA-2283629-C', 'CA-2298540-A1', 'CA-2550552-A1', 'CA-2562038-C', 'CA-2718348-C']}, 'var_functions.execute_python:42': {'total_ca_patents': 169, 'total_unique_pub_nums': 114, 'sample_pub_nums': ['US-2020025859-A1', 'US-2021000566-A1', 'US-2021181673-A1', 'US-12025581-B2', 'WO-2024112568-A1', 'CA-3161617-A1', 'US-2019328740-A1', 'KR-20050085437-A', 'US-6750960-B2', 'US-11421276-B2'], 'total_to_search': 114}, 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:46': {'california_pub_nums_count': 114, 'sample_pub_nums': ['AU-2003247814-A1', 'AU-2003297741-A1', 'AU-2004253879-A1', 'AU-2005269556-A1', 'AU-2007297661-A1', 'AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2017356943-A1', 'AU-2019275518-B2'], 'message': 'Ready to search for citing patents'}, 'var_functions.execute_python:48': {'patents_with_citations_in_sample': 1000, 'citing_patents_count': 0, 'unique_citing_assignees': 0, 'sample_assignees': [], 'sample_citing_patent': 'None'}, 'var_functions.execute_python:50': {'total_citing_assignees': 0, 'total_ca_publications': 114, 'sample_assignees': [], 'sample_ca_cpc_mapping': {'US-2022074631-A1': ['F25B21/00', 'F25B21/00', 'F25B21/00'], 'TW-201925402-A': ['C09J9/02', 'C09J9/02', 'C09J9/02'], 'US-11421276-B2': ['C12Q1/6883', 'C12Q1/6883', 'C12Q1/6883'], 'AU-2019275518-B2': ['A61K31/34', 'A61K31/351', 'A61K31/351', 'A61K31/357', 'A61K31/025'], 'JP-S6163700-A': ['C07K16/34', 'C07K16/34']}}, 'var_functions.execute_python:52': {'citing_patents_found': 0, 'total_patents_searched': 500, 'sample_citing': 'No matches found', 'ca_pub_nums_count': 114}, 'var_functions.query_db:54': [{'total': '277813'}], 'var_functions.execute_python:56': {'total_ca_patents': 169, 'extracted_pub_nums': 329, 'sample_pub_nums': ['AP-2011005954-A', 'AP-3334-A', 'AU-2001257114-A1', 'AU-2001296493-A', 'AU-2001296493-B2', 'AU-2002254753-A', 'AU-2002254753-B2', 'AU-2003247814-A', 'AU-2003247814-A1', 'AU-2003297741-A', 'AU-2003297741-A1', 'AU-2004253879-A', 'AU-2004253879-A1', 'AU-2005269556-A', 'AU-2005269556-A1'], 'total_database_patents': 277813}, 'var_functions.execute_python:58': {'total_california_patents': 169, 'extracted_publication_numbers': 114, 'patents_with_primary_cpc': 114, 'sample_mappings': {'US-2022074631-A1': ['F25B21/00'], 'TW-201925402-A': ['C09J9/02'], 'US-11421276-B2': ['C12Q1/6883'], 'AU-2019275518-B2': ['A61K31/351', 'A61K31/357', 'A61K31/025', 'A61K31/34'], 'JP-S6163700-A': ['C07K16/34'], 'US-2017281687-A1': ['A61K35/28'], 'AU-2003247814-A1': ['A61H9/005'], 'AU-2017356943-A1': ['C07C253/30'], 'US-6237292-B1': ['E04H9/021'], 'US-7745569-B2': ['C07K14/4711']}}, 'var_functions.execute_python:60': {'total_ca_pubs': 169, 'sample_like_query': "citation LIKE '%IL-23672515-A%' OR citation LIKE '%US-202016883515-A%' OR citation LIKE '%TW-107142982-A%' OR citation LIKE '%CA-3225295-A%' OR citation LIKE '%US-2023067015-W%'", 'ca_cpc_mappings_count': 169, 'sample_cpc_mappings': {'US-202117472182-A': ['F25B21/00'], 'TW-107142982-A': ['C09J9/02'], 'US-201916454755-A': ['C12Q1/6883'], 'AU-2019275518-A': ['A61K31/351', 'A61K31/34', 'A61K31/357', 'A61K31/025'], 'US-201515313510-A': ['H01M4/134']}}, 'var_functions.execute_python:62': {'total_ca_patents': 169, 'unique_publication_numbers': 169, 'patents_with_cpc_data': 169, 'sample_ca_publications': ['AP-2011005954-A', 'AU-2001296493-A', 'AU-2002254753-A', 'AU-2003247814-A1', 'AU-2003297741-A1', 'AU-2004253879-A1', 'AU-2005269556-A1', 'AU-2007297661-A1', 'AU-2008329628-A', 'AU-2008349842-A1'], 'sample_cpc_mappings': {'US-2022074631-A1': ['F25B21/00'], 'TW-201925402-A': ['C09J9/02'], 'US-11421276-B2': ['C12Q1/6883'], 'AU-2019275518-B2': ['A61K31/34', 'A61K31/351', 'A61K31/025', 'A61K31/357'], 'US-201515313510-A': ['H01M4/134']}, 'search_query_preview': "citation LIKE '%EP-4284234-A1%' OR citation LIKE '%WO-2024112568-A1%' OR citation LIKE '%US-91189497..."}, 'var_functions.execute_python:64': {'ca_patents_loaded': 169, 'ca_publications_mapped': 114, 'sample_mappings': {'US-2022074631-A1': ['F25B21/00'], 'TW-201925402-A': ['C09J9/02'], 'US-11421276-B2': ['C12Q1/6883'], 'AU-2019275518-B2': ['A61K31/34', 'A61K31/351', 'A61K31/357', 'A61K31/025'], 'JP-S6163700-A': ['C07K16/34'], 'US-2017281687-A1': ['A61K35/28'], 'AU-2003247814-A1': ['A61H9/005'], 'AU-2017356943-A1': ['C07C253/30'], 'US-6237292-B1': ['E04H9/021'], 'US-7745569-B2': ['C07K14/4711']}}, 'var_functions.execute_python:66': {'ca_publications_mapped': 169, 'sample_ca_pubs': ['US-2022074631-A1', 'TW-201925402-A', 'US-11421276-B2', 'AU-2019275518-B2', 'US-2017194630-A1', 'JP-S6163700-A', 'US-2017281687-A1', 'EP-1224461-B1', 'AU-2003247814-A1', 'AU-2017356943-A1'], 'citation_sample_size': 1000, 'ready_for_citation_search': True}}

exec(code, env_args)
