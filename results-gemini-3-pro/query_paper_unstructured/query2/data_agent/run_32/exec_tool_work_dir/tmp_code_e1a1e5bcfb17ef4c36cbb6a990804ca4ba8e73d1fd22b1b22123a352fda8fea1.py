code = """import json
import re

# Load Mongo docs with text
mongo_file = locals()['var_function-call-5957764959840731621']
with open(mongo_file, 'r') as f:
    mongo_docs = json.load(f)

# Load SQLite citations
sqlite_file = locals()['var_function-call-13725744379955539795']
with open(sqlite_file, 'r') as f:
    sqlite_citations = json.load(f)

# Map title -> citation_count
citations_map = {c['title']: c['citation_count'] for c in sqlite_citations}

acm_citation_counts = []
acm_titles = []

for doc in mongo_docs:
    filename = doc['filename']
    title = filename.rsplit('.', 1)[0]
    text = doc.get('text', '')
    
    # Check if published by ACM
    # Heuristic: Look for ACM in the first 3000 chars (header/footer of first page)
    # Common strings: "Copyright ... ACM", "Association for Computing Machinery", "permissions@acm.org"
    # Or just "ACM" in the conference header
    
    header_text = text[:3000]
    if "ACM" in header_text or "Association for Computing Machinery" in header_text:
        if title in citations_map:
            acm_citation_counts.append(citations_map[title])
            acm_titles.append(title)

# Calculate average
if len(acm_citation_counts) > 0:
    avg_citations = sum(acm_citation_counts) / len(acm_citation_counts)
else:
    avg_citations = 0

print("ACM Papers found:", len(acm_titles))
print("Average citations:", avg_citations)
print("__RESULT__:")
print(avg_citations)"""

env_args = {'var_function-call-13725744379955539795': 'file_storage/function-call-13725744379955539795.json', 'var_function-call-16281852908939748059': 158, 'var_function-call-7061098653727589076': 'file_storage/function-call-7061098653727589076.json', 'var_function-call-7343253709634976495': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-8333179605566181681': ['ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'A Lived Informatics Model of Personal Informatics.txt'], 'var_function-call-16257406837857240081': 'file_storage/function-call-16257406837857240081.json', 'var_function-call-11046189042643845610': ['How to Drive a London Bus: Measuring Performance in a Mobile and Remote Workplace.txt', 'Intelligent Computing in Personal Informatics: Key Design Considerations.txt', 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats.txt', 'ClimbSense: Automatic Climbing Route Recognition Using Wrist-worn Inertia Measurement Units.txt', 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture.txt', 'Why We Use and Abandon Smart Devices.txt', 'Reviewing Reflection: On the Use of Reflection in Interactive System Design.txt', 'Making Sense of Sleep Sensors: How Sleep Sensing Technologies Support and Undermine Sleep Health.txt', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media.txt', 'Technologies for Everyday Life Reflection: Illustrating a Design Space.txt', 'Blood Pressure Beyond the Clinic: Rethinking a Health Metric for Everyone.txt', 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing.txt', 'Barriers to Engagement with a Personal Informatics Productivity Tool.txt', 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt', 'Predicting Interruptibility for Manual Data Collection: A Cluster-based User Model.txt', 'Trajectories of Engagement and Disengagement with a Story-Based Smoking Cessation App.txt', 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers.txt', 'Live Interest Meter: Learning from Quantified Feedback in Mass Lectures.txt', 'SleepTight: Low-burden, Self-monitoring Technology for Capturing and Reflecting on Sleep Behaviors.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'Sensor Requirements for Activity Recognition on Smart Watches.txt', 'Quantified Self Meets Social Media: Sharing of Weight Updates on Twitter.txt', 'A Lived Informatics Model of Personal Informatics.txt', "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps.txt", 'TastyBeats: Designing Palatable Representations of Physical Activity.txt', 'Goal-oriented Visualizations of Activity Tracking: A Case Study with Engineering Students.txt', 'Sundroid: Solar Radiation Awareness with Smartphones.txt', 'Charting Design Preferences on Wellness Wearables.txt', 'Designing a Wellness Self-management Tool for Older Adults: Results from a Field Trial of YourWellness.txt', 'Lullaby: A Capture & Access System for Understanding the Sleep Environment.txt', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App.txt', 'Contextual Influences on the Use and Non-Use of Digital Technology While Exercising at the Gym.txt', 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection.txt', 'Self-tracking Cultures: Towards a Sociology of Personal Informatics.txt', "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure.txt", 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness.txt', 'Real-life Experiences with an Adaptive Light Bracelet.txt', "We'Ve Bin Watching You: Designing for Reflection and Social Persuasion to Promote Sustainable Lifestyles.txt", 'Pass the Ball: Enforced Turn-Taking in Activity Tracking.txt', 'Social (Media) Jet Lag: How Usage of Social Technology Can Modulate and Reflect Circadian Rhythms.txt', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt", 'From Nobody Cares to Way to Go!: A Design Framework for Social Sharing in Personal Informatics.txt', 'TimeAware: Leveraging Framing Effects to Enhance Personal Productivity.txt', 'QuittyLink: Using Smartphones for Personal Counseling to Help People Quit Smoking.txt', 'No Longer Wearing: Investigating the Abandonment of Personal Health-tracking Technologies on Craigslist.txt', 'Leveraging Intermediated Interactions to Support Utilization of Persuasive Personal Health Informatics.txt', 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis.txt', 'Persuasive Technology in the Real World: A Study of Long-term Use of Activity Sensing Devices for Fitness.txt', 'ConCap: Designing to Empower Individual Reflection on Chronic Conditions Using Mobile Apps.txt', 'Personal Tracking of Screen Time on Digital Devices.txt', 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating.txt', 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace.txt', 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations.txt', 'FutureSelf: What Happens When We Forecast Self-Trackers? Future Health Statuses?.txt'], 'var_function-call-5957764959840731621': 'file_storage/function-call-5957764959840731621.json'}

exec(code, env_args)
