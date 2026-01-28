code = """import json

# Load citations data  
ct_path = locals()['var_functions.query_db:10']
with open(ct_path, 'r') as f:
    citations = json.load(f)

# Load papers data
pd_path = locals()['var_functions.query_db:16']
with open(pd_path, 'r') as f:
    papers = json.load(f)

print('Citations loaded:', len(citations))
print('Papers loaded:', len(papers))

# Build citation dictionary
cite_dict = {}
for rec in citations:
    title = rec.get('title', '').strip().lower()
    if title:
        cite_dict[title] = cite_dict.get(title, 0) + int(rec.get('citation_count', 0))

print('Unique papers in citations:', len(cite_dict))

# Find food papers
food_keywords = ['food', 'eating', 'nutrition', 'diet', 'meal', 'restaurant', 'grocery', 'calorie', 'weight loss', 'weight management']
food_papers = []
food_citations = 0

for paper in papers:
    filename = paper.get('filename', '')
    if filename:
        title = filename.replace('.txt', '')
        title_lower = title.lower()
        if any(term in title_lower for term in food_keywords):
            count = cite_dict.get(title_lower, 0)
            if count > 0:
                food_papers.append((title, count))
                food_citations += count

print('Food papers found:', len(food_papers))
print('Total citations:', food_citations)

result = {
    'count': len(food_papers),
    'total_citations': food_citations
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}], 'var_functions.list_db:14': ['paper_docs'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'total_food_papers': 4, 'papers_with_citations': 4, 'total_citation_count': 1328, 'top_papers': [['ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 452], ['A Lived Informatics Model of Personal Informatics', 390], ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 266], ['A Stage-based Model of Personal Informatics Systems', 220]]}, 'var_functions.execute_python:22': {'total_food_domain_papers_identified': 0, 'papers_with_citation_data': 0, 'total_citation_count': 0, 'papers': []}, 'var_functions.execute_python:26': {'total_food_papers': 0, 'papers_with_data': 0, 'total_citations': 0, 'papers': []}, 'var_functions.execute_python:30': {'status': 'debug_complete'}}

exec(code, env_args)
