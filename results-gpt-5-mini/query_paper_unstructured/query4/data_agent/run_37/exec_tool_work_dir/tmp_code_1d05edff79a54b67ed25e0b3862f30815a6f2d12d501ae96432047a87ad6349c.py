code = """import json, re
# Load 2016 docs
with open(var_call_kfsh25XV4dUQLkhdsrTz3Wia, 'r', encoding='utf-8') as f:
    docs_2016 = json.load(f)
# Load aggregated citations (file path)
with open(var_call_I69hr4IoOVcu3F9cpYCfdYmn, 'r', encoding='utf-8') as f:
    citations_all = json.load(f)

# build citation dict with normalized titles
def norm(s):
    return re.sub(r'[^A-Za-z0-9]', '', s).lower()

cit_map = {}
for rec in citations_all:
    t = rec.get('title','').strip()
    tc = rec.get('total_citations', 0)
    try:
        tc_int = int(tc)
    except:
        try:
            tc_int = int(float(tc))
        except:
            tc_int = 0
    cit_map[norm(t)] = tc_int

results = []
for doc in docs_2016:
    filename = doc.get('filename','')
    text = doc.get('text','') or ''
    if not filename:
        continue
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    # detect year: look in first 500 chars for a 4-digit year
    head = text[:1000]
    year = None
    m = re.search(r"\b(19|20)\d{2}\b", head)
    if m:
        year = int(m.group(0))
    else:
        if re.search(r"\b2016\b", text):
            year = 2016
    # domain check for physical activity
    domain_terms = [r'physical\s*activity', r'activity tracking', r'fitness', r'exercise']
    is_physical = any(re.search(pat, text, flags=re.I) for pat in domain_terms)
    if year == 2016 and is_physical:
        tc = cit_map.get(norm(title), None)
        if tc is None:
            # try to find best match by substring
            for k,v in cit_map.items():
                if norm(title) in k or k in norm(title):
                    tc = v
                    break
        if tc is None:
            tc = 0
        results.append({'title': title, 'total_citations': tc})

# dedupe
seen=set(); unique=[]
for r in results:
    if r['title'] not in seen:
        seen.add(r['title']); unique.append(r)

print('__RESULT__:')
print(json.dumps(unique))"""

env_args = {'var_call_z44fGCrcdv8xi0cJHcIwkqeH': 'file_storage/call_z44fGCrcdv8xi0cJHcIwkqeH.json', 'var_call_9MgAY2bXiWE3HmFw3vDrjYJp': [], 'var_call_a7lRT9qkRRvzCoLIoTWBvXFu': 'file_storage/call_a7lRT9qkRRvzCoLIoTWBvXFu.json', 'var_call_I69hr4IoOVcu3F9cpYCfdYmn': 'file_storage/call_I69hr4IoOVcu3F9cpYCfdYmn.json', 'var_call_kxa12E2MxuHKbmWJXk3L8du3': [], 'var_call_zqpzazna1jCnfKTTzQ6DPwWC': 'file_storage/call_zqpzazna1jCnfKTTzQ6DPwWC.json', 'var_call_d589z7pHY5g3uVAtPA2Hxqvw': [{'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'total_citations': '221'}, {'title': 'Activity Tracking in Vivo', 'total_citations': '316'}, {'title': 'Activity Tracking: Barriers, Workarounds and Customisation', 'total_citations': '91'}, {'title': 'Bringing New Voices to Design of Exercise Technology: Participatory Design with Vulnerable Young Adults', 'total_citations': '419'}, {'title': "But, I Don'T Take Steps: Examining the Inaccessibility of Fitness Trackers for Wheelchair Athletes", 'total_citations': '554'}, {'title': 'Data Representations for In-situ Exploration of Health and Fitness Data', 'total_citations': '245'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'total_citations': '259'}, {'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'total_citations': '349'}, {'title': 'Facts, Interactivity and Videotape: Exploring the Design Space of Data in Interactive Video Storytelling', 'total_citations': '430'}, {'title': 'Family Health Promotion in Low-SES Neighborhoods: A Two-Month Study of Wearable Activity Tracking', 'total_citations': '400'}, {'title': 'Fine-grained Sharing of Sensed Physical Activity: A Value Sensitive Approach', 'total_citations': '98'}, {'title': 'Goal-oriented Visualizations of Activity Tracking: A Case Study with Engineering Students', 'total_citations': '339'}, {'title': 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'total_citations': '133'}, {'title': 'HealthyTogether: Exploring Social Incentives for Mobile Fitness Applications', 'total_citations': '340'}, {'title': 'How Do We Engage with Activity Trackers?: A Longitudinal Study of Habito', 'total_citations': '367'}, {'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'total_citations': '316'}, {'title': 'Low Sampling Rate for Physical Activity Recognition', 'total_citations': '348'}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure", 'total_citations': '542'}, {'title': 'Move into Another World of Happy: Insights for Designing Affect-based Physical Activity Interventions', 'total_citations': '107'}, {'title': 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations', 'total_citations': '190'}, {'title': 'Pass the Ball: Enforced Turn-Taking in Activity Tracking', 'total_citations': '344'}, {'title': 'Patina Engraver: Visualizing Activity Logs As Patina in Fashionable Trackers', 'total_citations': '497'}, {'title': 'Persistent Sharing of Fitness App Status on Twitter', 'total_citations': '462'}, {'title': 'Personalization Revisited: A Reflective Approach Helps People Better Personalize Health Services and Motivates Them to Increase Physical Activity', 'total_citations': '12'}, {'title': 'Persuasive Technology in the Real World: A Study of Long-term Use of Activity Sensing Devices for Fitness', 'total_citations': '421'}, {'title': 'Quantified Recess: Design of an Activity for Elementary Students Involving Analyses of Their Own Movement Data', 'total_citations': '340'}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals', 'total_citations': '335'}, {'title': 'Self-Reflection and Personal Physicalization Construction', 'total_citations': '80'}, {'title': 'Sensor Requirements for Activity Recognition on Smart Watches', 'total_citations': '488'}, {'title': 'Sharing Automatically Tracked Activity Data: Implications for Therapists and People with Mobility Impairments', 'total_citations': '80'}, {'title': 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'total_citations': '404'}, {'title': 'Social Fabric Fitness: The Design and Evaluation of Wearable E-textile Displays to Support Group Running', 'total_citations': '47'}, {'title': 'Supporting Meaningful Personal Fitness: The Tracker Goal Evolution Model', 'total_citations': '191'}, {'title': 'SweatAtoms: Materializing Physical Activity', 'total_citations': '428'}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity', 'total_citations': '180'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', 'total_citations': '278'}, {'title': 'ThinkActive: Designing for Pseudonymous Activity Tracking in the Classroom', 'total_citations': '225'}, {'title': 'Understanding Physical Activity Through 3D Printed Material Artifacts', 'total_citations': '46'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity', 'total_citations': '358'}, {'title': 'VRFit: An Interactive Dashboard for Visualising of Virtual Reality Exercise and Daily Step Data', 'total_citations': '441'}, {'title': 'When Fitness Meets Social Networks: Investigating Fitness Tracking and Social Practices on WeRun', 'total_citations': '276'}, {'title': "When Fitness Trackers Don'T 'Fit': End-user Difficulties in the Assessment of Personal Tracking Device Accuracy", 'total_citations': '155'}], 'var_call_pMqJ8mj0iwJfLkB5yqA9bCtQ': [], 'var_call_kfsh25XV4dUQLkhdsrTz3Wia': 'file_storage/call_kfsh25XV4dUQLkhdsrTz3Wia.json', 'var_call_nl95nyvMPSBNdvI7Bdlp48F1': ['A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'Charting Design Preferences on Wellness Wearables', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings', 'Communicating Uncertainty in Fertility Prognosis', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'DataSelfie: Empowering People to Design Personalized Visuals to Represent Their Data', 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'Designing in the Dark: Eliciting Self-tracking Dimensions for Understanding Enigmatic Disease', 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance', 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats', 'Entangled with Numbers: Quantified Self and Others in a Team-Based Online Game', 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'How Information Sharing About Care Recipients by Family Caregivers Impacts Family Communication', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps", 'Leveraging Intermediated Interactions to Support Utilization of Persuasive Personal Health Informatics', 'Making Sense of Sleep Sensors: How Sleep Sensing Technologies Support and Undermine Sleep Health', 'Modeling Interdependent and Periodic Real-World Action Sequences', "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure", 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations', 'Patient Perspectives on Self-Management Technologies for Chronic Fatigue Syndrome', 'Personal Tracking of Screen Time on Digital Devices', 'Predicting Interruptibility for Manual Data Collection: A Cluster-based User Model', 'Quantified Factory Worker: Designing a Worker Feedback Dashboard', 'Quantified Self Meets Social Media: Sharing of Weight Updates on Twitter', 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis', 'Scaffolding for an OLM for Long-Term Physical Activity Goals', 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace', "Supporting Coping with Parkinson's Disease Through Self Tracking", 'Supporting Meaningful Personal Fitness: The Tracker Goal Evolution Model', 'Technologies for Everyday Life Reflection: Illustrating a Design Space', 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', "The 'Self' As Barrier for Self-Management Technologies in Healthcare?", "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System", 'Trajectories of Engagement and Disengagement with a Story-Based Smoking Cessation App', 'Turn to the Self in Human-Computer Interaction: Care of the Self in Negotiating the Human-Technology Relationship', 'Understanding Animals: A Critical Challenge in ACI', 'Understanding Personal Productivity: How Knowledge Workers Define, Evaluate, and Reflect on Their Productivity', 'Visual ODLs: Co-Designing Patient-Generated Observations of Daily Living to Support Data-Driven Conversations in Pediatric Care', 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating']}

exec(code, env_args)
