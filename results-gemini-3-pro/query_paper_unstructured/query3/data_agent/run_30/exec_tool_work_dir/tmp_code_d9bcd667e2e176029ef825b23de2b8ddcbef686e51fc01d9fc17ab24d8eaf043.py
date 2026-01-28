code = """import json
import re
import pandas as pd

# Load citations
with open(locals()['var_function-call-6020655889257574954'], 'r') as f:
    citations_data = json.load(f)
df_citations = pd.DataFrame(citations_data)
# Convert citation_count to numeric
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'])

# Load papers
with open(locals()['var_function-call-12945244942482490428'], 'r') as f:
    papers = json.load(f)

debug_list = []
matching_titles = []

for p in papers:
    title = p['filename'].replace('.txt', '')
    text = p['text']
    
    # Extract year
    header_text = text[:1000]
    years = re.findall(r'20\d{2}', header_text)
    published_year = int(years[0]) if years else None
    
    # Check contribution
    is_empirical = "empirical" in text.lower()
    
    debug_list.append({
        "title": title,
        "year": published_year,
        "is_empirical": is_empirical
    })
    
    if published_year and published_year > 2016 and is_empirical:
        matching_titles.append(title)

# Compute sums
df_matching = df_citations[df_citations['title'].isin(matching_titles)]
result_df = df_matching.groupby('title')['citation_count'].sum().reset_index()

print("__RESULT__:")
print(json.dumps({
    "matches": result_df.to_dict(orient='records'),
    "debug": debug_list
}))"""

env_args = {'var_function-call-12710699781919047137': 'file_storage/function-call-12710699781919047137.json', 'var_function-call-4291090424664498879': ['paper_docs'], 'var_function-call-15848114717037089156': [{'cid': '0', 'name': 'id', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '1'}, {'cid': '1', 'name': 'title', 'type': 'TEXT', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'citation_count', 'type': 'INTEGER', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'citation_year', 'type': 'INTEGER', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-6799070853489164674': 'file_storage/function-call-6799070853489164674.json', 'var_function-call-17861381846449372899': [], 'var_function-call-2694959544840446415': 'file_storage/function-call-2694959544840446415.json', 'var_function-call-8715248679689147439': 'file_storage/function-call-8715248679689147439.json', 'var_function-call-411178734668789802': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'contribution_contexts': ['rdi,  Megan  Taylor,  and  Frank  Xu  for  their  contributions  through  survey  design  and  parti'], 'empirical_contexts': []}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'contribution_contexts': ['informatics systems.    We  provide  three  main  contributions  in  this  paper:  1)  we  identify '], 'empirical_contexts': []}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'contribution_contexts': [], 'empirical_contexts': ['cal effects on the user.  SYSTEM OVERVIEW Several empirical principles in animated ﬁlm making provid']}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'contribution_contexts': [' although  some  UPs  were  pleased  with  their  contribution “I like drawing!” (UP4),  some  did n'], 'empirical_contexts': ['  T.  Kortum  and  James  T.  Miller.  2008.  An  Empirical  Evaluation  of  the  System  Usability ', ' Susanna  Raj.  2018.  Circles  vs.  scales:  an  empirical  evaluation  of  emotional assessment GU']}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'contribution_contexts': ['s  focus  on  the  patient is important, the main contribution of this research is  a  system  desig', 'atients’ activities outside therapy.   A  second  contribution  is  offered  through  the  design  o'], 'empirical_contexts': []}], 'var_function-call-15082852831104243869': ['Citations', 'sqlite_sequence'], 'var_function-call-12945244942482490428': 'file_storage/function-call-12945244942482490428.json', 'var_function-call-6020655889257574954': 'file_storage/function-call-6020655889257574954.json', 'var_function-call-14298331136714285140': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '164911713881'}]}

exec(code, env_args)
