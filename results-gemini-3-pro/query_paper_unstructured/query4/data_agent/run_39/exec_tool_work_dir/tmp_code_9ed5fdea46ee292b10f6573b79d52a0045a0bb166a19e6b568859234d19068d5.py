code = """import json
import re

file_path = locals()['var_function-call-10008279034646517979']
with open(file_path, 'r') as f:
    papers = json.load(f)

candidates = []

venue_pattern = r"(CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|MobileHCI|UIST)"
year_pattern = r"('16|2016)"

for paper in papers:
    text = paper.get('text', '')
    # Search in first 2000 chars for header info
    head = text[:2000]
    # Search in last 2000 chars for footer info (sometimes copyright is at the end)
    tail = text[-2000:]
    
    combined = head + "\n" + tail
    
    # Check for Copyright 2016
    if re.search(r"Copyright\s+(\u00a9|&copy;)?\s*2016", combined, re.IGNORECASE):
        candidates.append(paper['filename'])
        continue
        
    # Check for Venue + 2016
    if re.search(venue_pattern + r".{0,20}" + year_pattern, combined, re.IGNORECASE):
        candidates.append(paper['filename'])
        continue

    # Check for "Permission ... 2016"
    if re.search(r"Permission.*2016", combined, re.IGNORECASE):
        candidates.append(paper['filename'])
        continue
        
print("__RESULT__:")
print(json.dumps(candidates))"""

env_args = {'var_function-call-14274151391044550289': 'file_storage/function-call-14274151391044550289.json', 'var_function-call-14274151391044549302': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-10008279034646517979': 'file_storage/function-call-10008279034646517979.json', 'var_function-call-10893568931888303487': [], 'var_function-call-408830920945652955': ["UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.wash", 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowled', 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard Unive', 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  conditi', ' Barriers to Engagement with a Personal Informatics \nProductivity Tool \nJon Bird \nCity University London \nSchool of Engineering & \nMathematical Sciences \nLondon, EC1V 0HB \nJon.bird@city.ac.uk \n\nCassie Cornish-Tresstail \nUCL Interaction Centre \nGower Street \nLondon, W1CE 6BT \ncassandra.cornish-\ntrest']}

exec(code, env_args)
