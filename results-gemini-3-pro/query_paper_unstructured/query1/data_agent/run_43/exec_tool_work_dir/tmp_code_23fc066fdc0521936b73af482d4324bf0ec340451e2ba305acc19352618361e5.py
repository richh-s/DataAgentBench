code = """import json
import pandas as pd

# Load papers
with open(locals()['var_function-call-10671652742287375173'], 'r') as f:
    papers = json.load(f)

# Load citations
with open(locals()['var_function-call-10038520539297588104'], 'r') as f:
    citations = json.load(f)

df_citations = pd.DataFrame(citations)
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'])

newline = chr(10)
double_newline = newline + newline

def get_keywords(text):
    text_lower = text.lower()
    keywords = ""
    # Try Author Keywords
    start = text_lower.find("author keywords")
    if start != -1:
        # Find end (double newline or next section)
        end1 = text_lower.find(double_newline, start)
        end2 = text_lower.find("acm classification", start)
        end3 = text_lower.find("introduction", start)
        
        candidates = [e for e in [end1, end2, end3] if e != -1 and e > start]
        if candidates:
            end = min(candidates)
            keywords += text_lower[start:end]
            
    # Try ACM Classification
    start_acm = text_lower.find("acm classification keywords")
    if start_acm != -1:
        end1 = text_lower.find(double_newline, start_acm)
        end2 = text_lower.find("introduction", start_acm)
        candidates = [e for e in [end1, end2] if e != -1 and e > start_acm]
        if candidates:
            end = min(candidates)
            keywords += " " + text_lower[start_acm:end]
            
    return keywords

food_titles = []
food_terms = ["food", "diet", "eating", "nutrition"]

for p in papers:
    filename = p['filename']
    title = filename.replace('.txt', '')
    text = p['text']
    
    # Check Title
    if any(term in title.lower() for term in food_terms):
        food_titles.append(title)
        continue
        
    # Check Keywords
    keywords = get_keywords(text)
    if any(term in keywords for term in food_terms):
        food_titles.append(title)
        continue

# Filter citations
food_citations = df_citations[df_citations['title'].isin(food_titles)]
total_citations = food_citations['citation_count'].sum()

print("__RESULT__:")
print(json.dumps(int(total_citations)))"""

env_args = {'var_function-call-4706990439072147394': 'file_storage/function-call-4706990439072147394.json', 'var_function-call-4706990439072147581': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-789985204037697992': 'file_storage/function-call-789985204037697992.json', 'var_function-call-10038520539297588104': 'file_storage/function-call-10038520539297588104.json', 'var_function-call-6756475489867741448': 0, 'var_function-call-14441792341353093179': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'has_food_in_text': True, 'snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characteriz"}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'has_food_in_text': True, 'snippet': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowledge.  A  class  of  systems \ncalled  personal  informatics  is  appearing  that  help  people \ncollect and reflect on personal information. However, there \nis no comprehensive list of problems that use'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'has_food_in_text': False, 'snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard University\nCambridge, MA, USA\neyue@college.harvard.edu\n\nABSTRACT\nSelf-tracking physiological and psychological data poses the\nchallenge of presentation and interpretation. Insightful nar-\nratives for self-'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'has_food_in_text': True, 'snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  condition, \naffecting  20%  of  the  population.  Even  though  it  is  a \ntreatable  condition,  people  often  do  not  seek  treatment.  In \nthis paper, we  describe how we co-designed and evaluated \nwith'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'has_food_in_text': False, 'snippet': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent Crocher1,3, Frank Vetere1, Suranga Nanayakkara1,4 \n1Microsoft Research Centre for SocialNUI, The University of Melbourne, Australia \n2Queensland University of Technology, Brisbane, Australia \n3Department of Mechanical Engineering, The University of Melbourne, Australia \n4Augmented Human Lab, Singapor'}], 'var_function-call-12396229705465881554': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'keywords_snippet': 'Author Keywords  Lived Informatics; Personal Informatics; Self-Tracking;  Lapsing; Physical Activity; Finances; Location. '}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'keywords_snippet': 'Author Keywords  Personal informatics, collection, reflection, model, barriers '}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'keywords_snippet': 'Not Found'}], 'var_function-call-16020022388704703752': [], 'var_function-call-2426335157302515662': [], 'var_function-call-11799278089327443143': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'count': 13}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'count': 13}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'count': 1}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'count': 0}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'count': 0}], 'var_function-call-16706573878102499289': [{'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'food': 13, 'diet': 0, 'nutrition': 0, 'eating': 9, 'total': 22}, {'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'food': 13, 'diet': 0, 'nutrition': 0, 'eating': 5, 'total': 18}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'food': 0, 'diet': 1, 'nutrition': 0, 'eating': 10, 'total': 11}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'food': 0, 'diet': 0, 'nutrition': 0, 'eating': 3, 'total': 3}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'food': 1, 'diet': 1, 'nutrition': 0, 'eating': 0, 'total': 2}], 'var_function-call-16618640162915587585': 5, 'var_function-call-15720309966878672766': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-9033867705320150093': ['paper_docs'], 'var_function-call-9033867705320149158': ['Citations', 'sqlite_sequence'], 'var_function-call-15118389576806615827': [{'title': 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture'}, {'title': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling'}, {'title': "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps"}, {'title': 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance'}, {'title': 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers'}, {'title': 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats'}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity'}, {'title': 'Toward Health Information Technology That Supports Overweight/Obese Women in Addressing Emotion- and Stress-Related Eating'}, {'title': 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating'}, {'title': 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness'}, {'title': 'Lunch Line: Using Public Displays and Mobile Devices to Encourage Healthy Eating in an Organization'}, {'title': 'Why and What Did We Throw out?: Probing on Reflection Through the Food Waste Diary'}, {'title': 'More Than a Show: Using Personalized Immersive Theater to Educate and Engage the Public in Technology Ethics'}, {'title': 'Supporting Patient-Provider Collaboration to Identify Individual Triggers Using Food and Symptom Journals'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'Quantified Self: An Interdisciplinary Immersive Theater Project Supporting a Collaborative Learning Environment for CS Ethics'}, {'title': 'TummyTrials: A Feasibility Study of Using Self-Experimentation to Detect Individualized Food Triggers'}, {'title': 'Co-Designing Food Trackers with Dietitians: Identifying Design Opportunities for Food Tracker Customization'}, {'title': 'Identifying and Planning for Individualized Change: Patient-Provider Collaboration Using Lightweight Food Diaries in Healthy Eating and Irritable Bowel Syndrome'}, {'title': 'TableChat: Mobile Food Journaling to Facilitate Family Support for Healthy Eating'}, {'title': 'Snot, Sweat, Pain, Mud, and Snow: Performance and Experience in the Use of Sports Watches'}, {'title': 'Soylent Diet Self-Experimentation: Design Challenges in Extreme Citizen Science Projects'}, {'title': 'My Doctor is Keeping an Eye on Me!: Exploring the Clinical Applicability of a Mobile Food Logger'}, {'title': 'Can SAL Support Self Reflection for Health and Nutrition?'}, {'title': 'Predicting About-to-Eat Moments for Just-in-Time Eating Intervention'}], 'var_function-call-5692667445092422713': 'file_storage/function-call-5692667445092422713.json', 'var_function-call-1941515165641134350': [{'COUNT(*)': '1405'}], 'var_function-call-12688638102771479759': [{'COUNT(DISTINCT title)': '259'}], 'var_function-call-10671652742287375173': 'file_storage/function-call-10671652742287375173.json'}

exec(code, env_args)
