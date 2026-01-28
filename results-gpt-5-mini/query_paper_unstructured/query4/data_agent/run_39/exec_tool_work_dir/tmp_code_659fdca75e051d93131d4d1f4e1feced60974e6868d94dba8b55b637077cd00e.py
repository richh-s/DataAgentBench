code = """import json, re
# Load Mongo query results for selected filenames
path_docs = var_call_EV6UhbkYTkpdLTSPn1umOiFh
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)
# Load citations aggregated totals
path_cit = var_call_dUI72YM2tUPWqWc9noXwOSUb
with open(path_cit, 'r', encoding='utf-8') as f:
    citations = json.load(f)
# build map of title->total_citations (int)
cit_map = {c['title']: int(c['total_citations']) for c in citations}

# domain keywords
domain_kw = ['physical activity', 'activity tracker', 'activity trackers', 'activity tracking', 'physical activities', 'fitness', 'exercise']

results = []
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    text_low = text.lower()
    # detect publication year 2016
    year2016 = bool(re.search(r"\b2016\b", text))
    # detect domain
    domain_match = any(kw in text_low for kw in domain_kw)
    if year2016 and domain_match:
        total_cit = cit_map.get(title)
        if total_cit is None:
            # try some normalized matches
            for k in cit_map.keys():
                if k.lower() == title.lower():
                    total_cit = cit_map[k]; break
        results.append({"title": title, "total_citations": total_cit if total_cit is not None else None})

# Remove duplicates
seen = set(); uniq = []
for r in results:
    if r['title'] not in seen:
        seen.add(r['title']); uniq.append(r)

print("__RESULT__:")
print(json.dumps(uniq))"""

env_args = {'var_call_R3Jsc9jJ2f081nEgJYmXt0we': 'file_storage/call_R3Jsc9jJ2f081nEgJYmXt0we.json', 'var_call_CRWoBTvRBnOAaxGATytfY7eg': [], 'var_call_DX5qm54njXAG3VA8Ns0XT0CT': 'file_storage/call_DX5qm54njXAG3VA8Ns0XT0CT.json', 'var_call_oa0IkubHrYmUaxkc3inyJOzE': [], 'var_call_ypSCdY3MpucsmohKpzfZVJau': 'file_storage/call_ypSCdY3MpucsmohKpzfZVJau.json', 'var_call_zeocturV7lV5Q3GfltpOhPo8': [], 'var_call_nX85GeNenY1UOFZPNHgqMvho': ['Citations', 'sqlite_sequence'], 'var_call_dUI72YM2tUPWqWc9noXwOSUb': 'file_storage/call_dUI72YM2tUPWqWc9noXwOSUb.json', 'var_call_HS0tHZMzux3t4ZnYFl8gaUgi': [{'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'total_citations': 221}, {'title': 'Activity Tracking in Vivo', 'total_citations': 316}, {'title': 'Activity Tracking: Barriers, Workarounds and Customisation', 'total_citations': 91}, {'title': 'Bringing New Voices to Design of Exercise Technology: Participatory Design with Vulnerable Young Adults', 'total_citations': 419}, {'title': "But, I Don'T Take Steps: Examining the Inaccessibility of Fitness Trackers for Wheelchair Athletes", 'total_citations': 554}, {'title': 'Data Representations for In-situ Exploration of Health and Fitness Data', 'total_citations': 245}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'total_citations': 259}, {'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'total_citations': 349}, {'title': 'Facts, Interactivity and Videotape: Exploring the Design Space of Data in Interactive Video Storytelling', 'total_citations': 430}, {'title': 'Family Health Promotion in Low-SES Neighborhoods: A Two-Month Study of Wearable Activity Tracking', 'total_citations': 400}, {'title': 'Fine-grained Sharing of Sensed Physical Activity: A Value Sensitive Approach', 'total_citations': 98}, {'title': 'Goal-oriented Visualizations of Activity Tracking: A Case Study with Engineering Students', 'total_citations': 339}, {'title': 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'total_citations': 133}, {'title': 'HealthyTogether: Exploring Social Incentives for Mobile Fitness Applications', 'total_citations': 340}, {'title': 'How Do We Engage with Activity Trackers?: A Longitudinal Study of Habito', 'total_citations': 367}, {'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'total_citations': 316}, {'title': 'Low Sampling Rate for Physical Activity Recognition', 'total_citations': 348}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure", 'total_citations': 542}, {'title': 'Move into Another World of Happy: Insights for Designing Affect-based Physical Activity Interventions', 'total_citations': 107}, {'title': 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations', 'total_citations': 190}, {'title': 'Pass the Ball: Enforced Turn-Taking in Activity Tracking', 'total_citations': 344}, {'title': 'Patina Engraver: Visualizing Activity Logs As Patina in Fashionable Trackers', 'total_citations': 497}, {'title': 'Persistent Sharing of Fitness App Status on Twitter', 'total_citations': 462}, {'title': 'Personalization Revisited: A Reflective Approach Helps People Better Personalize Health Services and Motivates Them to Increase Physical Activity', 'total_citations': 12}, {'title': 'Persuasive Technology in the Real World: A Study of Long-term Use of Activity Sensing Devices for Fitness', 'total_citations': 421}, {'title': 'Quantified Recess: Design of an Activity for Elementary Students Involving Analyses of Their Own Movement Data', 'total_citations': 340}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals', 'total_citations': 335}, {'title': 'Sensor Requirements for Activity Recognition on Smart Watches', 'total_citations': 488}, {'title': 'Sharing Automatically Tracked Activity Data: Implications for Therapists and People with Mobility Impairments', 'total_citations': 80}, {'title': 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'total_citations': 404}, {'title': 'Social Fabric Fitness: The Design and Evaluation of Wearable E-textile Displays to Support Group Running', 'total_citations': 47}, {'title': 'Supporting Meaningful Personal Fitness: The Tracker Goal Evolution Model', 'total_citations': 191}, {'title': 'SweatAtoms: Materializing Physical Activity', 'total_citations': 428}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity', 'total_citations': 180}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', 'total_citations': 278}, {'title': 'ThinkActive: Designing for Pseudonymous Activity Tracking in the Classroom', 'total_citations': 225}, {'title': 'Understanding Physical Activity Through 3D Printed Material Artifacts', 'total_citations': 46}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity', 'total_citations': 358}, {'title': 'VRFit: An Interactive Dashboard for Visualising of Virtual Reality Exercise and Daily Step Data', 'total_citations': 441}, {'title': 'When Fitness Meets Social Networks: Investigating Fitness Tracking and Social Practices on WeRun', 'total_citations': 276}, {'title': "When Fitness Trackers Don'T 'Fit': End-user Difficulties in the Assessment of Personal Tracking Device Accuracy", 'total_citations': 155}], 'var_call_EV6UhbkYTkpdLTSPn1umOiFh': 'file_storage/call_EV6UhbkYTkpdLTSPn1umOiFh.json'}

exec(code, env_args)
