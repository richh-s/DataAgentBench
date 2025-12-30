code = """import json
import re

citations_file = locals()['var_function-call-8931525846963248243']
with open(citations_file, 'r') as f:
    citations = json.load(f)

papers_file = locals()['var_function-call-4192422070354728246']
with open(papers_file, 'r') as f:
    papers = json.load(f)

citation_map = {c['title']: c['citation_count'] for c in citations}

total_citations = 0
chi_papers = []

for p in papers:
    if not p['filename'].endswith('.txt'):
        continue
    title = p['filename'][:-4]
    
    if title in citation_map:
        text = p['text']
        # Check first 5000 characters (roughly first page)
        search_area = text[:5000]
        
        # Regex for CHI year: CHI '14, CHI 2014, CHI 2015, CHI '15, etc.
        # \bCHI\b to ensure it's the word CHI.
        # Followed by space, optional ', and 2 or 4 digits.
        if re.search(r"\bCHI\s*['\u2019]?\d{2,4}\b", search_area, re.IGNORECASE):
            is_chi = True
        elif "Conference on Human Factors in Computing Systems" in search_area:
            is_chi = True
        elif "CHI Conference" in search_area:
            is_chi = True
        else:
            is_chi = False
            
        # Specific check for Ubicomp to exclude if both appear (unlikely but possible in references?)
        # But references are usually at the end. First 5000 chars should be safe.
        # However, sometimes "presented at CHI" might be in the text.
        # The header usually has the venue.
        
        if is_chi:
            # Double check it's not another venue?
            # e.g. "Previous work at CHI..." might appear in Intro.
            # But usually the copyright block or header is distinctive.
            # The copyright block usually says "Permission to make ... CHI 'XX..."
            
            # Let's count it.
            total_citations += citation_map[title]
            chi_papers.append(title)

print("__RESULT__:")
print(json.dumps({"total_citations": total_citations, "chi_paper_count": len(chi_papers), "sample_chi_papers": chi_papers[:10]}))"""

env_args = {'var_function-call-8931525846963248243': 'file_storage/function-call-8931525846963248243.json', 'var_function-call-17301308444494823963': {'count': 188, 'filenames': ['Exploring the Value of Parent Tracked Baby Data in Interactions with Healthcare Professionals: A Data-Enabled Design Exploration.txt', 'SweatAtoms: Materializing Physical Activity.txt', 'Designing a Wellness Self-management Tool for Older Adults: Results from a Field Trial of YourWellness.txt', 'Personal Informatics for Sport: Meaning, Body, and Social Relations in Amateur and Elite Athletes.txt', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media.txt', 'Crafting a View of Self-Tracking Data in the Clinical Visit.txt', 'Social (Media) Jet Lag: How Usage of Social Technology Can Modulate and Reflect Circadian Rhythms.txt', 'Data, Data Everywhere, and Still Too Hard to Link: Insights from User Interactions with Diabetes Apps.txt', 'Sensor Requirements for Activity Recognition on Smart Watches.txt', 'Health Multimedia: Lifestyle Recommendations Based on Diverse Observations.txt']}, 'var_function-call-6838254019764142939': 'file_storage/function-call-6838254019764142939.json', 'var_function-call-4192422070354728246': 'file_storage/function-call-4192422070354728246.json', 'var_function-call-8855315205875236819': {'total_citations': 0, 'chi_paper_count': 0, 'sample_chi_papers': []}, 'var_function-call-13924674519054514697': [{'title': 'A Lived Informatics Model of Personal Informatics', 'header': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.wash"}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'header': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard Unive'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'header': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  conditi'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'header': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent Crocher1,3, Frank Vetere1, Suranga Nanayakkara1,4 \n1Microsoft Research Centre for SocialNUI, The Univ'}]}

exec(code, env_args)
