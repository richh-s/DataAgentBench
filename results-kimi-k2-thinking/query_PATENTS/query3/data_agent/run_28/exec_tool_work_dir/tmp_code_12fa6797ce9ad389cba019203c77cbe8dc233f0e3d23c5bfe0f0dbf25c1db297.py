code = """import json
import re

# Read data from files
uc_file = locals()['var_functions.query_db:20']
all_file = locals()['var_functions.query_db:28']

with open(uc_file, 'r') as f:
    uc_patents = json.load(f)

with open(all_file, 'r') as f:
    all_patents = json.load(f)

# Build UC publication numbers set
uc_pub_numbers = set()
for patent in uc_patents:
    info = patent['Patents_info']
    match = re.search(r'(?:pub\. number|publication number|pub\. no\.)\s+([A-Z0-9-]+)', 
                      info, re.IGNORECASE)
    if match:
        uc_pub_numbers.add(match.group(1))

print('UC patents count:', len(uc_patents))
print('UC pub numbers found:', len(uc_pub_numbers))

# Find citing patents
results = []
for patent in all_patents:
    info = patent['Patents_info']
    if 'UNIV CALIFORNIA' in info:
        continue
    
    citations_str = patent.get('citation', '[]')
    if citations_str and citations_str != '[]':
        try:
            citations = json.loads(citations_str)
            for citation in citations:
                cited_pub = citation.get('publication_number')
                if cited_pub and cited_pub in uc_pub_numbers:
                    # Get CPC codes
                    cpc_str = patent.get('cpc', '[]')
                    if cpc_str and cpc_str != '[]':
                        try:
                            cpc_list = json.loads(cpc_str)
                            cpc_codes = [item.get('code') for item in cpc_list if item.get('code')]
                        except:
                            cpc_codes = []
                    else:
                        cpc_codes = []
                    
                    # Get assignee
                    assignee = 'Unknown'
                    words = info.split()
                    if words:
                        name_parts = []
                        for word in words[:6]:
                            if re.match(r'^[A-Z0-9\-]{2,}$', word):
                                name_parts.append(word)
                            else:
                                break
                        if name_parts:
                            name = ' '.join(name_parts)
                            name = re.split(r'\s+(?:and|holds|is|has|owns|assigned)\s+', name, 1)[0]
                            assignee = name
                    
                    if assignee != 'UNIV CALIFORNIA':
                        results.append({
                            'assignee': assignee,
                            'cpc_codes': cpc_codes
                        })
        except:
            pass

print('Total citing patents found (excluding UC):', len(results))

# Count unique assignees
assignees = [r['assignee'] for r in results]
from collections import Counter
assignee_counts = Counter(assignees)
print('Unique assignees:', len(assignee_counts))

# Prepare CPC codes for lookup
all_cpc_codes = set()
for r in results:
    all_cpc_codes.update(r['cpc_codes'])

print('Unique CPC codes to look up:', len(all_cpc_codes))

output = {
    'total_results': len(results),
    'assignee_counts': dict(assignee_counts),
    'sample_results': results[:10],
    'cpc_codes_list': list(all_cpc_codes)[:50]  # First 50 for now
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:10': ['cpc_definition'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:18': {'sample_patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'sample_citation_type': "<class 'str'>", 'sample_citation_length': 653}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'total_uc_patents': 169, 'total_citations': 1308}, 'var_functions.execute_python:24': {'total_cited_pub_numbers': 1112, 'sample': ['US-2016010076-A1', 'US-4642569-A', 'US-5403841-A', 'EP-0474894-A1', 'US-2010305187-A1', 'US-2010197518-A1', 'US-7074888-B1', 'US-2014245496-A1', 'US-2020245905-A1', 'US-4940658-A']}, 'var_functions.execute_python:26': {'uc_pub_numbers_count': 114, 'citation_map_size': 1112, 'sample_cited': ['US-4599677-A', 'US-2015129765-A1', 'FR-3105380-A1', 'US-11466906-B2', 'US-2001053519-A1']}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:30': {'total_citing_patents': 4, 'unique_citing_assignees': 4, 'top_assignees': {'CALIFORNIA INST OF TECHN and has publication number US-2005165588-A1.': 1, 'Unknown': 1, 'CRYSTAL IS INC and has publication no. US-9447521-B2.': 1, 'US application (number US-2000608-A)': 1}}}

exec(code, env_args)
