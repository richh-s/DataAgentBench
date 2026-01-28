code = """import json
import re

# Get the data from storage variables
citations_data = []
papers_data = []

# Try to load citations data
try:
    citations_var = locals()['var_functions.query_db:5']
    if isinstance(citations_var, str) and citations_var.endswith('.json'):
        with open(citations_var, 'r') as f:
            citations_data = json.load(f)
    else:
        citations_data = citations_var
except:
    citations_data = []

# Try to load papers data
try:
    papers_var = locals()['var_functions.query_db:6']
    if isinstance(papers_var, str) and papers_var.endswith('.json'):
        with open(papers_var, 'r') as f:
            papers_data = json.load(f)
    else:
        papers_data = papers_var
except:
    papers_data = []

print('Loaded %d papers and %d citations' % (len(papers_data), len(citations_data)))

# Clean title function
def clean_title(title):
    if not title:
        return ''
    title = title.replace('.txt', '')
    title = title.lower()
    title = re.sub(r'[^a-z0-9\s]', ' ', title)
    title = re.sub(r'\s+', ' ', title.strip())
    stop = ['a','an','the','and','or','but','in','on','at','to','for','of','with','by','from']
    words = [w for w in title.split() if w not in stop]
    return ' '.join(words)

# Find CHI papers
chi_titles = []
for paper in papers_data:
    text = paper.get('text', '')
    if not text:
        continue
    # Check for CHI
    if 'CHI' in text or 'Human Factors in Computing Systems' in text:
        filename = paper.get('filename', '')
        title = filename.replace('.txt', '')
        chi_titles.append(clean_title(title))

print('Found %d CHI papers' % len(chi_titles))

# Process citations and sum for CHI papers
chi_citations = 0
counted = 0
for citation in citations_data:
    if not isinstance(citation, dict):
        continue
    cite_year = int(citation.get('citation_year', 0))
    if cite_year != 2020:
        continue
    title = citation.get('title', '')
    clean = clean_title(title)
    if clean in chi_titles:
        chi_citations += int(citation.get('citation_count', 0))
        counted += 1

print('Counted %d papers with 2020 citations' % counted)
print('Total citations: %d' % chi_citations)
print('__RESULT__:')
print(json.dumps({'total_citations': chi_citations, 'papers_count': counted}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
