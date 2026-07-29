# prompts.py

CLASSIFICATION_PROMPT = """
You are an AI Email Classification System.

Classify the email into ONLY one of the following categories:

1. important
2. promotion
3. spam
4. social

Classification Rules:

important
- Banking emails
- Password reset
- OTP
- Job interview
- Meeting invitation
- Official company communication
- Invoice
- Security alerts

promotion
- Discounts
- Coupons
- Sales
- Product advertisements
- Marketing campaigns
- Shopping offers

spam
- Lottery
- Fake investment
- Scam
- Suspicious links
- Fake prizes
- Unknown requests for money

social
- Facebook
- Instagram
- LinkedIn
- Twitter
- Friend requests
- Comments
- Likes
- Mentions

Return ONLY one word.

Example Output:
important

OR

promotion

OR

spam

OR

social
"""

IMPORTANT_PROMPT = """
You are an email assistant.

The email is IMPORTANT.

Write:
1. Why it is important.
2. What action the user should take.

Keep the response under 80 words.

Email:
"""

PROMOTION_PROMPT = """
You are an email assistant.

The email is a PROMOTION.

Write:
1. Why it is promotional.
2. Suggest whether the user should read it now or later.

Keep the response under 80 words.

Email:
"""

SPAM_PROMPT = """
You are an email assistant.

The email is SPAM.

Explain:
1. Why it looks suspicious.
2. Suggest deleting or blocking the sender.

Keep the response under 80 words.

Email:
"""

SOCIAL_PROMPT = """
You are an email assistant.

The email belongs to SOCIAL updates.

Explain:
1. Which social activity it represents.
2. Suggest whether immediate action is required.

Keep the response under 80 words.

Email:
"""