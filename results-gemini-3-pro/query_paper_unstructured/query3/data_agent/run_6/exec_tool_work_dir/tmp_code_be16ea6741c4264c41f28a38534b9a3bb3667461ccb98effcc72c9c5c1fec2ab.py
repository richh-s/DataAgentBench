code = """import json
import re
import pandas as pd

# Load papers
with open(locals()['var_function-call-6644090029617197834'], 'r') as f:
    papers = json.load(f)

print(f"Total papers: {len(papers)}")

# Load citations
with open(locals()['var_function-call-9482827288994490825'], 'r') as f:
    citations_data = json.load(f)
citations_df = pd.DataFrame(citations_data)
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])

matching_papers = []
debug_failures = []

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Extract Year
    years = re.findall(r'20\d\d', text[:2000])
    valid_years = [int(y) for y in years if 2000 <= int(y) <= 2030]
    
    year = valid_years[0] if valid_years else 0
    
    # Check empirical
    is_empirical = 'empirical' in text.lower()
    
    if year == 0:
        debug_failures.append({"title": title, "snippet": text[:200]})
        
    if year > 2016 and is_empirical:
        matching_papers.append(title)

# Filter citations
filtered_citations = citations_df[citations_df['title'].isin(matching_papers)]
final_stats = filtered_citations.groupby('title')['citation_count'].sum().reset_index()
output = final_stats.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(output))
print("__DEBUG__:")
print(json.dumps(debug_failures))"""

env_args = {'var_function-call-16968373354653802012': 'file_storage/function-call-16968373354653802012.json', 'var_function-call-12820784951702258902': ['paper_docs'], 'var_function-call-12820784951702258801': [{'cid': '0', 'name': 'id', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '1'}, {'cid': '1', 'name': 'title', 'type': 'TEXT', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'citation_count', 'type': 'INTEGER', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'citation_year', 'type': 'INTEGER', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-15186585176547387853': 'file_storage/function-call-15186585176547387853.json', 'var_function-call-9482827288994489608': 'file_storage/function-call-9482827288994489608.json', 'var_function-call-9482827288994490825': 'file_storage/function-call-9482827288994490825.json', 'var_function-call-9811688043533249505': [], 'var_function-call-6165134770704943783': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'year': None, 'is_empirical': False}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'year': None, 'is_empirical': False}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'year': None, 'is_empirical': True}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'year': None, 'is_empirical': True}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'year': None, 'is_empirical': False}], 'var_function-call-18017037742468947379': {'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'match': '2015', 'first_500': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characteriz"}, 'var_function-call-12774794714977033763': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': 266}], 'var_function-call-438412191688867448': [{'t': 'A Lived Informatics ', 'y': 2015, 'e': False}, {'t': 'A Stage-based Model ', 'y': 0, 'e': False}, {'t': 'A Trip to the Moon: ', 'y': 0, 'e': True}, {'t': 'A Wee Bit More Inter', 'y': 2019, 'e': True}, {'t': 'ArmSleeve: A Patient', 'y': 0, 'e': False}], 'var_function-call-6644090029617197834': 'file_storage/function-call-6644090029617197834.json'}

exec(code, env_args)
