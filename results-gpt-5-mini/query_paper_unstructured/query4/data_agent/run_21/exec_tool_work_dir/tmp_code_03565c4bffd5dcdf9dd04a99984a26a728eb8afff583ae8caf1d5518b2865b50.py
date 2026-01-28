code = """import json
# Load the citation query result
citations = var_call_S8MH1IUX0zVxr1R5XrCYC1Hw
# Load the extracted paper list
papers = var_call_fZvdQPPcrrlhJTh9MjWiXR8D

# Build mapping from title to total citations
cit_map = {c['title']: int(c['total_citations']) for c in citations}

output = []
for p in papers:
    title = p['title']
    total = cit_map.get(title, 0)
    output.append({'title': title, 'total_citations': total})

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_ljFqEPHt3JaolG63Bbs4op2U': 'file_storage/call_ljFqEPHt3JaolG63Bbs4op2U.json', 'var_call_fZvdQPPcrrlhJTh9MjWiXR8D': [{'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'filename': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers.txt'}, {'title': 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace', 'filename': 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace.txt'}, {'title': 'Technologies for Everyday Life Reflection: Illustrating a Design Space', 'filename': 'Technologies for Everyday Life Reflection: Illustrating a Design Space.txt'}], 'var_call_S8MH1IUX0zVxr1R5XrCYC1Hw': [{'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'total_citations': '349'}, {'title': 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace', 'total_citations': '434'}, {'title': 'Technologies for Everyday Life Reflection: Illustrating a Design Space', 'total_citations': '358'}]}

exec(code, env_args)
