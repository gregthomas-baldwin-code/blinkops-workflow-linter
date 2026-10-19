> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# String Utilities

> Utility actions for formatting, parsing, and transforming string data in Blink workflows.

## Byte Truncate String

Truncate a string to a specified number of bytes while preserving UTF-8 character boundaries.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | String | The input string to truncate. Can be provided with or without quotes. |
  | Max Bytes | The maximum number of bytes for the truncated string.<br /><br />Examples:<br />• `10` - 10 bytes<br />• `10000` - 10 kb<br />• `10000000` - 10 mb |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/5vRdj3j1qJ24yHPz/img/Utilities/string_utilities-bytetruncate.png?fit=max&auto=format&n=5vRdj3j1qJ24yHPz&q=85&s=55428871f994f103d3c01c870bd8b41f" width="1812" height="802" data-path="img/Utilities/string_utilities-bytetruncate.png" />
</Frame>

## Convert To Lower Case

Converts a string to lower case.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | String | The string which will be converted to lower case. For example: For the string - `Hello World`, the returned string will be: `hello world` |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/I0bBfTOFYhQg2L0_/img/Utilities/string_utilities-lower.png?fit=max&auto=format&n=I0bBfTOFYhQg2L0_&q=85&s=2256b29be70afdd61c938fc1a7899c40" width="1992" height="878" data-path="img/Utilities/string_utilities-lower.png" />
</Frame>

## Convert To Upper Case

Converts a string to upper case.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | String | The string which will be converted to upper case. For example: For the string - `Hello World`, the returned string will be: `HELLO WORLD` |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/UPn1JESoLe3D6-WO/img/Utilities/string_utilities-upper.png?fit=max&auto=format&n=UPn1JESoLe3D6-WO&q=85&s=c5ce8f199a1686f8b491e87f4eba25ec" width="1990" height="882" data-path="img/Utilities/string_utilities-upper.png" />
</Frame>

## Find String

Returns the index of the first occurrence of a substring within the given string. The action returns -1 if the value is not found.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | String | The original string where the `Value` will be searched. |
  | Substring | The substring to be find within the original `String`. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/I0bBfTOFYhQg2L0_/img/Utilities/string_utilities-find.png?fit=max&auto=format&n=I0bBfTOFYhQg2L0_&q=85&s=dd7601dff67e1276928e5587d3ea75e5" width="1988" height="876" data-path="img/Utilities/string_utilities-find.png" />
</Frame>

## Generate Random String

Generates a random string of specified length with the given character sets.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | String Length | The length of the generated string, default 10. |
  | Include Special Chars | `[!-*]` character set - `!@#$%&*`. |
  | Include Uppercase Chars | `[A-Z]` character set - `ABCDEFGHIJKLMNOPQRSTUVWXYZ`. |
  | Include Digit Chars | `[0-9]` character set - `0123456789`. |
  | Custom Characters | 'Characters that will be appended to character pool. For example: `Bl1#K@p$`.' |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/UPn1JESoLe3D6-WO/img/Utilities/string_utilities-random.png?fit=max&auto=format&n=UPn1JESoLe3D6-WO&q=85&s=30c86e970d7feff7a3bbccc33209173e" width="1988" height="878" data-path="img/Utilities/string_utilities-random.png" />
</Frame>

## Get String Length

Get length of a string.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | String | The string whose length will be returned. For example: For the string - `Hello World`, the returned value will be: 11 |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/I0bBfTOFYhQg2L0_/img/Utilities/string_utilities-length.png?fit=max&auto=format&n=I0bBfTOFYhQg2L0_&q=85&s=c4e9c0db0b4852658dbf643c77dde70b" width="1992" height="876" data-path="img/Utilities/string_utilities-length.png" />
</Frame>

## Join String

Concatenate any number of strings into a single string using an optional separator. Equivalent to Python's join() method.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | String List | The list of strings that needs to be concatenated. Also, it could be a single string like `"blink"`. In this case, each character will act as a 'substring'. For example: The input string - `"blink"` (with quotes) will act the same as the following input: `["b", "l", "i", "n", "k"]` |
  | Separator | The string that will be inserted in between each one of the 'Strings'. For example: For the string list - `["I", "Love", "Blink"]` and the separator - `#`, the returned string will be: `I#Love#Blink` |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/I0bBfTOFYhQg2L0_/img/Utilities/string_utilities-join.png?fit=max&auto=format&n=I0bBfTOFYhQg2L0_&q=85&s=89567dbe872fb4482cc47c9748240d14" width="1988" height="876" data-path="img/Utilities/string_utilities-join.png" />
</Frame>

## Replace String

Replaces a given substring with another string.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | String | The original string where replacements will be made. |
  | Old Substring | The substring to be find within the original `String` parameter. |
  | New Substring | The replacement substring. |
  | Count | The maximum number of replacements to perform. If empty, replaces all occurrences. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/UPn1JESoLe3D6-WO/img/Utilities/string_utilities-replace.png?fit=max&auto=format&n=UPn1JESoLe3D6-WO&q=85&s=2aa37029b7513f257b06cacffac541a2" width="1990" height="874" data-path="img/Utilities/string_utilities-replace.png" />
</Frame>

## Split String

Splits a given string according to the specified delimiter and returns a list of substrings.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | String | The string that needs to be split. |
  | Delimiter | The delimiter based on which the string will be split. For example: For the string - `Hello there, this is Blink's example!` and the delimiter - `,`, the returned list looks like the following: `["Hello there", " this is Blink's example!"]` |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/UPn1JESoLe3D6-WO/img/Utilities/string_utilities-split.png?fit=max&auto=format&n=UPn1JESoLe3D6-WO&q=85&s=6e12b246c88b0e11abbb347d019814cf" width="1990" height="882" data-path="img/Utilities/string_utilities-split.png" />
</Frame>

## Trim Spaces

Removes all leading and trailing whitespaces from a given string.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | String | The string that needs to be trimmed. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/UPn1JESoLe3D6-WO/img/Utilities/string_utilities-trimspace.png?fit=max&auto=format&n=UPn1JESoLe3D6-WO&q=85&s=0167b2e9bd62c88898f2d73af726edc7" width="1988" height="876" data-path="img/Utilities/string_utilities-trimspace.png" />
</Frame>

## Trim String

Shorten a string from either or both sides, using optional `Start` and `End` indexes. This action is based on Python's array slicing, where the start index is included and the end index is excluded.

For example, using the string `blinkops` and the input indexes `0` and `-3`, the output will be: `blink`. The same as if the `End` index was `5`.

Additional options:

* Use only `Start` to trim from the beginning: `Start: 2` → `inkops`
* Use only `End` to trim from the end: `End: 5` → `blink`
* Leave both empty to get the full string

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | String | The string that needs to be trimmed. |
  | Start Index | The index of the first character you want to **include** in the slice. The string will be trimmed from this index (inclusive). **Note**: The first character's index is `0`. |
  | End Index | The index of the first character you want to **exclude** from the slice. The string will be trimmed to this index (exclusive). **Note**: The last character's index is `-1` or the length of the string. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/UPn1JESoLe3D6-WO/img/Utilities/string_utilities-trimstring.png?fit=max&auto=format&n=UPn1JESoLe3D6-WO&q=85&s=9ac3e55146ff2d9e101db432efcf8a91" width="1988" height="878" data-path="img/Utilities/string_utilities-trimstring.png" />
</Frame>

## Truncate String

Shortens a given string to a limited number of characters.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | String | The string that will be shortened. |
  | Limit | The amount of characters the string will be limited to. For example: For the string - `Hello World` and the limit `8`, the returned value will be: `Hello Wo`<br />**Note**: You can truncate the string from the end using a `Negative Limit`. For instance: the limit `-2` will remove the last 2 characters. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/UPn1JESoLe3D6-WO/img/Utilities/string_utilities-truncate.png?fit=max&auto=format&n=UPn1JESoLe3D6-WO&q=85&s=f0a3a0e83419aded7f54cbdd7d4abdc5" width="1994" height="876" data-path="img/Utilities/string_utilities-truncate.png" />
</Frame>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.