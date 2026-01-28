code = """import json
fp = var_call_M1jpQmPozSELv6uoJLSU56ly
with open(fp, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Build a dict for quick lookup
cit_dict = {c['title']: int(c['total_citations']) for c in citations}

# Load paper docs to find empirical papers after 2016
fp2 = var_call_B722YM6cJSlUDr6ypsTpU1Yg
with open(fp2, 'r', encoding='utf-8') as f:
    docs = json.load(f)

results = []
for d in docs:
    filename = d.get('filename','')
    title = filename[:-4] if filename.endswith('.txt') else filename
    text = d.get('text','') or ''
    low = text.lower()
    if 'empir' not in low:
        continue
    # try to extract publication year
    import re
    years = re.findall(r"\b(19\d{2}|20\d{2})\b", text)
    years_int = sorted(set([int(y) for y in years if 1900 <= int(y) <= 2026]))
    pub_year = years_int[0] if years_int else None
    if pub_year and pub_year > 2016:
        total_citations = cit_dict.get(title)
        if total_citations is None:
            # try with different spacing or quotes
            alt = title.replace('"','').strip()
            total_citations = cit_dict.get(alt)
        if total_citations is None:
            # couldn't find citation data
            total_citations = None
        results.append({'title': title, 'year': pub_year, 'total_citations': total_citations})

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_B722YM6cJSlUDr6ypsTpU1Yg': 'file_storage/call_B722YM6cJSlUDr6ypsTpU1Yg.json', 'var_call_RxOG1HVxK3CTMUeMoESWjDWa': [], 'var_call_6hd0kHjAYhvGArwOs55dpgml': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'years_found': [], 'first_year': None}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'years_found': [], 'first_year': None}, {'title': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'years_found': [], 'first_year': None}, {'title': 'Charting Design Preferences on Wellness Wearables', 'years_found': [], 'first_year': None}, {'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'years_found': [], 'first_year': None}, {'title': 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings', 'years_found': [], 'first_year': None}, {'title': 'Communicating Uncertainty in Fertility Prognosis', 'years_found': [], 'first_year': None}, {'title': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'years_found': [], 'first_year': None}, {'title': 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'years_found': [], 'first_year': None}, {'title': 'Entangled with Numbers: Quantified Self and Others in a Team-Based Online Game', 'years_found': [], 'first_year': None}, {'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'years_found': [], 'first_year': None}, {'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'years_found': [], 'first_year': None}, {'title': 'Fine-grained Sharing of Sensed Physical Activity: A Value Sensitive Approach', 'years_found': [], 'first_year': None}, {'title': 'From Nobody Cares to Way to Go!: A Design Framework for Social Sharing in Personal Informatics', 'years_found': [], 'first_year': None}, {'title': 'Goal-oriented Visualizations of Activity Tracking: A Case Study with Engineering Students', 'years_found': [], 'first_year': None}, {'title': 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'years_found': [], 'first_year': None}, {'title': 'Heed: Exploring the Design of Situated Self-Reporting Devices', 'years_found': [], 'first_year': None}, {'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'years_found': [], 'first_year': None}, {'title': 'Intelligent Computing in Personal Informatics: Key Design Considerations', 'years_found': [], 'first_year': None}, {'title': 'Leveraging Intermediated Interactions to Support Utilization of Persuasive Personal Health Informatics', 'years_found': [], 'first_year': None}, {'title': 'Making Sense of Sleep Sensors: How Sleep Sensing Technologies Support and Undermine Sleep Health', 'years_found': [], 'first_year': None}, {'title': 'Modeling Interdependent and Periodic Real-World Action Sequences', 'years_found': [], 'first_year': None}, {'title': 'MoodLight: Exploring Personal and Social Implications of Ambient Display of Biosensor Data', 'years_found': [], 'first_year': None}, {'title': 'No Forests Without Trees: Particulars and Patterns in Visualizing Personal Communication', 'years_found': [], 'first_year': None}, {'title': 'No Longer Wearing: Investigating the Abandonment of Personal Health-tracking Technologies on Craigslist', 'years_found': [], 'first_year': None}, {'title': 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations', 'years_found': [], 'first_year': None}, {'title': 'Patient Perspectives on Self-Management Technologies for Chronic Fatigue Syndrome', 'years_found': [], 'first_year': None}, {'title': 'Personal Tracking of Screen Time on Digital Devices', 'years_found': [], 'first_year': None}, {'title': 'Personalization Revisited: A Reflective Approach Helps People Better Personalize Health Services and Motivates Them to Increase Physical Activity', 'years_found': [], 'first_year': None}, {'title': 'Quantified Self Meets Social Media: Sharing of Weight Updates on Twitter', 'years_found': [], 'first_year': None}, {'title': 'QuittyLink: Using Smartphones for Personal Counseling to Help People Quit Smoking', 'years_found': [], 'first_year': None}, {'title': 'Real-life Experiences with an Adaptive Light Bracelet', 'years_found': [], 'first_year': None}, {'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'years_found': [], 'first_year': None}, {'title': 'Reviewing Reflection: On the Use of Reflection in Interactive System Design', 'years_found': [], 'first_year': None}, {'title': 'Sitting in the Same Boat: A Case Study of a Combined Awareness System and Behaviour Change Technology', 'years_found': [], 'first_year': None}, {'title': 'SleepTight: Low-burden, Self-monitoring Technology for Capturing and Reflecting on Sleep Behaviors', 'years_found': [], 'first_year': None}, {'title': 'Social (Media) Jet Lag: How Usage of Social Technology Can Modulate and Reflect Circadian Rhythms', 'years_found': [], 'first_year': None}, {'title': 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'years_found': [], 'first_year': None}, {'title': "Supporting Coping with Parkinson's Disease Through Self Tracking", 'years_found': [], 'first_year': None}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', 'years_found': [], 'first_year': None}, {'title': "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System", 'years_found': [], 'first_year': None}, {'title': 'Tiny Habits in the Giant Enterprise: Understanding the Dynamics of a Quantified Workplace', 'years_found': [], 'first_year': None}, {'title': 'Trajectories of Engagement and Disengagement with a Story-Based Smoking Cessation App', 'years_found': [], 'first_year': None}, {'title': 'Turn to the Self in Human-Computer Interaction: Care of the Self in Negotiating the Human-Technology Relationship', 'years_found': [], 'first_year': None}, {'title': 'Understanding Animals: A Critical Challenge in ACI', 'years_found': [], 'first_year': None}, {'title': 'Understanding Personal Productivity: How Knowledge Workers Define, Evaluate, and Reflect on Their Productivity', 'years_found': [], 'first_year': None}, {'title': "We'Ve Bin Watching You: Designing for Reflection and Social Persuasion to Promote Sustainable Lifestyles", 'years_found': [], 'first_year': None}, {'title': 'What Health Topics Older Adults Want to Track: A Participatory Design Study', 'years_found': [], 'first_year': None}], 'var_call_bS5ywk92K7AY8xa1A8pjk7j7': [], 'var_call_M1jpQmPozSELv6uoJLSU56ly': 'file_storage/call_M1jpQmPozSELv6uoJLSU56ly.json'}

exec(code, env_args)
