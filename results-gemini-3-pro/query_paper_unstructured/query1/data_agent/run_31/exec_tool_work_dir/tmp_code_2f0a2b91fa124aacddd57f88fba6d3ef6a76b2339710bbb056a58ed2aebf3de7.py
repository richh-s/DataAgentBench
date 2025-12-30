code = """import json
import re

citations_path = locals()['var_function-call-99245770254800995']
papers_path = locals()['var_function-call-5874155478376628757']

with open(citations_path, 'r') as f:
    citations = json.load(f)

with open(papers_path, 'r') as f:
    papers = json.load(f)

food_papers = []
potential_food_papers = []

for paper in papers:
    text = paper.get('text', '').lower()
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Extract keywords section
    # Strategy: Find "author keywords" or "keywords" (if author keywords not found)
    # Stop at "acm classification" or "introduction" or "abstract" (if keywords appear before abstract? unlikely) or double newline followed by header
    
    # We'll try to capture a chunk after "keywords"
    kw_start = text.find('author keywords')
    if kw_start == -1:
        kw_start = text.find('keywords') # This might match "acm classification keywords", so be careful
        # If it matches "acm classification keywords", we want to avoid that if possible, or assume the line after is keywords?
        # "acm classification keywords" usually comes AFTER author keywords or BEFORE? 
        # In snippet 1: Author Keywords ... ACM Classification Keywords.
        # In snippet 2: Keywords ... ACM Classification Keywords.
        # In snippet 3: Keywords (from Classification?) ... Author Keywords.
        
        # If we find "keywords" and it's part of "acm classification keywords", we might be looking at the wrong place if we want Author Keywords.
        # But if "Author Keywords" is missing, maybe "Keywords" is the header.
        pass
        
    # Let's try regex to be more specific
    # Look for "Keywords" at the start of a line or following a newline
    # And capture until "ACM Classification" or "Introduction"
    
    # Regex: `(author keywords|keywords)\s*[:\n](.*?)(acm classification|introduction)`
    match = re.search(r'(author keywords|keywords)\s*[:\n\r]+(.*?)(acm classification|introduction)', text, re.DOTALL)
    
    is_food = False
    if match:
        extracted = match.group(2)
        # Check if 'food' in extracted
        if 'food' in extracted:
            is_food = True
            # print(f"Found food in keywords for: {title}")
    
    if is_food:
        food_papers.append(title)
    
    if 'food' in text:
        potential_food_papers.append(title)

# Compute citations
total_citations = 0
for cit in citations:
    if cit['title'] in food_papers:
        c = cit['citation_count']
        if isinstance(c, str):
            c = int(c) if c.strip() else 0
        total_citations += c

print("__RESULT__:")
print(json.dumps({
    "total_citations": total_citations, 
    "food_papers_count": len(food_papers), 
    "food_papers": food_papers,
    "potential_food_papers_count": len(potential_food_papers),
    "potential_food_papers": potential_food_papers
}))"""

env_args = {'var_function-call-853909438841445340': 'file_storage/function-call-853909438841445340.json', 'var_function-call-1978902813264061650': 'file_storage/function-call-1978902813264061650.json', 'var_function-call-99245770254800995': 'file_storage/function-call-99245770254800995.json', 'var_function-call-5874155478376628757': 'file_storage/function-call-5874155478376628757.json', 'var_function-call-1098255190598746852': {'total_citations': 0, 'food_papers': []}, 'var_function-call-17104759845065888599': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'keyword_snippet': 'Keywords \nLived Informatics; Personal Informatics; Self-Tracking; \nLapsing; Physical Activity; Finances; Location. \n\nACM Classification Keywords \nH.5.m. Information interfaces and presentation (e.g., '}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'keyword_snippet': 'Keywords \nPersonal informatics, collection, reflection, model, barriers \n\nACM Classification Keywords \nH5.m.  Information  interfaces  and  presentation  (e.g.,  HCI): \nMiscellaneous.  \n\nGeneral Terms'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'keyword_snippet': 'Keywords\nH.5.1. Information interfaces and presentation (e.g., HCI):\nAnimations.\n\nAuthor Keywords\nPersonalization; animation; emotion; engagement; empathy;\nself-reﬂection.\n\nINTRODUCTION\nThe developmen'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'keyword_snippet': 'KEYWORDS \nMobile  Health  Applications;  Assistive  Technology;  Co-Design; \nInterviews; Usability; Overactive Bladder \n\nACM Reference format: \n\nAna-Maria  Salai  and  Lynne  Baillie.  2019.  A  Wee  '}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'keyword_snippet': 'Keywords \nWearable technology; dashboard; information visualization; \nstroke rehabilitation; occupational therapy  \n\nACM Classification Keywords \nH.5.m. Information interfaces and presentation (e.g., '}]}

exec(code, env_args)
