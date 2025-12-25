code = """import json

top_5_indices = locals()['var_function-call-22747974122713311']

# Manually map indices to countries based on general knowledge
index_to_country = {
    "IXIC": "United States",
    "399001.SZ": "China",
    "GDAXI": "Germany",
    "TWII": "Taiwan",
    "NSEI": "India"
}

final_result = []
for item in top_5_indices:
    index_symbol = item['Index']
    country = index_to_country.get(index_symbol, "Unknown") # Default to 'Unknown' if not found
    final_result.append({
        "Index": index_symbol,
        "OverallReturn": item['OverallReturn'],
        "Country": country
    })

answer_string = "The 5 indices with the highest overall returns from monthly investments since 2000 are:\n"
for item in final_result:
    answer_string += f"- {item['Index']} ({item['Country']}): {item['OverallReturn']:.2f}%\n"

print("__RESULT__:")
print(json.dumps(answer_string))"""

env_args = {'var_function-call-14422826081707029859': 'file_storage/function-call-14422826081707029859.json', 'var_function-call-22747974122713311': [{'Index': 'IXIC', 'OverallReturn': 378.59663101868654}, {'Index': '399001.SZ', 'OverallReturn': 134.4545336356674}, {'Index': 'GDAXI', 'OverallReturn': 131.93527211722625}, {'Index': 'TWII', 'OverallReturn': 131.51952869880722}, {'Index': 'NSEI', 'OverallReturn': 121.46893972422373}]}

exec(code, env_args)
