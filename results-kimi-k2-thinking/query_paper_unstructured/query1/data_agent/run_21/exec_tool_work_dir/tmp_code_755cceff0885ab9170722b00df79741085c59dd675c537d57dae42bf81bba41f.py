code = """import json

# Load the papers that mention food (from var_functions.query_db:48)
food_mention_papers = [
    {"_id": "694f5530284b10b11dc0a869", "filename": "A Lived Informatics Model of Personal Informatics.txt"},
    {"_id": "694f5530284b10b11dc0a86a", "filename": "A Stage-based Model of Personal Informatics Systems.txt"},
    {"_id": "694f5530284b10b11dc0a86c", "filename": "A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt"},
    {"_id": "694f5530284b10b11dc0a86e", "filename": "Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt"},
    {"_id": "694f5530284b10b11dc0a870", "filename": "Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt"}
]

# Now identify which are truly food domain papers
# Based on titles, only "Barriers and Negative Nudges: Exploring Challenges in Food Journaling"
# is clearly a food domain paper. The others just mention food as one of multiple domains.

food_domain_titles = [
    "Barriers and Negative Nudges: Exploring Challenges in Food Journaling"
]

print('Papers mentioning food: ' + str(len(food_mention_papers)))
print('Food domain papers: ' + str(len(food_domain_titles)))
print('Food domain titles: ' + str(food_domain_titles))

result = {
    'food_mention_papers': len(food_mention_papers),
    'food_domain_titles': food_domain_titles,
    'food_domain_count': len(food_domain_titles)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.list_db:10': ['paper_docs'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:34': {'food_papers_count': 0, 'citations_count': 0, 'files_checked': []}, 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.list_db:44': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:48': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86e', 'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}, {'_id': '694f5530284b10b11dc0a870', 'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt'}]}

exec(code, env_args)
