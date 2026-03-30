import re
import random

rules = [
    (r"hello", ["Hi there!", "Hello!", "Hey!"]),
    (r"my name is (.*)", ["Nice to meet you %1", "Hello %1"]),
    (r"i feel (.*)", ["Why do you feel %1?", "What makes you feel %1?"]),
    (r"i am (.*)", ["How long have you been %1?", "Why are you %1?"]),
    (r"because (.*)", ["Is that the real reason?", "What else contributes?"]),
    (r"my mother (.*)", ["Tell me more about your mother.", "How does she affect you?"]),
    (r"i need (.*)", ["Why do you need %1?", "Would it help you to get %1?"]),
    (r"quit", ["Goodbye!"])
]

def get_eliza_response(user_input: str) -> str:
    for pattern, responses in rules:
        match = re.match(pattern, user_input.lower())
        if match:
            response = random.choice(responses)
            for i in range(1, len(match.groups()) + 1):
                response = response.replace(f"%{i}", match.group(i))
            return response
    return "Tell me more."