code = """import json
import re

# Access the data
data_key = 'var_function-call-5264877127341526861'
file_path = locals().get(data_key)

with open(file_path, 'r') as f:
    articles = json.load(f)

# Re-use classification logic (simplified for brevity here, assuming it's same as before)
categories = {
    'Business': {'market', 'stock', 'price', 'company', 'corp', 'inc', 'share', 'profit', 'revenue', 'economy', 'bank', 'deal', 'dollar', 'oil', 'gas', 'trade', 'business', 'industry', 'ceo', 'sales', 'fed', 'rates', 'deficit', 'inflation', 'nasdaq', 'dow'},
    'Sci/Tech': {'computer', 'software', 'hardware', 'internet', 'web', 'online', 'technology', 'tech', 'science', 'space', 'nasa', 'microsoft', 'google', 'intel', 'linux', 'virus', 'phone', 'mobile', 'network', 'chip', 'apple', 'ibm', 'server', 'game', 'video', 'windows', 'code', 'developer', 'bug', 'unix', 'dos', 'memory', 'app', 'digital'},
    'World': {'president', 'minister', 'official', 'government', 'police', 'military', 'army', 'war', 'peace', 'attack', 'bomb', 'killed', 'iraq', 'iran', 'palestine', 'israel', 'un', 'election', 'politics', 'nuclear', 'korea', 'china', 'russia'},
    'Sports': {'olympics', 'olympic', 'gold', 'medal', 'athens', 'basketball', 'football', 'soccer', 'baseball', 'nba', 'nfl', 'nhl', 'tournament', 'championship', 'athlete', 'coach', 'sport', 'game', 'match', 'score', 'victory', 'cup', 'team', 'league', 'tennis', 'golf', 'boxing', 'cricket', 'rugby', 'hockey', 'f1', 'racing', 'swimming', 'gymnastics', 'sox', 'yankees', 'mets', 'doping'}
}

def classify(title, desc):
    text = (title + " " + desc).lower()
    tokens = re.findall(r'\w+', text)
    token_set = set(tokens)
    scores = {cat: 0 for cat in categories}
    for cat, keywords in categories.items():
        matches = token_set.intersection(keywords)
        scores[cat] += len(matches)
        if cat == 'Sports':
            if 'olympics' in matches or 'olympic' in matches: scores['Sports'] += 3
            if 'athens' in matches: scores['Sports'] += 2
        if cat == 'Sci/Tech':
            if 'microsoft' in matches or 'google' in matches: scores['Sci/Tech'] += 2
        if cat == 'World':
            if 'iraq' in matches: scores['World'] += 2
    
    if 'game' in tokens:
        tech_indicators = {'software', 'computer', 'video', 'windows', 'console', 'developer', 'bug', 'code'}
        if token_set.intersection(tech_indicators):
            scores['Sci/Tech'] += 2
            scores['Sports'] -= 1
        else:
            scores['Sports'] += 1

    max_cat = max(scores, key=scores.get)
    if scores[max_cat] == 0: return "Unknown"
    return max_cat

sports_articles = []
for art in articles:
    cat = classify(art.get('title', ''), art.get('description', ''))
    if cat == 'Sports':
        sports_articles.append(art)

sports_articles.sort(key=lambda x: len(x.get('description', '')), reverse=True)

top_5 = []
for i in range(min(5, len(sports_articles))):
    top_5.append({
        "title": sports_articles[i]['title'],
        "len": len(sports_articles[i]['description']),
        "preview": sports_articles[i]['description'][:100]
    })

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-16303435935020228874': ['articles'], 'var_function-call-16303435935020230519': ['authors', 'article_metadata'], 'var_function-call-11932383749502743792': [{'_id': '69446602bc717173969e3f7b', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-11932383749502745537': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-17726508914481105227': [{'_id': '69446602bc717173969e3f7b', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69446602bc717173969e3f7c', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69446602bc717173969e3f7d', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69446602bc717173969e3f7e', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69446602bc717173969e3f7f', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-11472611331630481807': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-11703216715718506924': 'No sports articles found.', 'var_function-call-5264877127341526861': 'file_storage/function-call-5264877127341526861.json', 'var_function-call-15378500491017219362': {'total_articles': 10000, 'sports_count': 2165, 'top_sports_article': {'article_id': '183', 'title': "Why Windows isn't Unix", 'description': '\\\\"I first heard about this from one of the developers of the hit game SimCity, who\\told me that there was a critical bug in his application: it used memory right\\after freeing it, a major no-no that happened to work OK on DOS but would not\\work under Windows where memory that is freed is likely to be snatched up by\\another running application right away. The testers on the Windows team were\\going through various popular applications, testing them to make sure they\\worked OK, but SimCity kept crashing. They reported this to the Windows\\developers, who disassembled SimCity, stepped through it in a debugger, found\\the bug, and added special code that checked if SimCity was running, and if it\\did ...\\\\'}}, 'var_function-call-89385635820246599': {'title': 'THECHAT', 'description_length': 631, 'description_preview': '&lt;em&gt; Dean Cain has spent much of his life in a uniform. He\'s done time as an all-American safety at Princeton (where he established a since-broken single-season Division I-AA record for interceptions), an undrafted free agent with the Buffalo Bills (before a preseason knee injury ended his football career), a sportsman of the future (in the aptly named movie "Futuresport") and an iconic superhero (in television\'s "Lois and Clark: The New Adventures of Superman"). Next up is a set of pinstripes -- Cain plays star third baseman Conrad Dean in the CBS drama "Clubhouse," which is scheduled to debut next month. &lt;/em&gt;'}}

exec(code, env_args)
