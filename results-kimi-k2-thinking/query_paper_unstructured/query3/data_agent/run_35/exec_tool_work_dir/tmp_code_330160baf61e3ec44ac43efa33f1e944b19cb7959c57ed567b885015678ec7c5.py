code = """import json

# Get the filtered titles from previous analysis
filtered_result = locals()['var_functions.execute_python:14']
filtered_titles = filtered_result['filtered_titles']

print("Papers to find citations for:")
for title in filtered_titles:
    print("  - " + title)

# Get citations data
citations = locals()['var_functions.query_db:16']
print("\nSample citations:")
for cit in citations[:5]:
    print("  - " + cit['title'] + " (" + cit['citation_year'] + "): " + cit['citation_count'])

print('__RESULT__:')
print(json.dumps({
    'paper_titles': filtered_titles,
    'citation_sample': citations[:5]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}, {'_id': '694f5530284b10b11dc0a86e', 'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}, {'_id': '694f5530284b10b11dc0a86f', 'filename': 'Barriers to Engagement with a Personal Informatics Productivity Tool.txt'}, {'_id': '694f5530284b10b11dc0a870', 'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt'}, {'_id': '694f5530284b10b11dc0a871', 'filename': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt"}, {'_id': '694f5530284b10b11dc0a872', 'filename': 'Blood Pressure Beyond the Clinic: Rethinking a Health Metric for Everyone.txt'}, {'_id': '694f5530284b10b11dc0a873', 'filename': 'Charting Design Preferences on Wellness Wearables.txt'}, {'_id': '694f5530284b10b11dc0a874', 'filename': 'ClimbSense: Automatic Climbing Route Recognition Using Wrist-worn Inertia Measurement Units.txt'}, {'_id': '694f5530284b10b11dc0a875', 'filename': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt"}, {'_id': '694f5530284b10b11dc0a876', 'filename': 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings.txt'}, {'_id': '694f5530284b10b11dc0a877', 'filename': 'Communicating Uncertainty in Fertility Prognosis.txt'}, {'_id': '694f5530284b10b11dc0a878', 'filename': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media.txt'}, {'_id': '694f5530284b10b11dc0a879', 'filename': 'ConCap: Designing to Empower Individual Reflection on Chronic Conditions Using Mobile Apps.txt'}, {'_id': '694f5530284b10b11dc0a87a', 'filename': 'Contextual Influences on the Use and Non-Use of Digital Technology While Exercising at the Gym.txt'}, {'_id': '694f5530284b10b11dc0a87b', 'filename': 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness.txt'}, {'_id': '694f5530284b10b11dc0a87c', 'filename': 'DataSelfie: Empowering People to Design Personalized Visuals to Represent Their Data.txt'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:14': {'filtered_titles': ['A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App'], 'count': 2}, 'var_functions.query_db:16': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}]}

exec(code, env_args)
