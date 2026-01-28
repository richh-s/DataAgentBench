code = """import json

with open(locals()['var_function-call-4898156154949996726'], 'r') as f:
    paper_docs = json.load(f)

for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    if title not in ["A Lived Informatics Model of Personal Informatics", "ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation"]:
        print(f"--- {title} ---")
        print(doc.get('text', '')[:500])
        print("...")
print("__RESULT__:")
print("Done")"""

env_args = {'var_function-call-15503541887771276820': 'file_storage/function-call-15503541887771276820.json', 'var_function-call-11206421856392368221': {'count': 158, 'first_10': ['Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing.txt', 'Sundroid: Solar Radiation Awareness with Smartphones.txt', 'Why We Use and Abandon Smart Devices.txt', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App.txt', 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set.txt', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt", 'Reviewing Reflection: On the Use of Reflection in Interactive System Design.txt', 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers.txt', 'Beyond Self-Tracking and Reminders: Designing Smartphone Apps That Support Habit Formation.txt', 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection.txt']}, 'var_function-call-7875939014614819259': 'file_storage/function-call-7875939014614819259.json', 'var_function-call-509776034096291468': [{'_id': '694f5530284b10b11dc0a869'}, {'_id': '694f5530284b10b11dc0a86a'}, {'_id': '694f5530284b10b11dc0a86b'}, {'_id': '694f5530284b10b11dc0a86c'}, {'_id': '694f5530284b10b11dc0a86d'}], 'var_function-call-2979635559747287389': 5, 'var_function-call-10712887416649131953': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-4898156154949996726': 'file_storage/function-call-4898156154949996726.json', 'var_function-call-18280883742595085125': {'average': 68.5, 'count': 2, 'titles_found': [['A Lived Informatics Model of Personal Informatics', 50], ['ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 87]]}}

exec(code, env_args)
