code = """import json

# Load data from storage
empirical_papers = locals()['var_functions.execute_python:12']
citation_data = locals()['var_functions.query_db:14']

if isinstance(citation_data, str) and citation_data.endswith('.json'):
    with open(citation_data, 'r') as f:
        all_citations = json.load(f)
else:
    all_citations = citation_data

# Build citation lookup
citation_dict = {}
for rec in all_citations:
    citation_dict[rec['title']] = int(rec['total_citations'])

# Match papers
matched = []
for paper in empirical_papers:
    title = paper['title']
    citations = citation_dict.get(title, 0)
    if citations == 0:
        # Try case-insensitive
        for k, v in citation_dict.items():
            if title.lower() == k.lower():
                citations = v
                break
    matched.append({
        'title': title,
        'year': paper['year'],
        'total_citations': citations
    })

# Sort by citations
matched_sorted = sorted(matched, key=lambda x: x['total_citations'], reverse=True)

print('Total papers:', len(matched_sorted))
print('Top 10:')
for i, p in enumerate(matched_sorted[:10]):
    print(i+1, p['title'], 'Year:', p['year'], 'Citations:', p['total_citations'])

final_answer = []
final_answer.append('Papers with empirical contribution published after 2016:')
final_answer.append('')
for p in matched_sorted:
    line1 = 'Title: ' + p['title']
    line2 = 'Total Citations: ' + str(p['total_citations'])
    final_answer.append(line1)
    final_answer.append(line2)
    final_answer.append('')

answer_text = '\n'.join(final_answer)

result = {
    'papers': matched_sorted,
    'answer': answer_text
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:12': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018, 'contribution': ['artifact', 'theoretical', 'empirical']}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019, 'contribution': ['survey', 'artifact', 'theoretical', 'empirical']}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'year': 2019, 'contribution': ['artifact', 'theoretical', 'empirical']}, {'title': 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings', 'year': 2018, 'contribution': ['survey', 'artifact', 'theoretical', 'empirical']}, {'title': 'Communicating Uncertainty in Fertility Prognosis', 'year': 2017, 'contribution': ['artifact', 'theoretical', 'empirical']}, {'title': 'DataSelfie: Empowering People to Design Personalized Visuals to Represent Their Data', 'year': 2018, 'contribution': ['artifact', 'theoretical', 'empirical']}, {'title': 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'year': 2018, 'contribution': ['artifact', 'theoretical', 'empirical']}, {'title': 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance', 'year': 2018, 'contribution': ['artifact', 'theoretical', 'empirical']}, {'title': 'Exploring the Value of Parent Tracked Baby Data in Interactions with Healthcare Professionals: A Data-Enabled Design Exploration', 'year': 2017, 'contribution': ['artifact', 'theoretical', 'empirical']}, {'title': 'FutureSelf: What Happens When We Forecast Self-Trackers? Future Health Statuses?', 'year': 2017, 'contribution': ['artifact', 'theoretical', 'empirical']}, {'title': "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps", 'year': 2017, 'contribution': ['artifact', 'theoretical', 'empirical']}, {'title': 'Making Sense of Sleep Sensors: How Sleep Sensing Technologies Support and Undermine Sleep Health', 'year': 2017, 'contribution': ['survey', 'artifact', 'theoretical', 'empirical']}, {'title': 'Opportunities for Oral Health Monitoring Technologies Beyond the Dental Clinic', 'year': 2018, 'contribution': ['artifact', 'theoretical', 'empirical']}, {'title': 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations', 'year': 2017, 'contribution': ['artifact', 'theoretical', 'empirical']}, {'title': 'Patient Perspectives on Self-Management Technologies for Chronic Fatigue Syndrome', 'year': 2017, 'contribution': ['survey', 'artifact', 'empirical']}, {'title': 'Quantified Factory Worker: Designing a Worker Feedback Dashboard', 'year': 2017, 'contribution': ['artifact', 'theoretical', 'empirical']}, {'title': 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'year': 2018, 'contribution': ['artifact', 'theoretical', 'empirical']}, {'title': "Supporting Coping with Parkinson's Disease Through Self Tracking", 'year': 2017, 'contribution': ['artifact', 'theoretical', 'empirical']}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', 'year': 2018, 'contribution': ['artifact', 'theoretical', 'empirical']}, {'title': "The 'Self' As Barrier for Self-Management Technologies in Healthcare?", 'year': 2018, 'contribution': ['artifact', 'theoretical', 'empirical']}, {'title': "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System", 'year': 2018, 'contribution': ['artifact', 'theoretical', 'empirical']}, {'title': 'Turn to the Self in Human-Computer Interaction: Care of the Self in Negotiating the Human-Technology Relationship', 'year': 2019, 'contribution': ['artifact', 'theoretical', 'empirical']}, {'title': 'Understanding Animals: A Critical Challenge in ACI', 'year': 2018, 'contribution': ['artifact', 'theoretical', 'empirical']}, {'title': 'Understanding Personal Productivity: How Knowledge Workers Define, Evaluate, and Reflect on Their Productivity', 'year': 2019, 'contribution': ['artifact', 'theoretical', 'empirical']}, {'title': 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating', 'year': 2017, 'contribution': ['artifact', 'theoretical', 'empirical']}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
