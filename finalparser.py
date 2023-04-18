import sys
from pycparser import parse_file, c_ast, c_parser
from graphviz import Digraph
import re

c_code = '''
int main()
{
    int a=2;
    int b=3;
    int c=a+b-2;
    if(c>0){
        printf(c);
    }
    return 0;
}
'''

ENTITY_NAMES = {
    'FuncDef': 'function',
    'FuncDecl': 'function declaration',
    'ID': 'identifier',
    'TypeDecl': 'type declaration',
    'Constant': 'constant',
    'Return': 'return statement',
    'If': 'if statement',
    'While': 'while loop',
    'For': 'for loop',
    'UnaryOp': 'unary operator',
    'BinaryOp': 'binary operator',
    'Decl': 'variable declaration',
    'Assignment': 'assignment statement',
    'ArrayRef': 'array reference',
    'StructRef': 'structure reference',
}

parser = c_parser.CParser()

def preprocess(c_code):
    c_code = re.sub(r'#\s*include\s*<.*?>', '', c_code)
    c_code = c_code.replace('\r', '')
    # print(c_code)
    return c_code


def generate_ast(c_code):
    ast = parser.parse(c_code)
    return ast

def generate_parse_tree(ast):
    dot = Digraph(comment='Parse Tree')
    dot.attr('node', shape='rectangle', fontname='Times-Roman')
    dot.attr('edge', fontname='Courier')
    dot.node(str(id(ast)), str(ast.__class__.__name__))

    def add_nodes(node):
        for _, child in node.children():
            child_id = id(child)
            entity_name = ENTITY_NAMES.get(type(child).__name__)
            label = entity_name if entity_name is not None else type(child).__name__
            dot.node(str(child_id), str(label))
            dot.edge(str(id(node)),str(child_id))
            add_nodes(child)

    add_nodes(ast)
    dot.render('parse_tree', format='pdf', cleanup=True, directory= './static')

if __name__ == '__main__':
    c_code=preprocess(c_code)
    ast = generate_ast(c_code)
    print(ast)
    generate_parse_tree(ast)


