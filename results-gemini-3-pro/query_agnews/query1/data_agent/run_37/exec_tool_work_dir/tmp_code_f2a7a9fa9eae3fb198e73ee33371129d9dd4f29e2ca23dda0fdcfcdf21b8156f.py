code = """import json
import re

file_path = locals()['var_function-call-7752384695117518704']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Regex based keywords
keywords = {
    'Sports': [
        r'\bolympics?\b', r'\bfootball\b', r'\bsoccer\b', r'\bbasketball\b', r'\bbaseball\b', 
        r'\btennis\b', r'\bgolf\b', r'\bhockey\b', r'\bmedal\b', r'\bathlete\b', r'\bchampion\b', 
        r'\btournament\b', r'\bstadium\b', r'\bnba\b', r'\bnfl\b', r'\bmlb\b', r'\bfifa\b', 
        r'\buefa\b', r'\bwimbledon\b', r'\bathens\b', r'\bgold\b', r'\bsilver\b', r'\bbronze\b', 
        r'\bworld cup\b', r'\drugby\b', r'\bcricket\b', r'\bf1\b', r'\bracing\b', r'\bcoach\b', 
        r'\bsquad\b', r'\bmarathon\b', r'\bsprint\b', r'\bswim(ming)?\b', r'\bgymnastics?\b'
    ],
    'Tech': [
        r'\bsoftware\b', r'\bhardware\b', r'\binternet\b', r'\bcomputer\b', r'\bmicrosoft\b', 
        r'\bgoogle\b', r'\bintel\b', r'\blinux\b', r'\bwindows\b', r'\bunix\b', r'\bvirus\b', 
        r'\btechnology\b', r'\bspace\b', r'\bnasa\b', r'\bapple\b', r'\bibm\b', r'\bweb\b', 
        r'\bonline\b', r'\bserver\b', r'\bdownload\b'
    ]
}

def count_matches(text, patterns):
    count = 0
    for p in patterns:
        if re.search(p, text, re.IGNORECASE):
            count += 1
    return count

candidates = []

for article in articles:
    text = article.get('title', '') + " " + article.get('description', '')
    
    # Simple check: If Sports score > Tech score and Sports score > 0
    s_score = count_matches(text, keywords['Sports'])
    t_score = count_matches(text, keywords['Tech'])
    
    if s_score > 0 and s_score >= t_score:
        # Also check against Business/World broadly if needed, but let's assume Sports keywords are distinct enough from Business/World for now
        # Or better, just collect all that have sports keywords and sort them, then I inspect.
        candidates.append(article)

# Sort by description length descending
candidates.sort(key=lambda x: len(x.get('description', '')), reverse=True)

# Return top 5
print('__RESULT__:')
print(json.dumps(candidates[:5]))"""

env_args = {'var_function-call-13104621924763589325': [{'_id': '694480101a20f323c78a04b2', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694480101a20f323c78a04b3', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694480101a20f323c78a04b4', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694480101a20f323c78a04b5', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694480101a20f323c78a04b6', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-6733588393098441366': [{'_id': '694480101a20f323c78a04b2', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694480101a20f323c78a04b3', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694480101a20f323c78a04b4', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694480101a20f323c78a04b5', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694480101a20f323c78a04b6', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-12515281274921194462': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}], 'var_function-call-4082764859491298474': [{'_id': '694480101a20f323c78a04b2', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694480101a20f323c78a04b3', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694480101a20f323c78a04b4', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694480101a20f323c78a04b5', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694480101a20f323c78a04b6', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-7752384695117518704': 'file_storage/function-call-7752384695117518704.json', 'var_function-call-11819510026672765726': {'_id': '694480101a20f323c78a0569', 'article_id': '183', 'title': "Why Windows isn't Unix", 'description': '\\\\"I first heard about this from one of the developers of the hit game SimCity, who\\told me that there was a critical bug in his application: it used memory right\\after freeing it, a major no-no that happened to work OK on DOS but would not\\work under Windows where memory that is freed is likely to be snatched up by\\another running application right away. The testers on the Windows team were\\going through various popular applications, testing them to make sure they\\worked OK, but SimCity kept crashing. They reported this to the Windows\\developers, who disassembled SimCity, stepped through it in a debugger, found\\the bug, and added special code that checked if SimCity was running, and if it\\did ...\\\\'}}

exec(code, env_args)
