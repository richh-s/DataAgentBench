code = """import json
import re

# Load papers
with open(locals()['var_function-call-12774124181016147194'], 'r') as f:
    papers_data = json.load(f)

# Titles of interest
titles_of_interest = [
    "A Lived Informatics Model of Personal Informatics.txt",
    "A Stage-based Model of Personal Informatics Systems.txt",
    "A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt"
]

debug_info = []

for p in papers_data:
    if p['filename'] in titles_of_interest:
        info = "--- File: " + p['filename'] + " ---"
        text_lower = p['text'].lower()
        
        # Find "Keywords" or "Index Terms"
        match = re.search(r'(author keywords|keywords|index terms)', text_lower)
        if match:
            start_idx = match.start()
            end_idx = min(len(p['text']), start_idx + 300)
            keywords_text = p['text'][start_idx:end_idx].replace(chr(10), ' ')
            info += " Keywords Section: " + keywords_text
        else:
            info += " NO KEYWORDS FOUND"
        
        debug_info.append(info)

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-2229407460365091455': 'file_storage/function-call-2229407460365091455.json', 'var_function-call-12774124181016146207': 'file_storage/function-call-12774124181016146207.json', 'var_function-call-12774124181016147194': 'file_storage/function-call-12774124181016147194.json', 'var_function-call-12375458960310420055': '0', 'var_function-call-10051261772612968329': 'done', 'var_function-call-10959694939226740713': {'count': 3, 'examples': ['--- Match in: A Lived Informatics Model of Personal Informatics.txt --- Context: ...r  tracking  location  [24,30],  finances  [20],  food  [11],  weight  [19,25],  and  physical  acti...', '--- Match in: A Stage-based Model of Personal Informatics Systems.txt --- Context: ...projects  on  her  personal  behavior,  such  as  food  consumption  and  sneezes  (http://ellieharr...', '--- Match in: A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt --- Context: ...sist  of  avoiding  bladder  irritants  (certain  food  and  drinks)  and  consuming  a  proper  amo...']}}

exec(code, env_args)
