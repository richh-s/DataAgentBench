code = """import json

# Read the citation data for 2018
citation_file = locals()['var_functions.query_db:2']
with open(citation_file, 'r') as f:
    citations_2018 = json.load(f)

# Read all paper documents
paper_docs_file = locals()['var_functions.query_db:12']
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Create a dictionary mapping paper titles to their citation counts for 2018
citation_dict = {item['title'].lower(): int(item['citation_count']) for item in citations_2018}

# Identify ACM papers and collect their citation counts for 2018
acm_citation_counts = []
acm_papers_found = []

for paper in paper_docs:
    # Check if paper is from ACM
    text = paper.get('text', '').lower()
    if 'acm' in text:
        # Extract title from filename
        filename = paper.get('filename', '')
        if filename.endswith('.txt'):
            title = filename[:-4].lower()  # Remove .txt and convert to lowercase
            
            # Check if this paper has citations in 2018
            if title in citation_dict:
                acm_citation_counts.append(citation_dict[title])
                acm_papers_found.append({
                    'title': filename[:-4],
                    'citations_2018': citation_dict[title]
                })

# Calculate average citation count
result = {
    'total_acm_papers_with_citations': len(acm_citation_counts),
    'acm_citation_counts': acm_citation_counts,
    'average_citations': sum(acm_citation_counts) / len(acm_citation_counts) if acm_citation_counts else 0
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': 'Loaded 158 citation records for 2018', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': 'Loaded 158 citation records for 2018 and 5 paper documents', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
