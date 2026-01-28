code = """import json
import re

# Load all data
citations_file = locals()['var_functions.query_db:18']
papers_file = locals()['var_functions.query_db:16']

with open(citations_file, 'r') as f:
    citations = json.load(f)

with open(papers_file, 'r') as f:
    papers = json.load(f)

# Create a mapping of paper titles to their domains
paper_domains = {}
for paper in papers:
    # Extract title from filename
    title = paper['filename'].replace('.txt', '')
    text = paper['text'].lower()
    
    # Check for food domain
    food_keywords = ['food', 'diet', 'eating', 'nutrition', 'meal', 'calorie', 'dietary']
    is_food = any(keyword in text for keyword in food_keywords)
    
    paper_domains[title] = {
        'is_food': is_food,
        'text_preview': text[:200]  # Just for verification
    }

# Sum citations by paper title
citations_by_paper = {}
for citation in citations:
    title = citation['title']
    count = int(citation['citation_count'])
    
    if title not in citations_by_paper:
        citations_by_paper[title] = 0
    citations_by_paper[title] += count

# Calculate total for food domain papers
total_food_citations = 0
food_papers_list = []

for title, total_cites in citations_by_paper.items():
    if title in paper_domains and paper_domains[title]['is_food']:
        total_food_citations += total_cites
        food_papers_list.append({
            'title': title,
            'citations': total_cites
        })

# Also check for papers that exist in citations but not in paper_docs
missing_in_papers = []
for title in citations_by_paper.keys():
    if title not in paper_domains:
        missing_in_papers.append(title)

print('__RESULT__:')
print(json.dumps({
    'total_food_citations': total_food_citations,
    'food_papers_count': len(food_papers_list),
    'food_papers': food_papers_list,
    'total_citations_processed': len(citations),
    'total_unique_papers_with_citations': len(citations_by_paper),
    'papers_in_mongodb': len(papers),
    'missing_papers_in_mongodb': len(missing_in_papers)
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:1': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:14': {'citations_count': 1405, 'papers_count': 5}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'total_citations': 1405, 'total_papers': 5}, 'var_functions.execute_python:22': {'food_papers_count': 5, 'total_citation_count': 1593, 'food_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'domains': ['food', 'physical activity', 'exercise', 'fitness', 'mental', 'finances', 'location', 'chronic'], 'is_food': True}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'domains': ['food', 'physical activity', 'exercise', 'sleep', 'finances', 'productivity', 'location', 'diabetes'], 'is_food': True}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'domains': ['food', 'physical activity', 'exercise', 'sleep', 'mental', 'social interactions'], 'is_food': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'domains': ['food', 'physical activity', 'exercise', 'fitness', 'mental', 'productivity', 'location', 'chronic'], 'is_food': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'domains': ['food', 'exercise', 'sleep', 'mental', 'location', 'chronic'], 'is_food': True}]}}

exec(code, env_args)
