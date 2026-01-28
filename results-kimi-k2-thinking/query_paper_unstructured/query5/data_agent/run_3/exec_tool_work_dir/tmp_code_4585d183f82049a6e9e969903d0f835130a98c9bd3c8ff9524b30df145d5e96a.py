code = """import json, re, sys, os

# Get file paths from storage
citations_path = var_functions.query_db:7
papers_path = var_functions.query_db:8

# Load citations data
if isinstance(citations_path, str) and os.path.exists(citations_path):
    with open(citations_path, 'r') as f:
        citations_data = json.load(f)
else:
    citations_data = citations_path

# Load papers data  
if isinstance(papers_path, str) and os.path.exists(papers_path):
    with open(papers_path, 'r') as f:
        papers_data = json.load(f)
else:
    papers_data = papers_path

print('Citations:', len(citations_data))
print('Papers:', len(papers_data))
print('Sample citation:', citations_data[0])
print('Sample paper filename:', papers_data[0].get('filename'))

# Find CHI papers
chi_papers = []
for paper in papers_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '').lower()
    if 'chi' in filename.lower() or 'chi' in text:
        title = filename.replace('.txt', '')
        year_match = re.search(r'(20\d\d)', text)
        year = year_match.group(1) if year_match else None
        chi_papers.append({'title': title, 'year': year, 'filename': filename})

print('CHI papers found:', len(chi_papers))
if chi_papers:
    print('First CHI paper:', chi_papers[0])

# Match citations with CHI papers
citations_2020 = [c for c in citations_data if c.get('citation_year') == 2020]
print('2020 citations:', len(citations_2020))

# Create title mapping
citation_titles = {c.get('title', '').lower(): c for c in citations_2020}
chi_citations = []

for paper in chi_papers:
    paper_title = paper['title'].lower()
    if paper_title in citation_titles:
        citation_info = citation_titles[paper_title]
        chi_citations.append({
            'title': paper['title'],
            'citation_count': citation_info.get('citation_count'),
            'year': paper['year']
        })

print('Direct title matches found:', len(chi_citations))

# Check other matching approaches if direct match fails
if len(chi_citations) < 10:  # If very few matches, try substring matching
    paper_titles = {paper['title'].lower(): paper for paper in chi_papers}
    for citation in citations_2020:
        cite_title = citation.get('title', '').lower()
        for paper_title, paper in paper_titles.items():
            if cite_title in paper_title or paper_title in cite_title:
                chi_citations.append({
                    'title': paper['title'],
                    'citation_count': citation.get('citation_count'),
                    'year': paper['year']
                })
                break

print('Total CHI matches:', len(chi_citations))

# Sum citation counts
total_citations = 0
for item in chi_citations:
    count = item.get('citation_count')
    if count:
        total_citations += int(count)

print('Total citation count for CHI papers in 2020:', total_citations)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}], 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
