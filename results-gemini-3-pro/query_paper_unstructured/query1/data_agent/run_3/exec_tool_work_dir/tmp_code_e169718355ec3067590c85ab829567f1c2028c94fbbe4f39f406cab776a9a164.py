code = """import json
import re

# Load paper docs (the one with 99 items)
with open(locals()['var_function-call-9193027681353351891'], 'r') as f:
    paper_docs = json.load(f)

# Load citations
with open(locals()['var_function-call-10278166770112498048'], 'r') as f:
    citations = json.load(f)

food_titles = set()

for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    title = filename.replace('.txt', '')
    
    # Check title
    if 'food' in title.lower():
        food_titles.add(title)
        continue
        
    # Check keywords
    # Regex to find keywords section
    # Looking for "Keywords" or "Author Keywords" followed by text until a section header
    # Common headers: INTRODUCTION, ACM Classification, ABSTRACT, CCS Concepts
    match = re.search(r'(Author Keywords|Keywords)([\s\S]{1,1000}?)(INTRODUCTION|ACM Classification|ABSTRACT|CCS Concepts)', text, re.IGNORECASE)
    if match:
        keywords_block = match.group(2)
        if 'food' in keywords_block.lower():
            food_titles.add(title)
            continue
            
    # Also check if 'food' is in the text? No, as discussed, false positives.
    # But wait, what if 'food' is a domain but not in keywords?
    # The prompt says "Common domains include: 'food'... Fields like domain... may contain multiple values".
    # This implies extraction. Keywords are the best proxy.

total_citations = 0
citation_count = 0

for cit in citations:
    if cit['title'] in food_titles:
        try:
            total_citations += int(cit['citation_count'])
            citation_count += 1
        except ValueError:
            pass

print("__RESULT__:")
print(json.dumps({
    "food_titles": list(food_titles),
    "total_citations": total_citations,
    "citation_record_count": citation_count
}))"""

env_args = {'var_function-call-5922621878014711528': ['paper_docs'], 'var_function-call-11455490410163430330': 'file_storage/function-call-11455490410163430330.json', 'var_function-call-8384665205253997752': 'file_storage/function-call-8384665205253997752.json', 'var_function-call-10278166770112498048': 'file_storage/function-call-10278166770112498048.json', 'var_function-call-2640047506381148300': {'food_titles': [], 'total_citations': 0, 'count_of_citation_records': 0}, 'var_function-call-515143036915456539': {'titles': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'], 'keywords_extraction_sample': 'Author Keywords \nLived Informatics; Personal Informatics; Self-Tracking; \nLapsing; Physical Activity; Finances; Location. \n\nACM Classification', 'papers_with_food_in_text': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'], 'count_food_in_text': 3}, 'var_function-call-951559434042508986': {'total_papers': 5, 'papers_with_food_in_text': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt']}, 'var_function-call-8448969420270097609': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-3752428650940545030': ['Why and What Did We Throw out?: Probing on Reflection Through the Food Waste Diary', 'My Doctor is Keeping an Eye on Me!: Exploring the Clinical Applicability of a Mobile Food Logger', 'Identifying and Planning for Individualized Change: Patient-Provider Collaboration Using Lightweight Food Diaries in Healthy Eating and Irritable Bowel Syndrome', 'Supporting Patient-Provider Collaboration to Identify Individual Triggers Using Food and Symptom Journals', 'TummyTrials: A Feasibility Study of Using Self-Experimentation to Detect Individualized Food Triggers', 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'Co-Designing Food Trackers with Dietitians: Identifying Design Opportunities for Food Tracker Customization', 'TableChat: Mobile Food Journaling to Facilitate Family Support for Healthy Eating', 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture'], 'var_function-call-8437126543979926920': [], 'var_function-call-9193027681353351891': 'file_storage/function-call-9193027681353351891.json', 'var_function-call-14112794957952023730': 99}

exec(code, env_args)
