code = """import json

result_key = locals()['var_function-call-9298471269662001174']
# It is a list (stringified in the result preview, but in python locals it is the object or path?)
# The execute_python result storage stores the *return value* of the script?
# No, "The result is stored under key...". If it was a file path (large), I load it.
# If it was a short string, it is the string.
# The previous result shows: `The result is: [...]`. This is a JSON string.
# So I need to parse it if I want to use it.
# Wait, "The result is stored under key... The result is: ...".
# If the result was large, it would be a file path.
# The result looks like a JSON string.
# Let's assume it's a string.

data = json.loads(result_key) if isinstance(result_key, str) else result_key
# If it's a list, use it directly.

lines = []
for item in data:
    lines.append(f"Title: {item['title']}, Total Citation Count: {item['total_citation_count']}")

answer = "\n".join(lines)
print("__RESULT__:")
print(json.dumps(answer))"""

env_args = {'var_function-call-224810883549294860': 'file_storage/function-call-224810883549294860.json', 'var_function-call-9456626268790233779': ['paper_docs'], 'var_function-call-16636765420084793523': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-3193368456383189036': 'file_storage/function-call-3193368456383189036.json', 'var_function-call-13531993563476914468': 'file_storage/function-call-13531993563476914468.json', 'var_function-call-13038935966288007214': [], 'var_function-call-12102494195742263056': 'DEBUG', 'var_function-call-11442590404274087377': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'error': 'No valid year > 2016 found', 'years_found': []}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'error': 'No valid year > 2016 found', 'years_found': []}, {'title': 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings', 'error': 'No valid year > 2016 found', 'years_found': []}, {'title': 'Communicating Uncertainty in Fertility Prognosis', 'error': 'No valid year > 2016 found', 'years_found': []}, {'title': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'error': 'No valid year > 2016 found', 'years_found': []}], 'var_function-call-6830701130609361220': {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'text_len': 54376, 'prefix': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard University\nCambridge, MA, USA\neyue@college.harvard.edu\n\nABSTRACT\nSelf-tracking physiological and psychological data poses the\nchallenge of presentation and interpretation. Insightful nar-\nratives for self-', 'chi_2018_index': 2513, 'context': 'CHI 2018, April 21–26, 2018, Montréal, QC, Canada\n© 2018 Copyright held by the owner/author(s). Publ', 'regex_2018_count': 33, 'regex_complex_found': []}, 'var_function-call-9298471269662001174': [{'title': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'total_citation_count': 467}, {'title': 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings', 'total_citation_count': 402}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citation_count': 266}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citation_count': 265}, {'title': 'Communicating Uncertainty in Fertility Prognosis', 'total_citation_count': 264}]}

exec(code, env_args)
