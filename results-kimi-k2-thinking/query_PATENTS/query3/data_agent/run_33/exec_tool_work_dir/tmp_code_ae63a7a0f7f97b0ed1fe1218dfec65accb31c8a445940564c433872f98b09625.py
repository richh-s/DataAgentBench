code = """import json
import re

# Load a sample of patents to check citation formats
print('Loading sample of patents to check citation data...')
all_patents_path = locals()['var_functions.query_db:24']
with open(all_patents_path, 'r') as f:
    all_patents = json.load(f)

# Get a subset for detailed inspection
sample_patents = all_patents[:200]  # First 200 patents

# Collect all unique citation publication numbers
citation_numbers = set()
california_citation_matches = []

for patent in sample_patents:
    patents_info = patent.get('Patents_info', '')
    citation_data = patent.get('citation', '')
    
    if citation_data and citation_data != '[]':
        try:
            citations = json.loads(citation_data) if isinstance(citation_data, str) else citation_data
            
            for citation in citations:
                cited_pub = citation.get('publication_number', '')
                if cited_pub:
                    citation_numbers.add(cited_pub)
                    
                    # Check if this looks like it might be a California patent
                    if 'US-' in cited_pub:
                        california_citation_matches.append({
                            'cited_pub': cited_pub,
                            'patent_info': patents_info[:100] + '...'  # Truncate for readability
                        })
        except:
            pass

print(f'Found {len(citation_numbers)} unique citation publication numbers')
print(f'Found {len(california_citation_matches)} US citations to review')

# Now let's check against actual California patents more carefully
print('\\nLoading California patents to build lookup...')
california_pubs_path = locals()['var_functions.query_db:50']
with open(california_pubs_path, 'r') as f:
    california_patents = json.load(f)

# Build a lookup of California publication numbers in various formats
california_lookup = set()
california_by_prefix = {}

for patent in california_patents:
    patents_info = patent.get('Patents_info', '')
    # Extract publication number
    pub_match = re.search(r'pub\. number\s+([A-Z]+-[A-Z0-9]+-[A-Z0-9]+)', patents_info)
    if pub_match:
        pub_num = pub_match.group(1)
        california_lookup.add(pub_num)
        
        # Also extract by country prefix
        country = pub_num.split('-')[0]
        if country not in california_by_prefix:
            california_by_prefix[country] = set()
        california_by_prefix[country].add(pub_num)

print(f'California lookup contains {len(california_lookup)} publication numbers')

# Check for matches
potential_matches = []
for cited_pub in citation_numbers:
    if cited_pub in california_lookup:
        potential_matches.append(cited_pub)

print(f'Direct matches found: {len(potential_matches)}')
if potential_matches:
    print('Matching publication numbers:', potential_matches[:10])

# Save detailed analysis
analysis = {
    'total_citations_in_sample': len(citation_numbers),
    'us_citation_count': len([c for c in citation_numbers if 'US-' in c]),
    'direct_matches_to_california': len(potential_matches),
    'matching_numbers': potential_matches[:20],
    'sample_citation_numbers': list(citation_numbers)[:50]
}

print('__RESULT__:')
print(json.dumps(analysis, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', '__builtins__', 'json', 're'], 'var_functions.execute_python:12': {'california_patents_path': 'file_storage/functions.query_db:5.json', 'table_list_path': ['publicationinfo']}, 'var_functions.execute_python:14': {'num_california_patents': 5, 'sample_patent_citations': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4599677-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2015129765-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "FR-3105380-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-11466906-B2",\n    "type": ""\n  }\n]'}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'total_california_patents': 5, 'total_cited_publications': 33, 'sample_cited_publications': ['US-2012015904-A1', 'US-2006078882-A1', 'US-2016265059-A1', 'US-2003199000-A1', 'US-2015129765-A1', 'US-9410204-B2', 'US-2002115120-A1', 'US-2004191783-A1', 'US-10047396-B2', 'US-2015018234-A1'], 'citations_by_patent': [{'california_patent_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'cited_publication_numbers': ['US-4599677-A', 'US-2015129765-A1', 'US-11466906-B2']}, {'california_patent_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.', 'cited_publication_numbers': []}, {'california_patent_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.', 'cited_publication_numbers': ['US-2001053519-A1', 'US-2002115120-A1', 'US-2003119064-A1', 'US-2003199000-A1', 'US-2004191783-A1', 'US-2004203083-A1', 'US-2006046259-A1', 'US-2006078882-A1', 'US-2007042425-A1', 'US-2007050146-A1', 'US-2007280917-A1', 'US-2009148933-A1', 'US-2009197774-A1', 'US-2010105046-A1', 'US-2010197518-A1', 'US-2010216115-A1', 'US-2012015904-A1', 'US-2012065087-A1', 'US-2012316076-A1', 'US-2015018234-A1', 'US-9057109-B2', 'US-9200322-B2', 'US-9410204-B2', 'US-2016237501-A1', 'US-2016265059-A1', 'US-2016289765-A1', 'US-2017029891-A1', 'US-9803243-B2', 'US-10047396-B2', 'US-10196690-B2']}, {'california_patent_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.', 'cited_publication_numbers': []}, {'california_patent_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.', 'cited_publication_numbers': []}]}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'total_UNIV_CALIFORNIA_patents': 159, 'sample_publication_numbers': ['US-202117472182-A', 'TW-107142982-A', 'US-201916454755-A', 'AU-2019275518-A', 'US-201515313510-A', 'JP-13313985-A', 'US-201715625819-A', 'EP-00992018-A', 'AU-2003247814-A', 'AU-2017356943-A'], 'sample_patent': {'publication_number': 'US-202117472182-A', 'patent_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'cpc_field': ''}}, 'var_functions.execute_python:28': {'total_california_publications': 159, 'citing_assignees_count': 0, 'top_citing_assignees': []}, 'var_functions.execute_python:30': {'total_california_publications': 84, 'sample_california_publications': ['WO-2017214343-A1', 'IL-274176-A', 'US-11376346-B2', 'AU-2019275518-B2', 'EP-0826155-A4', 'US-2017281687-A1', 'CN-100339724-C', 'ID-23426-A', 'WO-2018026404-A3', 'CA-3027364-A1'], 'total_publications': 138486}, 'var_functions.execute_python:32': {'total_california_publications': 84, 'citing_assignees_count': 0, 'sample_california_cpc_codes': {}, 'top_citing_assignees': []}, 'var_functions.execute_python:34': {'total_california_publications': 167, 'sample_publications': ['PE-20130764-A1', 'US-3666017D-A', 'WO-2017214343-A1', 'US-2017050153-A1', 'US-2020025859-A1', 'AU-2409401-A', 'EP-2029921-A4', 'US-8361933-B2', 'US-2023171142-A1', 'US-2021101879-A1'], 'sample_mapping': {'US-2022074631-A1': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'TW-201925402-A': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.', 'US-11421276-B2': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.', 'AU-2019275518-B2': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.', 'US-2017194630-A1': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.'}}, 'var_functions.execute_python:36': {'total_california_publications': 84, 'citing_assignees_found': 0, 'top_citing_assignees': []}, 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:44': [{'symbol': 'A01K2227/108', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'titleFull': 'Ovine'}, {'symbol': 'A01K2227/106', 'titleFull': 'Primate'}, {'symbol': 'A01K2227/706', 'titleFull': 'Insects, e.g. Drosophila melanogaster, medfly'}, {'symbol': 'A01K2227/703', 'titleFull': 'Worms, e.g. Caenorhabdities elegans'}, {'symbol': 'A01K2267/025', 'titleFull': 'Animal producing cells or organs for transplantation'}, {'symbol': 'A01K2267/0393', 'titleFull': 'Animal model comprising a reporter system for screening tests'}], 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.execute_python:52': {'total_california_publications': 84, 'sample_mapping': {'US-2022074631-A1': ['F25B21/00', 'F28D15/00', 'F25B21/00', 'F28D15/00', 'F25B21/00'], 'TW-201925402-A': ['C09J11/04', 'C09J9/02', 'C09D11/52', 'C09D11/322', 'C09J9/02', 'C09D11/037', 'C09J11/04', 'C09D11/52', 'C09D11/322', 'C09D11/037', 'C08K3/08', 'C09J9/02', 'C09D11/037', 'C08K3/042', 'C09J11/04', 'C09D11/322', 'C09D11/52'], 'AU-2019275518-B2': ['A61K31/357', 'A61K31/34', 'A61K31/08', 'A61D7/04', 'A61K31/025', 'A61K31/357', 'A61P43/00', 'A61P25/20', 'A61K31/045', 'A61K31/02', 'A61P23/00', 'A61K9/007', 'A61K31/341', 'A61M16/01', 'A61D7/04', 'A61K31/351', 'A61K31/351', 'A61K31/34', 'A61K31/08', 'A61K31/025', 'A61P43/00', 'A61K31/02', 'A61K31/045', 'A61P11/00', 'A61K31/357', 'A61P23/00', 'A61P25/20', 'A61M16/01', 'A61K31/357', 'A61P11/00', 'A61K9/007', 'A61K31/025', 'A61K31/015', 'A61K31/341', 'A61K31/025', 'A61K31/045', 'A61K31/341', 'A61K31/351', 'A61K31/357', 'A61K31/08', 'A61K9/007', 'A61P23/00', 'A61K31/34', 'A61K31/015'], 'US-2017194630-A1': ['H01M10/0525', 'H01M4/386', 'H01M4/0469', 'H01M4/382', 'H01M4/625', 'H01M10/0569', 'H01M4/1395', 'H01M4/0483', 'H01M4/382', 'H01M4/1395', 'H01M10/0525', 'H01M4/0471', 'H01M4/134', 'H01M4/366', 'H01M4/0469', 'H01M4/625', 'H01M4/0471', 'H01M4/386', 'H01M4/134', 'H01M4/366', 'H01M10/0569', 'H01M10/0525', 'H01M4/386', 'H01M4/382', 'H01M4/134', 'H01M4/1395', 'H01M4/625', 'H01M4/0483', 'H01M4/0471', 'H01M4/0492', 'H01M4/0469', 'H01M4/74', 'H01M4/134', 'H01M4/382', 'H01M4/1395', 'H01M4/0471', 'H01M4/625', 'H01M4/386', 'H01M10/0525'], 'JP-S6163700-A': ['C07K16/30', 'A61P35/00', 'C07K16/34', 'C07K16/30', 'C07K16/34']}}, 'var_functions.execute_python:54': {'total_citations_found': 0, 'total_california_patents_cited': 84, 'assignees_by_citation_count': [], 'assignees_by_unique_cpc_codes': []}, 'var_functions.execute_python:58': {'total_citing_assignees': 0, 'total_california_patents_cited': 0, 'top_assignees': []}}

exec(code, env_args)
