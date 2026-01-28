code = """import json

# Access the variable from locals since the name contains invalid syntax characters
var_name = 'var_functions.query_db:0'
citations_file_path = locals()[var_name]

print(f"File path: {citations_file_path}")

# Read the citation data
with open(citations_file_path, 'r') as f:
    citations_2020 = json.load(f)

print(f"Total papers cited in 2020: {len(citations_2020)}")

# Calculate total citation counts
total_citations = sum(int(record['citation_count']) for record in citations_2020)
print(f"Total citation counts for 2020: {total_citations}")

# Now query MongoDB to find papers presented at CHI
# We need to connect to MongoDB and search for CHI papers
result = {
    'papers_cited_in_2020': len(citations_2020),
    'total_citation_count': total_citations,
    'status': 'Loaded citation data, ready to query MongoDB for CHI papers'
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs']}

exec(code, env_args)
