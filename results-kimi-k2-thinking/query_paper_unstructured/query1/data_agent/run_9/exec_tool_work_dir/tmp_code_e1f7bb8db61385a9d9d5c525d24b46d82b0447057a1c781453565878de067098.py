code = """import json

# Food papers from the query
food_papers = [
    {"filename": "Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt"},
    {"filename": "Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness.txt"},
    {"filename": "Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers.txt"},
    {"filename": "Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance.txt"},
    {"filename": "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps.txt"}
]

# Extract titles (remove .txt extension)
food_titles = []
for paper in food_papers:
    title = paper['filename'].replace('.txt', '')
    food_titles.append(title)

print('Food domain paper titles:')
for title in food_titles:
    print('  ' + title)

# Now we need to load the citations data
# Let's find the citations file from our environment
import os
files = os.listdir('.')

# Find the citations JSON file
citations_file = None
for f in files:
    if f.endswith('.json'):
        # Check if it's the citations file by looking at size or content
        size = os.path.getsize(f)
        if size > 10000:  # Likely the citations file
            citations_file = f
            break

print('\nCitations file: ' + citations_file)

# Load citations data
with open(citations_file, 'r') as f:
    citations = json.load(f)

print('Total citation records: ' + str(len(citations)))

# Sum citations for food papers
total_citations = 0
found_papers = []

for citation in citations:
    cit_title = citation['title']
    if cit_title in food_titles:
        cit_count = int(citation['total_citations'])
        total_citations += cit_count
        found_papers.append((cit_title, cit_count))

print('\nFood papers with citations:')
for title, count in found_papers:
    print('  ' + title + ': ' + str(count))

print('\nTotal citations for food domain: ' + str(total_citations))

print('__RESULT__:')
print(str(total_citations))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:5': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}, {'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt'}], 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_functions.query_db:54': [{'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}, {'filename': 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness.txt'}, {'filename': 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers.txt'}, {'filename': 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance.txt'}, {'filename': "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps.txt"}]}

exec(code, env_args)
