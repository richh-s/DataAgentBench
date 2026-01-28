code = """import json

with open(locals()['var_function-call-15503541887771276820'], 'r') as f:
    citations = json.load(f)

filenames = [c['title'] + ".txt" for c in citations]
print("__RESULT__:")
print(json.dumps(filenames))"""

env_args = {'var_function-call-15503541887771276820': 'file_storage/function-call-15503541887771276820.json', 'var_function-call-11206421856392368221': {'count': 158, 'first_10': ['Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing.txt', 'Sundroid: Solar Radiation Awareness with Smartphones.txt', 'Why We Use and Abandon Smart Devices.txt', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App.txt', 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set.txt', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt", 'Reviewing Reflection: On the Use of Reflection in Interactive System Design.txt', 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers.txt', 'Beyond Self-Tracking and Reminders: Designing Smartphone Apps That Support Habit Formation.txt', 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection.txt']}}

exec(code, env_args)
