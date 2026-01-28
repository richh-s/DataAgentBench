code = """import json
import re

citations_file = locals()['var_function-call-31182004423683262']
papers_file = locals()['var_function-call-113400827574739216']

with open(citations_file, 'r') as f:
    citations = json.load(f)

with open(papers_file, 'r') as f:
    papers = json.load(f)

chi_titles = set()
chi_patterns = [
    r"CHI\s+'\d{2}",          # CHI '15
    r"CHI\s+20\d{2}",        # CHI 2015
    r"Conference on Human Factors in Computing Systems",
    r"CHI Conference"
]

for p in papers:
    text = p.get('text', '')
    if not text:
        continue
    
    # Check first 5000 characters
    header = text[:5000]
    
    is_chi = False
    for pattern in chi_patterns:
        if re.search(pattern, header, re.IGNORECASE):
            is_chi = True
            break
            
    if is_chi:
        title = p['filename'].replace('.txt', '')
        chi_titles.add(title)

total_citations = 0
for c in citations:
    if c['title'] in chi_titles:
        total_citations += int(c['citation_count'])

print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_function-call-31182004423683262': 'file_storage/function-call-31182004423683262.json', 'var_function-call-31182004423683057': 'file_storage/function-call-31182004423683057.json', 'var_function-call-15517411522846928457': 'file_storage/function-call-15517411522846928457.json', 'var_function-call-12736721488613794591': 0, 'var_function-call-15094498137369451799': 'debug_done', 'var_function-call-4553672010578709336': ['Loaded 188 citations and 5 papers.', 'Sample Citations Titles:', 'Sundroid: Solar Radiation Awareness with Smartphones', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'Why We Use and Abandon Smart Devices', 'Sample Paper Headers:', 'Filename: A Lived Informatics Model of Personal Informatics.txt', 'Header: "UBICOMP \'15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\\n\\nA Lived Informatics Model of Personal Informatics \\n\\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \\n1Computer Science & Engineering, 2Hu"', 'Filename: A Stage-based Model of Personal Informatics Systems.txt', "Header: 'A Stage-Based Model of Personal Informatics Systems \\nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \\n1Human Computer Interaction Institute, 2School of Design \\nCarnegie Mellon University, Pittsburgh, PA 152'", 'Filename: A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', "Header: 'Fengjiao Peng\\nMIT Media Lab\\nCambridge, MA, USA\\nfpeng@mit.edu\\n\\nA Trip to the Moon: Personalized Animated Movies for\\nSelf-reﬂection\\nVeronica Crista LaBelle\\nMIT\\nCambridge, MA, USA\\nvlabelle@mit.edu\\nRosali'", 'Filename: A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', "Header: 'A Wee Bit More Interaction: Designing and Evaluating  \\nan Overactive Bladder App\\n\\nAna-Maria Salai \\n Heriot-Watt University \\n Edinburgh, UK \\n as152@hw.ac.uk \\n\\nLynne Baillie \\n Heriot-Watt University \\n E'", 'Filename: ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', "Header: 'ArmSleeve: a Patient Monitoring System to Support \\nOccupational Therapists in Stroke Rehabilitation \\nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \\nVincent C'", "Total papers with 'CHI' in first 500 chars: 0"], 'var_function-call-15358249879816549186': 'file_storage/function-call-15358249879816549186.json', 'var_function-call-113400827574739216': 'file_storage/function-call-113400827574739216.json'}

exec(code, env_args)
