code = """import json
import pandas as pd

citations_path = locals()['var_function-call-13231219773529852876']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)
df_citations = pd.DataFrame(citations_data)

paper_title = "Barriers and Negative Nudges: Exploring Challenges in Food Journaling"
citations = df_citations[df_citations['title'] == paper_title]

print("__RESULT__:")
print(json.dumps(citations.to_dict(orient='records')))"""

env_args = {'var_function-call-2303008597307440717': 'file_storage/function-call-2303008597307440717.json', 'var_function-call-13231219773529852876': 'file_storage/function-call-13231219773529852876.json', 'var_function-call-1470986514462479797': 'file_storage/function-call-1470986514462479797.json', 'var_function-call-2063711702066525845': 270, 'var_function-call-16517891764845827685': ['Barriers and Negative Nudges: Exploring Challenges in Food Journaling'], 'var_function-call-17873304284800706501': [{'title': 'A Lived Informatics Model of Personal Informatics', 'context': 'food  [11],  weight  [19,25], \nand  physical  activity  [16,34]  and  to  develop  research \nprototy'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'context': 'food  consumption  and  sneezes  (http://ellieharrison.com). \nThese  are  extreme  examples,  but  r'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'context': 'food  and  drinks)  and  consuming  a  proper  amount \nof liquid per day. The PFM training consists '}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'context': 'food journals [5,6]: “I got behind on \nkeeping up with it and couldn’t find the time to start back u'}]}

exec(code, env_args)
