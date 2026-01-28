code = """import json
import re

# Read the citations data for 2020
citations_file = locals()['var_functions.query_db:0']
citations_data = []
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Read the paper documents data
papers_file = locals()['var_functions.query_db:4']
papers_data = []
with open(papers_file, 'r') as f:
    papers_data = json.load(f)

# Extract title from filename and venue from text for each paper
paper_info = []
for paper in papers_data:
    filename = paper['filename']
    text = paper['text']
    
    # Extract title (filename without .txt)
    title = filename.replace('.txt', '')
    
    # Extract venue - look for CHI specifically
    venue = None
    chi_patterns = [
        r"CHI\s*'\d{2}",
        r"CHI\s*\d{4}",
        r"Proceedings of the .*?CHI",
        r"ACM Conference on Human Factors",
        r"Conference on Human Factors in Computing Systems"
    ]
    
    for pattern in chi_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            venue = "CHI"
            break
    
    # Only include papers where we identified CHI venue
    if venue == "CHI":
        paper_info.append({
            'title': title,
            'venue': venue
        })

# Create a dictionary for easy lookup by lowercase title
papers_dict = {p['title'].lower().strip(): p for p in paper_info}

# Find CHI papers cited in 2020
chi_citations = []
for citation in citations_data:
    cite_title = citation['title'].lower().strip()
    
    # Check if this title exists in our CHI papers
    if cite_title in papers_dict:
        chi_citations.append({
            'title': citation['title'],
            'citation_count': int(citation['citation_count']),
            'venue': 'CHI'
        })

# Calculate total citations for CHI papers
total_citations = sum(c['citation_count'] for c in chi_citations)
chi_papers_count = len(chi_citations)

result = {
    'total_citation_count': total_citations,
    'chi_papers_identified': chi_papers_count,
    'sample_chi_papers': chi_citations[:5]  # Show first 5 as sample
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
