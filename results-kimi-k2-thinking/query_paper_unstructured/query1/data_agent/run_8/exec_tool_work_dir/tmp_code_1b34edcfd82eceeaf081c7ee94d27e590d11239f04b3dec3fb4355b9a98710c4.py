code = """import json
import re

# Load all papers from MongoDB
papers_file = locals()['var_functions.query_db:10']
papers = []
with open(papers_file, 'r') as f:
    papers = json.load(f)

# Load all citations from SQLite
citations_file = locals()['var_functions.query_db:5']
citations = []
with open(citations_file, 'r') as f:
    citations = json.load(f)

# Create a mapping from paper titles to their domains
# Extract title from filename (remove .txt extension)
paper_domains = {}
for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = paper.get('text', '')
    
    # Look for domain information in the text
    # The hint says to use substring/contains matching
    # Let's look for various ways domain might be mentioned
    domains = []
    
    # Common domain patterns to look for
    domain_keywords = ['food', 'physical activity', 'sleep', 'mental', 'finances', 
                      'productivity', 'screen time', 'social interactions', 
                      'location', 'chronic', 'diabetes', 'health_behavior']
    
    text_lower = text.lower()
    for keyword in domain_keywords:
        if keyword in text_lower:
            domains.append(keyword)
    
    if title:
        paper_domains[title] = domains

# Also create mapping for lowercase titles for better matching
paper_domains_lower = {k.lower(): v for k, v in paper_domains.items()}

# Get food papers
food_papers = []
for title, domains in paper_domains.items():
    if 'food' in domains:
        food_papers.append(title)

# Debug info
print('__RESULT__:')
print(json.dumps({
    "total_papers_loaded": len(papers),
    "papers_with_titles": len(paper_domains),
    "food_papers_found": food_papers,
    "food_papers_count": len(food_papers)
}))"""

env_args = {'var_functions.query_db:0': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'citations_count': 1405, 'papers_count': 5}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'total_papers': 5, 'total_citations': 1405}}

exec(code, env_args)
