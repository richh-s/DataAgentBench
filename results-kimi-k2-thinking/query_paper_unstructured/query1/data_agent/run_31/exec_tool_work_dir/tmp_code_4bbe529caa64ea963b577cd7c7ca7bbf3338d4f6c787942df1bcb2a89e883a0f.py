code = """import json

# Get the data from storage
citations_result = locals()['var_functions.query_db:11']
papers_result = locals()['var_functions.query_db:10']

# Check if these are file paths or direct data
print('Citations result type:', type(citations_result))
print('Papers result type:', type(papers_result))

# Load the actual data
if isinstance(citations_result, str):
    with open(citations_result, 'r') as f:
        citations_data = json.load(f)
else:
    citations_data = citations_result

if isinstance(papers_result, str):
    with open(papers_result, 'r') as f:
        papers_data = json.load(f)
else:
    papers_data = papers_result

print('Citations count:', len(citations_data))
print('Papers count:', len(papers_data))

# Find food domain papers
food_keywords = ['food', 'diet', 'nutrition', 'eating', 'meal', 'dietary', 'calorie', 'cuisine']
food_paper_titles = []

for paper in papers_data:
    text = paper.get('text', '').lower()
    filename = paper.get('filename', '')
    
    if any(keyword in text for keyword in food_keywords):
        title = filename.replace('.txt', '')
        food_paper_titles.append(title)

print('Food papers found:', len(food_paper_titles))

# Calculate total citations
total_food_citations = 0
matches = 0

for citation in citations_data:
    title = citation.get('title', '')
    if title in food_paper_titles:
        total_food_citations += int(citation.get('total_citations'))
        matches += 1

print('Total matching papers:', matches)
print('Total citation count:', total_food_citations)

__RESULT__ = str(total_food_citations)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
