code = """import json
import re

# Read the citation data for 2020
citation_file = var_functions.query_db:2
with open(citation_file, 'r') as f:
    citations_data = json.load(f)

# Read the paper documents
paper_file = var_functions.query_db:5
with open(paper_file, 'r') as f:
    paper_docs = json.load(f)

print('Total citation records for 2020:', len(citations_data))
print('Total paper documents:', len(paper_docs))

# Helper function to extract venue from paper text
def extract_venue(text, filename):
    # Look for venue patterns in the first few lines
    lines = text.split('\n')[:10]
    text_start = ' '.join(lines)
    
    # Check for CHI specifically first - using simple string find
    if 'CHI' in text_start:
        # Check if it's followed by year pattern
        chi_pattern = re.compile(r"CHI\s+'\d{2}", re.IGNORECASE)
        if chi_pattern.search(text_start):
            return 'CHI'
    
    return None

# Extract paper information
papers_info = []
for doc in paper_docs:
    title = doc['filename'].replace('.txt', '')
    text = doc['text']
    venue = extract_venue(text, doc['filename'])
    papers_info.append({
        'title': title,
        'venue': venue
    })

# Filter for CHI papers
chi_papers = [p for p in papers_info if p['venue'] == 'CHI']
print('Total CHI papers found:', len(chi_papers))

# Create title to citation count mapping
citation_map = {}
for item in citations_data:
    citation_map[item['title']] = int(item['citation_count'])

# Match CHI papers with citations and sum
total_citations = 0
matched_count = 0
for paper in chi_papers:
    title = paper['title']
    if title in citation_map:
        total_citations += citation_map[title]
        matched_count += 1

print('Matched CHI papers with citation data:', matched_count)
print('Total citations for CHI papers in 2020:', total_citations)

result = {'total_citations': total_citations, 'matched_papers': matched_count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
