code = """import json
import re
import pandas as pd

with open(locals()['var_function-call-12792815428648479832'], 'r') as f:
    paper_docs = json.load(f)

with open(locals()['var_function-call-15343514597715386657'], 'r') as f:
    citations_data = json.load(f)

df_citations = pd.DataFrame(citations_data)
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'])

target_titles = []

for doc in paper_docs:
    text = doc['text']
    filename = doc['filename']
    title = filename.replace('.txt', '')
    
    # Extract Year
    # Find first 20XX in first 3000 chars
    header_text = text[:3000]
    years = re.findall(r'20[0-9]{2}', header_text)
    
    pub_year = 0
    if years:
        # Take the first one
        pub_year = int(years[0])
    
    # Check empirical
    is_empirical = "empirical" in text.lower()
    
    if pub_year > 2016 and is_empirical:
        target_titles.append(title)

# Filter citations
matched_citations = df_citations[df_citations['title'].isin(target_titles)]

# Group by title
result_df = matched_citations.groupby('title')['citation_count'].sum().reset_index()

# Sort by title or citations? No specific order requested.
result_list = result_df.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result_list))"""

env_args = {'var_function-call-9689432006532158130': 'file_storage/function-call-9689432006532158130.json', 'var_function-call-7106794807816664619': 'file_storage/function-call-7106794807816664619.json', 'var_function-call-12792815428648479832': 'file_storage/function-call-12792815428648479832.json', 'var_function-call-15343514597715386657': 'file_storage/function-call-15343514597715386657.json', 'var_function-call-16410926222375514887': [], 'var_function-call-17506932778829537594': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'years': [], 'has_empirical': False, 'snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN  A Lived Informatics Model of Personal Informatics  "}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'years': [], 'has_empirical': False, 'snippet': 'A Stage-Based Model of Personal Informatics Systems  Ian Li1, Anind Dey1, and Jodi Forlizzi1,2  1Hum'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'years': [], 'has_empirical': True, 'snippet': 'Fengjiao Peng MIT Media Lab Cambridge, MA, USA fpeng@mit.edu  A Trip to the Moon: Personalized Anima'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'years': [], 'has_empirical': True, 'snippet': 'A Wee Bit More Interaction: Designing and Evaluating   an Overactive Bladder App  Ana-Maria Salai   '}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'years': [], 'has_empirical': False, 'snippet': 'ArmSleeve: a Patient Monitoring System to Support  Occupational Therapists in Stroke Rehabilitation '}], 'var_function-call-14463308120016227623': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'found_years': ['2015'], 'snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN  A"}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'found_years': [], 'snippet': 'A Stage-Based Model of Personal Informatics System'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'found_years': [], 'snippet': 'Fengjiao Peng MIT Media Lab Cambridge, MA, USA fpe'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'found_years': [], 'snippet': 'A Wee Bit More Interaction: Designing and Evaluati'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'found_years': [], 'snippet': 'ArmSleeve: a Patient Monitoring System to Support '}], 'var_function-call-11334381408533130884': {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'text_preview': 'A Wee Bit More Interaction: Designing and Evaluating   an Overactive Bladder App  Ana-Maria Salai   Heriot-Watt University   Edinburgh, UK   as152@hw.ac.uk   Lynne Baillie   Heriot-Watt University   Edinburgh, UK   l.baillie@hw.ac.uk  ABSTRACT   Overactive  Bladder  (OAB)  is  a  widespread  condition,  affecting  20%  of  the  population.  Even  though  it  is  a  treatable  condition,  people  often  do  not  seek  treatment.  In  this paper, we  describe how we co-designed and evaluated  with  30  stakeholders  (9  medical  professionals  and  21  end- users)  an  OAB  mobile  health  application  that  aims  to  increase  adherence  to  self-managed  treatment.  Our  results  support previous research that visualizing progress, setting  goals, receiving reminders and feedback  increases  use.  We  discovered  that  games  could  be  used  successfully  as  a  distraction technique for urge suppression. Contrary to the  current research direction, automatically calculated features  could  be  a  detriment  to  app  interaction.  Regarding  evaluation,  we  found  that  designers  may  not  want  to  rely  only  on  questionnaires  when  assessing  the  success  of  a  game and its emotional impact on users.   CCS CONCEPTS  • Human-centered  computing  ~  User  studies;  Usability  Testing;  Field Studies   KEYWORDS  Mobile  Health  Applications;  Assistive  Technology;  Co-Design;  Interviews; Usability; Overactive Bladder   ACM Reference format:   Ana-Maria  Salai  and  Lynne  Baillie.  2019.  A  Wee  Bit  More  Interaction:  Designing  and  Evaluating  an  Overactive  Bladder  App.  In  2019  CHI  Conference on Human Factors in Computing Systems Proceedings (CHI 2019),  May 4–9, 2019, Glagsow, Scotland, UK. ACM,  NY,  NY,  USA.  Paper  703,  13  pages. https://doi.org/10.1145/3290605.3300933   Permission to make digital or hard copies of all or part of this work for personal or  classroom use is granted without fee provided that copies are not made or distribut'}}

exec(code, env_args)
