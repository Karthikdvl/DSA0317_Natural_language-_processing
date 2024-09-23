import re
def parse_expression(expression):
    pattern = r'([a-zA-Z]+)\(([^)]+)\)'
    matches = re.findall(pattern, expression)
    if matches:
        for predicate, terms in matches:
            print(f"Predicate: {predicate}, Terms: {terms.split(', ')}")
    else:
        print("Invalid expression")
expression = "loves(John, Mary)"
parse_expression(expression)
