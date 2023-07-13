# python3

# Task. Your friend is making a text editor for programmers. He is currently working on a feature that will
# find errors in the usage of different types of brackets. Code can contain any brackets from the set
# []{}(), where the opening brackets are [,{, and ( and the closing brackets corresponding to them
# are ],}, and ).
# For convenience, the text editor should not only inform the user that there is an error in the usage
# of brackets, but also point to the exact place in the code with the problematic bracket. First priority
# is to find the first unmatched closing bracket which either doesn’t have an opening bracket before it,
# like ] in ](), or closes the wrong opening bracket, like } in ()[}. If there are no such mistakes, then
# it should find the first unmatched opening bracket without the corresponding closing bracket after it,
# like ( in {}([]. If there are no mistakes, text editor should inform the user that the usage of brackets
# is correct.
# Apart from the brackets, code can contain big and small latin letters, digits and punctuation marks.

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