from genlib.gen_data import generate_file_path
from genlib.gen_ruleset import Rules

tab_0 = '\n'
tab_1 = '\n    '
tab_2 = '\n        '
and_exp = 'and'


# def test_eq2(self):
#     c = Calculator()
#     r1 = c.resolve_eq(3, 4, 1)
#     r2 = c.resolve_eq(1, -1, -1)
#     r3 = c.resolve_eq(9, -5, 0)
#     r4 = c.resolve_eq(5, 0, -4)
#     self.assertAlmostEqual(r1[0], [-0.3333333333333333, -1.0][0])
#     self.assertAlmostEqual(r2[0], [1.618033988749895, -0.6180339887498949][0])
#     self.assertAlmostEqual(r3[0], [0.5555555555555556, 0.0][0])
#     self.assertAlmostEqual(r4[0], [0.894427190999916, -0.894427190999916][0])


def generate_test_file(file_path, file_name, imports, rules):
    generate_file_path(file_path)
    with open(file_path + file_name, 'w') as f:
        write_imports(f, imports)
        write_func(f, rules)
        write_test_by_rules(f, rules)


def write_func(f, rules: Rules):
    inputs_and_output_vars = rules.get_inferred_inputs_and_output()
    params = ''
    for input in inputs_and_output_vars['inputs']:
        params += input + ', '
    params = params[:-2]
    f.write(tab_0 + tab_0 + tab_0)
    f.write('def func(' + params + '):')
    f.write(tab_1 + inputs_and_output_vars['output'] + ' = None')
    first = True
    for r in rules.all():
        f.write(mount_if(r, first))
        first = False
        f.write(mount_then(r))
    f.write(tab_1 + 'return ' + inputs_and_output_vars['output'])

    # inputs_and_output_vars['output']


def mount_if(r, first):
    if first:
        if_c = tab_1 + 'if '
    else:
        if_c = tab_1 + 'elif '
    for if_clause in r.if_clauses:
        if_c += ' '.join(if_clause) + " " + and_exp + " "
    return replace_last_ocurrency(if_c, ' and', ':')


def mount_then(r):
    then_c = tab_2
    for then in r.then:
        if then[len(then) - 1][0] != '[':
            then_c += ' '.join(then) + ' '
    return then_c


def write_imports(f, imports):
    f.write('import unittest\n')
    for i in imports:
        f.write(i)


def write_test_by_rules(f, rules: Rules):
    f.write(tab_0 + tab_0)
    f.write(tab_0 + 'class TestStringMethods(unittest.TestCase):')
    f.write(tab_1 + 'pass')
    f.write(tab_0)


def replace_last_ocurrency(s, old, new):
    return (s[::-1].replace(old[::-1], new[::-1], 1))[::-1]
