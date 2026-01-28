code = """import json
import re

# Read all patents data
all_patents_path = locals()['var_functions.query_db:24']
with open(all_patents_path, 'r') as f:
    all_patents = json.load(f)

# Load California publications data
california_pubs_path = locals()['var_functions.query_db:22']
with open(california_pubs_path, 'r') as f:
    california_patents_raw = json.load(f)

# Build set of California publication numbers
california_publications = set()
california_patent_cpc_codes = {}

for patent in california_patents_raw:
    patents_info = patent.get('Patents_info', '')
    
    # Extract publication number for California patents
    pub_match = re.search(r'(?:has pub\. number |with publication no\. |with pub\. number |pub\. number )([A-Z]+-[A-Z0-9]+-[A-Z0-9]+)', patents_info)
    if pub_match:
        pub_num = pub_match.group(1)
        california_publications.add(pub_num)
        
        # Store CPC codes for this California patent
        cpc_data = patent.get('cpc', '')
        if cpc_data:
            try:
                cpc_list = json.loads(cpc_data) if isinstance(cpc_data, str) else cpc_data
                cpc_codes = []
                for cpc_item in cpc_list:
                    if isinstance(cpc_item, dict):
                        code = cpc_item.get('code', '')
                        # Get primary CPC codes (inventive=True or first=True)
                        if cpc_item.get('inventive') or cpc_item.get('first'):
                            cpc_codes.append(code)
                            
                california_patent_cpc_codes[pub_num] = cpc_codes
            except:
                california_patent_cpc_codes[pub_num] = []

# Now find citing patents and their assignees
citing_assignees = {}

for patent in all_patents:
    patents_info = patent.get('Patents_info', '')
    
    # Skip California patents themselves
    if 'UNIV CALIFORNIA' in patents_info:
        continue
    
    # Extract assignee
    assignee = None
    assignee_patterns = [
        r'^([^,]+?) (?:holds the|assigned to|belonging to|owned by)',
        r'^The ([^,]+?) (?:holds|assigned|belonging|owned)',
        r'^In [A-Z]{2}, the ([^,]+?) (?:holds|assigned|belonging|owned)',
        r'^Patent filing [^,]*? from [A-Z]{2}, (?:held|assigned|owned) by ([^,]+?)',
        r'^Application [^,]*? from [A-Z]{2}, (?:belonging|assigned|owned) to ([^,]+?)',
        r'^In [A-Z]{2}, the patent (?:filing|application) [^,]*? is (?:assigned|owned) to ([^,]+?)'
    ]
    
    for pattern in assignee_patterns:
        match = re.search(pattern, patents_info)
        if match and match.group(1):
            assignee = match.group(1).strip()
            assignee = re.sub(r'\s+and$', '', assignee)
            break
    
    # Parse citations
    citation_data = patent.get('citation', '')
    if citation_data and citation_data != '[]':
        try:
            citations = json.loads(citation_data) if isinstance(citation_data, str) else citation_data
            
            for citation in citations:
                cited_pub = citation.get('publication_number', '')
                # Check if this citation matches a California publication
                if cited_pub and cited_pub in california_publications:
                    if assignee and 'UNIV CALIFORNIA' not in assignee:
                        if assignee not in citing_assignees:
                            citing_assignees[assignee] = {
                                'count': 0,
                                'cited_california_patents': set(),
                                'cited_cpc_codes': set()
                            }
                        citing_assignees[assignee]['count'] += 1
                        citing_assignees[assignee]['cited_california_patents'].add(cited_pub)
                        # Add CPC codes from this cited California patent
                        if cited_pub in california_patent_cpc_codes:
                            citing_assignees[assignee]['cited_cpc_codes'].update(california_patent_cpc_codes[cited_pub])
        except:
            continue

# Sort and prepare results
sorted_assignees = sorted(citing_assignees.items(), key=lambda x: x[1]['count'], reverse=True)

output = {
    'total_california_publications': len(california_publications),
    'citing_assignees_found': len(citing_assignees),
    'top_citing_assignees': []
}

for i, (assignee, info) in enumerate(sorted_assignees[:20]):
    cpc_codes = list(info['cited_cpc_codes'])
    output['top_citing_assignees'].append({
        'rank': i + 1,
        'assignee': assignee,
        'citation_count': info['count'],
        'unique_california_patents_cited': len(info['cited_california_patents']),
        'cited_cpc_codes': cpc_codes[:10]  # Limit to first 10 for readability
    })

print('__RESULT__:')
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', '__builtins__', 'json', 're'], 'var_functions.execute_python:12': {'california_patents_path': 'file_storage/functions.query_db:5.json', 'table_list_path': ['publicationinfo']}, 'var_functions.execute_python:14': {'num_california_patents': 5, 'sample_patent_citations': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4599677-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2015129765-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "FR-3105380-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-11466906-B2",\n    "type": ""\n  }\n]'}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'total_california_patents': 5, 'total_cited_publications': 33, 'sample_cited_publications': ['US-2012015904-A1', 'US-2006078882-A1', 'US-2016265059-A1', 'US-2003199000-A1', 'US-2015129765-A1', 'US-9410204-B2', 'US-2002115120-A1', 'US-2004191783-A1', 'US-10047396-B2', 'US-2015018234-A1'], 'citations_by_patent': [{'california_patent_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'cited_publication_numbers': ['US-4599677-A', 'US-2015129765-A1', 'US-11466906-B2']}, {'california_patent_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.', 'cited_publication_numbers': []}, {'california_patent_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.', 'cited_publication_numbers': ['US-2001053519-A1', 'US-2002115120-A1', 'US-2003119064-A1', 'US-2003199000-A1', 'US-2004191783-A1', 'US-2004203083-A1', 'US-2006046259-A1', 'US-2006078882-A1', 'US-2007042425-A1', 'US-2007050146-A1', 'US-2007280917-A1', 'US-2009148933-A1', 'US-2009197774-A1', 'US-2010105046-A1', 'US-2010197518-A1', 'US-2010216115-A1', 'US-2012015904-A1', 'US-2012065087-A1', 'US-2012316076-A1', 'US-2015018234-A1', 'US-9057109-B2', 'US-9200322-B2', 'US-9410204-B2', 'US-2016237501-A1', 'US-2016265059-A1', 'US-2016289765-A1', 'US-2017029891-A1', 'US-9803243-B2', 'US-10047396-B2', 'US-10196690-B2']}, {'california_patent_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.', 'cited_publication_numbers': []}, {'california_patent_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.', 'cited_publication_numbers': []}]}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'total_UNIV_CALIFORNIA_patents': 159, 'sample_publication_numbers': ['US-202117472182-A', 'TW-107142982-A', 'US-201916454755-A', 'AU-2019275518-A', 'US-201515313510-A', 'JP-13313985-A', 'US-201715625819-A', 'EP-00992018-A', 'AU-2003247814-A', 'AU-2017356943-A'], 'sample_patent': {'publication_number': 'US-202117472182-A', 'patent_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'cpc_field': ''}}, 'var_functions.execute_python:28': {'total_california_publications': 159, 'citing_assignees_count': 0, 'top_citing_assignees': []}, 'var_functions.execute_python:30': {'total_california_publications': 84, 'sample_california_publications': ['WO-2017214343-A1', 'IL-274176-A', 'US-11376346-B2', 'AU-2019275518-B2', 'EP-0826155-A4', 'US-2017281687-A1', 'CN-100339724-C', 'ID-23426-A', 'WO-2018026404-A3', 'CA-3027364-A1'], 'total_publications': 138486}, 'var_functions.execute_python:32': {'total_california_publications': 84, 'citing_assignees_count': 0, 'sample_california_cpc_codes': {}, 'top_citing_assignees': []}, 'var_functions.execute_python:34': {'total_california_publications': 167, 'sample_publications': ['PE-20130764-A1', 'US-3666017D-A', 'WO-2017214343-A1', 'US-2017050153-A1', 'US-2020025859-A1', 'AU-2409401-A', 'EP-2029921-A4', 'US-8361933-B2', 'US-2023171142-A1', 'US-2021101879-A1'], 'sample_mapping': {'US-2022074631-A1': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'TW-201925402-A': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.', 'US-11421276-B2': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.', 'AU-2019275518-B2': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.', 'US-2017194630-A1': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.'}}}

exec(code, env_args)
