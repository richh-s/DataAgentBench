code = """import json
import re

# Load the data
file_path = locals()['var_function-call-6036018550432900631']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Keywords
keywords_sports = set(["sport", "sports", "olympic", "olympics", "medal", "gold", "silver", "bronze", "football", "soccer", "basketball", "baseball", "tennis", "golf", "hockey", "cricket", "rugby", "boxing", "racing", "f1", "formula one", "nascar", "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "champion", "championship", "tournament", "league", "cup", "athlete", "player", "coach", "team", "match", "game", "score", "win", "loss", "victory", "defeat", "record", "athens", "swimming", "gymnastics", "track", "field", "marathon", "stadium", "doping", "drug", "title", "bonds", "armstrong", "phelps", "woods", "williams", "federer", "roddick", "schumacher", "ferrari", "yankees", "red sox", "lakers", "pistons", "arsenal", "manchester", "chelsea", "real madrid", "barcelona", "ac milan", "juventus", "inter", "quarterback", "touchdown", "homerun", "slam", "wimbledon", "open", "masters", "cup", "bowl", "series", "playoff", "final", "semifinal"])

keywords_politics = set(["senate", "congress", "democrat", "republican", "bush", "kerry", "election", "vote", "poll", "parliament", "legislature", "policy", "campaign", "president", "minister", "prime minister", "iraq", "iran", "war", "military", "troops", "bomb", "blast", "kill", "police", "court", "judge", "law", "legal", "stock", "market", "economy", "oil", "price", "software", "internet", "technology", "microsoft", "google"])

def is_sports(title, desc):
    text = (title + " " + desc).lower()
    tokens = re.findall(r'\w+', text)
    
    score = 0
    for t in tokens:
        if t in keywords_sports:
            score += 1
        if t in keywords_politics:
            score -= 2 # Strong penalty for politics/business keywords
            
    # Heuristics
    if "olympic" in text or "athens" in text:
        score += 3
        
    return score > 0

candidates = []
for a in articles:
    if is_sports(a['title'], a['description']):
        candidates.append(a)

# Sort by description length descending
candidates.sort(key=lambda x: len(x['description']), reverse=True)

# Return top 5
top_5 = candidates[:5]
result = [{"title": c['title'], "desc_len": len(c['description']), "description": c['description']} for c in top_5]

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-9821206441971068824': ['articles'], 'var_function-call-9821206441971066019': ['authors', 'article_metadata'], 'var_function-call-9708188625832290358': [{'_id': '69446302e64442a00bf5d969', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-9708188625832291827': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-5673689165236548416': [{'_id': '69446302e64442a00bf5d969', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69446302e64442a00bf5d96a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69446302e64442a00bf5d96b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69446302e64442a00bf5d96c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69446302e64442a00bf5d96d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-355172535146539447': [{'_id': '69446302e64442a00bf5d969', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69446302e64442a00bf5d96a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69446302e64442a00bf5d96b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69446302e64442a00bf5d96c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69446302e64442a00bf5d96d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-16676322079434033556': 'file_storage/function-call-16676322079434033556.json', 'var_function-call-1093242531798274301': 'file_storage/function-call-1093242531798274301.json', 'var_function-call-1093242531798276056': [{'count(*)': '127600'}], 'var_function-call-6036018550432900631': 'file_storage/function-call-6036018550432900631.json', 'var_function-call-8054804172114473445': {'title': '2004 US Senate Outlook', 'desc_len': 944, 'description': "With all the hoopla over Bush and Kerry, some of you may not have been paying close attention to the other races going on in this loaded US political season. I've read a good dozen or so Senate outlooks, and my blurry eyes and spinning brain kept getting lost in all the numbers and losing track of who, ultimately, was likely to control the Senate on November third. So I made my very own Senate outlook to figure it out (or add further confusion, depending on what you think of my predictions). The bad news is, we probably won't know who controls the Senate on November third. The good news, if you're a Democrat (or a person who loves one), is that my best guess at this point is that when the dust settles, Democrats will probably be in control by the very slimmest possible margin. Shock! But everyone knows the Dems have no chance of taking either house of Congress. I think everyone hasn't been paying attention. Read on for my rundown."}}

exec(code, env_args)
