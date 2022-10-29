def valid_parentheses(string):
    if string.count('(') + string.count(')') == 0:
        return True
    bracket_line = ''
    for elem in string:
        if elem == '(' or elem == ')':
            if elem == '(':
                bracket_line += '('
            elif len(bracket_line) > 0:
                bracket_line = bracket_line.replace('(', '', 1)
            else:
                return False
    if bracket_line != '':
        return False
    return True
