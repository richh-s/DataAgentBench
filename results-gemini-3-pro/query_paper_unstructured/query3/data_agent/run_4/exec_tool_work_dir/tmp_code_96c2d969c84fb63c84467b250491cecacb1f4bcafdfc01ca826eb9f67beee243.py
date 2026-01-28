code = """import json
import re

docs_path = locals()['var_function-call-7183910782658905231']
citations_path = locals()['var_function-call-1716571983847186930']

with open(docs_path, 'r') as f:
    docs = json.load(f)

with open(citations_path, 'r') as f:
    citations_list = json.load(f)

citation_map = {}
for item in citations_list:
    val = item['total_citations']
    if val is None:
        val = 0
    citation_map[item['title']] = int(val)

results = []
year_pattern = re.compile(r'\b(20\d{2})\b')

for doc in docs:
    title = doc['filename'].replace('.txt', '')
    text = doc.get('text', '')
    if not text:
        continue
        
    stripped_text = text.strip()
    
    # Extract year from first 2000 chars of stripped text
    head = stripped_text[:2000]
    matches = year_pattern.findall(head)
    valid_years = [int(y) for y in matches if 2000 <= int(y) <= 2025]
    
    if not valid_years:
        continue
    
    # Pick first year
    pub_year = valid_years[0]
    
    # Constraint: published AFTER 2016 (i.e. >= 2017)
    if pub_year > 2016:
        # Check contribution
        if 'empirical' in text.lower():
            count = citation_map.get(title, 0)
            results.append({"title": title, "citation_count": count})

# If still empty, debug
if not results:
    # Print debug for one doc
    doc = docs[0]
    t = doc.get('text', '').strip()[:1000]
    m = year_pattern.findall(t)
    print(f"DEBUG: Doc 0 matches: {m}")
else:
    print("__RESULT__:")
    print(json.dumps(results))"""

env_args = {'var_function-call-2488897031636296364': 'file_storage/function-call-2488897031636296364.json', 'var_function-call-2488897031636298801': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-13084840739219341064': 'file_storage/function-call-13084840739219341064.json', 'var_function-call-11712304195294590657': 'file_storage/function-call-11712304195294590657.json', 'var_function-call-14759133979912557114': [{'count(*)': '1405'}], 'var_function-call-1716571983847186930': 'file_storage/function-call-1716571983847186930.json', 'var_function-call-6824277840340661163': [], 'var_function-call-178942177689054954': [{'title': 'A Lived Informatics Model of Personal Informatics', 'years_found': [], 'pub_year': None, 'has_empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'years_found': [], 'pub_year': None, 'has_empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'years_found': [], 'pub_year': None, 'has_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'years_found': [], 'pub_year': None, 'has_empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'years_found': [], 'pub_year': None, 'has_empirical': False}, {'title': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'years_found': [], 'pub_year': None, 'has_empirical': True}, {'title': 'Barriers to Engagement with a Personal Informatics Productivity Tool', 'years_found': [], 'pub_year': None, 'has_empirical': False}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'years_found': [], 'pub_year': None, 'has_empirical': False}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'years_found': [], 'pub_year': None, 'has_empirical': False}, {'title': 'Blood Pressure Beyond the Clinic: Rethinking a Health Metric for Everyone', 'years_found': [], 'pub_year': None, 'has_empirical': False}, {'title': 'Charting Design Preferences on Wellness Wearables', 'years_found': [], 'pub_year': None, 'has_empirical': True}, {'title': 'ClimbSense: Automatic Climbing Route Recognition Using Wrist-worn Inertia Measurement Units', 'years_found': [], 'pub_year': None, 'has_empirical': False}, {'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'years_found': [], 'pub_year': None, 'has_empirical': True}, {'title': 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings', 'years_found': [], 'pub_year': None, 'has_empirical': True}, {'title': 'Communicating Uncertainty in Fertility Prognosis', 'years_found': [], 'pub_year': None, 'has_empirical': True}, {'title': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'years_found': [], 'pub_year': None, 'has_empirical': True}, {'title': 'ConCap: Designing to Empower Individual Reflection on Chronic Conditions Using Mobile Apps', 'years_found': [], 'pub_year': None, 'has_empirical': False}, {'title': 'Contextual Influences on the Use and Non-Use of Digital Technology While Exercising at the Gym', 'years_found': [], 'pub_year': None, 'has_empirical': False}, {'title': 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'years_found': [], 'pub_year': None, 'has_empirical': False}, {'title': 'DataSelfie: Empowering People to Design Personalized Visuals to Represent Their Data', 'years_found': [], 'pub_year': None, 'has_empirical': False}], 'var_function-call-15958983164615655688': {'matches': []}, 'var_function-call-9574412683836725906': 'done', 'var_function-call-4471664899404326616': 'done', 'var_function-call-7183910782658905231': 'file_storage/function-call-7183910782658905231.json', 'var_function-call-10066388550283772544': [], 'var_function-call-14026525895019555224': [{'title': 'A Lived Informatics Model of Personal Informatics', 'pub_year': None, 'is_empirical': False, 'years_found': [], 'text_len': 68339}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'pub_year': None, 'is_empirical': False, 'years_found': [], 'text_len': 63309}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'pub_year': None, 'is_empirical': True, 'years_found': [], 'text_len': 54376}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'pub_year': None, 'is_empirical': True, 'years_found': [], 'text_len': 74850}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'pub_year': None, 'is_empirical': False, 'years_found': [], 'text_len': 73461}, {'title': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'pub_year': None, 'is_empirical': True, 'years_found': [], 'text_len': 27658}, {'title': 'Barriers to Engagement with a Personal Informatics Productivity Tool', 'pub_year': None, 'is_empirical': False, 'years_found': [], 'text_len': 72635}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'pub_year': None, 'is_empirical': False, 'years_found': [], 'text_len': 30774}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'pub_year': None, 'is_empirical': False, 'years_found': [], 'text_len': 85065}, {'title': 'Blood Pressure Beyond the Clinic: Rethinking a Health Metric for Everyone', 'pub_year': None, 'is_empirical': False, 'years_found': [], 'text_len': 58639}], 'var_function-call-17986035673947587349': 'done'}

exec(code, env_args)
