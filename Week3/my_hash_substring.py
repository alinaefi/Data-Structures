"""Find pattern in text
Problem Introduction
In this problem, your goal is to implement the Rabin–Karp’s algorithm.
Problem Description
Task. In this problem your goal is to implement the Rabin–Karp’s algorithm for searching the given pattern
in the given text.
Input Format. There are two strings in the input: the pattern 𝑃 and the text 𝑇.
Constraints. 1 ≤ |𝑃| ≤ |𝑇| ≤ 5 · 105
. The total length of all occurrences of 𝑃 in 𝑇 doesn’t exceed 108
. The
pattern and the text contain only latin letters.
Output Format. Print all the positions of the occurrences of 𝑃 in 𝑇 in the ascending order. Use 0-based
indexing of positions in the the text 𝑇."""

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

