code = """import json
import re

with open(locals()['var_function-call-5351248468420054587'], 'r') as f:
    papers = json.load(f)

titles_2016 = []

for p in papers:
    text = p.get('text', '')
    # Check first 5000 chars for metadata
    header = text[:5000] 
    
    # Check for physical activity
    # The query already filtered for it, but let's double check it's not just in the references (which would be at the end).
    # "Common domains include: 'physical activity'".
    # I'll check if "physical activity" appears in the first 5000 characters (likely abstract/intro/keywords).
    if 'physical activity' not in header.lower():
        # Maybe it is in the body? The user said "domain: ... physical activity".
        # If it's only in references, it's not the domain.
        # But for now, let's assume if it's in the text, it's relevant, but prioritize if in abstract/keywords.
        pass # If not in header, might be less relevant, but let's stick to the prompt's implied "domain" extraction.
             # I'll count it if it's anywhere in the text, but let's use the full text check I did in Mongo.
             # Wait, the Mongo query checked the WHOLE text.
             # Let's trust the Mongo query for domain for now, or refine it.
             # If I filter strictly by "physical activity" in Abstract/Keywords, I might miss some.
             # Let's stick to "is in text" but maybe filter out if ONLY in references? (Hard to detect references section reliably).
             # Let's proceed with just the date check first.

    # Year extraction
    # Patterns for 2016
    is_2016 = False
    
    # 1. Look for explicit conference headers
    if re.search(r"(?:CHI|UbiComp|Ubicomp|CSCW|DIS|IUI|OzCHI|TEI|AH|PervasiveHealth|WWW).{0,20}\b2016\b", header, re.IGNORECASE):
        is_2016 = True
    elif re.search(r"\b2016\b.{0,20}(?:CHI|UbiComp|Ubicomp|CSCW|DIS|IUI|OzCHI|TEI|AH|PervasiveHealth|WWW)", header, re.IGNORECASE):
        is_2016 = True
        
    # 2. Look for Copyright lines
    if not is_2016:
        if re.search(r"Copyright\s+(?:©|\(c\)|held by|20\d\d\s+©)?\s*2016", header, re.IGNORECASE):
            is_2016 = True
        elif re.search(r"©\s*2016", header):
            is_2016 = True
            
    # 3. Look for "Month DD-DD, 2016" or "Month, 2016"
    if not is_2016:
        if re.search(r"(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(?:–|-|—)\d{1,2},?\s+2016", header, re.IGNORECASE):
            is_2016 = True
            
    # 4. Negative check: if we found 2016, make sure it's not actually 2017/2018 paper citing 2016.
    # A paper from 2017 usually has "2017" in the copyright/conference line.
    # If "2017" or "2018" appears in the same high-value spots, we should probably discard or compare.
    
    if is_2016:
        # Check for later years in high-value spots
        if re.search(r"(?:CHI|UbiComp|Ubicomp|CSCW|DIS|IUI|OzCHI|TEI|AH|PervasiveHealth|WWW).{0,20}\b201[7-9]\b", header, re.IGNORECASE):
            is_2016 = False
        elif re.search(r"Copyright\s+(?:©|\(c\)|held by|20\d\d\s+©)?\s*201[7-9]", header, re.IGNORECASE):
            is_2016 = False
            
    if is_2016:
        titles_2016.append(p['filename'].replace('.txt', ''))

print("__RESULT__:")
print(json.dumps(titles_2016))"""

env_args = {'var_function-call-2934941311290250447': 'file_storage/function-call-2934941311290250447.json', 'var_function-call-2934941311290249234': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-5351248468420054587': 'file_storage/function-call-5351248468420054587.json', 'var_function-call-13759386154784005960': [], 'var_function-call-7878444052374706843': [{'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'header': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard University\nCambridge, MA, USA\neyue@college.harvard.edu\n\nABSTRACT\nSelf-tracking physiological and psychological data poses the\nchallenge of presentation and interpretation. Insightful nar-\nratives for self-'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'header': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  condition, \naffecting  20%  of  the  population.  Even  though  it  is  a \ntreatable  condition,  people  often  do  not  seek  treatment.  In \nthis paper, we  describe how we co-designed and evaluated \nwith'}, {'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt', 'header': 'Beyond Abandonment to Next Steps: Understanding and \nDesigning for Life after Personal Informatics Tool Use \n\nDaniel A. Epstein1, Monica Caraway2, Chuck Johnston2, \nAn Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {mcaraway, chuck2, anping, smunson}@uw.edu \n\nABSTRACT \nRecent  research  examines  how  and  why  people  abandon \nself-tracking tools. We exten'}, {'filename': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt", 'header': 'Beyond Behavior: The Coach’s Perspective \n on Technology in Health Coaching \n\nHeleen Rutjes \n Human-Technology Interaction \n Eindhoven University of Technology \n Eindhoven, the Netherlands \n H.Rutjes@tue.nl \n\nMartijn C. Willemsen \n Human-Technology Interaction \n Eindhoven University of Technology \n Eindhoven, the Netherlands \n M.C.Willemsen@tue.com \n\nWijnand A. IJsselsteijn  \nHuman-Technology Interaction \n Eindhoven University of Technology \n Eindhoven, the Netherlands \n W.A.IJsselsteijn@tue.com'}, {'filename': 'Charting Design Preferences on Wellness Wearables.txt', 'header': 'Charting Design Preferences on Wellness Wearables  \n\nJuho Rantakari1, Virve Inget2, Ashley Colley1, Jonna Häkkilä1 \n\n1University of Lapland \nYliopistokatu 8 \n96400 Rovaniemi, Finland \nfirstname.lastname@ulapland.fi \n\n2Center for Ubiquitous Computing \nP.O Box 4500 \n90014 University of Oulu, Finland \nfirstname.lastname@oulu.fi \n\nABSTRACT \nThis paper presents a study on people’s preferences with wearable \nwellness  devices.  The  results  are  based  on  an  online  survey \n(n=84),  where  people  '}]}

exec(code, env_args)
