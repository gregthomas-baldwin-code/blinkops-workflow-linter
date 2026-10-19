> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Functions

> Use expression language functions to manipulate and transform dynamic variables in Blink workflows.

To apply functions to a dynamic variable or a static variable you must wrap the chosen function in the double curly brackets syntax: `{{}}`, as seen in the following example.
In the following example we are using the [`decode_base_64(s)` string manipulation function](#string-manipulation-functions) to decode a Base64-encoded string (a static variable) and return the original decoded string.

<Frame>
  <video controls autoPlay muted zoom loop allowFullScreen className="w-full aspect-video" src="https://www.dropbox.com/scl/fi/w9w2njanl2wwjv0g7o39g/DynamicVarFunction.mp4?rlkey=ch4elbek8opipcgdd2qol363j&st=lxbb5x10&raw=1" />
</Frame>

<Tip>
  You can also use [Utility Actions](/docs/workflows/building-workflows/actions/actions#action-types) to apply specific function logic to dynamic variables throughout the workflow.
</Tip>

## Supported Functions

### String Manipulation Functions

<div className="integrations-table">
  | Function | Description | Example | Notes |
  | - | - | - | - |
  | `split(s, separator)` | Slices `s` into all substrings separated by the specified separator and returns a list of those substrings. | `split("a,b,c", ",")` → `["a", "b", "c"]` | The separator must be provided as a quoted string literal, such as `","`. |
  | `replace(s, old, new)` | Returns a copy of the string `s` with all instances of `old` replaced by `new`. | `replace("hello world", "world", "Blink")` → `"hello Blink"` | `old` and `new` must be provided as quoted string literals. |
  | `trim(s, cutset)` | Returns a slice of the string `s` with all leading and trailing Unicode code points contained in `cutset` removed. | `trim("!!hello!!", "!")` → `"hello"` | The `cutset` must be provided as a quoted string literal. |
  | `trim_space(s)` | Returns a slice of the string `s` with all leading and trailing whitespace removed, as defined by Unicode. | `trim_space("  hello world  ")` → `"hello world"` | Removes whitespace from the beginning and end of the string only. |
  | `trim_prefix(s, prefix)` | Returns `s` without the provided leading prefix string. If `s` doesn't start with `prefix`, `s` is returned unchanged. | `trim_prefix("https://blinkops.com", "https://")` → `"blinkops.com"` | The prefix must be provided as a quoted string literal. |
  | `trim_suffix(s, suffix)` | Returns `s` without the provided trailing suffix string. If `s` doesn't end with `suffix`, `s` is returned unchanged. | `trim_suffix("report.json", ".json")` → `"report"` | The suffix must be provided as a quoted string literal. |
  | `str(input)` | Converts an input to a string value. | `str(12345)` → `"12345"` | Useful when a value must be explicitly converted to a string. |
  | `max_str(input)` | Receives a list of strings and returns the largest one by lexicographical order. | `max_str(["apple", "banana", "cherry"])` → `"cherry"` | Values are compared lexicographically, not by string length. |
  | `max_num(input)` | Receives a list of numbers and returns the largest one. | `max_num([10, 25, 5])` → `25` | The input must contain numeric values. |
  | `query_escape(input)` | Escapes the given string into URL query encoding. | `query_escape("hello world!")` → `"hello+world%21"` | Useful when inserting values into URL query parameters. |
  | `query_unescape(input)` | Decodes the given URL query-encoded string. | `query_unescape("hello+world%21")` → `"hello world!"` | Reverses URL query encoding. |
  | `encode_base_64(input)` | Encodes any input value to a Base64-encoded string. | `encode_base_64("hello")` → `"aGVsbG8="` | Returns the Base64-encoded representation of the input. |
  | `decode_base_64(s)` | Decodes a Base64-encoded string and returns the original decoded string. | `decode_base_64("aGVsbG8=")` → `"hello"` | The input must be a valid Base64-encoded string. |
  | `is_uuid(input)` | Checks whether the input string is a valid UUID. | `is_uuid("550e8400-e29b-41d4-a716-446655440000")` → `true` | Returns `true` for a valid UUID format and `false` otherwise. |
  | `to_lower(input)` | Changes all input characters to lowercase. | `to_lower("HELLO WORLD")` → `"hello world"` | Useful for normalizing string values before comparison. |
  | `to_upper(input)` | Changes all input characters to uppercase. | `to_upper("hello world")` → `"HELLO WORLD"` | Useful for normalizing string values before comparison. |
</div>

***

### Table Manipulation Functions

<div className="integrations-table">
  | Function | Description |
  | - | - |
  | `table_to_csv(input)` | Produces CSV output from a table format step output. |
  | `table_to_ascii(input)` | Produces ASCII table output from a table format step output. |
  | `table_to_html(input)` | Produces HTML table output from table step output. |
</div>

***

### Array & List Functions

<div className="integrations-table">
  | Function | Description |
  | - | - |
  | `reverse(arr)` | Returns an array in reverse order of its indices. |
  | `empty(arr)` | Checks whether an array or string is empty. |
  | `not_empty(arr)` | Checks whether an array or string is not empty. |
  | `safe_contains(arr, val)` | Checks if an array contains a value safely. |
  | `query_arr_format(arr)` | Formats an array for query usage. |
  | `range(start, end)` | Generates a numeric range between two values. |
</div>

***

### Numeric Functions

<div className="integrations-table">
  | Function | Description |
  | - | - |
  | `int(input)` | Converts input to an integer. |
  | `float(input)` | Converts input to a float. |
  | `safe_add(a, b)` | Safely adds two numbers. |
  | `safe_sub(a, b)` | Safely subtracts two numbers. |
  | `increment(n)` | Increments a number by one. |
  | `divide(a, b)` | Divides two numbers. |
  | `modulo(a, b)` | Returns the remainder of division. |
  | `max_num(input)` | Receives a list of numbers and returns the largest one. |
</div>

***

### Boolean & Comparison Functions

<div className="integrations-table">
  | Function | Description |
  | - | - |
  | `boolean(input)` | Converts input into a boolean value. |
  | `bool(input)` | Alias for boolean conversion. |
  | `exists(input)` | Returns true if the input exists and is not null. |
  | `safe_eq(a, b)` | Safely checks equality between two values. |
  | `safe_lt(a, b)` | Safely checks if a is less than b. |
  | `safe_gt(a, b)` | Safely checks if a is greater than b. |
</div>

***

### JSON & Object Functions

<div className="integrations-table">
  | Function | Description |
  | - | - |
  | `prettify_json(input)` | Format a JSON with human-readable spacing. |
  | `prettifyJSON(input)` | Alias for prettify\_json. |
  | `obj(kv...)` | Creates a JSON object. |
  | `arr(values...)` | Creates a JSON array. |
  | `bool_or_null(v)` | Returns a boolean or null. |
  | `int_or_null(v)` | Returns an integer or null. |
  | `float_or_null(v)` | Returns a float or null. |
  | `obj_or_null(v)` | Returns an object or null. |
  | `arr_or_null(v)` | Returns an array or null. |
</div>

***

### Utility & Generator Functions

<div className="integrations-table">
  | Function | Description |
  | - | - |
  | `random(min, max)` | Returns a randomly generated number between two values. |
  | `random_uuid()` | Returns a randomly generated UUID. |
  | `sort_events(arr)` | Sorts events chronologically. |
  | `md5(input)` | Returns an MD5 hash of the input. |
  | `parse_severity(input)` | Parses a severity value. |
  | `quote_literal(input)` | Escapes and quotes an input value. |
  | `value_or_default(value, defaultValue)` | Returns `value` if it is not `null`; otherwise returns `defaultValue`. |
</div>

***

### URL & Map Functions

<div className="integrations-table">
  | Function | Description |
  | - | - |
  | `query_escape(input)` | URL-encodes a query string. |
  | `query_unescape(input)` | Decodes a URL-encoded query string. |
  | `encode_url_with_percent_space(input)` | Encodes a URL using percent-encoded spaces. |
  | `keyvalue_to_map(input)` | Converts key-value pairs into a map. |
  | `merge_maps(m1, m2)` | Merges two maps together. |
  | `cleanup_map(map)` | Removes empty or null values from a map. |
  | `append_keyvalue_to_map(map, kv)` | Appends a key-value pair to a map. |
  | `map_to_query(map)` | Converts a map into a query string. |
  | `decode_key_value_body(body)` | Decodes a URL-encoded request body. |
</div>

***

### Date-Time Functions

<Note>
  Please note that the following date & time formats are accepted.

  1. Epoch time in seconds: `1725916800`
  2. Epoch time in milliseconds: `1725916800000`
  3. RFC3339: `2006-01-02T15:04:05Z07:00`
  4. ISO: `2006-01-02T15:04:05Z0700`
  5. RFC3339 Nano:` 2006-01-02T15:04:05.999999999Z07:00`

  The **default date format** is dates in UTC timezone in [RFC3339 format](https://datatracker.ietf.org/doc/html/rfc3339).
</Note>

<div className="integrations-table">
  | Function | Description |
  | - | - |
  | `now()` | Returns the current time in RFC3339 format. |
  | `now_unix()` | Returns the elapsed epoch current time in seconds. |
  | `now_unix_mili()` | Returns the elapsed epoch current time in milliseconds. |
  | `today()` | Returns the current date at midnight UTC. |
  | `to_date(input)` | Converts input into a date object. |
  | `to_epoch(input)` | Converts a date to epoch seconds. |
  | `to_epoch_mili(input)` | Converts a date to epoch milliseconds. |
  | `to_local_time(date, tz)` | Formats the date as local time in a given time zone. |
  | `date_format(layout, date)` | Formats the date using Golang layout conventions. |
  | `max_date(input)` | Receives a list of dates and returns the most recent one. |
  | `add(date, duration)` | Adds a duration to a date. |
  | `sub(date, duration)` | Subtracts a duration from a date. |
</div>

***

#### Date Arithmetic

To add and subtract time interval from another time use **+** and **-**

```bash theme={"dark"}
to_date("2022-11-13T08:26:02Z") + "3h"  ==> 2022-11-13T11:26:02Z
to_date("2022-11-13T08:26:02Z") - "5m"  ==> 2022-11-13T08:21:02Z
```

Supported intervals:

```bash theme={"dark"}
	"s":  Second
	"m":  Minute
	"h":  Hour
```

<Note>**Note**: **Day**, **Month** and **Year** are not supported because they have variable lengths.</Note>

#### To Date

Use `to_date` to transform date string representation or date represented as Epoch time (seconds since 1970-01-01) into date. This enables performing date operations on the date such as **+/-**.

```bash theme={"dark"}
to_date("2022-11-13T08:26:02Z") + "3h"  ==> 2022-11-13T11:26:02Z
to_date(211863600) ==> 1976-09-18T03:00:00Z
```

#### To Epoch

Transforms the date string into Epoch time (seconds since 1970-01-01).
Also works with input which is already an Epoch, in which case it returns the input as is.

```bash theme={"dark"}
to_epoch("1976-09-18T03:00:00Z") ==> 211863600
to_epoch("211863600") ==> 211863600
```

#### To Epoch Mili

Transforms the date string into Epoch Milliseconds time (milliseconds since 1970-01-01).
Also works with input which is already an Epoch Milliseconds, in which case it returns the input as is.

```bash theme={"dark"}
to_epoch_mili("1976-09-18T03:00:00Z") ==> 211863600000
to_epoch_mili("211863600000") ==> 211863600000
```

#### To Local Time

Format the date as local time in a given time zone. Accepts dates as Epoch time or string in [RFC3339 format](https://datatracker.ietf.org/doc/html/rfc3339).

```bash theme={"dark"}
to_local_time("2020-01-31T18:09:41Z", "UTC")
  ==>  2020-01-31T18:09:41Z
to_local_time("2020-01-31T18:09:41Z", "Europe/Berlin")
  ==> 2020-01-31T19:09:41+01:00
to_local_time("2020-01-31T18:09:41Z", "America/New_York")
  ==> 2020-01-31T13:09:41-05:00
```

#### Date Format

Format the date in a requested format.

**Inputs:**

1. Layout in Golang date format convention (use exact pattern values).
2. Input date in [RFC3339 format](https://datatracker.ietf.org/doc/html/rfc3339) or as an Epoch time (seconds since 1970-01-01).

**Common Format Patterns:**

| Pattern | Use Case |
| - | - |
| `2006-01-02` | ISO date |
| `2006-01-02T15:04:05Z07:00` | RFC3339/ISO 8601 |
| `January 2, 2006` | Human-readable |
| `01/02/2006` | US format |
| `02/01/2006` | European format |
| `3:04PM` | Time only (12h) |
| `15:04:05` | Time only (24h) |
| `Mon Jan 2, 2006` | Day with date |

For more information and additional valid layouts, refer to [Golang date format convention documentation](https://pkg.go.dev/time#Layout).

**Examples:**

```bash theme={"dark"}
date_format("2006-01-02T15:04:05.000Z", "2022-07-07T15:14:12Z")
   ==>  2022-07-07T15:14:12.000Z
date_format("2006-01-02", "2022-07-07T15:14:12Z")
	 ==> 2022-07-07
date_format("2006-01-02", "2022-07-07T15:14:12Z") + "24h"
	 ==> 2022-07-08
```


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.