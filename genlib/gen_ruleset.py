import os


class Rule(object):

    def __init__(self):
        self.if_clauses = []
        self.then = []

    def add_if(self, if_clause):
        self.if_clauses.append(if_clause)

    def add_then(self, then):
        self.then.append(then)

    def is_empty(self):
        return len(self.if_clauses) == 0 and len(self.then) == 0


rule = Rule()
rules = []
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
    print 'Clauses:'
    print "============================================="
    for r in rules:
        print "if - " + r.if_clauses.__str__()
        print "then - " + r.then.__str__()
        print "============================================="
