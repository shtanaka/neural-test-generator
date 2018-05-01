import os, re


class Rule(object):

    def __init__(self):
        self.if_clauses = []
        self.then = []
        self.inputs = []

    def add_if(self, if_clause):
        self.if_clauses.append(if_clause)

    def add_then(self, then):
        self.then.append(then)

    def is_empty(self):
        return len(self.if_clauses) == 0 and len(self.then) == 0


class Rules(object):

    def __init__(self):
        self.rules = []

    def all(self) -> '[] of Rule':
        return self.rules

    def get(self, index: int) -> Rule:
        return self.rules[index]

    def count(self) -> int:
        return self.rules.__len__()

    def append(self, r: Rule):
        return self.rules.append(r)

    def get_inferred_inputs_and_output(self) -> []:
        if len(self.rules) > 0:
            return self.__find_inputs_from_rules()
        else:
            return None

    def __find_inputs_from_rules(self):
        r = self.rules[0]
        output = None
        inputs = []
        for thens in r.then:
            for string in thens:
                regex_search = re.search('[a-zA-Z]', string)
                if regex_search:
                    if not output:
                        output = string
                    else:
                        inputs.append(string)
        return {'inputs': inputs, 'output': output}

    def __getitem__(self, index):
        return self.rules[index]


rule: Rule = Rule()
rules = Rules()
status = ''


def map_data(file_path):
    global rules
    global rule
    global status
    if os.path.exists(os.path.dirname(file_path)):
        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                line_start = line.split(' ', 1)[0]
                process_line(line_start)
                if status == 'BREAK':
                    if not rule.is_empty():
                        rules.append(rule)
                    break
                elif status == 'RULE':
                    if not rule.is_empty():
                        rules.append(rule)
                        rule = Rule()
                elif status == 'IF':
                    if line_start == 'IF' or line == '':
                        pass
                    else:
                        rule.add_if(line.split(" "))
                elif status == 'THEN':
                    if line_start == 'THEN' or line == '':
                        pass
                    else:
                        rule.add_then(line.split(" "))


def process_line(line_start):
    global status
    if line_start == 'Rule:':
        status = 'RULE'
    elif line_start == 'IF':
        status = 'IF'
    elif line_start == 'THEN':
        status = 'THEN'
    elif line_start == 'Time':
        status = 'BREAK'
    elif line_start == '':
        pass
    else:
        pass
    # if status != '' and line_start != '' and line_start != 'THEN' and line_start != 'IF':
    #     print status


def print_clauses():
    global rules
    print('Clauses:')
    print("=============================================")
    for r in rules:
        print("if - " + r.if_clauses.__str__())
        print("then - " + r.then.__str__())
        print("=============================================")
