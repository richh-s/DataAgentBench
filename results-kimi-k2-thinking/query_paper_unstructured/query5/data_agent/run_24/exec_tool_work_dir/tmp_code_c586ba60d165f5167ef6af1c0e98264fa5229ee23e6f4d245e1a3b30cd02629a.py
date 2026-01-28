code = """import json

# Read the citations for 2020 using locals()
citations_file = locals()['var_functions.query_db:2']
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Read the papers from CHI using locals()
papers_file = locals()['var_functions.query_db:5']
with open(papers_file, 'r') as f:
    papers_data = json.load(f)

# Extract titles from CHI papers
chi_titles = []
for paper in papers_data:
    title = paper['filename'].replace('.txt', '')
    chi_titles.append(title)

# Match with citations and sum
total_citations = 0
matched_count = 0
for citation in citations_data:
    cit_title = citation['title']
    if cit_title in chi_titles:
        total_citations += int(citation['citation_count'])
        matched_count += 1

# Return the final result
result = {
    "matched_papers": matched_count,
    "total_citation_count": total_citations
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
