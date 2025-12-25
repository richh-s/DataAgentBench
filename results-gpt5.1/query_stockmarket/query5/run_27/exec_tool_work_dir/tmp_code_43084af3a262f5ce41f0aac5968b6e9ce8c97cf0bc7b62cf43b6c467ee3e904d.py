code = """import json
from pathlib import Path
obj = json.loads(Path(var_call_iHaMCzuNVB0LBMLDPJO7MFsv).read_text())
print('__RESULT__:')
print(json.dumps(obj['sql']))"""

env_args = {'var_call_IJuRdD3kxGYIhyNBk5CRauep': 'file_storage/call_IJuRdD3kxGYIhyNBk5CRauep.json', 'var_call_gP1IxlZ2zvc6LTNaIgIhhOSQ': 'file_storage/call_gP1IxlZ2zvc6LTNaIgIhhOSQ.json', 'var_call_iHaMCzuNVB0LBMLDPJO7MFsv': 'file_storage/call_iHaMCzuNVB0LBMLDPJO7MFsv.json'}

exec(code, env_args)
