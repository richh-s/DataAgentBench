code = """import json
import re

# Get file paths
paper_docs_path = locals()['var_functions.query_db:22']
citations_path = locals()['var_functions.query_db:38']
citation_titles_path = locals()['var_functions.query_db:5']

# Load all data
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

with open(citations_path, 'r') as f:
    all_citations = json.load(f)

# Food-related keywords
food_keywords = ['food', 'diet', 'nutrition', 'eating', 'meal']

# Identify food domain papers from citation data
food_papers = []
for citation in all_citations:
    title = citation['title']
    title_lower = title.lower()
    
    has_food_domain = False
    for keyword in food_keywords:
        if keyword in title_lower:
            has_food_domain = True
            break
    
    if has_food_domain:
        food_papers.append({
            'title': title,
            'citations': int(citation['total_citations'])
        })

# Calculate total citations
total_citations = sum([paper['citations'] for paper in food_papers])

print('Food domain papers found: ' + str(len(food_papers)))
print('Total citation count: ' + str(total_citations))

# Sample papers
print('Sample food papers:')
for i, paper in enumerate(food_papers[:5]):
    print(str(i+1) + '. ' + paper['title'] + ' - ' + str(paper['citations']) + ' citations')

result = {
    'total_citations': total_citations,
    'paper_count': len(food_papers)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:18': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App'], 'var_functions.query_db:20': [{'title': 'A Lived Informatics Model of Personal Informatics', 'total_citations': '390'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'total_citations': '220'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': '266'}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': [], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation'], 'var_functions.query_db:32': [{'title': 'A Lived Informatics Model of Personal Informatics', 'total_citations': '390'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'total_citations': '220'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': '265'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': '266'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'total_citations': '452'}], 'var_functions.execute_python:36': ['Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps", 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance', 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'Toward Health Information Technology That Supports Overweight/Obese Women in Addressing Emotion- and Stress-Related Eating', 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating', 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'Lunch Line: Using Public Displays and Mobile Devices to Encourage Healthy Eating in an Organization', 'Why and What Did We Throw out?: Probing on Reflection Through the Food Waste Diary', 'Supporting Patient-Provider Collaboration to Identify Individual Triggers Using Food and Symptom Journals', 'TummyTrials: A Feasibility Study of Using Self-Experimentation to Detect Individualized Food Triggers', 'Co-Designing Food Trackers with Dietitians: Identifying Design Opportunities for Food Tracker Customization', 'Identifying and Planning for Individualized Change: Patient-Provider Collaboration Using Lightweight Food Diaries in Healthy Eating and Irritable Bowel Syndrome', 'TableChat: Mobile Food Journaling to Facilitate Family Support for Healthy Eating', 'Soylent Diet Self-Experimentation: Design Challenges in Extreme Citizen Science Projects', 'My Doctor is Keeping an Eye on Me!: Exploring the Clinical Applicability of a Mobile Food Logger', 'Can SAL Support Self Reflection for Health and Nutrition?', 'Predicting About-to-Eat Moments for Just-in-Time Eating Intervention'], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.list_db:40': ['paper_docs']}

exec(code, env_args)
