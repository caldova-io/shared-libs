from datetime import date, datetime
from typing import Any

Primitive = str | int | float | bool | None | date | datetime


class SqlQuery:
    def __init__(self, table: str) -> None:
        self.table = table
        self.fields: list[str] = ["*"]
        self.filters: list[str] = []
        self.sort_clause = ""
        self.row_limit: int | None = None

    @classmethod
    def from_table(cls, table: str) -> "SqlQuery":
        return cls(table)

    def select(self, fields: list[str]) -> "SqlQuery":
        self.fields = fields or ["*"]
        return self

    def where(self, field: str, value: Primitive) -> "SqlQuery":
        self.filters.append(f"{field} = {self._render(value)}")
        return self

    def where_raw(self, clause: str) -> "SqlQuery":
        self.filters.append(clause)
        return self

    def order_by(self, field: str, direction: str = "asc") -> "SqlQuery":
        self.sort_clause = f" ORDER BY {field} {direction.upper()}"
        return self

    def limit(self, count: int) -> "SqlQuery":
        self.row_limit = count
        return self

    def to_sql(self) -> str:
        where = f" WHERE {' AND '.join(self.filters)}" if self.filters else ""
        limit = "" if self.row_limit is None else f" LIMIT {self.row_limit}"
        return f"SELECT {', '.join(self.fields)} FROM {self.table}{where}{self.sort_clause}{limit}"

    def _render(self, value: Primitive) -> str:
        if value is None:
            return "NULL"
        if isinstance(value, bool):
            return "TRUE" if value else "FALSE"
        if isinstance(value, (int, float)):
            return str(value)
        if isinstance(value, (date, datetime)):
            return f"'{value.isoformat()}'"
        return f"'{value}'"


def build_insert(table: str, record: dict[str, Primitive]) -> str:
    fields = list(record.keys())
    values = [_render_value(record[field]) for field in fields]
    return f"INSERT INTO {table} ({', '.join(fields)}) VALUES ({', '.join(values)})"


def _render_value(value: Primitive) -> str:
    if value is None:
        return "NULL"
    if isinstance(value, bool):
        return "TRUE" if value else "FALSE"
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, (date, datetime)):
        return f"'{value.isoformat()}'"
    return f"'{value}'"
