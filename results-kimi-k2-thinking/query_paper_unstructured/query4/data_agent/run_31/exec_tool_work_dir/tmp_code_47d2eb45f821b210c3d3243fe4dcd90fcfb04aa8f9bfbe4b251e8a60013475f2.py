code = """import json

# Access the full result
result_path = locals().get('var_functions.query_db:2', '')

with open(result_path, 'r') as f:
    papers = json.load(f)

# Extract titles of papers from 2016 in physical activity domain
titles_2016_physical_activity = []
for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = paper.get('text', '')
    
    # Check if paper mentions 2016 and physical activity
    has_2016 = '2016' in text
    has_physical_activity = 'physical activity' in text.lower()
    
    if has_2016 and has_physical_activity and title:
        titles_2016_physical_activity.append(title)

print(f"Total papers from 2016 in 'physical activity' domain: {len(titles_2016_physical_activity)}")

# Create a safe result dictionary
result_dict = {
    'count': len(titles_2016_physical_activity),
    'titles': titles_2016_physical_activity
}

print('__RESULT__:')
print(json.dumps(result_dict))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'is_2016': True, 'has_physical_activity': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'is_2016': True, 'has_physical_activity': True}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'is_2016': True, 'has_physical_activity': True}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'is_2016': True, 'has_physical_activity': True}, {'title': 'Charting Design Preferences on Wellness Wearables', 'is_2016': True, 'has_physical_activity': True}, {'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'is_2016': True, 'has_physical_activity': True}, {'title': 'Communicating Uncertainty in Fertility Prognosis', 'is_2016': True, 'has_physical_activity': True}, {'title': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'is_2016': True, 'has_physical_activity': True}, {'title': 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'is_2016': True, 'has_physical_activity': True}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'is_2016': True, 'has_physical_activity': True}]}

exec(code, env_args)
