code = """import json, re
with open(var_call_zqpzazna1jCnfKTTzQ6DPwWC, 'r', encoding='utf-8') as f:
    paper_docs = json.load(f)
with open(var_call_d589z7pHY5g3uVAtPA2Hxqvw, 'r', encoding='utf-8') as f:
    activity_citations = json.load(f)

cit_lookup = {rec['title'].strip(): int(rec['total_citations']) for rec in activity_citations}
results = []
for doc in paper_docs:
    filename = doc.get('filename','')
    text = doc.get('text','') or ''
    if not filename:
        continue
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    head = text[:800]
    year = None
    # search for any 4-digit year in header
    m = re.search(r'\b(19|20)\d{2}\b', head)
    if m:
        year = int(m.group(0))
    else:
        if re.search(r'\b2016\b', text):
            year = 2016
    # domain check
    domain_terms = ['physical activity', 'activity tracking', 'fitness', 'exercise', 'physicalactivity']
    is_physical = any(term in text.lower() for term in domain_terms)
    if year == 2016 and is_physical:
        tc = cit_lookup.get(title)
        if tc is None:
            def norm(s):
                return re.sub(r'[^A-Za-z0-9]', '', s).lower()
            ntitle = norm(title)
            for k,v in cit_lookup.items():
                if norm(k) == ntitle:
                    tc = v
                    break
        if tc is None:
            tc = 0
        results.append({'title': title, 'total_citations': tc})
# deduplicate
seen = set()
unique = []
for r in results:
    if r['title'] not in seen:
        seen.add(r['title'])
        unique.append(r)
print('__RESULT__:')
print(json.dumps(unique))"""

env_args = {'var_call_z44fGCrcdv8xi0cJHcIwkqeH': 'file_storage/call_z44fGCrcdv8xi0cJHcIwkqeH.json', 'var_call_9MgAY2bXiWE3HmFw3vDrjYJp': [], 'var_call_a7lRT9qkRRvzCoLIoTWBvXFu': 'file_storage/call_a7lRT9qkRRvzCoLIoTWBvXFu.json', 'var_call_I69hr4IoOVcu3F9cpYCfdYmn': 'file_storage/call_I69hr4IoOVcu3F9cpYCfdYmn.json', 'var_call_kxa12E2MxuHKbmWJXk3L8du3': [], 'var_call_zqpzazna1jCnfKTTzQ6DPwWC': 'file_storage/call_zqpzazna1jCnfKTTzQ6DPwWC.json', 'var_call_d589z7pHY5g3uVAtPA2Hxqvw': [{'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'total_citations': '221'}, {'title': 'Activity Tracking in Vivo', 'total_citations': '316'}, {'title': 'Activity Tracking: Barriers, Workarounds and Customisation', 'total_citations': '91'}, {'title': 'Bringing New Voices to Design of Exercise Technology: Participatory Design with Vulnerable Young Adults', 'total_citations': '419'}, {'title': "But, I Don'T Take Steps: Examining the Inaccessibility of Fitness Trackers for Wheelchair Athletes", 'total_citations': '554'}, {'title': 'Data Representations for In-situ Exploration of Health and Fitness Data', 'total_citations': '245'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'total_citations': '259'}, {'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'total_citations': '349'}, {'title': 'Facts, Interactivity and Videotape: Exploring the Design Space of Data in Interactive Video Storytelling', 'total_citations': '430'}, {'title': 'Family Health Promotion in Low-SES Neighborhoods: A Two-Month Study of Wearable Activity Tracking', 'total_citations': '400'}, {'title': 'Fine-grained Sharing of Sensed Physical Activity: A Value Sensitive Approach', 'total_citations': '98'}, {'title': 'Goal-oriented Visualizations of Activity Tracking: A Case Study with Engineering Students', 'total_citations': '339'}, {'title': 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'total_citations': '133'}, {'title': 'HealthyTogether: Exploring Social Incentives for Mobile Fitness Applications', 'total_citations': '340'}, {'title': 'How Do We Engage with Activity Trackers?: A Longitudinal Study of Habito', 'total_citations': '367'}, {'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'total_citations': '316'}, {'title': 'Low Sampling Rate for Physical Activity Recognition', 'total_citations': '348'}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure", 'total_citations': '542'}, {'title': 'Move into Another World of Happy: Insights for Designing Affect-based Physical Activity Interventions', 'total_citations': '107'}, {'title': 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations', 'total_citations': '190'}, {'title': 'Pass the Ball: Enforced Turn-Taking in Activity Tracking', 'total_citations': '344'}, {'title': 'Patina Engraver: Visualizing Activity Logs As Patina in Fashionable Trackers', 'total_citations': '497'}, {'title': 'Persistent Sharing of Fitness App Status on Twitter', 'total_citations': '462'}, {'title': 'Personalization Revisited: A Reflective Approach Helps People Better Personalize Health Services and Motivates Them to Increase Physical Activity', 'total_citations': '12'}, {'title': 'Persuasive Technology in the Real World: A Study of Long-term Use of Activity Sensing Devices for Fitness', 'total_citations': '421'}, {'title': 'Quantified Recess: Design of an Activity for Elementary Students Involving Analyses of Their Own Movement Data', 'total_citations': '340'}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals', 'total_citations': '335'}, {'title': 'Self-Reflection and Personal Physicalization Construction', 'total_citations': '80'}, {'title': 'Sensor Requirements for Activity Recognition on Smart Watches', 'total_citations': '488'}, {'title': 'Sharing Automatically Tracked Activity Data: Implications for Therapists and People with Mobility Impairments', 'total_citations': '80'}, {'title': 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'total_citations': '404'}, {'title': 'Social Fabric Fitness: The Design and Evaluation of Wearable E-textile Displays to Support Group Running', 'total_citations': '47'}, {'title': 'Supporting Meaningful Personal Fitness: The Tracker Goal Evolution Model', 'total_citations': '191'}, {'title': 'SweatAtoms: Materializing Physical Activity', 'total_citations': '428'}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity', 'total_citations': '180'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', 'total_citations': '278'}, {'title': 'ThinkActive: Designing for Pseudonymous Activity Tracking in the Classroom', 'total_citations': '225'}, {'title': 'Understanding Physical Activity Through 3D Printed Material Artifacts', 'total_citations': '46'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity', 'total_citations': '358'}, {'title': 'VRFit: An Interactive Dashboard for Visualising of Virtual Reality Exercise and Daily Step Data', 'total_citations': '441'}, {'title': 'When Fitness Meets Social Networks: Investigating Fitness Tracking and Social Practices on WeRun', 'total_citations': '276'}, {'title': "When Fitness Trackers Don'T 'Fit': End-user Difficulties in the Assessment of Personal Tracking Device Accuracy", 'total_citations': '155'}]}

exec(code, env_args)
