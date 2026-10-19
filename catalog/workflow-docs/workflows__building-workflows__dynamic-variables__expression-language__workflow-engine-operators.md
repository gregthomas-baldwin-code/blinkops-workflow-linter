> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Operators and Literals

> Use expression language operators to combine and modify dynamic variables in Blink workflows.

To apply operators to a dynamic variable or to a static variable, you must wrap the chosen function in the double curly brackets syntax: `{{}}`, as seen in the following example.
This example demonstrates the use of the [`array[:]` slice function](#slices) with a **step** dynamic variable. It extracts elements from the step output starting from index 2 (inclusive), to index 4 (exclusive). So, it retrieves the elements at indices 2 and 3.

```The Syntax theme={"dark"}
{{ steps.last.output[2:4]}}
```

<Frame>
  <video controls autoPlay muted zoom loop allowFullScreen className="w-full aspect-video" src="https://www.dropbox.com/scl/fi/wc5cb9bsdx4ez4ssvarv8/OperatorsDynamicVars.mp4?rlkey=v6mrjovoerbindlgx39mzudrv&st=vuetrp7m&raw=1" />
</Frame>

<Tip>
  You can also use [Utility Actions](/docs/workflows/building-workflows/actions/actions#action-types) to apply specific operator logic to dynamic variables throughout the workflow.
</Tip>

## Supported literals

The following literals are supported:

1. **strings** - single and double quotes (e.g. `"hello"`, `'hello'`)
2. **numbers** - e.g. `103`, `2.5`, `.5`
3. **arrays** - e.g. `[1, 2, 3]`
4. **maps** - e.g. `{foo: "bar"}`
5. **booleans** - `true` and `false`
6. **nil** - `nil`

## Digit separators

Integer literals may contain digit separators to allow digit grouping into more legible forms.

Example:

```
10_000_000_000
```

## Accessing public properties

Public properties on structs can be accessed by using the `.` syntax.
If you pass an array into an expression, use the `[]` syntax to access array keys.

```js theme={"dark"}
foo.Array[0].Value;
```

## Functions and methods

Functions may be called using `()` syntax. The `.` syntax can also be used to call methods on a struct.

```js theme={"dark"}
price.String();
```

## Supported operators

Operators are symbols or keywords that perform actions on values, like adding, comparing, or combining them. Supported operators include:

### Arithmetic operators

* `+` (addition)
* `-` (subtraction)
* `*` (multiplication)
* `/` (division)
* `%` (modulus)
* `**` (pow)

Example:

```js theme={"dark"}
life + universe + everything;
```

### Comparison operators

* `==` (equal)
* `!=` (not equal)
* `<` (less than)
* `>` (greater than)
* `<=` (less than or equal to)
* `>=` (greater than or equal to)

### Logical operators

* `not` or `!`
* `and` or `&&`
* `or` or `||`

Example:

```
life < universe || life < everything
```

### String operators

* `+` (concatenation)
* `matches` (regex match)
* `contains` (string contains)
* `startsWith` (has prefix)
* `endsWith` (has suffix)

To test if a string does *not* match a regex, use the logical `not` operator in combination with the `matches` operator:

```js theme={"dark"}
not ("foo" matches "^b.+")
```

You must use parenthesis because the unary operator `not` has precedence over the binary operator `matches`.

Example:

```js theme={"dark"}
"Arthur" + " " + "Dent";
```

Result will be set to `Arthur Dent`.

### Membership operators

* `in` (contain)
* `not in` (does not contain)

Example:

```js theme={"dark"}
user.Group in ["human_resources", "marketing"];
```

```js theme={"dark"}
"foo" in { foo: 1, bar: 2 };
```

### Ternary operators

* `foo ? 'yes' : 'no'`

Example:

```js theme={"dark"}
user.Age > 30 ? "mature" : "immature";
```

## Built-in functions

* `len` (length of array, map or string)
* `all` (will return `true` if all element satisfies the predicate)
* `none` (will return `true` if all elements do NOT satisfy the predicate)
* `any` (will return `true` if any element satisfies the predicate)
* `one` (will return `true` if exactly ONE element satisfies the predicate)
* `filter` (filter array by the predicate)
* `map` (map all items with the closure)
* `count` (returns number of elements what satisfies the predicate)

Examples:

Ensure all tweets are less than 280 chars.

```js theme={"dark"}
all(Tweets, {.Size < 280})
```

Ensure there is exactly one winner.

```js theme={"dark"}
one(Participants, {.Winner})
```

## Closures

* `{...}` (closure)

Closures allowed only with builtin functions. To access current item use `#` symbol.

```js theme={"dark"}
map(0..9, {# / 2})
```

If the item of array is struct, it's possible to access fields of struct with omitted `#` symbol (`#.Value` becomes `.Value`).

```js theme={"dark"}
filter(Tweets, {len(.Value) > 280})
```

## Slices

* `array[:]` (slice)

Slices can work with arrays or strings.

Example:

Variable `array` is `[1,2,3,4,5]`.

```js theme={"dark"}
array[1:5] == [2,3,4]
array[3:] == [4,5]
array[:4] == [1,2,3]
array[:] == array
```

## Examples:

```json theme={"dark"}
{{ steps.last.status == 'OK' }}
{{ steps.S1.output + ' ' + steps.S2.output }}
{{ steps.last.output contains "test" }}
{{ len(steps.last.output) }}
{{ steps.last.output[10:14] }}
```


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.