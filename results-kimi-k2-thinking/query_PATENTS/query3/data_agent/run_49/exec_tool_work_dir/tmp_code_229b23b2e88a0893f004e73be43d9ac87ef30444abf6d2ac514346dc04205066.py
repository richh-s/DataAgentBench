code = """import json
import re

# Load UC data
cpc_codes_by_pubnum = {}
uc_file_path = locals()['var_functions.query_db:14']
with open(uc_file_path, 'r') as f:
    uc_data = json.load(f)

# Build UC set
uc_pub_numbers = set()
pubnum_pattern = r'pub\.? number\s*([A-Z]{2}-[A-Z0-9-]+)'

for entry in uc_data:
    patents_info = entry.get('Patents_info', '')
    match = re.search(pubnum_pattern, patents_info)
    if match:
        pub_num = match.group(1).strip()
        pub_num = re.sub(r'\s*-\s*', '-', pub_num)
        uc_pub_numbers.add(pub_num)
        
        # Store CPC codes
        cpc_field = entry.get('cpc', '[]')
        try:
            cpc_data = json.loads(cpc_field)
            subclasses = set()
            for item in cpc_data:
                code = item.get('code', '') if isinstance(item, dict) else ''
                if code:
                    m = re.match(r'([A-Z][0-9]{2}[A-Z]?)', code)
                    if m:
                        subclasses.add(m.group(1))
            cpc_codes_by_pubnum[pub_num] = list(subclasses)
        except:
            cpc_codes_by_pubnum[pub_num] = []

print(f"UC patents: {len(uc_pub_numbers)}")
print(f"Sample: {list(uc_pub_numbers)[:5]}")

# Now scan citation data for matches
citation_path = locals()['var_functions.query_db:26']
with open(citation_path, 'r') as f:
    all_citations = json.load(f)

# Find actual citations of UC patents
uc_citations = []  # List of (citing_assignee, cited_uc_patent)
processed = 0

for entry in all_citations[:50000]:  # Process subset first for speed
    processed += 1
    if processed % 10000 == 0:
        print(f"Processed {processed}")
    
    patents_info = entry.get('Patents_info', '')
    
    # Skip UC patents
    if 'UNIV CALIFORNIA' in patents_info.upper():
        continue
    
    # Extract assignee
    assignee = None
    patterns = [
        r'^([^,\.]+?)\s+(holds|hold|owns|is owned by|is assigned to|assigned to)',
        r'^(?:In [A-Z]{2},\s*)?([^,\.]+?)\s+(holds|hold|owns|application|patent filing)',
    ]
    
    for pat in patterns:
        m = re.search(pat, patents_info)
        if m:
            candidate = m.group(1).strip()
            if candidate and candidate not in ['is', 'the application', 'patent filing', 'application']:
                assignee = candidate
                break
    
    if not assignee or len(assignee) > 200 or 'UNIV CALIFORNIA' in assignee.upper():
        continue
    
    # Check citations
    citation_field = entry.get('citation', '[]')
    try:
        citations = json.loads(citation_field)
        for citation in citations:
            if isinstance(citation, dict):
                cited_pub = citation.get('publication_number', '')
                if cited_pub:
                    cited_norm = re.sub(r'\s*-\s*', '-', str(cited_pub))
                    if cited_norm in uc_pub_numbers:
                        uc_citations.append((assignee, cited_norm))
                        print(f"Match: {assignee} cites {cited_norm}")
    except:
        pass

print(f"Found {len(uc_citations)} UC citations in sample")

if uc_citations:
    print("Sample citations:")
    for i, (assignee, pubnum) in enumerate(uc_citations[:10]):
        print(f"  {assignee} -> {pubnum} (CPC: {cpc_codes_by_pubnum.get(pubnum, [])})")

print('__RESULT__:')
print(json.dumps({
    'uc_patents': len(uc_pub_numbers),
    'citations_found': len(uc_citations),
    'sample': uc_citations[:5]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:16': ['cpc_definition'], 'var_functions.execute_python:22': 'Loaded 169 UNIV CALIFORNIA patents', 'var_functions.execute_python:24': {'count': 59, 'sample': ['US-2022074631-A1', 'TW-201925402-A', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'US-9061071-B2', 'EP-0826155-A4', 'RO-70061-A', 'WO-2021102420-A1', 'WO-2012162563-A2']}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': 'Proceed to loading citation data', 'var_functions.execute_python:30': 'UC data loaded successfully', 'var_functions.execute_python:32': 'Citation data loaded, 277813 records', 'var_functions.execute_python:34': {'citing_assignee_count': 0, 'top_assignees': []}, 'var_functions.execute_python:36': {'citing_assignees_count': 1, 'matches_found': 1, 'top_assignees': ['US patent application (no. US-201715785968-A) is held by BLOOM ENERGY CORP and has publication no. US-10615444-B2.']}, 'var_functions.execute_python:40': {'total_citations': 1, 'unique_assignees': 1, 'assignees': ['The US patent']}, 'var_functions.execute_python:42': {'total_records': 277813, 'samples': [{'index': 0, 'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "JP-H01209663-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n '}, {'index': 1, 'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "DE-3533193-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n  '}, {'index': 2, 'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "JP-S53139639-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n '}, {'index': 3, 'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "EP-0126544-A2",\n    "type": ""\n  },\n  {\n    "application_number": "",\n  '}, {'index': 4, 'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4051340-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n   '}]}}

exec(code, env_args)
