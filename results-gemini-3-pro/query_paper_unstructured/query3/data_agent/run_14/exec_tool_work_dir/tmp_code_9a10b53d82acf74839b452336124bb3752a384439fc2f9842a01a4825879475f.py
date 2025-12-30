code = """import json
import re

with open(locals()['var_function-call-9752705045220679725'], 'r') as f:
    docs = json.load(f)

valid_titles = []

for doc in docs:
    text = doc['text']
    filename = doc['filename']
    title = filename.replace('.txt', '')
    
    # Year Extraction
    header_text = text[:3000]
    years = re.findall(r'20\d{2}', header_text)
    
    year = None
    if years:
        # Take the first year found
        year = int(years[0])
    
    # Contribution Check
    is_empirical = 'empirical' in text.lower()
    
    if year and year > 2016 and is_empirical:
        valid_titles.append(title)

print("__RESULT__:")
print(json.dumps(valid_titles))"""

env_args = {'var_function-call-17324318872041737699': 'file_storage/function-call-17324318872041737699.json', 'var_function-call-7414201362251444319': 'file_storage/function-call-7414201362251444319.json', 'var_function-call-9752705045220679725': 'file_storage/function-call-9752705045220679725.json', 'var_function-call-1938541816739605350': [], 'var_function-call-14592760295992219980': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'source': 'None', 'is_empirical': False, 'first_50_chars': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA"}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': 2010, 'source': 'Copyright', 'is_empirical': False, 'first_50_chars': 'A Stage-Based Model of Personal Informatics System'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'source': 'None', 'is_empirical': True, 'first_50_chars': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpe'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'source': 'None', 'is_empirical': True, 'first_50_chars': 'A Wee Bit More Interaction: Designing and Evaluati'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'source': 'None', 'is_empirical': False, 'first_50_chars': 'ArmSleeve: a Patient Monitoring System to Support '}], 'var_function-call-6994792123040706619': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'all_years_found': ['2015'], 'venue_years_found': [['UBICOMP', '15']], 'has_empirical': False, 'contrib_context': 'contributions  through  survey  design  and  participant  interviews. \nWe  also  thank  Elena  Agapi'}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'all_years_found': ['2010', '2010', '2010'], 'venue_years_found': [], 'has_empirical': False, 'contrib_context': 'contributions  in  this  paper:  1)  we \nidentify  problems  across  personal  informatics  tools,  '}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'all_years_found': ['2018', '2018', '2018'], 'venue_years_found': [], 'has_empirical': True, 'contrib_context': ''}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'all_years_found': ['2019', '2019', '2019', '2019', '2019', '2019', '2019', '2018'], 'venue_years_found': [], 'has_empirical': True, 'contrib_context': 'contribution “I like drawing!” (UP4),  some  did not like \ndrawing: “I don’t like drawing things.” ('}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'all_years_found': ['2016', '2016'], 'venue_years_found': [], 'has_empirical': False, 'contrib_context': 'contribution of this research is \na  system  designed  to  support  the  work  of  occupational \nthe'}]}

exec(code, env_args)
