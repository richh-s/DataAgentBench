code = """import json
import re

# Load the data from stored results
citations_2020 = var_functions.query_db:5
paper_docs = var_functions.query_db:9

# Create a dictionary of 2020 citations by title
citations_by_title = {}
for citation in citations_2020:
    title = citation['title']
    count = int(citation['citation_count'])
    citations_by_title[title] = count

print(f"Total 2020 citation records: {len(citations_2020)}")
print(f"Unique papers with 2020 citations: {len(citations_by_title)}")

# Function to check if a paper was presented at CHI
def is_chi_paper(doc):
    text = doc['text']
    # Look for CHI conference patterns like "CHI '15", "CHI 2015", "CHI'15", etc.
    chi_patterns = [
        r"CHI\s*['`]\s*\d{2}",
        r"CHI\s*\d{4}",
        r"CHI\s+Conference",
        r"Proceedings of CHI",
        r"ACM\s+CHI"
    ]
    
    for pattern in chi_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            return True
    return False

# Find all CHI papers
chi_papers = []
for doc in paper_docs:
    if is_chi_paper(doc):
        title = doc['filename'].replace('.txt', '')
        chi_papers.append(title)

print(f"Total CHI papers found: {len(chi_papers)}")

# Match CHI papers with 2020 citations
matched_papers = []
total_citations = 0

for chi_title in chi_papers:
    if chi_title in citations_by_title:
        count = citations_by_title[chi_title]
        matched_papers.append({
            'title': chi_title,
            'citations_2020': count
        })
        total_citations += count

print(f"CHI papers with 2020 citations: {len(matched_papers)}")
print(f"Total citation count: {total_citations}")

# Show some examples
if matched_papers:
    print(f"Example matched papers: {matched_papers[:3]}")

__RESULT__ = total_citations
print("__RESULT__:")
print(json.dumps(__RESULT__))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json'}

exec(code, env_args)
