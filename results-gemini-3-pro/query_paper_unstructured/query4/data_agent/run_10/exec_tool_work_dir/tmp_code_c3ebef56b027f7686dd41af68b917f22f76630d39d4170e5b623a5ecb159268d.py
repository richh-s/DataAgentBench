code = """import json
import re

with open(locals()['var_function-call-14412117665521451328'], 'r') as f:
    papers = json.load(f)

papers_2016 = []
for p in papers:
    text = p.get('text', '')
    header = text[:1000]
    # Look for 2016 in header
    if '2016' in header:
        papers_2016.append({"title": p['filename'], "header": header[:300]})

print("__RESULT__:")
print(json.dumps(papers_2016))"""

env_args = {'var_function-call-16010210468405756630': 'file_storage/function-call-16010210468405756630.json', 'var_function-call-16010210468405758491': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-10417048927437287642': 'file_storage/function-call-10417048927437287642.json', 'var_function-call-14412117665521451328': 'file_storage/function-call-14412117665521451328.json', 'var_function-call-14412117665521453199': 'file_storage/function-call-14412117665521453199.json', 'var_function-call-12849824086341018331': [], 'var_function-call-17112652123555691582': {'count_domain': 4, 'count_year_1000': 0, 'count_both': 0, 'samples': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'header': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'header': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'header': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'header': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E'}]}, 'var_function-call-4625275472682914253': 'file_storage/function-call-4625275472682914253.json'}

exec(code, env_args)
