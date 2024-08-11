from dataclasses import dataclass

from sqlalchemy.inspection import Inspectable
from sqlalchemy.sql._typing import _HasClauseElement
from sqlalchemy.sql.elements import ColumnElement, SQLCoreOperations
from sqlalchemy.sql.roles import (
    ExpressionElementRole,
    FromClauseRole,
    JoinTargetRole,
    TypedColumnsClauseRole,
)


@dataclass
class JoinArgs:
    target: (
        FromClauseRole
        | type
        | Inspectable[_HasClauseElement]
        | _HasClauseElement
        | JoinTargetRole
    )
    on_clause: (
        ColumnElement
        | _HasClauseElement
        | SQLCoreOperations
        | ExpressionElementRole
        | TypedColumnsClauseRole
    )
    is_outer: bool = False
    full: bool = False
