code = """import json
import re

# Read the citations data for 2020
citations_file = var_functions.query_db:0
citations_data = []
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Read the paper documents data
papers_file = var_functions.query_db:4
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
    
    # Extract venue - look for common venue indicators in text
    venue = None
    
    # Look for CHI specifically
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
    
    # Also check for other common venues for completeness
    if not venue:
        other_venues = ["Ubicomp", "CSCW", "DIS", "PervasiveHealth", "WWW", "IUI", "OzCHI", "TEI", "AH", "UbiComp"]
        for v in other_venues:
            if re.search(rf"{v}\s*'\d{{2}}", text, re.IGNORECASE) or re.search(rf"{v}\s*\d{{4}}", text, re.IGNORECASE):
                venue = v
                break
    
    if venue:  # Only include papers where we could identify a venue
        paper_info.append({
            'title': title,
            'venue': venue,
            'text_preview': text[:200]  # For debugging
        })

# Create a dictionary for easy lookup by title
papers_dict = {p['title'].lower().strip(): p for p in paper_info}

# Find CHI papers cited in 2020
chi_citations = []
for citation in citations_data:
    cite_title = citation['title'].lower().strip()
    
    # Check if this title exists in our papers and is from CHI
    if cite_title in papers_dict and papers_dict[cite_title]['venue'] == 'CHI':
        chi_citations.append({
            'title': citation['title'],
            'citation_count': int(citation['citation_count']),
            'venue': papers_dict[cite_title]['venue']
        })

# Calculate total citations for CHI papers
total_citations = sum(c['citation_count'] for c in chi_citations)

# Also get the count of CHI papers
chi_papers_count = len(chi_citations)

result = {
    'total_citation_count': total_citations,
    'chi_papers_count': chi_papers_count,
    'chi_papers': chi_citations
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
