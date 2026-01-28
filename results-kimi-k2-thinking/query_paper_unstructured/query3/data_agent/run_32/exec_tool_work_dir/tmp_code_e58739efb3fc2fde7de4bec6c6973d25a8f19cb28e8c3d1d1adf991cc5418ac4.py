code = """import json
import re

# Load data
mongo_data = locals()['var_functions.query_db:164']
citations = locals()['var_functions.query_db:160']

# Convert from file paths if needed
if isinstance(mongo_data, str) and mongo_data.endswith('.json'):
    mongo_path = mongo_data
    with open(mongo_path, 'r') as f:
        mongo_data = json.load(f)

if isinstance(citations, str) and citations.endswith('.json'):
    citation_path = citations
    with open(citation_path, 'r') as f:
        citations = json.load(f)

print('Loaded MongoDB papers:', len(mongo_data))
print('Loaded citation records:', len(citations))

# Build citation map for fast lookup
citation_map = {}
for cit in citations:
    citation_map[cit['title']] = int(cit['total_citations'])

# Find papers meeting criteria
results = []

for doc in mongo_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename or not text:
        continue
    
    title = filename.replace('.txt', '')
    
    # Extract year from text
    year = None
    
    # Pattern 1: Venue format like CHI '17, UbiComp '15
    venue_match = re.search(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
    if venue_match:
        year = 2000 + int(venue_match.group(1))
    else:
        # Pattern 2: Full year like 2017, 2018
        year_match = re.search(r"\b(20\d{2})\b", text)
        if year_match:
            year = int(year_match.group(1))
    
    # Check if paper has empirical contribution
    text_lower = text.lower()
    has_empirical = 'empirical' in text_lower or 'empirically' in text_lower
    
    # Apply filters
    if year and year > 2016 and has_empirical:
        # Check if we have citation data
        if title in citation_map:
            results.append({
                'title': title,
                'total_citations': citation_map[title]
            })

# Sort by citations descending
results.sort(key=lambda x: x['total_citations'], reverse=True)

print('Found papers meeting criteria:', len(results))

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.execute_python:38': {'papers': [], 'count': 0}, 'var_functions.execute_python:52': [], 'var_functions.execute_python:66': [], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.execute_python:76': [], 'var_functions.execute_python:80': [], 'var_functions.execute_python:84': [], 'var_functions.execute_python:88': [], 'var_functions.execute_python:96': [], 'var_functions.execute_python:100': [], 'var_functions.execute_python:110': [], 'var_functions.execute_python:116': [], 'var_functions.execute_python:120': [], 'var_functions.execute_python:124': [], 'var_functions.execute_python:130': [], 'var_functions.execute_python:134': [], 'var_functions.execute_python:138': [], 'var_functions.execute_python:140': [], 'var_functions.execute_python:146': [], 'var_functions.execute_python:150': [], 'var_functions.execute_python:152': [], 'var_functions.execute_python:156': [], 'var_functions.execute_python:158': [], 'var_functions.query_db:160': [{'title': '"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'total_citations': '53'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'total_citations': '313'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'total_citations': '390'}, {'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'total_citations': '368'}, {'title': 'A Situated Exploration of Designing for Personal Health Ecosystems Through Data-enabled Design', 'total_citations': '277'}, {'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'total_citations': '221'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'total_citations': '220'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': '265'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': '266'}, {'title': 'Activity Tracking in Vivo', 'total_citations': '316'}, {'title': 'Activity Tracking: Barriers, Workarounds and Customisation', 'total_citations': '91'}, {'title': 'Affordances for Self-tracking Wearable Devices', 'total_citations': '195'}, {'title': 'An Anxious Alliance', 'total_citations': '370'}, {'title': 'An Empirical Exploration of Mindfulness Design Using Solo Travel Domain', 'total_citations': '352'}, {'title': 'Anxiety and Autism: Towards Personalized Digital Health', 'total_citations': '520'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'total_citations': '452'}, {'title': 'Armbeta: Towards Accessible Wearable Technology to Quantify Upper Limb Movement and Activities', 'total_citations': '317'}, {'title': 'Balancing Accuracy and Fun: Designing Camera Based Mobile Games for Implicit Heart Rate Monitoring', 'total_citations': '345'}, {'title': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'total_citations': '270'}, {'title': 'Barriers to Engagement with a Personal Informatics Productivity Tool', 'total_citations': '306'}, {'title': 'Beacon: Designing a Portable Device for Self-Administering a Measure of Critical Flicker Frequency', 'total_citations': '307'}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'total_citations': '636'}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'total_citations': '271'}, {'title': 'Beyond Self-Tracking and Reminders: Designing Smartphone Apps That Support Habit Formation', 'total_citations': '144'}, {'title': 'Blood Pressure Beyond the Clinic: Rethinking a Health Metric for Everyone', 'total_citations': '200'}, {'title': 'Boundary Negotiating Artifacts in Personal Informatics: Patient-Provider Collaboration with Patient-Generated Data', 'total_citations': '240'}, {'title': 'Bringing New Voices to Design of Exercise Technology: Participatory Design with Vulnerable Young Adults', 'total_citations': '419'}, {'title': "But, I Don'T Take Steps: Examining the Inaccessibility of Fitness Trackers for Wheelchair Athletes", 'total_citations': '554'}, {'title': 'Can SAL Support Self Reflection for Health and Nutrition?', 'total_citations': '450'}, {'title': 'Caring Through Data: Attending to the Social and Emotional Experiences of Health Datafication', 'total_citations': '189'}, {'title': 'Charting Design Preferences on Wellness Wearables', 'total_citations': '269'}, {'title': 'ClimbSense: Automatic Climbing Route Recognition Using Wrist-worn Inertia Measurement Units', 'total_citations': '557'}, {'title': 'Clinical Data in Context: Towards Sensemaking Tools for Interpreting Personal Health Data', 'total_citations': '150'}, {'title': 'Closing the Feedback Loop: A 12-month Evaluation of ASTA, a Self-Tracking Application for ASHAs', 'total_citations': '197'}, {'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'total_citations': '466'}, {'title': 'Co-Designing Food Trackers with Dietitians: Identifying Design Opportunities for Food Tracker Customization', 'total_citations': '424'}, {'title': 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings', 'total_citations': '402'}, {'title': 'Communicating Uncertainty in Fertility Prognosis', 'total_citations': '264'}, {'title': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'total_citations': '467'}, {'title': 'ConCap: Designing to Empower Individual Reflection on Chronic Conditions Using Mobile Apps', 'total_citations': '240'}, {'title': 'Contextual Influences on the Use and Non-Use of Digital Technology While Exercising at the Gym', 'total_citations': '595'}, {'title': 'Crafting a View of Self-Tracking Data in the Clinical Visit', 'total_citations': '367'}, {'title': 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'total_citations': '153'}, {'title': 'Data Representations for In-situ Exploration of Health and Fitness Data', 'total_citations': '245'}, {'title': 'Data, Data Everywhere, and Still Too Hard to Link: Insights from User Interactions with Diabetes Apps', 'total_citations': '298'}, {'title': 'DataSelfie: Empowering People to Design Personalized Visuals to Represent Their Data', 'total_citations': '50'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'total_citations': '259'}, {'title': 'Design Considerations for Semi-automated Tracking: Self-care Plans in Spinal Cord Injury', 'total_citations': '126'}, {'title': 'Design Opportunities in Three Stages of Relationship Development Between Users and Self-Tracking Devices', 'total_citations': '343'}, {'title': 'Design Recommendations for Self-Monitoring in the Workplace: Studies in Software Development', 'total_citations': '392'}], 'var_functions.list_db:162': ['paper_docs'], 'var_functions.query_db:164': 'file_storage/functions.query_db:164.json'}

exec(code, env_args)
