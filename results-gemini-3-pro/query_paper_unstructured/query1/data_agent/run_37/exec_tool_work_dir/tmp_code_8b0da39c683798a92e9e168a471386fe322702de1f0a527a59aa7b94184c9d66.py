code = """import json
import re

# Load papers
with open(locals()['var_function-call-3345834275723385797'], 'r') as f:
    papers = json.load(f)

# Load citations
with open(locals()['var_function-call-13564221464732274520'], 'r') as f:
    citations = json.load(f)

food_papers_titles = set()

# Regex for title/keywords
# Note: "eating" might be in "meeting", so word boundary is important.
# "food" -> "food"
# "diet" -> "dietary", "diet"
# "nutrition" -> "nutritional"
# So maybe \b is too strict for "diet" (misses dietary).
# But \b is good for "eating" (avoids meeting).
# For "food", \b is good (avoids 'flood'?? unlikely in this context but safe).
# Let's use:
# food.*
# diet.*
# nutrition.*
# \beating\b
regex_pattern = r'\b(food\w*|diet\w*|nutrition\w*|eating)\b'

for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    text = paper.get('text', '')
    
    is_food = False
    
    # Check Title with regex
    if re.search(regex_pattern, title, re.IGNORECASE):
        is_food = True
    
    # Check Keywords if not already found
    if not is_food:
        lower_text = text.lower()
        start_idx = lower_text.find('author keywords')
        if start_idx != -1:
            end_idx = lower_text.find('acm classification keywords', start_idx)
            if end_idx == -1:
                 end_idx = lower_text.find('introduction', start_idx)
            if end_idx == -1:
                 end_idx = start_idx + 1000
            
            keywords_text = lower_text[start_idx:end_idx]
            # Check for 'food' specifically in keywords
            if 'food' in keywords_text: # simple substring in keywords section is usually safe
                is_food = True
    
    if is_food:
        food_papers_titles.add(title)

# Sum citations
total_citations = 0
matched_papers = []

for cit in citations:
    if cit['title'] in food_papers_titles:
        count = int(cit['citation_count'])
        total_citations += count
        matched_papers.append(cit['title'])

# Debug output
print("__RESULT__:")
print(json.dumps({
    "food_papers_count": len(food_papers_titles),
    "matched_citations_records": len(matched_papers),
    "total_citations": total_citations,
    "titles": list(food_papers_titles)
}))"""

env_args = {'var_function-call-18115772371800026671': 'file_storage/function-call-18115772371800026671.json', 'var_function-call-5992210223060542077': 'file_storage/function-call-5992210223060542077.json', 'var_function-call-13564221464732274520': 'file_storage/function-call-13564221464732274520.json', 'var_function-call-7850296922984733998': {'food_papers_count': 0, 'total_citations': 0, 'food_paper_titles': []}, 'var_function-call-6262404583647121035': {'total_papers': 5, 'titles_with_food': [], 'snippets': [{'title': 'A Lived Informatics Model of Personal Informatics', 'snippet': 'o  study  people’s  use  of  commercial  tools  for  tracking \nlocation  [24,30],  finances  [20],  food  [11],  weight  [19,25], \nand  physical  activity  [16,34]  and  to  develop  research \nprototy'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'snippet': 'ron.com), and Ellie Harrison, \nwho  created  art  projects  on  her  personal  behavior,  such  as \nfood  consumption  and  sneezes  (http://ellieharrison.com). \nThese  are  extreme  examples,  but  r'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'snippet': '  bladder  training). \nThe  lifestyle changes  consist  of  avoiding  bladder  irritants \n(certain  food  and  drinks)  and  consuming  a  proper  amount \nof liquid per day. The PFM training consists '}]}, 'var_function-call-9193793314079207812': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-12448764961698084004': 'file_storage/function-call-12448764961698084004.json', 'var_function-call-3345834275723385797': 'file_storage/function-call-3345834275723385797.json'}

exec(code, env_args)
