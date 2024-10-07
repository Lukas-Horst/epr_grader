__author__ = 'Lukas Horst'

import re


class ViolationChecker:

    __violation_groups = [
    'No deduction',
    'Global statements',
    'Imports',
    'Author variable',
    'Naming',
    'Docstring',
    'Spacing',
    'Classes',
    'Override',
    'Syntax'
    ]
    # {violation_name: [amount of the violation, description, violation_group]}
    __violations = None
    _style_check = ''
    __deduction = None

    def __init__(self, style_check: str, no_deduction: bool):
        self._style_check = style_check
        self.__deduction = no_deduction
        self.__violations = {'W0104': [0, 'Pointless statement', 0],
                        'W0201': [0, 'Attribute defined outside init', 7],
                        'W0231': [0, 'Super init not called', 7],
                        'W0232': [0, 'No init', 7],
                        'W0301': [0, 'Unnecessary semicolon', 0],
                        'W0311': [0, 'Bad indention', 6],
                        'W0401': [0, 'Wildcard import', 2],
                        'W0404': [0, 'Reimported', 2],
                        'W0603': [0, 'Global statement', 1],
                        'W0622': [0, 'Redefined builtin', 8],
                        'W0702': [0, 'Bare except', 0],
                        'W0705': [0, 'Duplicate except', 0],
                        'W0706': [0, 'Try except raise', 0],

                        'C0102': [0, 'Blacklisted name', 4],
                        'C0103': [0, 'Invalid name', 4],
                        'C0112': [0, 'Empty docstring', 5],
                        'C0114': [0, 'Missing module docstring', 5],
                        'C0115': [0, 'Missing class docstring', 5],
                        'C0116': [0, 'Missing function or method docstring', 5],
                        'C0121': [0, 'Singleton-comparison', 0],
                        'C0144': [0, 'Non ascii name', 4],
                        'C0321': [0, 'Multiple statements', 0],
                        'C0325': [0, 'Superfluous-parens', 0],
                        'C0410': [0, 'Multiple imports', 2],
                        'C0411': [0, 'Wrong import order', 2],
                        'C0412': [0, 'Ungrouped imports', 2],
                        'C0413': [0, 'Wrong import position', 2],
                        'C2100': [0, 'Missing author variable', 3],
                        'C2101': [0, 'Malformed author variable', 3],
                        'C2102': [0, 'Incorrectly assigned author variable', 3],

                        'E0001': [0, 'Syntax error', 9],
                        'E0102': [0, 'Function redefined', 8],
                        'E0211': [0, 'No Method argument', 7],
                        'E201': [0, 'Whitespace after \'(\'', 6],
                        'E202': [0, 'Whitespace before \')\'', 6],
                        'E203': [0, 'Whitespace before \':\'', 6],
                        'E211': [0, 'Whitespace before \'(\'', 6],
                        'E221': [0, 'Multiple spaces before operator', 6],
                        'E222': [0, 'Multiple spaces after operator', 6],
                        'E223': [0, 'Tab before operator', 6],
                        'E224': [0, 'Tab after operator', 6],
                        'E225': [0, 'Missing whitespace around operator', 6],
                        'E231': [0, 'Missing whitespace after \',\', \';\', or \':\'', 6],
                        'E251': [0, 'Unexpected spaces around keyword / parameter equals', 6],
                        'E261': [0, 'At least two spaces before inline comment', 6],
                        'E262': [0, 'Inline comment should start with \'# \'', 6],
                        'E265': [0, 'Block comment should start with \'# \'', 6],
                        'E271': [0, 'Multiple space after keyword', 6],
                        'E302': [0, 'Expected 2 blank lines', 6],
                        'E501': [0, 'Line too long > 99', 6],
                        'E502': [0, 'Backslash redundant between brackets', 0],
                        'E713': [0, 'Negative membership test should use \'not in\'', 0],
                        'E714': [0, 'Negative identity test should use \'is not\'', 0],
                        'E721': [0, 'Use \'isinstance\' instead of comparing types', 0]}

    def check_violations(self):
        """Method to search for all violations"""
        for violation_name, _ in self.__violations.items():
            all_violations = re.findall(rf',*{violation_name}.*', self._style_check)
            self.__violations[violation_name][0] = len(all_violations)

    def list_violation(self):
        """Method to return a list with all violations and the amount of the violations sort by
        groups"""
        violation_string = ''
        violation_groups_strings = []
        for i in range(10):
            violation_groups_strings.append('')
        for violation_name, value in self.__violations.items():
            violation_groups_strings[value[2]] += f'{violation_name} ({value[1]}): {value[0]}\n'
        for i, violation_group in enumerate(self.__violation_groups):
            if i == 0: continue
            violation_string += f'-----{violation_group}-----\n{violation_groups_strings[i]}'
            violation_amount = self.count_violations(i)
            violation_string += (f'\nFehler Insgesamt: {violation_amount}       Abzug: '
                                 f'{self.count_deduction(i, violation_amount)} Punkte\n\n')
            if i == 9:
                violation_string += f'-----No deduction-----\n{violation_groups_strings[0]}'
                violation_string += f'\nFehler Insgesamt: {violation_amount}       Abzug: 0 Punkte'
        return violation_string

    def count_violations(self, violation_group: int):
        """Method to count all violations"""
        all_violations = 0
        if violation_group == -1:
            for _, value in self.__violations.items():
                all_violations += value[0]
        else:
            for _, value in self.__violations.items():
                if value[2] == violation_group:
                    all_violations += value[0]
        return all_violations

    def count_deduction(self, violation_group: int, violation_amount=-1):
        """Method to count the deduction based on the group and amount"""
        if violation_amount == -1:
            violation_amount = self.count_violations(violation_group)
        if violation_group == 0:
            return 0
        elif violation_group == 3:
            if violation_amount > 0:
                # The deduction for the author variable
                return 2
            else:
                return 0
        elif not self.__deduction:
            return 0
        elif violation_group == 5:
            # Violation for docstrings with a max deduction
            return min(violation_amount*0.5, 2)
        else:
            # Cause group 6 is bigger it can get a higher deduction than 0.5
            if violation_group == 6 and violation_amount > 30:
                return 1
            elif violation_group == 6 and violation_amount > 20:
                return 0.75
            elif violation_amount > 9:
                return 0.5
            elif violation_amount > 1:
                return 0.25
            else:
                return 0
