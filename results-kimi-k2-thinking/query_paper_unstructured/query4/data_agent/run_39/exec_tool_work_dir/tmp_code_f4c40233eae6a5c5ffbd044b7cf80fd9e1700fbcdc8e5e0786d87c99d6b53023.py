code = """import json
import re
import os

# Load 2016 papers
papers_2016_file = locals()['var_functions.query_db:38']
with open(papers_2016_file, 'r') as f:
    papers_2016 = json.load(f)

print('Total 2016 papers loaded: ' + str(len(papers_2016)))

# Load citation data (activity papers)
citations_file = locals()['var_functions.query_db:36']
with open(citations_file, 'r') as f:
    activity_citations = json.load(f)

# Create a dictionary for citation lookup
citation_dict = {item['title']: int(item['total_citations']) for item in activity_citations}

print('Total activity citation records: ' + str(len(citation_dict)))

# Find 2016 papers that are about physical activity
results = []

for doc in papers_2016:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename or not text:
        continue
    
    title = os.path.splitext(filename)[0]
    
    # Check if paper is about physical activity based on content
    text_lower = text.lower()
    
    # Strong indicators this is a physical activity paper
    pa_indicators = [
        'physical activity tracking',
        'activity tracker',
        'fitness tracker', 
        'wearable activity',
        'exercise tracking',
        'self-tracking physical activity',
        'fitbit',
        'physical activity data',
        'sensed physical activity'
    ]
    
    # Check for physical activity focus
    is_physical_activity = False
    
    # Count occurrences of PA phrases
    pa_count = sum(1 for indicator in pa_indicators if indicator in text_lower)
    
    # If multiple PA-specific phrases appear, it's likely a PA paper
    if pa_count >= 2:
        is_physical_activity = True
    elif pa_count >= 1 and ('activity' in title.lower() or 'fitness' in title.lower() or 'exercise' in title.lower()):
        is_physical_activity = True
    
    if is_physical_activity and title in citation_dict:
        results.append({
            'title': title,
            'total_citation_count': citation_dict[title]
        })
        print('Found PA paper: ' + title + ' (' + str(citation_dict[title]) + ' citations)')

print('Total matches found: ' + str(len(results)))

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.query_db:0': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:22': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': 265}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': 266}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'total_citations': 452}], 'var_functions.list_db:26': ['paper_docs'], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:32': [], 'var_functions.execute_python:34': [], 'var_functions.query_db:36': [{'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'total_citations': '221'}, {'title': 'Activity Tracking in Vivo', 'total_citations': '316'}, {'title': 'Activity Tracking: Barriers, Workarounds and Customisation', 'total_citations': '91'}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'total_citations': '636'}, {'title': 'Bringing New Voices to Design of Exercise Technology: Participatory Design with Vulnerable Young Adults', 'total_citations': '419'}, {'title': "But, I Don'T Take Steps: Examining the Inaccessibility of Fitness Trackers for Wheelchair Athletes", 'total_citations': '554'}, {'title': 'Data Representations for In-situ Exploration of Health and Fitness Data', 'total_citations': '245'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'total_citations': '259'}, {'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'total_citations': '349'}, {'title': 'Facts, Interactivity and Videotape: Exploring the Design Space of Data in Interactive Video Storytelling', 'total_citations': '430'}, {'title': 'Family Health Promotion in Low-SES Neighborhoods: A Two-Month Study of Wearable Activity Tracking', 'total_citations': '400'}, {'title': 'Fine-grained Sharing of Sensed Physical Activity: A Value Sensitive Approach', 'total_citations': '98'}, {'title': 'Goal-oriented Visualizations of Activity Tracking: A Case Study with Engineering Students', 'total_citations': '339'}, {'title': 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'total_citations': '133'}, {'title': 'HealthyTogether: Exploring Social Incentives for Mobile Fitness Applications', 'total_citations': '340'}, {'title': 'How Do We Engage with Activity Trackers?: A Longitudinal Study of Habito', 'total_citations': '367'}, {'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'total_citations': '316'}, {'title': 'Low Sampling Rate for Physical Activity Recognition', 'total_citations': '348'}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure", 'total_citations': '542'}, {'title': 'Move into Another World of Happy: Insights for Designing Affect-based Physical Activity Interventions', 'total_citations': '107'}, {'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'total_citations': '284'}, {'title': 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations', 'total_citations': '190'}, {'title': 'Pass the Ball: Enforced Turn-Taking in Activity Tracking', 'total_citations': '344'}, {'title': 'Patina Engraver: Visualizing Activity Logs As Patina in Fashionable Trackers', 'total_citations': '497'}, {'title': 'Persistent Sharing of Fitness App Status on Twitter', 'total_citations': '462'}, {'title': 'Personalization Revisited: A Reflective Approach Helps People Better Personalize Health Services and Motivates Them to Increase Physical Activity', 'total_citations': '12'}, {'title': 'Persuasive Technology in the Real World: A Study of Long-term Use of Activity Sensing Devices for Fitness', 'total_citations': '421'}, {'title': 'Prescribing 10,000 Steps Like Aspirin: Designing a Novel Interface for Data-Driven Medical Consultations', 'total_citations': '285'}, {'title': 'Quantified Recess: Design of an Activity for Elementary Students Involving Analyses of Their Own Movement Data', 'total_citations': '340'}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals', 'total_citations': '335'}, {'title': 'Sensor Requirements for Activity Recognition on Smart Watches', 'total_citations': '488'}, {'title': 'Sharing Automatically Tracked Activity Data: Implications for Therapists and People with Mobility Impairments', 'total_citations': '80'}, {'title': 'Sharing Steps in the Workplace: Changing Privacy Concerns Over Time', 'total_citations': '123'}, {'title': 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'total_citations': '404'}, {'title': 'Social Fabric Fitness: The Design and Evaluation of Wearable E-textile Displays to Support Group Running', 'total_citations': '47'}, {'title': 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace', 'total_citations': '434'}, {'title': 'Supporting Meaningful Personal Fitness: The Tracker Goal Evolution Model', 'total_citations': '191'}, {'title': 'SweatAtoms: Materializing Physical Activity', 'total_citations': '428'}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity', 'total_citations': '180'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', 'total_citations': '278'}, {'title': 'ThinkActive: Designing for Pseudonymous Activity Tracking in the Classroom', 'total_citations': '225'}, {'title': 'Understanding Physical Activity Through 3D Printed Material Artifacts', 'total_citations': '46'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity', 'total_citations': '358'}, {'title': 'VRFit: An Interactive Dashboard for Visualising of Virtual Reality Exercise and Daily Step Data', 'total_citations': '441'}, {'title': 'When Fitness Meets Social Networks: Investigating Fitness Tracking and Social Practices on WeRun', 'total_citations': '276'}, {'title': "When Fitness Trackers Don'T 'Fit': End-user Difficulties in the Assessment of Personal Tracking Device Accuracy", 'total_citations': '155'}], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)
