code = """import json
path_mongo = var_call_5Fr9YDfjdx1RAzPDo7Hd08hK
path_cit = var_call_wLc89tLLAQJxpXJLjZQRx4G8

with open(path_mongo, 'r', encoding='utf-8') as f:
    docs = json.load(f)
with open(path_cit, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# build citation map
cit_map = {}
for c in citations:
    title = c.get('title')
    if title is None:
        continue
    # normalize whitespace
    t = title.strip()
    # convert total_citations to int when possible
    try:
        tc = int(c.get('total_citations'))
    except Exception:
        try:
            tc = int(float(c.get('total_citations')))
        except Exception:
            tc = None
    cit_map[t] = tc

# collect titles from mongo docs
titles = []
for d in docs:
    fn = d.get('filename')
    if not fn:
        continue
    t = fn
    if t.lower().endswith('.txt'):
        t = t[:-4]
    t = t.strip()
    if t not in titles:
        titles.append(t)

# build output
output = []
for t in titles:
    tc = cit_map.get(t)
    if tc is None:
        # try alternative matchings: some titles in citations may have different quotes or whitespace
        # try to find case-insensitive match
        match = None
        for k in cit_map.keys():
            if k.lower() == t.lower():
                match = k
                break
        if match:
            tc = cit_map.get(match)
    output.append({'title': t, 'total_citations': (None if tc is None else int(tc))})

import json as _json
print("__RESULT__:")
print(_json.dumps(output))"""

env_args = {'var_call_x3lcIfFpwdG8R83HKaR6vCyr': ['paper_docs'], 'var_call_dwPh5YwNHNe5FaYBiOE7aDyC': ['Citations', 'sqlite_sequence'], 'var_call_5Fr9YDfjdx1RAzPDo7Hd08hK': 'file_storage/call_5Fr9YDfjdx1RAzPDo7Hd08hK.json', 'var_call_wLc89tLLAQJxpXJLjZQRx4G8': 'file_storage/call_wLc89tLLAQJxpXJLjZQRx4G8.json', 'var_call_eYYMRXxLVzz1TMLLkatgnom2': [], 'var_call_1hdUw0yXPOESNwezuqTwymv5': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings', 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': 'Communicating Uncertainty in Fertility Prognosis', 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': 'Entangled with Numbers: Quantified Self and Others in a Team-Based Online Game', 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': 'Heed: Exploring the Design of Situated Self-Reporting Devices', 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': 'Making Sense of Sleep Sensors: How Sleep Sensing Technologies Support and Undermine Sleep Health', 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': 'Modeling Interdependent and Periodic Real-World Action Sequences', 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': 'No Forests Without Trees: Particulars and Patterns in Visualizing Personal Communication', 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': 'No Longer Wearing: Investigating the Abandonment of Personal Health-tracking Technologies on Craigslist', 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations', 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': 'Patient Perspectives on Self-Management Technologies for Chronic Fatigue Syndrome', 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': "Supporting Coping with Parkinson's Disease Through Self Tracking", 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System", 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': 'Trajectories of Engagement and Disengagement with a Story-Based Smoking Cessation App', 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': 'Turn to the Self in Human-Computer Interaction: Care of the Self in Negotiating the Human-Technology Relationship', 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': 'Understanding Animals: A Critical Challenge in ACI', 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': 'Understanding Personal Productivity: How Knowledge Workers Define, Evaluate, and Reflect on Their Productivity', 'year': None, 'has_empirical': False, 'has_empiric': False}]}

exec(code, env_args)
