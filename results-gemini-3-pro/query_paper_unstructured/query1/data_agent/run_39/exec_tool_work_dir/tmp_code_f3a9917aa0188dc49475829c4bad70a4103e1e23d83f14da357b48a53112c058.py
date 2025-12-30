code = """import json

# Load paper_docs
with open(locals()['var_function-call-16958740794073155916'], 'r') as f:
    paper_docs = json.load(f)

# Load citations
with open(locals()['var_function-call-9545123832461402324'], 'r') as f:
    citations = json.load(f)

food_papers = []
newline = chr(10)
double_newline = newline + newline

for paper in paper_docs:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    text = paper.get('text', '')
    text_lower = text.lower()
    
    is_food = False
    
    # 1. Check title
    if 'food' in title.lower():
        is_food = True
    
    if not is_food:
        # 2. Check keywords
        kw_starts = ["author keywords", "index terms", "keywords"]
        found_keywords = False
        
        for start_phrase in kw_starts:
            start_idx = text_lower.find(start_phrase)
            if start_idx != -1:
                found_keywords = True
                # snippet from start of keywords
                snippet = text_lower[start_idx:start_idx+600]
                
                # Truncate at double newline
                end_idx = snippet.find(double_newline)
                if end_idx != -1:
                    snippet = snippet[:end_idx]
                
                # Truncate at next section headers
                for section in ["introduction", "abstract", "acm classification", "general terms"]:
                    if section in snippet and snippet.find(section) > 10: # ensure we don't cut immediately if keywords is part of header
                         snippet = snippet.split(section)[0]
                
                if 'food' in snippet:
                    is_food = True
                break # Stop checking other keyword markers if one found
        
        # 3. If keywords NOT found, check Abstract
        if not found_keywords:
             start_idx = text_lower.find("abstract")
             if start_idx != -1:
                snippet = text_lower[start_idx:start_idx+2000]
                
                end_idx = snippet.find("introduction")
                if end_idx != -1:
                    snippet = snippet[:end_idx]
                
                # Also stop if we hit keyword markers (in case we missed them or they are later)
                for start_phrase in kw_starts:
                    k_idx = snippet.find(start_phrase)
                    if k_idx != -1:
                        snippet = snippet[:k_idx]

                if 'food' in snippet:
                    is_food = True

    if is_food:
        food_papers.append(title)

# Filter citations
total_citations = 0
food_papers_set = set(food_papers)
citations_list = []

for cit in citations:
    if cit['title'] in food_papers_set:
        try:
            val = int(cit['citation_count'])
            total_citations += val
            citations_list.append(val)
        except:
            pass

print("__RESULT__:")
print(json.dumps({"food_papers_count": len(food_papers), "food_papers_titles": food_papers, "total_citations": total_citations}))"""

env_args = {'var_function-call-8528399130518209876': ['paper_docs'], 'var_function-call-8528399130518209403': ['Citations', 'sqlite_sequence'], 'var_function-call-5911009850598284906': 'file_storage/function-call-5911009850598284906.json', 'var_function-call-5911009850598284323': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-8131891965155681043': 'file_storage/function-call-8131891965155681043.json', 'var_function-call-9545123832461402324': 'file_storage/function-call-9545123832461402324.json', 'var_function-call-16177678008665017919': {'food_papers_count': 0, 'food_papers_titles': [], 'total_citations': 0}, 'var_function-call-9443954233437372911': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'context': 'r  tracking  location  [24,30],  finances  [20],  food  [11],  weight  [19,25],  and  physical  acti'}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'context': 'projects  on  her  personal  behavior,  such  as  food  consumption  and  sneezes  (http://ellieharr'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'context': 'sist  of  avoiding  bladder  irritants  (certain  food  and  drinks)  and  consuming  a  proper  amo'}], 'var_function-call-7379546396970470087': {'count': 5, 'titles': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt']}, 'var_function-call-16958740794073155916': 'file_storage/function-call-16958740794073155916.json', 'var_function-call-13973086622616753670': {'count': 99}, 'var_function-call-16637268328583096286': {'food_papers_count': 15, 'food_papers_titles': ['Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'Blood Pressure Beyond the Clinic: Rethinking a Health Metric for Everyone', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance', 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats', 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps", 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'TastyBeats: Designing Palatable Representations of Physical Activity', 'The Power of Mobile Notifications to Increase Wellbeing Logging Behavior', 'Understanding Animals: A Critical Challenge in ACI', "We'Ve Bin Watching You: Designing for Reflection and Social Persuasion to Promote Sustainable Lifestyles", 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating'], 'total_citations': 4096}, 'var_function-call-6764447582355296498': [{'title': 'Blood Pressure Beyond the Clinic: Rethinking a Health Metric for Everyone.txt', 'keywords': 'Author Keywords  Personal informatics; blood pressure; self-monitoring.   ACM Classification Keywords  J.3. Life and medical sciences: Health.   INTRODUCTION  Blood pressure (BP) is an important and widely used indi- cator for assessing cardiovascular health. One in five hyper- tensive  individuals '}, {'title': 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal.txt', 'keywords': 'Not Found'}, {'title': 'The Power of Mobile Notifications to Increase Wellbeing Logging Behavior.txt', 'keywords': 'Author Keywords  Mobile; Notifications; Behavior Change; Wellbeing;  Logging; Personal Informatics   ACM Classification Keywords  H.5.m. Information interfaces and presentation (e.g., HCI):  Miscellaneous.    General Terms  Human Factors; Design; Measurement.    INTRODUCTION  There is currently a gr'}, {'title': 'Understanding Animals: A Critical Challenge in ACI.txt', 'keywords': 'Author Keywords  Animal-Computer Interaction; Quantified Pets; Dog Blogs;  Social Media; Kinesthetic Empathy; Pet Dogs;   ACM Classification Keywords   H5.m.  Information  interfaces  and  presentation  (e.g.,  HCI):  Miscellaneous.    INTRODUCTION  In  recent  years,  we  have  seen an emergent des'}], 'var_function-call-13055218589341419348': {'text_snippet': 'Goal-setting And Achievement In Activity Tracking Apps: A Case\nStudy Of MyFitnessPal\n\nMitchell L. Gordon\nStanford University\nmgord@cs.stanford.edu\n\nTim Althoff\nUniversity of Washington\nalthoff@cs.washington.edu\n\nJure Leskovec\nStanford University\njure@cs.stanford.edu\n\nABSTRACT\nActivity tracking apps often make use of goals as one of their\ncore motivational tools. There are two critical components to this\ntool: setting a goal, and subsequently achieving that goal. Despite\nits crucial role in how a number of prominent self-tracking apps\nfunction, there has been relatively little investigation of the goal-\nsetting and achievement aspects of self-tracking apps.\n\nHere we explore this issue, investigating a particular goal setting\nand achievement process that is extensive, recorded, and crucial for\nboth the app and its users’ success: weight loss goals in MyFitness-\nPal. We present a large-scale study of 1.4 million users and weight\nloss goals, allowing for an unprecedented detailed view of how\npeople set and achieve their goals. We find that, even for difficult\nlong-term goals, behavior within the first 7 days predicts those who\nultimately achieve their goals, that is, those who lose at least as\nmuch weight as they set out to, and those who do not. For instance,\nhigh amounts of early weight loss, which some researchers have\nclassified as unsustainable, leads to higher goal achievement rates.\nWe also show that early food intake, self-monitoring motivation,\nand attitude towards the goal are important factors. We then show\nthat we can use our findings to predict goal achievement with an\naccuracy of 79% ROC AUC just 7 days after a goal is set. Finally,\nwe discuss how our findings could inform steps to improve goal\nachievement in self-tracking apps.\n\nACM Reference Format:\nMitchell L. Gordon, Tim Althoff, and Jure Leskovec. 2019. Goal-setting And\nAchievement In Activity Tracking Apps: A Case Study Of MyFitnessPal.\nIn Proceedings of the 2019 World Wide Web Conference (WWW ’19), '}, 'var_function-call-10588831863622034985': {'text_snippet': 'Does Journaling Encourage Healthier Choices?\nAnalyzing Healthy Eating Behaviors of Food Journalers\n\nPalakorn Achananuparp\nSingapore Management University\nSingapore, Singapore\npalakorna@smu.edu.sg\n\nEe-Peng Lim\nSingapore Management University\nSingapore, Singapore\neplim@smu.edu.sg\n\nVibhanshu Abhishek\nCarnegie Mellon University\nPittsburgh, PA\nvibs@andrew.cmu.edu\n\nABSTRACT\nPast research has shown the benefits of food journaling in promot-\ning mindful eating and healthier food choices. However, the links\nbetween journaling and healthy eating have not been thoroughly\nexamined. Beyond caloric restriction, do journalers consistently\nand sufficiently consume healthful diets? How different are their\neating habits compared to those of average consumers who tend\nto be less conscious about health? In this study, we analyze the\nhealthy eating behaviors of active food journalers using data from\nMyFitnessPal. Surprisingly, our findings show that food journalers\ndo not eat as healthily as they should de'}, 'var_function-call-1178634719989527861': {'has_keywords': False, 'snippet': ''}, 'var_function-call-8907242634215246053': {'has_keywords': True, 'snippet': 'Keywords \nPersuasive; \nbehavioral change; social networks; sustainable HCI. \n\ntechnology;  social  persuasion; \n\nreflection; \n\nACM Classification Keywords \nH.5.m [Information interfaces and presentati'}}

exec(code, env_args)
