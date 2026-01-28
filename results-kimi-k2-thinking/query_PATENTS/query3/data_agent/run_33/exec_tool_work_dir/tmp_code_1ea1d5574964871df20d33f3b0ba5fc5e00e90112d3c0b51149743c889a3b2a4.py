code = """import json
import re

# Read all patents data
all_patents_path = locals()['var_functions.query_db:24']
with open(all_patents_path, 'r') as f:
    all_patents = json.load(f)

# Extract California patents and create mapping
publication_to_assignee = {}
california_publications = set()
assignee_citations_found = {}

# First pass: collect all California publications
for patent in all_patents:
    patents_info = patent.get('Patents_info', '')
    if 'UNIV CALIFORNIA' in patents_info:
        pub_match = re.search(r'(US|WO|EP|AU|JP|KR|CN|CA|TW|RO|PT|IL|FR|DE)-[A-Z0-9]+-[A-Z0-9]+', patents_info)
        if pub_match:
            california_publications.add(pub_match.group())

# Second pass: find assignees that cite California patents
citing_assignees = {}

for patent in all_patents:
    patents_info = patent.get('Patents_info', '')
    
    # Skip California patents themselves
    if 'UNIV CALIFORNIA' in patents_info:
        continue
    
    # Get assignee name from this patent
    assignee_match = re.search(r'(.*?) holds? the |(.*?) assigned to |(.*?) belonging to |(.*?) owned by ', patents_info)
    current_assignee = None
    if assignee_match:
        for group in assignee_match.groups():
            if group:
                current_assignee = group.strip()
                break
    
    # Parse citations
    citation_data = patent.get('citation', '[]')
    if citation_data and citation_data != '[]':
        try:
            if isinstance(citation_data, str):
                citations = json.loads(citation_data)
            else:
                citations = citation_data
            
            for citation in citations:
                cited_pub = citation.get('publication_number')
                if cited_pub and cited_pub in california_publications:
                    # Found a citation to a California patent
                    if current_assignee not in citing_assignees:
                        citing_assignees[current_assignee] = {
                            'count': 0,
                            'cited_california_patents': set()
                        }
                    citing_assignees[current_assignee]['count'] += 1
                    citing_assignees[current_assignee]['cited_california_patents'].add(cited_pub)
        except:
            continue

# Prepare output
output = {
    'total_california_publications': len(california_publications),
    'citing_assignees_count': len(citing_assignees),
    'top_citing_assignees': []
}

# Sort by count and prepare top results
sorted_assignees = sorted(citing_assignees.items(), key=lambda x: x[1]['count'], reverse=True)
for assignee, info in sorted_assignees[:20]:
    output['top_citing_assignees'].append({
        'assignee': assignee,
        'citation_count': info['count'],
        'sample_cited_patents': list(info['cited_california_patents'])[:3]
    })

print('__RESULT__:')
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', '__builtins__', 'json', 're'], 'var_functions.execute_python:12': {'california_patents_path': 'file_storage/functions.query_db:5.json', 'table_list_path': ['publicationinfo']}, 'var_functions.execute_python:14': {'num_california_patents': 5, 'sample_patent_citations': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4599677-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2015129765-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "FR-3105380-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-11466906-B2",\n    "type": ""\n  }\n]'}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'total_california_patents': 5, 'total_cited_publications': 33, 'sample_cited_publications': ['US-2012015904-A1', 'US-2006078882-A1', 'US-2016265059-A1', 'US-2003199000-A1', 'US-2015129765-A1', 'US-9410204-B2', 'US-2002115120-A1', 'US-2004191783-A1', 'US-10047396-B2', 'US-2015018234-A1'], 'citations_by_patent': [{'california_patent_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'cited_publication_numbers': ['US-4599677-A', 'US-2015129765-A1', 'US-11466906-B2']}, {'california_patent_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.', 'cited_publication_numbers': []}, {'california_patent_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.', 'cited_publication_numbers': ['US-2001053519-A1', 'US-2002115120-A1', 'US-2003119064-A1', 'US-2003199000-A1', 'US-2004191783-A1', 'US-2004203083-A1', 'US-2006046259-A1', 'US-2006078882-A1', 'US-2007042425-A1', 'US-2007050146-A1', 'US-2007280917-A1', 'US-2009148933-A1', 'US-2009197774-A1', 'US-2010105046-A1', 'US-2010197518-A1', 'US-2010216115-A1', 'US-2012015904-A1', 'US-2012065087-A1', 'US-2012316076-A1', 'US-2015018234-A1', 'US-9057109-B2', 'US-9200322-B2', 'US-9410204-B2', 'US-2016237501-A1', 'US-2016265059-A1', 'US-2016289765-A1', 'US-2017029891-A1', 'US-9803243-B2', 'US-10047396-B2', 'US-10196690-B2']}, {'california_patent_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.', 'cited_publication_numbers': []}, {'california_patent_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.', 'cited_publication_numbers': []}]}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'total_UNIV_CALIFORNIA_patents': 159, 'sample_publication_numbers': ['US-202117472182-A', 'TW-107142982-A', 'US-201916454755-A', 'AU-2019275518-A', 'US-201515313510-A', 'JP-13313985-A', 'US-201715625819-A', 'EP-00992018-A', 'AU-2003247814-A', 'AU-2017356943-A'], 'sample_patent': {'publication_number': 'US-202117472182-A', 'patent_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'cpc_field': ''}}}

exec(code, env_args)
