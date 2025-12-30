code = """import json

# Load citations
file_path = locals()['var_function-call-4107798492102735370']
with open(file_path, 'r') as f:
    citations_data = json.load(f)

# Map filename -> citation_count
filename_counts = {}
filenames = []
for item in citations_data:
    fname = item['title'] + ".txt"
    filename_counts[fname] = item['citation_count']
    filenames.append(fname)

# Save map and list
with open('citation_counts_map.json', 'w') as f:
    json.dump(filename_counts, f)
with open('all_filenames.json', 'w') as f:
    json.dump(filenames, f)

# Initialize total
with open('total_citations.json', 'w') as f:
    json.dump({"total": 0}, f)

# Prepare Batch 1 (0 to 100)
batch1 = filenames[:100]
query1 = json.dumps({"collection": "paper_docs", "filter": {"filename": {"$in": batch1}}})

print("__RESULT__:")
print(query1)"""

env_args = {'var_function-call-4107798492102735370': 'file_storage/function-call-4107798492102735370.json', 'var_function-call-13958868829656037489': {'sample_filename': 'Sundroid: Solar Radiation Awareness with Smartphones.txt', 'titles_count': 188}, 'var_function-call-16540664085193316271': 'file_storage/function-call-16540664085193316271.json', 'var_function-call-15194230552685176329': 'file_storage/function-call-15194230552685176329.json', 'var_function-call-7159636388618458980': {'collection': 'paper_docs', 'filter': {'filename': {'$in': ['Sundroid: Solar Radiation Awareness with Smartphones.txt', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity.txt', 'Why We Use and Abandon Smart Devices.txt', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App.txt', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application.txt", 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt", "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt", 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers.txt', 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection.txt', 'Barriers to Engagement with a Personal Informatics Productivity Tool.txt', 'Modeling Interdependent and Periodic Real-World Action Sequences.txt', 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video.txt', 'How to Drive a London Bus: Measuring Performance in a Mobile and Remote Workplace.txt', 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations.txt', 'A Lived Informatics Model of Personal Informatics.txt', 'Charting Design Preferences on Wellness Wearables.txt', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media.txt', 'Heed: Exploring the Design of Situated Self-Reporting Devices.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis.txt', 'Technologies for Everyday Life Reflection: Illustrating a Design Space.txt', 'Personal Tracking of Screen Time on Digital Devices.txt', 'Sensor Requirements for Activity Recognition on Smart Watches.txt', 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture.txt', 'Defining Adherence: Making Sense of Physical Activity Tracker Data.txt', 'Live Interest Meter: Learning from Quantified Feedback in Mass Lectures.txt', 'Entangled with Numbers: Quantified Self and Others in a Team-Based Online Game.txt', 'Communicating Uncertainty in Fertility Prognosis.txt', 'Understanding Personal Productivity: How Knowledge Workers Define, Evaluate, and Reflect on Their Productivity.txt', 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings.txt', 'Visual ODLs: Co-Designing Patient-Generated Observations of Daily Living to Support Data-Driven Conversations in Pediatric Care.txt', 'Pass the Ball: Enforced Turn-Taking in Activity Tracking.txt', 'DataSelfie: Empowering People to Design Personalized Visuals to Represent Their Data.txt', 'Scaffolding for an OLM for Long-Term Physical Activity Goals.txt', 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace.txt', 'Turn to the Self in Human-Computer Interaction: Care of the Self in Negotiating the Human-Technology Relationship.txt', "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps.txt", 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'Leveraging Intermediated Interactions to Support Utilization of Persuasive Personal Health Informatics.txt', 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance.txt', 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers.txt', 'Understanding Animals: A Critical Challenge in ACI.txt', 'Social (Media) Jet Lag: How Usage of Social Technology Can Modulate and Reflect Circadian Rhythms.txt', 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats.txt', 'Designing a Wellness Self-management Tool for Older Adults: Results from a Field Trial of YourWellness.txt', 'TastyBeats: Designing Palatable Representations of Physical Activity.txt', 'Toward Health Information Technology That Supports Overweight/Obese Women in Addressing Emotion- and Stress-Related Eating.txt', 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices.txt', 'Exploring the Value of Parent Tracked Baby Data in Interactions with Healthcare Professionals: A Data-Enabled Design Exploration.txt']}}}}

exec(code, env_args)
