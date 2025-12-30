code = """import json
import re

citations_file = locals()['var_function-call-8931525846963248243']
with open(citations_file, 'r') as f:
    citations = json.load(f)

papers_file = locals()['var_function-call-4192422070354728246']
with open(papers_file, 'r') as f:
    papers = json.load(f)

citation_map = {}
for c in citations:
    try:
        count = int(c['citation_count'])
    except:
        count = 0
    # Store by title
    citation_map[c['title']] = count

total_citations = 0
chi_papers = []

for p in papers:
    if not p['filename'].endswith('.txt'):
        continue
    title = p['filename'][:-4]
    
    if title in citation_map:
        text = p['text']
        # Check first 5000 chars
        header = text[:5000]
        
        is_chi = False
        
        # 1. Full name
        if "Conference on Human Factors in Computing Systems" in header:
            is_chi = True
            
        # 2. CHI followed by year or 'Conference'
        # Regex: CHI followed by space/newline, then (digit or ' or "Conference")
        # \bCHI matches CHI word.
        # \s+ matches one or more whitespace (including newline).
        # (?: ... ) group.
        # [\d'] matches digit or apostrophe.
        # | Conference matches "Conference".
        elif re.search(r"\bCHI\s+(?:[\d']|Conference)", header):
            is_chi = True
            
        # 3. "Proceedings of the ... CHI"
        elif "Proceedings of the CHI" in header or "Proceedings of the ... CHI" in header: # unlikely literal "..."
            is_chi = True # Simplify

        # 4. Just "CHI 20xx" or "CHI 'xx" without \b if at start?
        # But \b should work.
        
        # Let's also check for "CHI" appearing in the first 100 characters in a standalone way?
        # e.g. "CHI 2018"
        
        if is_chi:
            total_citations += citation_map[title]
            chi_papers.append(title)

print("__RESULT__:")
print(json.dumps({"total_citations": total_citations, "chi_paper_count": len(chi_papers), "sample_chi_papers": chi_papers[:10]}))"""

env_args = {'var_function-call-8931525846963248243': 'file_storage/function-call-8931525846963248243.json', 'var_function-call-17301308444494823963': {'count': 188, 'filenames': ['Exploring the Value of Parent Tracked Baby Data in Interactions with Healthcare Professionals: A Data-Enabled Design Exploration.txt', 'SweatAtoms: Materializing Physical Activity.txt', 'Designing a Wellness Self-management Tool for Older Adults: Results from a Field Trial of YourWellness.txt', 'Personal Informatics for Sport: Meaning, Body, and Social Relations in Amateur and Elite Athletes.txt', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media.txt', 'Crafting a View of Self-Tracking Data in the Clinical Visit.txt', 'Social (Media) Jet Lag: How Usage of Social Technology Can Modulate and Reflect Circadian Rhythms.txt', 'Data, Data Everywhere, and Still Too Hard to Link: Insights from User Interactions with Diabetes Apps.txt', 'Sensor Requirements for Activity Recognition on Smart Watches.txt', 'Health Multimedia: Lifestyle Recommendations Based on Diverse Observations.txt']}, 'var_function-call-6838254019764142939': 'file_storage/function-call-6838254019764142939.json', 'var_function-call-4192422070354728246': 'file_storage/function-call-4192422070354728246.json', 'var_function-call-8855315205875236819': {'total_citations': 0, 'chi_paper_count': 0, 'sample_chi_papers': []}, 'var_function-call-13924674519054514697': [{'title': 'A Lived Informatics Model of Personal Informatics', 'header': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.wash"}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'header': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard Unive'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'header': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  conditi'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'header': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent Crocher1,3, Frank Vetere1, Suranga Nanayakkara1,4 \n1Microsoft Research Centre for SocialNUI, The Univ'}], 'var_function-call-15470796217763327864': {'total_citations': 16, 'chi_paper_count': 1, 'sample_chi_papers': ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App']}, 'var_function-call-1169271034824662916': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'snippet': 'CHI 2018, April 21–2'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'snippet': 'CHI \nConference on H'}]}

exec(code, env_args)
