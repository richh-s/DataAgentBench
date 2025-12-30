code = """import json
import re

file_papers = locals()['var_function-call-16262289729118297755']
file_citations = locals()['var_function-call-16262289729118296254']

with open(file_papers, 'r') as f:
    papers = json.load(f)

with open(file_citations, 'r') as f:
    citations = json.load(f)

citation_map = {}
for c in citations:
    t = c['title']
    try:
        count = int(c['citation_count'])
    except:
        count = 0
    citation_map[t] = citation_map.get(t, 0) + count

results = []
debug_missed = []

for p in papers:
    text = p['text']
    filename = p['filename']
    title = filename.replace('.txt', '')
    
    if 'physical activity' not in text.lower():
        continue

    is_2016 = False
    
    # Check for Copyright 2016
    # Pattern: Copyright (C) 2016, Copyright 2016, (c) 2016
    # Also check specific conference names
    
    search_text = text[:5000] # Check first 5000 chars
    
    if re.search(r"Copyright\s+(?:©|\(c\))?\s*2016", search_text, re.IGNORECASE):
        is_2016 = True
    elif re.search(r"©\s*2016", search_text):
        is_2016 = True
    # Conference patterns: WORD '16 or WORD 2016
    # Venues: CHI, Ubicomp, CSCW, DIS, PervasiveHealth, WWW, IUI, OzCHI, TEI, AH
    elif re.search(r"\b(CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*(?:'|’)?16\b", search_text, re.IGNORECASE):
        is_2016 = True
    elif re.search(r"\b(CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*2016\b", search_text, re.IGNORECASE):
        is_2016 = True
    
    if is_2016:
        count = citation_map.get(title, 0)
        results.append({"title": title, "total_citation_count": count})
    else:
        # Debug why it missed if 2016 is in text (it should be, due to mongo filter)
        # Maybe it's a 2015 paper with a 2016 citation?
        if "2016" in text[:1000]:
             debug_missed.append({"title": title, "excerpt": text[:300]})

print("__RESULT__:")
print(json.dumps(results))
# Also print debug info to stdout (not in __RESULT__) to help me if empty
if not results:
    print("DEBUG MISSED:")
    print(json.dumps(debug_missed[:3]))"""

env_args = {'var_function-call-3509049514350352642': 'file_storage/function-call-3509049514350352642.json', 'var_function-call-3509049514350351227': ['Citations', 'sqlite_sequence'], 'var_function-call-16262289729118297755': 'file_storage/function-call-16262289729118297755.json', 'var_function-call-16262289729118296254': 'file_storage/function-call-16262289729118296254.json', 'var_function-call-3925576988295596012': [], 'var_function-call-15489539225406102593': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'excerpt': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard University\nCambridge, MA, USA\neyue@college.harvard.edu\n\nABSTRACT\nSelf-tracking physiological and psychological data poses the\nchallenge of presentation and interpretation. Insightful nar-\nratives for self-'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'excerpt': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  condition, \naffecting  20%  of  the  population.  Even  though  it  is  a \ntreatable  condition,  people  often  do  not  seek  treatment.  In \nthis paper, we  describe how we co-designed and evaluated \nwith'}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt', 'excerpt': 'Beyond Abandonment to Next Steps: Understanding and \nDesigning for Life after Personal Informatics Tool Use \n\nDaniel A. Epstein1, Monica Caraway2, Chuck Johnston2, \nAn Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {mcaraway, chuck2, anping, smunson}@uw.edu \n\nABSTRACT \nRecent  research  examines  how  and  why  people  abandon \nself-tracking tools. We exten'}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt", 'excerpt': 'Beyond Behavior: The Coach’s Perspective \n on Technology in Health Coaching \n\nHeleen Rutjes \n Human-Technology Interaction \n Eindhoven University of Technology \n Eindhoven, the Netherlands \n H.Rutjes@tue.nl \n\nMartijn C. Willemsen \n Human-Technology Interaction \n Eindhoven University of Technology \n Eindhoven, the Netherlands \n M.C.Willemsen@tue.com \n\nWijnand A. IJsselsteijn  \nHuman-Technology Interaction \n Eindhoven University of Technology \n Eindhoven, the Netherlands \n W.A.IJsselsteijn@tue.com'}, {'title': 'Charting Design Preferences on Wellness Wearables.txt', 'excerpt': 'Charting Design Preferences on Wellness Wearables  \n\nJuho Rantakari1, Virve Inget2, Ashley Colley1, Jonna Häkkilä1 \n\n1University of Lapland \nYliopistokatu 8 \n96400 Rovaniemi, Finland \nfirstname.lastname@ulapland.fi \n\n2Center for Ubiquitous Computing \nP.O Box 4500 \n90014 University of Oulu, Finland \nfirstname.lastname@oulu.fi \n\nABSTRACT \nThis paper presents a study on people’s preferences with wearable \nwellness  devices.  The  results  are  based  on  an  online  survey \n(n=84),  where  people  '}]}

exec(code, env_args)
