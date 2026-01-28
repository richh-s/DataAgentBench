code = """import json

# Load citations data
citations_path = locals()['var_functions.query_db:16']
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Filter for physical activity papers in 2016 citations
physical_activity_papers = []
keywords = ['physical activity', 'fitness', 'exercise', 'activity tracking', 'wearable', 'activity tracker']

for citation in citations:
    title = citation.get('title', '')
    citation_count = citation.get('citation_count', 0)
    title_lower = title.lower()
    
    # Check if paper is related to physical activity
    is_physical_activity = any(keyword in title_lower for keyword in keywords)
    
    # Additional check for activity-related terms
    if not is_physical_activity:
        if 'activity' in title_lower and any(word in title_lower for word in ['track', 'monitor', 'sense', 'capture']):
            is_physical_activity = True
    
    if is_physical_activity:
        physical_activity_papers.append({
            'title': title,
            'total_citation_count': int(citation_count)
        })

# Sort by citation count (highest first)
physical_activity_papers.sort(key=lambda x: x['total_citation_count'], reverse=True)

print('Total physical activity papers with 2016 citations:', len(physical_activity_papers))
print('\n__RESULT__:')
print(json.dumps(physical_activity_papers))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'paper_count': 5, 'sample_keys': ['_id', 'filename', 'text'], 'sample_filename': 'A Lived Informatics Model of Personal Informatics.txt'}, 'var_functions.execute_python:14': {'all_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': 2015, 'domain': ['physical activity', 'food', 'finances'], 'venue': ['CHI', 'Ubicomp', 'CSCW'], 'source': ['ACM'], 'contribution': ['empirical', 'artifact', 'theoretical']}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'domain': ['physical activity', 'food', 'sleep', 'finances'], 'venue': ['CHI', 'Ubicomp'], 'source': ['ACM', 'IEEE'], 'contribution': ['empirical', 'artifact', 'theoretical']}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2016, 'domain': ['physical activity', 'sleep', 'mental'], 'venue': ['CHI'], 'source': ['ACM'], 'contribution': ['empirical', 'artifact', 'theoretical']}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2016, 'domain': ['physical activity', 'food', 'mental'], 'venue': ['CHI'], 'source': ['ACM', 'IEEE'], 'contribution': ['empirical', 'artifact', 'theoretical']}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': 2016, 'domain': ['food', 'sleep'], 'venue': ['CHI'], 'source': ['ACM', 'IEEE'], 'contribution': ['empirical', 'artifact', 'theoretical']}], 'papers_2016_physical_activity': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2016, 'domain': ['physical activity', 'sleep', 'mental'], 'venue': ['CHI'], 'source': ['ACM'], 'contribution': ['empirical', 'artifact', 'theoretical']}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2016, 'domain': ['physical activity', 'food', 'mental'], 'venue': ['CHI'], 'source': ['ACM', 'IEEE'], 'contribution': ['empirical', 'artifact', 'theoretical']}]}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': [], 'var_functions.execute_python:24': [{'title': "When Fitness Trackers Don'T 'Fit': End-user Difficulties in the Assessment of Personal Tracking Device Accuracy", 'citation_count': 100}, {'title': 'Patina Engraver: Visualizing Activity Logs As Patina in Fashionable Trackers', 'citation_count': 96}, {'title': 'Low Sampling Rate for Physical Activity Recognition', 'citation_count': 88}, {'title': 'HealthyTogether: Exploring Social Incentives for Mobile Fitness Applications', 'citation_count': 75}, {'title': 'Persuasive Technology in the Real World: A Study of Long-term Use of Activity Sensing Devices for Fitness', 'citation_count': 72}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity', 'citation_count': 65}, {'title': 'SweatAtoms: Materializing Physical Activity', 'citation_count': 61}, {'title': 'Activity Tracking: Barriers, Workarounds and Customisation', 'citation_count': 60}, {'title': "But, I Don'T Take Steps: Examining the Inaccessibility of Fitness Trackers for Wheelchair Athletes", 'citation_count': 54}, {'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': 44}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity', 'citation_count': 39}, {'title': 'Affordances for Self-tracking Wearable Devices', 'citation_count': 36}, {'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'citation_count': 36}, {'title': 'Pass the Ball: Enforced Turn-Taking in Activity Tracking', 'citation_count': 32}, {'title': 'How Do We Engage with Activity Trackers?: A Longitudinal Study of Habito', 'citation_count': 29}, {'title': 'Goal-oriented Visualizations of Activity Tracking: A Case Study with Engineering Students', 'citation_count': 15}, {'title': 'Personalization Revisited: A Reflective Approach Helps People Better Personalize Health Services and Motivates Them to Increase Physical Activity', 'citation_count': 12}, {'title': 'Social Fabric Fitness: The Design and Evaluation of Wearable E-textile Displays to Support Group Running', 'citation_count': 3}]}

exec(code, env_args)
