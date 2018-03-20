# -*- coding: utf-8 -*-

from maths.nodes import AstNode
from .BaseStmt import *


class ReturnStmt(BaseStmt):
    value = None

    def __init__(self, value: AstNode=None):
        super().__init__()
        self.value = value

    def __str__(self):
        return "[Return %s]" % self.value