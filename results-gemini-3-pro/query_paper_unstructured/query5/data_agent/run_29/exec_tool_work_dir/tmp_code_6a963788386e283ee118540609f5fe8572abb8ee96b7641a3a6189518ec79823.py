code = """import json
import re

# Load citations if not already loaded (safe check)
cit_file = locals().get('var_function-call-6787168720447240942')
if cit_file:
    with open(cit_file, 'r') as f:
        citations = json.load(f)
else:
    # If variables were lost (unlikely), handle error or assume loaded
    pass

# Create lookup
citation_map = {c['title'] + ".txt": int(c['citation_count']) for c in citations}

# Load Batch 1 results
batch1_file = locals()['var_function-call-7564138397359396590']
with open(batch1_file, 'r') as f:
    batch1_docs = json.load(f)

# Function to check if CHI
def is_chi(text):
    # Check first 500 chars for venue
    header = text[:500]
    if "Conference on Human Factors in Computing Systems" in header:
        return True
    # Check for CHI 'xx or CHI 20xx
    if re.search(r"CHI\s+'\d{2}", header) or re.search(r"CHI\s+20\d{2}", header):
        return True
    return False

chi_citations_batch1 = 0
chi_papers_batch1 = []

for doc in batch1_docs:
    if is_chi(doc['text']):
        count = citation_map.get(doc['filename'], 0)
        chi_citations_batch1 += count
        chi_papers_batch1.append(doc['filename'])

print(f"Batch 1 CHI papers: {len(chi_papers_batch1)}")
print(f"Batch 1 CHI citations: {chi_citations_batch1}")

# Prepare Batch 2 filenames
filenames = [c['title'] + ".txt" for c in citations]
batch2 = filenames[50:100]

print("__RESULT__:")
print(json.dumps({
    "batch1_sum": chi_citations_batch1,
    "batch2_filenames": batch2
}))"""

env_args = {'var_function-call-6787168720447240942': 'file_storage/function-call-6787168720447240942.json', 'var_function-call-8317175203464136568': 'file_storage/function-call-8317175203464136568.json', 'var_function-call-11529890176534547758': 'file_storage/function-call-11529890176534547758.json', 'var_function-call-63839196414706902': {'count': 188, 'sample': {'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65'}}, 'var_function-call-4721039501757598262': 'file_storage/function-call-4721039501757598262.json', 'var_function-call-4152211640730931800': [{'_id': '694f5530284b10b11dc0a869'}, {'_id': '694f5530284b10b11dc0a86a'}, {'_id': '694f5530284b10b11dc0a86b'}, {'_id': '694f5530284b10b11dc0a86c'}, {'_id': '694f5530284b10b11dc0a86d'}], 'var_function-call-8607789987885693285': 'file_storage/function-call-8607789987885693285.json', 'var_function-call-1079362033276818739': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-5587663968911552224': 'file_storage/function-call-5587663968911552224.json', 'var_function-call-15010692503854524086': 5, 'var_function-call-4614670717740065921': ['Sundroid: Solar Radiation Awareness with Smartphones.txt', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity.txt', 'Why We Use and Abandon Smart Devices.txt', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App.txt', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application.txt", 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt", "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt", 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers.txt', 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection.txt', 'Barriers to Engagement with a Personal Informatics Productivity Tool.txt', 'Modeling Interdependent and Periodic Real-World Action Sequences.txt', 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video.txt', 'How to Drive a London Bus: Measuring Performance in a Mobile and Remote Workplace.txt', 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations.txt', 'A Lived Informatics Model of Personal Informatics.txt', 'Charting Design Preferences on Wellness Wearables.txt', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media.txt', 'Heed: Exploring the Design of Situated Self-Reporting Devices.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis.txt', 'Technologies for Everyday Life Reflection: Illustrating a Design Space.txt', 'Personal Tracking of Screen Time on Digital Devices.txt', 'Sensor Requirements for Activity Recognition on Smart Watches.txt', 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture.txt', 'Defining Adherence: Making Sense of Physical Activity Tracker Data.txt', 'Live Interest Meter: Learning from Quantified Feedback in Mass Lectures.txt', 'Entangled with Numbers: Quantified Self and Others in a Team-Based Online Game.txt', 'Communicating Uncertainty in Fertility Prognosis.txt', 'Understanding Personal Productivity: How Knowledge Workers Define, Evaluate, and Reflect on Their Productivity.txt', 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings.txt', 'Visual ODLs: Co-Designing Patient-Generated Observations of Daily Living to Support Data-Driven Conversations in Pediatric Care.txt', 'Pass the Ball: Enforced Turn-Taking in Activity Tracking.txt', 'DataSelfie: Empowering People to Design Personalized Visuals to Represent Their Data.txt', 'Scaffolding for an OLM for Long-Term Physical Activity Goals.txt', 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace.txt', 'Turn to the Self in Human-Computer Interaction: Care of the Self in Negotiating the Human-Technology Relationship.txt', "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps.txt", 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'Leveraging Intermediated Interactions to Support Utilization of Persuasive Personal Health Informatics.txt', 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance.txt', 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers.txt', 'Understanding Animals: A Critical Challenge in ACI.txt', 'Social (Media) Jet Lag: How Usage of Social Technology Can Modulate and Reflect Circadian Rhythms.txt', 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats.txt', 'Designing a Wellness Self-management Tool for Older Adults: Results from a Field Trial of YourWellness.txt', 'TastyBeats: Designing Palatable Representations of Physical Activity.txt', 'Toward Health Information Technology That Supports Overweight/Obese Women in Addressing Emotion- and Stress-Related Eating.txt', 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices.txt', 'Exploring the Value of Parent Tracked Baby Data in Interactions with Healthcare Professionals: A Data-Enabled Design Exploration.txt'], 'var_function-call-7564138397359396590': 'file_storage/function-call-7564138397359396590.json'}

exec(code, env_args)
