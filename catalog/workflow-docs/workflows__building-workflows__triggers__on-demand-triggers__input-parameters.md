> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Input Parameters

> Define input parameters that users provide when manually triggering a Blink workflow.

On-demand workflows can use **user-input parameters** to allow dynamic use of relevant values during execution. By defining these parameters, users can tailor workflows to specific needs without altering the workflow logic. Input parameters in on-demand workflows are always provided at runtime, enabling flexible and adaptable execution for various scenarios.

<Accordion title="Example Use Cases" icon="magnifying-glass-plus">
  <Card title="Standardize Customer Name Formatting" icon="user">
    **Business Use Case:**\
    In customer relationship management (CRM) systems, user-entered data can be inconsistent (e.g., lowercase names, extra spaces). Standardizing names ensures consistency across reports, email communications, and customer records. To do this, the builder defines the customer name as a free text field for the input parameter when building the workflow.

    <br />

    **When Input is Entered:**

    * The user provides a **customer's full name** at runtime when adding or updating a record.

    <br />

    **Workflow Action:**

    * The workflow trims extra spaces and formats the name into **Title Case** (`John Doe` instead of `JOHN DOE` or `john doe`).
    * The formatted name is then stored or used in customer communications.

    <br />

    **See It In Action**

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/VXKzhvwYkcutAgt0/img/InputParams/input-use-variables.gif?s=498ecf5afc5b2e737dce14493ddfa071" width="1520" height="820" data-path="img/InputParams/input-use-variables.gif" />
    </Frame>
  </Card>

  <Card title="Select a Report Type" icon="file-chart-column">
    **Business Use Case:**\
    Organizations often generate reports based on predefined categories such as Sales, Marketing, or Finance. This input allows users to dynamically select the type of report to generate. To do this, the builder defines the available report types for the input parameter Single Select list when building the workflow.

    <br />

    **When Input is Entered:**

    * At the start of the workflow, the user selects a report type from the list that you configured.

    <br />

    **Workflow Action:**

    * The workflow references `{{ inputs.report_type }}` to determine the type of report.
    * The corresponding report is generated and stored.

    <br />

    **See It In Action**

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/VXKzhvwYkcutAgt0/img/InputParams/input-new-report.gif?s=540f07e6c0cf1f73308a9805bd02d489" width="1436" height="898" data-path="img/InputParams/input-new-report.gif" />
    </Frame>
  </Card>

  <Card title="Get a List of Dev Tasks" icon="code">
    **Business Use Case:**\
    Technical teams often track tickets they’ve opened for customers, but dev teams prefer to limit direct access for efficiency and security reasons.

    With Blink, collaborating teams can trigger a Self-Service Portal flow to retrieve ticket statuses without disrupting dev team workflows.

    In this example, ClickUp is used to manage sprints. The builder sets up a multi-select input for ClickUp spaces, allowing users to choose one or more spaces and receive task statuses via email.

    <br />

    **When Input is Entered:**\
    The users choose one or more spaces within ClickUp from which to receive ticket statuses via email.

    <br />

    **Parameters:**

    `spaces` (Multi-Select, required) → One or more ClickUp spaces to retrieve tasks from.

    <br />

    **Workflow Action:**

    Query ClickUp for tasks in the selected spaces, format the results, and send an email with the list.

    <br />

    **See It In Action:**

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/VXKzhvwYkcutAgt0/img/InputParams/input-clickup-example.gif?s=07faf5685c08574fe5db30ce5f607f09" width="1666" height="998" data-path="img/InputParams/input-clickup-example.gif" />
    </Frame>
  </Card>
</Accordion>

***

## Input Parameter Configuration Options

By using input parameters, workflows can be more flexible and adaptable to different scenarios without requiring changes to the workflow logic itself.

Input parameters can be configured to provide flexibility in workflow execution. They can be:

<div className="integrations-table">
  | Input Control Type | Description |
  | - | - |
  | **Mandatory or optional** | Some parameters require input before execution, while others can be left empty. |
  | **Flexible Input Fields** | Builders can configure different kinds of lists including a controlled set of options from which the users can choose when triggering the workflow, enable free text, use checkboxes and configure other input types as well. |
  | **Static or dynamic** | Static inputs remain fixed, whereas dynamic inputs retrieve values from [global variables](/docs/workflows/building-workflows/dynamic-variables/global-variables). |
</div>

## Input Parameter Types

<Note>
  The *file* [input parameter](/docs/workflows/building-workflows/triggers/on-demand-triggers/input-parameters) is not supported in triggered [subflows](/docs/workflows/building-workflows/actions/basic-actions/subflow-actions).
</Note>

When defining an on-demand workflow, you can choose from the following input parameter types:

<div className="integrations-table">
  | Parameter Type | Description | Example |
  | - | - | - |
  | **Text** | Single-line text input for short entries | A user name |
  | **Long Text** | Multi-line text field for detailed input | A description or detailed explanation |
  | **Rich Text** | Allows you to format long text with enhanced styling options beyond plain text. You can apply formatting such as bold, italics, headings, lists, links, code blocks, and more. | **bold**, *italics*, `code blocks`, [links](#) |
  | **Number** | Numeric value input | `100` |
  | **Single-Select** | Choose one value from the list; if enabled, users can alternatively add free text. | Choose one from the following:  - Apple - Orange - Banana |
  | **Multi-Select** | Choose multiple values from the list; if enabled, users can alternatively add free text. | Choose all that apply: - Apple - Orange - Banana |
  | **Checkbox** | True/False input | |
  | **Date and Time** | Pick a specific date/time or relative value | |
  | **Connection** | Select a configured connection | From the list of available connections. |
  | **File** | Upload a file (Max: **500MB**) | For example, a `PDF ` |
  | **List** | Provide multiple string values | A list of values. For example, a list of names:  Biff, Martin, Lorraine |
</div>

***

## Configure Input Parameters

<Steps>
  <Step title="Select the On-Demand Workflow">
    [Navigate to the on-demand workflow](/docs/workflows/building-workflows/workflow-editor) that you would like to update with input parameters.
  </Step>

  <Step title="Add Input Parameters to the Trigger">
    From **TRIGGER: ON-DEMAND**, click **+**.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/VXKzhvwYkcutAgt0/img/InputParams/input-configure.gif?s=d83d10d728d6f9626aac185d9c1aa744" width="1520" height="820" data-path="img/InputParams/input-configure.gif" />
    </Frame>
  </Step>

  <Step title="Configure Input Parameter Details">
    Configure the input parameter:

    <div className="integrations-table">
      | Field | Description |
      | - | - |
      | Parameter Name | Unique identifier for the parameter |
      | Parameter Type | Choose the [relevant type](#input-parameter-types) |
      | Display Name | User-friendly name (optional) - this is the way the field will appear in the form for the user. |
      | Required | Toggle on/off to enforce input or leave it as optional. |
      | Placeholder (Available for relevant types) | Sample text shown in the input field (optional). For example, if a User Name is the required input, you can enter an example of the expected format in the placeholder. |
      | Valid and Default Values (Available for relevant types) | Configure the values that are allowed for the parameter. The default value is the pre-populated value (optional). For example, if the input is a date, you can configure the date in advance for the default value. |
      | Options List Mode (Available for relevant types) | Static (values that you manually add when building the workflow) or Dynamic (fetched from a source) |
      | Instructional Text | When enabled, this text is displayed as the tooltip or helper text for this input parameter field |
      | Description | The text shown to the user, either as a tooltip or as helper text, depending on the selected option. |
    </div>

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/EHFuvoqhz9d_YX_e/img/Automations/AdvancedInputSettings.png?fit=max&auto=format&n=EHFuvoqhz9d_YX_e&q=85&s=c0376779595baaf228d3b318a763c268" width="1723" height="1077" data-path="img/Automations/AdvancedInputSettings.png" />
    </Frame>

    <Accordion title="Tip: Configure Input Parameters using the Variable Picker or Expression Language" icon="lightbulb">
      <Tip>
        You can configure input parameters to be referenced in any subsequent workflow steps using either the **Variable Picker** or **Expression Language**, depending on how you want to apply them.

        The following demonstrates the connection between the input and the subsequent steps, where the user enters a prospect name when prompted, and then the next step formats that name:

        <Frame>
          <img src="https://mintcdn.com/blinkops-2/VXKzhvwYkcutAgt0/img/InputParams/input-use-variables.gif?s=498ecf5afc5b2e737dce14493ddfa071" width="1520" height="820" data-path="img/InputParams/input-use-variables.gif" />
        </Frame>

        <div className="integrations-table">
          | Method | Description |
          | - | - |
          | **Variable Picker** | Easily insert input parameters into workflow actions via the [Variable Picker](/docs/workflows/building-workflows/dynamic-variables/variable-picker), which provides a UI-based selection tool. |
          | **Expression Language** | Manually reference input parameters within expressions using [Expression Language](/docs/workflows/building-workflows/dynamic-variables/expression-language/workflow-engine-functions) for more advanced logic and dynamic processing. |
        </div>
      </Tip>
    </Accordion>
  </Step>

  <Step title="Save and Test the Input Parameter">
    Click **Add** to save the parameter.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/FISMXG4NmouWdZPE/img/InputParams/add-input-param.png?fit=max&auto=format&n=FISMXG4NmouWdZPE&q=85&s=16344c8548dc7a1ead8e21998adb9347" width="1717" height="1085" data-path="img/InputParams/add-input-param.png" />
    </Frame>

    The parameter appears in the **TRIGGER** section. When the workflow runs, the value will be retrieved in real time.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/VXKzhvwYkcutAgt0/img/InputParams/input-param-trigger.png?fit=max&auto=format&n=VXKzhvwYkcutAgt0&q=85&s=6e0124cda3d66db004a5cd3314203a52" width="1332" height="883" data-path="img/InputParams/input-param-trigger.png" />
    </Frame>
  </Step>
</Steps>

<Tip> If you go to the [Run Logs](/docs/workflows/debugging-workflows/workflow-run-logs#settings) tab, you can easily copy input parameter values, by selecting the <Icon icon="copy" /> button for quick access. Additionally, you can hover over an input parameter and scroll through long text for better visibility.</Tip>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/VXKzhvwYkcutAgt0/img/InputParams/CopyInputParams.png?fit=max&auto=format&n=VXKzhvwYkcutAgt0&q=85&s=bcc1bb442a1eec52302fdae7643b2b55" width="1728" height="1090" data-path="img/InputParams/CopyInputParams.png" />
</Frame>

***

## Related Articles

<CardGroup cols={3}>
  <Card title="Using On-Demand Triggers" icon="user" href="/docs/workflows/building-workflows/triggers/on-demand-triggers">
    Learn how to manually trigger workflows in BlinkOps.
  </Card>

  <Card title="Testing Workflows" icon="magnifying-glass-arrows-rotate" href="/docs/workflows/testing-workflows">
    Explore methods for testing your workflows to ensure accuracy.
  </Card>

  <Card title="Managing Workflow Permissions" icon="folder-gear" href="/docs/blink-platform/account-management/roles#workspaces-role-scope">
    Control access and permissions for workflow execution.
  </Card>
</CardGroup>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.