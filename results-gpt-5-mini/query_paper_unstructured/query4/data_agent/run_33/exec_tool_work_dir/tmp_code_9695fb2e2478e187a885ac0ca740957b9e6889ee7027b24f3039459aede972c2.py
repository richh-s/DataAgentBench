code = """import json
# Load citations match list
with open(var_call_MzzADZNImqH9RoHFLYlI1nWB, 'r', encoding='utf-8') as f:
    pa_matches = json.load(f)

# Load full paper docs
with open(var_call_MofUK2m03WbBxbNaWInNuQUc, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Build a set of titles to find
titles_set = set([r['title'] for r in pa_matches])

found = []
for d in docs:
    filename = d.get('filename','')
    title = filename.rsplit('.txt',1)[0]
    if title in titles_set:
        # try to extract year from header (first 200 chars)
        text = d.get('text') or ''
        import re
        m = re.search(r"\b(19|20)\d{2}\b", text[:300])
        year = int(m.group(0)) if m else None
        found.append({'title': title, 'filename': filename, 'year': year})

print('__RESULT__:')
print(json.dumps(found))"""

env_args = {'var_call_MofUK2m03WbBxbNaWInNuQUc': 'file_storage/call_MofUK2m03WbBxbNaWInNuQUc.json', 'var_call_CVUkhUcAwiQzAT1X9ezOtb8s': [], 'var_call_8e2mPHQzlupulgcMsl5j9Fx8': 'file_storage/call_8e2mPHQzlupulgcMsl5j9Fx8.json', 'var_call_1dqZJPG8Xcds5IamNQEwYsx4': [], 'var_call_FGeeAyPEj8L6Pq4zzkFbmoSo': ['Citations', 'sqlite_sequence'], 'var_call_CI4flWKd1V2IDGAGR2Msmp2L': 'file_storage/call_CI4flWKd1V2IDGAGR2Msmp2L.json', 'var_call_MzzADZNImqH9RoHFLYlI1nWB': [{'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'total_citations': 221}, {'title': 'Activity Tracking in Vivo', 'total_citations': 316}, {'title': 'Activity Tracking: Barriers, Workarounds and Customisation', 'total_citations': 91}, {'title': 'Bringing New Voices to Design of Exercise Technology: Participatory Design with Vulnerable Young Adults', 'total_citations': 419}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'total_citations': 259}, {'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'total_citations': 349}, {'title': 'Facts, Interactivity and Videotape: Exploring the Design Space of Data in Interactive Video Storytelling', 'total_citations': 430}, {'title': 'Family Health Promotion in Low-SES Neighborhoods: A Two-Month Study of Wearable Activity Tracking', 'total_citations': 400}, {'title': 'Fine-grained Sharing of Sensed Physical Activity: A Value Sensitive Approach', 'total_citations': 98}, {'title': 'Goal-oriented Visualizations of Activity Tracking: A Case Study with Engineering Students', 'total_citations': 339}, {'title': 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'total_citations': 133}, {'title': 'How Do We Engage with Activity Trackers?: A Longitudinal Study of Habito', 'total_citations': 367}, {'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'total_citations': 316}, {'title': 'Low Sampling Rate for Physical Activity Recognition', 'total_citations': 348}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure", 'total_citations': 542}, {'title': 'Move into Another World of Happy: Insights for Designing Affect-based Physical Activity Interventions', 'total_citations': 107}, {'title': 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations', 'total_citations': 190}, {'title': 'Pass the Ball: Enforced Turn-Taking in Activity Tracking', 'total_citations': 344}, {'title': 'Patina Engraver: Visualizing Activity Logs As Patina in Fashionable Trackers', 'total_citations': 497}, {'title': 'Personalization Revisited: A Reflective Approach Helps People Better Personalize Health Services and Motivates Them to Increase Physical Activity', 'total_citations': 12}, {'title': 'Persuasive Technology in the Real World: A Study of Long-term Use of Activity Sensing Devices for Fitness', 'total_citations': 421}, {'title': 'Quantified Recess: Design of an Activity for Elementary Students Involving Analyses of Their Own Movement Data', 'total_citations': 340}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals', 'total_citations': 335}, {'title': 'Sensor Requirements for Activity Recognition on Smart Watches', 'total_citations': 488}, {'title': 'Sharing Automatically Tracked Activity Data: Implications for Therapists and People with Mobility Impairments', 'total_citations': 80}, {'title': 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'total_citations': 404}, {'title': 'SweatAtoms: Materializing Physical Activity', 'total_citations': 428}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity', 'total_citations': 180}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', 'total_citations': 278}, {'title': 'ThinkActive: Designing for Pseudonymous Activity Tracking in the Classroom', 'total_citations': 225}, {'title': 'Understanding Physical Activity Through 3D Printed Material Artifacts', 'total_citations': 46}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity', 'total_citations': 358}, {'title': 'VRFit: An Interactive Dashboard for Visualising of Virtual Reality Exercise and Daily Step Data', 'total_citations': 441}]}

exec(code, env_args)
