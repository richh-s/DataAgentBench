code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-3568411121950664652'], 'r') as f:
    papers = json.load(f)

with open(locals()['var_function-call-13014987171249501074'], 'r') as f:
    citations = json.load(f)

df_citations = pd.DataFrame(citations)
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'])

food_papers = []
debug_matches = []

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    text_lower = text.lower()
    
    # Check for keywords sections
    # Regex: Look for "author keywords" or "keywords" or "index terms"
    # followed by text.
    # We'll grab the next 500 chars.
    
    keyword_indices = [m.start() for m in re.finditer(r'(author\s+)?keywords|index\s+terms', text_lower)]
    
    is_food = False
    if keyword_indices:
        for idx in keyword_indices:
            snippet = text_lower[idx:idx+500]
            if 'food' in snippet:
                is_food = True
                debug_matches.append({"title": title, "snippet_preview": snippet[:100]})
                break
    
    if is_food:
        food_papers.append(title)

# Filter citations
food_citations = df_citations[df_citations['title'].isin(food_papers)]
total_citations = int(food_citations['citation_count'].sum())

print("__RESULT__:")
print(json.dumps({
    "count_food_papers": len(food_papers),
    "total_citations": total_citations,
    "sample_titles": food_papers[:5]
}))"""

env_args = {'var_function-call-11340871341150089119': ['paper_docs'], 'var_function-call-11340871341150087996': ['Citations', 'sqlite_sequence'], 'var_function-call-6885705562055430499': 'file_storage/function-call-6885705562055430499.json', 'var_function-call-6885705562055430382': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-2249233586870449944': 'file_storage/function-call-2249233586870449944.json', 'var_function-call-13014987171249504047': 'file_storage/function-call-13014987171249504047.json', 'var_function-call-13014987171249501074': 'file_storage/function-call-13014987171249501074.json', 'var_function-call-1951529117087221933': 0, 'var_function-call-5778143031438185739': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'has_food_in_text': True, 'keyword_matches': 2, 'snippets': ['author keywords \nlived informatics; personal informatics; self-tracking; \nlapsing; physical activity; finances; location. \n\nacm classification keywords \nh.5.m. information interfaces and presentation ', 'keywords \nh.5.m. information interfaces and presentation (e.g., hci). \n\nintroduction \npersonal informatics, or collecting and reflecting on personal \ninformation,  has  become  increasingly  prevalent']}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'has_food_in_text': True, 'keyword_matches': 2, 'snippets': ['author keywords \npersonal informatics, collection, reflection, model, barriers \n\nacm classification keywords \nh5.m.  information  interfaces  and  presentation  (e.g.,  hci): \nmiscellaneous.  \n\ngenera', 'keywords \nh5.m.  information  interfaces  and  presentation  (e.g.,  hci): \nmiscellaneous.  \n\ngeneral terms \ndesign, human factors \n\nintroduction and motivation \nthe  importance  of  knowing  oneself ']}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'has_food_in_text': True, 'keyword_matches': 1, 'snippets': ['keywords \nmobile  health  applications;  assistive  technology;  co-design; \ninterviews; usability; overactive bladder \n\nacm reference format: \n\nana-maria  salai  and  lynne  baillie.  2019.  a  wee  ']}], 'var_function-call-8725256020034930623': {'titles_with_food_in_filename': [], 'count_food_in_text': 3, 'sample_food_text_titles': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt']}, 'var_function-call-8568562397093437383': 5, 'var_function-call-3568411121950664652': 'file_storage/function-call-3568411121950664652.json', 'var_function-call-3568411121950664111': 1405}

exec(code, env_args)
