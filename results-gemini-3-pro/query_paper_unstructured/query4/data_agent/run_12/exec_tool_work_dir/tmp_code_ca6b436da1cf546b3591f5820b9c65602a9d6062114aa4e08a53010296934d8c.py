code = """import json

file_path = locals()['var_function-call-5896966146300588964']
with open(file_path, 'r') as f:
    papers = json.load(f)

results = []
for p in papers:
    text = p.get('text', '')
    if 'physical activity' in text.lower() and '2016' in text:
        # Find all occurrences of 2016 in the first 5000 chars (headers)
        # If found in header, likely publication year.
        # If only found deep in text, likely citation.
        snippet_header = text[:5000]
        if '2016' in snippet_header:
            # Get context
            idx = snippet_header.find('2016')
            ctx = snippet_header[max(0, idx-100):min(len(snippet_header), idx+100)]
            results.append({'filename': p['filename'], 'context': ctx})

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_function-call-2683298839036433804': ['paper_docs'], 'var_function-call-17469928963468779101': 'file_storage/function-call-17469928963468779101.json', 'var_function-call-5896966146300588964': 'file_storage/function-call-5896966146300588964.json', 'var_function-call-15408307413232285076': [], 'var_function-call-3201152881564540203': ['Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard University\nCambridge, MA, USA\neyue@college.harvard.edu\n\nABSTRACT\nSelf-tracking physiological and psychological data poses the\nchallenge of presentation and interpretation. Insightful nar-\nratives for self-', 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  condition, \naffecting  20%  of  the  population.  Even  though  it  is  a \ntreatable  condition,  people  often  do  not  seek  treatment.  In \nthis paper, we  describe how we co-designed and evaluated \nwith', 'Beyond Abandonment to Next Steps: Understanding and \nDesigning for Life after Personal Informatics Tool Use \n\nDaniel A. Epstein1, Monica Caraway2, Chuck Johnston2, \nAn Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {mcaraway, chuck2, anping, smunson}@uw.edu \n\nABSTRACT \nRecent  research  examines  how  and  why  people  abandon \nself-tracking tools. We exten', 'Beyond Behavior: The Coach’s Perspective \n on Technology in Health Coaching \n\nHeleen Rutjes \n Human-Technology Interaction \n Eindhoven University of Technology \n Eindhoven, the Netherlands \n H.Rutjes@tue.nl \n\nMartijn C. Willemsen \n Human-Technology Interaction \n Eindhoven University of Technology \n Eindhoven, the Netherlands \n M.C.Willemsen@tue.com \n\nWijnand A. IJsselsteijn  \nHuman-Technology Interaction \n Eindhoven University of Technology \n Eindhoven, the Netherlands \n W.A.IJsselsteijn@tue.com', 'Charting Design Preferences on Wellness Wearables  \n\nJuho Rantakari1, Virve Inget2, Ashley Colley1, Jonna Häkkilä1 \n\n1University of Lapland \nYliopistokatu 8 \n96400 Rovaniemi, Finland \nfirstname.lastname@ulapland.fi \n\n2Center for Ubiquitous Computing \nP.O Box 4500 \n90014 University of Oulu, Finland \nfirstname.lastname@oulu.fi \n\nABSTRACT \nThis paper presents a study on people’s preferences with wearable \nwellness  devices.  The  results  are  based  on  an  online  survey \n(n=84),  where  people  '], 'var_function-call-8273447706356724648': [], 'var_function-call-4497238418139650191': {'count': 5, 'examples': [['A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'ng, François\n\nGuimbetiere, and Tanzeem Choudhury. 2016.\nEmotionCheck: leveraging bodily signals and '], ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'Paul  Dendale,  Kris  Luyten  and  Karin \nConinx. 2016. Back on bike: the BoB mobile cycling app for'], ['Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt', "ons from Permissions@acm.org. \nCHI'16, May 07-12, 2016, San Jose, CA, USA  \n© 2016 ACM. ISBN 978-1-4"]]}}

exec(code, env_args)
