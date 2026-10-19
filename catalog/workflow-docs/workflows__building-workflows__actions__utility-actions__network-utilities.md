> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Network Utilities

> Utility actions for network analysis, DNS lookups, and security checks in Blink workflows.

## Check IP in CIDR

Checks if an IP address belongs to a specific network (CIDR block). Returns `True` or `False`.

For example: The given IP `192.168.1.10`, and the CIDR `192.168.1.0/24` will result in the output `True`.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | IP Address | The IP that needs to be checked as a plain string. |
  | CIDR | The network, represented as a CIDR. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/I0bBfTOFYhQg2L0_/img/Utilities/network_utilities-checkipincidr.png?fit=max&auto=format&n=I0bBfTOFYhQg2L0_&q=85&s=3425fe5d4127bb716c53a0f172a77edf" width="1986" height="874" data-path="img/Utilities/network_utilities-checkipincidr.png" />
</Frame>

## Defang Entity

Alters potentially malicious content within a string entity (like a URL, email address, or domain) to make it appear harmless.

For example:
For the string: `https://www.malwarebytes.com/malware`, and the method `Replace`, the returned string will be: `hXXps://www[.]malwarebytes[.]com/malware `.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | String | The string entity that needs to be defanged. |
  | Method | The "defanging" method. The supported methods are: <ul><li>Replace - This method replaces sensitive parts (protocol prefixes in URLs, `@` in emails, and `.` in domains) with placeholders like `hXXp://` and `[at]`.</li><li>Brackets - This method adds square brackets around the suspicious elements to visually indicate potential risk without altering the core content.</li></ul> |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/I0bBfTOFYhQg2L0_/img/Utilities/network_utilities-defangent.png?fit=max&auto=format&n=I0bBfTOFYhQg2L0_&q=85&s=488fb2a934f02d69467476d3990a8cda" width="1988" height="878" data-path="img/Utilities/network_utilities-defangent.png" />
</Frame>

## Decode URL

Converts a given URL encoded string into a string.

For example:
For the encoded string:`https%3A//blinkops.com/utility%3Fname%3Ddecode_url`, the returned string will be: `https://blinkops.com/utility?name=decode_url`.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Encoded URL | The encoded URL that needs to be converted into a string. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/I0bBfTOFYhQg2L0_/img/Utilities/network_utilities-decodeurl.png?fit=max&auto=format&n=I0bBfTOFYhQg2L0_&q=85&s=b7c3bd6d526729f223cdbdeff301a540" width="1986" height="876" data-path="img/Utilities/network_utilities-decodeurl.png" />
</Frame>

## Encode URL

Converts a given url string into url encoded format.

For example:
For the string: `https://blinkops.com/utility?name=encode_url`, the returned encoded URL will be: `https%3A//blinkops.com/utility%3Fname%3Dencode_url`.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | URL | The URL that needs to be converted into URL-encoded format. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/I0bBfTOFYhQg2L0_/img/Utilities/network_utilities-encodeurl.png?fit=max&auto=format&n=I0bBfTOFYhQg2L0_&q=85&s=b94764ee8566ba6376327bafae483408" width="1988" height="876" data-path="img/Utilities/network_utilities-encodeurl.png" />
</Frame>

## Refang Entity

Reverts a defanged entity back to its original form.

For example:
For the string: `hXXps://www[.]malwarebytes[.]com/malware`, and the method `Replace`, the returned string will be: `https://www.malwarebytes.com/malware`.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Defanged String | The string entity that needs to be reverted to its previous form. |
  | Method | The "defanging" method used originally. The supported methods are: <ul><li>Replace - This method replaces sensitive parts (protocol prefixes in URLs, `@` in emails, and `.` in domains) with placeholders like `hXXp://` and `[at]`.</li><li>Brackets - This method adds square brackets around the suspicious elements to visually indicate potential risk without altering the core content.</li></ul> |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/I0bBfTOFYhQg2L0_/img/Utilities/network_utilities-refangent.png?fit=max&auto=format&n=I0bBfTOFYhQg2L0_&q=85&s=5bd0f7f5241cb6fdd16d5baae89eb4d8" width="1988" height="876" data-path="img/Utilities/network_utilities-refangent.png" />
</Frame>

## WhoIs Query

The **WhoIs Query** utility action allows you to run a whois query on domains and IP addresses.

<Tip>
  Some WhoIs commands might take some time as the command searches across all servers to find the requested data.

  In-case of a timeout we suggest to increase the `Timeout` in the action settings.
</Tip>

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | WhoIs Query | The WhoIs query to run. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/I0bBfTOFYhQg2L0_/img/Utilities/network_utilities-whois.png?fit=max&auto=format&n=I0bBfTOFYhQg2L0_&q=85&s=e9627ee17a509b632daa0b0bdaae9847" width="1990" height="876" data-path="img/Utilities/network_utilities-whois.png" />
</Frame>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.