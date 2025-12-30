code = """import json
import re

# Load citations
citations_path = locals()['var_function-call-16918491452103176986']
if isinstance(citations_path, str):
    with open(citations_path, 'r') as f:
        citations = json.load(f)
else:
    citations = citations_path

# Create title -> citation map (convert count to int)
title_to_citations = {}
for c in citations:
    try:
        title_to_citations[c['title']] = int(c['citation_count'])
    except ValueError:
        title_to_citations[c['title']] = 0

# Load papers from batches
batch_files = [
    locals()['var_function-call-16318215653155260663'],
    locals()['var_function-call-10245232174905301322'],
    locals()['var_function-call-9637255288090962634']
]

papers = []
for bf in batch_files:
    if isinstance(bf, str):
        with open(bf, 'r') as f:
            papers.extend(json.load(f))
    else:
        papers.extend(bf)

# Filter for ACM papers
acm_papers = []
acm_citations = []

for p in papers:
    text = p.get('text', '')
    header = text[:5000] # Check first 5000 chars
    
    # Check for ACM indicators
    is_acm = False
    if "Copyright" in header and "ACM" in header:
        is_acm = True
    elif "Permission to make" in header and "ACM" in header:
        is_acm = True
    elif "ACM Classification Keywords" in header:
        is_acm = True
    elif "Association for Computing Machinery" in header:
        is_acm = True
    # Relaxed check: just ACM in header? No, risky.
    
    if is_acm:
        title = p['filename'][:-4]
        if title in title_to_citations:
            count = title_to_citations[title]
            acm_papers.append(title)
            acm_citations.append(count)

# Calculate average
if acm_citations:
    avg_citations = sum(acm_citations) / len(acm_citations)
else:
    avg_citations = 0

print(f"Found {len(acm_papers)} ACM papers out of {len(papers)} processed.")
print(f"Average citation count: {avg_citations}")
print("__RESULT__:")
print(json.dumps(avg_citations))"""

env_args = {'var_function-call-16918491452103176986': 'file_storage/function-call-16918491452103176986.json', 'var_function-call-2065725143731253530': 'file_storage/function-call-2065725143731253530.json', 'var_function-call-338667310084266534': {'count': 158, 'filenames_sample': ['Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing.txt', 'Sundroid: Solar Radiation Awareness with Smartphones.txt', 'Why We Use and Abandon Smart Devices.txt', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App.txt', 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set.txt']}, 'var_function-call-12839390599410482913': 'file_storage/function-call-12839390599410482913.json', 'var_function-call-12990868199474423311': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-742193960865613679': ['694f5530284b10b11dc0a869', '694f5530284b10b11dc0a86d'], 'var_function-call-10502241309305470194': 5, 'var_function-call-13806387405528960265': 'file_storage/function-call-13806387405528960265.json', 'var_function-call-10191910439105865949': 'file_storage/function-call-10191910439105865949.json', 'var_function-call-4264967823021131778': ['694f5530284b10b11dc0a869', '694f5530284b10b11dc0a86d', '694f5530284b10b11dc0a86e', '694f5530284b10b11dc0a86f', '694f5530284b10b11dc0a870', '694f5530284b10b11dc0a872', '694f5530284b10b11dc0a873', '694f5530284b10b11dc0a874', '694f5530284b10b11dc0a875', '694f5530284b10b11dc0a878', '694f5530284b10b11dc0a879', '694f5530284b10b11dc0a87a', '694f5530284b10b11dc0a87b', '694f5530284b10b11dc0a87e', '694f5530284b10b11dc0a882', '694f5530284b10b11dc0a884', '694f5530284b10b11dc0a885', '694f5530284b10b11dc0a888', '694f5530284b10b11dc0a889', '694f5530284b10b11dc0a88a', '694f5530284b10b11dc0a88e', '694f5530284b10b11dc0a890', '694f5530284b10b11dc0a891', '694f5530284b10b11dc0a892', '694f5530284b10b11dc0a893', '694f5530284b10b11dc0a894', '694f5530284b10b11dc0a895', '694f5530284b10b11dc0a897', '694f5530284b10b11dc0a89a', '694f5530284b10b11dc0a89b', '694f5530284b10b11dc0a89d', '694f5530284b10b11dc0a89e', '694f5530284b10b11dc0a8a0', '694f5530284b10b11dc0a8a2', '694f5530284b10b11dc0a8a3', '694f5530284b10b11dc0a8a5', '694f5530284b10b11dc0a8a6', '694f5530284b10b11dc0a8a7', '694f5530284b10b11dc0a8a8', '694f5530284b10b11dc0a8a9', '694f5530284b10b11dc0a8aa', '694f5530284b10b11dc0a8ab', '694f5530284b10b11dc0a8ad', '694f5530284b10b11dc0a8ae', '694f5530284b10b11dc0a8b0', '694f5530284b10b11dc0a8b1', '694f5530284b10b11dc0a8b4', '694f5530284b10b11dc0a8b5', '694f5530284b10b11dc0a8b8', '694f5530284b10b11dc0a8b9', '694f5530284b10b11dc0a8be', '694f5530284b10b11dc0a8c0', '694f5530284b10b11dc0a8c7', '694f5530284b10b11dc0a8ca', '694f5530284b10b11dc0a8cb'], 'var_function-call-816863913214786722': {'collection': 'paper_docs', 'filter': {'_id': {'$in': ['694f5530284b10b11dc0a869', '694f5530284b10b11dc0a86d', '694f5530284b10b11dc0a86e', '694f5530284b10b11dc0a86f', '694f5530284b10b11dc0a870', '694f5530284b10b11dc0a872', '694f5530284b10b11dc0a873', '694f5530284b10b11dc0a874', '694f5530284b10b11dc0a875', '694f5530284b10b11dc0a878', '694f5530284b10b11dc0a879', '694f5530284b10b11dc0a87a', '694f5530284b10b11dc0a87b', '694f5530284b10b11dc0a87e', '694f5530284b10b11dc0a882', '694f5530284b10b11dc0a884', '694f5530284b10b11dc0a885', '694f5530284b10b11dc0a888', '694f5530284b10b11dc0a889', '694f5530284b10b11dc0a88a', '694f5530284b10b11dc0a88e', '694f5530284b10b11dc0a890', '694f5530284b10b11dc0a891', '694f5530284b10b11dc0a892', '694f5530284b10b11dc0a893', '694f5530284b10b11dc0a894', '694f5530284b10b11dc0a895', '694f5530284b10b11dc0a897', '694f5530284b10b11dc0a89a', '694f5530284b10b11dc0a89b', '694f5530284b10b11dc0a89d', '694f5530284b10b11dc0a89e', '694f5530284b10b11dc0a8a0', '694f5530284b10b11dc0a8a2', '694f5530284b10b11dc0a8a3', '694f5530284b10b11dc0a8a5', '694f5530284b10b11dc0a8a6', '694f5530284b10b11dc0a8a7', '694f5530284b10b11dc0a8a8', '694f5530284b10b11dc0a8a9', '694f5530284b10b11dc0a8aa', '694f5530284b10b11dc0a8ab', '694f5530284b10b11dc0a8ad', '694f5530284b10b11dc0a8ae', '694f5530284b10b11dc0a8b0', '694f5530284b10b11dc0a8b1', '694f5530284b10b11dc0a8b4', '694f5530284b10b11dc0a8b5', '694f5530284b10b11dc0a8b8', '694f5530284b10b11dc0a8b9', '694f5530284b10b11dc0a8be', '694f5530284b10b11dc0a8c0', '694f5530284b10b11dc0a8c7', '694f5530284b10b11dc0a8ca', '694f5530284b10b11dc0a8cb']}}}, 'var_function-call-14079047020875151105': [['694f5530284b10b11dc0a869', '694f5530284b10b11dc0a86d', '694f5530284b10b11dc0a86e', '694f5530284b10b11dc0a86f', '694f5530284b10b11dc0a870', '694f5530284b10b11dc0a872', '694f5530284b10b11dc0a873', '694f5530284b10b11dc0a874', '694f5530284b10b11dc0a875', '694f5530284b10b11dc0a878', '694f5530284b10b11dc0a879', '694f5530284b10b11dc0a87a', '694f5530284b10b11dc0a87b', '694f5530284b10b11dc0a87e', '694f5530284b10b11dc0a882', '694f5530284b10b11dc0a884', '694f5530284b10b11dc0a885', '694f5530284b10b11dc0a888', '694f5530284b10b11dc0a889', '694f5530284b10b11dc0a88a'], ['694f5530284b10b11dc0a88e', '694f5530284b10b11dc0a890', '694f5530284b10b11dc0a891', '694f5530284b10b11dc0a892', '694f5530284b10b11dc0a893', '694f5530284b10b11dc0a894', '694f5530284b10b11dc0a895', '694f5530284b10b11dc0a897', '694f5530284b10b11dc0a89a', '694f5530284b10b11dc0a89b', '694f5530284b10b11dc0a89d', '694f5530284b10b11dc0a89e', '694f5530284b10b11dc0a8a0', '694f5530284b10b11dc0a8a2', '694f5530284b10b11dc0a8a3', '694f5530284b10b11dc0a8a5', '694f5530284b10b11dc0a8a6', '694f5530284b10b11dc0a8a7', '694f5530284b10b11dc0a8a8', '694f5530284b10b11dc0a8a9'], ['694f5530284b10b11dc0a8aa', '694f5530284b10b11dc0a8ab', '694f5530284b10b11dc0a8ad', '694f5530284b10b11dc0a8ae', '694f5530284b10b11dc0a8b0', '694f5530284b10b11dc0a8b1', '694f5530284b10b11dc0a8b4', '694f5530284b10b11dc0a8b5', '694f5530284b10b11dc0a8b8', '694f5530284b10b11dc0a8b9', '694f5530284b10b11dc0a8be', '694f5530284b10b11dc0a8c0', '694f5530284b10b11dc0a8c7', '694f5530284b10b11dc0a8ca', '694f5530284b10b11dc0a8cb']], 'var_function-call-5285239423828302058': [], 'var_function-call-7905619288319975721': [['A Lived Informatics Model of Personal Informatics.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt', 'Barriers to Engagement with a Personal Informatics Productivity Tool.txt', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt', 'Blood Pressure Beyond the Clinic: Rethinking a Health Metric for Everyone.txt', 'Charting Design Preferences on Wellness Wearables.txt', 'ClimbSense: Automatic Climbing Route Recognition Using Wrist-worn Inertia Measurement Units.txt', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt", 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media.txt', 'ConCap: Designing to Empower Individual Reflection on Chronic Conditions Using Mobile Apps.txt', 'Contextual Influences on the Use and Non-Use of Digital Technology While Exercising at the Gym.txt', 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness.txt', 'Designing a Wellness Self-management Tool for Older Adults: Results from a Field Trial of YourWellness.txt', 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats.txt', 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing.txt', 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers.txt', 'From Nobody Cares to Way to Go!: A Design Framework for Social Sharing in Personal Informatics.txt', 'FutureSelf: What Happens When We Forecast Self-Trackers? Future Health Statuses?.txt', 'Goal-oriented Visualizations of Activity Tracking: A Case Study with Engineering Students.txt'], ['How to Drive a London Bus: Measuring Performance in a Mobile and Remote Workplace.txt', 'Intelligent Computing in Personal Informatics: Key Design Considerations.txt', "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps.txt", 'Leveraging Intermediated Interactions to Support Utilization of Persuasive Personal Health Informatics.txt', 'Live Interest Meter: Learning from Quantified Feedback in Mass Lectures.txt', 'Lullaby: A Capture & Access System for Understanding the Sleep Environment.txt', 'Making Sense of Sleep Sensors: How Sleep Sensing Technologies Support and Undermine Sleep Health.txt', "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure.txt", 'No Longer Wearing: Investigating the Abandonment of Personal Health-tracking Technologies on Craigslist.txt', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App.txt', 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations.txt', 'Pass the Ball: Enforced Turn-Taking in Activity Tracking.txt', 'Personal Tracking of Screen Time on Digital Devices.txt', 'Persuasive Technology in the Real World: A Study of Long-term Use of Activity Sensing Devices for Fitness.txt', 'Predicting Interruptibility for Manual Data Collection: A Cluster-based User Model.txt', 'Quantified Self Meets Social Media: Sharing of Weight Updates on Twitter.txt', 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis.txt', 'QuittyLink: Using Smartphones for Personal Counseling to Help People Quit Smoking.txt', 'Real-life Experiences with an Adaptive Light Bracelet.txt', 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection.txt'], ['Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture.txt', 'Reviewing Reflection: On the Use of Reflection in Interactive System Design.txt', 'Self-tracking Cultures: Towards a Sociology of Personal Informatics.txt', 'Sensor Requirements for Activity Recognition on Smart Watches.txt', 'SleepTight: Low-burden, Self-monitoring Technology for Capturing and Reflecting on Sleep Behaviors.txt', 'Social (Media) Jet Lag: How Usage of Social Technology Can Modulate and Reflect Circadian Rhythms.txt', 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace.txt', 'Sundroid: Solar Radiation Awareness with Smartphones.txt', 'TastyBeats: Designing Palatable Representations of Physical Activity.txt', 'Technologies for Everyday Life Reflection: Illustrating a Design Space.txt', 'TimeAware: Leveraging Framing Effects to Enhance Personal Productivity.txt', 'Trajectories of Engagement and Disengagement with a Story-Based Smoking Cessation App.txt', "We'Ve Bin Watching You: Designing for Reflection and Social Persuasion to Promote Sustainable Lifestyles.txt", 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating.txt', 'Why We Use and Abandon Smart Devices.txt']], 'var_function-call-16318215653155260663': 'file_storage/function-call-16318215653155260663.json', 'var_function-call-10245232174905301322': 'file_storage/function-call-10245232174905301322.json', 'var_function-call-9637255288090962634': 'file_storage/function-call-9637255288090962634.json'}

exec(code, env_args)
