# -*- coding: utf-8 -*-
from typing import List, Optional

import util
from algo.stmts import BaseStmt, CodeBlock
from maths.nodes import AstNode


class BlockStmt(BaseStmt):
    def __init__(self, children: CodeBlock):
        super().__init__()
        self.set_children(children)

    def __str__(self):
        return "{ %s }" % ", ".join(str(x) for x in self.children)

    def __repr__(self):
        return "BlockStmt(%r)" % self.children

    def python(self) -> List[str]:
        header = self.python_header()
        lines = [l for sub in self.children for l in sub.python()]
        if header is not None:
            lines = ["\t" + l for l in lines]
            return [header] + lines
        return lines

    def python_header(self) -> Optional[str]:
        return None

    def set_children(self, children: CodeBlock):
        self.children = children
        for c in self.children:
            c.parent = self

    def get_children(self) -> List[AstNode]:
        return util.flatten(x.get_children() for x in self.children)
