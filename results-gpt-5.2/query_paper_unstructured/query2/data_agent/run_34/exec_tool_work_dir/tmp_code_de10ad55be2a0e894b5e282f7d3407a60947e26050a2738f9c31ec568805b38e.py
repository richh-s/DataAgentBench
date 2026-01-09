code = """import json

# recompute final average using previously loaded info by reloading quickly
cit_path = var_call_lhFvPE9YVBHGdn7iY52xvBz3
with open(cit_path, 'r', encoding='utf-8') as f:
    citations = json.load(f)

docs_path = var_call_euNumx1ZaLA6zKpMsVbVsWUY
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

import re
pat_acm = re.compile(r"\bACM\b|Association for Computing Machinery|acm\.org", re.IGNORECASE)
acm_titles = set()
for d in docs:
    fn = d.get('filename','') or ''
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    if pat_acm.search(d.get('text','') or ''):
        acm_titles.add(title)

counts = []
for r in citations:
    if r.get('title') in acm_titles:
        try:
            counts.append(int(r.get('citation_count')))
        except Exception:
            pass

avg = sum(counts)/len(counts) if counts else None
out = {"average_citation_count_2018_for_acm_papers": avg}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_lhFvPE9YVBHGdn7iY52xvBz3': 'file_storage/call_lhFvPE9YVBHGdn7iY52xvBz3.json', 'var_call_euNumx1ZaLA6zKpMsVbVsWUY': 'file_storage/call_euNumx1ZaLA6zKpMsVbVsWUY.json', 'var_call_frI3g49aDo4ZLwjJpiMnKgcp': {'acm_papers_with_2018_citations': 0, 'average_2018_citation_count': None}, 'var_call_OS6vTeguw3FAMLpbq9GIorl9': {'n_docs': 99, 'n_acm_docs_detected': 82, 'n_2018_citation_rows': 158, 'n_matches': 47, 'avg': 60.765957446808514, 'sample_matches': ['A Lived Informatics Model of Personal Informatics', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'Blood Pressure Beyond the Clinic: Rethinking a Health Metric for Everyone', 'Charting Design Preferences on Wellness Wearables', 'ClimbSense: Automatic Climbing Route Recognition Using Wrist-worn Inertia Measurement Units', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'ConCap: Designing to Empower Individual Reflection on Chronic Conditions Using Mobile Apps', 'Contextual Influences on the Use and Non-Use of Digital Technology While Exercising at the Gym', 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats', 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'From Nobody Cares to Way to Go!: A Design Framework for Social Sharing in Personal Informatics', 'FutureSelf: What Happens When We Forecast Self-Trackers? Future Health Statuses?', 'How to Drive a London Bus: Measuring Performance in a Mobile and Remote Workplace', 'Intelligent Computing in Personal Informatics: Key Design Considerations', "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps"]}}

exec(code, env_args)
