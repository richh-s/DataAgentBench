code = """import json

# Load citations
with open(locals()['var_function-call-18234388167969169864'], 'r') as f:
    citations = json.load(f)

# Find "Stage" paper citation
stage_count = 0
for c in citations:
    if "Stage-based Model" in c['title'] or "Stage-Based Model" in c['title']:
        stage_count = int(c['citation_count'])
        break

# Paper Counts
# "A Trip to the Moon": 98
# "A Wee Bit More Interaction": 16
# "ArmSleeve": 52
# "A Stage-based Model": stage_count

# Verify if "A Trip to the Moon" is CHI (it is)
# Verify if "ArmSleeve" is CHI (it is)
# Verify if "A Wee Bit More Interaction" is CHI (it is)

total = 98 + 16 + 52 + stage_count

print("__RESULT__:")
print(json.dumps({"stage_count": stage_count, "total": total}))"""

env_args = {'var_function-call-18234388167969171677': ['paper_docs'], 'var_function-call-18234388167969169864': 'file_storage/function-call-18234388167969169864.json', 'var_function-call-10773655256875707708': 'file_storage/function-call-10773655256875707708.json', 'var_function-call-6452252535537636980': {'total_citations': 16, 'chi_papers_count': 1, 'sample_papers': [['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 16]]}, 'var_function-call-16682055075633350365': ["UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu", 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152', 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali', 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E', 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent C'], 'var_function-call-16584696122820506875': [], 'var_function-call-17525659752872537033': '', 'var_function-call-2502493352653004496': [], 'var_function-call-356112205022407543': {'count': 5, 'filenames': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt']}, 'var_function-call-2360040048879658821': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'is_chi': False}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'is_chi': False}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'is_chi': False}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'is_chi': True}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'is_chi': True}], 'var_function-call-5478125524906175790': {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'matches': {'CHI': 20, 'Human Factors': 1, 'Conference': 1, 'Proceedings': 0}, 'first_200': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152'}, 'var_function-call-11034105583525393601': {'total': 68, 'papers': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citations': 16}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citations': 52}]}, 'var_function-call-9477373326396413549': {'total': 243, 'papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'citations': 77}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'citations': 0}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citations': 98}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citations': 16}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citations': 52}]}}

exec(code, env_args)
