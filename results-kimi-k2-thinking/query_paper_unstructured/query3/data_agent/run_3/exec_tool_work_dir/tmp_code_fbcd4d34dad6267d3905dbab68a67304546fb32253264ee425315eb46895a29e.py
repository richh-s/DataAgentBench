code = """import json
import re

# Load the citations data from the file
citations_path = locals()['var_functions.query_db:26']
with open(citations_path, 'r') as f:
    citations = json.load(f)

print('Loaded', len(citations), 'citation records')
print('Sample citations (first 3):')
for i, cit in enumerate(citations[:3]):
    print(f"  {i+1}. {cit['title'][:50]}... - {cit['total_citations']} citations")

# Load the paper documents from the file
paper_docs_path = locals()['var_functions.query_db:28']
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

print('\nLoaded', len(paper_docs), 'paper documents')
print('Sample paper:')
first_paper = paper_docs[0]
print(f"  Filename: {first_paper['filename']}")
print(f"  Text preview: {first_paper['text'][:200]}...")

# Function to extract year from paper text
def extract_year(text):
    # Look for patterns like: 2017, '17, UBICOMP '17, CHI 2018, etc.
    # Search in the first 2000 characters where metadata usually appears
    text_start = text[:2000]
    
    # Pattern 1: Four digit year (most common)
    year_match = re.search(r'(\b20\d{2}\b)', text_start)
    if year_match:
        return int(year_match.group(1))
    
    # Pattern 2: Two digit year with apostrophe (e.g., '17)
    year_match = re.search(r"['`](\d{2})\b", text_start)
    if year_match:
        year = int(year_match.group(1))
        return 2000 + year if year < 50 else 1900 + year
    
    return None

# Function to check if paper has empirical contribution
def is_empirical(text):
    text_lower = text.lower()
    # Check for 'empirical' keyword in the text
    # This is a simple approach - could be refined
    return 'empirical' in text_lower

# Process papers: extract info and filter
empirical_papers_after_2016 = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename or not text:
        continue
    
    title = filename.replace('.txt', '')
    year = extract_year(text)
    empirical = is_empirical(text)
    
    if year and year > 2016 and empirical:
        empirical_papers_after_2016.append({
            'title': title,
            'year': year
        })

print(f"\nFound {len(empirical_papers_after_2016)} empirical papers published after 2016")

if empirical_papers_after_2016:
    print('\nSample papers:')
    for i, paper in enumerate(empirical_papers_after_2016[:5]):
        print(f"  {i+1}. ({paper['year']}) {paper['title'][:60]}...")

# Now join with citations to get total counts
# Create a dict for quick lookup of citation counts by title
citation_dict = {cit['title']: int(cit['total_citations']) for cit in citations}

# Match papers with their citations
results = []
matched_count = 0
for paper in empirical_papers_after_2016:
    title = paper['title']
    if title in citation_dict:
        total_citations = citation_dict[title]
        results.append({
            'title': title,
            'total_citations': total_citations
        })
        matched_count += 1

print(f"\nMatched {matched_count} papers with citation data")

# Sort by citation count descending
results.sort(key=lambda x: x['total_citations'], reverse=True)

print('\nTop results:')
for i, result in enumerate(results[:10]):
    print(f"  {i+1}. ({result['total_citations']} citations) {result['title'][:60]}...")

# Output final results
print('\n__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
