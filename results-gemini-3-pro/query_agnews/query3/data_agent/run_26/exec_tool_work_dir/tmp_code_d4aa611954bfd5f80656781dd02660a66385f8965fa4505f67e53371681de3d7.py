code = """import json
import re

# Load metadata (id_to_year)
meta_file = locals()['var_function-call-15834934156015708964']
with open(meta_file, 'r') as f:
    meta_data = json.load(f)
    id_to_year = meta_data['id_to_year'] # Keys are strings or ints? The previous script printed them as ints in the list, but let's check. 
    # JSON keys are always strings! "id_to_year" in JSON will have string keys "3": 2020.
    # So I should cast them to int or keep as string. 
    # Let's verify what json.load produces for keys. They will be strings.

# Load articles
articles_file = locals()['var_function-call-9188141615407215187']
with open(articles_file, 'r') as f:
    articles = json.load(f)

# Keywords
business_keywords = {
    "economy", "business", "market", "stock", "stocks", "share", "shares", "trade", "profit", "loss", "investment", "investor", "bank", "banking", 
    "dollar", "euro", "currency", "price", "prices", "oil", "gold", "finance", "financial", "corporate", "company", "companies", "firm", "firms", 
    "sales", "revenue", "cost", "inflation", "rate", "rates", "fed", "federal reserve", "central bank", "ipo", "merger", "acquisition", "deal", 
    "buyout", "retail", "consumer", "growth", "recession", "recovery", "index", "dow", "nasdaq", "wall street", "bond", "yield", "ceo", "earnings", 
    "quarter", "analyst", "forecast", "sector", "industry", "manufacturing", "production", "output", "demand", "supply", "debt", "loan", "credit",
    "budget", "deficit", "tax", "jobs", "employment", "unemployment", "hiring", "wage", "salary", "bonus", "strike", "union", "wto", "imf", "gdp"
}

scitech_keywords = {
    "computer", "software", "internet", "web", "online", "technology", "tech", "science", "space", "nasa", "satellite", "orbit", "robot", "phone", 
    "mobile", "wireless", "broadband", "chip", "processor", "microsoft", "google", "apple", "ibm", "linux", "windows", "server", "network", "data", 
    "virus", "hacker", "security", "email", "browser", "search", "biotech", "genetics", "drug", "pharmaceutical", "medicine", "disease", "treatment", 
    "health", "research", "study", "scientist", "telescope", "astronomy", "physics", "chemistry", "biology", "launch", "flight", "digital", "electronic"
}

sports_keywords = {
    "sport", "sports", "game", "match", "team", "player", "coach", "manager", "club", "league", "cup", "tournament", "championship", "medal", "olympics", 
    "football", "soccer", "baseball", "basketball", "hockey", "tennis", "golf", "cricket", "rugby", "racing", "driver", "f1", "nascar", "stadium", 
    "score", "win", "won", "winner", "loss", "lost", "victory", "defeat", "goal", "touchdown", "points", "rank", "title", "champion", "athlete", 
    "season", "playoff", "final", "semi-final", "world cup", "super bowl"
}

world_keywords = {
    "world", "international", "country", "nation", "government", "president", "minister", "parliament", "congress", "senate", "election", "vote", 
    "poll", "democracy", "war", "conflict", "battle", "fight", "army", "military", "troops", "soldier", "police", "attack", "bomb", "blast", "explosion", 
    "terror", "terrorist", "iraq", "afghanistan", "iran", "korea", "china", "russia", "israel", "palestine", "peace", "treaty", "talks", "summit", 
    "un", "united nations", "eu", "nuclear", "weapon", "kill", "killed", "dead", "wound", "injured", "disaster", "earthquake", "flood", "hurricane", 
    "storm", "crash", "accident", "protest", "riot", "crisis", "law", "court", "judge", "trial", "prison", "rights", "refugee", "aid"
}

def classify(text):
    text = text.lower()
    words = re.findall(r'\w+', text)
    counts = {"Business": 0, "Sci/Tech": 0, "Sports": 0, "World": 0}
    
    for w in words:
        if w in business_keywords: counts["Business"] += 1
        if w in scitech_keywords: counts["Sci/Tech"] += 1
        if w in sports_keywords: counts["Sports"] += 1
        if w in world_keywords: counts["World"] += 1
    
    # Heuristic for specific overlaps
    # "oil" is in Business, but "oil" + "iraq" might be World.
    # "company" is Business.
    # "team" is Sports.
    # "president" is World.
    
    # Just take max
    if max(counts.values()) == 0:
        return "Unknown"
    
    # Tie breaking: Business > World > Sci/Tech > Sports (arbitrary, but let's see)
    # Or just use the one with strict max.
    sorted_cats = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    if sorted_cats[0][1] > sorted_cats[1][1]:
        return sorted_cats[0][0]
    else:
        # Tie
        # If tie between Business and World, and "oil" is present, check context? Hard.
        # Let's prioritize Business for this query as we want to find Business articles.
        # But wait, if I prioritize Business, I might overcount.
        # Let's prioritize the one that appears first in the sorted list (stable sort?).
        # Dictionary order is insertion order.
        return sorted_cats[0][0]

business_counts = {}
for y in range(2010, 2021):
    business_counts[y] = 0

for art in articles:
    aid_str = art.get('article_id')
    # Convert to int to lookup in id_to_year which came from JSON (keys are strings)
    # id_to_year keys are strings "3", "9".
    if aid_str in id_to_year:
        year = id_to_year[aid_str]
        text = (art.get('title', '') + " " + art.get('description', ''))
        cat = classify(text)
        if cat == "Business":
            business_counts[year] += 1

total_business = sum(business_counts.values())
years_count = 11 # 2010 to 2020 inclusive
average = total_business / years_count

print("__RESULT__:")
print(json.dumps({"counts": business_counts, "average": average}))"""

env_args = {'var_function-call-12051989784931741793': ['authors', 'article_metadata'], 'var_function-call-8881788724553702350': 'file_storage/function-call-8881788724553702350.json', 'var_function-call-15834934156015708964': 'file_storage/function-call-15834934156015708964.json', 'var_function-call-241652876630569464': 14860, 'var_function-call-13057485116789306292': [{'_id': '6944d765bc50274a4486b1ca', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944d765bc50274a4486b1cb', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944d765bc50274a4486b1cc', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944d765bc50274a4486b1cd', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944d765bc50274a4486b1ce', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-3033909346262757513': 127583, 'var_function-call-16449323081972518628': 3, 'var_function-call-6251446830907674104': 'file_storage/function-call-6251446830907674104.json', 'var_function-call-2159420247817862812': [{'_id': '6944d765bc50274a4486b1ca', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-16504892324367978163': [{'_id': '6944d765bc50274a4486b1ca', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944d765bc50274a4486b1cb', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944d765bc50274a4486b1cc', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944d765bc50274a4486b1cd', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944d765bc50274a4486b1ce', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-9188141615407215187': 'file_storage/function-call-9188141615407215187.json'}

exec(code, env_args)
