code = """import json

# Get the file path from the stored variable
file_path = locals()['var_functions.query_db:2']
print("File path:", file_path)

# Read the actual MongoDB documents
with open(file_path, 'r') as f:
    docs = json.load(f)

print("Total documents loaded:", len(docs))
print("Sample document keys:", list(docs[0].keys()) if docs else "No documents")

# Extract project information from documents
all_projects = []

for doc in docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Simple parsing - look for project-like headings
    if 'text' in doc:
        all_projects.append({
            'filename': filename,
            'text_preview': text[:500]  # First 500 chars for inspection
        })

print("Documents with text:", len(all_projects))

# Return just a summary for now
result = {
    "total_docs": len(docs),
    "sample_keys": list(docs[0].keys()) if docs else [],
    "doc_preview": docs[0].get('text', '')[:300] if docs else ""
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:16': {'key': 'var_functions.query_db:2', 'type': "<class 'str'>", 'length': 38}}

exec(code, env_args)
