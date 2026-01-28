code = """import json
import re

# Read paper docs data
paper_docs_file = locals()['var_functions.query_db:14']
with open(paper_docs_file, 'r') as f:
    papers = json.load(f)

# Extract food domain papers based on content analysis
food_domain_papers = []
food_keywords = ['food', 'eating', 'diet', 'meal', 'nutrition', 'calorie', 'dietary', 'dieting']

for paper in papers:
    filename = paper['filename']
    text = paper['text']
    title = filename.replace('.txt', '')
    
    # More comprehensive check for food domain
    # Look for explicit domain mentions or food-focused content
    is_food_paper = False
    
    # Check if the paper is primarily about food (not just mentioning it as an example)
    text_lower = text.lower()
    
    # Count food keyword occurrences
    food_mentions = sum(len(re.findall(r'\b' + keyword + r'\b', text_lower)) for keyword in food_keywords)
    
    # If food is mentioned frequently, it's likely a food domain paper
    if food_mentions >= 3:  # Threshold for being food-focused
        is_food_paper = True
    
    # Check for explicit domain statements
    domain_patterns = [
        r'domain.*food',
        r'food.*domain',
        r'tracking.*food',
        r'food.*tracking',
        r'food journal',
        r'food logging'
    ]
    
    for pattern in domain_patterns:
        if re.search(pattern, text_lower):
            is_food_paper = True
            break
    
    if is_food_paper:
        food_domain_papers.append(title)

# Read citations data
citations_file = locals()['var_functions.query_db:8']
with open(citations_file, 'r') as f:
    citations = json.load(f)

# Find citations for food domain papers
food_citation_total = 0
matched_papers = set()

for citation in citations:
    citation_title = citation['title']
    
    # Check if citation matches any food domain paper
    for food_paper in food_domain_papers:
        if citation_title == food_paper:
            food_citation_total += int(citation['citation_count'])
            matched_papers.add(food_paper)
            break

print('__RESULT__:')
print(json.dumps({
    'food_domain_papers': food_domain_papers,
    'matched_papers': list(matched_papers),
    'total_citation_count': food_citation_total,
    'num_citation_records': sum(1 for c in citations for fp in food_domain_papers if c['title'] == fp)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': [], 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_citations': 0, 'food_paper_titles': [], 'citation_count': 0}, 'var_functions.execute_python:18': {'total_citations': 1405, 'total_papers': 5, 'exact_matches_count': 5, 'food_citation_titles_count': 104, 'food_paper_titles_count': 1, 'food_citation_titles': ['Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling'], 'food_paper_titles': ['Barriers and Negative Nudges: Exploring Challenges in Food Journaling']}, 'var_functions.execute_python:20': {'total_citation_count': 5221, 'unique_food_papers': 19, 'paper_totals': {'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture': 426, 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling': 270, "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps": 272, 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance': 276, 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers': 362, 'Toward Health Information Technology That Supports Overweight/Obese Women in Addressing Emotion- and Stress-Related Eating': 284, 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating': 143, 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness': 153, 'Lunch Line: Using Public Displays and Mobile Devices to Encourage Healthy Eating in an Organization': 410, 'Why and What Did We Throw out?: Probing on Reflection Through the Food Waste Diary': 317, 'Supporting Patient-Provider Collaboration to Identify Individual Triggers Using Food and Symptom Journals': 125, 'TummyTrials: A Feasibility Study of Using Self-Experimentation to Detect Individualized Food Triggers': 331, 'Co-Designing Food Trackers with Dietitians: Identifying Design Opportunities for Food Tracker Customization': 424, 'Identifying and Planning for Individualized Change: Patient-Provider Collaboration Using Lightweight Food Diaries in Healthy Eating and Irritable Bowel Syndrome': 247, 'TableChat: Mobile Food Journaling to Facilitate Family Support for Healthy Eating': 213, 'Soylent Diet Self-Experimentation: Design Challenges in Extreme Citizen Science Projects': 36, 'My Doctor is Keeping an Eye on Me!: Exploring the Clinical Applicability of a Mobile Food Logger': 105, 'Can SAL Support Self Reflection for Health and Nutrition?': 450, 'Predicting About-to-Eat Moments for Just-in-Time Eating Intervention': 377}}, 'var_functions.query_db:22': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}]}

exec(code, env_args)
