code = """import json

# Load citations
with open(locals()['var_function-call-1625930341030172972'], 'r') as f:
    citations = json.load(f)

# Load paper texts
with open(locals()['var_function-call-14860406429223890990'], 'r') as f:
    papers = json.load(f)

# Create a map of title -> citation_count
citation_map = {c['title']: int(c['citation_count']) for c in citations}

acm_citation_sum = 0
acm_paper_count = 0

matched_papers = []

for p in papers:
    text = p.get('text', "")
    filename = p.get('filename', "")
    title = filename.replace(".txt", "")
    
    # Check if ACM is in text
    # Heuristic: look for "ACM"
    if "ACM" in text:
        if title in citation_map:
            count = citation_map[title]
            acm_citation_sum += count
            acm_paper_count += 1
            matched_papers.append(title)

average = acm_citation_sum / acm_paper_count if acm_paper_count > 0 else 0

print(f"Total ACM papers found: {acm_paper_count}")
print(f"Total citations: {acm_citation_sum}")
print(f"Average citation count: {average}")

print("__RESULT__:")
print(json.dumps(average))"""

env_args = {'var_function-call-1625930341030172972': 'file_storage/function-call-1625930341030172972.json', 'var_function-call-13977181496462038220': 'file_storage/function-call-13977181496462038220.json', 'var_function-call-12384276026889794839': 'file_storage/function-call-12384276026889794839.json', 'var_function-call-15504972561961046607': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-4599745652298373250': {'count': 5, 'first_doc': {'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}}, 'var_function-call-5147705068000109282': 'file_storage/function-call-5147705068000109282.json', 'var_function-call-12081599907189404359': {'collection': 'paper_docs', 'filter': {'filename': {'$in': ['Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing.txt', 'Sundroid: Solar Radiation Awareness with Smartphones.txt', 'Why We Use and Abandon Smart Devices.txt', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App.txt', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt", 'Reviewing Reflection: On the Use of Reflection in Interactive System Design.txt', 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers.txt', 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection.txt', 'Barriers to Engagement with a Personal Informatics Productivity Tool.txt', 'How to Drive a London Bus: Measuring Performance in a Mobile and Remote Workplace.txt', 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations.txt', 'A Lived Informatics Model of Personal Informatics.txt', 'Charting Design Preferences on Wellness Wearables.txt', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media.txt', 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis.txt', 'Technologies for Everyday Life Reflection: Illustrating a Design Space.txt', 'Personal Tracking of Screen Time on Digital Devices.txt', 'Sensor Requirements for Activity Recognition on Smart Watches.txt', 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture.txt', 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt', 'Live Interest Meter: Learning from Quantified Feedback in Mass Lectures.txt', 'Quantified Self Meets Social Media: Sharing of Weight Updates on Twitter.txt', 'Pass the Ball: Enforced Turn-Taking in Activity Tracking.txt', 'Blood Pressure Beyond the Clinic: Rethinking a Health Metric for Everyone.txt', 'No Longer Wearing: Investigating the Abandonment of Personal Health-tracking Technologies on Craigslist.txt', 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace.txt', "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps.txt", 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'FutureSelf: What Happens When We Forecast Self-Trackers? Future Health Statuses?.txt', 'Predicting Interruptibility for Manual Data Collection: A Cluster-based User Model.txt', 'Leveraging Intermediated Interactions to Support Utilization of Persuasive Personal Health Informatics.txt', 'Social (Media) Jet Lag: How Usage of Social Technology Can Modulate and Reflect Circadian Rhythms.txt', 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats.txt', 'Designing a Wellness Self-management Tool for Older Adults: Results from a Field Trial of YourWellness.txt', 'TastyBeats: Designing Palatable Representations of Physical Activity.txt', 'Self-tracking Cultures: Towards a Sociology of Personal Informatics.txt', 'Trajectories of Engagement and Disengagement with a Story-Based Smoking Cessation App.txt', 'Persuasive Technology in the Real World: A Study of Long-term Use of Activity Sensing Devices for Fitness.txt', 'Real-life Experiences with an Adaptive Light Bracelet.txt', 'From Nobody Cares to Way to Go!: A Design Framework for Social Sharing in Personal Informatics.txt', 'Lullaby: A Capture & Access System for Understanding the Sleep Environment.txt', 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating.txt', 'Making Sense of Sleep Sensors: How Sleep Sensing Technologies Support and Undermine Sleep Health.txt', 'Goal-oriented Visualizations of Activity Tracking: A Case Study with Engineering Students.txt', 'QuittyLink: Using Smartphones for Personal Counseling to Help People Quit Smoking.txt', 'Contextual Influences on the Use and Non-Use of Digital Technology While Exercising at the Gym.txt', 'Intelligent Computing in Personal Informatics: Key Design Considerations.txt', "We'Ve Bin Watching You: Designing for Reflection and Social Persuasion to Promote Sustainable Lifestyles.txt", 'TimeAware: Leveraging Framing Effects to Enhance Personal Productivity.txt', "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure.txt", 'ClimbSense: Automatic Climbing Route Recognition Using Wrist-worn Inertia Measurement Units.txt', 'SleepTight: Low-burden, Self-monitoring Technology for Capturing and Reflecting on Sleep Behaviors.txt', 'ConCap: Designing to Empower Individual Reflection on Chronic Conditions Using Mobile Apps.txt', 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness.txt', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt']}}, 'projection': {'filename': 1, 'text': 1}}, 'var_function-call-14860406429223890990': 'file_storage/function-call-14860406429223890990.json'}

exec(code, env_args)
