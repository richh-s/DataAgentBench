code = """import json
import os

# Read the citations for 2020
citations_file = var_functions.query_db:2
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

print(f"Total 2020 citations records: {len(citations_data)}")
print(f"First few records: {citations_data[:3]}")

# Read the papers from CHI
papers_file = var_functions.query_db:5
with open(papers_file, 'r') as f:
    papers_data = json.load(f)

print(f"Total CHI papers: {len(papers_data)}")
print(f"First few papers: {papers_data[:3]}")

# Extract titles from CHI papers
chi_titles = []
for paper in papers_data:
    title = paper['filename'].replace('.txt', '')
    chi_titles.append(title)

print(f"Extracted {len(chi_titles)} titles from CHI papers")
print(f"First few titles: {chi_titles[:5]}")

# Match with citations and sum
total_citations = 0
matched_count = 0

for citation in citations_data:
    cit_title = citation['title']
    if cit_title in chi_titles:
        total_citations += int(citation['citation_count'])
        matched_count += 1
        # Debug: print first few matches
        if matched_count <= 3:
            print(f"Match found: {cit_title} - {citation['citation_count']} citations")

print(f"\nMatched {matched_count} papers")
print(f"Total citations: {total_citations}")

# Return the final result
result = {
    "matched_papers": matched_count,
    "total_citation_count": total_citations
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
