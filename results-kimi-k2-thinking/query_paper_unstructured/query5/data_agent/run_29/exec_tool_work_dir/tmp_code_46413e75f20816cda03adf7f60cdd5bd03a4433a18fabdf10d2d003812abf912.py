code = """import json
import re

# Load the citation data from the file
citations_file_path = var_functions.query_db:2
with open(citations_file_path, 'r') as f:
    citations_data = json.load(f)

# Load the paper documents from the file
papers_file_path = var_functions.query_db:6
with open(papers_file_path, 'r') as f:
    papers_data = json.load(f)

# Debug: Print sizes
print(f"Total citations for 2020: {len(citations_data)}")
print(f"Total papers in MongoDB: {len(papers_data)}")

# Extract paper information from MongoDB documents
paper_info = []
for doc in papers_data:
    filename = doc['filename']
    text = doc.get('text', '')
    
    # Extract title (filename without .txt)
    title = filename.replace('.txt', '')
    
    # Extract venue - look for common conference abbreviations
    # Common patterns: CHI, UbiComp, CSCW, DIS, etc.
    venue = None
    text_upper = text.upper()
    
    # Check for CHI specifically
    if 'CHI' in text_upper or 'CHI ' in text or 'Conference on Human Factors' in text:
        venue = 'CHI'
    elif 'UBICOMP' in text_upper or 'UbiComp' in text:
        venue = 'UbiComp'
    elif 'CSCW' in text_upper:
        venue = 'CSCW'
    elif 'DIS' in text_upper:
        venue = 'DIS'
    elif 'PERVASIVEHEALTH' in text_upper:
        venue = 'PervasiveHealth'
    elif 'PERVASIVE' in text_upper and 'HEALTH' in text_upper:
        venue = 'PervasiveHealth'
    elif 'WWW' in text_upper:
        venue = 'WWW'
    elif 'IUI' in text_upper:
        venue = 'IUI'
    elif 'OZCHI' in text_upper:
        venue = 'OzCHI'
    elif 'TEI' in text_upper:
        venue = 'TEI'
    elif 'AH' in text_upper and re.search(r'\bAH\b', text):
        venue = 'AH'
    
    # Extract year from text - look for patterns like 20XX, 19XX or specific year mentions
    year_match = re.search(r'(20\d{2}|19\d{2})', text)
    year = int(year_match.group(1)) if year_match else None
    
    # Extract source (publisher) - look for ACM, IEEE, PubMed
    source = None
    if 'ACM' in text_upper:
        source = 'ACM'
    elif 'IEEE' in text_upper:
        source = 'IEEE'
    elif 'PUBMED' in text_upper or 'PubMed' in text:
        source = 'PubMed'
    
    paper_info.append({
        'title': title,
        'venue': venue,
        'year': year,
        'source': source,
        'text': text[:1000]  # Store first 1000 chars for debugging
    })

# Debug: Show some extracted papers
print(f"Extracted paper info for {len(paper_info)} papers")
chi_papers = [p for p in paper_info if p['venue'] == 'CHI']
print(f"CHI papers found: {len(chi_papers)}")

# Create a lookup dictionary for paper info by title
paper_lookup = {p['title']: p for p in paper_info}

# Find CHI papers that have citations in 2020
chi_citations_2020 = []
for citation in citations_data:
    citation_title = citation['title']
    citation_count = int(citation['citation_count'])
    citation_year = int(citation['citation_year'])
    
    # Check if this paper is in our paper info and is CHI
    if citation_title in paper_lookup:
        paper = paper_lookup[citation_title]
        if paper['venue'] == 'CHI' and citation_year == 2020:
            chi_citations_2020.append({
                'title': citation_title,
                'citation_count': citation_count,
                'venue': paper['venue'],
                'paper_year': paper['year']
            })

# Debug: Show CHI papers with 2020 citations
print(f"\nCHI papers cited in 2020: {len(chi_citations_2020)}")
for paper in chi_citations_2020[:5]:  # Show first 5
    print(f"  - {paper['title']}: {paper['citation_count']} citations")

# Calculate total citation count
total_citations = sum(p['citation_count'] for p in chi_citations_2020)

print('__RESULT__:')
print(json.dumps({
    'chi_papers_count': len(chi_citations_2020),
    'total_citation_count': total_citations,
    'chi_papers': chi_citations_2020
}))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
