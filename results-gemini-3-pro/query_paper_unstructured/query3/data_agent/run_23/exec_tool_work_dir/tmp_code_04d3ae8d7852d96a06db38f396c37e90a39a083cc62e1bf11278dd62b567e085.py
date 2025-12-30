code = """import json
import re

file_path = locals()['var_function-call-4838891230296315133']
with open(file_path, 'r') as f:
    papers = json.load(f)

info = []
for p in papers:
    text = p.get('text', '')
    years_strs = re.findall(r'20\d{2}', text)
    years = [int(y) for y in years_strs if 2000 <= int(y) <= 2025]
    max_year = max(years) if years else "None"
    info.append({"title": p['filename'], "max_year": max_year})

print("__RESULT__:")
print(json.dumps(info))"""

env_args = {'var_function-call-12813325699209905495': 'file_storage/function-call-12813325699209905495.json', 'var_function-call-4838891230296315133': 'file_storage/function-call-4838891230296315133.json', 'var_function-call-7940884221126680243': [], 'var_function-call-10237573905537353095': {'count': 5, 'first_paper_preview': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard University\nCambridge, MA, USA\neyue@college.harvard.edu\n\nABSTRACT\nSelf-tracking physiological and psychological data poses the\nchallenge of presentation and interpretation. Insightful nar-\nratives for self-', 'first_filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, 'var_function-call-3171940235740849659': [], 'var_function-call-8299822262991482344': [{'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'years_found': []}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'years_found': []}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt', 'years_found': []}, {'filename': 'Charting Design Preferences on Wellness Wearables.txt', 'years_found': []}, {'filename': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt", 'years_found': []}], 'var_function-call-15795029037569779783': ['A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App'], 'var_function-call-11594253664732293282': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': '265'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': '266'}]}

exec(code, env_args)
