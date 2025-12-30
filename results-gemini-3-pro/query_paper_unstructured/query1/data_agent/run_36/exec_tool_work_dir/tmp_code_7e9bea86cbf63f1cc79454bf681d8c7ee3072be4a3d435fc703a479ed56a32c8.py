code = """import json

with open(locals()['var_function-call-13014987171249504047'], 'r') as f:
    papers = json.load(f)

titles_with_food_text = []
titles_with_food_title = []

for p in papers:
    text = p.get('text', '').lower()
    filename = p.get('filename', '')
    if 'food' in filename.lower():
        titles_with_food_title.append(filename)
    if 'food' in text:
        titles_with_food_text.append(filename)

print("__RESULT__:")
print(json.dumps({"titles_with_food_in_filename": titles_with_food_title, "count_food_in_text": len(titles_with_food_text), "sample_food_text_titles": titles_with_food_text[:10]}))"""

env_args = {'var_function-call-11340871341150089119': ['paper_docs'], 'var_function-call-11340871341150087996': ['Citations', 'sqlite_sequence'], 'var_function-call-6885705562055430499': 'file_storage/function-call-6885705562055430499.json', 'var_function-call-6885705562055430382': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-2249233586870449944': 'file_storage/function-call-2249233586870449944.json', 'var_function-call-13014987171249504047': 'file_storage/function-call-13014987171249504047.json', 'var_function-call-13014987171249501074': 'file_storage/function-call-13014987171249501074.json', 'var_function-call-1951529117087221933': 0, 'var_function-call-5778143031438185739': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'has_food_in_text': True, 'keyword_matches': 2, 'snippets': ['author keywords \nlived informatics; personal informatics; self-tracking; \nlapsing; physical activity; finances; location. \n\nacm classification keywords \nh.5.m. information interfaces and presentation ', 'keywords \nh.5.m. information interfaces and presentation (e.g., hci). \n\nintroduction \npersonal informatics, or collecting and reflecting on personal \ninformation,  has  become  increasingly  prevalent']}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'has_food_in_text': True, 'keyword_matches': 2, 'snippets': ['author keywords \npersonal informatics, collection, reflection, model, barriers \n\nacm classification keywords \nh5.m.  information  interfaces  and  presentation  (e.g.,  hci): \nmiscellaneous.  \n\ngenera', 'keywords \nh5.m.  information  interfaces  and  presentation  (e.g.,  hci): \nmiscellaneous.  \n\ngeneral terms \ndesign, human factors \n\nintroduction and motivation \nthe  importance  of  knowing  oneself ']}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'has_food_in_text': True, 'keyword_matches': 1, 'snippets': ['keywords \nmobile  health  applications;  assistive  technology;  co-design; \ninterviews; usability; overactive bladder \n\nacm reference format: \n\nana-maria  salai  and  lynne  baillie.  2019.  a  wee  ']}]}

exec(code, env_args)
