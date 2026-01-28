code = """import json

# Read the UC patents data
result_path = locals()['var_functions.query_db:16']
with open(result_path, 'r') as f:
    uc_patents = json.load(f)

# First, let's collect all unique citation publication numbers
all_citation_pub_numbers = set()
for patent in uc_patents:
    if patent['citation'] and patent['citation'] != '[]':
        try:
            citations = json.loads(patent['citation'])
            for citation in citations:
                pub_num = citation.get('publication_number')
                if pub_num and pub_num.strip():
                    all_citation_pub_numbers.add(pub_num.strip())
        except:
            continue

print('Number of UC patents with citations: ' + str(len(uc_patents)))
print('Number of unique citation publication numbers: ' + str(len(all_citation_pub_numbers)))
print('Sample citation numbers: ' + str(list(all_citation_pub_numbers)[:10]))

result = {
    'uc_patents_count': len(uc_patents),
    'unique_citations_count': len(all_citation_pub_numbers),
    'citation_numbers': list(all_citation_pub_numbers)
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': [{'total': '169'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:22': {'status': 'success', 'count': 87}}

exec(code, env_args)
