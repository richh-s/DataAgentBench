code = """import json
import re

# Get food-related papers from MongoDB
paper_docs_file = locals()['var_functions.query_db:14']
with open(paper_docs_file, 'r') as f:
    papers = json.load(f)

# Extract titles that mention food
food_paper_titles = []
food_keywords = ['food', 'eating', 'diet', 'meal', 'nutrition', 'calorie']

for paper in papers:
    filename = paper['filename']
    text = paper['text']
    title = filename.replace('.txt', '')
    
    # Check if any food keyword appears in the text
    for keyword in food_keywords:
        if re.search(r'\b' + keyword + r'\b', text, re.IGNORECASE):
            food_paper_titles.append(title)
            break

# Get citations from SQLite
citations_file = locals()['var_functions.query_db:8']
with open(citations_file, 'r') as f:
    citations = json.load(f)

# Filter citations for food papers and sum them
food_citation_data = []
total_citations = 0

for citation in citations:
    citation_title = citation['title']
    
    # Check if this citation title matches any food paper
    for food_title in food_paper_titles:
        if food_title == citation_title:
            food_citation_data.append(citation)
            total_citations += int(citation['citation_count'])
            break

print('__RESULT__:')
print(json.dumps({
    'total_citations': total_citations,
    'food_paper_titles': food_paper_titles,
    'citation_count': len(food_citation_data)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': [], 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
