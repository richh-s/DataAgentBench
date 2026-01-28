code = """import json
import re

citation_path = locals()['var_functions.query_db:0']
mongodb_path = locals()['var_functions.query_db:2']

with open(citation_path, 'r') as f:
    citations = json.load(f)

with open(mongodb_path, 'r') as f:
    papers = json.load(f)

# Debug: check first few records
print(f"Total citations: {len(citations)}")
print(f"Total papers: {len(papers)}")
print(f"First 3 citation titles: {[c['title'] for c in citations[:3]]}")
print(f"First 3 paper filenames: {[p.get('filename') for p in papers[:3]]}")

# Extract paper info more carefully
paper_titles = []
for i, paper in enumerate(papers[:100]):  # Process a subset first
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = paper.get('text', '')
    
    # Find year - try multiple patterns
    year = None
    # Pattern 1: four digit year
    match = re.search(r'\b(201[7-9]|202[0-9])\b', text)
    if match:
        year = int(match.group(1))
    else:
        # Pattern 2: two digit year after venue (e.g., UBICOMP '15)
        match = re.search(r"\b(')(1[7-9]|2[0-9])\b", text)
        if match:
            year_num = int(match.group(2))
            year = 2000 + year_num if year_num < 50 else 1900 + year_num
    
    # Check for empirical
    has_empirical = 'empirical' in text.lower()
    
    # Extract venue
    venue_match = re.search(r'(CHI|Ubicomp|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UIST)', text)
    venue = venue_match.group(1) if venue_match else None
    
    if title and year and year > 2016 and has_empirical:
        paper_titles.append(title)
        if i < 10:  # Debug first few matches
            print(f"Match: {title}, Year: {year}, Empirical: {has_empirical}")

print(f"\nPapers with empirical and year>2016: {len(paper_titles)}")

# Check which of these are in citations
citation_titles = set(c['title'] for c in citations)
matched_titles = [t for t in paper_titles if t in citation_titles]
print(f"Matched with citations: {len(matched_titles)}")

# Get full results
all_paper_info = []
for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = paper.get('text', '')
    
    # Year extraction
    year = None
    match = re.search(r'\b(201[7-9]|202[0-9])\b', text)
    if match:
        year = int(match.group(1))
    else:
        match = re.search(r"\b(')(1[7-9]|2[0-9])\b", text)
        if match:
            year_num = int(match.group(2))
            year = 2000 + year_num if year_num < 50 else 1900 + year_num
    
    has_empirical = 'empirical' in text.lower()
    
    if title and year and year > 2016 and has_empirical:
        all_paper_info.append({'title': title, 'year': year})

# Full join
title_to_citations = {c['title']: int(c['total_citations']) for c in citations}
final_results = []

for paper in all_paper_info:
    citations_count = title_to_citations.get(paper['title'], 0)
    if citations_count > 0:
        final_results.append({
            'title': paper['title'],
            'year': paper['year'],
            'total_citations': citations_count
        })

final_results.sort(key=lambda x: x['total_citations'], reverse=True)

# Debug info
print(f"\nDebug: Total papers found: {len(all_paper_info)}")
print(f"Debug: Final results count: {len(final_results)}")

print('__RESULT__:')
print(json.dumps(final_results, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': []}

exec(code, env_args)
