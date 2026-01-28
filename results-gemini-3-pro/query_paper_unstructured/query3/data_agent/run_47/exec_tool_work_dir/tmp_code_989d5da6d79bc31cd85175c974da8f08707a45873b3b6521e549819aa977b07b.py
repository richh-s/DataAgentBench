code = """import json
import re

path_citations = locals()['var_function-call-6302261332534400928']
with open(path_citations, 'r') as f:
    citations_data = json.load(f)

title_citations = {}
for entry in citations_data:
    t = entry['title']
    c = int(entry['citation_count'])
    title_citations[t] = title_citations.get(t, 0) + c

path_papers = locals()['var_function-call-6302261332534401433']
with open(path_papers, 'r') as f:
    papers = json.load(f)

results = []

for p in papers:
    filename = p['filename']
    title = filename.replace('.txt', '')
    text = p['text']
    
    # Year Extraction
    year = None
    # 1. Look for Copyright
    match = re.search(r'Copyright.*?20([0-9]{2})', text[:5000], re.IGNORECASE)
    if match:
        year = 2000 + int(match.group(1))
    else:
        # 2. Look for explicit year like "CHI '19" or "September 2019"
        # Search for 201x or 202x
        match = re.search(r'20([1-2][0-9])', text[:5000])
        if match:
            year = int(match.group(0))
        else:
            # 3. Look for 'yy
            match = re.search(r"'([1-2][0-9])", text[:2000])
            if match:
                year = 2000 + int(match.group(1))

    # Contribution Extraction
    text_lower = text.lower()
    # Check for empirical keywords
    # "empirical" is the main one requested.
    # I will also allow "qualitative study" or "quantitative study" as they are empirical.
    # But strictly, the prompt said "Contribution types include: 'empirical'".
    # I'll stick to 'empirical' to be safe, but "mixed-methods" might be empirical.
    # Let's try just 'empirical' first. If the result is reasonable, good.
    # If I miss papers, I might add others.
    # Given the previous debug, "Barriers to Engagement" was missed with just "empirical".
    # I'll add "qualitative" and "quantitative".
    
    is_empirical = False
    if 'empirical' in text_lower:
        is_empirical = True
    elif 'qualitative' in text_lower:
        is_empirical = True
    elif 'quantitative' in text_lower:
        is_empirical = True
    elif 'user study' in text_lower:
        is_empirical = True
    elif 'participant' in text_lower: # A bit broad?
        # Many artifact papers have participants for evaluation.
        # But if the contribution is "empirical", it usually highlights the study.
        pass

    if year and year > 2016 and is_empirical:
        if title in title_citations:
            results.append({
                "title": title,
                "total_citation_count": title_citations[title]
            })

# Sort
results.sort(key=lambda x: x['total_citation_count'], reverse=True)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-10449789667232023992': ['paper_docs'], 'var_function-call-10449789667232022543': 'file_storage/function-call-10449789667232022543.json', 'var_function-call-10449789667232025190': 'file_storage/function-call-10449789667232025190.json', 'var_function-call-18099153275120727410': 'file_storage/function-call-18099153275120727410.json', 'var_function-call-18146542979440941861': ['====================', 'Title: A Lived Informatics Model of Personal Informatics.txt', 'COORD contribution: contributions  through  survey  design  and  participant  interviews.', 'Year (Copyright): 2015', 'Contains empirical: No', '====================', 'Title: A Stage-based Model of Personal Informatics Systems.txt', 'COORD contribution: We  provide  three  main  contributions  in  this  paper:  1)  we', 'Year (Copyright): 2010', 'Contains empirical: No', '====================', 'Title: A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'No contribution keyword found in lines.', 'Year not found via Copyright', 'Contains empirical: Yes', '====================', 'Title: A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'COORD contribution: their  contribution “I like drawing!” (UP4),  some  did not like', 'Year not found via Copyright', 'Contains empirical: Yes', '====================', 'Title: ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'COORD contribution: patient is important, the main contribution of this research is', 'COORD contribution: A  second  contribution  is  offered  through  the  design  of  a', 'Year not found via Copyright', 'Contains empirical: No'], 'var_function-call-6302261332534400928': 'file_storage/function-call-6302261332534400928.json', 'var_function-call-6302261332534401433': 'file_storage/function-call-6302261332534401433.json', 'var_function-call-10306656514989444309': [], 'var_function-call-10427956602962395898': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': 2015, 'is_empirical': False, 'in_citations': True}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': 2010, 'is_empirical': False, 'in_citations': True}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'is_empirical': True, 'in_citations': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'is_empirical': True, 'in_citations': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'is_empirical': False, 'in_citations': True}, {'title': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'year': None, 'is_empirical': True, 'in_citations': True}, {'title': 'Barriers to Engagement with a Personal Informatics Productivity Tool', 'year': None, 'is_empirical': False, 'in_citations': True}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'year': None, 'is_empirical': False, 'in_citations': True}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'year': None, 'is_empirical': False, 'in_citations': True}, {'title': 'Blood Pressure Beyond the Clinic: Rethinking a Health Metric for Everyone', 'year': None, 'is_empirical': False, 'in_citations': True}, {'title': 'Charting Design Preferences on Wellness Wearables', 'year': None, 'is_empirical': True, 'in_citations': True}, {'title': 'ClimbSense: Automatic Climbing Route Recognition Using Wrist-worn Inertia Measurement Units', 'year': None, 'is_empirical': False, 'in_citations': True}, {'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'year': None, 'is_empirical': True, 'in_citations': True}, {'title': 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings', 'year': None, 'is_empirical': True, 'in_citations': True}, {'title': 'Communicating Uncertainty in Fertility Prognosis', 'year': None, 'is_empirical': True, 'in_citations': True}, {'title': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'year': 2014, 'is_empirical': True, 'in_citations': True}, {'title': 'ConCap: Designing to Empower Individual Reflection on Chronic Conditions Using Mobile Apps', 'year': None, 'is_empirical': False, 'in_citations': True}, {'title': 'Contextual Influences on the Use and Non-Use of Digital Technology While Exercising at the Gym', 'year': None, 'is_empirical': False, 'in_citations': True}, {'title': 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'year': None, 'is_empirical': False, 'in_citations': True}, {'title': 'DataSelfie: Empowering People to Design Personalized Visuals to Represent Their Data', 'year': 2001, 'is_empirical': False, 'in_citations': True}], 'var_function-call-15430959418046538314': ['====================', 'Title: A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'Header: Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard Unive', '====================', 'Title: A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'Header: A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  conditi']}

exec(code, env_args)
