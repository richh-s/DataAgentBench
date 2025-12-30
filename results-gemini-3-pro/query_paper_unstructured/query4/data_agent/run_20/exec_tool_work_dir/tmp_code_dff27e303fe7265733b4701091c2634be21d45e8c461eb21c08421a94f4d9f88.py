code = """import json
import re

file_path = locals()['var_function-call-5659440359998634894']
with open(file_path, 'r') as f:
    papers = json.load(f)

targets = ["A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt", "A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt"]

snippets = {}
for p in papers:
    if p['filename'] in targets:
        text = p['text']
        indices = [m.start() for m in re.finditer('2016', text)]
        p_snippets = []
        for i in indices:
            s = text[max(0, i-50):min(len(text), i+50)]
            p_snippets.append(s)
        snippets[p['filename']] = p_snippets

print("__RESULT__:")
print(json.dumps(snippets))"""

env_args = {'var_function-call-7797754870209307186': 'file_storage/function-call-7797754870209307186.json', 'var_function-call-5659440359998634894': 'file_storage/function-call-5659440359998634894.json', 'var_function-call-5805009466190750349': [], 'var_function-call-5373249832684589791': ["UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characteriz", 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowledge.  A  class  of  systems \ncalled  personal  informatics  is  appearing  that  help  people \ncollect and reflect on personal information. However, there \nis no comprehensive list of problems that use', 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard University\nCambridge, MA, USA\neyue@college.harvard.edu\n\nABSTRACT\nSelf-tracking physiological and psychological data poses the\nchallenge of presentation and interpretation. Insightful nar-\nratives for self-', 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  condition, \naffecting  20%  of  the  population.  Even  though  it  is  a \ntreatable  condition,  people  often  do  not  seek  treatment.  In \nthis paper, we  describe how we co-designed and evaluated \nwith', ' Barriers to Engagement with a Personal Informatics \nProductivity Tool \nJon Bird \nCity University London \nSchool of Engineering & \nMathematical Sciences \nLondon, EC1V 0HB \nJon.bird@city.ac.uk \n\nCassie Cornish-Tresstail \nUCL Interaction Centre \nGower Street \nLondon, W1CE 6BT \ncassandra.cornish-\ntrestrail.10@ucl.ac.uk \n\nAnna L Cox \nUCL Interaction Centre \nGower Street \nLondon, W1CE 6BT \nAnna.cox@ucl.ac.uk \n\nEmily I M Collins \nUCL Interaction Centre \nGower Street \nLondon, W1CE 6BT \ne.collins@ucl.ac'], 'var_function-call-3695825724961897250': [], 'var_function-call-17915866204133786997': ['A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt']}

exec(code, env_args)
