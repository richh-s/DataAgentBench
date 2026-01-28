code = """import json

# Read the query result file
result_file = var_functions.query_db:2

# Load the full results
with open(result_file, 'r') as f:
    all_docs = json.load(f)

print('Total documents:', len(all_docs))

# Look for documents from 2022
filenames_2022 = []
for doc in all_docs:
    filename = doc.get('filename', '')
    if '2022' in filename:
        filenames_2022.append(filename)

print('Documents with 2022 in filename:', len(filenames_2022))

# Look for Spring 2022 mentions
spring_keywords = ['spring', 'march', 'april', 'may']
for doc in all_docs:
    text = doc.get('text', '').lower()
    has_2022 = '2022' in text
    has_spring = any(keyword in text for keyword in spring_keywords)
    if has_2022 and has_spring:
        print('Found Spring 2022 mention in:', doc['filename'])
        # Print a snippet
        snippet_start = text.find('2022') - 100
        snippet_end = text.find('2022') + 200
        if snippet_start < 0:
            snippet_start = 0
        print(doc['text'][snippet_start:snippet_end])
        print('---')

print('__RESULT__')
print('Analysis of civic documents completed')"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
