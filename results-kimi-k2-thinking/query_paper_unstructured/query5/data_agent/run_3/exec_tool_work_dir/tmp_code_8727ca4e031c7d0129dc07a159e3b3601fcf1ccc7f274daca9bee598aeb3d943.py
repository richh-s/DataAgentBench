code = """import json, re, os
c_path = locals()['var_functions.query_db:7']
p_path = locals()['var_functions.query_db:8']

with open(c_path) as f:
    citations = json.load(f)

with open(p_path) as f:
    papers = json.load(f)

# Look at some actual data
print('Sample citations (first 20):')
for i, c in enumerate(citations[:20]):
    print(f"{i+1}. '{c.get('title')}' - year: {c.get('citation_year')}")

print('\nSample paper filenames (first 20):')
for i, p in enumerate(papers[:20]):
    print(f"{i+1}. '{p.get('filename')}'")

# Find CHI papers properly
print('\nSearching for CHI papers...')
chi_papers = []
for i, paper in enumerate(papers):
    filename = paper.get('filename', '').lower()
    text = paper.get('text', '').lower()
    
    # More precise CHI detection
    if 'chi' in filename:
        # Extract title from filename
        title = paper.get('filename', '').replace('.txt', '')
        
        # Try to find year in text
        year_match = re.search(r'(19|20)\d\d', paper.get('text', ''))
        year = year_match.group() if year_match else None
        
        chi_papers.append({
            'index': i,
            'title': title,
            'year': year,
            'filename': paper.get('filename')
        })

print(f'\nFound {len(chi_papers)} CHI papers (by filename):')
for p in chi_papers[:10]:
    print(f"  {p['title']}")

# Also check text content for CHI mentions
print('\nChecking for CHI in paper text...')
chi_in_text = []
for i, paper in enumerate(papers[:100]):  # Check first 100 papers
    text = paper.get('text', '').lower()
    if 'chi' in text and 'chi' not in paper.get('filename', '').lower():
        # Look for CHI with year pattern
        if re.search(r'chi\s*(19|20)\d\d', text) or 'conference on human factors' in text:
            title = paper.get('filename', '').replace('.txt', '')
            chi_in_text.append({'index': i, 'title': title})

print(f'Found {len(chi_in_text)} additional CHI papers (by text content):')
for p in chi_in_text[:5]:
    print(f"  {p['title']}")

# Now let's do careful matching
all_chi = chi_papers + chi_in_text
citations_2020 = [c for c in citations if c.get('citation_year') == 2020]

print(f'\nTotal CHI papers: {len(all_chi)}')
print(f'Total 2020 citations: {len(citations_2020)}')

# Try to match more carefully
matches = []
for citation in citations_2020:
    cite_title = citation.get('title', '').lower().strip()
    
    for paper in all_chi:
        paper_title = paper['title'].lower().strip()
        
        # More flexible matching
        if (paper_title == cite_title or 
            paper_title in cite_title or 
            cite_title in paper_title or
            paper_title.replace(' ', '') == cite_title.replace(' ', '') or
            paper_title.replace('-', ' ') == cite_title.replace('-', ' ')):
            matches.append({
                'paper_title': paper['title'],
                'citation_title': citation.get('title'),
                'citation_count': int(citation.get('citation_count', 0))
            })
            break

print(f'\nFound {len(matches)} matches:')
for m in matches[:10]:
    print(f"  {m['paper_title'][:60]}... - {m['citation_count']} citations")

total_citations = sum(m['citation_count'] for m in matches)

print('__RESULT__:')
print(json.dumps({
    'total_citations_2020': total_citations, 
    'papers_matched': len(matches),
    'total_chi_papers': len(all_chi)
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}], 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:18': {'total_chi_citations_2020': 0, 'chi_papers_counted': 0}, 'var_functions.execute_python:22': {'citations_type': "<class 'str'>", 'papers_type': "<class 'str'>"}, 'var_functions.execute_python:24': {'total_citations': 0, 'papers_matched': 0}, 'var_functions.execute_python:30': {'total_citations_2020': 0, 'chi_papers_counted': 0, 'total_chi_papers': 4}}

exec(code, env_args)
