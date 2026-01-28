code = """import json
import re

# Load the full result from the file
with open('/tmp/tmp_d5q7p7j.json', 'r') as f:
    documents = json.load(f)

print(f"Number of documents: {len(documents)}")

# Extract project information from documents
projects = []
for doc_idx, doc in enumerate(documents):
    text = doc['text']
    filename = doc['filename']
    
    # Look for project information patterns
    # Common patterns: project names, dates, etc.
    
    # Search for Spring 2022 mentions
    spring_2022_patterns = [
        r'Spring\s+2022',
        r'2022-Spring',
        r'2022.*Spring'
    ]
    
    if any(re.search(pattern, text, re.IGNORECASE) for pattern in spring_2022_patterns):
        projects.append({
            'doc_idx': doc_idx,
            'filename': filename,
            'text_snippet': text[:500]
        })

print(f"Documents mentioning Spring 2022: {len(projects)}")
for p in projects[:3]:
    print(f"\n--- Document {p['doc_idx']}: {p['filename']} ---")
    print(p['text_snippet'][:500])

print("__RESULT__:")
print(json.dumps(projects))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
