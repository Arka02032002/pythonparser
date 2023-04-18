import re

def tokenize(code):
    keywords = ["auto", "break", "case", "char", "const", "continue", "default", "do", "double", "else", "enum", "extern", "float", "for", "goto", "if", "int", "long", "register", "return", "short", "signed", "sizeof", "static", "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while"]
    tokens = []
    for line in code.split("\n"):
        # Remove preprocessor directives
        line = re.sub(r'#\w+.*', '', line)
        # Tokenize line
        for match in re.finditer(r"(\w+)|([^\w\s])", line):
            token = match.group()
            if token in keywords:
                tokens.append((token))
            elif re.match(r"\d+", token):
                tokens.append((token))
            elif token != " " and token != "\n":
                tokens.append((token))
    return tokens

code = """
#include <stdio.h>

int main() {
    int x = 5;
    printf("Hello, world! x=%d\n", x);
    return 0;
}
"""

print(tokenize(code))

