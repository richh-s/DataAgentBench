code = """import json
import re

path = locals()['var_function-call-2585691326327215227']
with open(path, 'r') as f:
    papers = json.load(f)

for p in papers:
    title = p['filename'].replace('.txt', '')
    text = p['text']
    # Extract Author Keywords
    # Usually "Author Keywords" followed by keywords.
    match = re.search(r'Author Keywords\s*(.*?)(?:ACM Classification|INTRODUCTION)', text, re.DOTALL | re.IGNORECASE)
    keywords = match.group(1).strip() if match else "Not found"
    print(f"Title: {title}")
    print(f"Keywords: {keywords}")
    print("-" * 20)

print("__RESULT__:")
print(json.dumps("Done"))"""

env_args = {'var_function-call-13604834933233695573': 'file_storage/function-call-13604834933233695573.json', 'var_function-call-13672825597397015902': 'file_storage/function-call-13672825597397015902.json', 'var_function-call-2585691326327215227': 'file_storage/function-call-2585691326327215227.json', 'var_function-call-4981003287102314854': [], 'var_function-call-13805358010662920095': "SELECT citation_count FROM Citations WHERE title IN ('')", 'var_function-call-2766234641160202705': "SELECT citation_count FROM Citations WHERE title IN ('')", 'var_function-call-10201737980555806332': {'count': 5, 'keys': ['_id', 'filename', 'text'], 'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'text_len': 68339, 'text_preview': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n", 'has_food_substring': True}, 'var_function-call-5911334932760044983': "SELECT citation_count FROM Citations WHERE title IN ('A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use')"}

exec(code, env_args)
