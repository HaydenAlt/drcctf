a = "flag"

b = ""
for c in a:
    if 'a' <= c <= 'z':
        b += chr((ord(c) - ord('a') + 13) % 26 + ord('a'))
    elif 'A' <= c <= 'Z':
        b += chr((ord(c) - ord('A') + 13) % 26 + ord('A'))
    else:
        b += c
d = b[::-1]

print(f"Result: {d}")
