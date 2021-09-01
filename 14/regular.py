""""
109. Python Regular Expressions Part One
"""
from re import search, findall, finditer, compile as compiles

if __name__ == "__main__":
    TEXT = "The agent's phone number is 408-5555-1234. Call phone soon!"
    PATTERN = "phone"
    match = search(PATTERN, TEXT)
    matches = findall(PATTERN, TEXT)
    print(match.span(), match.group())
    print(matches)
    for mat in finditer(PATTERN, TEXT):
        print(mat.span(), mat.group())
    phone_pattern = compiles(r"(\d{3})-(\d{4})-(\d{3})")
    phone = search(phone_pattern, TEXT)
    print(phone.span(), phone.group())
    print(phone.group(1))
    CAT = "The cats in the hat went splat."
    print(search(r"cat|dog", CAT))
    print(search(r"cat(s)", CAT))
    print(findall(r"...at", CAT))
    print(search(r"^\d", "1 is a number. 2"))
    print(findall(r"\d$", "this 11 is a number. 2"))
    PHRASE = "There are 3 numbers! 34 inside 5, this sentence. remove?"
    print(findall(r"[^\d]+", PHRASE))
    clean = findall(r"[^!.,? $]+", PHRASE)
    print(" ".join(clean))
    LONG_TEXT = "Only fi-nd the hypen-text in th-is long sen-tence."
    print(findall(r"[\w]+-[\w]+", LONG_TEXT))
