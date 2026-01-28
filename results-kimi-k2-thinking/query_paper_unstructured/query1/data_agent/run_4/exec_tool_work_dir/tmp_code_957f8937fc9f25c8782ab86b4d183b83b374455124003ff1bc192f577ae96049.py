code = """import json
import re

# Get the file paths from storage
paper_docs_path = locals()['var_functions.query_db:9']
citation_titles_path = locals()['var_functions.query_db:5']

# Read the paper documents
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

# Read the citation titles
with open(citation_titles_path, 'r') as f:
    citation_titles = json.load(f)

# Extract titles from citation records
citation_title_set = set([item['title'] for item in citation_titles])

print('Total paper documents: ' + str(len(paper_docs)))
print('Total unique citation titles: ' + str(len(citation_title_set)))

# Extract paper information from documents
papers = []
for doc in paper_docs:
    filename = doc['filename']
    text = doc['text'] if 'text' in doc else ''
    
    # Extract title (filename without .txt)
    title = filename.replace('.txt', '')
    
    # Extract year - look for year patterns in text
    year_match = re.search(r"(19|20)\d{2}", text)
    year = year_match.group() if year_match else None
    
    # Extract venue - look for common venue patterns
    venue_patterns = [r"CHI", r"Ubicomp", r"UbiComp", r"CSCW", r"DIS", r"PervasiveHealth", r"WWW", r"IUI", r"OzCHI", r"TEI", r"AH", r"UBICOMP"]
    venue = None
    for pattern in venue_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            venue = pattern.upper()
            break
    
    # Extract source - look for publisher patterns
    source_patterns = [r"ACM", r"IEEE", r"PubMed"]
    source = None
    for pattern in source_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            source = pattern
            break
    
    # Extract domain - look for common domain patterns
    domain_patterns = [r"food", r"physical activity", r"sleep", r"mental", r"finances", r"productivity", r"screen time", r"social interactions", r"location", r"chronic", r"diabetes", r"health_behavior"]
    domains = []
    for pattern in domain_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            domains.append(pattern.lower())
    
    # Extract contribution - look for contribution patterns
    contribution_patterns = [r"empirical", r"artifact", r"theoretical", r"survey", r"methodological"]
    contributions = []
    for pattern in contribution_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            contributions.append(pattern.lower())
    
    papers.append({
        'title': title,
        'year': year,
        'venue': venue,
        'source': source,
        'domains': domains,
        'contributions': contributions,
        'has_citations': title in citation_title_set
    })

# Count papers in food domain
food_papers = [p for p in papers if 'food' in p['domains']]
print('Papers in food domain: ' + str(len(food_papers)))
food_with_citations = [p for p in food_papers if p['has_citations']]
print('Food papers with citations: ' + str(len(food_with_citations)))

# Create mapping of food paper titles
food_paper_titles = [p['title'] for p in food_papers]

# Print the result in the required format
print("__RESULT__:")
print(json.dumps(food_paper_titles))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
