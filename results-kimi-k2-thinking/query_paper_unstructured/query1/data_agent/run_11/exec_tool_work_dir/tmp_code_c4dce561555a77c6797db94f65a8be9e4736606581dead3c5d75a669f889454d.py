code = """import json

# Load citations
citations_file = locals()['var_functions.query_db:8']
with open(citations_file, 'r') as f:
    citations = json.load(f)

# Food paper titles from our analysis
food_paper_titles = [
    "A Lived Informatics Model of Personal Informatics",
    "A Stage-based Model of Personal Informatics Systems", 
    "A Trip to the Moon: Personalized Animated Movies for Self-reflection",
    "A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App",
    "ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation"
]

# Check which food papers have citation records
citation_titles = set([c['title'] for c in citations])
matching_papers = []

for paper_title in food_paper_titles:
    if paper_title in citation_titles:
        matching_papers.append(paper_title)

# Also check for partial matches or similar titles
partial_matches = {}
for paper_title in food_paper_titles:
    for cit_title in citation_titles:
        # Check if paper title is contained in citation title or vice versa
        if paper_title.lower() in cit_title.lower() or cit_title.lower() in paper_title.lower():
            if paper_title not in partial_matches:
                partial_matches[paper_title] = []
            partial_matches[paper_title].append(cit_title)

result = {
    'exact_matches': matching_papers,
    'num_exact_matches': len(matching_papers),
    'partial_matches': partial_matches,
    'total_citation_titles': len(citation_titles)
}

# Also check all citations that mention food/eating
food_citation_keywords = ['food', 'eating', 'nutrition', 'diet', 'meal', 'calorie', 'weight']
food_related_citations = []

for citation in citations:
    cit_title_lower = citation['title'].lower()
    if any(keyword in cit_title_lower for keyword in food_citation_keywords):
        food_related_citations.append({
            'title': citation['title'],
            'citation_count': int(citation['citation_count'])
        })

result['food_related_citation_titles'] = food_related_citations
result['num_food_related_citations'] = len(food_related_citations)

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'total_citations': 1405, 'total_papers': 5, 'sample_citations': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}]}, 'var_functions.execute_python:14': {'food_papers_found': 5, 'food_paper_titles': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation'], 'food_citation_records': 31, 'total_citation_count': 1593}, 'var_functions.execute_python:16': [{'title': 'A Lived Informatics Model of Personal Informatics', 'has_food': True, 'has_nutrition': False, 'has_diet': False, 'text_preview': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characteriz"}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'has_food': True, 'has_nutrition': False, 'has_diet': False, 'text_preview': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowledge.  A  class  of  systems \ncalled  personal  informatics  is  appearing  that  help  people \ncollect and reflect on personal information. However, there \nis no comprehensive list of problems that use'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'has_food': True, 'has_nutrition': False, 'has_diet': False, 'text_preview': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard University\nCambridge, MA, USA\neyue@college.harvard.edu\n\nABSTRACT\nSelf-tracking physiological and psychological data poses the\nchallenge of presentation and interpretation. Insightful nar-\nratives for self-'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'has_food': True, 'has_nutrition': False, 'has_diet': True, 'text_preview': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  condition, \naffecting  20%  of  the  population.  Even  though  it  is  a \ntreatable  condition,  people  often  do  not  seek  treatment.  In \nthis paper, we  describe how we co-designed and evaluated \nwith'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'has_food': True, 'has_nutrition': False, 'has_diet': True, 'text_preview': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent Crocher1,3, Frank Vetere1, Suranga Nanayakkara1,4 \n1Microsoft Research Centre for SocialNUI, The University of Melbourne, Australia \n2Queensland University of Technology, Brisbane, Australia \n3Department of Mechanical Engineering, The University of Melbourne, Australia \n4Augmented Human Lab, Singapor'}], 'var_functions.execute_python:18': {'num_citation_records': 1405, 'num_papers': 5, 'sample_citation_titles': ['Sundroid: Solar Radiation Awareness with Smartphones', 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing'], 'all_paper_titles': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation']}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'total_citation_titles': 259, 'total_paper_docs': 5, 'sample_citation_titles': ["Things You Don'T Want to Know About Yourself: Ambivalence About Tracking and Sharing Personal Information for Behaviour Change", 'Predicting Interruptibility for Manual Data Collection: A Cluster-based User Model', 'Trajectories of Engagement and Disengagement with a Story-Based Smoking Cessation App', 'Designing for Diabetes Decision Support Systems with Fluid Contextual Reasoning', 'Balancing Accuracy and Fun: Designing Camera Based Mobile Games for Implicit Heart Rate Monitoring', 'Self-reflection on Personal Values to Support Value-sensitive Design', 'ClimbSense: Automatic Climbing Route Recognition Using Wrist-worn Inertia Measurement Units', 'Scaffolding for an OLM for Long-Term Physical Activity Goals', 'Intelligent Computing in Personal Informatics: Key Design Considerations', 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'Using Context to Reveal Factors That Affect Physical Activity', 'Informing Design for Reflection: An Overview of Current Everyday Practices', 'Leveraging Intermediated Interactions to Support Utilization of Persuasive Personal Health Informatics', 'Quantified Factory Worker - Expert Evaluation and Ethical Considerations of Wearable Self-tracking Devices', "The Quantified Patient in the Doctor's Office: Challenges & Opportunities", 'Sensor Requirements for Activity Recognition on Smart Watches', 'Sharing Automatically Tracked Activity Data: Implications for Therapists and People with Mobility Impairments', 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'Enhancing Personal Informatics Through Social Sensemaking', 'Supporting Meaningful Personal Fitness: The Tracker Goal Evolution Model']}, 'var_functions.execute_python:24': {'food_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'keyword_hits': {'food': 13, 'eating': 5, 'meal': 1, 'calorie': 1, 'weight': 15}, 'total_mentions': 35}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'keyword_hits': {'food': 13, 'eating': 9, 'meal': 1, 'calorie': 3, 'weight': 5}, 'total_mentions': 31}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'keyword_hits': {'eating': 10, 'diet': 1, 'meal': 1, 'weight': 2}, 'total_mentions': 14}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'keyword_hits': {'eating': 3}, 'total_mentions': 3}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'keyword_hits': {'food': 1, 'diet': 1, 'meal': 1}, 'total_mentions': 3}], 'num_food_papers': 5}}

exec(code, env_args)
