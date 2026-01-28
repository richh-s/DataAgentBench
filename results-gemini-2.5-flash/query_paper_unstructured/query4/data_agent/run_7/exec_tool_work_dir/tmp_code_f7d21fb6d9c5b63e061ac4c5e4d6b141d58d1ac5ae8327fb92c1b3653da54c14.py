code = """import json
import pandas as pd

file_path = locals()['var_function-call-82359061990851726']
with open(file_path, 'r') as f:
    full_results = json.load(f)

# Filter for papers published in 2016 and in 'physical activity' domain
filtered_papers = []
for doc in full_results:
    text = doc.get('text', '')
    filename = doc.get('filename', '')

    # Check for '2016' as publication year and 'physical activity' in the text
    # This is a heuristic and might need refinement depending on text structure
    # For now, I'll look for "2016" in the text as a strong indicator of publication year.
    # And "physical activity" as domain.
    if "2016" in text and "physical activity" in text:
        title = filename.replace('.txt', '')
        filtered_papers.append({'title': title})

# Extract titles from the filtered papers
titles = [paper['title'] for paper in filtered_papers]

__RESULT__:
print(json.dumps(titles))"""

env_args = {'var_function-call-894598418542309128': [{'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a870', 'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt'}, {'_id': '694f5530284b10b11dc0a871', 'filename': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt"}, {'_id': '694f5530284b10b11dc0a873', 'filename': 'Charting Design Preferences on Wellness Wearables.txt'}], 'var_function-call-82359061990851726': 'file_storage/function-call-82359061990851726.json'}

exec(code, env_args)
