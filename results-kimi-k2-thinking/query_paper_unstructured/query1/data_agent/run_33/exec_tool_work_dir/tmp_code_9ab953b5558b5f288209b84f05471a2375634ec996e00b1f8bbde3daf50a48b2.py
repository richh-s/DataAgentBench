code = """import json

# Load papers from the JSON file
papers_file_path = 'var_functions.query_db:2.json'
try:
    with open(papers_file_path, 'r') as f:
        papers = json.load(f)
except Exception as e:
    print(f'Error loading papers: {e}')
    papers = []

# Get citations from the variable
citations = var_functions.query_db_5

print(f'Papers loaded: {len(papers)}')
print(f'Citations loaded: {len(citations)}')

# Show first paper structure
if papers:
    first_paper = papers[0]
    print('\nFirst paper keys:', list(first_paper.keys()))
    print('First paper filename:', first_paper.get('filename'))
    print('First paper text preview:', first_paper.get('text', '')[:200])

# Show first citation structure
if citations:
    first_citation = citations[0]
    print('\nFirst citation:', first_citation)

# Extract title from filename for papers
food_papers = []
for paper in papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '').lower()
    
    # Check if paper is in food domain
    # Look for food-related keywords in the text
    food_keywords = ['food', 'diet', 'nutrition', 'eating', 'meal']
    is_food = any(keyword in text for keyword in food_keywords)
    
    if is_food:
        # Extract title from filename (remove .txt)
        title = filename.replace('.txt', '') if filename.endswith('.txt') else filename
        food_papers.append({
            'title': title,
            'filename': filename
        })

print(f'\nFood papers found: {len(food_papers)}')
if food_papers:
    print('Sample food papers:')
    for p in food_papers[:5]:
        print(f"  - {p['title']}")"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}]}

exec(code, env_args)
