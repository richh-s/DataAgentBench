code = """import json
import re

# Load the MongoDB data from the stored file
with open('/tmp/tmpb1b8k8h6.json', 'r') as f:
    civic_docs_data = json.load(f)

print("Number of documents:", len(civic_docs_data))
print("First document keys:", list(civic_docs_data[0].keys()))

# Let's look at the first document's text to understand the format
doc = civic_docs_data[0]
print("Filename:", doc.get('filename', 'N/A'))

# Check for Spring 2022 references in the documents
spring_2022_projects = []
for i, doc in enumerate(civic_docs_data):
    text = doc.get('text', '')
    # Look for project information with Spring 2022 dates
    if '2022' in text and 'Spring' in text:
        spring_2022_projects.append({
            'doc_id': i,
            'filename': doc.get('filename'),
            'has_spring_2022': True
        })

print("Documents with '2022' and 'Spring':", len(spring_2022_projects))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
