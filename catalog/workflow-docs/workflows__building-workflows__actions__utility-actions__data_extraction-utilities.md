> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Extraction Utilities

> Apply regular expressions to identify and extract defined patterns of data.

## Extract all data Types

Extract specified data types from the given text or JSON, supporting custom regex-based filtering for precise data retrieval.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Text Or JSON | The input text or JSON from which patterns will be extracted. |
  | Data Types | Select data types to search for within the input text or JSON, each selected type will be used to identify relevant matches in the text. |
  | RegExes | A list of custom regular expression patterns to match within the input text or JSON. Multiple regex patterns can be provided, separated by the OR operator. These patterns allow free-form searching beyond the predefined data types. |
  | Remove Duplicates | When checked, repeated values in each array in the final result are removed. |
</div>

<Note>
  **Note:**

  Use two vertical bar symbols || as the OR operator when writing expressions in the RegExes list.
</Note>

### Data Types

Each predefined regex will search for specific matching data in the text or JSON inputs:

* **CVEs** - Extracts Common Vulnerabilities and Exposures (CVE) identifiers in the format `CVE-YYYY-NNNN` to `CVE-YYYY-NNNNNNN`, where the year is four digits and the ID ranges from four to seven digits.
* **Email Addresses** - Extracts complete email addresses including the username and domain parts (e.g., `user@example.com`).
* **Email Domains** - Extracts only the domain portion from email addresses (e.g., `example.com` from `user@example.com`).
* **IPV4** - Extracts valid IPv4 addresses (e.g., `192.168.0.1`) within the standard range (`0.0.0.0` to `255.255.255.255`).
* **IPV6** - Extracts full IPv6 addresses in standard colon-separated hexadecimal format (e.g., `2001:0db8:85a3:0000:0000:8a2e:0370:7334`).
* **MD5** - Extracts 32-character hexadecimal MD5 hash strings.
* **SHA1** - Extracts 40-character hexadecimal SHA-1 hash strings.
* **SHA256** - Extracts 64-character hexadecimal SHA-256 hash strings.
* **URL Domains** - Extracts domain names from URLs, including subdomains, but excluding the protocol and path (e.g., `example.com` from `https://example.com/page`).
* **URLs** - Extracts full URLs starting with a protocol (e.g.,`https://`, `ftp://`, `file:///`), followed by a domain and optional path, query, or fragment (e.g., `https://www.google.com/`, `https://example.com/images/avatar`).

#### Results without removing duplicates

<Frame>
  <img src="https://mintcdn.com/blinkops-2/ZUtie3exEe7_7B_M/img/Actions/ExtractAllDataTypesWithDuplicates.png?fit=max&auto=format&n=ZUtie3exEe7_7B_M&q=85&s=d84b7976299434ff6e505451a7dec3b1" width="1207" height="712" data-path="img/Actions/ExtractAllDataTypesWithDuplicates.png" />
</Frame>

#### Results after removing duplicates

<Frame>
  <img src="https://mintcdn.com/blinkops-2/ZUtie3exEe7_7B_M/img/Actions/ExtractAllDataTypesWithoutDuplicates.png?fit=max&auto=format&n=ZUtie3exEe7_7B_M&q=85&s=51ebfa3fceaf1832aa0fb69a32800525" width="1207" height="712" data-path="img/Actions/ExtractAllDataTypesWithoutDuplicates.png" />
</Frame>

## Extract Email Addresses

Get all email addresses extracted from the provided input.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Text or JSON | The input text or JSON object to extract email addresses from. |
  | Remove Duplicates | When checked, repeated values in the final result are removed. |
</div>

#### Results without removing duplicates

<Frame>
  <img src="https://mintcdn.com/blinkops-2/ZUtie3exEe7_7B_M/img/Actions/ExtractEmailAddressesWithDups.png?fit=max&auto=format&n=ZUtie3exEe7_7B_M&q=85&s=0ed51adc1d198325e9faab307843c332" width="1814" height="808" data-path="img/Actions/ExtractEmailAddressesWithDups.png" />
</Frame>

#### Results after removing duplicates

<Frame>
  <img src="https://mintcdn.com/blinkops-2/ZUtie3exEe7_7B_M/img/Actions/ExtractEmailAddressesWithoutDups.png?fit=max&auto=format&n=ZUtie3exEe7_7B_M&q=85&s=21ae2b38aded11dd65f21bb11eaa20d3" width="1810" height="800" data-path="img/Actions/ExtractEmailAddressesWithoutDups.png" />
</Frame>

## Extract Email Domains

Get all email domains extracted from the provided input.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Text or JSON | The input text or JSON object to extract email domains from. |
  | Remove Duplicates | When checked, repeated values in the final result are removed. |
</div>

## Extract URL parts

Extract URL parts (scheme, netloc, path, params, query, fragment, hostname, port).

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | URL | The URL to extract parts from. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/ZUtie3exEe7_7B_M/img/Actions/ExtractURLParts.png?fit=max&auto=format&n=ZUtie3exEe7_7B_M&q=85&s=b5b06a2b91ca7c3c43474dadf7df646f" width="1207" height="413" data-path="img/Actions/ExtractURLParts.png" />
</Frame>

#### Results without removing duplicates

<Frame>
  <img src="https://mintcdn.com/blinkops-2/ZUtie3exEe7_7B_M/img/Actions/ExtractEmailDomainsWithDups.png?fit=max&auto=format&n=ZUtie3exEe7_7B_M&q=85&s=b84d750f9aae15ae626f2257a9bffd33" width="1213" height="404" data-path="img/Actions/ExtractEmailDomainsWithDups.png" />
</Frame>

#### Results after removing duplicates

<Frame>
  <img src="https://mintcdn.com/blinkops-2/ZUtie3exEe7_7B_M/img/Actions/ExtractEmailDomainsWithoutDups.png?fit=max&auto=format&n=ZUtie3exEe7_7B_M&q=85&s=b71381c4d9962a2631a8cb924f94d80b" width="1213" height="404" data-path="img/Actions/ExtractEmailDomainsWithoutDups.png" />
</Frame>

## Extract URLs

Get a list of URLs in the order they are found in the provided text or JSON object.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Text or JSON | The input text or JSON object to extract URLs from. |
  | Remove Duplicates | When checked, repeated values in the final result are removed. |
</div>

#### Results without removing duplicates

<Frame>
  <img src="https://mintcdn.com/blinkops-2/ZUtie3exEe7_7B_M/img/Actions/ExtractURLsWithDups.png?fit=max&auto=format&n=ZUtie3exEe7_7B_M&q=85&s=257f11d38c9669571552782c5db8eb2f" width="1213" height="404" data-path="img/Actions/ExtractURLsWithDups.png" />
</Frame>

#### Results after removing duplicates

<Frame>
  <img src="https://mintcdn.com/blinkops-2/ZUtie3exEe7_7B_M/img/Actions/ExtractURLsWithoutDups.png?fit=max&auto=format&n=ZUtie3exEe7_7B_M&q=85&s=e07a661d4d316b664f078267798af5d8" width="1213" height="404" data-path="img/Actions/ExtractURLsWithoutDups.png" />
</Frame>

## RegEx Match

Returns a list of RegEx matches in the order they are found when applied to a provided string. This action specifically utilizes Python's RegEx flavor.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | String | The string for which regex matches are to be returned. |
  | RegEx | The regular expression pattern used to search the string. Provide only the pattern you wish to match. If you are including group matching, please enclose the group within (?:) rather than ().<br />For example: For the string - `test1, test2, test3` and the RegEx - `test1`, the returned list looks like the following: \["test1"] For the string - `aabbaa` and the RegEx - `(?:aabb)`, the returned list looks like the following: \["aabb"] |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/I0bBfTOFYhQg2L0_/img/Utilities/data_extraction_utilities-regexmatch.png?fit=max&auto=format&n=I0bBfTOFYhQg2L0_&q=85&s=f7d486595e4b79b8720986cbaf23df80" width="1992" height="876" data-path="img/Utilities/data_extraction_utilities-regexmatch.png" />
</Frame>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.