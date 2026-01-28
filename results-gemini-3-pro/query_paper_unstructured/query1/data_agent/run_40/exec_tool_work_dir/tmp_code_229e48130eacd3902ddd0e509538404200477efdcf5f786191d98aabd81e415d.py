code = """import json

file_path = locals()['var_function-call-17774907068370160114']
with open(file_path, 'r') as f:
    papers = json.load(f)

food_papers = []

for p in papers:
    filename = p.get('filename', '')
    text = p.get('text', '')
    title = filename.replace('.txt', '')
    
    is_food = False
    
    # Check title
    if 'food' in title.lower():
        is_food = True
    else:
        # Check Keywords
        # Find "Author Keywords"
        lower_text = text.lower()
        idx = lower_text.find("author keywords")
        if idx != -1:
            # Check the next 500 characters
            snippet = lower_text[idx:idx+500]
            if "food" in snippet:
                is_food = True
        else:
            # Try just "keywords"
            idx = lower_text.find("keywords")
            if idx != -1:
                snippet = lower_text[idx:idx+500]
                # Check that it's not "keywords" in the middle of a sentence
                # Usually keywords are at the start of a line or after abstract
                if "food" in snippet:
                    # Double check it's not a false positive like "keywords such as food"
                    # But for now, let's assume it's a signal. 
                    # Given the limited domain list, "food" appearing near "keywords" is strong.
                    is_food = True

    if is_food:
        food_papers.append(title)

print("__RESULT__:")
print(json.dumps(food_papers))"""

env_args = {'var_function-call-2991259327904718266': ['paper_docs'], 'var_function-call-2991259327904718481': ['Citations', 'sqlite_sequence'], 'var_function-call-10512507186521432510': 'file_storage/function-call-10512507186521432510.json', 'var_function-call-12545833755252698609': 'file_storage/function-call-12545833755252698609.json', 'var_function-call-10414038178410062022': [], 'var_function-call-9109714520814129217': {'total_papers': 5, 'titles_preview': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation'], 'food_in_text_count': 3, 'food_in_text_titles': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App']}, 'var_function-call-8738282695325536530': [{'count(*)': '1405'}], 'var_function-call-17774907068370160114': 'file_storage/function-call-17774907068370160114.json', 'var_function-call-2658141669876443659': {'count': 99, 'titles': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'Barriers to Engagement with a Personal Informatics Productivity Tool', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'Blood Pressure Beyond the Clinic: Rethinking a Health Metric for Everyone', 'Charting Design Preferences on Wellness Wearables', 'ClimbSense: Automatic Climbing Route Recognition Using Wrist-worn Inertia Measurement Units', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings', 'Communicating Uncertainty in Fertility Prognosis', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'ConCap: Designing to Empower Individual Reflection on Chronic Conditions Using Mobile Apps', 'Contextual Influences on the Use and Non-Use of Digital Technology While Exercising at the Gym', 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'DataSelfie: Empowering People to Design Personalized Visuals to Represent Their Data']}}

exec(code, env_args)
