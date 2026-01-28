code = """import json

# Read citations data
citations_file = locals()['var_functions.query_db:8']
with open(citations_file, 'r') as f:
    citations = json.load(f)

# Food-related keywords
food_keywords = ['food', 'eating', 'diet', 'meal', 'nutrition', 'calorie', 'dietary']

# Filter for food papers and sum citations
food_citations = []
total_citation_count = 0

for citation in citations:
    title = citation['title']
    # Check if any food keyword is in the title
    if any(keyword.lower() in title.lower() for keyword in food_keywords):
        citation_count = int(citation['citation_count'])
        total_citation_count += citation_count
        food_citations.append({
            'title': title,
            'year': citation['citation_year'],
            'count': citation_count
        })

# Group by title to see each paper's total
from collections import defaultdict
paper_totals = defaultdict(int)
for citation in food_citations:
    paper_totals[citation['title']] += citation['count']

print('__RESULT__:')
print(json.dumps({
    'total_citation_count': total_citation_count,
    'unique_food_papers': len(paper_totals),
    'paper_totals': dict(paper_totals)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': [], 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_citations': 0, 'food_paper_titles': [], 'citation_count': 0}, 'var_functions.execute_python:18': {'total_citations': 1405, 'total_papers': 5, 'exact_matches_count': 5, 'food_citation_titles_count': 104, 'food_paper_titles_count': 1, 'food_citation_titles': ['Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling'], 'food_paper_titles': ['Barriers and Negative Nudges: Exploring Challenges in Food Journaling']}}

exec(code, env_args)
