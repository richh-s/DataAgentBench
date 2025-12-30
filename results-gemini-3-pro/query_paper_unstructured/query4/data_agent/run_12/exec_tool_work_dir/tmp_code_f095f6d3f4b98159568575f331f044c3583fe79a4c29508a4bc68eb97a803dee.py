code = """import json
import re

file_path = locals()['var_function-call-5896966146300588964']
with open(file_path, 'r') as f:
    papers = json.load(f)

matches = []
venue_pattern = re.compile(r'(CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)', re.IGNORECASE)

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    if 'physical activity' not in text.lower():
        continue
        
    # Check first 3000 chars for metadata
    header = text[:3000]
    
    is_2016 = False
    
    # Check for Copyright/Permission lines
    if re.search(r'(Copyright|©|Permission).*?2016', header, re.IGNORECASE):
        is_2016 = True
        # Double check it doesn't say "Copyright 2017" in the same block (e.g. if 2016 is mentioned in text)
        # But "Copyright ... 2016" is usually specific.
        
    # Check for Venue + 2016
    # e.g. "CHI 2016", "CHI '16"
    if venue_pattern.search(header):
        if re.search(r'(2016|\'16)\b', header):
             # We found a venue and 2016. Check proximity or just existence in header.
             # If "CHI 2015" is there, it might be 2015.
             # Let's count years found in header.
             years = re.findall(r'\b20(1[0-9])\b', header)
             # If 2016 is the most frequent or only year?
             # Or if 2016 is present and > 2016 is not.
             if '16' in years and not any(int(y) > 16 for y in years):
                 is_2016 = True
             elif re.search(r"'\s*16\b", header):
                 # Check for '17, '18
                 if not re.search(r"'\s*(1[7-9]|[2-9][0-9])\b", header):
                     is_2016 = True

    # Check for specific "Copyright 20xx" to rule out others
    copyright_years = re.findall(r'Copyright.*?20(1[0-9])', header, re.IGNORECASE)
    if copyright_years:
        if '16' in copyright_years:
            is_2016 = True
        else:
            # If copyright 2015 or 2017 is explicitly there, override
            is_2016 = False
            
    if is_2016:
        matches.append(title)

print('__RESULT__:')
print(json.dumps(matches))"""

env_args = {'var_function-call-2683298839036433804': ['paper_docs'], 'var_function-call-17469928963468779101': 'file_storage/function-call-17469928963468779101.json', 'var_function-call-5896966146300588964': 'file_storage/function-call-5896966146300588964.json', 'var_function-call-15408307413232285076': [], 'var_function-call-3201152881564540203': ['Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard University\nCambridge, MA, USA\neyue@college.harvard.edu\n\nABSTRACT\nSelf-tracking physiological and psychological data poses the\nchallenge of presentation and interpretation. Insightful nar-\nratives for self-', 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  condition, \naffecting  20%  of  the  population.  Even  though  it  is  a \ntreatable  condition,  people  often  do  not  seek  treatment.  In \nthis paper, we  describe how we co-designed and evaluated \nwith', 'Beyond Abandonment to Next Steps: Understanding and \nDesigning for Life after Personal Informatics Tool Use \n\nDaniel A. Epstein1, Monica Caraway2, Chuck Johnston2, \nAn Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {mcaraway, chuck2, anping, smunson}@uw.edu \n\nABSTRACT \nRecent  research  examines  how  and  why  people  abandon \nself-tracking tools. We exten', 'Beyond Behavior: The Coach’s Perspective \n on Technology in Health Coaching \n\nHeleen Rutjes \n Human-Technology Interaction \n Eindhoven University of Technology \n Eindhoven, the Netherlands \n H.Rutjes@tue.nl \n\nMartijn C. Willemsen \n Human-Technology Interaction \n Eindhoven University of Technology \n Eindhoven, the Netherlands \n M.C.Willemsen@tue.com \n\nWijnand A. IJsselsteijn  \nHuman-Technology Interaction \n Eindhoven University of Technology \n Eindhoven, the Netherlands \n W.A.IJsselsteijn@tue.com', 'Charting Design Preferences on Wellness Wearables  \n\nJuho Rantakari1, Virve Inget2, Ashley Colley1, Jonna Häkkilä1 \n\n1University of Lapland \nYliopistokatu 8 \n96400 Rovaniemi, Finland \nfirstname.lastname@ulapland.fi \n\n2Center for Ubiquitous Computing \nP.O Box 4500 \n90014 University of Oulu, Finland \nfirstname.lastname@oulu.fi \n\nABSTRACT \nThis paper presents a study on people’s preferences with wearable \nwellness  devices.  The  results  are  based  on  an  online  survey \n(n=84),  where  people  ']}

exec(code, env_args)
