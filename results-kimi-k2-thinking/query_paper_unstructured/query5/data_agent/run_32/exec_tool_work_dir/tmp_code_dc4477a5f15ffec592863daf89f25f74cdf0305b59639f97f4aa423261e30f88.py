code = """import json

# Load data
citations_path = "var_functions.query_db:16"
try:
    with open(citations_path, 'r') as f:
        citations_2020 = json.load(f)
except Exception as e:
    print('Error loading citations:', e)
    citations_2020 = []

papers_path = "var_functions.query_db:2"
try:
    with open(papers_path, 'r') as f:
        papers = json.load(f)
except Exception as e:
    print('Error loading papers:', e)
    papers = []

# Function to check if paper is CHI
def is_chi_paper(doc):
    text = doc.get('text', '')
    # Simple check for CHI in first 2000 characters
    header = text[:2000].upper()
    return 'CHI' in header and ("'" in text[:2000] or '20' in text[:2000])

# Get CHI paper titles
chi_titles = set()
for paper in papers:
    if is_chi_paper(paper):
        filename = paper.get('filename', '')
        title = filename.replace('.txt', '')
        chi_titles.add(title.lower())

# Sum citations for CHI papers
total_citations = 0
for cite in citations_2020:
    cite_title = cite.get('title', '')
    if cite_title and cite_title.lower() in chi_titles:
        count = int(cite.get('citation_count', 0))
        total_citations += count

print('__RESULT__:')
print(json.dumps({'total_citations_from_chi_papers_in_2020': total_citations}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
