code = """import json
import re

# Load citations
with open(locals()['var_function-call-16373116911178695907'], 'r') as f:
    citations = json.load(f)
citation_map = {c['title'] + ".txt": int(c['citation_count']) for c in citations}

# Load Chunk 1 papers
with open(locals()['var_function-call-18157864605633541603'], 'r') as f:
    papers_chunk1 = json.load(f)

# Process Chunk 1
sum_chunk1 = 0
for paper in papers_chunk1:
    text = paper.get('text', '')
    # Check first 2000 chars for venue
    header = text[:2000]
    # Check for CHI
    if re.search(r'\bCHI\b', header) or "Conference on Human Factors in Computing Systems" in header:
        filename = paper.get('filename')
        if filename in citation_map:
            sum_chunk1 += citation_map[filename]

# Prepare Chunk 2 filenames
filenames = [c['title'] + ".txt" for c in citations]
chunk2 = filenames[50:100]

print("__RESULT__:")
print(json.dumps({"chunk2_filenames": chunk2, "chunk1_sum": sum_chunk1}))"""

env_args = {'var_function-call-16373116911178694920': ['Citations', 'sqlite_sequence'], 'var_function-call-16373116911178695907': 'file_storage/function-call-16373116911178695907.json', 'var_function-call-16373116911178696894': 'file_storage/function-call-16373116911178696894.json', 'var_function-call-13177130613489876308': 188, 'var_function-call-10911967024250333804': 'file_storage/function-call-10911967024250333804.json', 'var_function-call-9748881427492013847': 'file_storage/function-call-9748881427492013847.json', 'var_function-call-1936871565962322545': 'file_storage/function-call-1936871565962322545.json', 'var_function-call-18151132234637647575': {'citations_count': 188, 'paper_docs_count': 5}, 'var_function-call-2516633047553626079': 'file_storage/function-call-2516633047553626079.json', 'var_function-call-16179770808455181191': 'file_storage/function-call-16179770808455181191.json', 'var_function-call-5191192080476357211': ['Sundroid: Solar Radiation Awareness with Smartphones.txt', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity.txt', 'Why We Use and Abandon Smart Devices.txt', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App.txt', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application.txt", 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt", "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt", 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers.txt', 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection.txt', 'Barriers to Engagement with a Personal Informatics Productivity Tool.txt', 'Modeling Interdependent and Periodic Real-World Action Sequences.txt', 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video.txt', 'How to Drive a London Bus: Measuring Performance in a Mobile and Remote Workplace.txt', 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations.txt', 'A Lived Informatics Model of Personal Informatics.txt', 'Charting Design Preferences on Wellness Wearables.txt', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media.txt', 'Heed: Exploring the Design of Situated Self-Reporting Devices.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis.txt', 'Technologies for Everyday Life Reflection: Illustrating a Design Space.txt', 'Personal Tracking of Screen Time on Digital Devices.txt', 'Sensor Requirements for Activity Recognition on Smart Watches.txt', 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture.txt', 'Defining Adherence: Making Sense of Physical Activity Tracker Data.txt', 'Live Interest Meter: Learning from Quantified Feedback in Mass Lectures.txt', 'Entangled with Numbers: Quantified Self and Others in a Team-Based Online Game.txt', 'Communicating Uncertainty in Fertility Prognosis.txt', 'Understanding Personal Productivity: How Knowledge Workers Define, Evaluate, and Reflect on Their Productivity.txt', 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings.txt', 'Visual ODLs: Co-Designing Patient-Generated Observations of Daily Living to Support Data-Driven Conversations in Pediatric Care.txt', 'Pass the Ball: Enforced Turn-Taking in Activity Tracking.txt', 'DataSelfie: Empowering People to Design Personalized Visuals to Represent Their Data.txt', 'Scaffolding for an OLM for Long-Term Physical Activity Goals.txt', 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace.txt', 'Turn to the Self in Human-Computer Interaction: Care of the Self in Negotiating the Human-Technology Relationship.txt', "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps.txt", 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'Leveraging Intermediated Interactions to Support Utilization of Persuasive Personal Health Informatics.txt', 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance.txt', 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers.txt', 'Understanding Animals: A Critical Challenge in ACI.txt', 'Social (Media) Jet Lag: How Usage of Social Technology Can Modulate and Reflect Circadian Rhythms.txt', 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats.txt', 'Designing a Wellness Self-management Tool for Older Adults: Results from a Field Trial of YourWellness.txt', 'TastyBeats: Designing Palatable Representations of Physical Activity.txt', 'Toward Health Information Technology That Supports Overweight/Obese Women in Addressing Emotion- and Stress-Related Eating.txt', 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices.txt', 'Exploring the Value of Parent Tracked Baby Data in Interactions with Healthcare Professionals: A Data-Enabled Design Exploration.txt'], 'var_function-call-18157864605633541603': 'file_storage/function-call-18157864605633541603.json'}

exec(code, env_args)
