code = """import json
import re

# Read the citations data
citations_file = var_functions.query_db:5
citations_data = json.loads(open(citations_file).read())

# Read the paper documents data
papers_file = var_functions.query_db:6
papers_data = json.loads(open(papers_file).read())

# Add title field from filename
for paper in papers_data:
    if 'filename' in paper:
        paper['title'] = paper['filename'].replace('.txt', '')

# Function to extract metadata from text
def extract_info(text):
    info = {'year': None, 'venue': [], 'source': [], 'contribution': [], 'domain': []}
    
    # Extract year
    year_match = re.search(r'\b(20\d{2})\b', text)
    if year_match:
        info['year'] = int(year_match.group(1))
    
    # Extract venues
    venues = re.findall(r'(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)', text, re.IGNORECASE)
    info['venue'] = list(set([v.upper() for v in venues]))
    
    # Extract sources
    sources = re.findall(r'(ACM|IEEE|PubMed)', text, re.IGNORECASE)
    info['source'] = list(set([s.upper() for s in sources]))
    
    # Extract contributions
    contributions = re.findall(r'(empirical|artifact|theoretical|survey|methodological)', text, re.IGNORECASE)
    info['contribution'] = list(set([c.lower() for c in contributions]))
    
    # Extract domains
    domains = ['food', 'physical activity', 'sleep', 'mental', 'finances', 'productivity', 'screen time', 'social interactions', 'location', 'chronic', 'diabetes', 'health_behavior']
    text_lower = text.lower()
    for domain in domains:
        if domain in text_lower:
            info['domain'].append(domain)
    info['domain'] = list(set(info['domain']))
    
    return info

# Extract metadata for all papers
for paper in papers_data:
    if 'text' in paper:
        paper.update(extract_info(paper['text']))

# Filter for empirical papers published after 2016
empirical_papers = [p for p in papers_data if p.get('year') and p['year'] > 2016 and 'empirical' in p.get('contribution', [])]

# Build citation dictionary for fast lookup
citation_dict = {}
for cite in citations_data:
    title = cite['title']
    if title not in citation_dict:
        citation_dict[title] = 0
    citation_dict[title] += int(cite['citation_count'])

# Calculate total citations for empirical papers
results = []
for paper in empirical_papers:
    title = paper['title']
    total_citations = citation_dict.get(title, 0)
    results.append({'title': title, 'total_citations': total_citations, 'year': paper['year']})

# Sort by citations descending
results_sorted = sorted(results, key=lambda x: x['total_citations'], reverse=True)

print('__RESULT__:')
print(json.dumps(results_sorted[0:10]))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
