code = """import json

file_path = locals()['var_function-call-4863138715288248504']
with open(file_path, 'r') as f:
    papers = json.load(f)

filenames_to_check = [
    "A Stage-based Model of Personal Informatics Systems.txt",
    "A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt",
    "A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt"
]

snippets = {}
for paper in papers:
    if paper['filename'] in filenames_to_check:
        snippets[paper['filename']] = paper['text'][:500]

print("__RESULT__:")
print(json.dumps(snippets))"""

env_args = {'var_function-call-1438467208148862698': 'file_storage/function-call-1438467208148862698.json', 'var_function-call-987307425493553399': 'file_storage/function-call-987307425493553399.json', 'var_function-call-4863138715288248504': 'file_storage/function-call-4863138715288248504.json', 'var_function-call-6286417956079604125': [], 'var_function-call-2642568662990670730': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'years_found': ['2015'], 'header_snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'years_found': [], 'header_snippet': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'years_found': [], 'header_snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'years_found': [], 'header_snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E'}], 'var_function-call-16800725899917521487': 5, 'var_function-call-6303312242109604911': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'header_years': ['2015'], 'all_years_count': 46, 'has_domain': True}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'header_years': [], 'all_years_count': 47, 'has_domain': True}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'header_years': [], 'all_years_count': 70, 'has_domain': True}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'header_years': [], 'all_years_count': 119, 'has_domain': True}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'header_years': [], 'all_years_count': 72, 'has_domain': False}]}

exec(code, env_args)
