code = """import json
import re

# Load UC publication numbers
uc_patents_file = locals()['var_functions.query_db:14']
with open(uc_patents_file, 'r') as f:
    uc_patents = json.load(f)

uc_pub_numbers = set()
for patent in uc_patents:
    info = patent['Patents_info'].upper()
    matches = re.findall(r'\b([A-Z]{2}-\d{4,}[A-Z0-9-]*)\b', info)
    for match in matches:
        uc_pub_numbers.add(match)

print('Have', len(uc_pub_numbers), 'UC publication numbers')

# Load patents with citations
all_patents_file = locals()['var_functions.query_db:42']
with open(all_patents_file, 'r') as f:
    all_patents = json.load(f)

# Find patents citing UC patents
citing_patents = []
uc_citations_found = set()

for patent in all_patents:
    citations = patent.get('citation', [])
    if not citations or citations == '[]':
        continue
    
    # Parse citation JSON
    if isinstance(citations, str):
        try:
            citations = json.loads(citations)
        except:
            continue
    
    # Check each citation
    for citation in citations:
        pub_num = citation.get('publication_number', '')
        if pub_num and pub_num in uc_pub_numbers:
            # This patent cites a UC patent
            # Check if it's not a UC patent itself
            patent_info = patent['Patents_info']
            if 'UNIV CALIFORNIA' not in patent_info.upper():
                citing_patents.append({
                    'patent_info': patent_info,
                    'cited_uc_patent': pub_num,
                    'cpc': patent.get('cpc', [])
                })
                uc_citations_found.add(pub_num)
                break  # No need to check more citations for this patent

print('Found', len(citing_patents), 'patents citing UC patents (excluding UC)')
print('These cite', len(uc_citations_found), 'different UC patents')

# Save results
with open('/tmp/citing_patents.json', 'w') as f:
    json.dump(citing_patents, f)

print('First citing patent:', citing_patents[0]['patent_info'][:150] if citing_patents else 'None')"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'citation': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4599677-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2015129765-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "FR-3105380-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-11466906-B2",\n    "type": ""\n  }\n]'}], 'var_functions.execute_python:12': {'sample_patent': {'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'citation': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4599677-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2015129765-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "FR-3105380-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-11466906-B2",\n    "type": ""\n  }\n]'}}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:24': {'count': 169, 'first_keys': ['Patents_info', 'citation']}, 'var_functions.execute_python:26': {'uc_patent_count': 169, 'uc_pub_numbers_count': 114, 'sample_uc_numbers': ['AU-2003297741-A1', 'AU-3353000-A', 'HR-P20201231-T1', 'US-2017087258-A1', 'AU-2015364602-B2', 'HK-1250569-A1', 'MX-2013002850-A', 'CA-2718348-C', 'JP-2009260386-A', 'KR-20050085437-A']}, 'var_functions.query_db:28': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'citation': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4599677-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2015129765-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "FR-3105380-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-11466906-B2",\n    "type": ""\n  }\n]'}], 'var_functions.execute_python:34': {'uc_patent_count': 169, 'uc_pub_numbers_count': 187, 'sample_uc_numbers': ['AP-2011005954-A', 'AU-2001296493-A', 'AU-2003247814-A', 'AU-2003247814-A1', 'AU-2003297741-A1', 'AU-2004253879-A', 'AU-2004253879-A1', 'AU-2005269556-A', 'AU-2005269556-A1', 'AU-2007297661-A1']}, 'var_functions.execute_python:38': {'count': 187, 'sample': ['US-2021000566-A1', 'AU-7724398-A', 'US-2017015812-W', 'CA-3055214-A', 'US-202117472182-A']}, 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.execute_python:46': {'total_uc_patents': 169, 'unique_uc_pub_numbers': 114, 'sample_numbers': ['US-2019328740-A1', 'US-2019209590-A1', 'CA-2283629-C', 'US-2017087258-A1', 'IL-244029-A0', 'MX-2013002850-A', 'US-11546022-B2', 'US-2021181673-A1', 'CA-3161617-A1', 'RO-70061-A']}, 'var_functions.execute_python:52': {'total_patents_with_citations': 137678, 'uc_patent_publications': 0, 'citing_patents_count': 0}, 'var_functions.execute_python:56': {'uc_patent_count': 169, 'uc_pub_numbers_count': 187, 'sample_numbers': ['AP-2011005954-A', 'AU-2001296493-A', 'AU-2003247814-A', 'AU-2003247814-A1', 'AU-2003297741-A1', 'AU-2004253879-A', 'AU-2004253879-A1', 'AU-2005269556-A', 'AU-2005269556-A1', 'AU-2007297661-A1']}}

exec(code, env_args)
