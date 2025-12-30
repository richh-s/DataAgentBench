code = """import json

# Load MongoDB docs (with text)
with open(locals()['var_function-call-3603238818244495525'], 'r') as f:
    mongo_docs = json.load(f)

# Load SQLite citations
with open(locals()['var_function-call-3465492661884944588'], 'r') as f:
    citations = json.load(f)

# Create lookup for citations
# key: title, value: citation_count (converted to int)
citation_map = {}
for r in citations:
    try:
        citation_map[r['title']] = int(r['citation_count'])
    except ValueError:
        pass # Skip invalid

acm_citations = []
debug_info = []

for doc in mongo_docs:
    filename = doc.get('filename', '')
    if not filename.endswith('.txt'):
        continue
    title = filename[:-4]
    
    if title in citation_map:
        text = doc.get('text', '')
        # Check for ACM source
        header_text = text[:5000]
        # Check for ACM
        # Common patterns: "Copyright ... ACM", "Permission ... ACM", "ACM Classification"
        is_acm = "ACM" in header_text
        
        # Refine: if only "IEEE" is present, it's not ACM.
        if "IEEE" in header_text and "ACM" not in header_text:
            is_acm = False
        
        # If both are present, usually the copyright holder determines it.
        # But "ACM" is a strong indicator if in header.
            
        if is_acm:
            count = citation_map[title]
            acm_citations.append(count)
            debug_info.append({"title": title, "count": count})

# Calculate average
if len(acm_citations) > 0:
    avg = sum(acm_citations) / len(acm_citations)
else:
    avg = 0

print(f"Found {len(acm_citations)} ACM papers cited in 2018.")
print(f"Average citation count: {avg}")

print("__RESULT__:")
print(json.dumps({"average": avg, "count": len(acm_citations), "sample": debug_info[:5]}))"""

env_args = {'var_function-call-3465492661884944588': 'file_storage/function-call-3465492661884944588.json', 'var_function-call-5093555136357275627': 'file_storage/function-call-5093555136357275627.json', 'var_function-call-9313904331850907827': {'count': 158, 'filenames_preview': ['Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing.txt', 'Sundroid: Solar Radiation Awareness with Smartphones.txt', 'Why We Use and Abandon Smart Devices.txt', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App.txt', 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set.txt']}, 'var_function-call-13887185202303649787': 'file_storage/function-call-13887185202303649787.json', 'var_function-call-5679702400551775489': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-12282390523872244281': 'Debug done', 'var_function-call-8492502438044727987': {'mongo_type': "<class 'list'>", 'mongo_len': 5, 'mongo_sample': {'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, 'sqlite_type': "<class 'str'>"}, 'var_function-call-11408419078720510866': 'file_storage/function-call-11408419078720510866.json', 'var_function-call-13814881666308117599': [['Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing.txt', 'Sundroid: Solar Radiation Awareness with Smartphones.txt', 'Why We Use and Abandon Smart Devices.txt', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App.txt', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt", 'Reviewing Reflection: On the Use of Reflection in Interactive System Design.txt', 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers.txt', 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection.txt', 'Barriers to Engagement with a Personal Informatics Productivity Tool.txt', 'How to Drive a London Bus: Measuring Performance in a Mobile and Remote Workplace.txt', 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations.txt', 'A Lived Informatics Model of Personal Informatics.txt', 'Charting Design Preferences on Wellness Wearables.txt', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media.txt', 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis.txt', 'Technologies for Everyday Life Reflection: Illustrating a Design Space.txt', 'Personal Tracking of Screen Time on Digital Devices.txt', 'Sensor Requirements for Activity Recognition on Smart Watches.txt', 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture.txt', 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt', 'Live Interest Meter: Learning from Quantified Feedback in Mass Lectures.txt', 'Quantified Self Meets Social Media: Sharing of Weight Updates on Twitter.txt', 'Pass the Ball: Enforced Turn-Taking in Activity Tracking.txt', 'Blood Pressure Beyond the Clinic: Rethinking a Health Metric for Everyone.txt', 'No Longer Wearing: Investigating the Abandonment of Personal Health-tracking Technologies on Craigslist.txt', 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace.txt', "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps.txt", 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'FutureSelf: What Happens When We Forecast Self-Trackers? Future Health Statuses?.txt', 'Predicting Interruptibility for Manual Data Collection: A Cluster-based User Model.txt', 'Leveraging Intermediated Interactions to Support Utilization of Persuasive Personal Health Informatics.txt', 'Social (Media) Jet Lag: How Usage of Social Technology Can Modulate and Reflect Circadian Rhythms.txt', 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats.txt', 'Designing a Wellness Self-management Tool for Older Adults: Results from a Field Trial of YourWellness.txt', 'TastyBeats: Designing Palatable Representations of Physical Activity.txt', 'Self-tracking Cultures: Towards a Sociology of Personal Informatics.txt', 'Trajectories of Engagement and Disengagement with a Story-Based Smoking Cessation App.txt', 'Persuasive Technology in the Real World: A Study of Long-term Use of Activity Sensing Devices for Fitness.txt', 'Real-life Experiences with an Adaptive Light Bracelet.txt', 'From Nobody Cares to Way to Go!: A Design Framework for Social Sharing in Personal Informatics.txt', 'Lullaby: A Capture & Access System for Understanding the Sleep Environment.txt', 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating.txt', 'Making Sense of Sleep Sensors: How Sleep Sensing Technologies Support and Undermine Sleep Health.txt', 'Goal-oriented Visualizations of Activity Tracking: A Case Study with Engineering Students.txt', 'QuittyLink: Using Smartphones for Personal Counseling to Help People Quit Smoking.txt', 'Contextual Influences on the Use and Non-Use of Digital Technology While Exercising at the Gym.txt', 'Intelligent Computing in Personal Informatics: Key Design Considerations.txt', "We'Ve Bin Watching You: Designing for Reflection and Social Persuasion to Promote Sustainable Lifestyles.txt", 'TimeAware: Leveraging Framing Effects to Enhance Personal Productivity.txt', "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure.txt"], ['ClimbSense: Automatic Climbing Route Recognition Using Wrist-worn Inertia Measurement Units.txt', 'SleepTight: Low-burden, Self-monitoring Technology for Capturing and Reflecting on Sleep Behaviors.txt', 'ConCap: Designing to Empower Individual Reflection on Chronic Conditions Using Mobile Apps.txt', 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness.txt', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt']], 'var_function-call-3603238818244495525': 'file_storage/function-call-3603238818244495525.json'}

exec(code, env_args)
