# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if not (next in "{[()}]"):
            continue
        if next in "([{":
            # Process opening bracket
            opening_bracket = Bracket(next,i)
            opening_brackets_stack.append(opening_bracket)
        else:
            # if no opening brackets found
            if opening_brackets_stack == []:
                closing_bracket = Bracket(next, i)
                # push the first closing bracket to stack
                opening_brackets_stack.append(closing_bracket)
                break
            if next in ")]}":
                # Process closing bracket
                closing_bracket = Bracket(next,i)
                # check whether brackets match
                match = are_matching(opening_brackets_stack.pop().char, closing_bracket.char)
              
                if not match:
                    # push unmatched bracket to stack
                    unmatched_bracket = Bracket(next,i)
                    opening_brackets_stack.append(unmatched_bracket)
                    break
          
                
    return opening_brackets_stack


def main():
    text = input()
    mismatch = find_mismatch(text)

    # Printing answer, write your code here
    if (mismatch == []):
        print("Success")
    else:
        print(mismatch.pop().position+1)


if __name__ == "__main__":
    main()