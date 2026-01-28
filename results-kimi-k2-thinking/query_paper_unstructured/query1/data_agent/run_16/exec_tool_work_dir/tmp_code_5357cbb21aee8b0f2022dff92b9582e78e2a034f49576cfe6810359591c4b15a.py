code = """import json
import re

# Load the data paths
paper_docs_path = locals()['var_functions.query_db:6']
citations_path = locals()['var_functions.query_db:12']

# Read full data
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

with open(citations_path, 'r') as f:
    citations = json.load(f)

print(f"Total papers: {len(paper_docs)}")
print(f"Total citation records: {len(citations)}")

# First, let's find papers that contain 'food' in their text
food_papers = []
for doc in paper_docs:
    text_lower = doc['text'].lower()
    if 'food' in text_lower:
        title = doc['filename'].replace('.txt', '')
        # Try to extract year
        year_match = re.search(r'\b(200[0-9]|201[0-9]|202[0-9])\b', text_lower)
        year = int(year_match.group(0)) if year_match else None
        
        # Try to extract venue
        venue_match = re.search(r'\b(chi|ubicomp|cscw|dis|pervasivehealth|www|iui|ozchi|tei|ah)\b', text_lower)
        venue = venue_match.group(0).upper() if venue_match else ''
        
        food_papers.append({
            'title': title,
            'year': year,
            'venue': venue,
            'filename': doc['filename']
        })

print(f"Papers with 'food' in text: {len(food_papers)}")
print("Sample food papers:", food_papers[:5])

# Check which food papers have citations
citation_titles = {c['title'].lower(): int(c['total_citations']) for c in citations}

food_papers_with_citations = []
total_citations = 0
for paper in food_papers:
    paper_title_lower = paper['title'].lower()
    # Try exact match first
    if paper_title_lower in citation_titles:
        citations_count = citation_titles[paper_title_lower]
        food_papers_with_citations.append({
            'title': paper['title'],
            'citations': citations_count
        })
        total_citations += citations_count
    else:
        # Try fuzzy matching
        for cit_title, cit_count in citation_titles.items():
            if paper_title_lower in cit_title or cit_title in paper_title_lower:
                food_papers_with_citations.append({
                    'title': paper['title'],
                    'citations': cit_count
                })
                total_citations += cit_count
                break

print(f"Food papers with citations: {len(food_papers_with_citations)}")
print(f"Total citations: {total_citations}")

result = {
    'paper_info': food_papers,
    'food_papers_with_citations': food_papers_with_citations,
    'total_citation_count': total_citations
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.list_db:2': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': 'file_storage/functions.execute_python:16.json'}

exec(code, env_args)
