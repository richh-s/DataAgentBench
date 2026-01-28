code = """# Access the papers data from storage variable
papers_data = var_functions.query_db_2

# Access citations from storage variable  
citations = var_functions.query_db_5

print('Papers type:', type(papers_data))
print('Citations type:', type(citations))

# Parse papers if it's a string
if isinstance(papers_data, str):
    import json
    papers = json.loads(papers_data)
else:
    papers = papers_data

print('Number of papers:', len(papers))
print('Number of citations:', len(citations))

# Build maps
paper_titles = set()
food_papers = set()

for paper in papers:
    filename = paper.get('filename', '')
    if filename and filename.endswith('.txt'):
        title = filename[:-4]
        paper_titles.add(title)
        
        # Check for food domain in text
        text = paper.get('text', '').lower()
        if 'food' in text:
            food_papers.add(title)

print('Total papers with titles:', len(paper_titles))
print('Food domain papers:', len(food_papers))

# Match citations with food papers
total_citations = 0
paper_citation_map = {}

for citation in citations:
    cit_title = citation.get('title', '')
    if cit_title in food_papers:
        cit_count = int(citation.get('citation_count', 0))
        total_citations += cit_count
        paper_citation_map[cit_title] = paper_citation_map.get(cit_title, 0) + cit_count

print('Unique food papers with citations:', len(paper_citation_map))
print('Total citations for food domain:', total_citations)

# Show some food papers
if food_papers:
    print('\nSample food papers:')
    for i, title in enumerate(list(food_papers)[:5]):
        cit_count = paper_citation_map.get(title, 0)
        print(f'{i+1}. {title} (citations: {cit_count})')"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}]}

exec(code, env_args)
