code = """import json
import re
from collections import defaultdict

# Load the UC patents data
result_file = locals()['var_functions.query_db:6']
if isinstance(result_file, str) and result_file.endswith('.json'):
    with open(result_file, 'r') as f:
        uc_patents = json.load(f)
else:
    uc_patents = result_file

# Extract all cited publication numbers (excluding empty ones and non-patent citations)
cited_publications = []
for patent in uc_patents:
    citation_str = patent.get('citation', '[]')
    if citation_str and citation_str != '[]':
        try:
            citations = json.loads(citation_str)
            for cit in citations:
                pub_num = cit.get('publication_number', '')
                if pub_num and pub_num.strip():
                    cited_publications.append(pub_num)
        except:
            # Try to extract with regex if JSON parsing fails
            pub_nums = re.findall(r'"publication_number"\s*:\s*"([^"]+)"', citation_str)
            for pub_num in pub_nums:
                if pub_num and pub_num.strip() and pub_num != '':
                    cited_publications.append(pub_num)

# Remove duplicates
cited_publications = list(set(cited_publications))

print('__RESULT__:')
print(json.dumps(f"Found {len(cited_publications)} unique cited publication numbers"))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'Found 5 patents from UNIV CALIFORNIA', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:8': 'Found 169 patents assigned to UNIV CALIFORNIA'}

exec(code, env_args)
