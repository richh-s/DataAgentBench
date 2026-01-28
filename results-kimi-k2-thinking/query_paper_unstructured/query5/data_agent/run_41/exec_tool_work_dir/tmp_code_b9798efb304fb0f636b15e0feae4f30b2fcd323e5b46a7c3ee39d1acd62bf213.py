code = """import json
import re

# Access the stored variables properly
citations_data_key = 'var_functions.query_db:0'
papers_data_key = 'var_functions.query_db:1'

# Read the citations data from 2020
citations_file = locals().get(citations_data_key)
citations_data = []
if isinstance(citations_file, str) and citations_file.endswith('.json'):
    with open(citations_file, 'r') as f:
        citations_data = json.load(f)
else:
    citations_data = locals().get(citations_data_key)

# Read the paper documents
papers_file = locals().get(papers_data_key)
papers_data = []
if isinstance(papers_file, str) and papers_file.endswith('.json'):
    with open(papers_file, 'r') as f:
        papers_data = json.load(f)
else:
    papers_data = locals().get(papers_data_key)

print(f"Total citations in 2020: {len(citations_data)}")
print(f"Total papers in MongoDB: {len(papers_data)}")

# Create a mapping of title to citation count for 2020
citations_map = {}
for citation in citations_data:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    citations_map[title.lower().strip()] = count

print(f"Citations map size: {len(citations_map)}")

# Extract CHI papers and their citation counts
chi_citation_total = 0
chi_paper_count = 0
chi_papers_with_citations = []

for paper in papers_data:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Check if this is a CHI paper by looking for CHI venue in the text
    # Look for patterns like "CHI", "Conference on Human Factors", etc.
    is_chi = False
    
    # Common patterns for CHI conference
    chi_patterns = [
        r'\bCHI\b',
        r'Conference on Human Factors in Computing Systems',
        r'Human Factors in Computing Systems',
        r'CHI \d{4}'
    ]
    
    for pattern in chi_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            is_chi = True
            break
    
    if is_chi:
        # Check if this paper has citations in 2020
        citation_count = citations_map.get(title.lower().strip(), 0)
        if citation_count > 0:
            chi_citation_total += citation_count
            chi_paper_count += 1
            chi_papers_with_citations.append({
                'title': title,
                'citations': citation_count
            })

print(f"CHI papers with 2020 citations: {chi_paper_count}")
print(f"Total citation count for CHI papers in 2020: {chi_citation_total}")

result = {
    'total_citation_count': chi_citation_total,
    'chi_papers_count': chi_paper_count,
    'chi_papers_with_citations': chi_papers_with_citations
}

# Print the result
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)
