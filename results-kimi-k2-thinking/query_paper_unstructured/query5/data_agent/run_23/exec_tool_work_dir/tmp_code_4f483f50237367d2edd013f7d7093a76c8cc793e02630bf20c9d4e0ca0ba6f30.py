code = """import json
import re

# Access the stored results directly
citations_2020 = var_functions.query_db:5
paper_docs = var_functions.query_db:9

print(f"Total 2020 citations records: {len(citations_2020)}")
print(f"Total paper documents: {len(paper_docs)}")

# Create mapping of paper titles to documents
paper_dict = {}
for doc in paper_docs:
    title = doc['filename'].replace('.txt', '')
    paper_dict[title] = doc

print(f"Number of papers mapped: {len(paper_dict)}")

# Find papers that were presented at CHI
chi_papers = []
for doc in paper_docs:
    text = doc['text']
    # Look for CHI conference patterns
    if re.search(r'\bCHI\s*\d{4}\b', text) or re.search(r'CHI\s+\d{2,4}', text):
        title = doc['filename'].replace('.txt', '')
        # Try to extract year from text
        year_match = re.search(r'CHI\s*[\'\']?\s*(\d{4})', text)
        year = year_match.group(1) if year_match else 'Unknown'
        chi_papers.append({
            'title': title,
            'year': year,
            'filename': doc['filename']
        })

print(f"CHI papers found: {len(chi_papers)}")
print(f"First 5 CHI papers: {chi_papers[:5]}")

# Now match with 2020 citations
chi_titles = set(p['title'] for p in chi_papers)
citations_to_match = {c['title']: int(c['citation_count']) for c in citations_2020}

print(f"\nSample citation titles: {list(citations_to_match.keys())[:5]}")
print(f"Sample CHI paper titles: {list(chi_titles)[:5]}")

# Find matches
matches = []
for chi_paper in chi_papers:
    chi_title = chi_paper['title']
    if chi_title in citations_to_match:
        matches.append({
            'title': chi_title,
            'citation_count': citations_to_match[chi_title],
            'year': chi_paper['year']
        })

print(f"\nFound {len(matches)} CHI papers with 2020 citations")
if matches:
    print(f"Total citations: {sum(m['citation_count'] for m in matches)}")
    print(f"Sample matches: {matches[:5]}")"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json'}

exec(code, env_args)
