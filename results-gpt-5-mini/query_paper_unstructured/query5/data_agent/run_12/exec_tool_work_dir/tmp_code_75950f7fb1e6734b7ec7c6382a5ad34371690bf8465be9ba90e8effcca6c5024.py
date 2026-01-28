code = """import json, re
path_citations = var_call_gFwFvyf3mPGfKL0vFQmrcJZX
path_papers = var_call_kcMrujPTFLPyK4epIvakeN2T

with open(path_citations, 'r', encoding='utf-8') as f:
    citations = json.load(f)
with open(path_papers, 'r', encoding='utf-8') as f:
    papers = json.load(f)

# Identify CHI papers by searching for CHI indicators in text
chi_indicators = [r"\bCHI\b", r"SIGCHI", r"Human Factors in Computing Systems", r"Proceedings of the.*CHI", r"ACM CHI", r"CHI Conference"]
chi_titles = set()
for doc in papers:
    filename = doc.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text','')
    for pat in chi_indicators:
        if re.search(pat, text, flags=re.IGNORECASE):
            chi_titles.add(title)
            break

# normalization function
import unicodedata
import string

def normalize(s):
    if s is None:
        return ''
    s = s.lower()
    # remove punctuation
    s = ''.join(ch if ch.isalnum() or ch.isspace() else ' ' for ch in s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

chi_norm = {normalize(t): t for t in chi_titles}

matched = []
total = 0
for rec in citations:
    title = rec.get('title')
    cc = rec.get('citation_count', 0)
    try:
        c = int(cc)
    except:
        try:
            c = int(float(cc))
        except:
            c = 0
    n = normalize(title)
    if n in chi_norm:
        matched.append({'title': title, 'citation_count': c})
        total += c

matched_sorted = sorted(matched, key=lambda x: x['citation_count'], reverse=True)

out = {'num_matched_papers': len(matched_sorted), 'total_citations_2020': total, 'papers': matched_sorted}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_gFwFvyf3mPGfKL0vFQmrcJZX': 'file_storage/call_gFwFvyf3mPGfKL0vFQmrcJZX.json', 'var_call_kcMrujPTFLPyK4epIvakeN2T': 'file_storage/call_kcMrujPTFLPyK4epIvakeN2T.json', 'var_call_vp4xBBEe2kesakgiwy8DfF37': {'papers': [], 'total_citations': 0, 'num_papers': 0}, 'var_call_H5IJRosiM6eRKeoFuFManJ5s': {'num_matching_docs': 99, 'sample_matches': [{'title': 'A Lived Informatics Model of Personal Informatics', 'matches': ['CHI']}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'matches': ['CHI']}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'matches': ['CHI']}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'matches': ['CHI', 'Human Factors in Computing Systems', 'ACM CHI']}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'matches': ['CHI', 'SIGCHI', 'Human Factors in Computing Systems', 'Proceedings of the.*CHI', 'CHI Conference']}, {'title': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'matches': ['CHI']}, {'title': 'Barriers to Engagement with a Personal Informatics Productivity Tool', 'matches': ['CHI', 'SIGCHI', 'Human Factors in Computing Systems']}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'matches': ['CHI', 'SIGCHI', 'Human Factors in Computing Systems', 'Proceedings of the.*CHI', 'CHI Conference']}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'matches': ['CHI', 'SIGCHI', 'Human Factors in Computing Systems', 'Proceedings of the.*CHI', 'CHI Conference']}, {'title': 'Blood Pressure Beyond the Clinic: Rethinking a Health Metric for Everyone', 'matches': ['CHI', 'ACM CHI']}, {'title': 'Charting Design Preferences on Wellness Wearables', 'matches': ['CHI', 'SIGCHI', 'Human Factors in Computing Systems', 'Proceedings of the.*CHI', 'CHI Conference']}, {'title': 'ClimbSense: Automatic Climbing Route Recognition Using Wrist-worn Inertia Measurement Units', 'matches': ['CHI']}, {'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'matches': ['CHI', 'SIGCHI', 'Human Factors in Computing Systems', 'Proceedings of the.*CHI', 'CHI Conference']}, {'title': 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings', 'matches': ['CHI', 'SIGCHI', 'Human Factors in Computing Systems', 'Proceedings of the.*CHI']}, {'title': 'Communicating Uncertainty in Fertility Prognosis', 'matches': ['CHI', 'SIGCHI', 'Human Factors in Computing Systems', 'Proceedings of the.*CHI', 'CHI Conference']}, {'title': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'matches': ['CHI']}, {'title': 'ConCap: Designing to Empower Individual Reflection on Chronic Conditions Using Mobile Apps', 'matches': ['CHI', 'SIGCHI']}, {'title': 'Contextual Influences on the Use and Non-Use of Digital Technology While Exercising at the Gym', 'matches': ['CHI']}, {'title': 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'matches': ['CHI', 'SIGCHI', 'Human Factors in Computing Systems', 'Proceedings of the.*CHI', 'CHI Conference']}, {'title': 'DataSelfie: Empowering People to Design Personalized Visuals to Represent Their Data', 'matches': ['CHI', 'SIGCHI', 'Human Factors in Computing Systems', 'Proceedings of the.*CHI', 'CHI Conference']}]}}

exec(code, env_args)
