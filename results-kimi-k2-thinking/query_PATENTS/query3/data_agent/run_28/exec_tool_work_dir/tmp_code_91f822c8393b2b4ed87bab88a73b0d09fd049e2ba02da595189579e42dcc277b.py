code = """import json
import re

# Get UC patents file path
uc_file_path = locals()['var_functions.query_db:20']

# Read all patents assigned to UNIV CALIFORNIA
with open(uc_file_path, 'r') as f:
    uc_patents = json.load(f)

# Build a mapping of publication numbers to UC patents for quick lookup
uc_pub_numbers = set()
for patent in uc_patents:
    # Extract publication number from Patents_info field
    info = patent['Patents_info']
    # Look for patterns like "pub. number US-2022074631-A1" or "publication number US-11081687-B2"
    match = re.search(r'(?:pub\. number|publication number|pub\. no\.)\s+([A-Z0-9-]+)', info, re.IGNORECASE)
    if match:
        uc_pub_numbers.add(match.group(1))

print('UC publication numbers found:', len(uc_pub_numbers))
print('Sample UC pub numbers:', list(uc_pub_numbers)[:10])

# Extract all cited publication numbers and map back to UC patents
citation_map = {}  # cited_pub_num -> list of uc_patent_info
for patent in uc_patents:
    citations_str = patent.get('citation', '[]')
    if citations_str and citations_str != '[]':
        try:
            citations = json.loads(citations_str)
            for citation in citations:
                cited_pub = citation.get('publication_number')
                if cited_pub:
                    if cited_pub not in citation_map:
                        citation_map[cited_pub] = []
                    citation_map[cited_pub].append(patent['Patents_info'])
        except:
            continue

print('Total unique cited publications:', len(citation_map))

print('__RESULT__:')
print(json.dumps({
    'uc_pub_numbers_count': len(uc_pub_numbers),
    'citation_map_size': len(citation_map),
    'sample_cited': list(citation_map.keys())[:5]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:10': ['cpc_definition'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:18': {'sample_patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'sample_citation_type': "<class 'str'>", 'sample_citation_length': 653}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'total_uc_patents': 169, 'total_citations': 1308}, 'var_functions.execute_python:24': {'total_cited_pub_numbers': 1112, 'sample': ['US-2016010076-A1', 'US-4642569-A', 'US-5403841-A', 'EP-0474894-A1', 'US-2010305187-A1', 'US-2010197518-A1', 'US-7074888-B1', 'US-2014245496-A1', 'US-2020245905-A1', 'US-4940658-A']}}

exec(code, env_args)
