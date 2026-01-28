code = """import json

# Read the citation data for 2020
citation_file = var_functions.query_db:2
with open(citation_file, 'r') as f:
    citations_data = json.load(f)

# Read the paper documents
paper_file = var_functions.query_db:5
with open(paper_file, 'r') as f:
    paper_docs = json.load(f)

print(f"Total citation records for 2020: {len(citations_data)}")
print(f"Total paper documents: {len(paper_docs)}")

# Helper function to extract venue from paper text
import re

def extract_venue(text, filename):
    # Look for venue patterns in the first few lines
    lines = text.split('\n')[:10]  # Check first 10 lines
    text_start = ' '.join(lines)
    
    # Common venue patterns
    patterns = [
        r"CHI\s+'\d{2}",
        r"CSCW\s+'\d{2}",
        r"UbiComp\s+'\d{2}",
        r"Ubicomp\s+'\d{2}",
        r"DIS\s+'\d{2}",
        r"PervasiveHealth\s+'\d{2}",
        r"WWW\s+'\d{2}",
        r"IUI\s+'\d{2}",
        r"OzCHI\s+'\d{2}",
        r"TEI\s+'\d{2}",
        r"AH\s+'\d{2}"
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text_start, re.IGNORECASE)
        if match:
            venue = match.group(0).split("'")[0].strip().upper()
            return venue
    
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
print(f"Total CHI papers found: {len(chi_papers)}")

# Create title to citation count mapping
citation_map = {item['title']: int(item['citation_count']) for item in citations_data}

# Match CHI papers with citations and sum
total_citations = 0
matched_count = 0
for paper in chi_papers:
    title = paper['title']
    if title in citation_map:
        total_citations += citation_map[title]
        matched_count += 1

print(f"Matched {matched_count} CHI papers with citation data")
print(f"Total citations for CHI papers in 2020: {total_citations}")

print('__RESULT__:')
print(json.dumps({"total_citations": total_citations, "matched_papers": matched_count}))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
