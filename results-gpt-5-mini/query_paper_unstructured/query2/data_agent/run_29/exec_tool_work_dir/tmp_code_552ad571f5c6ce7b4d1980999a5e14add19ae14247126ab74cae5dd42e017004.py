code = """import json
import pandas as pd
import re

with open(var_call_l3PPpLM8azB2GyPcKmLRSWmP, 'r') as f:
    citations = json.load(f)
with open(var_call_LyPn518D1Z9V3O9rDu5LttwR, 'r') as f:
    papers = json.load(f)

# DataFrames
df_c = pd.DataFrame(citations)
df_p = pd.DataFrame(papers)

# Normalize citation_count
if 'citation_count' in df_c.columns:
    df_c['citation_count'] = pd.to_numeric(df_c['citation_count'], errors='coerce').fillna(0).astype(int)
else:
    df_c['citation_count'] = 0

# Extract title from filename
if 'filename' in df_p.columns:
    df_p['title'] = df_p['filename'].str.replace(r'\.txt$', '', regex=True)
else:
    df_p['title'] = None

# Normalize titles
def normalize_title(t):
    if t is None:
        return ''
    s = str(t).strip().lower()
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"[^0-9a-z ]+", "", s)
    return s

if 'title' in df_c.columns:
    df_c['title_norm'] = df_c['title'].apply(normalize_title)
else:
    df_c['title_norm'] = ['']*len(df_c)

df_p['title_norm'] = df_p['title'].apply(normalize_title)

# Robust ACM detection in text
def is_acm_text(text):
    if not isinstance(text, str):
        return False
    txt = text
    checks = [
        re.search(r'acm', txt, flags=re.I) is not None,
        re.search(r'\bdoi\.org/10\.1145', txt, flags=re.I) is not None,
        re.search(r'proceedings of the acm', txt, flags=re.I) is not None,
        re.search(r'copyright[\s\S]{0,30}acm', txt, flags=re.I) is not None,
        'acm press' in txt.lower(),
        'association for computing machinery' in txt.lower()
    ]
    return any(checks)

if 'text' in df_p.columns:
    df_p['source_is_acm'] = df_p['text'].apply(is_acm_text)
else:
    df_p['source_is_acm'] = False

# Merge on normalized title
df_p_min = df_p[['title_norm','source_is_acm','title']].copy()
df_merged = pd.merge(df_c, df_p_min, on='title_norm', how='left', indicator=True)

# Filter to ACM
df_acm = df_merged[df_merged['source_is_acm'] == True]

num_acm = int(len(df_acm))
avg = None
if num_acm>0:
    avg = round(float(df_acm['citation_count'].mean()), 2)

# Prepare sample
sample = []
for _,row in df_acm[['title','citation_count']].drop_duplicates().head(20).iterrows():
    sample.append({'title': row['title'] if pd.notna(row['title']) else None, 'citation_count': int(row['citation_count'])})

result = {
    'average_citation_count': None if avg is None else avg,
    'num_acm_citation_records': num_acm,
    'sample_acm_records': sample
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_l3PPpLM8azB2GyPcKmLRSWmP': 'file_storage/call_l3PPpLM8azB2GyPcKmLRSWmP.json', 'var_call_JpdX0be34W7QvGpbBwH5EoYN': ['paper_docs'], 'var_call_LyPn518D1Z9V3O9rDu5LttwR': 'file_storage/call_LyPn518D1Z9V3O9rDu5LttwR.json', 'var_call_ot8o1VcWilpQ4hD8fqPulUQC': {'average_citation_count': None, 'num_acm_papers_considered': 0}, 'var_call_XtWWLN8dMLbtU9XrALfuOBUX': 'file_storage/call_XtWWLN8dMLbtU9XrALfuOBUX.json', 'var_call_jx0Rd4Uv3k2QWGB5RZGnVZmA': {'average_citation_count': None, 'num_acm_citation_records_considered': 0, 'sample_acm_papers': []}, 'var_call_FR9XI9RTQfddcghl8QRqSj0N': {'num_citation_records': 158, 'num_paper_docs': 99, 'num_intersection_titles': 55, 'match_examples': [{'title_norm': 'intelligent computing in personal informatics key design considerations', 'paper_titles': ['Intelligent Computing in Personal Informatics: Key Design Considerations'], 'has_acm': False}, {'title_norm': 'blood pressure beyond the clinic rethinking a health metric for everyone', 'paper_titles': ['Blood Pressure Beyond the Clinic: Rethinking a Health Metric for Everyone'], 'has_acm': False}, {'title_norm': 'reviewing reflection on the use of reflection in interactive system design', 'paper_titles': ['Reviewing Reflection: On the Use of Reflection in Interactive System Design'], 'has_acm': False}, {'title_norm': 'live interest meter learning from quantified feedback in mass lectures', 'paper_titles': ['Live Interest Meter: Learning from Quantified Feedback in Mass Lectures'], 'has_acm': False}, {'title_norm': 'closing the gap supporting patients transition to selfmanagement after hospitalization', 'paper_titles': ["Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization"], 'has_acm': False}, {'title_norm': 'barriers and negative nudges exploring challenges in food journaling', 'paper_titles': ['Barriers and Negative Nudges: Exploring Challenges in Food Journaling'], 'has_acm': False}, {'title_norm': 'a lived informatics model of personal informatics', 'paper_titles': ['A Lived Informatics Model of Personal Informatics'], 'has_acm': False}, {'title_norm': 'steps choices and moral accounting observations from a stepcounting campaign in the workplace', 'paper_titles': ['Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace'], 'has_acm': False}, {'title_norm': 'quantified self meets social media sharing of weight updates on twitter', 'paper_titles': ['Quantified Self Meets Social Media: Sharing of Weight Updates on Twitter'], 'has_acm': False}, {'title_norm': 'making sense of sleep sensors how sleep sensing technologies support and undermine sleep health', 'paper_titles': ['Making Sense of Sleep Sensors: How Sleep Sensing Technologies Support and Undermine Sleep Health'], 'has_acm': False}, {'title_norm': 'sleeptight lowburden selfmonitoring technology for capturing and reflecting on sleep behaviors', 'paper_titles': ['SleepTight: Low-burden, Self-monitoring Technology for Capturing and Reflecting on Sleep Behaviors'], 'has_acm': False}, {'title_norm': 'contextual influences on the use and nonuse of digital technology while exercising at the gym', 'paper_titles': ['Contextual Influences on the Use and Non-Use of Digital Technology While Exercising at the Gym'], 'has_acm': False}, {'title_norm': 'reflective informatics conceptual dimensions for designing technologies of reflection', 'paper_titles': ['Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection'], 'has_acm': False}, {'title_norm': 'sensor requirements for activity recognition on smart watches', 'paper_titles': ['Sensor Requirements for Activity Recognition on Smart Watches'], 'has_acm': False}, {'title_norm': 'lullaby a capture  access system for understanding the sleep environment', 'paper_titles': ['Lullaby: A Capture & Access System for Understanding the Sleep Environment'], 'has_acm': False}, {'title_norm': 'why we use and abandon smart devices', 'paper_titles': ['Why We Use and Abandon Smart Devices'], 'has_acm': False}, {'title_norm': 'weve bin watching you designing for reflection and social persuasion to promote sustainable lifestyles', 'paper_titles': ["We'Ve Bin Watching You: Designing for Reflection and Social Persuasion to Promote Sustainable Lifestyles"], 'has_acm': False}, {'title_norm': 'goaloriented visualizations of activity tracking a case study with engineering students', 'paper_titles': ['Goal-oriented Visualizations of Activity Tracking: A Case Study with Engineering Students'], 'has_acm': False}, {'title_norm': 'tastybeats designing palatable representations of physical activity', 'paper_titles': ['TastyBeats: Designing Palatable Representations of Physical Activity'], 'has_acm': False}, {'title_norm': 'expense control a gamified semiautomated crowdbased approach for receipt capturing', 'paper_titles': ['Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing'], 'has_acm': False}], 'sample_citation_titles_first30': ['Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'Sundroid: Solar Radiation Awareness with Smartphones', 'Why We Use and Abandon Smart Devices', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'Reviewing Reflection: On the Use of Reflection in Interactive System Design', 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'Beyond Self-Tracking and Reminders: Designing Smartphone Apps That Support Habit Formation', 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'Barriers to Engagement with a Personal Informatics Productivity Tool', 'How to Drive a London Bus: Measuring Performance in a Mobile and Remote Workplace', 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations', 'A Lived Informatics Model of Personal Informatics', 'Charting Design Preferences on Wellness Wearables', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis', 'Technologies for Everyday Life Reflection: Illustrating a Design Space', 'Personal Tracking of Screen Time on Digital Devices', 'Sensor Requirements for Activity Recognition on Smart Watches', 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'Live Interest Meter: Learning from Quantified Feedback in Mass Lectures', 'Quantified Self Meets Social Media: Sharing of Weight Updates on Twitter', 'Pass the Ball: Enforced Turn-Taking in Activity Tracking', 'Blood Pressure Beyond the Clinic: Rethinking a Health Metric for Everyone', 'No Longer Wearing: Investigating the Abandonment of Personal Health-tracking Technologies on Craigslist', 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace', "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps", 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation'], 'sample_paper_filenames_first30': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt', 'Barriers to Engagement with a Personal Informatics Productivity Tool.txt', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt', "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt", 'Blood Pressure Beyond the Clinic: Rethinking a Health Metric for Everyone.txt', 'Charting Design Preferences on Wellness Wearables.txt', 'ClimbSense: Automatic Climbing Route Recognition Using Wrist-worn Inertia Measurement Units.txt', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt", 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings.txt', 'Communicating Uncertainty in Fertility Prognosis.txt', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media.txt', 'ConCap: Designing to Empower Individual Reflection on Chronic Conditions Using Mobile Apps.txt', 'Contextual Influences on the Use and Non-Use of Digital Technology While Exercising at the Gym.txt', 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness.txt', 'DataSelfie: Empowering People to Design Personalized Visuals to Represent Their Data.txt', 'Defining Adherence: Making Sense of Physical Activity Tracker Data.txt', 'Designing a Wellness Self-management Tool for Older Adults: Results from a Field Trial of YourWellness.txt', 'Designing in the Dark: Eliciting Self-tracking Dimensions for Understanding Enigmatic Disease.txt', 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers.txt', 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance.txt', 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats.txt', 'Entangled with Numbers: Quantified Self and Others in a Team-Based Online Game.txt', 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing.txt', 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers.txt', 'Exploring the Value of Parent Tracked Baby Data in Interactions with Healthcare Professionals: A Data-Enabled Design Exploration.txt']}}

exec(code, env_args)
