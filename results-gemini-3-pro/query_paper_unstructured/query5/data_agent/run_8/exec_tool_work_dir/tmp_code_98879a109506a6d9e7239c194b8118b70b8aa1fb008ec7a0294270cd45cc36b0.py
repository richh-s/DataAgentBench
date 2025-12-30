code = """import json
import re

with open(locals()['var_function-call-4961661729464848456'], 'r') as f:
    citations = json.load(f)
citation_map = {c['title']: int(c['citation_count']) for c in citations}

with open(locals()['var_function-call-14263536467630025147'], 'r') as f:
    papers = json.load(f)

chi_papers = []
total_citations = 0

for paper in papers:
    title = paper.get('filename', '')[:-4]
    if title not in citation_map:
        continue
        
    text = paper.get('text', '')
    
    # Locate permission block
    perm_match = re.search(r"Permission to make digital or hard copies", text, re.IGNORECASE)
    if perm_match:
        start = perm_match.start()
        # Look at the block and slightly after (where venue usually is)
        # 1000 chars should cover the copyright notice
        snippet = text[start:start+1000]
    else:
        # Fallback to header
        snippet = text[:2000]
        
    # Check for CHI
    # Patterns: CHI 'XX, CHI 20XX, Human Factors in Computing Systems
    is_chi = False
    if re.search(r"Conference on Human Factors in Computing Systems", snippet, re.IGNORECASE):
        is_chi = True
    elif re.search(r"\bCHI\s*['’]?\s*(?:20)?\d{2}", snippet):
        is_chi = True
        
    # Check for negation (other venues) if CHI was found? 
    # Or just if other venues are found, check if they are the primary one?
    # If "UbiComp" is in the snippet, it's likely UbiComp.
    # But what if "CHI" is also mentioned?
    # Usually the venue name appears prominently.
    # Let's count matches?
    # If "UbiComp" appears, it's NOT CHI. (Unless it's "Presented at CHI, extended to UbiComp"? No.)
    
    if re.search(r"UbiComp", snippet, re.IGNORECASE):
        is_chi = False
    if re.search(r"CSCW", snippet): # Case sensitive usually
        is_chi = False
    if re.search(r"\bDIS\s*['’]?\s*\d", snippet): # DIS '14
        is_chi = False
    # ... add others if needed, but CHI/UbiComp/CSCW are the main ones in this domain.
    
    if is_chi:
        chi_papers.append(title)
        total_citations += citation_map[title]

print(f"Identified {len(chi_papers)} CHI papers.")
print(f"Total citations: {total_citations}")
print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_function-call-4961661729464848456': 'file_storage/function-call-4961661729464848456.json', 'var_function-call-4306319526809017372': 188, 'var_function-call-9160616424066584020': 'file_storage/function-call-9160616424066584020.json', 'var_function-call-16237189493323066997': 5, 'var_function-call-14263536467630025147': 'file_storage/function-call-14263536467630025147.json', 'var_function-call-95742628409748684': 1551, 'var_function-call-6733428787577609903': 16, 'var_function-call-17501030019706782583': {'total': 16, 'papers': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'count': 16}]}, 'var_function-call-5225444022116205832': [], 'var_function-call-14680094483701822161': [{'title': 'A Lived Informatics Model of Personal Informatics', 'match': 'CHI Year'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'match': 'CHI Year'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'match': 'Full Name'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'match': 'Full Name'}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'match': 'Full Name'}], 'var_function-call-7239758174783740011': [{'title': 'A Lived Informatics Model of Personal Informatics', 'header': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN  A Lived Informatics Model of Personal Informatics  "}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'header': 'Fengjiao Peng MIT Media Lab Cambridge, MA, USA fpeng@mit.edu  A Trip to the Moon: Personalized Anima'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'header': 'A Wee Bit More Interaction: Designing and Evaluating   an Overactive Bladder App  Ana-Maria Salai   '}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'header': 'ArmSleeve: a Patient Monitoring System to Support  Occupational Therapists in Stroke Rehabilitation '}, {'title': 'Barriers to Engagement with a Personal Informatics Productivity Tool', 'header': ' Barriers to Engagement with a Personal Informatics  Productivity Tool  Jon Bird  City University Lo'}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'header': 'Beyond Abandonment to Next Steps: Understanding and  Designing for Life after Personal Informatics T'}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'header': 'Beyond Behavior: The Coach’s Perspective   on Technology in Health Coaching   Heleen Rutjes   Human-'}, {'title': 'Charting Design Preferences on Wellness Wearables', 'header': 'Charting Design Preferences on Wellness Wearables    Juho Rantakari1, Virve Inget2, Ashley Colley1, '}, {'title': 'ClimbSense: Automatic Climbing Route Recognition Using Wrist-worn Inertia Measurement Units', 'header': 'ClimbSense - Automatic Climbing Route Recognition using Wrist-worn Inertia Measurement Units Florian'}, {'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'header': 'Closing the Gap: Supporting Patients’ Transition   to Self-Management after Hospitalization   Ari H '}], 'var_function-call-4365208543066403133': 1893, 'var_function-call-16377022919636549182': 61, 'var_function-call-2847063484787585829': {'sundroid_header': 'Sundroid: Solar Radiation Awareness with Smartphones∗  Thomas Fahrni, Michael Kuhn, Philipp Sommer, Roger Wattenhofer, and Samuel Welten Computer Engineering and Networks Laboratory ETH Zurich, Switzerland ﬁrstname.lastname@tik.ee.ethz.ch  ABSTRACT While the sun is important for our health, overexpo', 'chi_papers': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'count': 16}, {'title': 'Patient Perspectives on Self-Management Technologies for Chronic Fatigue Syndrome', 'count': 43}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', 'count': 2}], 'total': 61}, 'var_function-call-1886946324018678199': 'Done', 'var_function-call-4292012880260422153': {'snippet': 'Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for proﬁt or commercial advantage and that copies bear this notice and the full citation on the ﬁrst page. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior speciﬁc permission and/or a fee. UbiComp’11, September 17–21, 2011, Beijing, China. Copyright 2011 ACM 978-1-4503-0630-0/11/0', 'chi_indices': [47792, 48417, 48668, 49229], 'total_chi': 4}}

exec(code, env_args)
