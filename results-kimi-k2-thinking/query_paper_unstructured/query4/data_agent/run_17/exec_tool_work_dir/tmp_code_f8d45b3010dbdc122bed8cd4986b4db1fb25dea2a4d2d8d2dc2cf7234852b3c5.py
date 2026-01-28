code = """import json

# Read the MongoDB results file
with open('/tmp/tmpa8i6hpt8.json', 'r') as f:
    papers_data = json.load(f)

print('Total papers found: ' + str(len(papers_data)))

papers_2016 = []

for paper in papers_data:
    text = paper['text']
    # Check if text contains 2016
    if '2016' in text:
        # Check for physical activity (case insensitive)
        lower_text = text.lower()
        if 'physical activity' in lower_text:
            filename = paper['filename']
            title = filename.replace('.txt', '')
            papers_2016.append(title)

print('\nPapers from 2016 mentioning physical activity: ' + str(len(papers_2016)))
if papers_2016:
    print('\nPaper titles:')
    for title in papers_2016:
        print('  - ' + title)
else:
    print('No 2016 papers found')

# Prepare result for next step
result = {
    'papers_2016': [{'title': title} for title in papers_2016],
    'count': len(papers_2016)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:9': {'status': 'debugging'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
