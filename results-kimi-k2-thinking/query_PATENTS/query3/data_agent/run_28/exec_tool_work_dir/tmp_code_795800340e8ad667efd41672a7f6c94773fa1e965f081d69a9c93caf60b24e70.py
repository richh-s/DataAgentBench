code = """import json
import re

# Get the file path for university of california patents
file_path = locals()['var_functions.query_db:20']

# Read all patents assigned to UNIV CALIFORNIA
with open(file_path, 'r') as f:
    uc_patents = json.load(f)

# Extract all cited publication numbers
cited_pub_numbers = []
for patent in uc_patents:
    citations_str = patent.get('citation', '[]')
    if citations_str and citations_str != '[]':
        try:
            citations = json.loads(citations_str)
            for citation in citations:
                pub_num = citation.get('publication_number')
                if pub_num:
                    cited_pub_numbers.append(pub_num)
        except:
            continue

# Remove duplicates
cited_pub_numbers = list(set(cited_pub_numbers))

print('Unique cited publication numbers:', len(cited_pub_numbers))
print('Sample cited numbers:', cited_pub_numbers[:10])

# Create query to find all patents with those publication numbers
# We need to batch this since there might be many
print('__RESULT__:')
print(json.dumps({
    'total_cited_pub_numbers': len(cited_pub_numbers),
    'sample': cited_pub_numbers[:10]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:10': ['cpc_definition'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:18': {'sample_patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'sample_citation_type': "<class 'str'>", 'sample_citation_length': 653}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'total_uc_patents': 169, 'total_citations': 1308}}

exec(code, env_args)
