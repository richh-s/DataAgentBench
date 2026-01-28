code = """import json
import os

# Read food-related papers from MongoDB query
food_papers_file = locals()['var_functions.query_db:28']
with open(food_papers_file, 'r') as f:
    food_papers = json.load(f)

print('Total papers in food query:', len(food_papers))

# Extract titles from MongoDB papers with food keywords
food_keywords = ['food', 'eating', 'diet', 'dietary', 'nutrition', 'meal', 'cuisine', 'journal']
food_titles = []

for paper in food_papers:
    filename = paper['filename']
    # Clean title (remove .txt)
    clean_title = filename.replace('.txt', '')
    # Check if food-related
    lower_title = clean_title.lower()
    for keyword in food_keywords:
        if keyword in lower_title:
            food_titles.append(clean_title)
            break

print('Food papers titles extracted:', len(food_titles))
print('Sample titles:', food_titles[:10])

# Read citations data
citations_file = locals()['var_functions.query_db:26']
with open(citations_file, 'r') as f:
    citations = json.load(f)

print('Total citation records:', len(citations))

# Create dictionary mapping title to citation count
citation_dict = {}
for item in citations:
    citation_dict[item['title']] = int(item['total_citations'])

# Match food papers with citations and sum
total_citations = 0
matched_papers = 0
matched_list = []

for title in food_titles:
    if title in citation_dict:
        cit_count = citation_dict[title]
        total_citations += cit_count
        matched_papers += 1
        matched_list.append((title, cit_count))

print('Matched papers with citations:', matched_papers)
print('Total citation count:', total_citations)

# Show top papers
top_papers = sorted(matched_list, key=lambda x: x[1], reverse=True)
print('Top 5 cited papers:')
for i, (title, count) in enumerate(top_papers[:5], 1):
    print(f"{i}. {count} citations: {title}")

result = {'total_citations': total_citations, 'papers_count': matched_papers}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:14': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing'}, {'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:24': {'total_citations': 143, 'papers_matched': 1}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:30': {'food_titles': ['Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'Can SAL Support Self Reflection for Health and Nutrition?', 'Co-Designing Food Trackers with Dietitians: Identifying Design Opportunities for Food Tracker Customization', 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance', 'Examining Unlock Journaling with Diaries and Reminders for In Situ Self-Report in Health and Wellness', 'Flexible and Mindful Self-Tracking: Design Implications from Paper Bullet Journals', 'Identifying and Planning for Individualized Change: Patient-Provider Collaboration Using Lightweight Food Diaries in Healthy Eating and Irritable Bowel Syndrome', "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps", "It's Just My History Isn'T It?: Understanding Smart Journaling Practices", 'Lunch Line: Using Public Displays and Mobile Devices to Encourage Healthy Eating in an Organization', 'My Doctor is Keeping an Eye on Me!: Exploring the Clinical Applicability of a Mobile Food Logger', 'Predicting About-to-Eat Moments for Just-in-Time Eating Intervention', 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'Soylent Diet Self-Experimentation: Design Challenges in Extreme Citizen Science Projects', 'Supporting Patient-Provider Collaboration to Identify Individual Triggers Using Food and Symptom Journals', 'TableChat: Mobile Food Journaling to Facilitate Family Support for Healthy Eating', 'Toward Health Information Technology That Supports Overweight/Obese Women in Addressing Emotion- and Stress-Related Eating', 'TummyTrials: A Feasibility Study of Using Self-Experimentation to Detect Individualized Food Triggers', 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating', 'Why and What Did We Throw out?: Probing on Reflection Through the Food Waste Diary'], 'count': 22}}

exec(code, env_args)
