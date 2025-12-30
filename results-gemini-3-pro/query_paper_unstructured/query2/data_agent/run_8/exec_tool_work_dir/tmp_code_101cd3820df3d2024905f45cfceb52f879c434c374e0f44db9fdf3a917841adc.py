code = """import json

file_path_docs = locals()['var_function-call-3540073977128497152']
with open(file_path_docs, 'r') as f:
    docs = json.load(f)

target_title = "One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App"
target_doc = next((d for d in docs if d['filename'] == target_title + ".txt"), None)

if target_doc:
    print("__RESULT__:")
    print(json.dumps(target_doc['text']))
else:
    print("__RESULT__:")
    print(json.dumps("Not Found"))"""

env_args = {'var_function-call-17666330447833607191': 'file_storage/function-call-17666330447833607191.json', 'var_function-call-11031819639720739797': 'file_storage/function-call-11031819639720739797.json', 'var_function-call-11580890549591616551': 158, 'var_function-call-15015239705628452412': 'file_storage/function-call-15015239705628452412.json', 'var_function-call-12301809577552988153': 'file_storage/function-call-12301809577552988153.json', 'var_function-call-291982586650051971': 'file_storage/function-call-291982586650051971.json', 'var_function-call-7820464138049076348': 5, 'var_function-call-3540073977128497152': 'file_storage/function-call-3540073977128497152.json', 'var_function-call-16924924423564672170': 60.092592592592595, 'var_function-call-2801795861932674547': {'total_cited_papers': 158, 'papers_found_in_docs': 55, 'acm_papers_count': 54, 'avg': 60.092592592592595}, 'var_function-call-11335091958675771062': 99, 'var_function-call-3869507606233161924': {'intersection_count': 55, 'missing_docs_count': 103, 'extra_docs_count': 44, 'sample_missing': ['Help Me Help You: Shared Reflection for Personal Data', "Understanding Quantified-selfers' Practices in Collecting and Exploring Personal Data", 'Personal Informatics in Chronic Illness Management', 'Snot, Sweat, Pain, Mud, and Snow: Performance and Experience in the Use of Sports Watches', 'Health Multimedia: Lifestyle Recommendations Based on Diverse Observations'], 'sample_extra': ['Personalization Revisited: A Reflective Approach Helps People Better Personalize Health Services and Motivates Them to Increase Physical Activity', 'Patient Perspectives on Self-Management Technologies for Chronic Fatigue Syndrome', 'MoodLight: Exploring Personal and Social Implications of Ambient Display of Biosensor Data', 'A Stage-based Model of Personal Informatics Systems', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application"]}, 'var_function-call-11727531475390724060': [{'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'text_preview': '\n\nOne Step Forward, Two Steps Back: The Key to \nWearables in the Field is the App \n\nBliss Altenhoff, Haley Vaigneur and Kelly Caine \nDepartment of Psychology, Department of Industrial Engineering, Sch'}]}

exec(code, env_args)
