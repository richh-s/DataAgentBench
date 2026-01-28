code = """import json
import pandas as pd

# load previous result
res = var_call_G2qdEz0Mb6MmTaAdUbh8pGMP
if isinstance(res, str):
    res = json.loads(res)

# Print final in required format
print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_call_ahqwjozL6QvTYIUbXXnyJbvi': ['packageinfo'], 'var_call_O8NNkifflCK49r0SEgUGADGt': ['project_info', 'project_packageversion'], 'var_call_LexZ7D9ewAeYv1w6hl4D1ztH': 'file_storage/call_LexZ7D9ewAeYv1w6hl4D1ztH.json', 'var_call_VjHaCoRgGUMmcX1y4bYGiHth': 'file_storage/call_VjHaCoRgGUMmcX1y4bYGiHth.json', 'var_call_aCZiCOiYfZLSIq0xIXC8zUkd': 'file_storage/call_aCZiCOiYfZLSIq0xIXC8zUkd.json', 'var_call_G2qdEz0Mb6MmTaAdUbh8pGMP': [{'Package': '@dylanvann/svelte', 'Version': '3.25.4', 'ProjectName': 'sveltejs/svelte', 'Stars': 73499}, {'Package': '@dumc11/tailwindcss', 'Version': '0.4.0', 'ProjectName': 'tailwindcss/tailwindcss', 'Stars': 73464}, {'Package': '@dman777/shadow-dom-quill-temp', 'Version': '1.0.0', 'ProjectName': 'quilljs/quill', 'Stars': 42407}, {'Package': '@dynasty/styled-components', 'Version': '3.2.1', 'ProjectName': 'styled-components/styled-components', 'Stars': 39660}, {'Package': '@dothq/styled-components', 'Version': '1.0.0', 'ProjectName': 'styled-components/styled-components', 'Stars': 39660}]}

exec(code, env_args)
