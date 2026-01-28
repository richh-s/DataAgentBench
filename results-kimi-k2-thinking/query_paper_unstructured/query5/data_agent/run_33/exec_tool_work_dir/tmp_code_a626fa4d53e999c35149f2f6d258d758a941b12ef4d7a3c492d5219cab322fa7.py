code = """import json
import re

# Load the paper data (CHI papers)
papers_file = var_functions.query_db:10
with open(papers_file.replace("'", ""), 'r') as f:
    papers_data = json.load(f)

# Load the citations data (2020 citations)
citations_file = var_functions.query_db:11
with open(citations_file.replace("'", ""), 'r') as f:
    citations_data = json.load(f)

# Create a dictionary of titles from citations for easy lookup
citations_dict = {}
for citation in citations_data:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    citations_dict[title.lower().strip()] = count

# Process paper data to identify CHI papers and get their citations
chi_papers_citations = []

for paper in papers_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '')
    
    # Check if it's a CHI paper - look for CHI venue in text or filename
    # Common patterns for CHI papers
    is_chi = False
    
    # Check filename contains CHI
    if 'chi' in filename.lower():
        is_chi = True
    
    # Check text contains CHI conference references
    if not is_chi:
        # Look for CHI patterns in the text
        chi_patterns = [
            r'CHI\s*\'\d{2}',  # CHI '15, CHI '16 etc
            r'CHI\s*\d{4}',   # CHI 2015, CHI 2016 etc
            r'Proceedings of the .*CHI',  # Proceedings of the ... CHI
            r'Conference on Human Factors',  # Full conference name
        ]
        
        for pattern in chi_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                is_chi = True
                break
    
    if is_chi:
        # Get citation count for 2020 if available
        citation_count = citations_dict.get(title.lower().strip(), 0)
        if citation_count > 0:
            chi_papers_citations.append({
                'title': title,
                'citation_count': citation_count
            })

# Calculate total citations
total_citations = sum(paper['citation_count'] for paper in chi_papers_citations)

print('__RESULT__:')
print(json.dumps({
    'total_chi_papers_with_citations': len(chi_papers_citations),
    'total_citation_count': total_citations,
    'chi_papers': chi_papers_citations
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:1': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
