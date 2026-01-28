code = """import json

# Access the file paths
civic_docs_file = var_functions.query_db:4
funding_file = var_functions.query_db:5

# Read and parse the civic documents
with open(civic_docs_file, 'r') as f:
    content = f.read()
    # Try to parse as JSON array
    try:
        civic_docs = json.loads(content)
    except:
        # If that fails, try line-by-line
        civic_docs = []
        f.seek(0)
        for line in f:
            line = line.strip()
            if line:
                try:
                    civic_docs.append(json.loads(line))
                except:
                    pass

# Read and parse the funding data
with open(funding_file, 'r') as f:
    content = f.read()
    try:
        funding = json.loads(content)
    except:
        funding = []
        f.seek(0)
        for line in f:
            line = line.strip()
            if line:
                try:
                    funding.append(json.loads(line))
                except:
                    pass

print("__RESULT__:")
print(json.dumps({
    "civic_docs_count": len(civic_docs),
    "funding_count": len(funding),
    "first_doc_filename": civic_docs[0].get("filename") if civic_docs else "No data",
    "sample_funding": funding[:3]
}, default=str))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
