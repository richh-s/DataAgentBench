code = """import json
import re

# Load Paper Docs Candidates
with open(locals()['var_function-call-4190209602007516202'], 'r') as f:
    papers = json.load(f)

print(f"Number of papers from Mongo: {len(papers)}")

# Print header of first 3 papers
for p in papers[:3]:
    print(f"--- Title: {p['filename']} ---")
    print(p['text'][:500])
    print("-------------------------------")

# Load Citations keys
with open(locals()['var_function-call-10263286268720561281'], 'r') as f:
    citations_data = json.load(f)
citation_titles = set(c['title'] for c in citations_data)

# Check if titles from papers exist in citations
matches = 0
for p in papers:
    t = p['filename'].replace('.txt', '')
    if t in citation_titles:
        matches += 1

print(f"Number of title matches with citations: {matches}")"""

env_args = {'var_function-call-4042789943322229169': ['paper_docs'], 'var_function-call-4042789943322227422': ['Citations', 'sqlite_sequence'], 'var_function-call-12606358993077835147': 'file_storage/function-call-12606358993077835147.json', 'var_function-call-9821348660880975822': 'file_storage/function-call-9821348660880975822.json', 'var_function-call-10263286268720561281': 'file_storage/function-call-10263286268720561281.json', 'var_function-call-4190209602007516202': 'file_storage/function-call-4190209602007516202.json', 'var_function-call-14190727982573706246': []}

exec(code, env_args)
