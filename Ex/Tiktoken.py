import tiktoken

tt_encoding = tiktoken.get_encoding("cl100k_base")

text = """Many words map to one token, but some don't: indivisible.
Unicode characters like emojis may be split into many tokens containing the underlying bytes: 🤚🏾
Sequences of characters commonly found next to each other may be grouped together: 1234567890"""

tokens = tt_encoding.encode(text)
print("tokens: ", tokens)
print("++++++++++++++++++++++")

textDecode = tt_encoding.decode(tokens)
print("textDecode: ", textDecode)
print("======================")

total_token = len(tokens)
print(total_token)
