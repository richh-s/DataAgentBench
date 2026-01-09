code = """import json, re

def load_maybe_path(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

docs = load_maybe_path(var_call_gTRoysy304z0d0jMDBpm8Hii)

chi_titles=set()
for d in docs:
    fn=d.get('filename','')
    title=fn[:-4] if fn.lower().endswith('.txt') else fn
    text=(d.get('text') or '')
    head=text[:12000]
    # look for explicit proceedings lines
    if re.search(r"\bCHI\s*'\d{2}\b", head):
        chi_titles.add(title); continue
    if re.search(r"Proceedings\s+of\s+the\s+SIGCHI", head, re.IGNORECASE):
        chi_titles.add(title); continue
    if re.search(r"\bSIGCHI\b", head):
        # may still be CHI
        if re.search(r"\bCHI\b", head):
            chi_titles.add(title); continue

print('__RESULT__:')
print(json.dumps({"num":len(chi_titles),"sample":sorted(list(chi_titles))[:20]}))"""

env_args = {'var_call_J8txm9Nm7LXRKe115bQZgmuM': 'file_storage/call_J8txm9Nm7LXRKe115bQZgmuM.json', 'var_call_gTRoysy304z0d0jMDBpm8Hii': 'file_storage/call_gTRoysy304z0d0jMDBpm8Hii.json', 'var_call_o7UdNyy6q6k4D0wRTLCPmT1C': {'total_citation_count_for_CHI_papers_cited_in_2020': 0, 'num_CHI_papers_matched': 0}, 'var_call_R4pn9lj8tqFzL717v1cJhOhe': [{'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'head': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowledge.  A  class  of  systems \ncalled  personal  informatics  is  appearing  that  help  people \ncollect and reflect on personal information. However, there \nis no comprehensive list of problems that use'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'head': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard University\nCambridge, MA, USA\neyue@college.harvard.edu\n\nABSTRACT\nSelf-tracking physiological and psychological data poses the\nchallenge of presentation and interpretation. Insightful nar-\nratives for self-'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'head': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  condition, \naffecting  20%  of  the  population.  Even  though  it  is  a \ntreatable  condition,  people  often  do  not  seek  treatment.  In \nthis paper, we  describe how we co-designed and evaluated \nwith'}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt', 'head': 'Barriers and Negative Nudges:  \nExploring Challenges in Food Journaling   \nFelicia Cordeiro1, Daniel A. Epstein1, Edison Thomaz3, Elizabeth Bales1,2, \nArvind K. Jagannathan3, Gregory D. Abowd3, James Fogarty1 \n\n1 Computer Science & Engineering \n2 Human Centered Design & Engineering \nDUB Group, University of Washington \n{felicia0, depstein, lizbales, jfogarty} \n@cs.washington.edu \n\nABSTRACT  \nAlthough food journaling is understood to be both important \nand  difficult,  little  work  has  empirica'}, {'filename': 'Barriers to Engagement with a Personal Informatics Productivity Tool.txt', 'head': ' Barriers to Engagement with a Personal Informatics \nProductivity Tool \nJon Bird \nCity University London \nSchool of Engineering & \nMathematical Sciences \nLondon, EC1V 0HB \nJon.bird@city.ac.uk \n\nCassie Cornish-Tresstail \nUCL Interaction Centre \nGower Street \nLondon, W1CE 6BT \ncassandra.cornish-\ntrestrail.10@ucl.ac.uk \n\nAnna L Cox \nUCL Interaction Centre \nGower Street \nLondon, W1CE 6BT \nAnna.cox@ucl.ac.uk \n\nEmily I M Collins \nUCL Interaction Centre \nGower Street \nLondon, W1CE 6BT \ne.collins@ucl.ac'}]}

exec(code, env_args)
