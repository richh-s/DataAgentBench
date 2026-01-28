code = """import json

# Access papers data
papers = eval(open('var_functions.query_db:2.json', 'r').read())

# Access citations data  
citations = var_functions.query_db_5

print('Papers count:', len(papers))
print('Citations count:', len(citations))

# Extract food papers and create title mapping
food_titles = set()
paper_map = {}

for p in papers:
    fn = p.get('filename', '')
    if fn.endswith('.txt'):
        title = fn[:-4]
        paper_map[title] = p
        if 'food' in p.get('text', '').lower():
            food_titles.add(title)

print('Food papers found:', len(food_titles))

# Sum citations for food papers
total = 0
matches = 0
for c in citations:
    ct = c.get('title', '')
    if ct in food_titles:
        total += int(c.get('citation_count', 0))
        matches += 1

print('Matching citations:', matches)
print('Total citation count:', total)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}]}

exec(code, env_args)
