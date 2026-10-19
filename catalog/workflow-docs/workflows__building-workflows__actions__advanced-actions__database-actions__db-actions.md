> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Run Database Actions

> Run Database Actions allow you to perform SQL statements against remote databases.

Blink supports multiple types of SQL servers and database providers:

<CardGroup>
  <Card title="PostgresSQL" icon="database" iconType="solid" horizontal />

  <Card title="MySQL" icon="database" iconType="solid" horizontal />

  <Card title="ClickHouse" icon="database" href="/docs/integrations/clickhouse" iconType="solid" horizontal />

  <Card title="Oracle Database" icon="database" iconType="solid" horizontal />

  <Card title="Microsoft SQL Server" icon="microsoft" href="/docs/integrations/microsoft-sql-server" iconType="solid" horizontal />

  <Card title="Snowflake" icon="snowflake" href="/docs/integrations/snowflake" iconType="solid" horizontal />

  <Card title="Vertica" icon="database" href="/docs/integrations/vertica" iconType="solid" horizontal />
</CardGroup>

All Run Database Actions enable you to view results in the following output formats:

* Table
* Comma Separated Values (CSV)
* JSON

**Note:** There is a max limit on the amount of data returned.
Use `SELECT`, `WHERE`, and `LIMIT` clauses to reduce the result size.

## Creating a connection

For [Snowflake](/docs/integrations/snowflake/#creating-a-snowflake-connection) and [Vertica](/docs/integrations/vertica/#creating-a-vertica-connection), refer to their corresponding documentation pages.

For the other database types, you can connect in two ways:

### Connecting via password

1. Access your database server.
2. Choose which account and database you wish to connect with.
3. In the Blink platform, choose the type of server (Postgres, MySQL, etc.).
4. Insert your username and password.
5. Insert the hostname (IP or domain) of the server along with the port number to connect with.
6. Insert the name of the database to use to connect.

### Connecting via Database Source Name

You can connect directly via a Database Source Name (DSN) to pass any unique connection or authentication parameters.

Refer to the [Postgres](https://github.com/jackc/pgx/blob/279c3c0a20e0dbee3c4b644f58e5e3b3de8e051f/pgconn/config.go#L32),
[MySQL](https://github.com/go-sql-driver/mysql#dsn-data-source-name), and [ClickHouse](https://github.com/ClickHouse/clickhouse-go#dsn)
documentation on how to format their respective DSN strings.

## Actions

### Run Postgres Query

Runs a PostgreSQL query on a database.

| Parameter | Description |
| - | - |
| SQL Query | SQL statement to execute. |
| Output format | Representation of the output result. |

<Frame>
  <img src="https://mintcdn.com/blinkops-2/3_6WnkGGmnkZFzEe/img/Actions/RunPostgresQuery.png?fit=max&auto=format&n=3_6WnkGGmnkZFzEe&q=85&s=4db1a7fa10166f023d57cb59614f395b" width="1814" height="802" data-path="img/Actions/RunPostgresQuery.png" />
</Frame>

### Run MySQL Query

Runs a MySQL query on a database.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | SQL Query | SQL statement(s) to execute. |
  | Output format | Representation of the output result. When executing multiple statements, only the first statement's results will be displayed. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/3_6WnkGGmnkZFzEe/img/Actions/RunMySQLQuery.png?fit=max&auto=format&n=3_6WnkGGmnkZFzEe&q=85&s=0783691e7bd61f8ee06444b73a66d5c7" width="1810" height="806" data-path="img/Actions/RunMySQLQuery.png" />
</Frame>

### Run Oracle Database Query

Run a query on an Oracle database.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Query | SQL or PL/SQL statement(s) to execute.<br /><br />For SQL queries, use standard SQL syntax without a semicolon at the end. For PL/SQL blocks, include semicolons within the block and end with a semicolon, for example -<br /><br />`<br/>begin DBMS_LOCK.sleep(7); end;<br/>` |
  | Output Format | Representation of the output result. Only the first statement's results will be displayed. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/3_6WnkGGmnkZFzEe/img/Actions/RunOracleDatabaseQuery.png?fit=max&auto=format&n=3_6WnkGGmnkZFzEe&q=85&s=fa6216aeb34cfa099b90dbddd9904359" width="1812" height="802" data-path="img/Actions/RunOracleDatabaseQuery.png" />
</Frame>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.