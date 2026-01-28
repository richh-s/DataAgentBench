code = """# First, let's inspect what we have
papers_2016_list = locals()['var_functions.query_db:28']
pa_citations_list = locals()['var_functions.query_db:30']

# Create a dictionary for fast citation lookup
citation_dict = {}
for item in pa_citations_list:
    citation_dict[item['title']] = int(item['total_citations'])

# Check for physical activity domain
import re

results = []
for paper in papers_2016_list:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # Check if physical activity domain
    if re.search(r'physical activity|activity tracker|fitness tracker|exercise', text, re.IGNORECASE):
        title = filename.replace('.txt', '')
        if title in citation_dict:
            results.append({
                'title': title,
                'total_citations': citation_dict[title]
            })

print(f'Found {len(results)} papers')
for r in results:
    print(f"{r['title']}: {r['total_citations']}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs'], 'var_functions.execute_python:14': {'count': 38}, 'var_functions.query_db:16': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': [{'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'total_citations': '221'}, {'title': 'Bringing New Voices to Design of Exercise Technology: Participatory Design with Vulnerable Young Adults', 'total_citations': '419'}, {'title': "But, I Don'T Take Steps: Examining the Inaccessibility of Fitness Trackers for Wheelchair Athletes", 'total_citations': '554'}, {'title': 'Data Representations for In-situ Exploration of Health and Fitness Data', 'total_citations': '245'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'total_citations': '259'}, {'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'total_citations': '349'}, {'title': 'Fine-grained Sharing of Sensed Physical Activity: A Value Sensitive Approach', 'total_citations': '98'}, {'title': 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'total_citations': '133'}, {'title': 'HealthyTogether: Exploring Social Incentives for Mobile Fitness Applications', 'total_citations': '340'}, {'title': 'Low Sampling Rate for Physical Activity Recognition', 'total_citations': '348'}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure", 'total_citations': '542'}, {'title': 'Move into Another World of Happy: Insights for Designing Affect-based Physical Activity Interventions', 'total_citations': '107'}, {'title': 'Persistent Sharing of Fitness App Status on Twitter', 'total_citations': '462'}, {'title': 'Personalization Revisited: A Reflective Approach Helps People Better Personalize Health Services and Motivates Them to Increase Physical Activity', 'total_citations': '12'}, {'title': 'Persuasive Technology in the Real World: A Study of Long-term Use of Activity Sensing Devices for Fitness', 'total_citations': '421'}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals', 'total_citations': '335'}, {'title': 'Social Fabric Fitness: The Design and Evaluation of Wearable E-textile Displays to Support Group Running', 'total_citations': '47'}, {'title': 'Supporting Meaningful Personal Fitness: The Tracker Goal Evolution Model', 'total_citations': '191'}, {'title': 'SweatAtoms: Materializing Physical Activity', 'total_citations': '428'}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity', 'total_citations': '180'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', 'total_citations': '278'}, {'title': 'Understanding Physical Activity Through 3D Printed Material Artifacts', 'total_citations': '46'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity', 'total_citations': '358'}, {'title': 'VRFit: An Interactive Dashboard for Visualising of Virtual Reality Exercise and Daily Step Data', 'total_citations': '441'}, {'title': 'When Fitness Meets Social Networks: Investigating Fitness Tracking and Social Practices on WeRun', 'total_citations': '276'}, {'title': "When Fitness Trackers Don'T 'Fit': End-user Difficulties in the Assessment of Personal Tracking Device Accuracy", 'total_citations': '155'}]}

exec(code, env_args)
