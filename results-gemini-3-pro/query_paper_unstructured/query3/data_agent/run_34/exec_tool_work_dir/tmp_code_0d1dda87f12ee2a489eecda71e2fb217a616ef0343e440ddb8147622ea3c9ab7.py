code = """import json
import re

papers_file = locals()['var_function-call-13531993563476914468']
with open(papers_file, 'r') as f:
    papers = json.load(f)

debug_out = {}

if papers:
    paper = papers[0]
    text = paper.get('text', '')
    debug_out['title'] = paper.get('filename')
    debug_out['text_len'] = len(text)
    debug_out['prefix'] = text[:500]
    
    # Check specifically for "CHI 2018"
    idx = text.find("CHI 2018")
    debug_out['chi_2018_index'] = idx
    if idx != -1:
        debug_out['context'] = text[idx:idx+100]

    # Test regex
    years = re.findall(r'2018', text)
    debug_out['regex_2018_count'] = len(years)

    years_complex = re.findall(r'\b(20(?:1[7-9]|2[0-4]))\b', text)
    debug_out['regex_complex_found'] = years_complex[:10]

print("__RESULT__:")
print(json.dumps(debug_out))"""

env_args = {'var_function-call-224810883549294860': 'file_storage/function-call-224810883549294860.json', 'var_function-call-9456626268790233779': ['paper_docs'], 'var_function-call-16636765420084793523': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-3193368456383189036': 'file_storage/function-call-3193368456383189036.json', 'var_function-call-13531993563476914468': 'file_storage/function-call-13531993563476914468.json', 'var_function-call-13038935966288007214': [], 'var_function-call-12102494195742263056': 'DEBUG', 'var_function-call-11442590404274087377': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'error': 'No valid year > 2016 found', 'years_found': []}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'error': 'No valid year > 2016 found', 'years_found': []}, {'title': 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings', 'error': 'No valid year > 2016 found', 'years_found': []}, {'title': 'Communicating Uncertainty in Fertility Prognosis', 'error': 'No valid year > 2016 found', 'years_found': []}, {'title': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'error': 'No valid year > 2016 found', 'years_found': []}]}

exec(code, env_args)
