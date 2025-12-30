code = """import json

# Load citations
with open(locals()['var_function-call-15503541887771276820'], 'r') as f:
    citations = json.load(f)

# Create a dictionary for quick lookup: title -> citation_count
# Note: citations have 'title', 'citation_count', 'citation_year' (checked in query)
# The query was "SELECT title, citation_count FROM Citations WHERE citation_year = 2018"
citation_map = {c['title']: int(c['citation_count']) for c in citations}

# Load paper docs
with open(locals()['var_function-call-4898156154949996726'], 'r') as f:
    paper_docs = json.load(f)

acm_papers_count = 0
total_citations = 0
acm_titles = []

for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check if ACM
    # Heuristic: 'ACM' in first 2000 chars or 'Association for Computing Machinery'
    # The text preview showed "Copyright 2015 © ACM" and "ACM Classification Keywords"
    is_acm = False
    if 'ACM' in text[:3000] or 'Association for Computing Machinery' in text[:3000]:
        is_acm = True
    
    if is_acm:
        if title in citation_map:
            count = citation_map[title]
            total_citations += count
            acm_papers_count += 1
            acm_titles.append((title, count))

if acm_papers_count > 0:
    avg_citation = total_citations / acm_papers_count
else:
    avg_citation = 0

print("__RESULT__:")
print(json.dumps({
    "average": avg_citation,
    "count": acm_papers_count,
    "titles_found": acm_titles
}))"""

env_args = {'var_function-call-15503541887771276820': 'file_storage/function-call-15503541887771276820.json', 'var_function-call-11206421856392368221': {'count': 158, 'first_10': ['Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing.txt', 'Sundroid: Solar Radiation Awareness with Smartphones.txt', 'Why We Use and Abandon Smart Devices.txt', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App.txt', 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set.txt', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt", 'Reviewing Reflection: On the Use of Reflection in Interactive System Design.txt', 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers.txt', 'Beyond Self-Tracking and Reminders: Designing Smartphone Apps That Support Habit Formation.txt', 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection.txt']}, 'var_function-call-7875939014614819259': 'file_storage/function-call-7875939014614819259.json', 'var_function-call-509776034096291468': [{'_id': '694f5530284b10b11dc0a869'}, {'_id': '694f5530284b10b11dc0a86a'}, {'_id': '694f5530284b10b11dc0a86b'}, {'_id': '694f5530284b10b11dc0a86c'}, {'_id': '694f5530284b10b11dc0a86d'}], 'var_function-call-2979635559747287389': 5, 'var_function-call-10712887416649131953': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-4898156154949996726': 'file_storage/function-call-4898156154949996726.json'}

exec(code, env_args)
