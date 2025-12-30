code = """import json

papers_path = locals()['var_function-call-1470986514462479797']
with open(papers_path, 'r') as f:
    papers_data = json.load(f)

# Check for keyword section variations
variations = ["Author Keywords", "Index Terms", "Keywords"]
results = []

for paper in papers_data:
    if "Barriers and Negative Nudges" in paper['filename']:
        continue
    
    text = paper['text']
    lower_text = text.lower()
    
    found_keywords = ""
    for v in variations:
        idx = lower_text.find(v.lower())
        if idx != -1:
            snippet = text[idx:idx+300] # get original case
            found_keywords = snippet
            break
            
    if found_keywords:
        # Check if 'food' is in there
        if 'food' in found_keywords.lower():
            results.append({"title": paper['filename'], "keywords": found_keywords})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-2303008597307440717': 'file_storage/function-call-2303008597307440717.json', 'var_function-call-13231219773529852876': 'file_storage/function-call-13231219773529852876.json', 'var_function-call-1470986514462479797': 'file_storage/function-call-1470986514462479797.json', 'var_function-call-2063711702066525845': 270, 'var_function-call-16517891764845827685': ['Barriers and Negative Nudges: Exploring Challenges in Food Journaling'], 'var_function-call-17873304284800706501': [{'title': 'A Lived Informatics Model of Personal Informatics', 'context': 'food  [11],  weight  [19,25], \nand  physical  activity  [16,34]  and  to  develop  research \nprototy'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'context': 'food  consumption  and  sneezes  (http://ellieharrison.com). \nThese  are  extreme  examples,  but  r'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'context': 'food  and  drinks)  and  consuming  a  proper  amount \nof liquid per day. The PFM training consists '}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'context': 'food journals [5,6]: “I got behind on \nkeeping up with it and couldn’t find the time to start back u'}], 'var_function-call-14095558794202063105': [{'id': '190', 'title': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'citation_count': '92', 'citation_year': '2016'}, {'id': '191', 'title': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'citation_count': '40', 'citation_year': '2017'}, {'id': '192', 'title': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'citation_count': '52', 'citation_year': '2018'}, {'id': '193', 'title': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'citation_count': '86', 'citation_year': '2019'}]}

exec(code, env_args)
