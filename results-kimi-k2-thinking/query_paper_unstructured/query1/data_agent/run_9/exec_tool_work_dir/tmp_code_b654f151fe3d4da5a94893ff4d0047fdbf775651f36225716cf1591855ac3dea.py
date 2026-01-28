code = """import json
import os

print('Starting analysis...')

# Step 1: Define food paper titles from the query result
food_docs = [
    {"filename": "Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt"},
    {"filename": "Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness.txt"},
    {"filename": "Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers.txt"},
    {"filename": "Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture.txt"}
]

# Extract titles (remove .txt extension)
food_titles = []
for doc in food_docs:
    title = doc['filename'].replace('.txt', '')
    food_titles.append(title)

print('Food paper titles:', food_titles)

# Step 2: Load citations data from file
# Find the citations JSON file
citations_file = None
for filename in os.listdir('.'):
    if filename.endswith('.json'):
        with open(filename, 'r') as f:
            content = f.read()
            if 'title' in content and 'total_citations' in content:
                citations_file = filename
                break

print('Citations file:', citations_file)

# Load citations
with open(citations_file, 'r') as f:
    citations = json.load(f)

print('Total citation records:', len(citations))

# Step 3: Sum citations for food papers
total_citations = 0
matched_count = 0

for citation in citations:
    cit_title = citation['title']
    if cit_title in food_titles:
        cit_count = int(citation['total_citations'])
        total_citations += cit_count
        matched_count += 1
        print('Match:', cit_title, '->', cit_count, 'citations')

print('Matches found:', matched_count)
print('Total citations for food domain:', total_citations)

# Step 4: Output result
result = str(total_citations)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:5': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}, {'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt'}], 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_functions.query_db:54': [{'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}, {'filename': 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness.txt'}, {'filename': 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers.txt'}, {'filename': 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance.txt'}, {'filename': "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps.txt"}], 'var_functions.query_db:58': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_functions.query_db:62': [{'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}, {'filename': 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness.txt'}, {'filename': 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers.txt'}, {'filename': 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture.txt'}]}

exec(code, env_args)
