code = """import json
import re

papers_path = locals()['var_function-call-10894468654798374866']
with open(papers_path, 'r') as f:
    papers_data = json.load(f)

print("Debugging first 10 papers:")
for i, paper in enumerate(papers_data[:10]):
    filename = paper.get('filename', '')
    title = filename[:-4]
    text = paper.get('text', '')
    
    header_text = text[:2000]
    years = re.findall(r"20[12]\d", header_text)
    
    is_empirical = "empirical" in text[:10000].lower()
    
    print(f"{i}. Title: {title}")
    print(f"   Found Years: {years}")
    print(f"   Is Empirical: {is_empirical}")
    print("-" * 20)

print("__RESULT__:")
print(json.dumps("Debug Complete"))"""

env_args = {'var_function-call-5623558947517056704': 'file_storage/function-call-5623558947517056704.json', 'var_function-call-4507795440507618758': 'file_storage/function-call-4507795440507618758.json', 'var_function-call-10894468654798374866': 'file_storage/function-call-10894468654798374866.json', 'var_function-call-7275202975009130922': []}

exec(code, env_args)
