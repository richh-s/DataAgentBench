code = """import json
import re

file_path = locals()['var_function-call-11980837049529818020']
with open(file_path, 'r') as f:
    data = json.load(f)

# Define sports keywords
# Using a set for faster lookup, but regex is better for boundaries
sports_keywords = [
    "baseball", "basketball", "football", "soccer", "tennis", "hockey", "golf", "rugby", "cricket", "boxing", "wrestling", "athletics", "swimming", "gymnastics",
    "olympics", "olympic", "medal", "gold", "silver", "bronze",
    "nba", "nfl", "mlb", "nhl", "fifa", "uefa", "nascar", "f1", "formula one", "grand prix",
    "wimbledon", "us open", "french open", "australian open",
    "super bowl", "world cup", "championship", "tournament", "playoff", "stanley cup", "world series",
    "quarterback", "touchdown", "homerun", "shutout", "hat-trick",
    "lakers", "bulls", "knicks", "celtics", "yankees", "red sox", "dodgers", "giants", "patriots", "cowboys", "eagles", "packers", "red wings", "maple leafs", "canadiens", "rangers", "real madrid", "barcelona", "manchester united", "chelsea", "arsenal", "liverpool", "ac milan", "juventus", "bayern munich",
    "agassi", "federer", "roddick", "williams", "sharapova", "woods", "mickelson", "armstrong", "schumacher", "phelps", "thorpe", "bryant", "oneal", "duncan", "garnett", "james", "manning", "brady", "vick", "owens", "bonds", "sosa", "mcgwire", "jeter", "rodriguez", "martinez", "schilling", "johnson", "lemieux", "gretzky", "beckham", "ronaldo", "zidane", "henry",
    "coach", "athlete", "stadium", "winning streak", "losing streak", "varsity", "sport"
]

def is_sports(text):
    text = text.lower()
    for k in sports_keywords:
        if k in text:
            # Simple check, if needed can be stricter
            return True, k
    return False, None

# Sort by description length
sorted_data = sorted(data, key=lambda x: len(x.get('description', '')), reverse=True)

candidates = []
for d in sorted_data:
    text = (d.get('title', '') + " " + d.get('description', ''))
    is_sp, key = is_sports(text)
    if is_sp:
        candidates.append({
            'title': d.get('title'),
            'len': len(d.get('description', '')),
            'matched_keyword': key,
            'description': d.get('description')
        })
        if len(candidates) >= 3:
            break

print("__RESULT__:")
print(json.dumps(candidates))"""

env_args = {'var_function-call-14235117254003200453': [{'_id': '69446cc2ebf4f4e141509be9', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-14235117254003203414': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-2404915057031312117': [{'_id': '69446cc2ebf4f4e141509be9', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69446cc2ebf4f4e141509bea', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69446cc2ebf4f4e141509beb', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69446cc2ebf4f4e141509bec', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69446cc2ebf4f4e141509bed', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-6997860476864382213': [{'COUNT(*)': '127600'}], 'var_function-call-2820495118632274692': [], 'var_function-call-12963950434809988779': [{'_id': '69446cc2ebf4f4e141511119', 'article_id': '30000', 'title': 'Kerry Accuses Bush of Hiding the Truth About Iraq', 'description': 'Senator Kerry leveled his charges in a speech prepared for delivery later today before the National Guard Association in Las Vegas.'}], 'var_function-call-10886045983183967928': [{'_id': '69446cc2ebf4f4e141518649', 'article_id': '60000', 'title': 'BYTE OF THE APPLE', 'description': 'Apple lost one war to Microsoft by not licensing its Mac operating system. It may repeat the error with its iPod and music software.'}], 'var_function-call-17957036424541502436': [{'_id': '69446cc3ebf4f4e14151fb79', 'article_id': '90000', 'title': "Davenport's Victory Over Williams May Not Be Enough", 'description': ' LOS ANGELES (Reuters) - Top-ranked Lindsay Davenport pulled  off a stunning 3-6, 7-5, 6-1 win over Serena Williams at the  WTA Tour Championships Saturday, but her battling effort may  still might not be enough to get her into the semifinals.'}], 'var_function-call-11980837049529818020': 'file_storage/function-call-11980837049529818020.json'}

exec(code, env_args)
