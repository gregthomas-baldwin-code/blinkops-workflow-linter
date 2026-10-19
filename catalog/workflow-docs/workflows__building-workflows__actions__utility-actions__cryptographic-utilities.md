> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cryptographic Utilities

> Essential security and encoding operations for data protection and transformation.

## Decode Base64

Decodes the input text from base64 and prints the result to the output screen. The action supports either standard base64 or URL base64 encoding.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Text | The text to decode. |
  | Encoding Type | The type of encoding: `Standard` or `URL` |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/rI4Qa3pv_haSGbfd/img/Utilities/cryptographic_utilities-decodeBase64.png?fit=max&auto=format&n=rI4Qa3pv_haSGbfd&q=85&s=bcd98ae5bebdeafe0cb1a6eef30a8afb" width="1992" height="876" data-path="img/Utilities/cryptographic_utilities-decodeBase64.png" />
</Frame>

## Decode Hex

Converts a hex-encoded string to a string.

For example:
For the hexadecimal encoded string: `626C696E6B`, the returned string will be: `blink`.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Encoded String | The string that needs to be decoded. Bytes are decoded using UTF-8. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/rI4Qa3pv_haSGbfd/img/Utilities/cryptographic_utilities-decodeHEX.png?fit=max&auto=format&n=rI4Qa3pv_haSGbfd&q=85&s=d1a76d1d972452a1f87cc6d882ab2688" width="1992" height="878" data-path="img/Utilities/cryptographic_utilities-decodeHEX.png" />
</Frame>

## Decode JWT

Decode a JSON Web Token (JWT).

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | JWT | The complete JSON Web Token (JWT) string to be decoded. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/rI4Qa3pv_haSGbfd/img/Utilities/cryptographic_utilities-decoteJWT.png?fit=max&auto=format&n=rI4Qa3pv_haSGbfd&q=85&s=5493609980463eb3a32ef29b13366a3c" width="1986" height="876" data-path="img/Utilities/cryptographic_utilities-decoteJWT.png" />
</Frame>

## Encode Base64

Encodes the input text to base64 and prints the result to the output screen. The action supports either standard base64 or URL base64 encoding.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Text | The text to encode. |
  | Encoding Type | The type of encoding to decode: `Standard` or `URL` |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/rI4Qa3pv_haSGbfd/img/Utilities/cryptographic_utilities-encodeBase64.png?fit=max&auto=format&n=rI4Qa3pv_haSGbfd&q=85&s=c0a4c2aa8a912f9a8e23417d04422fe8" width="1992" height="874" data-path="img/Utilities/cryptographic_utilities-encodeBase64.png" />
</Frame>

## Encode Hex

Converts a regular string to its hex representation, encoding each character of the string into hexadecimal format.

For example:
For input string: `blink`, the returned hexadecimal string will be: `626c696e6b`.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | String | The string that will be encoded. First, it encodes the string to bytes (using UTF-8) and then the bytes to hex. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/I0bBfTOFYhQg2L0_/img/Utilities/cryptographic_utilities-encodeHEX.png?fit=max&auto=format&n=I0bBfTOFYhQg2L0_&q=85&s=30976d90ab3cc600d777d201980bc386" width="1984" height="872" data-path="img/Utilities/cryptographic_utilities-encodeHEX.png" />
</Frame>

## Encode JWT

Encode JSON Web Token (JWT).

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Sub | The subject identifier for whom this token is being created. |
  | Name | The human-readable name associated with the subject. |
  | Issued At Time (IAT) | The timestamp when this token was issued. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/I0bBfTOFYhQg2L0_/img/Utilities/cryptographic_utilities-encodeJWT.png?fit=max&auto=format&n=I0bBfTOFYhQg2L0_&q=85&s=4ef599f939d2dc4e2cdd514c17a4500e" width="1988" height="878" data-path="img/Utilities/cryptographic_utilities-encodeJWT.png" />
</Frame>

## Generate MD5 Hash

Generates a MD5 hash from a string or from a file.

For example:
For input string: `blink`, the returned generated MD5 hash will be: `40652ee9ae143f1c1c830f01a5449ecb`.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Source Type | Select whether to generate the hash from the `String` or from a `File`. |
  | String | The string from which to generate the MD5 hash. |
  | File Path | The file from which to generate the MD5 hash. |
  | Working Directory | The directory where the file is located. The filesystem state is preserved across steps using this directory to ensure that files and changes persist for continuity. <br /><br /> For more information - refer to the [Create Working Directory](https://docs.blinkops.com/docs/workflows/building-workflows/actions/utility-actions/file_system-utilities#create-working-directory) action documentation for guidance on setting up and selecting working directories. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/I0bBfTOFYhQg2L0_/img/Utilities/cryptographic_utilities-generateMD5.png?fit=max&auto=format&n=I0bBfTOFYhQg2L0_&q=85&s=fe9ba4d70d0ec606f131a4d6bd464a5c" width="1988" height="874" data-path="img/Utilities/cryptographic_utilities-generateMD5.png" />
</Frame>

## Generate Password

Generates a secret password and stores it in a variable.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Variable Name | The name of the variable to store the generated password in. |
  | Password Length | The password length, default 10. |
  | Include Special Chars | `[!-*]` character set - `!@#$%&*`. |
  | Include Lowercase Chars | `[a-z]` character set - `abcdedfghijklmnopqrst`. |
  | Include Uppercase Chars | `[A-Z]` character set - `ABCDEFGHIJKLMNOPQRSTUVWXYZ`. |
  | Include Digit Chars | `[0-9]` character set - `0123456789`. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/I0bBfTOFYhQg2L0_/img/Utilities/cryptographic_utilities-generate-password.png?fit=max&auto=format&n=I0bBfTOFYhQg2L0_&q=85&s=842fc6246b52588932e6bd214e644534" width="1992" height="872" data-path="img/Utilities/cryptographic_utilities-generate-password.png" />
</Frame>

## Generate SHA1 Hash

Generates a SHA1 hash from a string or from a file.

For example:
For input string: `blink`, the returned generated SHA1 hash will be: `dcae3a7a7c14a77ef384f1c5df6e63edc780eba0`.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Source Type | Select whether to generate the hash from the `String` or from a `File`. |
  | String | The string from which to generate the SHA1 hash. |
  | File Path | The path of the file from which to generate the SHA1 hash. |
  | Working Directory | The directory where the file is located. The filesystem state is preserved across steps using this directory to ensure that files and changes persist for continuity. <br /><br /> For more information - refer to the [Create Working Directory](https://docs.blinkops.com/docs/workflows/building-workflows/actions/utility-actions/file_system-utilities#create-working-directory) action documentation for guidance on setting up and selecting working directories. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/I0bBfTOFYhQg2L0_/img/Utilities/cryptographic_utilities-generateSHA1.png?fit=max&auto=format&n=I0bBfTOFYhQg2L0_&q=85&s=316b2b6703982148464aabfdcda8854e" width="1990" height="876" data-path="img/Utilities/cryptographic_utilities-generateSHA1.png" />
</Frame>

## Generate SHA256 Hash

Generates a SHA256 hash from a string or from a file.

For example:
For input string: `blink`, the returned generated SHA256 hash will be: `e14a51fded1fb9b43de815d3832da099053b583f1d2c01d0495a70f118df426c`.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Source Type | Select whether to generate the hash from the `String` or from a `File`. |
  | String | The string from which to generate the SHA256 hash. |
  | File Path | The path of the file from which to generate the SHA256 hash. |
  | Working Directory | The directory where the file is located. The filesystem state is preserved across steps using this directory to ensure that files and changes persist for continuity. <br /><br /> For more information - refer to the [Create Working Directory](https://docs.blinkops.com/docs/workflows/building-workflows/actions/utility-actions/file_system-utilities#create-working-directory) action documentation for guidance on setting up and selecting working directories. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/I0bBfTOFYhQg2L0_/img/Utilities/cryptographic_utilities-generateSHA256.png?fit=max&auto=format&n=I0bBfTOFYhQg2L0_&q=85&s=01b1a38b47bf7be8dcda0ecddd1f4d99" width="1988" height="878" data-path="img/Utilities/cryptographic_utilities-generateSHA256.png" />
</Frame>

## Generate UUID V4

Generates a random version 4 UUID.

**Note**: A Version 4 UUID is a universally unique identifier that is generated using random numbers. There is no warranty that the provided UUID is unique.

<Frame>
  <img src="https://mintcdn.com/blinkops-2/I0bBfTOFYhQg2L0_/img/Utilities/cryptographic_utilities-generateUUID4.png?fit=max&auto=format&n=I0bBfTOFYhQg2L0_&q=85&s=dc49f3c64dbe0fbeb9c12a89b61f0da5" width="1990" height="876" data-path="img/Utilities/cryptographic_utilities-generateUUID4.png" />
</Frame>

## Get TLS Certificate Information

Retrieves information about the security certificate (TLS/SSL) used by an endpoint for encrypted communication.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Hostname | The hostname of the endpoint. |
  | Port | The port number of the endpoint. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/I0bBfTOFYhQg2L0_/img/Utilities/cryptographic_utilities-getTLS.png?fit=max&auto=format&n=I0bBfTOFYhQg2L0_&q=85&s=5d9c5e40f2e945f91efc2e56b6494253" width="1990" height="876" data-path="img/Utilities/cryptographic_utilities-getTLS.png" />
</Frame>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.