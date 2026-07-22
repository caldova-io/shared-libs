export type Primitive = string | number | boolean | null | Date;

export class SqlQuery {
  private tableName = "";
  private selectedFields: string[] = ["*"];
  private filters: string[] = [];
  private sortClause = "";
  private rowLimit?: number;

  static from(table: string): SqlQuery {
    const query = new SqlQuery();
    query.tableName = table;
    return query;
  }

  select(fields: string[]): this {
    this.selectedFields = fields.length > 0 ? fields : ["*"];
    return this;
  }

  where(field: string, value: Primitive): this {
    this.filters.push(`${field} = ${this.render(value)}`);
    return this;
  }

  whereRaw(clause: string): this {
    this.filters.push(clause);
    return this;
  }

  orderBy(field: string, direction: "asc" | "desc" = "asc"): this {
    this.sortClause = ` ORDER BY ${field} ${direction.toUpperCase()}`;
    return this;
  }

  limit(count: number): this {
    this.rowLimit = count;
    return this;
  }

  toString(): string {
    const where = this.filters.length > 0 ? ` WHERE ${this.filters.join(" AND ")}` : "";
    const limit = this.rowLimit === undefined ? "" : ` LIMIT ${this.rowLimit}`;
    return `SELECT ${this.selectedFields.join(", ")} FROM ${this.tableName}${where}${this.sortClause}${limit}`;
  }

  private render(value: Primitive): string {
    if (value === null) return "NULL";
    if (value instanceof Date) return `'${value.toISOString()}'`;
    if (typeof value === "number") return String(value);
    if (typeof value === "boolean") return value ? "TRUE" : "FALSE";
    return `'${value}'`;
  }
}

export function buildInsert(table: string, record: Record<string, Primitive>): string {
  const fields = Object.keys(record);
  const values = fields.map((field) => renderValue(record[field]));
  return `INSERT INTO ${table} (${fields.join(", ")}) VALUES (${values.join(", ")})`;
}

function renderValue(value: Primitive): string {
  if (value === null) return "NULL";
  if (value instanceof Date) return `'${value.toISOString()}'`;
  if (typeof value === "number") return String(value);
  if (typeof value === "boolean") return value ? "TRUE" : "FALSE";
  return `'${value}'`;
}
