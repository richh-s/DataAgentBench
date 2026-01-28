code = """import json

# The result is stored under key var_query_db:2
# Read the full results from the file
result_file = var_query_db:2

# Read the full results
with open(result_file, 'r') as f:
    all_docs = json.load(f)

print('Total documents in civic_docs collection: %d' % len(all_docs))
print('Sample document structure preview:')
print(str(all_docs[0])[:500])
print('\n' + '='*50 + '\n')

# Check filenames to find 2022 documents
filenames_2022 = []
for doc in all_docs:
    filename = doc.get('filename', '')
    if '2022' in filename:
        filenames_2022.append(filename)

print('Documents with 2022 in filename: %d' % len(filenames_2022))
for name in filenames_2022[:10]:
    print(name)

print('\n' + '='*50 + '\n')

# Look for Spring 2022 mentions in the text
spring_2022_docs = []
for doc in all_docs:
    text = doc.get('text', '').lower()
    if '2022' in text and ('spring' in text or 'march' in text or 'april' in text or 'may' in text):
        spring_2022_docs.append(doc)

print('Documents mentioning 2022 and Spring/March/April/May: %d' % len(spring_2022_docs))

print('\n__RESULT__:\n')
print('Found %d documents potentially containing Spring 2022 projects' % len(spring_2022_docs))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
