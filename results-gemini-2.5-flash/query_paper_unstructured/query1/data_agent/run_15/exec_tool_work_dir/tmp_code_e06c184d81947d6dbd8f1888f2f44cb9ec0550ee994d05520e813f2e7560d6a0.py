code = """import json

citations_data = locals()['var_function-call-3824548333393067635']
total_citations = 0
for record in citations_data:
    total_citations += int(record['citation_count'])

print('__RESULT__:')
print(json.dumps(total_citations))"""

env_args = {'var_function-call-9698453009794764230': ['paper_docs'], 'var_function-call-11805892907595172719': [], 'var_function-call-7332118063498685844': 'file_storage/function-call-7332118063498685844.json', 'var_function-call-16620644718995955947': [], 'var_function-call-12548844503119020539': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App'], 'var_function-call-3824548333393067635': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '49'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '11'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '71'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '38'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '81'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '77'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '9'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '50'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '49'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '77'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '60'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '68'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'citation_count': '88'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'citation_count': '32'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'citation_count': '86'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'citation_count': '14'}]}

exec(code, env_args)
