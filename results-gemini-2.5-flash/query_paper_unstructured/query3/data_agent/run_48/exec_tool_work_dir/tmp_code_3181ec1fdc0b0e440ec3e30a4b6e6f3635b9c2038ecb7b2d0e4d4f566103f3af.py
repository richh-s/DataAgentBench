code = """import json
import re

paper_docs_data = json.load(open(locals()['var_function-call-558217748425387803'], 'r'))

extracted_papers_info = []

for doc in paper_docs_data:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    year = None
    year_match = re.search(r'(19|20)\d{2}', text)
    if year_match:
        year = int(year_match.group(0))

    is_empirical = 'empirical' in text.lower()

    if year is not None and year > 2016 and is_empirical:
        extracted_papers_info.append({
            'title': title,
            'year': year,
            'contribution': 'empirical'
        })

print('__RESULT__:')
print(json.dumps(extracted_papers_info))"""

env_args = {'var_function-call-11120416126101380269': ['paper_docs'], 'var_function-call-558217748425387803': 'file_storage/function-call-558217748425387803.json', 'var_function-call-18112218132182732411': [], 'var_function-call-6036035642582270495': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'contribution': ''}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'contribution': ''}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'contribution': ''}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'contribution': ''}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'contribution': ''}]}

exec(code, env_args)
