import re
import astroid
from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker


class EPRAuthorVariableChecker(BaseChecker):
    __implements__ = IAstroidChecker

    name = "epr-author-variable"
    priority = -10
    msgs = {
        "C2100": (
            "__author__ variable missing",
            "missing-author-variable",
            "All EPR modules need an author variable."
        ),
        "C2101": (
            "__author__ variable malformed",
            "malformed-author-variable",
            "Author varible string incorrect."
        ),
        "C2102": (
            "__author__ variable assigned incorrectly",
            "incorrectly-assigned-author-variable",
            "The author variable must be assigned a constant string."
        )
    }
    options = (
        (
            'use-pairs', {
                'default': False, 'type': 'yn', 'metavar': '<y_or_n>',
                'help': 'Check author variable for pairs rather than individuals'
            }
        ),
    )

    def __init__(self, linter):
        super(EPRAuthorVariableChecker, self).__init__(linter)
        self._found_author = False

    def visit_assign(self, node):
        if self._found_author:
            return
        if isinstance(node.targets[0], astroid.Subscript):
            return
        if node.targets[0].name != '__author__':
            return

        self._found_author = True
        if isinstance(node.value, astroid.node_classes.Const) \
                and node.value.pytype() == 'builtins.str':
            if self.linter.config.use_pairs:
                exp = re.compile(r'^[0-9]{7}, ?.+?, ?[0-9]{7}, ?.+')
            else:
                exp = re.compile(r'^[0-9]{7}, ?.+')
            if not exp.fullmatch(node.value.value):
                self.add_message('malformed-author-variable', node=node.value)
        else:
            self.add_message('incorrectly-assigned-author-variable', node=node.value)

    def leave_module(self, node):
        if not self._found_author:
            self.add_message('missing-author-variable', node=node)
        self._found_author = False


def register(linter):
    linter.register_checker(EPRAuthorVariableChecker(linter))
