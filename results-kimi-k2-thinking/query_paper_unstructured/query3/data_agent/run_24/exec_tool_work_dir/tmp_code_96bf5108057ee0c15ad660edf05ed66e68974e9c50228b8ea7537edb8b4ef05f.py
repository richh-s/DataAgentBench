code = """import json
import re

# Read paper documents
paper_docs_path = var_functions.query_db:2
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

# Extract paper information from documents
papers_info = []
for doc in paper_docs:
    # Extract title from filename
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else 'Unknown Title'
    
    # Extract text for analysis
    text = doc.get('text', '')
    
    # Extract year - look for patterns like CHI 2017, Ubicomp 2018, etc.
    year = None
    # Find venue with year
    venue_pattern = r'(CHI|Ubicomp|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UBICOMP)\s+\'?"?\s*(20\d{2})'
    matches = re.findall(venue_pattern, text, re.IGNORECASE)
    
    if matches:
        year = int(matches[0][1])
    else:
        # Alternative: look for year in the first few lines
        lines = text.split('\n')[:10]
        for line in lines:
            year_match = re.search(r'20\d{2}', line)
            if year_match:
                year = int(year_match.group())
                break
    
    # Determine contribution type
    contribution = ''
    text_lower = text.lower()
    
    # Check if paper mentions empirical work
    if 'empirical' in text_lower:
        contribution = 'empirical'
    
    papers_info.append({
        'title': title,
        'year': year,
        'contribution': contribution
    })

# Read citations
citations_path = var_functions.query_db:3
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Create a dictionary to sum citations per paper
citation_sums = {}
for cit in citations:
    title = cit.get('title', '')
    count = int(cit.get('citation_count', 0))
    if title in citation_sums:
        citation_sums[title] += count
    else:
        citation_sums[title] = count

# Filter papers: empirical contribution and published after 2016
results = []
for paper in papers_info:
    if paper['year'] and paper['year'] > 2016 and paper['contribution'] == 'empirical':
        title = paper['title']
        if title in citation_sums:
            results.append({
                'title': title,
                'total_citation_count': citation_sums[title]
            })

# If no results, provide debug information
if not results:
    empirical_papers = [p for p in papers_info if p['contribution'] == 'empirical']
    empirical_after_2016 = [p for p in empirical_papers if p['year'] and p['year'] > 2016]
    
    titles_with_citations = set(citation_sums.keys())
    empirical_titles = set([p['title'] for p in empirical_after_2016])
    matching_titles = empirical_titles.intersection(titles_with_citations)
    
    results = {
        'debug': {
            'total_papers': len(papers_info),
            'empirical_papers': len(empirical_papers),
            'empirical_after_2016': len(empirical_after_2016),
            'titles_with_citations': len(titles_with_citations),
            'matching_titles': len(matching_titles)
        },
        'matching_titles': list(matching_titles)
    }

# Print result
print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json'}

exec(code, env_args)
