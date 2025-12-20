code = """import json
import re

with open(locals()['var_function-call-9674498384229145557'], 'r') as f:
    articles = json.load(f)

sports_keywords = [
    "sport", "sports", "football", "baseball", "basketball", "soccer", "tennis", "golf", 
    "olympics", "olympic", "medal", "medals", "gold", "silver", "bronze", "athens", 
    "game", "match", "team", "league", "cup", "championship", "tournament", "coach", 
    "athlete", "athletes", "player", "players", "score", "scores", "scoring", "win", "wins", 
    "loss", "losses", "victory", "defeat", "nfl", "nba", "mlb", "nhl", "fifa", "uefa", 
    "racing", "f1", "nascar", "hockey", "cricket", "rugby", "boxing", "wrestling", 
    "swimming", "gymnastics", "marathon", "sprint", "relay", "doping", "phelps", "thorpe", 
    "rowing", "cycling", "volleyball", "diver", "diving", "hurdles", "triathlon"
]

other_keywords = [
    "market", "stock", "stocks", "price", "prices", "company", "companies", "corp", "inc", 
    "business", "economy", "trade", "profit", "loss", "dollar", "bank", "banks", "oil", 
    "gas", "energy", "wto", "imf", "fed", "inflation", "ipo", "google", "shares", "investor", 
    "fund", "revenue", "sales", "deal", "merger", "acquisition", "iraq", "president", 
    "minister", "government", "war", "peace", "election", "elections", "un", "united nations", 
    "eu", "europe", "technology", "science", "computer", "software", "internet", "web", 
    "microsoft", "intel", "nasa", "space", "nuclear", "terror", "military", "police", "attack"
]

def get_category(text):
    text = text.lower()
    sports_score = 0
    other_score = 0
    
    for kw in sports_keywords:
        # Use simple 'in' check for speed and coverage, word boundary is better but 'in' is often sufficient for scoring
        # But 'in' can be dangerous (e.g. 'win' in 'winter').
        # Let's use regex with boundaries.
        if re.search(r'\b' + re.escape(kw) + r'\b', text):
            sports_score += 1
            
    for kw in other_keywords:
        if re.search(r'\b' + re.escape(kw) + r'\b', text):
            other_score += 1
            
    if sports_score > other_score:
        return "Sports"
    return "Other"

candidates = []

for art in articles:
    text = (art.get('title', '') + " " + art.get('description', ''))
    cat = get_category(text)
    if cat == "Sports":
        candidates.append(art)

if not candidates:
    result = {"error": "No sports articles found"}
else:
    # Sort by description length desc
    candidates.sort(key=lambda x: len(x.get('description', '')), reverse=True)
    top = candidates[0]
    result = {
        "title": top['title'],
        "description_length": len(top['description']),
        "description_preview": top['description'][:100]
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-17250944776855184585': ['articles'], 'var_function-call-17250944776855184316': ['authors', 'article_metadata'], 'var_function-call-13601084253976166638': [{'_id': '69446509b7cb91ea91dd468b', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-13601084253976169751': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-2953041677624993579': [{'author_id': '0', 'name': 'Felicia Miles'}], 'var_function-call-175646378764434338': [{'_id': '69446509b7cb91ea91dd468b', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69446509b7cb91ea91dd468c', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69446509b7cb91ea91dd468d', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69446509b7cb91ea91dd468e', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69446509b7cb91ea91dd468f', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-2720222771617662260': [{'_id': '69446509b7cb91ea91dd468b', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69446509b7cb91ea91dd468c', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69446509b7cb91ea91dd468d', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69446509b7cb91ea91dd468e', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69446509b7cb91ea91dd468f', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-9674498384229145557': 'file_storage/function-call-9674498384229145557.json', 'var_function-call-15251398799869609527': 'No sports articles found.', 'var_function-call-15764102421113923973': {'total_articles': 10000, 'potential_sports_count': 1188, 'samples': ["'Madden,' 'ESPN' Football Score in Different Ways (Reuters)", "'Invisible' technology for Olympics", 'Satellite boosts Olympic security', "'Madden,' 'ESPN' Football Score in Different Ways", 'GAO Calls Stryker Too Heavy for Transport', 'Real "Danny Deckchairs" Soar With Just a Seat and Some Balloons', 'Ancient Olympics Mixed Naked Sports, Pagan Partying', 'Olympics Could Call Out the Couch Potatoes', 'Securing the gold in Athens', 'Olympic IT security requires advance planning', 'Olympic-size security demands advance planning', 'Unprecedented Electronic Digital Net for Olympics', 'Phelps, Thorpe Advance in 200 Freestyle (AP)', 'Dreaming done, NBA stars awaken to harsh Olympic reality (AFP)', 'Tough Race Ahead for Swimmer Phelps', 'Iranian Will Not Meet Israeli in Olympics Due to Weight', 'Colander Misses Chance to Emulate Jones', "Olympics-Doping-Greek Media Put Country's Honor Above Athletes", 'Olympics-Rowing-U.S. Eight Beats Canada to Set World Best Time', 'Greek runners are suspended']}}

exec(code, env_args)
