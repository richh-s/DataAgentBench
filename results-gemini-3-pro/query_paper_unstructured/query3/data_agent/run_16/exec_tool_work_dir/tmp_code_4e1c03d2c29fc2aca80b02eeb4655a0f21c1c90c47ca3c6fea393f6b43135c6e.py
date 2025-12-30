code = """import json
import re

citations_key = 'var_function-call-14861443508322681236'
papers_key = 'var_function-call-1947762228881266501'

with open(locals()[papers_key], 'r') as f:
    papers_data = json.load(f)

with open(locals()[citations_key], 'r') as f:
    citations_data = json.load(f)

# Process citations
citation_counts = {}
min_citation_years = {}
for c in citations_data:
    t = c['title']
    cnt = int(c['citation_count'])
    yr = int(c['citation_year'])
    
    citation_counts[t] = citation_counts.get(t, 0) + cnt
    
    if t not in min_citation_years or yr < min_citation_years[t]:
        min_citation_years[t] = yr

# Process papers
results = []
empirical_keywords = ['empirical', 'interview', 'survey', 'participant', 'user study', 'field study', 'mixed methods', 'qualitative study', 'quantitative study']

for paper in papers_data:
    title = paper.get('filename', '').replace('.txt', '')
    text = paper.get('text', '')
    
    # Year
    # Try regex first
    copyright_match = re.search(r'Copyright\s+(?:©|\(c\))?\s*(20\d{2})', text, re.IGNORECASE)
    header_years = re.findall(r'\b(20\d{2})\b', text[:500])
    
    pub_year = None
    if copyright_match:
        pub_year = int(copyright_match.group(1))
    elif header_years:
        pub_year = int(header_years[0])
    else:
        # Fallback to citation year
        pub_year = min_citation_years.get(title)
        
    # Filter Year > 2016
    if pub_year is None or pub_year <= 2016:
        continue
        
    # Contribution
    # Check for keywords
    text_lower = text.lower()
    is_empirical = False
    for kw in empirical_keywords:
        if kw in text_lower:
            is_empirical = True
            break
            
    if is_empirical:
        results.append({
            "title": title,
            "citation_count": citation_counts.get(title, 0)
        })

# Sort by citation count descending
results.sort(key=lambda x: x['citation_count'], reverse=True)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-13973424374790880036': 'file_storage/function-call-13973424374790880036.json', 'var_function-call-13973424374790878367': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-3366737603932088961': 'file_storage/function-call-3366737603932088961.json', 'var_function-call-8593920629685848414': {'count': 5, 'samples': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'year_extracted': None, 'contrib_context': 'contributions  through  survey  design  and  participant  interviews. \nWe  also  thank  Elena  Agapi'}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'year_extracted': None, 'contrib_context': 'contributions  in  this  paper:  1)  we \nidentify  problems  across  personal  informatics  tools,  '}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'year_extracted': None, 'contrib_context': None}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'year_extracted': None, 'contrib_context': 'contribution “I like drawing!” (UP4),  some  did not like \ndrawing: “I don’t like drawing things.” ('}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'year_extracted': None, 'contrib_context': 'contribution of this research is \na  system  designed  to  support  the  work  of  occupational \nthe'}]}, 'var_function-call-1947762228881266501': 'file_storage/function-call-1947762228881266501.json', 'var_function-call-14861443508322681236': 'file_storage/function-call-14861443508322681236.json', 'var_function-call-3974080567568237': [], 'var_function-call-3100392970530816796': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'years_found': [], 'has_empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'years_found': [], 'has_empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'years_found': [], 'has_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'years_found': [], 'has_empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'years_found': [], 'has_empirical': False}, {'title': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt', 'years_found': [], 'has_empirical': True}, {'title': 'Barriers to Engagement with a Personal Informatics Productivity Tool.txt', 'years_found': [], 'has_empirical': False}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt', 'years_found': [], 'has_empirical': False}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt", 'years_found': [], 'has_empirical': False}, {'title': 'Blood Pressure Beyond the Clinic: Rethinking a Health Metric for Everyone.txt', 'years_found': [], 'has_empirical': False}, {'title': 'Charting Design Preferences on Wellness Wearables.txt', 'years_found': [], 'has_empirical': True}, {'title': 'ClimbSense: Automatic Climbing Route Recognition Using Wrist-worn Inertia Measurement Units.txt', 'years_found': [], 'has_empirical': False}, {'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt", 'years_found': [], 'has_empirical': True}, {'title': 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings.txt', 'years_found': [], 'has_empirical': True}, {'title': 'Communicating Uncertainty in Fertility Prognosis.txt', 'years_found': [], 'has_empirical': True}, {'title': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media.txt', 'years_found': [], 'has_empirical': True}, {'title': 'ConCap: Designing to Empower Individual Reflection on Chronic Conditions Using Mobile Apps.txt', 'years_found': [], 'has_empirical': False}, {'title': 'Contextual Influences on the Use and Non-Use of Digital Technology While Exercising at the Gym.txt', 'years_found': [], 'has_empirical': False}, {'title': 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness.txt', 'years_found': [], 'has_empirical': False}, {'title': 'DataSelfie: Empowering People to Design Personalized Visuals to Represent Their Data.txt', 'years_found': [], 'has_empirical': False}], 'var_function-call-1010465434173921743': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'header_snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu", 'years_found': ['2015']}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'header_snippet': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152', 'years_found': []}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'header_snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali', 'years_found': []}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'header_snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E', 'years_found': []}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'header_snippet': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent C', 'years_found': []}, {'title': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt', 'header_snippet': 'Barriers and Negative Nudges:  \nExploring Challenges in Food Journaling   \nFelicia Cordeiro1, Daniel A. Epstein1, Edison Thomaz3, Elizabeth Bales1,2, \nArvind K. Jagannathan3, Gregory D. Abowd3, James ', 'years_found': []}, {'title': 'Barriers to Engagement with a Personal Informatics Productivity Tool.txt', 'header_snippet': ' Barriers to Engagement with a Personal Informatics \nProductivity Tool \nJon Bird \nCity University London \nSchool of Engineering & \nMathematical Sciences \nLondon, EC1V 0HB \nJon.bird@city.ac.uk \n\nCassie', 'years_found': []}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt', 'header_snippet': 'Beyond Abandonment to Next Steps: Understanding and \nDesigning for Life after Personal Informatics Tool Use \n\nDaniel A. Epstein1, Monica Caraway2, Chuck Johnston2, \nAn Ping2, James Fogarty1, Sean A. M', 'years_found': []}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt", 'header_snippet': 'Beyond Behavior: The Coach’s Perspective \n on Technology in Health Coaching \n\nHeleen Rutjes \n Human-Technology Interaction \n Eindhoven University of Technology \n Eindhoven, the Netherlands \n H.Rutjes@', 'years_found': []}, {'title': 'Blood Pressure Beyond the Clinic: Rethinking a Health Metric for Everyone.txt', 'header_snippet': 'Blood Pressure Beyond the Clinic:  \nRethinking a Health Metric for Everyone  \nLogan Kendall1,2, Dan Morris1, Desney Tan1 \n\n1Microsoft Research \n{dan; desney}@microsoft.com \n\nABSTRACT \nBlood pressure (', 'years_found': []}], 'var_function-call-17431805613401114587': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'year': 2015, 'is_empirical': False, 'copyright_found': True}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'year': 2010, 'is_empirical': False, 'copyright_found': True}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'year': None, 'is_empirical': True, 'copyright_found': False}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'year': None, 'is_empirical': True, 'copyright_found': False}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'year': None, 'is_empirical': False, 'copyright_found': False}, {'title': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt', 'year': 2015, 'is_empirical': True, 'copyright_found': True}, {'title': 'Barriers to Engagement with a Personal Informatics Productivity Tool.txt', 'year': 2014, 'is_empirical': False, 'copyright_found': True}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt', 'year': None, 'is_empirical': False, 'copyright_found': False}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt", 'year': None, 'is_empirical': False, 'copyright_found': False}, {'title': 'Blood Pressure Beyond the Clinic: Rethinking a Health Metric for Everyone.txt', 'year': None, 'is_empirical': False, 'copyright_found': False}, {'title': 'Charting Design Preferences on Wellness Wearables.txt', 'year': None, 'is_empirical': True, 'copyright_found': False}, {'title': 'ClimbSense: Automatic Climbing Route Recognition Using Wrist-worn Inertia Measurement Units.txt', 'year': None, 'is_empirical': False, 'copyright_found': False}, {'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt", 'year': None, 'is_empirical': True, 'copyright_found': False}, {'title': 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings.txt', 'year': None, 'is_empirical': True, 'copyright_found': False}, {'title': 'Communicating Uncertainty in Fertility Prognosis.txt', 'year': None, 'is_empirical': True, 'copyright_found': False}, {'title': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media.txt', 'year': None, 'is_empirical': True, 'copyright_found': False}, {'title': 'ConCap: Designing to Empower Individual Reflection on Chronic Conditions Using Mobile Apps.txt', 'year': None, 'is_empirical': False, 'copyright_found': False}, {'title': 'Contextual Influences on the Use and Non-Use of Digital Technology While Exercising at the Gym.txt', 'year': None, 'is_empirical': False, 'copyright_found': False}, {'title': 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness.txt', 'year': None, 'is_empirical': False, 'copyright_found': False}, {'title': 'DataSelfie: Empowering People to Design Personalized Visuals to Represent Their Data.txt', 'year': None, 'is_empirical': False, 'copyright_found': False}], 'var_function-call-8766788301100764565': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'min_citation_year': 2020}, {'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'min_citation_year': 2017}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'min_citation_year': 2020}]}

exec(code, env_args)
