code = """import json
import re

# Read paper documents
paper_docs_path = var_functions.query_db:18
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

# Read citation data
citations_path = var_functions.query_db:14
with open(citations_path, 'r') as f:
    citations = json.load(f)

print("Loading data...")
print(f"Paper documents: {len(paper_docs)}")
print(f"Citation records: {len(citations)}")

# Extract information from paper documents
def extract_paper_info(doc):
    text = doc['text']
    filename = doc['filename']
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '')
    
    # Extract year - look for patterns like YYYY
    year_match = re.search(r"'(\d{2})\b", text)
    year = None
    
    if year_match:
        year_val = int(year_match.group(1))
        # Handle years like '15 -> 2015, '16 -> 2016
        if year_val < 50:
            year = 2000 + year_val
        else:
            year = 1900 + year_val
    
    # Extract contribution type - look for empirical
    # Search for contribution keywords in the text
    has_empirical = 'empirical' in text.lower()
    
    return {
        'title': title,
        'year': year,
        'has_empirical': has_empirical,
        'filename': filename
    }

# Process all papers
papers = []
for doc in paper_docs:
    paper_info = extract_paper_info(doc)
    papers.append(paper_info)

print(f"Processed {len(papers)} papers")
print("Sample papers:")
for i, p in enumerate(papers[:5]):
    print(f"  {i+1}. {p['title'][:50]}... - Year: {p['year']}, Empirical: {p['has_empirical']}")

# Filter papers with empirical contribution after 2016
empirical_papers_2017_plus = [p for p in papers if p['has_empirical'] and p['year'] and p['year'] > 2016]

print(f"\nEmpirical papers after 2016: {len(empirical_papers_2017_plus)}")
for p in empirical_papers_2017_plus[:10]:
    print(f"  - {p['title'][:60]}... (Year: {p['year']})")"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:16': ['paper_docs'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
