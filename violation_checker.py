__author__ = 'Lukas Horst'

import re


class ViolationChecker:

    w0311 = 0  # Bad indention
    w0401 = 0   # Wildcard import
    w0622 = 0   # Redefined builtin
    c0103 = 0   # Invalid name
    c0116 = 0   # Missing function or method docstring
    c0114 = 0   # Missing module docstring
    c0121 = 0   # Singleton-comparison
    c0325 = 0   # Superfluous-parens
    c0413 = 0   # Wrong import position
    c2100 = 0   # Missing author variable
    c2101 = 0   # Malformed author variable
    c2102 = 0   # Incorrectly assigned author variable
    e0001 = 0   # Syntax error
    e0102 = 0   # Function redefined
    e231 = 0    # Missing whitespace after ','
    e251 = 0    # Unexpected spaces around keyword / parameter equals
    e261 = 0    # At least two spaces before inline comment
    e265 = 0    # Block comment should start with '# '
    e271 = 0    # Multiple space after keyword
    e302 = 0    # Expected 2 blank lines
    e501 = 0    # Line too long > 99
    style_check = ''


    def __init__(self, style_check):
        self.style_check = style_check


    def check_violations(self):
        w0311_violations = re.findall(r',*W0311.*', self.style_check)
        self.w0311 = len(w0311_violations)

        w0401_violations = re.findall(r',*W0401.*', self.style_check)
        self.w0401 = len(w0401_violations)

        w0622_violations = re.findall(r',*W0622.*', self.style_check)
        self.w0622 = len(w0622_violations)

        c0103_violations = re.findall(r',*C0103.*', self.style_check)
        self.c0103 = len(c0103_violations)

        c0114_violations = re.findall(r',*C0114.*', self.style_check)
        self.c0114 = len(c0114_violations)

        c0116_violations = re.findall(r',*C0116.*', self.style_check)
        self.c0116 = len(c0116_violations)

        c0121_violations = re.findall(r',*C0121.*', self.style_check)
        self.c0121 = len(c0121_violations)

        c0325_violations = re.findall(r',*C0325.*', self.style_check)
        self.c0325 = len(c0325_violations)

        c0413_violations = re.findall(r',*C0413.*', self.style_check)
        self.c0413 = len(c0413_violations)

        c2100_violations = re.findall(r',*C2100.*', self.style_check)
        self.c2100 = len(c2100_violations)

        c2101_violations = re.findall(r',*C2101.*', self.style_check)
        self.c2101 = len(c2101_violations)

        c2102_violations = re.findall(r',*C2102.*', self.style_check)
        self.c2102 = len(c2102_violations)

        e0001_violations = re.findall(r',*E0001.*', self.style_check)
        self.e0001 = len(e0001_violations)

        e0102_violations = re.findall(r',*E0102.*', self.style_check)
        self.e0102 = len(e0102_violations)

        e265_violations = re.findall(r',*E265.*', self.style_check)
        self.e265 = len(e265_violations)

        e501_violations = re.findall(r',*E501.*', self.style_check)
        self.e501 = len(e501_violations)

        e302_violations = re.findall(r',*E302.*', self.style_check)
        self.e302 = len(e302_violations)

        e231_violations = re.findall(r',*E231.*', self.style_check)
        self.e231 = len(e231_violations)

        e261_violations = re.findall(r',*E261.*', self.style_check)
        self.e261 = len(e261_violations)

        e271_violations = re.findall(r',*E271.*', self.style_check)
        self.e271 = len(e271_violations)

        e251_violations = re.findall(r',*E251.*', self.style_check)
        self.e251 = len(e251_violations)


    def list_violation(self):
        violations = ''
        violations += (f'W03111 (Bad indention): {self.w0311}'
                       f'\nW0401 (Wildcard import): {self.w0401}'
                       f'\nW0622 (Redefined builtin): {self.w0622}'
                       f'\nC0103 (Invalid name): {self.c0103}'
                       f'\nC0114 (Missing module docstring): {self.c0114}'
                       f'\nC0116 (Missing function or method docstring): {self.c0116}'
                       f'\nC0121 (Singleton-comparison): {self.c0121}'
                       f'\nC0325 (Superfluous-parens): {self.c0325}'
                       f'\nC0413 (Wrong import position): {self.c0413}'
                       f'\nC2100 (Missing author variable): {self.c2100}'
                       f'\nC2101 (Missing author variable): {self.c2101}'
                       f'\nC2102 (Incorrectly assigned author variable): {self.c2102}'
                       f'\nE0001 (Syntax error): {self.e0001}'
                       f'\nE0102 (Function redefined): {self.e0102}'
                       f'\nE231 (Missing whitespace after \',\'): {self.e231}'
                       f'\nE251 (Unexpected spaces around keyword / parameter equals): {self.e251}'
                       f'\nE261 (At least two spaces before inline comment): {self.e261}'
                       f'\nE265 (Block comment should start with \'# \'): {self.e265}'
                       f'\nE271 (Multiple space after keyword): {self.e271}'
                       f'\nE302 (Expected 2 blank lines): {self.e302}'
                       f'\nE501 (Line too long > 99): {self.e501}')
        return violations


if __name__ == '__main__':
    with open('G02_Voll/abgaben/Cynthia Celoudis_691452_assignsubmission_file/stylecheck.txt', 'r',
              encoding='utf-8') as file:
        file_content = file.read()
    violation_checker = ViolationChecker(file_content)
    violation_checker.check_violations()
    print(violation_checker.list_violation())
