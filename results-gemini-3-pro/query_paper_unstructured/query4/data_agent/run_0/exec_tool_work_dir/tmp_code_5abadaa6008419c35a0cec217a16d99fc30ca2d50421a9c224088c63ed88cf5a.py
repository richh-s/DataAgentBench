code = """import json
import re

file_path = locals()['var_function-call-2371613327861333471']

with open(file_path, 'r') as f:
    papers = json.load(f)

pa_pattern = re.compile(r"physical\s+activity", re.IGNORECASE)
header_year_regex = re.compile(r"(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)[\s\S]{0,50}(?:2016|'16)|Copyright\s*(?:©)?\s*2016|©\s*2016|ACM\s*2016|IEEE\s*2016", re.IGNORECASE)

titles = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # Check domain
    if not pa_pattern.search(text):
        continue

    # Check header for 2016
    header = text[:3000]
    if header_year_regex.search(header):
        title = filename.replace('.txt', '')
        titles.append(title)

print("__RESULT__:")
print(json.dumps(titles))"""

env_args = {'var_function-call-10785526798684626706': 'file_storage/function-call-10785526798684626706.json', 'var_function-call-5504457116591251088': 'file_storage/function-call-5504457116591251088.json', 'var_function-call-2371613327861333471': 'file_storage/function-call-2371613327861333471.json', 'var_function-call-15009766085818437093': [], 'var_function-call-3793400150331787097': [{'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'header': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard University\nCambridge, MA, USA\neyue@college.harvard.edu\n\nABSTRACT\nSelf-tracking physiological and psychological data poses the\nchallenge of presentation and interpretation. Insightful nar-\nratives for self-'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'header': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  condition, \naffecting  20%  of  the  population.  Even  though  it  is  a \ntreatable  condition,  people  often  do  not  seek  treatment.  In \nthis paper, we  describe how we co-designed and evaluated \nwith'}, {'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt', 'header': 'Beyond Abandonment to Next Steps: Understanding and \nDesigning for Life after Personal Informatics Tool Use \n\nDaniel A. Epstein1, Monica Caraway2, Chuck Johnston2, \nAn Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {mcaraway, chuck2, anping, smunson}@uw.edu \n\nABSTRACT \nRecent  research  examines  how  and  why  people  abandon \nself-tracking tools. We exten'}, {'filename': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt", 'header': 'Beyond Behavior: The Coach’s Perspective \n on Technology in Health Coaching \n\nHeleen Rutjes \n Human-Technology Interaction \n Eindhoven University of Technology \n Eindhoven, the Netherlands \n H.Rutjes@tue.nl \n\nMartijn C. Willemsen \n Human-Technology Interaction \n Eindhoven University of Technology \n Eindhoven, the Netherlands \n M.C.Willemsen@tue.com \n\nWijnand A. IJsselsteijn  \nHuman-Technology Interaction \n Eindhoven University of Technology \n Eindhoven, the Netherlands \n W.A.IJsselsteijn@tue.com'}, {'filename': 'Charting Design Preferences on Wellness Wearables.txt', 'header': 'Charting Design Preferences on Wellness Wearables  \n\nJuho Rantakari1, Virve Inget2, Ashley Colley1, Jonna Häkkilä1 \n\n1University of Lapland \nYliopistokatu 8 \n96400 Rovaniemi, Finland \nfirstname.lastname@ulapland.fi \n\n2Center for Ubiquitous Computing \nP.O Box 4500 \n90014 University of Oulu, Finland \nfirstname.lastname@oulu.fi \n\nABSTRACT \nThis paper presents a study on people’s preferences with wearable \nwellness  devices.  The  results  are  based  on  an  online  survey \n(n=84),  where  people  '}], 'var_function-call-8191779043002834645': [], 'var_function-call-4343706244245908380': 'Done', 'var_function-call-12593751550072133179': {'total_papers': 5, 'pa_count': 5, 'pa_2016_count': 5, 'contexts': ['101.\n\n5. Jean Costa, Alexander T Adams, Malte F Jung, François\n\nGuimbetiere, and Tanzeem Choudhury. 2016.\nEmotionCheck: leveraging bodily signals and false\nfeedback to regulate our emotions. In Procee', '/03/18/2973/ \n[22]  Eva  Geurts,  Mieke  Haesen,  Paul  Dendale,  Kris  Luyten  and  Karin \nConinx. 2016. Back on bike: the BoB mobile cycling app for secondary \nprevention  in  cardiac  patients. Pro', "specific permission\nand/or a fee. Request permissions from Permissions@acm.org. \nCHI'16, May 07-12, 2016, San Jose, CA, USA  \n© 2016 ACM. ISBN 978-1-4503-3362-7/16/05…$15.00  \nhttp://dx.doi.org/10.114", 'who is also a sports coach.  \n\nproviding \n\ncoaching \n\nonline \n\nand \n\nThe interviews, held in spring 2016, were semi-structured, \nand  conducted  by  one  researcher  in  a  face-to-face  setting. \nThe', 'requires prior specific permission \nand/or a fee. Request permissions from Permissions@acm.org. \nAH 2016, February 25-27, 2016, Geneva, Switzerland \n© 2016 ACM. ISBN 978-1-4503-3680-2/16/02…$15.00 \nDO']}}

exec(code, env_args)
