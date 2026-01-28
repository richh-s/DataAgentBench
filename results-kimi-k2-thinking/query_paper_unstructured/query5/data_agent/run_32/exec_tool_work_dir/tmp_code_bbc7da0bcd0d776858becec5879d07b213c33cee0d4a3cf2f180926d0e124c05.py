code = """import json
import re

# Load citations data
citations_path = "var_functions.query_db:16"
try:
    with open(citations_path, 'r') as f:
        citations_2020 = json.load(f)
except Exception as e:
    print('Error loading citations:', e)
    citations_2020 = []

# Load papers data
papers_path = "var_functions.query_db:2"
try:
    with open(papers_path, 'r') as f:
        papers = json.load(f)
except Exception as e:
    print('Error loading papers:', e)
    papers = []

# Function to extract paper info
def extract_paper_info(doc):
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Look for venue and year in first 30 lines
    lines = text.split('\n')[:30]
    venue = None
    year = None
    
    for line in lines:
        line_upper = line.upper()
        # Check for CHI
        if re.search(r'\bCHI\b', line_upper):
            venue = 'CHI'
            # Try to find year in same line
            year_match = re.search(r'\b(20\d{2})\b|\b(\d{2})\b', line)
            if year_match:
                yr = year_match.group(1) or year_match.group(2)
                if len(yr) == 2:
                    year = int('20' + yr)
                else:
                    year = int(yr)
            break
    
    if venue == 'CHI':
        return {'title': title, 'venue': venue, 'year': year}
    return None

# Extract CHI papers
chi_papers = []
for paper in papers:
    info = extract_paper_info(paper)
    if info:
        chi_papers.append(info)

# Create dictionary of CHI paper titles for lookup
chi_titles = {p['title'].lower(): p for p in chi_papers}

# Sum citations for CHI papers cited in 2020
total_citations = 0
chi_citations = []

for cite in citations_2020:
    cite_title = cite.get('title', '')
    if cite_title and cite_title.lower() in chi_titles:
        count = int(cite.get('citation_count', 0))
        total_citations += count
        chi_citations.append({
            'title': cite_title,
            'citations': count,
            'venue': 'CHI'
        })

print('__RESULT__:')
print(json.dumps({
    'total_citation_count': total_citations,
    'chi_citation_details': chi_citations[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
