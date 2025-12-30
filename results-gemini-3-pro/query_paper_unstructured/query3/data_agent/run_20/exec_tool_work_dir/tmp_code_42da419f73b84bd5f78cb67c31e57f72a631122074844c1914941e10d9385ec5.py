code = """import json
import re

# Load citations
with open(locals()['var_function-call-389901141376174398'], 'r') as f:
    citations_data = json.load(f)
citation_map = {item['title']: int(item['total_citations']) for item in citations_data}

# Load papers
with open(locals()['var_function-call-14157823481537147433'], 'r') as f:
    papers_data = json.load(f)

candidates = []

for paper in papers_data:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename

    # Find year in first 3000 chars
    match = re.search(r'20\d{2}', text[:3000])
    year = int(match.group(0)) if match else 0
    
    if year > 2016:
        has_empirical = 'empirical' in text.lower()
        in_citation_map = title in citation_map
        
        if has_empirical:
            # This is a match!
            candidates.append({
                "title": title,
                "total_citation_count": citation_map.get(title, 0),
                "debug_year": year,
                "in_map": in_citation_map
            })

print("__RESULT__:")
print(json.dumps(candidates))"""

env_args = {'var_function-call-11261961701334828073': ['paper_docs'], 'var_function-call-11261961701334829364': 'file_storage/function-call-11261961701334829364.json', 'var_function-call-11261961701334830655': ['Citations', 'sqlite_sequence'], 'var_function-call-11261961701334827850': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}], 'var_function-call-8802837961524065341': 'file_storage/function-call-8802837961524065341.json', 'var_function-call-389901141376174398': 'file_storage/function-call-389901141376174398.json', 'var_function-call-389901141376172653': 'file_storage/function-call-389901141376172653.json', 'var_function-call-8584235094798493494': [], 'var_function-call-10819417574072414189': [], 'var_function-call-18354289230382980981': ['Num citations: 259', 'Num papers: 5', {'title': 'A Lived Informatics Model of Personal Informatics', 'year': 2015, 'has_empirical': False, 'snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n"}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': 0, 'has_empirical': False, 'snippet': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Hum'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 0, 'has_empirical': True, 'snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Anima'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 0, 'has_empirical': True, 'snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n '}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': 0, 'has_empirical': False, 'snippet': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation '}], 'var_function-call-14157823481537147433': 'file_storage/function-call-14157823481537147433.json', 'var_function-call-3479710015239140496': [], 'var_function-call-15036682914001922687': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'year': 2015, 'has_empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'year': 0, 'has_empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'year': 0, 'has_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'year': 0, 'has_empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'year': 0, 'has_empirical': False}, {'title': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt', 'year': 0, 'has_empirical': True}, {'title': 'Barriers to Engagement with a Personal Informatics Productivity Tool.txt', 'year': 0, 'has_empirical': False}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt', 'year': 0, 'has_empirical': False}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt", 'year': 0, 'has_empirical': False}, {'title': 'Blood Pressure Beyond the Clinic: Rethinking a Health Metric for Everyone.txt', 'year': 0, 'has_empirical': False}, {'title': 'Charting Design Preferences on Wellness Wearables.txt', 'year': 0, 'has_empirical': True}, {'title': 'ClimbSense: Automatic Climbing Route Recognition Using Wrist-worn Inertia Measurement Units.txt', 'year': 0, 'has_empirical': False}, {'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt", 'year': 0, 'has_empirical': True}, {'title': 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings.txt', 'year': 0, 'has_empirical': True}, {'title': 'Communicating Uncertainty in Fertility Prognosis.txt', 'year': 0, 'has_empirical': True}, {'title': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media.txt', 'year': 0, 'has_empirical': True}, {'title': 'ConCap: Designing to Empower Individual Reflection on Chronic Conditions Using Mobile Apps.txt', 'year': 0, 'has_empirical': False}, {'title': 'Contextual Influences on the Use and Non-Use of Digital Technology While Exercising at the Gym.txt', 'year': 0, 'has_empirical': False}, {'title': 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness.txt', 'year': 0, 'has_empirical': False}, {'title': 'DataSelfie: Empowering People to Design Personalized Visuals to Represent Their Data.txt', 'year': 2001, 'has_empirical': False}], 'var_function-call-10824880202292723999': [[2015, 21], [2018, 18], [0, 13], [2016, 10], [2019, 8], [2017, 8], [2014, 6], [2013, 5], [2012, 4], [2011, 2], [2010, 1], [2001, 1], [2006, 1], [2030, 1]]}

exec(code, env_args)
