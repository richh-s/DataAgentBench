code = """import json, re
# Load the list of candidate titles from previous storage
candidate_titles = var_call_HhnLtC85rrp0OUQYavEVGgyY
# Load paper_docs full collection to check year for these titles. We'll query the whole collection file from earlier big queries.
# We have multiple Mongo query result files: var_call_ueY8ny6tvVKcJ9NNvBSzXQv9, var_call_zQema5txZszizqodvhPu7Oxr, var_call_jiSj5ODYQsrRs6zMyYqQsuSt
paths = [var_call_ueY8ny6tvVKcJ9NNvBSzXQv9, var_call_zQema5txZszizqodvhPu7Oxr, var_call_jiSj5ODYQsrRs6zMyYqQsuSt]
all_docs = []
for p in paths:
    with open(p,'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
            all_docs.extend(data)
        except:
            pass

# Build a mapping from title (filename without .txt) to detected year in text
title_year = {}
for doc in all_docs:
    filename = doc.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text','')
    # find first 4-digit year
    years = re.findall(r"\b(19[5-9][0-9]|20[0-2][0-9]|2026)\b", text)
    year = int(years[0]) if years else None
    title_year[title] = year

# Now for each candidate title, check if its year ==2016
titles_2016 = []
for t in candidate_titles:
    # titles in citations may not exactly match filename casing/quotes; try to match by exact or by substring
    matched = None
    # direct match
    if t in title_year and title_year[t]==2016:
        matched = t
    else:
        # try to find any title in title_year that contains t or vice versa
        for k in title_year:
            if (t.lower() in k.lower() or k.lower() in t.lower()) and title_year[k]==2016:
                matched = k
                break
    if matched:
        titles_2016.append(matched)

print('__RESULT__:')
print(json.dumps(titles_2016))"""

env_args = {'var_call_ueY8ny6tvVKcJ9NNvBSzXQv9': 'file_storage/call_ueY8ny6tvVKcJ9NNvBSzXQv9.json', 'var_call_k4guTGoCsoObrR3VeZLLdU84': [], 'var_call_zQema5txZszizqodvhPu7Oxr': 'file_storage/call_zQema5txZszizqodvhPu7Oxr.json', 'var_call_akrROVWBvQUPsCMRHuNVpUJU': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None}], 'var_call_jiSj5ODYQsrRs6zMyYqQsuSt': 'file_storage/call_jiSj5ODYQsrRs6zMyYqQsuSt.json', 'var_call_1eCuQsCsWNeZ3DNvrZ81xW1q': [], 'var_call_XcSb27QbArGXyjoYM8rd2vqw': 'file_storage/call_XcSb27QbArGXyjoYM8rd2vqw.json', 'var_call_HhnLtC85rrp0OUQYavEVGgyY': ['Activity Tracking in Vivo', 'Patina Engraver: Visualizing Activity Logs As Patina in Fashionable Trackers', 'ThinkActive: Designing for Pseudonymous Activity Tracking in the Classroom', 'Scaffolding for an OLM for Long-Term Physical Activity Goals', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'When Fitness Meets Social Networks: Investigating Fitness Tracking and Social Practices on WeRun', 'Bringing New Voices to Design of Exercise Technology: Participatory Design with Vulnerable Young Adults', 'Sharing Automatically Tracked Activity Data: Implications for Therapists and People with Mobility Impairments', 'Pass the Ball: Enforced Turn-Taking in Activity Tracking', "But, I Don'T Take Steps: Examining the Inaccessibility of Fitness Trackers for Wheelchair Athletes", 'Persistent Sharing of Fitness App Status on Twitter', 'Supporting Meaningful Personal Fitness: The Tracker Goal Evolution Model', 'Prescribing 10,000 Steps Like Aspirin: Designing a Novel Interface for Data-Driven Medical Consultations', 'How Do We Engage with Activity Trackers?: A Longitudinal Study of Habito', 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'Goal-oriented Visualizations of Activity Tracking: A Case Study with Engineering Students', 'Social Fabric Fitness: The Design and Evaluation of Wearable E-textile Displays to Support Group Running', 'Persuasive Technology in the Real World: A Study of Long-term Use of Activity Sensing Devices for Fitness', 'Data Representations for In-situ Exploration of Health and Fitness Data', 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', 'Sharing Steps in the Workplace: Changing Privacy Concerns Over Time', 'TastyBeats: Designing Palatable Representations of Physical Activity', 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations', 'VRFit: An Interactive Dashboard for Visualising of Virtual Reality Exercise and Daily Step Data', 'Quantified Recess: Design of an Activity for Elementary Students Involving Analyses of Their Own Movement Data', 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'Low Sampling Rate for Physical Activity Recognition', 'Understanding Physical Activity Through 3D Printed Material Artifacts', 'Move into Another World of Happy: Insights for Designing Affect-based Physical Activity Interventions', "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure", 'HealthyTogether: Exploring Social Incentives for Mobile Fitness Applications', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', "When Fitness Trackers Don'T 'Fit': End-user Difficulties in the Assessment of Personal Tracking Device Accuracy", 'Sensor Requirements for Activity Recognition on Smart Watches', 'Family Health Promotion in Low-SES Neighborhoods: A Two-Month Study of Wearable Activity Tracking', 'Activity Tracking: Barriers, Workarounds and Customisation', 'SweatAtoms: Materializing Physical Activity', 'Fine-grained Sharing of Sensed Physical Activity: A Value Sensitive Approach', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'Facts, Interactivity and Videotape: Exploring the Design Space of Data in Interactive Video Storytelling', 'Personalization Revisited: A Reflective Approach Helps People Better Personalize Health Services and Motivates Them to Increase Physical Activity', 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace', 'Using Context to Reveal Factors That Affect Physical Activity']}

exec(code, env_args)
