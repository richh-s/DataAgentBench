code = """import json

# Load data
citations_path = "var_functions.query_db:16"
try:
    with open(citations_path, 'r') as f:
        citations_2020 = json.load(f)
except Exception as e:
    print('Error loading citations:', e)
    citations_2020 = []

papers_path = "var_functions.query_db:2"
try:
    with open(papers_path, 'r') as f:
        papers = json.load(f)
except Exception as e:
    print('Error loading papers:', e)
    papers = []

# Extract CHI paper titles more carefully
def extract_chi_papers(docs):
    chi_papers = []
    for doc in docs:
        text = doc.get('text', '')
        filename = doc.get('filename', '')
        title = filename.replace('.txt', '')
        
        # Look for CHI venue markers in the text
        # Check first 100 lines for CHI reference
        lines = text.split('\n')[:100]
        is_chi = False
        publication_year = None
        
        for line in lines:
            # Look for patterns like CHI '20, CHI 2020, etc.
            if 'CHI' in line:
                # Check if this is a venue reference (not just a word)
                if any(marker in line for marker in ['Proceedings', 'Conference', 'ACM', 'paper', 'Paper']):
                    is_chi = True
                    # Try to extract year
                    import re
                    year_match = re.search(r'(20\d{2})', line)
                    if year_match:
                        publication_year = int(year_match.group(1))
                    break
        
        if is_chi:
            chi_papers.append({
                'title': title,
                'year': publication_year
            })
    
    return chi_papers

chi_papers = extract_chi_papers(papers)
chi_titles = {p['title'].lower(): p for p in chi_papers}

# Calculate total citations
total_citations = 0
count = 0
for cite in citations_2020:
    cite_title = cite.get('title', '')
    if cite_title and cite_title.lower() in chi_titles:
        citations = int(cite.get('citation_count', 0))
        total_citations += citations
        count += 1

result = {
    'total_citations': total_citations,
    'chi_papers_identified': len(chi_papers),
    'chi_papers_with_citations_in_2020': count
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'total_citations_from_chi_papers_in_2020': 0}}

exec(code, env_args)
