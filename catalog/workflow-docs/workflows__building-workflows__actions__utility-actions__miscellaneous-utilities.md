> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Miscellaneous Utilities

> Utility actions for screenshots, file conversions, and other miscellaneous operations in Blink workflows.

## Capture Website Screenshot

Get a webpage screenshot as a `.png` file using a provided URL.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | File Identifier | The identifier of the file. This will be used as an input for subsequent steps. |
  | URL | The URL to take the screenshot from (e.g. `https://google.com`). |
  | Wait For Selector | Optional CSS selector to wait for before taking the screenshot (e.g., `.main-content` or `#login`). |
  | Delay After Load (Seconds) | Optional number of seconds to wait after the page or selector is ready, before capturing the screenshot.<br />Maximum: `60` seconds.<br />Must be less than the step timeout. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/I0bBfTOFYhQg2L0_/img/Utilities/misc_utilities-capturewebsite.png?fit=max&auto=format&n=I0bBfTOFYhQg2L0_&q=85&s=6c97d03e9634df488693fe3f3169e561" alt="Screenshot WebPAge" width="2002" height="882" data-path="img/Utilities/misc_utilities-capturewebsite.png" />
</Frame>

## Generate Random Number

Generates a random integer within a specific inclusive range.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Minimum | The minimum value of the range (inclusive). |
  | Maximum | The maximum value of the range (inclusive). |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/I0bBfTOFYhQg2L0_/img/Utilities/misc_utilities-generaterandomnum.png?fit=max&auto=format&n=I0bBfTOFYhQg2L0_&q=85&s=52e05e598276185a2d681a83f224844a" width="1998" height="884" data-path="img/Utilities/misc_utilities-generaterandomnum.png" />
</Frame>

## Increment Variable

The **Increment Variable** utility action enables you to **increment** your **variable** by a value of one. You can choose the **variable** you would like to **increment** by selecting it from the dynamic dropdown menu.

<Frame>
  <img src="https://mintcdn.com/blinkops-2/LiDiL34PEmIGHJGK/img/Actions/increment.png?fit=max&auto=format&n=LiDiL34PEmIGHJGK&q=85&s=d6f2a4f3e02daae8c483e422205c66f4" width="2404" height="1673" data-path="img/Actions/increment.png" />
</Frame>

## Print

Print text to the step output screen.
<Note>To print the content of a file, use the `Get File Content` action instead.</Note>

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Text | The text or variable to print to the output screen. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/I0bBfTOFYhQg2L0_/img/Utilities/misc_utilities-print.png?fit=max&auto=format&n=I0bBfTOFYhQg2L0_&q=85&s=85230c23874e8e5ab263a3e1a4507747" width="2002" height="886" data-path="img/Utilities/misc_utilities-print.png" />
</Frame>

## Validate Structure

Validate if the input conforms to a specified data structure format.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Input | The input data to validate against the specified structure format. |
  | Structure Type | The expected structure format to validate the input against. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/YMkcIpIyeCNfqsxP/img/Utilities/misc_utilities-validatestructure.png?fit=max&auto=format&n=YMkcIpIyeCNfqsxP&q=85&s=8bae8f5894700a0dfc47c87b38c7da69" width="2414" height="806" data-path="img/Utilities/misc_utilities-validatestructure.png" />
</Frame>

### Validation Behavior

The action performs strict format validation based on the selected structure type:

**JSON Validation:**

* Checks for valid JSON syntax, including proper bracket/brace matching.
* Verifies correct key-value pair formatting.

**XML Validation:**

* Verifies well-formed XML structure with proper tag opening/closing.
* Checks for valid element nesting.

**YAML Validation:**

* Validates YAML syntax, including proper indentation.
* Checks for correct key-value pair formatting.

**CSV Validation:**

* Checks for valid CSV structure and formatting.

**EML Validation:**

* Validates email message format structure.
* Requires presence of essential headers (`From` and `Date`).


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.