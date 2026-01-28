code = """import json, re
# Load MongoDB query results for selected filenames
path_mongo = var_call_Bn0SjlGDfCrnA96M9GUeEp6Y
with open(path_mongo, 'r', encoding='utf-8') as f:
    mongo_records = json.load(f)

# Load citation totals grouped by title
path_cit = var_call_MLumbxhqVF3nCqRedTvljr8a
with open(path_cit, 'r', encoding='utf-8') as f:
    cit_records = json.load(f)

cit_dict = {}
for rec in cit_records:
    title = rec.get('title','')
    total = rec.get('total_citations', None)
    try:
        total_int = int(total) if total is not None else None
    except:
        try:
            total_int = int(float(total))
        except:
            total_int = None
    cit_dict[title] = total_int

results = []
seen = set()
for rec in mongo_records:
    filename = rec.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = rec.get('text','')
    if not re.search(r'physical activity', text, flags=re.I):
        continue
    # check for 2016 in header (first 1000 chars) or anywhere indicating publication
    head = text[:1200]
    pub2016 = False
    if re.search(r"\b2016\b", head):
        pub2016 = True
    if not pub2016:
        # look for CHI'16 or CHI 2016 or 'CHI'16' patterns anywhere in text
        if re.search(r"CHI\s*'?16|CHI\s*2016", text):
            pub2016 = True
        elif re.search(r"\b2016\b", text):
            pub2016 = True
    if pub2016:
        if title in seen:
            continue
        seen.add(title)
        # find matching title in citation dict (exact match)
        total = cit_dict.get(title)
        # sometimes citation titles in DB may include different punctuation; try simple normalization
        if total is None:
            # try to find by lower-case match
            for t,k in cit_dict.items():
                if t.lower() == title.lower():
                    total = k
                    break
        results.append({"title": title, "total_citations": total})

# Sort by title
results = sorted(results, key=lambda x: (x['title'] or '').lower())
print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_R6gwTreaDcfvqovoD3OXntlB': 'file_storage/call_R6gwTreaDcfvqovoD3OXntlB.json', 'var_call_SoNIw3qUMrpUQj9KJImwD4pv': [], 'var_call_KIGFc7rvmzz7P8e6jgdMDxDI': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'years': [], 'has_physical_activity': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'years': [], 'has_physical_activity': True}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'years': [], 'has_physical_activity': True}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'years': [], 'has_physical_activity': True}, {'title': 'Charting Design Preferences on Wellness Wearables', 'years': [], 'has_physical_activity': True}], 'var_call_xY5jFhX2kmhWZxFrIZamyzd8': ['Citations', 'sqlite_sequence'], 'var_call_MLumbxhqVF3nCqRedTvljr8a': 'file_storage/call_MLumbxhqVF3nCqRedTvljr8a.json', 'var_call_4mFzuOqu9whawkhIoJrvVOOs': 'file_storage/call_4mFzuOqu9whawkhIoJrvVOOs.json', 'var_call_rbAUDp58fKuBnmBYq4rrtpcj': [], 'var_call_kgbNG1J2fHoAUV0gB0LsOZaJ': ['A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity.txt', 'Activity Tracking in Vivo.txt', 'Activity Tracking: Barriers, Workarounds and Customisation.txt', 'Affordances for Self-tracking Wearable Devices.txt', 'Armbeta: Towards Accessible Wearable Technology to Quantify Upper Limb Movement and Activities.txt', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt', 'Beyond Self-Tracking and Reminders: Designing Smartphone Apps That Support Habit Formation.txt', 'Bringing New Voices to Design of Exercise Technology: Participatory Design with Vulnerable Young Adults.txt', "But, I Don'T Take Steps: Examining the Inaccessibility of Fitness Trackers for Wheelchair Athletes.txt", 'Closing the Feedback Loop: A 12-month Evaluation of ASTA, a Self-Tracking Application for ASHAs.txt', 'Co-Designing Food Trackers with Dietitians: Identifying Design Opportunities for Food Tracker Customization.txt', 'Crafting a View of Self-Tracking Data in the Clinical Visit.txt', 'Data Representations for In-situ Exploration of Health and Fitness Data.txt', 'Defining Adherence: Making Sense of Physical Activity Tracker Data.txt', 'Design Considerations for Semi-automated Tracking: Self-care Plans in Spinal Cord Injury.txt', 'Design Opportunities in Three Stages of Relationship Development Between Users and Self-Tracking Devices.txt', 'Designing for Self-Tracking of Emotion and Experience with Tangible Modality.txt', 'Designing in the Dark: Eliciting Self-tracking Dimensions for Understanding Enigmatic Disease.txt', 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance.txt', 'Engaging with Health Data: The Interplay Between Self-Tracking Activities and Emotions in Fertility Struggles.txt', 'Examining Menstrual Tracking to Inform the Design of Personal Informatics Tools.txt', 'Examining Self-Tracking by People with Migraine: Goals, Needs, and Opportunities in a Chronic Health Condition.txt', 'Expanding the Locus of Control: Design of a Mobile Quantified Self-Tracking Application for Whiplash Patients.txt', 'Exploring the Data Tracking and Sharing Preferences of Wheelchair Athletes.txt', 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers.txt', 'Exploring the Value of Parent Tracked Baby Data in Interactions with Healthcare Professionals: A Data-Enabled Design Exploration.txt', 'Facts, Interactivity and Videotape: Exploring the Design Space of Data in Interactive Video Storytelling.txt', 'Family Health Promotion in Low-SES Neighborhoods: A Two-Month Study of Wearable Activity Tracking.txt', 'Finding the Right Fit: Understanding Health Tracking in Workplace Wellness Programs.txt', 'Fine-grained Sharing of Sensed Physical Activity: A Value Sensitive Approach.txt', 'Flexible and Mindful Self-Tracking: Design Implications from Paper Bullet Journals.txt', 'FootStriker: An EMS-based Foot Strike Assistant for Running.txt', 'Fostering User Engagement: Improving Sense of Identity Through Cosmetic Customization in Wearable Trackers.txt', 'FutureSelf: What Happens When We Forecast Self-Trackers? Future Health Statuses?.txt', 'Gamification for Self-Tracking: From World of Warcraft to the Design of Personal Informatics Systems.txt', 'Goal-oriented Visualizations of Activity Tracking: A Case Study with Engineering Students.txt', 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal.txt', 'HealthyTogether: Exploring Social Incentives for Mobile Fitness Applications.txt', 'How Do We Engage with Activity Trackers?: A Longitudinal Study of Habito.txt', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application.txt", 'In Bed with Technology: Challenges and Opportunities for Sleep Tracking.txt', "It Feels Like I'm Managing Myself: HIV+ People Tracking Their Personal Health Information.txt", 'Low Sampling Rate for Physical Activity Recognition.txt', "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure.txt", 'Move into Another World of Happy: Insights for Designing Affect-based Physical Activity Interventions.txt', 'MyFootCare: A Mobile Self-tracking Tool to Promote Self-care Amongst People with Diabetic Foot Ulcers.txt', 'No Longer Wearing: Investigating the Abandonment of Personal Health-tracking Technologies on Craigslist.txt', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App.txt', 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations.txt', 'Pass the Ball: Enforced Turn-Taking in Activity Tracking.txt', 'Patina Engraver: Visualizing Activity Logs As Patina in Fashionable Trackers.txt', 'Persistent Sharing of Fitness App Status on Twitter.txt', 'Personal Tracking As Lived Informatics.txt', 'Personal Tracking of Screen Time on Digital Devices.txt', 'Personalization Revisited: A Reflective Approach Helps People Better Personalize Health Services and Motivates Them to Increase Physical Activity.txt', 'Persuasive Technology in the Real World: A Study of Long-term Use of Activity Sensing Devices for Fitness.txt', 'Prescribing 10,000 Steps Like Aspirin: Designing a Novel Interface for Data-Driven Medical Consultations.txt', 'Quantified Factory Worker - Expert Evaluation and Ethical Considerations of Wearable Self-tracking Devices.txt', 'Quantified Recess: Design of an Activity for Elementary Students Involving Analyses of Their Own Movement Data.txt', 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis.txt', 'Scaffolding for an OLM for Long-Term Physical Activity Goals.txt', 'Self-Reflection and Personal Physicalization Construction.txt', 'Self-tracking Cultures: Towards a Sociology of Personal Informatics.txt', 'Self-tracking for Mental Wellness: Understanding Expert Perspectives and Student Experiences.txt', 'Sensor Requirements for Activity Recognition on Smart Watches.txt', 'Sharing Automatically Tracked Activity Data: Implications for Therapists and People with Mobility Impairments.txt', 'Sharing Steps in the Workplace: Changing Privacy Concerns Over Time.txt', 'Shifting Dynamics or Breaking Sacred Traditions?: The Role of Technology in Twelve-step Fellowships.txt', 'Sleep Tracking in the Real World: A Qualitative Study into Barriers for Improving Sleep.txt', 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video.txt', 'Social Fabric Fitness: The Design and Evaluation of Wearable E-textile Displays to Support Group Running.txt', 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace.txt', "Supporting Collaborative Health Tracking in the Hospital: Patients' Perspectives.txt", "Supporting Coping with Parkinson's Disease Through Self Tracking.txt", 'Supporting Learning by Considering Emotions: Tracking and Visualization a Case Study.txt', 'Supporting Meaningful Personal Fitness: The Tracker Goal Evolution Model.txt', 'SweatAtoms: Materializing Physical Activity.txt', 'TastyBeats: Designing Palatable Representations of Physical Activity.txt', 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices.txt', "Things You Don'T Want to Know About Yourself: Ambivalence About Tracking and Sharing Personal Information for Behaviour Change.txt", 'ThinkActive: Designing for Pseudonymous Activity Tracking in the Classroom.txt', 'Understanding Physical Activity Through 3D Printed Material Artifacts.txt', 'Understanding the Adoption of Quantified Self-tracking Wearable Devices in the Organization Environment: An Empirical Case Study.txt', 'Using Context to Reveal Factors That Affect Physical Activity.txt', 'VRFit: An Interactive Dashboard for Visualising of Virtual Reality Exercise and Daily Step Data.txt', 'What Health Topics Older Adults Want to Track: A Participatory Design Study.txt', 'When Fitness Meets Social Networks: Investigating Fitness Tracking and Social Practices on WeRun.txt', "When Fitness Trackers Don'T 'Fit': End-user Difficulties in the Assessment of Personal Tracking Device Accuracy.txt", 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating.txt'], 'var_call_DBGBDvtIrHUBkHmOkyp12Ykx': 'file_storage/call_DBGBDvtIrHUBkHmOkyp12Ykx.json', 'var_call_0kcS8fW88ZUz3uSYKQqQGkxg': [], 'var_call_Bn0SjlGDfCrnA96M9GUeEp6Y': 'file_storage/call_Bn0SjlGDfCrnA96M9GUeEp6Y.json'}

exec(code, env_args)
