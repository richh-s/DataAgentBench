code = """import json
import re
import pandas as pd

file_path = locals()['var_function-call-1020461737059661264']

with open(file_path, 'r') as f:
    paper_docs = json.load(f)

physical_activity_papers_data = []

for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    # Check for 'physical activity' domain (case-insensitive) in the entire text
    if 'physical activity' in text.lower():
        physical_activity_papers_data.append({'title': title, 'text': text})

df_physical_activity_papers = pd.DataFrame(physical_activity_papers_data)

# Now, from this subset, filter for papers that contain '2016' as a likely publication year.
# We will assume a year mentioned in the first 1000 characters is a strong indicator of publication year.

papers_titles_2016_physical_activity = []

for index, row in df_physical_activity_papers.iterrows():
    text_snippet = row['text'][:1000] # Check first 1000 characters for publication year
    if re.search(r'\b2016\b', text_snippet):
        papers_titles_2016_physical_activity.append(row['title'])

print('__RESULT__:')
print(json.dumps(papers_titles_2016_physical_activity))"""

env_args = {'var_function-call-10668140555731164678': ['paper_docs'], 'var_function-call-1020461737059661264': 'file_storage/function-call-1020461737059661264.json', 'var_function-call-18293935031113841746': [], 'var_function-call-2347887543621677021': ['Citations', 'sqlite_sequence'], 'var_function-call-13651244775567562643': [], 'var_function-call-8697211431830606780': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'is_physical_activity_domain': True}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'is_physical_activity_domain': True}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'is_physical_activity_domain': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'is_physical_activity_domain': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'is_physical_activity_domain': False}], 'var_function-call-852955902957413167': [], 'var_function-call-14425437229186978218': [], 'var_function-call-781667464626310912': [], 'var_function-call-4561129352538845863': 'file_storage/function-call-4561129352538845863.json', 'var_function-call-13921114947480944330': [], 'var_function-call-14061200294000552431': [], 'var_function-call-8134151316194436233': 'file_storage/function-call-8134151316194436233.json', 'var_function-call-2586611087207286249': [], 'var_function-call-7630030699160760330': [], 'var_function-call-1310384801259058188': [], 'var_function-call-5629838757280383548': [], 'var_function-call-16785956330050197925': ['A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App'], 'var_function-call-17372391694843494030': [], 'var_function-call-15846715091230493913': 'file_storage/function-call-15846715091230493913.json', 'var_function-call-14911253998123745887': [], 'var_function-call-15644150398892477859': [], 'var_function-call-2686761644004723377': [], 'var_function-call-16575195614290340415': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App'], 'var_function-call-6215987539266455397': "SELECT title, SUM(citation_count) as total_citation_count FROM Citations WHERE title IN ('A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App') AND citation_year = 2016 GROUP BY title;", 'var_function-call-9812886162219014160': [], 'var_function-call-2147764625597118371': [], 'var_function-call-1700117408702943789': [], 'var_function-call-14150199598894937422': [], 'var_function-call-16216439507899093977': 'file_storage/function-call-16216439507899093977.json', 'var_function-call-1147605360639443697': [], 'var_function-call-7262839633274923274': [], 'var_function-call-15235621858144890173': []}

exec(code, env_args)
