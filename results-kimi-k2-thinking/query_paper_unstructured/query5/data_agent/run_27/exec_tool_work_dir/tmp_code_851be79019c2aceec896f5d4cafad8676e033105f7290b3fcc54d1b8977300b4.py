code = """import json

# Read the full data
citation_path = locals()['var_functions.query_db:0']
with open(citation_path, 'r') as f:
    citations_2020 = json.load(f)

paper_path = locals()['var_functions.query_db:2']
with open(paper_path, 'r') as f:
    paper_docs = json.load(f)

# Filter for CHI papers
chi_papers = []
for doc in paper_docs:
    text = doc.get('text', '').upper()
    # Check if it's a CHI paper
    if 'CHI' in text and ('HUMAN FACTORS IN COMPUTING SYSTEMS' in text or 'HUMAN FACTORS IN COMPUTING SYSTEMS' in text):
        title = doc['filename'].replace('.txt', '')
        chi_papers.append(title)

# Create a set for faster lookup
chi_paper_titles = set(chi_papers)

# Match with citations and sum total
total_citations = 0
matched_papers = 0
matched_citations = []

for cit in citations_2020:
    cit_title = cit['title']
    if cit_title in chi_paper_titles:
        citation_count = int(cit['citation_count'])
        total_citations += citation_count
        matched_papers += 1
        matched_citations.append({
            'title': cit_title,
            'citations': citation_count
        })

print('__RESULT__:')
print(json.dumps({
    'total_citations_2020': total_citations,
    'chi_papers_with_citations': matched_papers,
    'matched_papers': matched_citations
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': {'citation_records_2020': 100, 'paper_documents': 5}}

exec(code, env_args)
