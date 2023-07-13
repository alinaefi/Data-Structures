// Task. Your friend is making a text editor for programmers. He is currently working on a feature that will
// find errors in the usage of different types of brackets. Code can contain any brackets from the set
// []{}(), where the opening brackets are [,{, and ( and the closing brackets corresponding to them
// are ],}, and ).
// For convenience, the text editor should not only inform the user that there is an error in the usage
// of brackets, but also point to the exact place in the code with the problematic bracket. First priority
// is to find the first unmatched closing bracket which either doesn’t have an opening bracket before it,
// like ] in ](), or closes the wrong opening bracket, like } in ()[}. If there are no such mistakes, then
// it should find the first unmatched opening bracket without the corresponding closing bracket after it,
// like ( in {}([]. If there are no mistakes, text editor should inform the user that the usage of brackets
// is correct.
// Apart from the brackets, code can contain big and small latin letters, digits and punctuation marks.


import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Stack;

class Bracket {
    Bracket(char type, int position) {
        this.type = type;
        this.position = position;
    }

    boolean Match(char c) {
        if (this.type == '[' && c == ']')
            return true;
        if (this.type == '{' && c == '}')
            return true;
        if (this.type == '(' && c == ')')
            return true;
        return false;
    }

    char type;
    int position;
}

class check_brackets {
    public static void main(String[] args) throws IOException {
        InputStreamReader input_stream = new InputStreamReader(System.in);
        BufferedReader reader = new BufferedReader(input_stream);
        String text = reader.readLine();

        Stack<Bracket> opening_brackets_stack = new Stack<Bracket>();
        for (int position = 0; position < text.length(); ++position) {
            char next = text.charAt(position);

            if (next != '(' && next != ')' && next != '[' && next != ']' && next != '{' && next != '}') {
                continue;
            }

            if (next == '(' || next == '[' || next == '{') {
                // create a bracket
                Bracket opening_bracket = new Bracket(next, position);
                // push it to stack
                opening_brackets_stack.push(opening_bracket);
            } else {
                // check if stack is not empty
                if (opening_brackets_stack.empty()) {
                    Bracket unmatched_bracket = new Bracket(next, position);
                    // push the 1st unmatched bracket to stack
                    opening_brackets_stack.push(unmatched_bracket);
                    break;
                }
                if (next == ')' || next == ']' || next == '}') {
                // check the top element in the stack and remove it
                Bracket top_element = opening_brackets_stack.pop();
                // check if it matches the current closing bracket
                boolean match = top_element.Match(next);
                if (match == false) {
                    Bracket unmatched_bracket = new Bracket(next, position);
                    // push the 1st unmatched bracket to stack
                    opening_brackets_stack.push(unmatched_bracket);
                    break;
                }
            }
        }
        }

        // Printing answer
        if (opening_brackets_stack.empty()) {
            System.out.println("Success");
        } else {
            System.out.println(opening_brackets_stack.pop().position+1);
        }
        
    }
}
