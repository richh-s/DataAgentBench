code = """import json

file_path = locals()['var_function-call-7596994010682886382']
with open(file_path, 'r') as f:
    articles = json.load(f)

keywords = {
    "Sports": ["sport", "football", "soccer", "basketball", "baseball", "tennis", "golf", "hockey", "olympic", "athlete", "medal", "champion", "league", "cup", "game", "match", "score", "coach", "team", "nba", "nfl", "mlb", "nhl", "fifa", "uefa", "won", "lost", "victory", "defeat", "tournament", "race", "f1", "formula one", "driver", "cyclist", "swimmer", "runner", "sox", "yankees", "lakers", "bulls", "united", "city", "real madrid", "barcelona", "chelsea", "arsenal", "liverpool", "manchester", "series", "inning", "quarterback", "touchdown", "goal", "striker", "defender", "pitcher", "batter", "wimbledon", "open", "gold", "silver", "bronze", "record", "athens", "olympics"],
    "Business": ["market", "stock", "price", "company", "oil", "economy", "profit", "quarter", "dollar", "euro", "yen", "bank", "trade", "deal", "merger", "acquisition", "ceo", "cfo", "business", "industry", "corp", "inc", "ltd", "shares", "investor", "investment", "inflation", "rates", "fed", "federal reserve", "wall street", "nasdaq", "dow", "s&p", "revenue", "earnings", "imf", "wto", "deficit"],
    "Sci/Tech": ["software", "internet", "computer", "microsoft", "google", "apple", "space", "launch", "virus", "study", "science", "technology", "tech", "web", "online", "digital", "mobile", "phone", "chip", "processor", "server", "data", "network", "nasa", "astronomer", "biology", "physics", "chemistry", "discovery", "research", "scientist", "linux", "windows", "browser", "search engine"],
    "World": ["iraq", "president", "war", "minister", "bomb", "treaty", "un", "peace", "government", "country", "nation", "international", "politics", "election", "vote", "parliament", "senate", "congress", "bush", "kerry", "blair", "putin", "china", "russia", "iran", "korea", "israel", "palestin", "military", "army", "troops", "attack", "explosion", "hostage", "kidnapp", "official", "authorities", "police", "darfur", "sudan", "gaza", "baghdad"]
}

def classify(text):
    text = text.lower()
    scores = {cat: 0 for cat in keywords}
    for cat, kws in keywords.items():
        for kw in kws:
            if kw in text:
                scores[cat] += 1
    if all(s == 0 for s in scores.values()):
        return "Unclassified"
    return max(scores, key=scores.get)

sports_articles = []
for art in articles:
    content = art.get('title', '') + " " + art.get('description', '')
    category = classify(content)
    if category == "Sports":
        sports_articles.append(art)

# Find the one with longest description
longest_desc_len = -1
target_article = None

for art in sports_articles:
    desc = art.get('description', '')
    if len(desc) > longest_desc_len:
        longest_desc_len = len(desc)
        target_article = art

result = {
    "total_articles": len(articles),
    "sports_count": len(sports_articles),
    "target_article_title": target_article['title'] if target_article else None,
    "target_article_desc_len": longest_desc_len if target_article else 0
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-7035366264149176864': [{'_id': '6944675c097d9a4d3bf1df9a', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944675c097d9a4d3bf1df9b', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944675c097d9a4d3bf1df9c', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944675c097d9a4d3bf1df9d', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944675c097d9a4d3bf1df9e', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-659362784630958922': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}], 'var_function-call-2134585413192635529': [{'_id': '6944675c097d9a4d3bf1df9a', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944675c097d9a4d3bf1df9b', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944675c097d9a4d3bf1df9c', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944675c097d9a4d3bf1df9d', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944675c097d9a4d3bf1df9e', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-2330990286934082332': [{'_id': '6944675c097d9a4d3bf1df9a', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944675c097d9a4d3bf1df9b', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944675c097d9a4d3bf1df9c', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944675c097d9a4d3bf1df9d', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944675c097d9a4d3bf1df9e', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-7596994010682886382': 'file_storage/function-call-7596994010682886382.json', 'var_function-call-1990056132661216657': None, 'var_function-call-14491379230355912334': {'counts': {'Sports': 0, 'Business': 0, 'Sci/Tech': 0, 'World': 0, 'Unclassified': 1000}, 'unclassified_examples': ["Wall St. Bears Claw Back Into the Black (Reuters) Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again.", 'Carlyle Looks Toward Commercial Aerospace (Reuters) Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.', "Oil and Economy Cloud Stocks' Outlook (Reuters) Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.", 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters) Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.', 'Oil prices soar to all-time record, posing new menace to US economy (AFP) AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.']}}

exec(code, env_args)
