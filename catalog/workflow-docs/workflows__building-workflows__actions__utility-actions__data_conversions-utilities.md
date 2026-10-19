> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Data Conversions Utilities

> Essential format transformation capabilities for various data types and document formats.

## Convert CSV To HTML Table

Convert a CSV input to a HTML table.

**Notes:**

* All rows must have the same number of columns as the header (RFC 4180 compliant).
* The first row of the CSV will become the header and every row after it will be a new entry in the final HTML table.
* Any value containing a comma (`,`) must be enclosed in double quotes (`"..."`). The opening quote must appear immediately after the comma separator (no space).
* To include a literal double quote in a value, escape it by using two double quotes (`""`). This is especially important for JSON strings within a CSV cell.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | CSV Object | The CSV input to convert.<br /><br /> Example: `Header1,Header2,Header3 "Value, with comma",Normal Value,"{""key1"": ""value1"",""key2"": ""value2""}" Row2, ,Row2` |
  | Add Index Column | Select to add an index column with row numbers. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/o6QbEE5epEQlSrs6/img/Utilities/data_conversions_utilities-csvtohtmltable.png?fit=max&auto=format&n=o6QbEE5epEQlSrs6&q=85&s=5f245dfd62ad4119bd074cb288aa1b7d" width="3390" height="1118" data-path="img/Utilities/data_conversions_utilities-csvtohtmltable.png" />
</Frame>

## Convert CSV To JSON

Convert a CSV object to a JSON object.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | CSV Object | CSV object to convert to the JSON format. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/I0bBfTOFYhQg2L0_/img/Utilities/data_conversions_utilities-csvtojson.png?fit=max&auto=format&n=I0bBfTOFYhQg2L0_&q=85&s=e1254f9d958239bbcd4b0b43fd467775" width="1990" height="874" data-path="img/Utilities/data_conversions_utilities-csvtojson.png" />
</Frame>

## Convert EML To JSON

Convert EML data to JSON structure.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | EML Content | The EML string which will be converted to JSON. |
  | Include Properties | Select which advanced email properties to include in the JSON result.<br /><br />Advanced email data options:<br />• `cc` - Carbon copy recipients who receive a visible copy of the email.<br />• `bcc` - Blind carbon copy recipients who receive a hidden copy of the email.<br />• `reply_to` - The email address that replies should be sent to, which may differ from the sender.<br />• `message_id` - Unique identifier assigned to each email message.<br />• `in_reply_to` - Message ID of the email this message is responding to.<br />• `references` - Chain of Message IDs showing the conversation history.<br />• `attachments` - Files included with the email message.<br />• `headers` - Collection of all metadata fields in the email.<br />• `content_type` - Format of the email content (e.g., text/plain, text/html).<br />• `content_transfer_encoding` - Method used to encode the message content for transmission.<br />• `mime_version` - Version of MIME protocol used to structure the email.<br />• `return_path` - Email address for handling bounce-back messages.<br />• `delivered_to` - Final recipient's email address after any forwarding.<br />• `received` - Tracking information added by each server that processed the email.<br />• `authentication_results` - Results of email authentication checks.<br />• `dkim_signature` - Digital signature to verify the email's authenticity.<br />• `spf` - Sender Policy Framework record to prevent email spoofing. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/I0bBfTOFYhQg2L0_/img/Utilities/data_conversions_utilities-emltojson.png?fit=max&auto=format&n=I0bBfTOFYhQg2L0_&q=85&s=741585d9215399aab5b8cd2d6f25bf56" width="1986" height="872" data-path="img/Utilities/data_conversions_utilities-emltojson.png" />
</Frame>

## Convert HTML To Markdown

Convert HTML string to Markdown format.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | HTML Content | The HTML string which will be converted to Markdown.<br /><br />For example, for the HTML string:<br />`<b>Automate Everything</b> With <a href="https://www.blinkops.com/">Blink Ops</a>`<br /><br />The Markdown output will be:<br />`**Automate Everything** With [Blink Ops](https://www.blinkops.com/)` |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/I0bBfTOFYhQg2L0_/img/Utilities/data_conversions_utilities-htmltomarkdown.png?fit=max&auto=format&n=I0bBfTOFYhQg2L0_&q=85&s=bd113c60e01a9fa563f9ec7639b3aa77" width="1986" height="876" data-path="img/Utilities/data_conversions_utilities-htmltomarkdown.png" />
</Frame>

## Convert Markdown To HTML

Convert Markdown string to HTML format.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Markdown Content | The Markdown string which will be converted to HTML.<br /><br />For example, for the Markdown string:<br />`[Blink Ops](https://www.blinkops.com/)`<br /><br />The HTML output will be:<br />`<p><a href="https://www.blinkops.com/">Blink Ops</a></p>` |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/I0bBfTOFYhQg2L0_/img/Utilities/data_conversions_utilities-markdowntohtml.png?fit=max&auto=format&n=I0bBfTOFYhQg2L0_&q=85&s=a06c66084d8c8193845ef0a03b4b9293" width="1988" height="874" data-path="img/Utilities/data_conversions_utilities-markdowntohtml.png" />
</Frame>

## Convert HTML To PDF

Convert HTML to a `.pdf` file.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | File Identifier | The identifier of the file. This will be used as an input for subsequent steps. |
  | HTML Content | The HTML code to render. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/I0bBfTOFYhQg2L0_/img/Utilities/data_conversions_utilities-htmltopdf.png?fit=max&auto=format&n=I0bBfTOFYhQg2L0_&q=85&s=0aa1e0974e604e21613d5450d6ac10eb" alt="Convert HTML To PDF" width="1990" height="874" data-path="img/Utilities/data_conversions_utilities-htmltopdf.png" />
</Frame>

## Convert HTML To PNG

Convert HTML to a `.png` file.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | File Identifier | The identifier of the file. This will be used as input for subsequent steps. |
  | HTML Content | The HTML code to render. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/I0bBfTOFYhQg2L0_/img/Utilities/data_conversions_utilities-htmltopng.png?fit=max&auto=format&n=I0bBfTOFYhQg2L0_&q=85&s=c7c370a82bed168cca8f9fcb1edd9315" alt="Convert HTML To PNG" width="1990" height="878" data-path="img/Utilities/data_conversions_utilities-htmltopng.png" />
</Frame>

## Convert JSON To CSV

Convert a JSON object to a CSV object.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | JSON Object | JSON object to convert to the CSV format. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/I0bBfTOFYhQg2L0_/img/Utilities/data_conversions_utilities-jsontocsv.png?fit=max&auto=format&n=I0bBfTOFYhQg2L0_&q=85&s=ce4d19e91475bfcd4407ef5b23da9683" width="2020" height="890" data-path="img/Utilities/data_conversions_utilities-jsontocsv.png" />
</Frame>

## Convert JSON To YAML

Convert JSON string to YAML.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | JSON Content | The JSON string which will be converted to YAML. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/I0bBfTOFYhQg2L0_/img/Utilities/data_conversions_utilities-jsontoyaml.png?fit=max&auto=format&n=I0bBfTOFYhQg2L0_&q=85&s=5ea19dc186a2a0f53f202375abdb4320" width="1988" height="874" data-path="img/Utilities/data_conversions_utilities-jsontoyaml.png" />
</Frame>

## Convert YAML To JSON

Convert YAML string to JSON.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | YAML Content | The YAML string which will be converted to JSON. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/I0bBfTOFYhQg2L0_/img/Utilities/data_conversions_utilities-yamltojson.png?fit=max&auto=format&n=I0bBfTOFYhQg2L0_&q=85&s=341ec98e6d6faecb747b4aa784475bf3" width="1988" height="880" data-path="img/Utilities/data_conversions_utilities-yamltojson.png" />
</Frame>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.