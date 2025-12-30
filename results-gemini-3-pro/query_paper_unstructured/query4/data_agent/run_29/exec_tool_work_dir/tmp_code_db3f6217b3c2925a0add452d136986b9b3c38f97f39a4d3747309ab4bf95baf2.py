code = """import json
import re

with open(locals()['var_function-call-4420579621073480200'], 'r') as f:
    papers = json.load(f)

with open(locals()['var_function-call-4736821834278124027'], 'r') as f:
    citations = json.load(f)

citation_map = {}
for cit in citations:
    title = cit['title']
    try:
        count = int(cit['citation_count'])
    except:
        count = 0
    if title not in citation_map:
        citation_map[title] = 0
    citation_map[title] += count

results = []
year_regex = re.compile(r"(Copyright\s+(©\s*)?2016)|(©\s*2016)|((CHI|UbiComp|CSCW|DIS|IUI|TEI|PervasiveHealth|WWW|OzCHI|AH)\s*('16|2016))|(September\s+\d+\S*\d*,\s+2016)|(2016\s+ACM)", re.IGNORECASE)

# Additional negative check for other years to avoid false positives from references
# But usually publication year appears in headers/footers in a specific way.
# Let's rely on the positive matches first.

debug_matches = []

for p in papers:
    text = p.get('text', '')
    # Check domain again
    if 'physical activity' not in text.lower():
        continue
        
    # Check Year
    # We search the first 5000 chars which likely cover the first page and headers/footers
    header_text = text[:5000] 
    
    if year_regex.search(header_text):
        # Found 2016 marker
        filename = p['filename']
        if filename.endswith('.txt'):
            title = filename[:-4]
        else:
            title = filename
            
        count = citation_map.get(title, 0)
        results.append({"title": title, "total_citation_count": count})
        debug_matches.append(title)

# Sort
results.sort(key=lambda x: x['title'])

print("Found papers:", len(results))
print("Sample titles:", debug_matches[:5])
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-524279506149407119': ['paper_docs'], 'var_function-call-524279506149405588': 'file_storage/function-call-524279506149405588.json', 'var_function-call-524279506149408153': ['Citations', 'sqlite_sequence'], 'var_function-call-524279506149406622': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-9551284447428774224': [{'count(*)': '1405'}], 'var_function-call-9551284447428775563': 'file_storage/function-call-9551284447428775563.json', 'var_function-call-4736821834278124027': 'file_storage/function-call-4736821834278124027.json', 'var_function-call-1276767600603300389': [], 'var_function-call-8853061178265091948': 'debug_done', 'var_function-call-17995316611090094079': {'total_papers': 5, 'total_citations': 1405, 'pa_count': 4, 'year_2016_count': 0, 'match_count': 0, 'sample_matches': [], 'sample_citation_titles': ['Shifting Dynamics or Breaking Sacred Traditions?: The Role of Technology in Twelve-step Fellowships', 'How to Drive a London Bus: Measuring Performance in a Mobile and Remote Workplace', 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis', 'Rotating Online Behavior Change Interventions Increases Effectiveness But Also Increases Attrition'], 'test_title_in_citations': False}, 'var_function-call-4420579621073480200': 'file_storage/function-call-4420579621073480200.json', 'var_function-call-4810167469021822824': [], 'var_function-call-5660181614940294609': [{'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'header_snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard University\nCambridge, MA, USA\neyue@college.harvard.edu\n\nABSTRACT\nSelf-tracking physiological and psychological data poses the\nchallenge of presentation and interpretation. Insightful nar-\nratives for self-'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'header_snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  condition, \naffecting  20%  of  the  population.  Even  though  it  is  a \ntreatable  condition,  people  often  do  not  seek  treatment.  In \nthis paper, we  describe how we co-designed and evaluated \nwith'}, {'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt', 'header_snippet': 'Beyond Abandonment to Next Steps: Understanding and \nDesigning for Life after Personal Informatics Tool Use \n\nDaniel A. Epstein1, Monica Caraway2, Chuck Johnston2, \nAn Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {mcaraway, chuck2, anping, smunson}@uw.edu \n\nABSTRACT \nRecent  research  examines  how  and  why  people  abandon \nself-tracking tools. We exten'}, {'filename': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt", 'header_snippet': 'Beyond Behavior: The Coach’s Perspective \n on Technology in Health Coaching \n\nHeleen Rutjes \n Human-Technology Interaction \n Eindhoven University of Technology \n Eindhoven, the Netherlands \n H.Rutjes@tue.nl \n\nMartijn C. Willemsen \n Human-Technology Interaction \n Eindhoven University of Technology \n Eindhoven, the Netherlands \n M.C.Willemsen@tue.com \n\nWijnand A. IJsselsteijn  \nHuman-Technology Interaction \n Eindhoven University of Technology \n Eindhoven, the Netherlands \n W.A.IJsselsteijn@tue.com'}, {'filename': 'Charting Design Preferences on Wellness Wearables.txt', 'header_snippet': 'Charting Design Preferences on Wellness Wearables  \n\nJuho Rantakari1, Virve Inget2, Ashley Colley1, Jonna Häkkilä1 \n\n1University of Lapland \nYliopistokatu 8 \n96400 Rovaniemi, Finland \nfirstname.lastname@ulapland.fi \n\n2Center for Ubiquitous Computing \nP.O Box 4500 \n90014 University of Oulu, Finland \nfirstname.lastname@oulu.fi \n\nABSTRACT \nThis paper presents a study on people’s preferences with wearable \nwellness  devices.  The  results  are  based  on  an  online  survey \n(n=84),  where  people  '}]}

exec(code, env_args)
