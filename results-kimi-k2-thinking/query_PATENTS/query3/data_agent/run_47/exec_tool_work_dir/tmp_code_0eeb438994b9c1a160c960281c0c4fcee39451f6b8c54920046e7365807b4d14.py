code = """import json
import re
from collections import defaultdict

# Load California patents extract publication numbers and CPC codes
california_path = locals()['var_functions.query_db:14']
with open(california_path, 'r') as f:
    california_patents = json.load(f)

# Build comprehensive mapping of California publication numbers to their CPC codes
california_pub_to_cpcs = {}
all_ca_pub_nums = set()

for patent in california_patents:
    patents_info = patent['Patents_info']
    
    # Extract publication number
    pub_num = None
    patterns = [
        r'pub\. number\s+([A-Z]{2}-[A-Z0-9-]+)',
        r'publication number\s+([A-Z]{2}-[A-Z0-9-]+)',
        r'has publication number\s+([A-Z]{2}-[A-Z0-9-]+)',
        r'with publication number\s+([A-Z]{2}-[A-Z0-9-]+)',
        r'([A-Z]{2}-[A-Z0-9-]+)'  # Fallback: any pattern that looks like a publication number
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, patents_info, re.IGNORECASE)
        if matches:
            # Filter for likely publication numbers (with proper format)
            for match in matches:
                if len(match) > 10 and match.count('-') >= 2:
                    pub_num = match
                    break
        if pub_num:
            break
    
    if pub_num:
        all_ca_pub_nums.add(pub_num)
        
        # Get primary CPC codes (inventive + first = true)
        if patent.get('cpc'):
            try:
                cpc_data = json.loads(patent['cpc']) if isinstance(patent['cpc'], str) else patent['cpc']
                primary_cpcs = []
                
                for entry in cpc_data:
                    if (isinstance(entry, dict) and 
                        entry.get('inventive', False) and 
                        entry.get('first', False) and 
                        entry.get('code')):
                        primary_cpcs.append(entry['code'])
                
                if primary_cpcs:
                    california_pub_to_cpcs[pub_num] = list(set(primary_cpcs))
            except:
                pass

# Create a smaller test set for searching
sample_ca_pubs = list(all_ca_pub_nums)[:50]  # Limit to first 50 for practical search

# Create SQL patterns for searching citations
patterns_for_search = []
for pub_num in sample_ca_pubs:
    # Create patterns for different formats (with/without quotes, different spacing)
    pub_clean = pub_num.replace("'", "''")  # SQL escaping
    patterns_for_search.append(f"citation LIKE '%{pub_clean}%'")

# Build test queries (we'll use these to search)
test_query = " OR ".join(patterns_for_search[:10])  # Use first 10 patterns

print('__RESULT__:')
print(json.dumps({
    'total_ca_patents': len(california_patents),
    'unique_publication_numbers': len(all_ca_pub_nums),
    'patents_with_cpc_data': len(california_pub_to_cpcs),
    'sample_ca_publications': sorted(list(all_ca_pub_nums))[:10],
    'sample_cpc_mappings': {k: v for k, v in list(california_pub_to_cpcs.items())[:5]},
    'search_query_preview': test_query[:100] + "..." if len(test_query) > 100 else test_query
}, indent=2, default=str))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:18': {'total_california_patents': 169, 'sample_citations': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4599677-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n   ', 'sample_cpc': '[\n  {\n    "code": "Y02B30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "'}, 'var_functions.query_db:20': [{'symbol': 'A01K2227/108', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'titleFull': 'Ovine'}], 'var_functions.execute_python:22': {'total_california_patents': 169, 'extracted_publication_numbers': ['US-2022074631-A1', 'TW-201925402-A', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'US-9061071-B2', 'EP-0826155-A4', 'RO-70061-A', 'WO-2021102420-A1', 'WO-2012162563-A2']}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'total_california_patents': 169, 'extracted_publication_numbers_count': 114, 'sample_pub_nums': ['US-2017145219-A1', 'WO-2018026404-A3', 'US-11421276-B2', 'US-2019169580-A1', 'CN-101584047-A', 'US-2019328740-A1', 'CA-2283629-C', 'AU-2007297661-A1', 'US-2023279470-A1', 'WO-2023212447-A2']}, 'var_functions.query_db:28': [], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:32': {'patents_with_citations': 5, 'california_pub_nums': 114, 'sample_patent_citation': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, 'var_functions.query_db:34': [], 'var_functions.execute_python:36': {'sample_citation_full': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "JP-H01209663-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "JP-H0737617-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "WO-9744842-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "JP-H09330720-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "JP-H10294100-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "JP-H10302768-A",\n    "type": ""\n  },\n  {\n    "application_n'}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.execute_python:40': {'total_ca_patents': 169, 'unique_pub_nums': 114, 'sample_pub_nums': ['AU-2003247814-A1', 'AU-2003297741-A1', 'AU-2004253879-A1', 'AU-2005269556-A1', 'AU-2007297661-A1', 'AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2017356943-A1', 'AU-2019275518-B2', 'AU-2409401-A', 'AU-2898989-A', 'AU-3353000-A', 'AU-5938296-A', 'AU-6535890-A', 'CA-2283629-C', 'CA-2298540-A1', 'CA-2550552-A1', 'CA-2562038-C', 'CA-2718348-C']}, 'var_functions.execute_python:42': {'total_ca_patents': 169, 'total_unique_pub_nums': 114, 'sample_pub_nums': ['US-2020025859-A1', 'US-2021000566-A1', 'US-2021181673-A1', 'US-12025581-B2', 'WO-2024112568-A1', 'CA-3161617-A1', 'US-2019328740-A1', 'KR-20050085437-A', 'US-6750960-B2', 'US-11421276-B2'], 'total_to_search': 114}, 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:46': {'california_pub_nums_count': 114, 'sample_pub_nums': ['AU-2003247814-A1', 'AU-2003297741-A1', 'AU-2004253879-A1', 'AU-2005269556-A1', 'AU-2007297661-A1', 'AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2017356943-A1', 'AU-2019275518-B2'], 'message': 'Ready to search for citing patents'}, 'var_functions.execute_python:48': {'patents_with_citations_in_sample': 1000, 'citing_patents_count': 0, 'unique_citing_assignees': 0, 'sample_assignees': [], 'sample_citing_patent': 'None'}, 'var_functions.execute_python:50': {'total_citing_assignees': 0, 'total_ca_publications': 114, 'sample_assignees': [], 'sample_ca_cpc_mapping': {'US-2022074631-A1': ['F25B21/00', 'F25B21/00', 'F25B21/00'], 'TW-201925402-A': ['C09J9/02', 'C09J9/02', 'C09J9/02'], 'US-11421276-B2': ['C12Q1/6883', 'C12Q1/6883', 'C12Q1/6883'], 'AU-2019275518-B2': ['A61K31/34', 'A61K31/351', 'A61K31/351', 'A61K31/357', 'A61K31/025'], 'JP-S6163700-A': ['C07K16/34', 'C07K16/34']}}, 'var_functions.execute_python:52': {'citing_patents_found': 0, 'total_patents_searched': 500, 'sample_citing': 'No matches found', 'ca_pub_nums_count': 114}, 'var_functions.query_db:54': [{'total': '277813'}], 'var_functions.execute_python:56': {'total_ca_patents': 169, 'extracted_pub_nums': 329, 'sample_pub_nums': ['AP-2011005954-A', 'AP-3334-A', 'AU-2001257114-A1', 'AU-2001296493-A', 'AU-2001296493-B2', 'AU-2002254753-A', 'AU-2002254753-B2', 'AU-2003247814-A', 'AU-2003247814-A1', 'AU-2003297741-A', 'AU-2003297741-A1', 'AU-2004253879-A', 'AU-2004253879-A1', 'AU-2005269556-A', 'AU-2005269556-A1'], 'total_database_patents': 277813}, 'var_functions.execute_python:58': {'total_california_patents': 169, 'extracted_publication_numbers': 114, 'patents_with_primary_cpc': 114, 'sample_mappings': {'US-2022074631-A1': ['F25B21/00'], 'TW-201925402-A': ['C09J9/02'], 'US-11421276-B2': ['C12Q1/6883'], 'AU-2019275518-B2': ['A61K31/351', 'A61K31/357', 'A61K31/025', 'A61K31/34'], 'JP-S6163700-A': ['C07K16/34'], 'US-2017281687-A1': ['A61K35/28'], 'AU-2003247814-A1': ['A61H9/005'], 'AU-2017356943-A1': ['C07C253/30'], 'US-6237292-B1': ['E04H9/021'], 'US-7745569-B2': ['C07K14/4711']}}, 'var_functions.execute_python:60': {'total_ca_pubs': 169, 'sample_like_query': "citation LIKE '%IL-23672515-A%' OR citation LIKE '%US-202016883515-A%' OR citation LIKE '%TW-107142982-A%' OR citation LIKE '%CA-3225295-A%' OR citation LIKE '%US-2023067015-W%'", 'ca_cpc_mappings_count': 169, 'sample_cpc_mappings': {'US-202117472182-A': ['F25B21/00'], 'TW-107142982-A': ['C09J9/02'], 'US-201916454755-A': ['C12Q1/6883'], 'AU-2019275518-A': ['A61K31/351', 'A61K31/34', 'A61K31/357', 'A61K31/025'], 'US-201515313510-A': ['H01M4/134']}}}

exec(code, env_args)
