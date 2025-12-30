code = """import json
import pandas as pd

with open(locals()['var_function-call-12153821661542534380'], 'r') as f:
    papers_data = json.load(f)

matched_titles = ["A Lived Informatics Model of Personal Informatics", "ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation"]

snippets = {}
for p in papers_data:
    if p['filename'].replace('.txt', '') in matched_titles:
        snippets[p['filename']] = p['text'][:500] + "\n...\n" + p['text'][-500:]

print("__RESULT__:")
print(json.dumps(snippets))"""

env_args = {'var_function-call-12153821661542533629': 'file_storage/function-call-12153821661542533629.json', 'var_function-call-12153821661542534380': 'file_storage/function-call-12153821661542534380.json', 'var_function-call-7412265948695005483': 68.5, 'var_function-call-17202161529416673267': {'avg_loose': 68.5, 'avg_strict': 68.5, 'count_loose': 5, 'count_strict': 5}, 'var_function-call-11151052884622916441': {'citations_count': 158, 'papers_count': 5, 'sample_titles_citation': ['Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'Sundroid: Solar Radiation Awareness with Smartphones', 'Why We Use and Abandon Smart Devices', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set'], 'sample_filenames_paper': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt']}, 'var_function-call-1480742075555364436': ['paper_docs'], 'var_function-call-1480742075555364811': [{'_id': '694f5530284b10b11dc0a869'}, {'_id': '694f5530284b10b11dc0a86a'}, {'_id': '694f5530284b10b11dc0a86b'}, {'_id': '694f5530284b10b11dc0a86c'}, {'_id': '694f5530284b10b11dc0a86d'}], 'var_function-call-16619108135811056994': {'paper_titles': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation'], 'matched_titles': ['A Lived Informatics Model of Personal Informatics', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation'], 'matched_counts': ['50', '87'], 'average': 68.5}}

exec(code, env_args)
