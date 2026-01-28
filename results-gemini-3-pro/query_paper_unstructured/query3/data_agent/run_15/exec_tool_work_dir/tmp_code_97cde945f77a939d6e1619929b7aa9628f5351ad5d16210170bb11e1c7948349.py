code = """import json
import re

file_path = locals()['var_function-call-2573740285369106607']

with open(file_path, 'r') as f:
    docs = json.load(f)

print(f"Total docs: {len(docs)}")

targets = ["A Trip to the Moon: Personalized Animated Movies for Self-reflection", 
           "ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation"]

for doc in docs:
    title = doc['filename'].replace(".txt", "")
    if title in targets:
        text = doc['text']
        print(f"--- {title} ---")
        print(f"Header: {text[:200].replace(chr(10), ' ')}")
        # Check for any numbers
        nums = re.findall(r"\d{4}", text)
        print(f"Years found: {nums[:5]}")
        # Check for empirical keywords
        kw = ["participants", "user study", "interviews", "recruited", "empirical"]
        found = [k for k in kw if k in text.lower()]
        print(f"Keywords: {found}")

print("__RESULT__:")
print("Done")"""

env_args = {'var_function-call-7387203186474718594': 'file_storage/function-call-7387203186474718594.json', 'var_function-call-9551476032774433042': ['paper_docs'], 'var_function-call-7392786003504292061': {'explicit_contribution': '', 'empirical_context': '', 'years': ['2015', '2015', '2015', '2015', '2015', '2015', '2015', '2015', '2014', '2013']}, 'var_function-call-16070472679849682591': 'file_storage/function-call-16070472679849682591.json', 'var_function-call-14838569663088297683': 'file_storage/function-call-14838569663088297683.json', 'var_function-call-2573740285369106607': 'file_storage/function-call-2573740285369106607.json', 'var_function-call-17192200102339754629': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'year': 2015, 'contrib_context': 'contributions  through  survey  design  and  parti', 'has_empirical': False}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'year': None, 'contrib_context': 'contributions  in  this  paper:  1)  we  identify ', 'has_empirical': False}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'year': None, 'contrib_context': '', 'has_empirical': True}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'year': None, 'contrib_context': 'contribution “I like drawing!” (UP4),  some  did n', 'has_empirical': True}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'year': None, 'contrib_context': 'contribution of this research is  a  system  desig', 'has_empirical': False}], 'var_function-call-8037773018140063796': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'header_snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN  A Lived Informatics Model of Personal Informatics  ", 'contribution_snippet': 'contributions  through  survey  design  and  participant  interviews.  We  also  thank  Elena  Agapie,  Elizabeth  Bales,  Lucas  Franco  Colusso, Felicia Cordeiro, and Ravi Karkar for early feedback '}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'header_snippet': 'A Stage-Based Model of Personal Informatics Systems  Ian Li1, Anind Dey1, and Jodi Forlizzi1,2  1Hum', 'contribution_snippet': 'contributions  in  this  paper:  1)  we  identify  problems  across  personal  informatics  tools,  2)  we  introduce and discuss a model that improves the diagnosis,  in  personal  assessment,  and  '}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'header_snippet': 'Fengjiao Peng MIT Media Lab Cambridge, MA, USA fpeng@mit.edu  A Trip to the Moon: Personalized Anima', 'contribution_snippet': ''}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'header_snippet': 'A Wee Bit More Interaction: Designing and Evaluating   an Overactive Bladder App  Ana-Maria Salai   ', 'contribution_snippet': 'contribution “I like drawing!” (UP4),  some  did not like  drawing: “I don’t like drawing things.” (UP9).   3.3  Design Decisions   Based on the design findings from this study, we developed  the  fir'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'header_snippet': 'ArmSleeve: a Patient Monitoring System to Support  Occupational Therapists in Stroke Rehabilitation ', 'contribution_snippet': 'contribution of this research is  a  system  designed  to  support  the  work  of  occupational  therapists.    This  research  describes  the  design  of  the  ArmSleeve  system,  a  patient  monitor'}], 'var_function-call-1979176044345138821': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': 2015, 'is_empirical': True}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'is_empirical': True}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'is_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019, 'is_empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'is_empirical': True}], 'var_function-call-9674629944003180042': {'matches': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'missing_year': ['A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation']}}

exec(code, env_args)
