code = """import json
import re

# Load citations data
path_citations = locals().get('var_function-call-7498192109235549923')
with open(path_citations, 'r') as f:
    citations_data = json.load(f)
citation_map = {c['title']: int(c['citation_count']) for c in citations_data}
cited_titles = set(citation_map.keys())

# Load paper docs
path_docs = locals().get('var_function-call-7995451070674360072')
with open(path_docs, 'r') as f:
    docs = json.load(f)

chi_citations = 0
chi_papers = []

for doc in docs:
    fname = doc['filename']
    title = fname.replace('.txt', '')
    
    if title in cited_titles:
        text = doc['text']
        head = text[:5000]
        
        is_chi = False
        # Regex patterns
        # 1. "CHI 'XX" or "CHI'XX" or "CHI 20XX"
        # \bCHI matches start of CHI.
        # \s* matches optional space.
        # '? matches optional apostrophe.
        # \d{2} matches 2 digits.
        # \b ensures we end at word boundary (e.g. not CHI 150).
        # But '15 is not a word boundary if followed by space.
        # regex: \bCHI\s*'?\d{2}
        # Be careful with "CHI 15" matching "CHI 150".
        # So \d{2}(?!\d).
        
        if re.search(r"\bCHI\s*'?\d{2}\b", head):
             is_chi = True
        elif re.search(r"\bCHI\s+20\d{2}\b", head):
             is_chi = True
        elif "Conference on Human Factors in Computing Systems" in head:
             is_chi = True
        
        if is_chi:
            chi_citations += citation_map[title]
            chi_papers.append(title)

print(f"Identified {len(chi_papers)} CHI papers.")
print(f"Total citation count: {chi_citations}")
print("__RESULT__:")
print(json.dumps(chi_citations))"""

env_args = {'var_function-call-7498192109235549923': 'file_storage/function-call-7498192109235549923.json', 'var_function-call-1495859486444725251': 'file_storage/function-call-1495859486444725251.json', 'var_function-call-6405304347776267640': 188, 'var_function-call-15965521281973898392': 'file_storage/function-call-15965521281973898392.json', 'var_function-call-6154840779900112772': 'file_storage/function-call-6154840779900112772.json', 'var_function-call-4693824508147823644': 'file_storage/function-call-4693824508147823644.json', 'var_function-call-9895404596539580614': 16, 'var_function-call-7995451070674360072': 'file_storage/function-call-7995451070674360072.json', 'var_function-call-5270707642555143575': 0, 'var_function-call-15852451279442860116': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'header': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.wash"}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'header': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard Unive'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'header': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  conditi'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'header': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent Crocher1,3, Frank Vetere1, Suranga Nanayakkara1,4 \n1Microsoft Research Centre for SocialNUI, The Univ'}, {'filename': 'Barriers to Engagement with a Personal Informatics Productivity Tool.txt', 'header': ' Barriers to Engagement with a Personal Informatics \nProductivity Tool \nJon Bird \nCity University London \nSchool of Engineering & \nMathematical Sciences \nLondon, EC1V 0HB \nJon.bird@city.ac.uk \n\nCassie Cornish-Tresstail \nUCL Interaction Centre \nGower Street \nLondon, W1CE 6BT \ncassandra.cornish-\ntrest'}, {'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt', 'header': 'Beyond Abandonment to Next Steps: Understanding and \nDesigning for Life after Personal Informatics Tool Use \n\nDaniel A. Epstein1, Monica Caraway2, Chuck Johnston2, \nAn Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University'}, {'filename': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt", 'header': 'Beyond Behavior: The Coach’s Perspective \n on Technology in Health Coaching \n\nHeleen Rutjes \n Human-Technology Interaction \n Eindhoven University of Technology \n Eindhoven, the Netherlands \n H.Rutjes@tue.nl \n\nMartijn C. Willemsen \n Human-Technology Interaction \n Eindhoven University of Technology \n '}, {'filename': 'Charting Design Preferences on Wellness Wearables.txt', 'header': 'Charting Design Preferences on Wellness Wearables  \n\nJuho Rantakari1, Virve Inget2, Ashley Colley1, Jonna Häkkilä1 \n\n1University of Lapland \nYliopistokatu 8 \n96400 Rovaniemi, Finland \nfirstname.lastname@ulapland.fi \n\n2Center for Ubiquitous Computing \nP.O Box 4500 \n90014 University of Oulu, Finland \n'}, {'filename': 'ClimbSense: Automatic Climbing Route Recognition Using Wrist-worn Inertia Measurement Units.txt', 'header': 'ClimbSense - Automatic Climbing Route Recognition using\nWrist-worn Inertia Measurement Units\nFlorian Daiber\nGerman Research Center for\nArtiﬁcial Intelligence (DFKI)\nLancaster University\nﬂorian.daiber@dfki.de\n\nAntonio Kr ¨uger\nGerman Research Center for\nArtiﬁcial Intelligence (DFKI)\nkrueger@dfki.de\n\n'}, {'filename': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt", 'header': 'Closing the Gap: Supporting Patients’ Transition  \nto Self-Management after Hospitalization \n Ari H Pollack1,2, Uba Backonja4, Andrew D. Miller4, Sonali R. Mishra3, Maher Khelifi4,  \nLogan Kendall4, and Wanda Pratt3 \n2Division of Nephrology \nSeattle Children’s Hospital \nSeattle, WA, USA \n\n3The Infor'}], 'var_function-call-17919579643270498158': "Beyond Abandonment to Next Steps: Understanding and \nDesigning for Life after Personal Informatics Tool Use \n\nDaniel A. Epstein1, Monica Caraway2, Chuck Johnston2, \nAn Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {mcaraway, chuck2, anping, smunson}@uw.edu \n\nABSTRACT \nRecent  research  examines  how  and  why  people  abandon \nself-tracking tools. We extend this work with new insights \ndrawn from people reflecting on their experiences after they \nstop tracking, examining how designs continue to influence \npeople  even  after  abandonment.  We  further  contrast  prior \nwork  considering  abandonment  of  health  and  wellness \ntracking  tools  with  an  exploration  of  why  people  abandon \nfinancial  and  location  tracking  tools,  and  we  connect  our \nfindings  to  models  of  personal  informatics.  Surveying  193 \npeople and interviewing 12 people, we identify six reasons \nwhy people stop tracking and five perspectives on life after \ntracking.  We  discuss  these  results  and  opportunities  for \ndesign to consider life after self-tracking. \n\nAuthor Keywords \nPersonal informatics; self-tracking; abandonment. \n\nACM Classification Keywords \nH.5.m. Information interfaces and presentation (e.g., HCI). \n\nINTRODUCTION \nPersonal informatics is defined as the process of collecting \nand  reflecting  on  personal  information  [12],  and  is  now  a \ncommon practice in the lives of many people [7]. However, \npeople over time come to temporarily lapse or permanently \ndiscontinue self-tracking [4,5,6,11]. We study abandonment \nof self-tracking tools to gain insight into how to design tools \nthat: (1) better align with tracking objectives and practices, \nand (2) support better abandonment experiences. \n\nThis  paper  extends  current  understanding  of  abandonment \nwith  insights  drawn  from  people  reflecting  on  their \nexperiences after they stopped self-tracking. As part of this, \nwe  examine  how  designs  can  continue  to  influence  people \neven  after  abandonment.  We  extend  recent  work  examining \nself-tracking technology abandonment in health and wellness \n[4,5,11]  by  contrasting  it  with  abandonment  in  other \nself-tracking domains, specifically finance and location. We \n\nPermission  to  make  digital  or  hard  copies  of  all  or  part  of  this  work  for\npersonal or classroom use is granted without fee provided that copies are\nnot made or distributed for profit or commercial advantage and that copies\nbear  this  notice  and  the  full  citation  on  the  first  page.  Copyrights  for\ncomponents  of  this  work  owned  by  others  than  ACM  must  be  honored.\nAbstracting  with  credit  is  permitted.  To  copy  otherwise,  or  republish,  to\npost on servers or to redistribute to lists, requires prior specific permission\nand/or a fee. Request permissions from Permissions@acm.org. \nCHI'", 'var_function-call-5715942308764845845': 1532, 'var_function-call-7268487113225898502': 308}

exec(code, env_args)
