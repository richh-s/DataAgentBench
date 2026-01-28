code = """import json, re

# Load docs and citations
with open(var_call_ws1qHHRIDiTRjx2sqZhKHXcB, 'r') as f:
    docs = json.load(f)
with open(var_call_Yu8sRfoQ9H0o3vvDRCE7U41m, 'r') as f:
    citations = json.load(f)

cit_map = {c['title']: int(c['total_citations']) for c in citations}

results = []

for doc in docs:
    filename = doc.get('filename', '')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text', '')
    # find year in first 2000 chars
    head = text[:2000]
    year = None
    m = re.search(r"\b(20\d{2})\b", head)
    if m:
        y = int(m.group(1))
        if 2000 <= y <= 2024:
            year = y
    if year is None:
        m = re.search(r"\b(20\d{2})\b", text)
        if m:
            y = int(m.group(1))
            if 2000 <= y <= 2024:
                year = y
    # domain detection
    domain = False
    if re.search(r'physical\s*activity', text, re.I):
        domain = True
    elif re.search(r'\bactivity\b', title, re.I):
        domain = True

    if year == 2016 and domain:
        total = cit_map.get(title, 0)
        results.append({'title': title, 'total_citations': total})

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_LoAS7jJZv6Hq2gHMPVDaMQ4s': [{'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt'}, {'filename': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt"}, {'filename': 'Charting Design Preferences on Wellness Wearables.txt'}], 'var_call_VHUBb79gMr7rnViIIojE4OH5': 'file_storage/call_VHUBb79gMr7rnViIIojE4OH5.json', 'var_call_FboBebDHKGnqk26qrfP9zZmQ': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': '265'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': '266'}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'total_citations': '636'}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'total_citations': '271'}, {'title': 'Charting Design Preferences on Wellness Wearables', 'total_citations': '269'}], 'var_call_8s45VOTlZ7fFiRIv2lpI8sa4': [], 'var_call_qXBai4BehGQP9gBldKW7gLfZ': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'Barriers to Engagement with a Personal Informatics Productivity Tool.txt'}], 'var_call_BmR7PU1bDpsdOZe8ClB6oF8P': 'file_storage/call_BmR7PU1bDpsdOZe8ClB6oF8P.json', 'var_call_6hcauF4anM5LdjfCuMtqyqqe': [{'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}, {'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt'}, {'filename': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt"}], 'var_call_N1kPFVPmsE1lTLgsJjAA5Xqt': [{'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}, {'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt'}, {'filename': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt"}], 'var_call_LspQyQbd0kcChbdh23YQrEF0': 'file_storage/call_LspQyQbd0kcChbdh23YQrEF0.json', 'var_call_Yu8sRfoQ9H0o3vvDRCE7U41m': 'file_storage/call_Yu8sRfoQ9H0o3vvDRCE7U41m.json', 'var_call_FjZbcaT06gi6SNopMqohEGS3': [], 'var_call_3sA9JLLgXWhZho2GAkvQPOMc': [{'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'total_citations': '221'}, {'title': 'Activity Tracking in Vivo', 'total_citations': '316'}, {'title': 'Activity Tracking: Barriers, Workarounds and Customisation', 'total_citations': '91'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'total_citations': '259'}, {'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'total_citations': '349'}, {'title': 'Facts, Interactivity and Videotape: Exploring the Design Space of Data in Interactive Video Storytelling', 'total_citations': '430'}, {'title': 'Family Health Promotion in Low-SES Neighborhoods: A Two-Month Study of Wearable Activity Tracking', 'total_citations': '400'}, {'title': 'Fine-grained Sharing of Sensed Physical Activity: A Value Sensitive Approach', 'total_citations': '98'}, {'title': 'Goal-oriented Visualizations of Activity Tracking: A Case Study with Engineering Students', 'total_citations': '339'}, {'title': 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'total_citations': '133'}, {'title': 'How Do We Engage with Activity Trackers?: A Longitudinal Study of Habito', 'total_citations': '367'}, {'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'total_citations': '316'}, {'title': 'Low Sampling Rate for Physical Activity Recognition', 'total_citations': '348'}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure", 'total_citations': '542'}, {'title': 'Move into Another World of Happy: Insights for Designing Affect-based Physical Activity Interventions', 'total_citations': '107'}, {'title': 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations', 'total_citations': '190'}, {'title': 'Pass the Ball: Enforced Turn-Taking in Activity Tracking', 'total_citations': '344'}, {'title': 'Patina Engraver: Visualizing Activity Logs As Patina in Fashionable Trackers', 'total_citations': '497'}, {'title': 'Personalization Revisited: A Reflective Approach Helps People Better Personalize Health Services and Motivates Them to Increase Physical Activity', 'total_citations': '12'}, {'title': 'Persuasive Technology in the Real World: A Study of Long-term Use of Activity Sensing Devices for Fitness', 'total_citations': '421'}, {'title': 'Quantified Recess: Design of an Activity for Elementary Students Involving Analyses of Their Own Movement Data', 'total_citations': '340'}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals', 'total_citations': '335'}, {'title': 'Sensor Requirements for Activity Recognition on Smart Watches', 'total_citations': '488'}, {'title': 'Sharing Automatically Tracked Activity Data: Implications for Therapists and People with Mobility Impairments', 'total_citations': '80'}, {'title': 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'total_citations': '404'}, {'title': 'SweatAtoms: Materializing Physical Activity', 'total_citations': '428'}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity', 'total_citations': '180'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', 'total_citations': '278'}, {'title': 'ThinkActive: Designing for Pseudonymous Activity Tracking in the Classroom', 'total_citations': '225'}, {'title': 'Understanding Physical Activity Through 3D Printed Material Artifacts', 'total_citations': '46'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity', 'total_citations': '358'}], 'var_call_ws1qHHRIDiTRjx2sqZhKHXcB': 'file_storage/call_ws1qHHRIDiTRjx2sqZhKHXcB.json'}

exec(code, env_args)
