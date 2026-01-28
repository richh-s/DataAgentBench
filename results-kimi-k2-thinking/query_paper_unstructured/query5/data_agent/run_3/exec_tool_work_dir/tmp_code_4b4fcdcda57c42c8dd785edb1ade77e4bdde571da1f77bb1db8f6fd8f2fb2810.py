code = """import json
import re

citations_path = locals()['var_functions.query_db:7']
papers_path = locals()['var_functions.query_db:8']

with open(citations_path, 'r') as f:
    citations = json.load(f)

with open(papers_path, 'r') as f:
    papers = json.load(f)

print('Sample citation titles:')
for i, c in enumerate(citations[:10]):
    print(f"  {i+1}. '{c.get('title')}'")

print('\nSample paper filenames:')
for i, p in enumerate(papers[:10]):
    print(f"  {i+1}. '{p.get('filename')}'")

print('\nLooking for CHI in papers...')
chi_papers = []
for paper in papers[:100]:  # Check first 100
    filename = paper.get('filename', '')
    text = paper.get('text', '').lower()
    
    # Look for CHI-related patterns
    if 'chi' in filename.lower():
        chi_papers.append(paper)
    elif re.search(r'chi\s*\d{2,4}|conference on human factors', text, re.IGNORECASE):
        chi_papers.append(paper)

print(f'Found {len(chi_papers)} potential CHI papers in first 100')
for p in chi_papers[:5]:
    print(f"  Filename: {p.get('filename')}")

# Let's check some specific examples
print('\nChecking specific matches...')
citation_titles = [c.get('title', '').lower() for c in citations[:50]]
paper_titles = [p.get('filename', '').replace('.txt', '').lower() for p in papers[:50]]

common = set(citation_titles) & set(paper_titles)
print(f'Direct title matches in first 50: {len(common)}')

# Check if any CHI papers have citations in 2020
chi_filenames = {p.get('filename', '').replace('.txt', '').lower() for p in chi_papers}
chi_2020 = []

for citation in citations:
    if citation.get('citation_year') == 2020:
        cite_title = citation.get('title', '').lower()
        if cite_title in chi_filenames:
            chi_2020.append(int(citation.get('citation_count', 0)))

print(f'CHI papers cited in 2020: {len(chi_2020)}')
print(f'Total citations: {sum(chi_2020)}')

print('\nLet me try a broader search...')
# Try to find any papers with venue info that includes CHI
all_chi = []
for paper in papers:
    text = paper.get('text', '').lower()
    if 'chi' in text or 'conference on human factors' in text:
        title = paper.get('filename', '').replace('.txt', '')
        year_match = re.search(r'20\d\d', text)
        year = year_match.group() if year_match else None
        
        # Try to extract venue line
        lines = text.split('\n')
        venue = None
        for line in lines[:10]:  # Check first 10 lines
            if 'chi' in line.lower():
                venue = line.strip()
                break
        
        all_chi.append({
            'title': title,
            'year': year,
            'venue_snippet': venue
        })

print(f'Found {len(all_chi)} papers mentioning CHI')
for p in all_chi[:3]:
    print(f"  {p}")"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}], 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:18': {'total_chi_citations_2020': 0, 'chi_papers_counted': 0}, 'var_functions.execute_python:22': {'citations_type': "<class 'str'>", 'papers_type': "<class 'str'>"}, 'var_functions.execute_python:24': {'total_citations': 0, 'papers_matched': 0}}

exec(code, env_args)
