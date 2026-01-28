code = """import json, re

# Load citations data
citations_path = locals()['var_functions.query_db:46']
with open(citations_path, 'r') as f:
    citations_raw = json.load(f)

# Create citation lookup dictionary
citations_dict = {}
for item in citations_raw:
    citations_dict[item['title']] = int(item['total_citations'])

# Load papers data
papers_path = locals()['var_functions.query_db:52']
with open(papers_path, 'r') as f:
    papers_raw = json.load(f)

print('Processing', len(papers_raw), 'papers')

empirical_papers = []

for paper in papers_raw:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '').strip()
    
    if title not in citations_dict:
        continue
    
    years = re.findall(r'\b(201[0-9]|202[0-9])\b', text)
    if not years:
        continue
        
    year = max([int(y) for y in years])
    if year <= 2016:
        continue
    
    text_lower = text.lower()
    has_empirical = False
    
    # Check empirical keywords
    if 'empirical' in text_lower:
        has_empirical = True
    
    # Check for study/research keywords
    if not has_empirical:
        study_words = ['user study', 'field study', 'interview', 'experiment', 'evaluation', 'survey', 'participant']
        for word in study_words:
            if word in text_lower:
                has_empirical = True
                break
    
    if has_empirical:
        empirical_papers.append({
            'title': title,
            'year': year,
            'total_citations': citations_dict[title]
        })

print('Found', len(empirical_papers), 'empirical papers after 2016')

# Sort by citations
empirical_papers.sort(key=lambda x: x['total_citations'], reverse=True)

result = {
    'papers': empirical_papers,
    'total_count': len(empirical_papers)
}

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_functions.query_db:0': [{'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86e', 'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}, {'_id': '694f5530284b10b11dc0a873', 'filename': 'Charting Design Preferences on Wellness Wearables.txt'}, {'_id': '694f5530284b10b11dc0a875', 'filename': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt"}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.execute_python:16': {'total_processed': 99, 'empirical_after_2016': 0, 'sample_empirical': []}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:22': {'total_papers': 4, 'empirical_papers_after_2016': 0, 'papers': []}, 'var_functions.query_db:24': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity'}, {'title': 'Why We Use and Abandon Smart Devices'}, {'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App'}, {'title': 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set'}, {'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application"}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App'}, {'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization"}, {'title': 'Reviewing Reflection: On the Use of Reflection in Interactive System Design'}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching"}, {'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers'}, {'title': 'No Forests Without Trees: Particulars and Patterns in Visualizing Personal Communication'}, {'title': 'Beyond Self-Tracking and Reminders: Designing Smartphone Apps That Support Habit Formation'}, {'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection'}, {'title': 'Barriers to Engagement with a Personal Informatics Productivity Tool'}, {'title': 'Modeling Interdependent and Periodic Real-World Action Sequences'}, {'title': 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video'}, {'title': 'How to Drive a London Bus: Measuring Performance in a Mobile and Remote Workplace'}], 'var_functions.query_db:26': [{'title': "Everybody Knows What You'Re Doing: A Critical Design Approach to Personal Informatics", 'total_citations': '694'}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'total_citations': '636'}, {'title': 'Contextual Influences on the Use and Non-Use of Digital Technology While Exercising at the Gym', 'total_citations': '595'}, {'title': 'See Friendship, Sort of: How Conversation and Digital Traces Might Support Reflection on Friendships', 'total_citations': '593'}, {'title': 'Shifting Dynamics or Breaking Sacred Traditions?: The Role of Technology in Twelve-step Fellowships', 'total_citations': '587'}, {'title': 'ClimbSense: Automatic Climbing Route Recognition Using Wrist-worn Inertia Measurement Units', 'total_citations': '557'}, {'title': "It Feels Like I'm Managing Myself: HIV+ People Tracking Their Personal Health Information", 'total_citations': '556'}, {'title': "But, I Don'T Take Steps: Examining the Inaccessibility of Fitness Trackers for Wheelchair Athletes", 'total_citations': '554'}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure", 'total_citations': '542'}, {'title': 'Anxiety and Autism: Towards Personalized Digital Health', 'total_citations': '520'}, {'title': 'Go and Grow: Mapping Personal Data to a Living Plant', 'total_citations': '500'}, {'title': 'Patina Engraver: Visualizing Activity Logs As Patina in Fashionable Trackers', 'total_citations': '497'}, {'title': 'Leveraging Intermediated Interactions to Support Utilization of Persuasive Personal Health Informatics', 'total_citations': '492'}, {'title': 'Designing for Self-Tracking of Emotion and Experience with Tangible Modality', 'total_citations': '491'}, {'title': "We'Ve Bin Watching You: Designing for Reflection and Social Persuasion to Promote Sustainable Lifestyles", 'total_citations': '489'}, {'title': 'Sensor Requirements for Activity Recognition on Smart Watches', 'total_citations': '488'}, {'title': "Toss 'N' Turn: Smartphone As Sleep and Sleep Quality Detector", 'total_citations': '484'}, {'title': 'Personal Informatics in Chronic Illness Management', 'total_citations': '484'}, {'title': 'The Irony and Re-interpretation of Our Quantified Self', 'total_citations': '481'}, {'title': 'Everything We Do, Everything We Press: Data-Driven Remote Performance Management in a Mobile Workplace', 'total_citations': '476'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:30': {'papers': []}, 'var_functions.execute_python:36': {'total_papers': 0, 'after_2016': 0, 'sample': []}, 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.execute_python:48': {'empirical_papers': [], 'count': 0}, 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json'}

exec(code, env_args)
