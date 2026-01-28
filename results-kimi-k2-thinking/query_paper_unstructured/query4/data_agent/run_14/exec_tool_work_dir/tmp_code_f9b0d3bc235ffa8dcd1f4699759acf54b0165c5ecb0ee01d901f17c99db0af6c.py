code = """import json

mongo_result_path = locals()['var_functions.query_db:2']
print('Reading MongoDB results from:', mongo_result_path)

with open(mongo_result_path, 'r') as f:
    papers = json.load(f)

print('Total number of papers in database:', len(papers))

if papers:
    print('First paper structure keys:', list(papers[0].keys()))
    sample = papers[0]
    print('Sample paper filename:', sample.get('filename'))
    print('Sample text preview (first 500 chars):', sample.get('text', '').strip()[:500])
else:
    print('No papers in database')

# Create a simple result dictionary
result = {
    'paper_count': len(papers)
}
if papers:
    result['sample_keys'] = list(papers[0].keys())
    result['sample_filename'] = papers[0].get('filename')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
