code = """import json
import re

with open(locals()['var_function-call-17095788158205138574'], 'r') as f:
    papers = json.load(f)

infos = []
for p in papers:
    title = p['filename'].replace('.txt', '')
    text = p['text']
    
    # Check domain
    has_domain = 'physical activity' in text.lower()
    
    # Find year marker
    # Look for common conference patterns + year
    # Capture the year
    year_match = re.search(r"(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*(?:'|20)(\d\d)", text[:5000], re.IGNORECASE)
    year = year_match.group(1) if year_match else "Unknown"
    
    # Find Copyright year
    copy_match = re.search(r"Copyright.*?(?:19|20)(\d\d)", text[:5000], re.IGNORECASE | re.DOTALL)
    copy_year = copy_match.group(1) if copy_match else "Unknown"
    
    infos.append({
        "title": title,
        "has_domain": has_domain,
        "venue_year": year,
        "copy_year": copy_year,
        "snippet": text[:200].replace('\n', ' ')
    })

print("__RESULT__:")
print(json.dumps(infos))"""

env_args = {'var_function-call-16853199496411036361': 'file_storage/function-call-16853199496411036361.json', 'var_function-call-17095788158205138574': 'file_storage/function-call-17095788158205138574.json', 'var_function-call-7387633955592090896': 'file_storage/function-call-7387633955592090896.json', 'var_function-call-11266484425143730548': [], 'var_function-call-5358281181828038604': ['Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard Unive', 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  conditi', 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent Crocher1,3, Frank Vetere1, Suranga Nanayakkara1,4 \n1Microsoft Research Centre for SocialNUI, The Univ', 'Beyond Abandonment to Next Steps: Understanding and \nDesigning for Life after Personal Informatics Tool Use \n\nDaniel A. Epstein1, Monica Caraway2, Chuck Johnston2, \nAn Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University', 'Beyond Behavior: The Coach’s Perspective \n on Technology in Health Coaching \n\nHeleen Rutjes \n Human-Technology Interaction \n Eindhoven University of Technology \n Eindhoven, the Netherlands \n H.Rutjes@tue.nl \n\nMartijn C. Willemsen \n Human-Technology Interaction \n Eindhoven University of Technology \n '], 'var_function-call-9795341655051111948': [{'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'citation_count': 636}], 'var_function-call-1098490014859573711': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E'}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'snippet': 'Beyond Behavior: The Coach’s Perspective \n on Technology in Health Coaching \n\nHeleen Rutjes \n Human-Technology Interaction \n Eindhoven University of Technology \n Eindhoven, the Netherlands \n H.Rutjes@'}], 'var_function-call-12507445133015791911': 'file_storage/function-call-12507445133015791911.json', 'var_function-call-1001728322332553647': 5, 'var_function-call-2537074510682769091': {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'snippet': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent Crocher1,3, Frank Vetere1, Suranga Nanayakkara1,4 \n1Microsoft Research Centre for SocialNUI, The University of Melbourne, Australia \n2Queensland University of Technology, Brisbane, Australia \n3Department of Mechanical Engineering, The University of Melbourne, Australia \n4Augmented Human Lab, Singapor'}}

exec(code, env_args)
