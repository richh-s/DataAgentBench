code = """import json
import re

file_path = locals()['var_function-call-16322124554372865657']
with open(file_path, 'r') as f:
    papers = json.load(f)

target_title = "Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use"
target_paper = None
for p in papers:
    if target_title in p['filename']:
        target_paper = p
        break

if target_paper:
    text = target_paper['text']
    # Find all 2016 occurrences and print context
    matches = [m.start() for m in re.finditer('2016', text)]
    contexts = []
    for idx in matches:
        start = max(0, idx - 50)
        end = min(len(text), idx + 50)
        contexts.append(text[start:end].replace('\n', ' '))
    print("__RESULT__:")
    print(json.dumps(contexts))"""

env_args = {'var_function-call-4836586951926601287': ['paper_docs'], 'var_function-call-4836586951926600548': 'file_storage/function-call-4836586951926600548.json', 'var_function-call-218136711215706544': 'file_storage/function-call-218136711215706544.json', 'var_function-call-16322124554372865657': 'file_storage/function-call-16322124554372865657.json', 'var_function-call-805702450646494683': [], 'var_function-call-10525079842332072840': ['Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard University\nCambridge, MA, USA\neyue@college.harvard.edu\n\nABSTRACT\nSelf-tracking physiological and psychological data poses the\nchallenge of presentation and interpretation. Insightful nar-\nratives for self-', 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  condition, \naffecting  20%  of  the  population.  Even  though  it  is  a \ntreatable  condition,  people  often  do  not  seek  treatment.  In \nthis paper, we  describe how we co-designed and evaluated \nwith', 'Beyond Abandonment to Next Steps: Understanding and \nDesigning for Life after Personal Informatics Tool Use \n\nDaniel A. Epstein1, Monica Caraway2, Chuck Johnston2, \nAn Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {mcaraway, chuck2, anping, smunson}@uw.edu \n\nABSTRACT \nRecent  research  examines  how  and  why  people  abandon \nself-tracking tools. We exten'], 'var_function-call-16566829246681572860': ['Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use'], 'var_function-call-14301002802869887351': [{'id': '548', 'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'citation_count': '72', 'citation_year': '2017'}, {'id': '549', 'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'citation_count': '77', 'citation_year': '2018'}, {'id': '550', 'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'citation_count': '41', 'citation_year': '2019'}, {'id': '551', 'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'citation_count': '97', 'citation_year': '2020'}, {'id': '552', 'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'citation_count': '57', 'citation_year': '2021'}, {'id': '553', 'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'citation_count': '79', 'citation_year': '2022'}, {'id': '554', 'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'citation_count': '93', 'citation_year': '2023'}, {'id': '555', 'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'citation_count': '65', 'citation_year': '2024'}, {'id': '556', 'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'citation_count': '55', 'citation_year': '2025'}], 'var_function-call-15365358246560073191': 'Beyond Abandonment to Next Steps: Understanding and \nDesigning for Life after Personal Informatics Tool Use \n\nDaniel A. Epstein1, Monica Caraway2, Chuck Johnston2, \nAn Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {mcaraway, chuck2, anping, smunson}@uw.edu \n\nABSTRACT \nRecent  research  examines  how  and  why  people  abandon \nself-tracking tools. We extend this work with new insights \ndrawn from people reflecting on their experiences after they \nstop tracking, examining how designs continue to influence \npeople  even  after  abandonment.  We  further  contrast  prior \nwork  considering  abandonment  of  health  and  wellness \ntracking  tools  with  an  exploration  of  why  people  abandon \nfinancial  and  location  tracking  tools,  and  we  connect  our \nfindings  to  models  of  personal  informatics.  Surveying  193 \npeople and interviewing '}

exec(code, env_args)
