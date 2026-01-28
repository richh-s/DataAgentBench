code = """import json

# Read the full MongoDB query result
mongo_result_path = locals()['var_functions.query_db:2']
print("Reading MongoDB results from:", mongo_result_path)

# Read and parse the JSON file
with open(mongo_result_path, 'r') as f:
    papers = json.load(f)

print("Total number of papers in database:", len(papers))
if papers:
    print("First paper structure keys:", list(papers[0].keys()))
    sample = papers[0]
    print("\nSample paper filename:", sample.get('filename'))
    print("Sample paper text preview (first 500 chars):")
    print(sample.get('text', '')[:500])
else:
    print("No papers in database")

# Output data for storage
result_dict = {
    "paper_count": len(papers),
    "sample_keys": list(papers[0].keys()) if papers else [],
    "sample_filename": papers[0].get('filename') if papers else '',
    "sample_text_preview": papers[0].get('text', '')[:500] if papers else ''
}

print("__RESULT__:")
print(json.dumps(result_dict))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
