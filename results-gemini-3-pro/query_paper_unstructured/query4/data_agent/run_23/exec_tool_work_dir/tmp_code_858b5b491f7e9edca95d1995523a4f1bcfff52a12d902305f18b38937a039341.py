code = """import json
import re

with open(locals()['var_function-call-16720471753298143428'], 'r') as f:
    citations_data = json.load(f)

with open(locals()['var_function-call-6532184733094038919'], 'r') as f:
    papers_data = json.load(f)

def normalize_title(t):
    return t.strip().lower()

citation_map = {}
for entry in citations_data:
    t = normalize_title(entry['title'])
    count = int(entry['citation_count'])
    if t not in citation_map:
        citation_map[t] = 0
    citation_map[t] += count

results = []

for paper in papers_data:
    filename = paper['filename']
    text = paper['text']
    title = filename.replace('.txt', '').strip()
    norm_title = normalize_title(title)
    
    if 'physical activity' not in text.lower():
        continue
        
    header = text[:5000]
    
    is_2016 = False
    
    if re.search(r'Copyright\s+(©\s*)?2016', header, re.IGNORECASE):
        is_2016 = True
    elif re.search(r'(CHI|UbiComp|CSCW|DIS|IUI|PervasiveHealth|OzCHI|TEI|AH)\s*[\'\u2019]16', header, re.IGNORECASE):
        is_2016 = True
    elif re.search(r'(CHI|UbiComp|CSCW|DIS|IUI|PervasiveHealth|OzCHI|TEI|AH)\s*2016', header, re.IGNORECASE):
        is_2016 = True
    elif '2016' in header and ('ACM' in header or 'IEEE' in header):
         if not re.search(r'201[7-9]', header):
             is_2016 = True

    if is_2016:
        total_citations = citation_map.get(norm_title, 0)
        results.append({
            "title": title,
            "total_citations": total_citations
        })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-5019104688225349175': 'file_storage/function-call-5019104688225349175.json', 'var_function-call-4539344191155681833': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-6532184733094038919': 'file_storage/function-call-6532184733094038919.json', 'var_function-call-16720471753298143428': 'file_storage/function-call-16720471753298143428.json', 'var_function-call-5284581737905555654': [], 'var_function-call-1171159351277879851': [{'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'header': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard Unive'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'header': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  conditi'}, {'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt', 'header': 'Beyond Abandonment to Next Steps: Understanding and \nDesigning for Life after Personal Informatics Tool Use \n\nDaniel A. Epstein1, Monica Caraway2, Chuck Johnston2, \nAn Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University'}, {'filename': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt", 'header': 'Beyond Behavior: The Coach’s Perspective \n on Technology in Health Coaching \n\nHeleen Rutjes \n Human-Technology Interaction \n Eindhoven University of Technology \n Eindhoven, the Netherlands \n H.Rutjes@tue.nl \n\nMartijn C. Willemsen \n Human-Technology Interaction \n Eindhoven University of Technology \n '}, {'filename': 'Charting Design Preferences on Wellness Wearables.txt', 'header': 'Charting Design Preferences on Wellness Wearables  \n\nJuho Rantakari1, Virve Inget2, Ashley Colley1, Jonna Häkkilä1 \n\n1University of Lapland \nYliopistokatu 8 \n96400 Rovaniemi, Finland \nfirstname.lastname@ulapland.fi \n\n2Center for Ubiquitous Computing \nP.O Box 4500 \n90014 University of Oulu, Finland \n'}]}

exec(code, env_args)
