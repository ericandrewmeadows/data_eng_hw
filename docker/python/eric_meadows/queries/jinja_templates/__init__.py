CREATE_SCHEMA_IF_NOT_EXISTS = "create_schema_if_not_exists.jinja2"
DROP_AND_CREATE_TABLE_WITH_SCHEMA = "drop_and_create_table_with_schema.jinja2"

TEMPLATES = dict(
    CREATE_SCHEMA_IF_NOT_EXISTS=CREATE_SCHEMA_IF_NOT_EXISTS,
    DROP_AND_CREATE_TABLE_WITH_SCHEMA=DROP_AND_CREATE_TABLE_WITH_SCHEMA,
)

__all__ = ["TEMPLATES"]
