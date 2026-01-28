code = """import json

# Load all papers from the MongoDB query result (stored in var_functions.query_db:36)
with open('var_functions.query_db:36', 'r') as f:
    papers = json.load(f)

# Count total papers and look for food domain papers
total_papers = len(papers)
food_papers = []

for paper in papers:
    filename = paper['filename']
    title = filename.replace('.txt', '')
    text = paper['text'].lower()
    
    # Look for food as a research domain
    # Check if "food" appears in contexts that suggest it's a domain being studied
    if 'food' in text:
        # Count occurrences and check context
        lines = text.split('\n')
        food_mentions = 0
        domain_context_mentions = 0
        
        for line in lines:
            if 'food' in line:
                food_mentions += 1
                # Check if this line suggests food is a domain/tracking area
                if any(context in line for context in ['track', 'domain', 'research', 'study', 'self-', 'personal informatics']):
                    domain_context_mentions += 1
        
        # If food is mentioned multiple times and at least once in a research context,
        # it's likely a food domain paper
        if food_mentions >= 2:
            food_papers.append({
                'title': title,
                'food_mentions': food_mentions,
                'domain_context_mentions': domain_context_mentions
            })

print('Total papers: ' + str(total_papers))
print('Food domain papers: ' + str(len(food_papers)))
print('Sample food papers: ' + str([p['title'] for p in food_papers[:10]]))

result = {
    'total_papers': total_papers,
    'food_papers_count': len(food_papers),
    'food_papers': food_papers
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.list_db:10': ['paper_docs'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:34': {'food_papers_count': 0, 'citations_count': 0, 'files_checked': []}, 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
