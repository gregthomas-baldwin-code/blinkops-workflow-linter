> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# JSON Utilities

> Utility actions for parsing, transforming, and manipulating JSON data in Blink workflows.

## Compare JSON Structure

Compare two JSON objects to verify that they have an identical structure (matching keys and data types at all levels), regardless of their actual values.

**Note**: Array types will be validated using their first element only.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | First JSON | The first JSON object to compare against the second. |
  | Second JSON | The second JSON object to compare against the first. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/tzZ-4dIfb8gKd907/img/Utilities/json_utilities-compare_structure.png?fit=max&auto=format&n=tzZ-4dIfb8gKd907&q=85&s=f56587cacffc9f258eed4c07e6e314a7" width="2418" height="802" data-path="img/Utilities/json_utilities-compare_structure.png" />
</Frame>

## Merge JSON Objects

Merge two JSON objects.

If there are matching keys, the key from the `Merged JSON` will overwrite the values from the `Source JSON`.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Source JSON Object | The source JSON object to merge. |
  | Merged JSON Object | The JSON object containing the new data to be merged into the source. |
  | Recursive Merge | When selected, the merge will be executed in a recursive method and nested maps will be merged instead of overwritten. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/5S6z5MxgBLy6FDIP/img/Utilities/json_utilities_merge_json_objects.png?fit=max&auto=format&n=5S6z5MxgBLy6FDIP&q=85&s=f044a5c1f79294a1ef37ba01d75844ca" width="2270" height="796" data-path="img/Utilities/json_utilities_merge_json_objects.png" />
</Frame>

## Run JQ Command

Execute JQ queries to filter, transform, and extract data from JSON structures.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | JSON | The JSON data to query. Can be a JSON object, array, or string containing valid JSON. |
  | Query | The JQ query expression to execute.<br /><br />For Example, use `.field.array[0].subfield` to access nested fields. |
  | Working Directory | When a working directory is selected, the filesystem state is preserved across steps that use this directory. Files and changes in the chosen directory persist across steps, ensuring continuity.<br /><br />For more information, refer to the [Create Working Directory](https://docs.blinkops.com/docs/workflows/building-workflows/actions/utility-actions/file_system-utilities#create-working-directory) action documentation for guidance on setting up and selecting working directories. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/I0bBfTOFYhQg2L0_/img/Utilities/json_utilities-jq.png?fit=max&auto=format&n=I0bBfTOFYhQg2L0_&q=85&s=2b30bcfc78b6a672f91ba663024b7acf" width="1846" height="818" data-path="img/Utilities/json_utilities-jq.png" />
</Frame>

## Run JP Command

Execute JSONPath queries to search and extract data from JSON structures using path expressions.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | JSON | The JSON data to query. Can be a JSON object, array, or string containing valid JSON. |
  | Query | The JSONPath query expression to execute.<br /><br />For Example, use `field.array[0].subfield` to access nested fields. |
  | Unquoted | Remove surrounding quotes from string results. When enabled, string values are returned as plain text without quotation marks. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/I0bBfTOFYhQg2L0_/img/Utilities/json_utilities-jp.png?fit=max&auto=format&n=I0bBfTOFYhQg2L0_&q=85&s=6949f0dfa56641b5c9f0a22df1fbbc16" width="1850" height="816" data-path="img/Utilities/json_utilities-jp.png" />
</Frame>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.