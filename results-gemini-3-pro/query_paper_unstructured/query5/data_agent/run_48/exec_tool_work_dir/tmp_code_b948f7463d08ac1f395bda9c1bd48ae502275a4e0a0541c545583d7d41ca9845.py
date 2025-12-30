code = """import json
import os

data = locals()['var_function-call-12857888049469737703']
if isinstance(data, str) and os.path.exists(data):
    with open(data, 'r') as f:
        all_files = json.load(f)
else:
    all_files = data

# Load citations (this one was definitely a file path in previous calls)
cit_data = locals()['var_function-call-264858034059979045']
if isinstance(cit_data, str) and os.path.exists(cit_data):
    with open(cit_data, 'r') as f:
        citations = json.load(f)
else:
    citations = cit_data

db_filenames = set(f['filename'] for f in all_files)

matched = 0
matched_filenames = []
for c in citations:
    fname = c['title'] + ".txt"
    if fname in db_filenames:
        matched += 1
        matched_filenames.append(fname)
        
print(f"Total files in DB: {len(all_files)}")
print(f"Matches: {matched}")

print("__RESULT__:")
print(json.dumps({"total_files": len(all_files), "matches": matched, "matched_filenames": matched_filenames}))"""

env_args = {'var_function-call-264858034059979045': 'file_storage/function-call-264858034059979045.json', 'var_function-call-16262197769178367218': {'count': 188, 'sample_title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, 'var_function-call-2494524119581093015': 'file_storage/function-call-2494524119581093015.json', 'var_function-call-3380312142503180972': 'file_storage/function-call-3380312142503180972.json', 'var_function-call-8351315325764085192': 'file_storage/function-call-8351315325764085192.json', 'var_function-call-1959921926523090950': {'total_citations': 0, 'num_papers': 0}, 'var_function-call-8389437484024645991': 'Done', 'var_function-call-2898140987180465692': 'Done', 'var_function-call-8612993969594668577': {'total_citations': 114, 'num_papers': 2}, 'var_function-call-4793206800934394654': 'Done', 'var_function-call-14167168668467209418': {'matched': 5}, 'var_function-call-13560056867333161268': 'Done', 'var_function-call-54892687012586183': {}, 'var_function-call-8806135608073553679': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}, {'_id': '694f5530284b10b11dc0a86e', 'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}, {'_id': '694f5530284b10b11dc0a86f', 'filename': 'Barriers to Engagement with a Personal Informatics Productivity Tool.txt'}, {'_id': '694f5530284b10b11dc0a870', 'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt'}, {'_id': '694f5530284b10b11dc0a871', 'filename': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt"}, {'_id': '694f5530284b10b11dc0a872', 'filename': 'Blood Pressure Beyond the Clinic: Rethinking a Health Metric for Everyone.txt'}, {'_id': '694f5530284b10b11dc0a873', 'filename': 'Charting Design Preferences on Wellness Wearables.txt'}, {'_id': '694f5530284b10b11dc0a874', 'filename': 'ClimbSense: Automatic Climbing Route Recognition Using Wrist-worn Inertia Measurement Units.txt'}, {'_id': '694f5530284b10b11dc0a875', 'filename': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt"}, {'_id': '694f5530284b10b11dc0a876', 'filename': 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings.txt'}, {'_id': '694f5530284b10b11dc0a877', 'filename': 'Communicating Uncertainty in Fertility Prognosis.txt'}, {'_id': '694f5530284b10b11dc0a878', 'filename': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media.txt'}, {'_id': '694f5530284b10b11dc0a879', 'filename': 'ConCap: Designing to Empower Individual Reflection on Chronic Conditions Using Mobile Apps.txt'}, {'_id': '694f5530284b10b11dc0a87a', 'filename': 'Contextual Influences on the Use and Non-Use of Digital Technology While Exercising at the Gym.txt'}, {'_id': '694f5530284b10b11dc0a87b', 'filename': 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness.txt'}, {'_id': '694f5530284b10b11dc0a87c', 'filename': 'DataSelfie: Empowering People to Design Personalized Visuals to Represent Their Data.txt'}], 'var_function-call-12857888049469737703': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}]}

exec(code, env_args)
