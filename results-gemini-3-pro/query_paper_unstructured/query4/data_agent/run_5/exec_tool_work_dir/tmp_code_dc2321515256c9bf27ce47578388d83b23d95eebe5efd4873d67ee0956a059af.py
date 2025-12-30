code = """import json

with open(locals()['var_function-call-7732815880617685738'], 'r') as f:
    papers = json.load(f)

papers_with_2016 = []
for paper in papers:
    if '2016' in paper['text']:
        papers_with_2016.append(paper)

debug = []
if papers_with_2016:
    # Get snippets around "2016"
    for p in papers_with_2016[:5]:
        idx = p['text'].find('2016')
        snippet = p['text'][max(0, idx-50):min(len(p['text']), idx+50)]
        debug.append({"filename": p['filename'], "snippet": snippet})

print("__RESULT__:")
print(json.dumps(debug))"""

env_args = {'var_function-call-12176732640452715958': 'file_storage/function-call-12176732640452715958.json', 'var_function-call-9822203806490735992': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-7732815880617685738': 'file_storage/function-call-7732815880617685738.json', 'var_function-call-8701835322479169308': [], 'var_function-call-17030979673158927315': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'header_snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.wash"}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'header_snippet': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowled'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'header_snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard Unive'}], 'var_function-call-17187195514522168377': [], 'var_function-call-13325226924913816768': ['A Lived Informatics Model of Personal Informatics.txt']}

exec(code, env_args)
