code = """import json
import re

with open(locals()['var_function-call-17486704262329443494'], 'r') as f:
    citations_data = json.load(f)

with open(locals()['var_function-call-9673377435246489263'], 'r') as f:
    papers_data = json.load(f)

# Build citation map
citation_sums = {}
for entry in citations_data:
    title = entry['title']
    try:
        count = int(entry['citation_count'])
    except:
        count = 0
    citation_sums[title] = citation_sums.get(title, 0) + count

found_papers = []
total_citations = 0

for p in papers_data:
    text = p['text']
    filename = p['filename']
    title = filename.replace('.txt', '')
    
    # Try multiple patterns for keywords
    # Pattern 1: Author Keywords
    match = re.search(r'(?:Author Keywords|Keywords|Index Terms)(.*?)(?:ACM Classification Keywords|INTRODUCTION|General Terms|ABSTRACT|$)', text, re.DOTALL | re.IGNORECASE)
    
    keywords = ""
    if match:
        keywords = match.group(1).lower()
    
    # Check for "food" in keywords
    if 'food' in keywords:
        found_papers.append(title)
        total_citations += citation_sums.get(title, 0)
    else:
        # Fallback: check if "food" is in the Abstract?
        # Abstract usually follows ABSTRACT header.
        abstract_match = re.search(r'ABSTRACT(.*?)(?:Author Keywords|Keywords|Index Terms|INTRODUCTION|ACM Classification Keywords)', text, re.DOTALL | re.IGNORECASE)
        if abstract_match:
            abstract = abstract_match.group(1).lower()
            # If "food" appears in abstract, is it a food paper?
            # Maybe, but safer to check for "food tracking", "food journaling", "food diary", "food intake".
            # Or just "food".
            # Let's try to see if any additional papers are found with "food" in abstract.
            # I won't add them yet, but I'll list them to decide.
            pass

print("__RESULT__:")
print(json.dumps({"count": total_citations, "papers": found_papers}))"""

env_args = {'var_function-call-16442091982687073941': 'file_storage/function-call-16442091982687073941.json', 'var_function-call-8772526442893089747': 'file_storage/function-call-8772526442893089747.json', 'var_function-call-9673377435246489263': 'file_storage/function-call-9673377435246489263.json', 'var_function-call-17486704262329443494': 'file_storage/function-call-17486704262329443494.json', 'var_function-call-1266494665686074399': 0, 'var_function-call-4508597791168486055': 'done', 'var_function-call-13604048881481762108': {'titles': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'], 'keywords_sample': [{'file': 'A Lived Informatics Model of Personal Informatics.txt', 'kw': 'Lived Informatics; Personal Informatics; Self-Tracking; \nLapsing; Physical Activity; Finances; Location.'}, {'file': 'A Stage-based Model of Personal Informatics Systems.txt', 'kw': 'Personal informatics, collection, reflection, model, barriers'}, {'file': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'kw': 'Personalization; animation; emotion; engagement; empathy;\nself-reﬂection.'}, {'file': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'kw': 'None'}, {'file': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'kw': 'Wearable technology; dashboard; information visualization; \nstroke rehabilitation; occupational therapy'}], 'food_titles': []}}

exec(code, env_args)
