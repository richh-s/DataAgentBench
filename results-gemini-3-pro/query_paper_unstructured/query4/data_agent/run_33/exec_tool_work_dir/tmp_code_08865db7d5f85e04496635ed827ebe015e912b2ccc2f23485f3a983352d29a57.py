code = """import json

file_path = locals()['var_function-call-16576350255932723074']
with open(file_path, 'r') as f:
    papers = json.load(f)

target_titles = [
    "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization",
    "Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers",
    "Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace",
    "Technologies for Everyday Life Reflection: Illustrating a Design Space"
]

verification = {}

for p in papers:
    title = p.get('filename', '').replace('.txt', '')
    if title in target_titles:
        text_start = p.get('text', '')[:500]
        verification[title] = text_start

print("__RESULT__:")
print(json.dumps(verification))"""

env_args = {'var_function-call-2366143788913111129': ['paper_docs'], 'var_function-call-2366143788913114632': ['Citations', 'sqlite_sequence'], 'var_function-call-17599226762723281444': 'file_storage/function-call-17599226762723281444.json', 'var_function-call-11399838663012174565': 'file_storage/function-call-11399838663012174565.json', 'var_function-call-6378129950907540898': [], 'var_function-call-1573942914296370840': 'Debug Info Printed', 'var_function-call-12636404193079087539': {'total_papers': 5, 'first_paper_filename': 'A Lived Informatics Model of Personal Informatics.txt', 'first_paper_text_start': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.wash", 'pa_count': 4, 'y2016_count': 1, 'intersection_count': 0}, 'var_function-call-16576350255932723074': 'file_storage/function-call-16576350255932723074.json', 'var_function-call-3332750741001965095': ["Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace', 'Technologies for Everyday Life Reflection: Illustrating a Design Space'], 'var_function-call-13806221942076467329': "SELECT title, SUM(citation_count) as total_citations FROM Citations WHERE title IN ('Closing the Gap: Supporting Patients'' Transition to Self-Management After Hospitalization', 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace', 'Technologies for Everyday Life Reflection: Illustrating a Design Space') GROUP BY title", 'var_function-call-17669195039183897572': [{'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'total_citations': '466'}, {'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'total_citations': '349'}, {'title': 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace', 'total_citations': '434'}, {'title': 'Technologies for Everyday Life Reflection: Illustrating a Design Space', 'total_citations': '358'}]}

exec(code, env_args)
