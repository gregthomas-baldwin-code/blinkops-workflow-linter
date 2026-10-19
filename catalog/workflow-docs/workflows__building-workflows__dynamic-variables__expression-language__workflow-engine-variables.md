> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Dynamic Variable Syntax

> Use expression language syntax with double curly brackets to manually reference dynamic variables in Blink workflows.

<Note>
  Whether an expression is entered manually or chosen using the variable picker, it will be saved in the Workflow `YAML` using the syntax shown below.
</Note>

[Dynamic Variables](/docs/workflows/building-workflows/dynamic-variables/variable-picker) follow a structured syntax enclosed within double curly braces
`{{ }}`.
The syntax specifies the variable type and its reference path within the workflow. Understanding this format allows you to insert variables manually when necessary or desired.

<Tip>
  **Tip**

  When working with dynamic variables, sometimes the value can be `null`, which can cause issues when displaying values in the variable picker or workflow inputs.

  Here is a useful tip to replace `null` with a default value:

  1. If a variable might be null, you can use a ternary-style expression to replace it with a fallback value:
     * `{{event.payload.case.vendors != null ? event.payload.case.vendors : "N/a"}}`

  2. Another approach is to force the variable into a string format, which can ensure it does not remain null:
     * `str({{steps.s2.output}})`
</Tip>

### General Syntax Structure

```
{{ category.identifier }}
```

* `category` defines the [dynamic variables](/docs/workflows/building-workflows/dynamic-variables/variable-picker) type (e.g., inputs, steps, event, metadata).

* `identifier` specifies the exact reference within the category.

* For example, referencing an input parameter named 'slack\_channel':

```
{{ inputs.slack_channel }}
```

<Frame>
  <video controls autoPlay muted zoom loop allowFullScreen className="w-full aspect-video" src="https://www.dropbox.com/scl/fi/z0y9b0d23krlygfu7tv0l/DynamicVarSyntax.mp4?rlkey=efeboma662sogon5bwho6x848&st=mul7z662&raw=1" />
</Frame>

## Adding Dynamic Variables Manually in a Workflow

### Workflow Input Parameters

To reference data entered in workflow inputs, use the following syntax:

```
{{ inputs.param_name }}
```

<Note>
  `param_name` represents the name you assigned to the input parameter.
</Note>

### Event payload

To reference data returned from an event payload that triggered an [Event-Based](/docs/workflows/building-workflows/triggers/event-based-triggers/event-based-triggers) Workflow, use the following syntax:

```yaml theme={"dark"}
{{ event.payload }}             # full event payload
{{ event.payload.issue.user }}  # fetch the value of user attribute in event payload that can look like this: { "issue": {"user": "me" }}
```

### Step Output Variables

To reference data returned from a step’s output, use the following syntax:

```yaml theme={"dark"}
{{ steps.S1.output }} #  S1 refers to the step’s ID
```

<Note>
  The `S` in `steps.S1.output` represents a step in the workflow, and the number
  following it (`1` in this case) indicates the specific step being referenced.
  Each step in a workflow is assigned a unique identifier (`S1`, `S2`, etc.),
  allowing you to retrieve outputs from a particular step.
</Note>

💡 You can also use `last` instead of a `step ID` to reference the most recent step output:

```
{{ steps.last.output }}
```

### Step Status

To check the execution status of a previous step, use the following syntax:

```
{{ steps.S1.status }}
```

### Workflow Variables

To use Workflow's variables created by the [Set Variable Action](/docs/workflows/building-workflows/actions/basic-actions/flow-control-actions#set-variables), use the following syntax:

```
{{ variables.variable_name }}
```

### Metadata Variables

To access metadata (workflow-related information), use the following syntax

```yaml theme={"dark"}
{{ metadata.automation_name }}  # Workflow name
{{ metadata.automation_url }}   # Workflow link
{{ metadata.automation_id }}    # Workflow ID
{{ metadata.workspace_id }}      # Workspace ID
{{ metadata.pack_id }}          # Pack ID
{{ metadata.execution_id }}     # Execution ID
{{ metadata.execution_url }}    # Execution link
{{ metadata.start_time }}       # Execution start time
{{ metadata.user_email }}       # User who started execution
{{ metadata.user_groups }}      # User's assigned groups
```

### Python Actions

The syntax for referencing data returned from Python actions is different. In steps that include [Python actions](/docs/workflows/building-workflows/actions/basic-actions/code-actions#run-python), you need to use the `context` variable to access dynamic variables. This means that all the expressions mentioned above can be accessed in Python using the following syntax:

```yaml theme={"dark"}
context.inputs.param_name  # Input parameter
context.steps.S1.output  # Step output
context.steps.S1.output.user.id  # Specific key in step output
context.steps.last.output  # Last executed step output
context.steps.S1.status  # Step status
context.event.payload  # Full event payload
context.event.payload.issue.user  # Specific key in event payload
context.metadata.automation_name  # Metadata variable
```

In [Python actions](/docs/workflows/building-workflows/actions/basic-actions/code-actions#run-python), variables can be assigned a value, by using the following syntax:

```yaml theme={"dark"}
context.variables.variable_name = value # Assign a value to a workflow variable
```

***

## Best Practices

* Use the [Variable Picker](/docs/workflows/building-workflows/dynamic-variables/variable-picker#using-the-variable-picker-to-add-dynamic-variables) to avoid syntax errors.
* When referencing JSON keys with dots (.), use square bracket notation if needed.
* Step outputs are only available after execution; ensure dependencies are correctly structured.

***

## Common Expression Language Use Case Examples

This section provides practical examples of how to use Expression Language within Blink's workflows to manipulate data, apply logic, and dynamically build output values. Each use case highlights a specific pattern, such as conditional branching, string formatting, safe referencing of variables, or working with nested data structures, that is commonly needed when building automated logic in workflows.

<Note>
  All print steps are intended to display the content of a variable along with its expression. The variable can then be used like any standard variable, except in dynamic connection assignments.\
  **Best practice:** Start by using a print step to validate the variable's behavior. Once it returns the expected output, you can confidently use it as a regular variable wherever needed.
</Note>

<AccordionGroup>
  <Accordion title="Extract the Domain or Username from an Email Address">
    This use case demonstrates how to use the [split() function](/docs/workflows/building-workflows/dynamic-variables/expression-language/workflow-engine-functions#string-manipulation-functions) to extract either the domain or username portion of an email address using dynamic expressions.

    ## Extract the Domain from an Email Address

    Returns the domain part of an email (everything after the `@`).

    ### Syntax:

    `{{split(steps.1.output.payload.headers[0].value, '@')[1]}}`

    **Breakdown**:

    `steps.1.output.payload.headers[0].value`:  References the email address value returned in step 1 (`S1`), specifically from the first object in the headers array.

    `split(..., '@')` : Splits the email string into two parts at the @ symbol.

    `[1]`: Returns the second element of the array, which corresponds to the domain.

    ### Example:

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/0JKaSiVOyIaH-NI8/img/ExpressionLanguage/ExtractDomain.png?fit=max&auto=format&n=0JKaSiVOyIaH-NI8&q=85&s=de6eaad560bff767cf5be5580c554e2b" width="1728" height="1079" data-path="img/ExpressionLanguage/ExtractDomain.png" />
    </Frame>

    ***

    ## Extract the Username from an Email Address

    Extracts the portion of the email address that appears before the `@` symbol.

    ### Syntax:

    `{{split(steps.1.output.payload.headers[0].value, '@')[0]}}`

    **Breakdown**:

    Identical to the previous expression, but `[0]` retrieves the first element from the split array, representing the username.

    ### Example:

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/0JKaSiVOyIaH-NI8/img/ExpressionLanguage/ExtractBefore.png?fit=max&auto=format&n=0JKaSiVOyIaH-NI8&q=85&s=3205412fce52bcf45305a1f5ad3bb837" width="1728" height="1076" data-path="img/ExpressionLanguage/ExtractBefore.png" />
    </Frame>
  </Accordion>

  <Accordion title="Extract the Domain from a URL">
    ## Extract the Domain from a URL

    This use case demonstrates how to extract the domain portion from a full URL string by using nested split() functions.

    <Note>Note: This expression assumes that the URL begins with https\:// and that the domain follows immediately. Adjust the expression as needed for different URL formats.</Note>

    ### Syntax:

    `{{split(split(steps.3.output.files[0].webViewLink, 'https://')[1], '.')[0]}}`

    **Breakdown**:

    `steps.3.output.files[0].webViewLink`: Retrieves a URL (e.g., [https://drive.google.com/](https://drive.google.com/)...) from the first file object in step S3.

    `split(..., 'https://')[1]`: Removes the https\:// prefix and keeps the remaining part of the URL.

    * **Result**: drive.google.com/...

    `split(..., '.')[0]`: Splits the remaining string at the first period and returns the first element — the subdomain or main domain prefix.

    * Result: drive

    ### Example:

    In the following use case, we isolate the domain prefix from a URL, specifically extracting **drive** from a full URL such as `https://drive.google.com/...`. This is done by targeting the subdomain or first segment of the domain name following the `https://` prefix.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/0JKaSiVOyIaH-NI8/img/ExpressionLanguage/ExtractURLDomain.png?fit=max&auto=format&n=0JKaSiVOyIaH-NI8&q=85&s=818aebbaf3e209dd05d881102b3c6aa3" width="1725" height="1081" data-path="img/ExpressionLanguage/ExtractURLDomain.png" />
    </Frame>
  </Accordion>

  <Accordion title="Create a New URL Using Part of Another URL">
    ## Create a New URL Using Part of Another URL

    This use case demonstrates how to dynamically reconstruct a URL by removing a specific path segment and joining the remaining parts. In this example, the segment being removed is /api/v3, but this can be any string or path segment relevant to your use case.

    ### Syntax

    `{{split(steps.1.output.data.links.item, '/api/v3')[0] + split(steps.1.output.data.links.item, '/api/v3')[1]}}`

    **Breakdown**:

    `steps.1.output.data.links.item`: Retrieves the original URL from the output of step S1.

    `split(..., '/api/v3')`: Splits the URL at the /api/v3 segment.

    `[0]`: Returns the portion of the URL before /api/v3.

    `+`: Concatenates both parts together, effectively removing /api/v3.

    `[1]`: Returns the portion of the URL after /api/v3.

    ### Example:

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/0JKaSiVOyIaH-NI8/img/ExpressionLanguage/CreateNewURL.png?fit=max&auto=format&n=0JKaSiVOyIaH-NI8&q=85&s=0427258e0522c4cb9ebec84d8b19a37a" width="1722" height="1078" data-path="img/ExpressionLanguage/CreateNewURL.png" />
    </Frame>
  </Accordion>

  <Accordion title="Fallback if a Field is Null">
    ## Fallback if a Field is Null

    Checks if the username exists, if not, shows a fallback message.

    <Tip> It's better to even add an empty string than null.</Tip>

    ### Syntax:

    `{{steps.1.output.username!= null ? steps.1.output.username: 'User Not found'}}`

    ### Example:

    In the following example, the workflow attempts to retrieve user information from GitHub using the input `blinkopstester123`. Since the user does not exist, the API response does not return a `username` field—resulting in a `null` value. The expression checks for this and instead displays the fallback message `"User Not found"` to avoid showing a blank or `null` output.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/0JKaSiVOyIaH-NI8/img/ExpressionLanguage/NullValueField.png?fit=max&auto=format&n=0JKaSiVOyIaH-NI8&q=85&s=3309d1bbdae3f5039544f4ed4e759994" width="1728" height="1078" data-path="img/ExpressionLanguage/NullValueField.png" />
    </Frame>

    ***

    You can also wrap the expression in str() to ensure it doesn't remain null, which is useful when passing values into string-only fields:

    ### Syntax

    `str({{steps.s1.output}})`

    <Tip>It is often better to return an empty string or message than allow null to pass silently. This improves the clarity of logs and makes it easier to read</Tip>
  </Accordion>

  <Accordion title="Switch-Case Style Value Mapping">
    ## Switch-Case Style Value Mapping

    This use case demonstrates how to implement a switch-case-like logic within an expression to map specific input values to custom outputs. It is particularly useful for normalizing inconsistent values or applying conditional logic directly within a dynamic expression.

    <Note>returns a default string if not matched. </Note>

    ### Syntax:

    `{{event.payload.severity == "MEDIUM" ? "medium" : event.payload.severity == "Low"? "Low" : "Not Found"}}`

    #### Breakdown:

    `event.payload.severity`: Retrieves the severity value from the event payload.

    `== "MEDIUM"`: Checks if the value is "MEDIUM" and maps it to "medium" (lowercase).

    `== "Low"`: If the first condition fails, it checks for "Low" and maps it as-is.

    `"Not Found"`: If none of the conditions match, the expression returns a default fallback value of "Not Found".

    ### Example:

    Map known severity levels to preferred output formats (e.g., lowercase), and return a default value for any unmatched input.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/0JKaSiVOyIaH-NI8/img/ExpressionLanguage/MapSeverityLevel.png?fit=max&auto=format&n=0JKaSiVOyIaH-NI8&q=85&s=4bc83b96cb7fd4a9f057cab5b8bbb0d6" width="1727" height="1078" data-path="img/ExpressionLanguage/MapSeverityLevel.png" />
    </Frame>
  </Accordion>

  <Accordion title="Check if a Value is in a List">
    ## Check if a Value is in a List

    This use case demonstrates how to evaluate whether a specific value exists within a defined list. If the value is found, it returns a corresponding output; otherwise, it returns a fallback value.

    ### Syntax:

    `{{event.payload.severity in ["High", "Low"] ? steps.2.output.severity : "Not Found"}}`

    #### Breakdown:

    `event.payload.severity`: Retrieves the severity value from the incoming event payload.

    `in ["High", "Low"]`: Checks whether the severity is included in the specified list of allowed values.

    `? steps.2.output.severity`: If the value is in the list, return the severity output from step S2.

    `: "Not Found"`: If the value is not in the list, return "Not Found" as the default response.

    ### Example:

    Check whether the severity value from the event payload matches one of the allowed values ("High" or "Low"). If it matches, return the severity output from a previous step; if not, return a default string ( "Not Found").

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/0JKaSiVOyIaH-NI8/img/ExpressionLanguage/ChecksValueinList.png?fit=max&auto=format&n=0JKaSiVOyIaH-NI8&q=85&s=3dd40b5bce5a0a31919e52fae2cc9d49" width="1728" height="1081" data-path="img/ExpressionLanguage/ChecksValueinList.png" />
    </Frame>
  </Accordion>

  <Accordion title="Switch Based On Successful Action">
    ## Switch Based On Successful Action

    This use case demonstrates how to return a step’s output conditionally based on whether the step executed successfully. It allows you to avoid using additional variable-setting steps by referencing the success status directly.

    <Tip> This approach reduces workflow complexity by removing the need to create extra variables solely for the purpose of conditionally storing a value.</Tip>

    ### Syntax

    `{{steps.2.status == "OK" ? steps.2.output : steps.3.output}}`

    #### Breakdown:

    `steps.2.status`:

    * Checks the status of step 2 (`S2`).

    `== "OK"`: Evaluates whether step S2 executed successfully.

    `? steps.2.output`: If step S2 was successful, return its output.

    `: steps.3.output`: If step S2 was not successful, fall back to the output from step S3.

    <Note>This conditional approach is functionally similar to an `if-else` structure.</Note>

    ### Example:

    In workflows where you use branching logic (e.g., an If-Else condition), you often want to capture the output of the branch that actually executed. A common approach is to include a [Set Variable action](/docs/workflows/building-workflows/actions/basic-actions/flow-control-actions#set-variables) within each branch to define the result.

    However, you can simplify this by checking which branch step completed successfully and referencing its output directly—no additional variable step needed.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/0JKaSiVOyIaH-NI8/img/ExpressionLanguage/ConditionStatementsEL.png?fit=max&auto=format&n=0JKaSiVOyIaH-NI8&q=85&s=6a8343ab8e49dd241bbce824c5b29b6f" width="1728" height="1080" data-path="img/ExpressionLanguage/ConditionStatementsEL.png" />
    </Frame>
  </Accordion>

  <Accordion title="Use a Variable Within a Variable">
    ## Use a Variable Within a Variable

    This use case demonstrates how to reference a dynamic value inside another variable, which is particularly useful for mapping values or accessing specific data within a JSON object using a dynamic key.

    ### Syntax:

    1. `{{steps.2.output.keymap[ steps.1.output.selected_key]}}`

    #### Breakdown:

    The whole expression retrieves the value from keymap that corresponds to the key stored in `selected_key`.

    `steps.2.output.keymap`:  refers to the output of step 2, specifically the keymap JSON object.

    `[steps.1.output.selected_key]`: uses the value of selected\_key from step 1’s (`S1`) output as the dynamic key to access a value inside keymap.

    ### 2. Can also be chained:

    `{{steps.2.output.keymap[ steps.1.output.selected_key ][ steps.1.output.selected_key2 ]}}`

    #### Breakdown:

    This expression accesses a nested value within keymap by chaining two dynamic keys.

    * `steps.2.output.keymap`: A nested JSON object.

    * `[steps.1.output.selected_key]`: First-level dynamic key from step 1 output.

    * `[ steps.1.output.selected_key2]`: Second-level dynamic key from step 1 output.

    ### 3. Variable used inside another variable’s key:

    `{{steps.2.output.keymap[ steps.1.output.selected_key[ steps.1.output.selected_key2 ]]}}`

    #### Breakdown:

    `steps.1.output.selected_key`: A JSON object

    `[steps.1.output.selected_key2]`: dynamically accesses a key inside selected\_key.

    The result of `steps.1.output.selected_key[ steps.1.output.selected_key2]` is used as a key to index into `steps.2.output.keymap`

    ### Example:

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/0JKaSiVOyIaH-NI8/img/ExpressionLanguage/VarWithinVar.png?fit=max&auto=format&n=0JKaSiVOyIaH-NI8&q=85&s=2984cd8495c0c429d85ad29e1323b8c7" width="1725" height="1079" data-path="img/ExpressionLanguage/VarWithinVar.png" />
    </Frame>
  </Accordion>

  <Accordion title="Dynamic Loop Limiter">
    ## Dynamic Loop Limiter

    When configuring loops in workflows, it is important that the loop limit corresponds correctly to the size of the list it iterates over. Setting a loop limit that exceeds the length of the list will cause the loop to fail with an error.

    This use case demonstrates how to dynamically set the loop limit by comparing the length of the list with a predefined maximum limit and selecting the appropriate value to avoid errors.

    ### Syntax:

    `{{len(variables.data_to_loop) < variables.loop_max ? len(variables.data_to_loop)-1 : variables.loop_max}}`

    #### Breakdown:

    `len(variables.data_to_loop)`: Returns the number of items in the list stored in the variable data\_to\_loop.

    `< variables.loop_max`: Compares the list length to the maximum allowed number of iterations, loop\_max.

    `? ... : ...`: This ternary operator returns one of two values depending on the comparison:

    * **If true**, it returns `len(variables.data_to_loop) - 1` (the last valid index of the list).
    * **If false**, it returns the maximum loop limit, `variables.loop_max`.

    `len(variables.data_to_loop) - 1`: Because loops are zero-indexed, this sets the loop limit to the last valid item index if the list is shorter than the max limit.

    `variables.loop_max`: The maximum number of iterations allowed if the list is longer or equal in length.

    ### Examples

    1. **List shorter than `loop_max`**

       * `variables.data_to_loop = ["item1", "item2", "item3"]`
       * `variables.loop_max    = 5`

       **Evaluation**

       * `len(data_to_loop) = 3`
       * `3 < 5` → **True**
       * Result → `3 - 1 = 2`

       **Outcome**
       The loop limit is set to `2` (allowing indices 0, 1, 2).

    2. **List longer than `loop_max`**

       * `variables.data_to_loop = ["item1", "item2", "item3"]`
       * `variables.loop_max    = 2`

       **Evaluation**

       * `len(data_to_loop) = 3`
       * `3 < 2` → **False**
       * Result → `variables.loop_max = 2`

       **Outcome**
       The loop limit remains at `2`.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/0JKaSiVOyIaH-NI8/img/ExpressionLanguage/DynamicLoopLimiter.png?fit=max&auto=format&n=0JKaSiVOyIaH-NI8&q=85&s=9188782a991ca4452c0fce959493c7c3" width="1726" height="1077" data-path="img/ExpressionLanguage/DynamicLoopLimiter.png" />
    </Frame>
  </Accordion>

  <Accordion title="String Building">
    ## String Building

    This use case demonstrates how to dynamically build a descriptive string using values from multiple elements in email header (JSON format). By using a combination of direct references and string concatenation, you can format output data into a clear, readable message.

    ### Syntax:

    `{{steps.2.output.payload.headers[0].value + " ( " + steps.2.output.payload.headers[1].name + steps.2.output.payload.headers[1].value + " ) "}}`

    #### Breakdown:

    `inputs.Name`: This retrieves the Delivered-To email address from the email header.

    `+`: String concatenation which combines multiple substrings into one final string.

    `" ( " + ... + " ) "`: Literal characters that wrap the date value(`steps.2.output.payload.headers[1].value`) in parentheses.

    `steps.2.output.payload.headers[1].name`: Retrieves the name of the second header, which in this case is `Received`.

    `steps.2.output.payload.headers[1].value`: Represents metadata about the message transmission (e.g., SMTP server info, timestamp, etc.).

    ### Example:

    The expression combines multiple different strings into a single output:

    [johndoe@gmail.com](mailto:johndoe@gmail.com) (Received by 2002:a2ea:e990:0:b2d6:f3f:399 with SMTP id x16csp3161761qj; Wed, 10 Apr 2024 03:07:20 -0700 (PDT))

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/0JKaSiVOyIaH-NI8/img/ExpressionLanguage/BuildingStrings.png?fit=max&auto=format&n=0JKaSiVOyIaH-NI8&q=85&s=65cf528a664cbaf58d281cfe5af70d0f" width="1726" height="1076" data-path="img/ExpressionLanguage/BuildingStrings.png" />
    </Frame>
  </Accordion>
</AccordionGroup>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.