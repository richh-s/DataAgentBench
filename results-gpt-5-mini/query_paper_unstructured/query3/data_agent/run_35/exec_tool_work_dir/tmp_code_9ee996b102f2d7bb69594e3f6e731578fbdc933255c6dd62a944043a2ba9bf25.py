code = """import json, re

# Load mongo empirical-only results
path_emp = var_call_8nYJxglQajgq19kPg0Q0Stjm
with open(path_emp, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Load citations aggregate
path_cit = var_call_wLc89tLLAQJxpXJLjZQRx4G8
with open(path_cit, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Build citations map (normalized title -> total_citations)
cit_map = {}
for c in citations:
    title = c.get('title')
    if title is None:
        continue
    t = title.strip()
    try:
        tc = int(c.get('total_citations'))
    except Exception:
        try:
            tc = int(float(c.get('total_citations')))
        except Exception:
            tc = None
    cit_map[t.lower()] = tc

results = []

year_pattern = re.compile(r"\b(20(?:17|18|19|20|21|22|23|24|25|26))\b")

for d in docs:
    text = d.get('text','') or ''
    if not isinstance(text, str):
        continue
    if not re.search(r"\bempirical\b", text, flags=re.IGNORECASE):
        continue
    # extract year
    y = None
    m = year_pattern.search(text)
    if m:
        y = int(m.group(1))
    # if no year, try to find 'CHI 2018' pattern
    if y is None:
        m2 = re.search(r"CHI\s*(\d{4})", text, flags=re.IGNORECASE)
        if m2:
            y = int(m2.group(1))
    if y is None:
        # last resort: find any 4-digit year between 2010 and 2026
        m3 = re.search(r"\b(20\d{2})\b", text)
        if m3:
            yy = int(m3.group(1))
            if 2010 <= yy <= 2026:
                y = yy
    if y is None:
        continue
    if y <= 2016:
        continue
    fn = d.get('filename') or ''
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    title = title.strip()
    tc = cit_map.get(title.lower())
    results.append({'title': title, 'total_citations': (None if tc is None else int(tc))})

import json as _json
print("__RESULT__:")
print(_json.dumps(results))"""

env_args = {'var_call_x3lcIfFpwdG8R83HKaR6vCyr': ['paper_docs'], 'var_call_dwPh5YwNHNe5FaYBiOE7aDyC': ['Citations', 'sqlite_sequence'], 'var_call_5Fr9YDfjdx1RAzPDo7Hd08hK': 'file_storage/call_5Fr9YDfjdx1RAzPDo7Hd08hK.json', 'var_call_wLc89tLLAQJxpXJLjZQRx4G8': 'file_storage/call_wLc89tLLAQJxpXJLjZQRx4G8.json', 'var_call_eYYMRXxLVzz1TMLLkatgnom2': [], 'var_call_1hdUw0yXPOESNwezuqTwymv5': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings', 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': 'Communicating Uncertainty in Fertility Prognosis', 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': 'Entangled with Numbers: Quantified Self and Others in a Team-Based Online Game', 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': 'Heed: Exploring the Design of Situated Self-Reporting Devices', 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': 'Making Sense of Sleep Sensors: How Sleep Sensing Technologies Support and Undermine Sleep Health', 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': 'Modeling Interdependent and Periodic Real-World Action Sequences', 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': 'No Forests Without Trees: Particulars and Patterns in Visualizing Personal Communication', 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': 'No Longer Wearing: Investigating the Abandonment of Personal Health-tracking Technologies on Craigslist', 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations', 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': 'Patient Perspectives on Self-Management Technologies for Chronic Fatigue Syndrome', 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': "Supporting Coping with Parkinson's Disease Through Self Tracking", 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System", 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': 'Trajectories of Engagement and Disengagement with a Story-Based Smoking Cessation App', 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': 'Turn to the Self in Human-Computer Interaction: Care of the Self in Negotiating the Human-Technology Relationship', 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': 'Understanding Animals: A Critical Challenge in ACI', 'year': None, 'has_empirical': False, 'has_empiric': False}, {'title': 'Understanding Personal Productivity: How Knowledge Workers Define, Evaluate, and Reflect on Their Productivity', 'year': None, 'has_empirical': False, 'has_empiric': False}], 'var_call_bgmcgpdnNdh948IHcgSb91lp': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': 265}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': 266}, {'title': 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings', 'total_citations': 402}, {'title': 'Communicating Uncertainty in Fertility Prognosis', 'total_citations': 264}, {'title': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'total_citations': 467}, {'title': 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'total_citations': 362}, {'title': 'Entangled with Numbers: Quantified Self and Others in a Team-Based Online Game', 'total_citations': 97}, {'title': 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'total_citations': 133}, {'title': 'Heed: Exploring the Design of Situated Self-Reporting Devices', 'total_citations': 153}, {'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'total_citations': 316}, {'title': 'Making Sense of Sleep Sensors: How Sleep Sensing Technologies Support and Undermine Sleep Health', 'total_citations': 327}, {'title': 'Modeling Interdependent and Periodic Real-World Action Sequences', 'total_citations': 296}, {'title': 'No Forests Without Trees: Particulars and Patterns in Visualizing Personal Communication', 'total_citations': 195}, {'title': 'No Longer Wearing: Investigating the Abandonment of Personal Health-tracking Technologies on Craigslist', 'total_citations': 131}, {'title': 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations', 'total_citations': 190}, {'title': 'Patient Perspectives on Self-Management Technologies for Chronic Fatigue Syndrome', 'total_citations': 268}, {'title': 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'total_citations': 404}, {'title': "Supporting Coping with Parkinson's Disease Through Self Tracking", 'total_citations': 191}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', 'total_citations': 278}, {'title': "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System", 'total_citations': 72}, {'title': 'Trajectories of Engagement and Disengagement with a Story-Based Smoking Cessation App', 'total_citations': 48}, {'title': 'Turn to the Self in Human-Computer Interaction: Care of the Self in Negotiating the Human-Technology Relationship', 'total_citations': 235}, {'title': 'Understanding Animals: A Critical Challenge in ACI', 'total_citations': 161}, {'title': 'Understanding Personal Productivity: How Knowledge Workers Define, Evaluate, and Reflect on Their Productivity', 'total_citations': 306}], 'var_call_8nYJxglQajgq19kPg0Q0Stjm': 'file_storage/call_8nYJxglQajgq19kPg0Q0Stjm.json'}

exec(code, env_args)
