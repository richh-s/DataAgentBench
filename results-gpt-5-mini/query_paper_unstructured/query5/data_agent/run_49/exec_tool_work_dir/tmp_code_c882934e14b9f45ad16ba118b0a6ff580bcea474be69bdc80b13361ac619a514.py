code = """import json
import re
import pandas as pd

with open(var_call_fyy8qeXrrcwP3ziXUvVy0mmB, 'r', encoding='utf-8') as f:
    citations = json.load(f)
with open(var_call_i0bVz9Wu1fG8bFGs1JMg6jmP, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# DataFrames
df_c = pd.DataFrame(citations)
df_docs = pd.DataFrame(docs)

# Normalize titles
if 'filename' in df_docs.columns:
    df_docs['title'] = df_docs['filename'].str.replace(r'\.txt$', '', regex=True)
else:
    df_docs['title'] = ''

# Merge on title
merged = pd.merge(df_c, df_docs[['title','text']], on='title', how='left')

# Identify CHI by searching for 'CHI' near the top (first 500 chars) or patterns like "'CHI" or "CHI'" or 'SIGCHI'
chi_patterns = [r"\bCHI\b", r"'CHI", r"CHI'", r"SIGCHI", r"ACM CHI", r"Proceedings of the CHI"]
pattern = re.compile('|'.join(chi_patterns), flags=re.IGNORECASE)

def text_has_chi(t):
    if not isinstance(t, str):
        return False
    head = t[:1000]
    return bool(pattern.search(head))

merged['is_chi'] = merged['text'].apply(text_has_chi)

# Filter citations that are CHI papers
df_chi = merged[merged['is_chi']].copy()

# Convert citation_count
df_chi['citation_count'] = pd.to_numeric(df_chi['citation_count'], errors='coerce').fillna(0).astype(int)

records = df_chi[['title','citation_count']].to_dict(orient='records')
total = int(df_chi['citation_count'].sum())

result = {'papers': records, 'total_citations_2020': total, 'num_papers': len(records)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_fyy8qeXrrcwP3ziXUvVy0mmB': 'file_storage/call_fyy8qeXrrcwP3ziXUvVy0mmB.json', 'var_call_i0bVz9Wu1fG8bFGs1JMg6jmP': 'file_storage/call_i0bVz9Wu1fG8bFGs1JMg6jmP.json', 'var_call_Zj5sk21Zs04TPPnVwAeZMNyZ': {'papers': [], 'total_citations_2020': 0}, 'var_call_5R56JzxbhTxICTwkZKogpw0n': {'papers': [], 'total_citations_2020': 0}, 'var_call_YAHclIqBHg7QzcUEh7OnBzPm': {'sample_citation_titles_first_20': ['Sundroid: Solar Radiation Awareness with Smartphones', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'Why We Use and Abandon Smart Devices', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'Barriers to Engagement with a Personal Informatics Productivity Tool', 'Modeling Interdependent and Periodic Real-World Action Sequences', 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'How to Drive a London Bus: Measuring Performance in a Mobile and Remote Workplace', 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations', 'A Lived Informatics Model of Personal Informatics', 'Charting Design Preferences on Wellness Wearables', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'Heed: Exploring the Design of Situated Self-Reporting Devices', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection'], 'sample_doc_filenames_first_50': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt', "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt", 'Blood Pressure Beyond the Clinic: Rethinking a Health Metric for Everyone.txt', 'Charting Design Preferences on Wellness Wearables.txt', 'ClimbSense: Automatic Climbing Route Recognition Using Wrist-worn Inertia Measurement Units.txt', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt", 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings.txt', 'Communicating Uncertainty in Fertility Prognosis.txt', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media.txt', 'ConCap: Designing to Empower Individual Reflection on Chronic Conditions Using Mobile Apps.txt', 'Contextual Influences on the Use and Non-Use of Digital Technology While Exercising at the Gym.txt', 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness.txt', 'DataSelfie: Empowering People to Design Personalized Visuals to Represent Their Data.txt', 'Defining Adherence: Making Sense of Physical Activity Tracker Data.txt', 'Designing a Wellness Self-management Tool for Older Adults: Results from a Field Trial of YourWellness.txt', 'Designing in the Dark: Eliciting Self-tracking Dimensions for Understanding Enigmatic Disease.txt', 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers.txt', 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance.txt', 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats.txt', 'Entangled with Numbers: Quantified Self and Others in a Team-Based Online Game.txt', 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing.txt', 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers.txt', 'Exploring the Value of Parent Tracked Baby Data in Interactions with Healthcare Professionals: A Data-Enabled Design Exploration.txt', 'Fine-grained Sharing of Sensed Physical Activity: A Value Sensitive Approach.txt', 'From Nobody Cares to Way to Go!: A Design Framework for Social Sharing in Personal Informatics.txt', 'FutureSelf: What Happens When We Forecast Self-Trackers? Future Health Statuses?.txt', 'Goal-oriented Visualizations of Activity Tracking: A Case Study with Engineering Students.txt', 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal.txt', 'Heed: Exploring the Design of Situated Self-Reporting Devices.txt', 'How Information Sharing About Care Recipients by Family Caregivers Impacts Family Communication.txt', 'How to Drive a London Bus: Measuring Performance in a Mobile and Remote Workplace.txt', 'Intelligent Computing in Personal Informatics: Key Design Considerations.txt', "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps.txt", 'Leveraging Intermediated Interactions to Support Utilization of Persuasive Personal Health Informatics.txt', 'Live Interest Meter: Learning from Quantified Feedback in Mass Lectures.txt', 'Lullaby: A Capture & Access System for Understanding the Sleep Environment.txt', 'Making Sense of Sleep Sensors: How Sleep Sensing Technologies Support and Undermine Sleep Health.txt', "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure.txt", 'No Forests Without Trees: Particulars and Patterns in Visualizing Personal Communication.txt', 'No Longer Wearing: Investigating the Abandonment of Personal Health-tracking Technologies on Craigslist.txt', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App.txt', 'Opportunities for Oral Health Monitoring Technologies Beyond the Dental Clinic.txt', 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations.txt', 'Pass the Ball: Enforced Turn-Taking in Activity Tracking.txt']}}

exec(code, env_args)
