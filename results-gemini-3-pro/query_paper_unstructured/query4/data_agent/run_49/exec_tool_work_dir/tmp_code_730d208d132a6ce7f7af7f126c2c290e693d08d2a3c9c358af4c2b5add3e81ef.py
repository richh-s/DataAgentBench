code = """import json
import re

file_path = locals()['var_function-call-11172061455759427872']
with open(file_path, 'r') as f:
    papers = json.load(f)

papers_2016_all = []
venues = ["CHI", "UbiComp", "CSCW", "DIS", "PervasiveHealth", "WWW", "IUI", "OzCHI", "TEI", "AH"]
venue_pattern = r"(?i)(" + "|".join(venues) + r")[\s\S]{0,20}?(20[0-9]{2}|'[0-9]{2})"
copyright_pattern = r"(?i)Copyright[\s\S]{0,20}?(20[0-9]{2})"

for p in papers:
    text = p.get('text', '')
    found_years = []
    
    matches = re.findall(venue_pattern, text)
    for m in matches:
        y_str = m[1]
        if len(y_str) == 4:
            found_years.append(int(y_str))
        elif y_str.startswith("'"):
            found_years.append(int("20" + y_str[1:]))
            
    matches_cp = re.findall(copyright_pattern, text)
    for y_str in matches_cp:
        found_years.append(int(y_str))
        
    found_years = [y for y in found_years if 2000 <= y <= 2025]
    
    pub_year = max(found_years) if found_years else None
    
    if pub_year == 2016:
        papers_2016_all.append(p['filename'])

print('__RESULT__:')
print(json.dumps(papers_2016_all))"""

env_args = {'var_function-call-3489125586506889844': 'file_storage/function-call-3489125586506889844.json', 'var_function-call-3489125586506887483': ['Citations', 'sqlite_sequence'], 'var_function-call-13585702268998000327': 'file_storage/function-call-13585702268998000327.json', 'var_function-call-13585702268998000192': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-11172061455759427872': 'file_storage/function-call-11172061455759427872.json', 'var_function-call-12104304543771652425': [], 'var_function-call-12469198988654123846': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'candidates': []}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'candidates': []}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'candidates': []}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'candidates': []}], 'var_function-call-1351698192213324060': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'header': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu", 'years': ['2015']}], 'var_function-call-8254273891371820999': [], 'var_function-call-9585142687352628828': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'years': [2015]}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'years': []}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'years': []}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'years': []}], 'var_function-call-5890826038591021095': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowledge.  A  class  of  systems \ncalled  personal  informatics  is  appearing  that  help  people \ncollect and reflect on personal information. However, there \nis no comprehensive list of problems that users experience \nusing  these  systems,  and  no  guidance  for  making  these \nsystems  more  effective.  To  address  this,  we  conducted \nsurveys and interviews with people who collect and reflect \non  personal  information.  We  derived  a  stage-based  model \nof  personal  informatics  systems  composed  of  five  stages  \n(preparation, collection, integration, reflection, and action) \nand  identified  barriers  in  each  of  the  stages.  These  stages \nhave  four  essential  properties:  b', 'var_function-call-13808251501712543531': [], 'var_function-call-10500689497991568569': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'years_found': ['2015', 'Copyright 2015']}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'years_found': ['Copyright 2010']}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'years_found': []}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'years_found': []}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'years_found': []}], 'var_function-call-9819255489542778031': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  condition, \naffecting  20%  of  the  population.  Even  though  it  is  a \ntreatable  condition,  people  often  do  not  seek  treatment.  In \nthis paper, we  describe how we co-designed and evaluated \nwith', 'var_function-call-6402110201491853207': 'f My Soul – How People Bond with Their \nMobile Phones. In Proc. ACM MobileHCI’08. \n\n[61]   Lois M. Verbrugg 1980. Health diaries. Medical care 18.1: 73-95. \n[62]  Graham  Wilson  and  Stephen  A.  Brewster.  2017.  Multi-Moji: \nCombining  Thermal,  Vibrotactile  &  Visual  Stimuli  to  Expand  the \nAffective Range of Feedback. In Proc. CHI’17. \n\n[63]   2048, https://en.wikipedia.org/wiki/2048_(video_game) \n\nCHI 2019 Paper  CHI 2019, May 4–9, 2019, Glasgow, Scotland, UKPaper 703Page 14 \n \n \n \n \n\x0c', 'var_function-call-2332016280024086988': [], 'var_function-call-5450344732174506173': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'years_found': [2005, 2006, 2008, 2010, 2011, 2012, 2013, 2014, 2015], 'determined_year': 2015}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'years_found': [2003, 2006, 2008, 2009, 2010], 'determined_year': 2010}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'years_found': [2004, 2009, 2010, 2018], 'determined_year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'years_found': [2008, 2011, 2013, 2014, 2019], 'determined_year': 2019}]}

exec(code, env_args)
