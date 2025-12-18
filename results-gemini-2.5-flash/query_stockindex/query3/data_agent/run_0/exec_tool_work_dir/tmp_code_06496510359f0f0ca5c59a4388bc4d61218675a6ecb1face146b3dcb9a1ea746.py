code = """import json
import pandas as pd

top_indices_returns = json.loads(locals()['var_function-call-17924491885778729575'])

index_to_country = {
    'IXIC': 'United States',
    '399001.SZ': 'China',
    'GDAXI': 'Germany',
    'TWII': 'Taiwan',
    'NSEI': 'India'
}

answer_lines = ["The 5 indices with the highest overall returns since 2000, with regular monthly investments, are:"]
for item in top_indices_returns:
    index_symbol = item['Index']
    country = index_to_country.get(index_symbol, 'Unknown')
    line = "- " + index_symbol + " (" + country + "): " + str(round(item['Return'], 2))
    answer_lines.append(line)

final_answer = '\n'.join(answer_lines)

print('__RESULT__:')
print(json.dumps(final_answer))"""

env_args = {'var_function-call-14095839042875052654': 'file_storage/function-call-14095839042875052654.json', 'var_function-call-17924491885778729575': [{'Index': 'IXIC', 'Return': 3.786263717408535}, {'Index': '399001.SZ', 'Return': 1.347928823154433}, {'Index': 'GDAXI', 'Return': 1.3201203421480523}, {'Index': 'TWII', 'Return': 1.317355739060972}, {'Index': 'NSEI', 'Return': 1.2123905368580012}]}

exec(code, env_args)
