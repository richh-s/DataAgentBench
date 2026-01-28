code = """import json
import re

with open(locals()['var_function-call-3535475471263660703'], 'r') as f:
    papers = json.load(f)

print(f"Total papers: {len(papers)}")

candidates_2016 = []

for p in papers:
    text = p.get('text', '')
    # Check for 2016 in first 2000 chars
    # Patterns: "2016", "'16"
    head = text[:3000]
    
    if "2016" in head:
        candidates_2016.append(p)
    elif re.search(r"\b'16\b", head):
        candidates_2016.append(p)

print(f"Papers with '2016' or ''16' in header: {len(candidates_2016)}")

for p in candidates_2016:
    print(f"Title: {p['filename']}")
    # print snippet where 2016 is found
    # idx = p['text'].find('2016')
    # if idx == -1: idx = p['text'].find("'16")
    # print(f"Context: {p['text'][idx-50:idx+50].replace('\n', ' ')}")
    
    # Check for domain
    if "physical activity" in p['text'].lower():
        print("  -> Has 'physical activity' in text")
    else:
        print("  -> NO 'physical activity'")"""

env_args = {'var_function-call-3353327849135623283': ['paper_docs'], 'var_function-call-3353327849135620318': ['Citations', 'sqlite_sequence'], 'var_function-call-869967969559808981': 'file_storage/function-call-869967969559808981.json', 'var_function-call-869967969559806992': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-3535475471263660703': 'file_storage/function-call-3535475471263660703.json', 'var_function-call-3656629748920796517': 'file_storage/function-call-3656629748920796517.json', 'var_function-call-8186264000082721214': [], 'var_function-call-5808988951641865091': {'count_physical_activity_anywhere': 4, 'count_2016_in_header': 0, 'sample_pa_paper_header': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.wash", 'sample_2016_paper_header': 'None'}, 'var_function-call-1514539215580408878': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'header': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.wash"}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'header': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowled'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'header': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard Unive'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'header': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  conditi'}]}

exec(code, env_args)
