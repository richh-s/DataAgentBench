code = """import json

# Use locals() to access variables with special characters in names
papers_file_path = locals()['var_functions.query_db:125']
citations_file_path = locals()['var_functions.query_db:100']

print("Papers file path:", papers_file_path)
print("Citations file path:", citations_file_path)

# Load papers data
with open(papers_file_path, 'r') as f:
    all_papers = json.load(f)

# Load citations data  
with open(citations_file_path, 'r') as f:
    all_citations = json.load(f)

print('Loaded {} papers and {} citation records'.format(len(all_papers), len(all_citations)))

# Create citation lookup dictionary
citation_lookup = {}
for record in all_citations:
    citation_lookup[record['title']] = int(record['total_citations'])

# Find 2016 physical activity papers
papers_2016_pa = []
for paper in all_papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    if not filename:
        continue
    
    # Check if from 2016
    if '2016' not in text:
        continue
    
    title = filename.replace('.txt', '')
    text_lower = text.lower()
    title_lower = title.lower()
    
    # Physical activity keywords
    keywords = ['physical activity', 'fitness', 'exercise', 'workout']
    
    # Check if in title
    in_title = any(k in title_lower for k in keywords)
    
    # Count occurrences in text
    keyword_count = sum(text_lower.count(k) for k in keywords)
    
    if in_title or keyword_count >= 3:
        total_citations = citation_lookup.get(title, 0)
        papers_2016_pa.append({'title': title, 'total_citations': total_citations})

# Sort by citations descending
papers_2016_pa.sort(key=lambda x: x['total_citations'], reverse=True)

print('Found {} papers from 2016 in physical activity domain'.format(len(papers_2016_pa)))

# Show first few results
for i, paper in enumerate(papers_2016_pa[:5]):
    print('{}. {} - {} citations'.format(i+1, paper['title'][:60], paper['total_citations']))

# Generate output text
output = []
output.append('Papers from 2016 in Physical Activity Domain')
output.append('=' * 60)
output.append('Total papers found: {}'.format(len(papers_2016_pa)))
output.append('')

for paper in papers_2016_pa:
    output.append('Title: {}'.format(paper['title']))
    output.append('Total Citations: {}'.format(paper['total_citations']))
    output.append('')

result_text = '\n'.join(output)
print('__RESULT__:')
print(result_text)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': [{'title': '"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults'}, {'title': 'A Lived Informatics Model of Personal Informatics'}, {'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity'}, {'title': 'A Situated Exploration of Designing for Personal Health Ecosystems Through Data-enabled Design'}, {'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity'}, {'title': 'A Stage-based Model of Personal Informatics Systems'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App'}, {'title': 'Activity Tracking in Vivo'}, {'title': 'Activity Tracking: Barriers, Workarounds and Customisation'}, {'title': 'Affordances for Self-tracking Wearable Devices'}, {'title': 'An Anxious Alliance'}, {'title': 'An Empirical Exploration of Mindfulness Design Using Solo Travel Domain'}, {'title': 'Anxiety and Autism: Towards Personalized Digital Health'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation'}, {'title': 'Armbeta: Towards Accessible Wearable Technology to Quantify Upper Limb Movement and Activities'}, {'title': 'Balancing Accuracy and Fun: Designing Camera Based Mobile Games for Implicit Heart Rate Monitoring'}, {'title': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling'}, {'title': 'Barriers to Engagement with a Personal Informatics Productivity Tool'}, {'title': 'Beacon: Designing a Portable Device for Self-Administering a Measure of Critical Flicker Frequency'}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use'}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching"}, {'title': 'Beyond Self-Tracking and Reminders: Designing Smartphone Apps That Support Habit Formation'}, {'title': 'Blood Pressure Beyond the Clinic: Rethinking a Health Metric for Everyone'}, {'title': 'Boundary Negotiating Artifacts in Personal Informatics: Patient-Provider Collaboration with Patient-Generated Data'}, {'title': 'Bringing New Voices to Design of Exercise Technology: Participatory Design with Vulnerable Young Adults'}, {'title': "But, I Don'T Take Steps: Examining the Inaccessibility of Fitness Trackers for Wheelchair Athletes"}, {'title': 'Can SAL Support Self Reflection for Health and Nutrition?'}, {'title': 'Caring Through Data: Attending to the Social and Emotional Experiences of Health Datafication'}, {'title': 'Charting Design Preferences on Wellness Wearables'}, {'title': 'ClimbSense: Automatic Climbing Route Recognition Using Wrist-worn Inertia Measurement Units'}, {'title': 'Clinical Data in Context: Towards Sensemaking Tools for Interpreting Personal Health Data'}, {'title': 'Closing the Feedback Loop: A 12-month Evaluation of ASTA, a Self-Tracking Application for ASHAs'}, {'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization"}, {'title': 'Co-Designing Food Trackers with Dietitians: Identifying Design Opportunities for Food Tracker Customization'}, {'title': 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings'}, {'title': 'Communicating Uncertainty in Fertility Prognosis'}, {'title': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media'}, {'title': 'ConCap: Designing to Empower Individual Reflection on Chronic Conditions Using Mobile Apps'}, {'title': 'Contextual Influences on the Use and Non-Use of Digital Technology While Exercising at the Gym'}, {'title': 'Crafting a View of Self-Tracking Data in the Clinical Visit'}, {'title': 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness'}, {'title': 'Data Representations for In-situ Exploration of Health and Fitness Data'}, {'title': 'Data, Data Everywhere, and Still Too Hard to Link: Insights from User Interactions with Diabetes Apps'}, {'title': 'DataSelfie: Empowering People to Design Personalized Visuals to Represent Their Data'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data'}, {'title': 'Design Considerations for Semi-automated Tracking: Self-care Plans in Spinal Cord Injury'}, {'title': 'Design Opportunities in Three Stages of Relationship Development Between Users and Self-Tracking Devices'}, {'title': 'Design Recommendations for Self-Monitoring in the Workplace: Studies in Software Development'}], 'var_functions.query_db:46': [], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:50': [{'title': "But, I Don'T Take Steps: Examining the Inaccessibility of Fitness Trackers for Wheelchair Athletes", 'total_citations': '554'}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure", 'total_citations': '542'}, {'title': 'Persistent Sharing of Fitness App Status on Twitter', 'total_citations': '462'}, {'title': 'VRFit: An Interactive Dashboard for Visualising of Virtual Reality Exercise and Daily Step Data', 'total_citations': '441'}, {'title': 'SweatAtoms: Materializing Physical Activity', 'total_citations': '428'}, {'title': 'Persuasive Technology in the Real World: A Study of Long-term Use of Activity Sensing Devices for Fitness', 'total_citations': '421'}, {'title': 'Bringing New Voices to Design of Exercise Technology: Participatory Design with Vulnerable Young Adults', 'total_citations': '419'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity', 'total_citations': '358'}, {'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'total_citations': '349'}, {'title': 'Low Sampling Rate for Physical Activity Recognition', 'total_citations': '348'}, {'title': 'HealthyTogether: Exploring Social Incentives for Mobile Fitness Applications', 'total_citations': '340'}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals', 'total_citations': '335'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', 'total_citations': '278'}, {'title': 'When Fitness Meets Social Networks: Investigating Fitness Tracking and Social Practices on WeRun', 'total_citations': '276'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'total_citations': '259'}, {'title': 'Data Representations for In-situ Exploration of Health and Fitness Data', 'total_citations': '245'}, {'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'total_citations': '221'}, {'title': 'Supporting Meaningful Personal Fitness: The Tracker Goal Evolution Model', 'total_citations': '191'}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity', 'total_citations': '180'}, {'title': "When Fitness Trackers Don'T 'Fit': End-user Difficulties in the Assessment of Personal Tracking Device Accuracy", 'total_citations': '155'}, {'title': 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'total_citations': '133'}, {'title': 'Move into Another World of Happy: Insights for Designing Affect-based Physical Activity Interventions', 'total_citations': '107'}, {'title': 'Fine-grained Sharing of Sensed Physical Activity: A Value Sensitive Approach', 'total_citations': '98'}, {'title': 'Social Fabric Fitness: The Design and Evaluation of Wearable E-textile Displays to Support Group Running', 'total_citations': '47'}, {'title': 'Understanding Physical Activity Through 3D Printed Material Artifacts', 'total_citations': '46'}, {'title': 'Personalization Revisited: A Reflective Approach Helps People Better Personalize Health Services and Motivates Them to Increase Physical Activity', 'total_citations': '12'}], 'var_functions.query_db:56': 'file_storage/functions.query_db:56.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json', 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json', 'var_functions.query_db:82': [{'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'citation_count': '28'}, {'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'citation_count': '95'}, {'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'citation_count': '62'}, {'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'citation_count': '36'}, {'title': "But, I Don'T Take Steps: Examining the Inaccessibility of Fitness Trackers for Wheelchair Athletes", 'citation_count': '54'}, {'title': "But, I Don'T Take Steps: Examining the Inaccessibility of Fitness Trackers for Wheelchair Athletes", 'citation_count': '76'}, {'title': "But, I Don'T Take Steps: Examining the Inaccessibility of Fitness Trackers for Wheelchair Athletes", 'citation_count': '96'}, {'title': "But, I Don'T Take Steps: Examining the Inaccessibility of Fitness Trackers for Wheelchair Athletes", 'citation_count': '94'}, {'title': "But, I Don'T Take Steps: Examining the Inaccessibility of Fitness Trackers for Wheelchair Athletes", 'citation_count': '20'}, {'title': "But, I Don'T Take Steps: Examining the Inaccessibility of Fitness Trackers for Wheelchair Athletes", 'citation_count': '54'}, {'title': "But, I Don'T Take Steps: Examining the Inaccessibility of Fitness Trackers for Wheelchair Athletes", 'citation_count': '84'}, {'title': "But, I Don'T Take Steps: Examining the Inaccessibility of Fitness Trackers for Wheelchair Athletes", 'citation_count': '13'}, {'title': "But, I Don'T Take Steps: Examining the Inaccessibility of Fitness Trackers for Wheelchair Athletes", 'citation_count': '63'}, {'title': 'Data Representations for In-situ Exploration of Health and Fitness Data', 'citation_count': '83'}, {'title': 'Data Representations for In-situ Exploration of Health and Fitness Data', 'citation_count': '82'}, {'title': 'Data Representations for In-situ Exploration of Health and Fitness Data', 'citation_count': '77'}, {'title': 'Data Representations for In-situ Exploration of Health and Fitness Data', 'citation_count': '3'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'citation_count': '57'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'citation_count': '67'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'citation_count': '58'}], 'var_functions.query_db:84': [], 'var_functions.query_db:86': 'file_storage/functions.query_db:86.json', 'var_functions.query_db:90': 'file_storage/functions.query_db:90.json', 'var_functions.query_db:94': 'file_storage/functions.query_db:94.json', 'var_functions.query_db:100': 'file_storage/functions.query_db:100.json', 'var_functions.query_db:110': 'file_storage/functions.query_db:110.json', 'var_functions.query_db:116': 'file_storage/functions.query_db:116.json', 'var_functions.query_db:118': 'file_storage/functions.query_db:118.json', 'var_functions.query_db:125': 'file_storage/functions.query_db:125.json'}

exec(code, env_args)
