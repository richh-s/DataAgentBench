code = """import json

# Load citations data
citations_path = locals()['var_functions.query_db:2']
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Get food paper titles from previous analysis
# These are the papers that contain food keywords
food_titles = [
    "A Lived Informatics Model of Personal Informatics",
    "A Stage-based Model of Personal Informatics Systems", 
    "A Trip to the Moon: Personalized Animated Movies for Self-reflection",
    "A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App",
    "ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation"
]

# Calculate total citations for food papers
total_food_citations = 0
food_papers_citations = {}

for citation in citations:
    title = citation['title']
    if title in food_titles:
        count = int(citation['citation_count'])
        total_food_citations += count
        
        if title not in food_papers_citations:
            food_papers_citations[title] = 0
        food_papers_citations[title] += count

print('__RESULT__:')
print(json.dumps({
    'total_food_citations': total_food_citations,
    'food_papers_citations': food_papers_citations,
    'number_of_food_papers': len(food_papers_citations)
}, indent=2))"""

env_args = {'var_functions.query_db:0': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:10': {'total_papers': 5}, 'var_functions.execute_python:12': {'citations_count': 1405, 'papers_count': 5}, 'var_functions.execute_python:16': {'citations_loaded': 1405, 'papers_loaded': 5}, 'var_functions.execute_python:18': {'total_papers': 5, 'food_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'keywords': ['food', 'eating', 'meal', 'calorie', 'weight', 'bmi']}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'keywords': ['food', 'eating', 'meal', 'calorie', 'weight']}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'keywords': ['eating', 'bmi']}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'keywords': ['food', 'diet', 'meal']}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'keywords': ['eating', 'diet', 'meal', 'weight']}], 'all_paper_titles': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation']}}

exec(code, env_args)
