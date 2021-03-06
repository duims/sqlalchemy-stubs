from typing import Any, Optional
from ... import types as _sqltypes
from ...types import INTEGER as INTEGER, BIGINT as BIGINT, SMALLINT as SMALLINT, DECIMAL as DECIMAL, NUMERIC as NUMERIC, \
    FLOAT as FLOAT, DATETIME as DATETIME, DATE as DATE, BINARY as BINARY, \
    TEXT as TEXT, VARCHAR as VARCHAR, NVARCHAR as NVARCHAR, CHAR as CHAR, NCHAR as NCHAR

class REAL(_sqltypes.REAL):
    __visit_name__: str = ...

class TINYINT(_sqltypes.Integer):
    __visit_name__: str = ...

class TIME(_sqltypes.TIME):
    __visit_name__: str = ...

class _DateTimeBase(object): ...

class SMALLDATETIME(_DateTimeBase, _sqltypes.DateTime):
    __visit_name__: str = ...

class DATETIME2(_DateTimeBase, _sqltypes.DateTime):
    __visit_name__: str = ...

class DATETIMEOFFSET(_sqltypes.TypeEngine[Any]):
    __visit_name__: str = ...

    def __init__(self, precision: Optional[int] = ..., **kwargs: Any) -> None: ...

class TIMESTAMP(_sqltypes._Binary):
    __visit_name__: str = ...

    def __init__(self, convert_int: bool = ...) -> None: ...

class ROWVERSION(TIMESTAMP):
    __visit_name__: str = ...

class NTEXT(_sqltypes.UnicodeText):
    __visit_name__: str = ...

class VARBINARY(_sqltypes.VARBINARY, _sqltypes.LargeBinary):
    __visit_name__: str = ...

class IMAGE(_sqltypes.LargeBinary):
    __visit_name__: str = ...

class XML(_sqltypes.Text):
    __visit_name__: str = ...

class BIT(_sqltypes.TypeEngine[int]):
    __visit_name__: str = ...

class MONEY(_sqltypes.TypeEngine[Any]):
    __visit_name__: str = ...

class SMALLMONEY(_sqltypes.TypeEngine[Any]):
    __visit_name__: str = ...

class UNIQUEIDENTIFIER(_sqltypes.TypeEngine[str]):
    __visit_name__: str = ...

class SQL_VARIANT(_sqltypes.TypeEngine[Any]):
    __visit_name__: str = ...
