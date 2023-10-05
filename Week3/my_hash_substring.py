# python3
from random import randint

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def PolyHash(string):
    hash = 0
    for i in range(len(string)-1, -1, -1):
        hash = ord(string[i])+hash
    return hash

def PrecomputeHashes(text, pattern_length):
    text_length = len(text)
    H = [0] * (text_length - pattern_length+1)

    ascii_text = [0] * len(text)
    for i in range(text_length):
        symbol = ord(text[i])
        ascii_text[i] = symbol
    S = text[text_length-pattern_length:text_length]

    H[text_length-pattern_length] = PolyHash(S)
    # for i in range(text_length-pattern_length, -1
    for i in range(text_length-pattern_length-1, -1, -1):
        H[i] = H[i+1] + ascii_text[i] - ascii_text[i+(pattern_length)]
    return H


def get_occurrences(pattern, text):
    positions = []

    pHash = PolyHash(pattern)

    H = PrecomputeHashes(text, len(pattern))

    for i in range(len(text) - len(pattern)+1):
        if pHash != H[i]:
            continue
        if text[i:i+len(pattern)] == pattern:
            positions.append(i)
    return positions


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

