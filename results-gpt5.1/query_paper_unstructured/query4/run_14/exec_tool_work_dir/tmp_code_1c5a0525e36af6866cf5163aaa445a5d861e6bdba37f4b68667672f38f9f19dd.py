code = """import json, re, pandas as pd
from pathlib import Path

# load all physical-activity-related docs (no year filter)
path = Path(var_call_EZorOkUICpegXbhevhfpLZbl)
with path.open() as f:
    docs = json.load(f)

# helper to extract first plausible publication year (2010-2019)
def extract_year(text):
    m = re.search(r"\b(201[0-9])\b", text)
    return int(m.group(1)) if m else None

paper_years = {}
for d in docs:
    text = d.get('text','').lower()
    if 'physical activity' not in text:
        continue
    year = extract_year(d.get('text',''))
    if year:
        title = d.get('filename','').replace('.txt','')
        # keep earliest year seen
        paper_years[title] = min(paper_years.get(title, year), year)

print("__RESULT__:")
print(json.dumps(paper_years))"""

env_args = {'var_call_qNA1tdFUSzXCSy7o31tevlkI': 'file_storage/call_qNA1tdFUSzXCSy7o31tevlkI.json', 'var_call_zJwPKjsyq2sA33K6gjp7r1ed': ['Citations', 'sqlite_sequence'], 'var_call_asorXN4ntJuiv0JQNNYWRVhG': 'file_storage/call_asorXN4ntJuiv0JQNNYWRVhG.json', 'var_call_Pz5XSKhoFEAfXm9rl5irp9tc': ['A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'Activity Tracking in Vivo', 'Activity Tracking: Barriers, Workarounds and Customisation', 'Bringing New Voices to Design of Exercise Technology: Participatory Design with Vulnerable Young Adults', "But, I Don'T Take Steps: Examining the Inaccessibility of Fitness Trackers for Wheelchair Athletes", 'Data Representations for In-situ Exploration of Health and Fitness Data', 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'Facts, Interactivity and Videotape: Exploring the Design Space of Data in Interactive Video Storytelling', 'Family Health Promotion in Low-SES Neighborhoods: A Two-Month Study of Wearable Activity Tracking', 'Fine-grained Sharing of Sensed Physical Activity: A Value Sensitive Approach', 'FootStriker: An EMS-based Foot Strike Assistant for Running', 'Goal-oriented Visualizations of Activity Tracking: A Case Study with Engineering Students', 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'HealthyTogether: Exploring Social Incentives for Mobile Fitness Applications', 'How Do We Engage with Activity Trackers?: A Longitudinal Study of Habito', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'Low Sampling Rate for Physical Activity Recognition', "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure", 'Move into Another World of Happy: Insights for Designing Affect-based Physical Activity Interventions', 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations', 'Pass the Ball: Enforced Turn-Taking in Activity Tracking', 'Patina Engraver: Visualizing Activity Logs As Patina in Fashionable Trackers', 'Persistent Sharing of Fitness App Status on Twitter', 'Personalization Revisited: A Reflective Approach Helps People Better Personalize Health Services and Motivates Them to Increase Physical Activity', 'Persuasive Technology in the Real World: A Study of Long-term Use of Activity Sensing Devices for Fitness', 'Quantified Recess: Design of an Activity for Elementary Students Involving Analyses of Their Own Movement Data', 'Scaffolding for an OLM for Long-Term Physical Activity Goals', 'Sensor Requirements for Activity Recognition on Smart Watches', 'Sharing Automatically Tracked Activity Data: Implications for Therapists and People with Mobility Impairments', 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'Social Fabric Fitness: The Design and Evaluation of Wearable E-textile Displays to Support Group Running', 'Supporting Meaningful Personal Fitness: The Tracker Goal Evolution Model', 'SweatAtoms: Materializing Physical Activity', 'TastyBeats: Designing Palatable Representations of Physical Activity', 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', 'ThinkActive: Designing for Pseudonymous Activity Tracking in the Classroom', "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System", 'Understanding Physical Activity Through 3D Printed Material Artifacts', 'Using Context to Reveal Factors That Affect Physical Activity', 'VRFit: An Interactive Dashboard for Visualising of Virtual Reality Exercise and Daily Step Data', 'When Fitness Meets Social Networks: Investigating Fitness Tracking and Social Practices on WeRun', "When Fitness Trackers Don'T 'Fit': End-user Difficulties in the Assessment of Personal Tracking Device Accuracy"], 'var_call_NCw7GhASMwkGpO880rMTEVWm': [], 'var_call_EZorOkUICpegXbhevhfpLZbl': 'file_storage/call_EZorOkUICpegXbhevhfpLZbl.json', 'var_call_3HZknpp0s6HRJv1cZRfrC65P': []}

exec(code, env_args)
