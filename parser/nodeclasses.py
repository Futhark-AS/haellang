from dataclasses import dataclass
from __future__ import annotations


@dataclass
class ASTNode():
    pass

@dataclass
class ExpressionNode(ASTNode):
    pass

@dataclass
class GroupExpressionNode(ExpressionNode):
    inner_expression : ExpressionNode

@dataclass
class StatementNode(ASTNode):
    pass

@dataclass
class StatementsNode(ASTNode):
    head : StatementNode
    tail : StatementsNode

@dataclass
class EmptyNode(ASTNode):
    pass

@dataclass
class LiteralExpressionNode(ExpressionNode):
    literal: bool | str | int | float

@dataclass
class BinaryExpressionNode(ExpressionNode):
    left : ExpressionNode
    right : ExpressionNode

@dataclass
class DictBodyNode(ASTNode):
    key : ExpressionNode
    value : ExpressionNode
    tail : DictBodyNode

@dataclass
class DictExpressionNode(ExpressionNode):
    body : DictBodyNode

@dataclass
class ListBodyNode(ASTNode):
    head : ExpressionNode
    tail : ListBodyNode

@dataclass
class ListExpressionNode(ExpressionNode):
    body : ListBodyNode

@dataclass
class VariableExpressionNode(ExpressionNode):
    name : str

@dataclass
class ExpressionStatementNode(StatementNode):
    expression : ExpressionNode

@dataclass
class IfStatementNode(StatementNode):
    condition : ExpressionNode
    if_body : StatementsNode
    else_body : StatementsNode

@dataclass
class ParametersNode(ASTNode):
    name : str
    tail : ParametersNode

@dataclass
class FunctionExpressionNode(ExpressionNode):
    params : ParametersNode
    body : StatementsNode

@dataclass
class FunctionApplicationExpression(ExpressionNode):
    name : str
    args : ListBodyNode

@dataclass
class ReturnStatementNode(StatementNode):
    expression : ExpressionNode

@dataclass
class AssignStatementNode(StatementNode):
    name : str
    expression : ExpressionNode

@dataclass
class BreakStatementNode(StatementNode):
    pass
@dataclass
class WhileStatementNode(StatementNode):
    condition : ExpressionNode
    body : StatementsNode

@dataclass
class PrintStatementNode(StatementNode):
    expression : ExpressionNode
    newline : bool 

@dataclass
class PushExpressionNode(ExpressionNode):
    list_expression : ExpressionNode
    expression : ExpressionNode

@dataclass
class PopExpressionNode(ExpressionNode):
    list_expression : ExpressionNode

@dataclass
class ArrayIndexExpressionNode(ExpressionNode):
    list_expression : ExpressionNode
    index : ExpressionNode

@dataclass
class ChangeArrayIndexExpressionNode(ExpressionNode):
    list_expression : ExpressionNode
    index : ExpressionNode
    expression : ExpressionNode

@dataclass
class DictLookupExpressionNode(ExpressionNode):
    dict_expression : ExpressionNode
    key : ExpressionNode

@dataclass
class DictInsertExpressionNode(ExpressionNode):
    dict_expression : ExpressionNode
    key : ExpressionNode
    value : ExpressionNode

@dataclass
class DictRemoveExpressionNode(ExpressionNode):
    dict_expression : ExpressionNode
    key : ExpressionNode

@dataclass
class LengthExpressionNode(ExpressionNode):
    expression : ExpressionNode

@dataclass
class ImportStatementNode(StatementNode):
    module : str
    alias : str

@dataclass
class PassStatementNode(StatementNode):
    pass

@dataclass
class ImportedFunctionApplicationExpressionNode(ExpressionNode):
    module_alias : str
    name : str
    args : ListBodyNode
