code = """import json

# Get data from storage
emp_papers = locals()['var_functions.execute_python:12']
cite_data = locals()['var_functions.query_db:14']

# Load citations if needed
if isinstance(cite_data, str) and cite_data.endswith('.json'):
    with open(cite_data) as f:
        citations = json.load(f)
else:
    citations = cite_data

# Build citation map
cite_map = {}
for rec in citations:
    cite_map[rec['title']] = int(rec['total_citations'])

# Match and combine data
results = []
for p in emp_papers:
    title = p['title']
    year = p['year']
    cites = cite_map.get(title, 0)
    if cites == 0:
        for k, v in cite_map.items():
            if k.lower() == title.lower():
                cites = v
                break
    results.append([title, cites, year])

# Sort by citations descending
results.sort(key=lambda x: x[1], reverse=True)

# Create simple format for output
output_data = []
for r in results:
    output_data.append({'title': r[0], 'total_citations': r[1], 'year': r[2]})

# Just return the data structure, don't build complex strings
print('__RESULT__:')
print(json.dumps(output_data))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:12': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018, 'contribution': ['artifact', 'theoretical', 'empirical']}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019, 'contribution': ['survey', 'artifact', 'theoretical', 'empirical']}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'year': 2019, 'contribution': ['artifact', 'theoretical', 'empirical']}, {'title': 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings', 'year': 2018, 'contribution': ['survey', 'artifact', 'theoretical', 'empirical']}, {'title': 'Communicating Uncertainty in Fertility Prognosis', 'year': 2017, 'contribution': ['artifact', 'theoretical', 'empirical']}, {'title': 'DataSelfie: Empowering People to Design Personalized Visuals to Represent Their Data', 'year': 2018, 'contribution': ['artifact', 'theoretical', 'empirical']}, {'title': 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'year': 2018, 'contribution': ['artifact', 'theoretical', 'empirical']}, {'title': 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance', 'year': 2018, 'contribution': ['artifact', 'theoretical', 'empirical']}, {'title': 'Exploring the Value of Parent Tracked Baby Data in Interactions with Healthcare Professionals: A Data-Enabled Design Exploration', 'year': 2017, 'contribution': ['artifact', 'theoretical', 'empirical']}, {'title': 'FutureSelf: What Happens When We Forecast Self-Trackers? Future Health Statuses?', 'year': 2017, 'contribution': ['artifact', 'theoretical', 'empirical']}, {'title': "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps", 'year': 2017, 'contribution': ['artifact', 'theoretical', 'empirical']}, {'title': 'Making Sense of Sleep Sensors: How Sleep Sensing Technologies Support and Undermine Sleep Health', 'year': 2017, 'contribution': ['survey', 'artifact', 'theoretical', 'empirical']}, {'title': 'Opportunities for Oral Health Monitoring Technologies Beyond the Dental Clinic', 'year': 2018, 'contribution': ['artifact', 'theoretical', 'empirical']}, {'title': 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations', 'year': 2017, 'contribution': ['artifact', 'theoretical', 'empirical']}, {'title': 'Patient Perspectives on Self-Management Technologies for Chronic Fatigue Syndrome', 'year': 2017, 'contribution': ['survey', 'artifact', 'empirical']}, {'title': 'Quantified Factory Worker: Designing a Worker Feedback Dashboard', 'year': 2017, 'contribution': ['artifact', 'theoretical', 'empirical']}, {'title': 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'year': 2018, 'contribution': ['artifact', 'theoretical', 'empirical']}, {'title': "Supporting Coping with Parkinson's Disease Through Self Tracking", 'year': 2017, 'contribution': ['artifact', 'theoretical', 'empirical']}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', 'year': 2018, 'contribution': ['artifact', 'theoretical', 'empirical']}, {'title': "The 'Self' As Barrier for Self-Management Technologies in Healthcare?", 'year': 2018, 'contribution': ['artifact', 'theoretical', 'empirical']}, {'title': "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System", 'year': 2018, 'contribution': ['artifact', 'theoretical', 'empirical']}, {'title': 'Turn to the Self in Human-Computer Interaction: Care of the Self in Negotiating the Human-Technology Relationship', 'year': 2019, 'contribution': ['artifact', 'theoretical', 'empirical']}, {'title': 'Understanding Animals: A Critical Challenge in ACI', 'year': 2018, 'contribution': ['artifact', 'theoretical', 'empirical']}, {'title': 'Understanding Personal Productivity: How Knowledge Workers Define, Evaluate, and Reflect on Their Productivity', 'year': 2019, 'contribution': ['artifact', 'theoretical', 'empirical']}, {'title': 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating', 'year': 2017, 'contribution': ['artifact', 'theoretical', 'empirical']}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
