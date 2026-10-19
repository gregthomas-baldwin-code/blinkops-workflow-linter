> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Flow Control Actions

> Flow Control Actions allow users to control the flow of their Workflows

<div className="flow-table">
  | Flow Control Action Name | Icon |
  | - | - |
  | [If](#if) | <img src="https://mintcdn.com/blinkops-2/5NhCfwxxC44NScsN/img/Icons/If.svg?fit=max&auto=format&n=5NhCfwxxC44NScsN&q=85&s=ee5b82e222b34b444cde2331196c7118" width="35" height="35" data-path="img/Icons/If.svg" /> |
  | [Switch Case](#switch-case) | <img src="https://mintcdn.com/blinkops-2/5NhCfwxxC44NScsN/img/Icons/Switch.svg?fit=max&auto=format&n=5NhCfwxxC44NScsN&q=85&s=dbe26bde42c8d1d7f9dfcdab30060309" width="35" height="35" data-path="img/Icons/Switch.svg" /> |
  | [Loop Through](#loop-through) | <img src="https://mintcdn.com/blinkops-2/ojHYuDeYX5FWuN8a/img/Icons/forloop.svg?fit=max&auto=format&n=ojHYuDeYX5FWuN8a&q=85&s=320957fbbf1724e50557896c107c46d2" width="36" height="36" data-path="img/Icons/forloop.svg" /> |
  | [While](#while-loop) | <img src="https://mintcdn.com/blinkops-2/ojHYuDeYX5FWuN8a/img/Icons/while.svg?fit=max&auto=format&n=ojHYuDeYX5FWuN8a&q=85&s=d371fc2690fe115b93ba2c3940c4ab85" width="36" height="36" data-path="img/Icons/while.svg" /> |
  | [Wait](#wait) | <img src="https://mintcdn.com/blinkops-2/ojHYuDeYX5FWuN8a/img/Icons/Wait.svg?fit=max&auto=format&n=ojHYuDeYX5FWuN8a&q=85&s=6e58cc812e16d3bd758b24370c192496" width="36" height="36" data-path="img/Icons/Wait.svg" /> |
  | [Set variables](#set-variables) | <img src="https://mintcdn.com/blinkops-2/ojHYuDeYX5FWuN8a/img/Icons/variable.svg?fit=max&auto=format&n=ojHYuDeYX5FWuN8a&q=85&s=c4ef868667ece408c0296c04029f9634" width="36" height="36" data-path="img/Icons/variable.svg" /> |
  | [Note](#note) | <img src="https://mintcdn.com/blinkops-2/5NhCfwxxC44NScsN/img/Icons/Note.svg?fit=max&auto=format&n=5NhCfwxxC44NScsN&q=85&s=a47ced4d93a2a2df2344365dbe720a0f" width="36" height="36" data-path="img/Icons/Note.svg" /> |
  | [Run On Error](#run-on-error) | <img src="https://mintcdn.com/blinkops-2/5NhCfwxxC44NScsN/img/Icons/OnError.svg?fit=max&auto=format&n=5NhCfwxxC44NScsN&q=85&s=6df4c4a6c99187960664062b6b0f0d26" width="36" height="36" data-path="img/Icons/OnError.svg" /> |
  | [End Run](#end-run) | <img src="https://mintcdn.com/blinkops-2/5NhCfwxxC44NScsN/img/Icons/End.svg?fit=max&auto=format&n=5NhCfwxxC44NScsN&q=85&s=fd9ebdb48478e2fbd123cf41f0cd99c4" width="35" height="35" data-path="img/Icons/End.svg" /> |
</div>

<Note> **Note:** The user interface (UI) of specific flow control steps—such as [If](#if), [Switch](#switch-case), [Loop](#loop-through), [While](#while-loop), and [Run On Error](#run-on-error)—is intentionally designed to differ from standard steps. These flow controls serve as key *intersections* in the workflow, directing execution paths based on conditions, iterations, or variables. Their unique UI emphasizes their role in shaping the logic and flow of the workflow's execution.</Note>

***

## If

`If` actions in the Blink platform play a crucial role in controlling the flow of workflows. They evaluate conditions by comparing values, and based on these comparisons, trigger specific actions. This allows workflows to respond dynamically to different scenarios. By incorporating AND and OR logic, if statements enable more complex decision-making, as they can assess multiple conditions simultaneously, providing greater flexibility in handling various situations.

<Tip>
  <div className="flex flex-row items-center"><img src="https://mintcdn.com/blinkops-2/5NhCfwxxC44NScsN/img/Icons/CheckIf.svg?fit=max&auto=format&n=5NhCfwxxC44NScsN&q=85&s=3b55dbdfe7e6024b674c7bc7d84cc25f" width="24" height="24" data-path="img/Icons/CheckIf.svg" /> - The 'Check If' Icon </div>

  This icon, which appears to the left of the step, verifies whether a specific condition is either `true` or `false` without running the nested actions.
</Tip>

<div className="flex flex-row items-center"><img id="fc" src="https://mintcdn.com/blinkops-2/5NhCfwxxC44NScsN/img/Icons/If.svg?fit=max&auto=format&n=5NhCfwxxC44NScsN&q=85&s=ee5b82e222b34b444cde2331196c7118" width="35" height="35" data-path="img/Icons/If.svg" /><p className="ml-2"> Determines the workflow's direction based on whether a condition is `true` or `false`. If `true`, the workflow follows one course of action; if `false`, it follows an alternative course</p></div>

<Note>Adding steps to the `True` or `False` branch is optional — you can leave either branch empty if no action is needed.</Note>

<Accordion title="`If`- Use Case Example" icon="gear-complex-code">
  <Frame>
    <img src="https://mintcdn.com/blinkops-2/O8d41-iCEMqmd4Il/img/Actions/IfExample.png?fit=max&auto=format&n=O8d41-iCEMqmd4Il&q=85&s=2d2967a6e56c463e1d4dbc454cdfbab8" width="1727" height="1080" data-path="img/Actions/IfExample.png" />
  </Frame>

  The "If" statement in the use case example is being used to check whether a scanned URL is classified as "Malicious."

  * The workflow is triggered when a **new Gmail message** is received.

  * The system **extracts URLs** from the email.

  * Each URL is **scanned** using VirusTotal (or another scanning tool).

  * The **If statement** checks if the scanned URL is flagged as **"Malicious."**

    * If **true**, the workflow notifies a Slack channel and deletes the email to prevent potential threats.

    * If **false**, the workflow continues without taking these actions.
</Accordion>

***

## Switch Case

<div className="flex flex-row items-center"><img id="fc" src="https://mintcdn.com/blinkops-2/5NhCfwxxC44NScsN/img/Icons/Switch.svg?fit=max&auto=format&n=5NhCfwxxC44NScsN&q=85&s=dbe26bde42c8d1d7f9dfcdab30060309" width="35" height="35" data-path="img/Icons/Switch.svg" /><p className="ml-2">The Switch Case action allows you to compare a given value with a series of possible values and execute different blocks of actions based on the matching case value.</p></div>

<div className="integrations-table">
  | Flow Control Action Name | description |
  | - | - |
  | Switch Variable | The Switch Case includes a Switch Variable which is compared to a list of case values. If any of these case values matches the Switch Variable, it prompts the execution of a particular block of actions associated with that matching case value. |
  | Cases | Each Case is a value that is compared against the Switch Variable if the value of the Switch Variable matches a Case value, the corresponding block of actions associated with that will be executed |
  | Actions | Within each case, you can choose any set of actions to be performed. |
  | Case Default | The default case serves as a default output option and comes into play when the Switch Variable does not match any of the other Case values. |
</div>

<Tip>Reorder cases by easily dragging & dropping to reorder. The system evaluates cases from top to bottom: the first matching condition runs, and if no condition matches, the default case is used.</Tip>

<Accordion title="Configuring the Switch Case Flow Control" icon="list-ol">
  1. Begin by setting the switch case variable. This is the variable whose value will be evaluated against each case condition. Only the case with a matching condition will run its associated actions.

  <Frame>
    <img src="https://mintcdn.com/blinkops-2/vVU9PEubpmnJVn0j/img/Actions/SwitchVar.png?fit=max&auto=format&n=vVU9PEubpmnJVn0j&q=85&s=43d2936559c83d08f83c0db55e56e2a5" width="1728" height="1085" data-path="img/Actions/SwitchVar.png" />
  </Frame>

  2. Click the "Add Case" button to create a new case branch.

  <Frame>
    <img src="https://mintcdn.com/blinkops-2/yRkQ-wRlnQIXwr-A/img/Actions/AddCaseSwitch.png?fit=max&auto=format&n=yRkQ-wRlnQIXwr-A&q=85&s=28f00b5147dda2850e2dc3c5268585c3" width="1725" height="1078" data-path="img/Actions/AddCaseSwitch.png" />
  </Frame>

  3. Provide a case name and set the case condition- this is the specific value that the switch case variable (created in `step 1`) will be compared against.

  <Note>Case names update automatically based on their conditions.</Note>

  <Frame>
    <img src="https://mintcdn.com/blinkops-2/yRkQ-wRlnQIXwr-A/img/Actions/ConfigureSwitch.png?fit=max&auto=format&n=yRkQ-wRlnQIXwr-A&q=85&s=e756235d440d2fe69cdcfa8e95421f46" width="1724" height="1083" data-path="img/Actions/ConfigureSwitch.png" />
  </Frame>

  4. Inside each case, you can configure a unique set of actions that should run when that case is triggered.

  <Frame>
    <img src="https://mintcdn.com/blinkops-2/yRkQ-wRlnQIXwr-A/img/Actions/AddCaseActions.png?fit=max&auto=format&n=yRkQ-wRlnQIXwr-A&q=85&s=8d567d744084f7d531c2f2c732ea55db" width="1720" height="1076" data-path="img/Actions/AddCaseActions.png" />
  </Frame>
</Accordion>

<Accordion title="Switch- Use Case Example" icon="gear-complex-code">
  ### Overview

  In the provided workflow example, the **Switch case** action is used to implement conditional branching based on the incoming data from the **Blink Web Form response** trigger. It allows the workflow to take different paths depending on the value of a specified variable or condition.

  <Frame>
    <img src="https://mintcdn.com/blinkops-2/fCk0vBoCsdVcLcbp/img/Actions/WebFormDemo.png?fit=max&auto=format&n=fCk0vBoCsdVcLcbp&q=85&s=004adb623978c8f49cb5f982fb54155c" width="3450" height="2162" data-path="img/Actions/WebFormDemo.png" />
  </Frame>

  ### **Workflow Logic with `Switch Case` Action**

  1. **Switch Case Action:**
     * The workflow starts with a **Switch case** action that evaluates the user input from the [web form](/docs/blink-platform/web-form/web-form) response.

  2. **Case 1: Self-Service Actions**
     * If the web form submission indicates a self-service request, the workflow processes it by sending the request to the appropriate system and logging user feedback.

  3. **Case 2: Report an Issue**
     * If the submission is about reporting an issue, the workflow logs the report, creates an issue in Jira, and captures user feedback.

  4. **Case 3: Request Access**
     * If the submission is about requesting access, the workflow opens a ticket in ServiceNow with the request details, and captures user feedback.

  5. **Default Case:**
     * If the request does not match any specific case, the workflow treats it as a general request, creates a ticket in Zendesk, and logs user feedback.
</Accordion>

***

## Loop Through

<div className="flex flex-row items-center"><img id="fc" src="https://mintcdn.com/blinkops-2/ojHYuDeYX5FWuN8a/img/Icons/forloop.svg?fit=max&auto=format&n=ojHYuDeYX5FWuN8a&q=85&s=320957fbbf1724e50557896c107c46d2" width="36" height="36" data-path="img/Icons/forloop.svg" /><p className="ml-2">The loop through action executes an action or multiple actions for each element in a list. </p></div>

<Tip>
  To reference an item in a list you can use [Expression language](/docs/workflows/building-workflows/dynamic-variables/expression-language/workflow-engine-variables.mdx) or the [variable Picker](/docs/workflows/building-workflows/dynamic-variables/variable-picker) and the [JSON Dot Walking Method](/docs/workflows/building-workflows/dynamic-variables/variable-picker#referencing-a-key-in-a-json-object) to reference the current item in the loop.
</Tip>

<AccordionGroup>
  <Accordion title="Keywords" icon="list-radio">
    ### **Item**

    1. An **item** is an individual element in a list that is being looped through.

       * **Accepted Values:**
         * String
         * Numbers
         * Variable
         * List of JSON objects

       * **Supported Formats:**
         * **Comma-Separated:** Example: `1,2,3,4`
         * **Array Format:** Example: `[1,2,3,'c']`

    2. **index** - refers to the variable that keeps track of the current iteration. By default the first iteration index is `0`

    3. **total\_items**- refers to the total number of items in the list.
  </Accordion>

  <Accordion title="Debugging a Loop" icon="ban-bug">
    In the loop action there are three distinct methods you can use to debug a loop: `Run All`, `Run Next Item` and `Reset`.

    <Note> **Note**: The index in a list always starts from 0.</Note>

    <Icon icon="https://mintcdn.com/blinkops-2/5NhCfwxxC44NScsN/img/Icons/RunAll.svg?fit=max&auto=format&n=5NhCfwxxC44NScsN&q=85&s=07a4a8e5f0ba02261ba1e466919fbd03" size={30} width="24" height="24" data-path="img/Icons/RunAll.svg" /> - **Run All**: iterates through the entire list of items once.
    <Tip>If you hover over the **Run All** action, a tooltip will appear explaining the starting index and the index the iteration will stop at. </Tip>
    <Icon icon="https://mintcdn.com/blinkops-2/5NhCfwxxC44NScsN/img/Icons/RunNextIndex.svg?fit=max&auto=format&n=5NhCfwxxC44NScsN&q=85&s=876680939ec20333e3c95f3d0b7b9f83" size={30} width="24" height="24" data-path="img/Icons/RunNextIndex.svg" /> - **Run Next Item**: Runs the next item in the list when iterating through the list.

    <Icon icon="https://mintcdn.com/blinkops-2/5NhCfwxxC44NScsN/img/Icons/RunNextItem.svg?fit=max&auto=format&n=5NhCfwxxC44NScsN&q=85&s=0e0f97a7ab811156a9a2dc2b7f67952e" size={30} width="24" height="24" data-path="img/Icons/RunNextItem.svg" /> - **Load Next Index**: Allows users to load the next iteration of a loop and work with the loop item variable without executing the entire loop.
    <Tip>If you hover over the **Run Next Index** action, a tooltip will appear explaining the index that will run next.</Tip>
    <Icon icon="https://mintcdn.com/blinkops-2/5NhCfwxxC44NScsN/img/Icons/Reset.svg?fit=max&auto=format&n=5NhCfwxxC44NScsN&q=85&s=3df52bf34fcc45f63df70a9b71df6396" size={30} width="24" height="24" data-path="img/Icons/Reset.svg" /> - **Reset**: resets all the changes made when applying any settings to the loop.
  </Accordion>

  <Accordion title="Advanced Settings" icon="gear">
    1. **Start from Index** allows you to start your loop at a specified index in your input list.

    2. **Stop at Index** allows you to end your loop at a specified index in your input list.

    <Note>
      Please note when using the **Run All** or the **Run Next Item** action and an advanced setting has been applied, it will continue iterating through the list based on the previous list index displayed in the output.

      For example, if you start the loop iteration in the middle of a list and then choose the **Run All** action, it won't restart the loop from the beginning of the list. Instead, it will resume the loop from where you left off.

      The **Start from Index** and the **Stop at Index** advanced settings are applied in both edit mode as well as run time.
    </Note>
  </Accordion>

  <Accordion title="For Each Loop- Use Case Example" icon="gear-complex-code">
    ### Overview

    This workflow is designed to detect and respond to potentially malicious emails in Gmail. It starts when a new email arrives and extracts key details, including any URLs present in the email. The workflow then analyzes each URL to determine if it is malicious. If a malicious URL is found, the workflow takes automated response actions, such as notifying a channel and deleting the email.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/O8d41-iCEMqmd4Il/img/Actions/ForEachExample.png?fit=max&auto=format&n=O8d41-iCEMqmd4Il&q=85&s=54384b1727862bfe8dcc951683193840" width="1727" height="1080" data-path="img/Actions/ForEachExample.png" />
    </Frame>

    ### **Workflow Logic with Loop Action**

    The loop action iterates over each URL extracted from the email. Here’s how it works:

    1. **Extract URLs** – The workflow retrieves all URLs from the email.
    2. **Loop on Each URL** – The loop action takes each URL one by one and processes it through the following steps:
       * **Scan URL** – The URL is checked using a security service (e.g., VirusTotal).
       * **If Malicious** – A condition checks if the scan result marks the URL as malicious.
       * **Notify & Delete** – If malicious, the workflow notifies a designated channel (e.g., Slack) and deletes the email from Gmail.
  </Accordion>
</AccordionGroup>

## While Loop

<div className="flex flex-row items-center"><img id="fc" src="https://mintcdn.com/blinkops-2/ojHYuDeYX5FWuN8a/img/Icons/while.svg?fit=max&auto=format&n=ojHYuDeYX5FWuN8a&q=85&s=d371fc2690fe115b93ba2c3940c4ab85" width="36" height="36" data-path="img/Icons/while.svg" /><p className="ml-2"> The **'While'** action enables you to run an action or multiple actions for as long as specified conditions are met.</p></div>

<Note>
  **Note:** By default, if the condition is not met at the start, the while loop will not execute at all.
</Note>

<AccordionGroup>
  <Accordion title="Advanced Settings" icon="gear">
    ### Do-While Loop

    1. A `Do-while` loop ensures a step or multiple steps are executed at least once. After the initial execution, it repeatedly runs the subsequent steps for as long as the specified conditions are met.

    2. You can enter the maximum amount of iterations you would like your` While` Loop or `Do-while` loop to carry out.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/6FB3Ba1GMrUPQ2E_/img/Actions/DoWhileNew.png?fit=max&auto=format&n=6FB3Ba1GMrUPQ2E_&q=85&s=bffe061002eead28a4432d70b3ef933c" width="1728" height="1076" data-path="img/Actions/DoWhileNew.png" />
    </Frame>
  </Accordion>

  <Accordion title="While Loop- Use Case Example" icon="gear-complex-code">
    ### Overview

    This **Splunk Suspicious File Alert** workflow automates threat response by analyzing potentially malicious files detected by Splunk, creating a Jira issue, and checking VirusTotal for threat intelligence. If a file has more than three malicious detections, it prompts a security analyst via Slack to decide whether to isolate the affected endpoint using Cortex XDR.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/fCk0vBoCsdVcLcbp/img/Actions/WhileExample.png?fit=max&auto=format&n=fCk0vBoCsdVcLcbp&q=85&s=937671522fbc85fb339801ae30c83092" width="1728" height="1083" data-path="img/Actions/WhileExample.png" />
    </Frame>

    ### **Workflow Logic with `While` Action**

    The while loop in the workflow is configured with the condition:

    **If "malicious" is greater than 3, continue looping.**

    * This means the workflow will repeatedly check if the number of malicious detections in the file report (from VirusTotal) exceeds 3. If this condition holds true, the loop will continue executing the steps inside it.

    **Inside the loop:**

    * A Slack message is sent to ask a question.
    * If the answer equals "Isolate", the endpoint is isolated using Cortex XDR.
  </Accordion>
</AccordionGroup>

***

## Wait

<div className="flex flex-row items-center"><img id="fc" src="https://mintcdn.com/blinkops-2/ojHYuDeYX5FWuN8a/img/Icons/Wait.svg?fit=max&auto=format&n=ojHYuDeYX5FWuN8a&q=85&s=6e58cc812e16d3bd758b24370c192496" width="36" height="36" data-path="img/Icons/Wait.svg" /><p className="ml-2">The **'Wait'**  Action pauses the workflow for a set time before continuing to run the rest of the workflow. You can specify the wait time in **seconds, minutes, or hours**.</p></div>

<Note>
  The "Wait" action will have a maximum timeout of `14` days. For more information please visit the [Workflows Runtime Limitations](/docs/workflows/system-limits) section of our documentation.
</Note>

<div className="integrations-table">
  | Variable type | Default value | |
  | - | - | - |
  | Wait For | 1. [Time Interval](#wait-for-time-interval), 2. [Workflow Execution](#wait-for-workflow-execution), 3. [Web Form Response](#wait-for-web-form-response) or 4. [Callback Response](#wait-for-callback-response) | |
  | Timeout | The time value- when reached, the step is completed and the workflow will continue | |
  | Time Unit | Seconds, Minutes, or Hours. | |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/fCk0vBoCsdVcLcbp/img/Actions/Wait.png?fit=max&auto=format&n=fCk0vBoCsdVcLcbp&q=85&s=06ab938ee6663274cb6267f71dac0791" width="3456" height="2152" data-path="img/Actions/Wait.png" />
</Frame>

<AccordionGroup title="Wait">
  <Accordion title="Wait for: Time Interval" icon="pause">
    This is the default mode for the *Wait Action*. It directs the Workflow to wait a specified amount of time until it continues running. When configuring the step, specify the number of seconds, minutes or hours to wait.
  </Accordion>

  <Accordion title="Wait for: Workflow Execution" icon="pause">
    This mode enables you to wait for steps in your Workflow that execute other workflows asynchronously. The step is paused until all the executions it is waiting for, have finished running. The output of the Wait Action will return details of the executions it is waiting for.
  </Accordion>

  <Accordion title="Wait For: Web Form Response" icon="pause">
    The mode is used with the [New Web Form Action](/docs/blink-platform/web-form) to pause the workflow until a response from a user is submitted through the web form. This ensures the workflow proceeds only after the necessary input is received.
  </Accordion>

  <Accordion title="Wait For: Callback Response" icon="pause">
    This mode is used together with the [Generate Callback URL](/docs/workflows/building-workflows/actions/basic-actions/http-actions/generate-callback-url) action. It pauses the workflow until the external service completes its process and sends back the required data, allowing the workflow to resume once a response is received.

    * In the **Wait** step, under the **Callback URL's** parameter, users should provide a single callback URL or a comma-separated list of URLs to wait for.
    * The **Wait** action completes only after all specified callback URLs have responded.
  </Accordion>
</AccordionGroup>

***

## Set Variables

<div className="flex flex-row items-center"><img src="https://mintcdn.com/blinkops-2/ojHYuDeYX5FWuN8a/img/Icons/variable.svg?fit=max&auto=format&n=ojHYuDeYX5FWuN8a&q=85&s=c4ef868667ece408c0296c04029f9634" width="36" height="36" data-path="img/Icons/variable.svg" /><p className="ml-2">The set variables Action enables users to define variables and use them in the execution of the Workflow. </p></div>

**Defining and using variables:**

<Steps>
  <Step>
    Add the 'Set Variables' action to the Workflow Editor to create a set variables Step.
  </Step>

  <Step>
    Select a variable type (boolean, numeric, string, or list.)
  </Step>

  <Step>
    Enter a name for the variable.
  </Step>

  <Step>
    Set the value for the variable. If not set, the default values are as follows:

    <div className="integrations-table">
      | Variable Type | Default value | Notes |
      | - | - | - |
      | Numeric | 0 | |
      | String | "" | |
      | List | \[] | Lists can be comma-separated or in `JSON` list format. |
      | Boolean | false | When defining a Boolean-type variable, the Blink supports multiple input formats to represent `true` and `false`. <br /> The following values are interpreted as **true**: <ul> <li>`true`/`TRUE`/ `True` </li> <li>`1`</li><li> `t` / `T` </li></ul>The following values are interpreted as **false**: <ul> <li> `false`/ `FALSE`/ `False` </li><li>`0` </li><li> `f` / `F` </li> <li>If no value is provided (i.e., the field is left blank), it is automatically interpreted as **false** by default. This normalization ensures consistent Boolean handling regardless of input format.</li> </ul> |
    </div>
  </Step>

  <Step>
    Click the 'Add Variable' button to add more variables
  </Step>

  <Step>
    Use the newly created variable, in the following steps of your workflow, using the [Variable Picker](/docs/workflows/building-workflows/dynamic-variables/variable-picker) or [Blink's Expression Language](/docs/workflows/building-workflows/dynamic-variables/expression-language/workflow-engine-variables).
  </Step>
</Steps>

<Accordion title="'Set Variable' Action- Use Case Example" icon="gear-complex-code">
  <Frame>
    <img src="https://mintcdn.com/blinkops-2/YCPogV16GcSamxG0/img/Actions/SetVariableExample.png?fit=max&auto=format&n=YCPogV16GcSamxG0&q=85&s=f10749842694e755c983c80c5c5c31a6" width="1728" height="1082" data-path="img/Actions/SetVariableExample.png" />
  </Frame>

  The **'Set Variable'** action allows you to store and reuse values in different parts of your workflow, depending on how you configure it.

  In the following workflow use case example, we assign a variable to store the name of a Slack channel (type: string). This variable is then referenced in two actions:

  In the [Ask a Question Via Slack](/docs/workflows/building-workflows/actions/advanced-actions/interactive-actions/ask-a-question/ask-a-question-slack) action (Step 1), where it is used in the "To" parameter to specify the recipient channel.
  In the [Send Slack Message](/docs/workflows/building-workflows/actions/advanced-actions/interactive-actions/slack-interactivity) action (step 9), where it is reused to send a message to the same channel.
</Accordion>

***

## Note

<div className="flex flex-row items-center"><img id="fc-actions" src="https://mintcdn.com/blinkops-2/5NhCfwxxC44NScsN/img/Icons/Note.svg?fit=max&auto=format&n=5NhCfwxxC44NScsN&q=85&s=a47ced4d93a2a2df2344365dbe720a0f" width="36" height="36" data-path="img/Icons/Note.svg" /><p className="ml-2">The 'Note' action provides a [rich text editor](/docs/blink-platform/interface-components/rich-text-editor) that allows you to add helpful instructions, explanations, or contextual guidance for end-users within a Workflow. The text editor supports Markdown (`md`) syntax. This action is useful for adding clarity to complex workflows, ensuring users understand the next steps or any important details.</p></div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/YCPogV16GcSamxG0/img/Actions/Notes.png?fit=max&auto=format&n=YCPogV16GcSamxG0&q=85&s=ecea647eb28f75f53ed409e8a3b44514" width="1728" height="1083" data-path="img/Actions/Notes.png" />
</Frame>

***

## Run - On Error

<div className="flex flex-row items-center"><img src="https://mintcdn.com/blinkops-2/5NhCfwxxC44NScsN/img/Icons/OnError.svg?fit=max&auto=format&n=5NhCfwxxC44NScsN&q=85&s=6df4c4a6c99187960664062b6b0f0d26" width="36" height="36" data-path="img/Icons/OnError.svg" /><p className="ml-2">The **Run - On Error** action is used to handle errors that might occur during the execution of a workflow. It utilizes a dual-step structure, consisting of **Run** and **On Error**, designed to efficiently manage any errors that might arise while executing actions within the **Run** phase.</p></div>

* **Run**: This step is designed for placing action(s) that contribute to the overall Workflow sequence.
* **On Error**: If there is an error during Run block, the flow will automatically shift to the On Error block. In this block, specific actions are taken to address the error. The error JSON object will be made available within the **On Error** block to assist in handling the error.

<Note>
  If an error occurs in the **Run** block but is successfully handled in the **On-Error** block, the workflow will continue to run after executing the **On-Error** block. However, if errors occur in both the **Run** and **On-Error** blocks, then the workflow will **fail**.
</Note>

<Accordion title="Run- On Error- Use Case Example" icon="gear-complex-code">
  <Frame>
    <img src="https://mintcdn.com/blinkops-2/YCPogV16GcSamxG0/img/Actions/OnErrorExample.png?fit=max&auto=format&n=YCPogV16GcSamxG0&q=85&s=848775c1598800a04a285d6313cc9e48" width="3454" height="2158" data-path="img/Actions/OnErrorExample.png" />
  </Frame>

  ### **Workflow Logic with `Run - On Error` Action**

  1. The workflow is triggered when a new user is added to a group in Okta.

  2. It retrieves the user's email and asks an administrator (via Slack) if they authorized the action.

  3. If the admin denies responsibility, the workflow deactivates the user in Okta and notifies the security team.

  4. The **On Error** statement is a fail-safe mechanism that catches any unexpected issues (e.g., API failures, Slack/Okta connection issues, or execution errors).

  5. If an error occurs at any step, it sends a notification to the security group via Slack, alerting them to unusual activity.
</Accordion>

***

## End Run

<div className="flex flex-row items-center"><img id="fc" src="https://mintcdn.com/blinkops-2/5NhCfwxxC44NScsN/img/Icons/End.svg?fit=max&auto=format&n=5NhCfwxxC44NScsN&q=85&s=fd9ebdb48478e2fbd123cf41f0cd99c4" width="35" height="35" data-path="img/Icons/End.svg" /><p className="ml-2">The End Run Action enables you to select the final status of an execution, **Completed** or **Failed**. </p></div>

<Accordion title="End Run- Use Case Example" icon="gear-complex-code">
  ### Overview

  This workflow monitors when a user is added to a privileged group and verifies the action to ensure it's authorized. Depending on the user's response, the workflow either closes the case or initiates remediation steps.

  <Frame>
    <img src="https://mintcdn.com/blinkops-2/6FB3Ba1GMrUPQ2E_/img/Actions/EndRunExample.png?fit=max&auto=format&n=6FB3Ba1GMrUPQ2E_&q=85&s=32c4e3c642400e8e897ea3e16a1a4764" width="1728" height="1078" data-path="img/Actions/EndRunExample.png" />
  </Frame>

  ### **Workflow Logic with `End Run` Action**

  1. **Set Variables**
     Captures key information related to the event, such as the user details, group name, and timestamp.

  2. **Verify Action with User**
     Sends a Slack message to the affected user, prompting them to confirm whether the action was expected and authorized.

  3. **Evaluate User Response**
     A conditional check is used to determine if the user acknowledged the action as approved.

     * **If the user approved the action:**

       * **Close Case as Approved**
         The incident is considered benign and marked as resolved.
       * **End Run with Status: Completed**
         Stops workflow execution and marks the run as successful.

     * **If the user did not approve or did not respond:**

       * **Deactivate User**
         Disables the user's account in Okta.
       * **Revoke All User Sessions**
         Ends all active sessions for the user to prevent further access.
       * **Update Case Severity**
         Escalates the case severity level to reflect the potential risk.
       * **Send Message to Security Group**
         Notifies the security team via Slack about the unauthorized or unverified action.

  ***

  ### Purpose of the "End Run" Action

  The **"End run with status Completed"** step ensures the workflow concludes cleanly when no further action is required. It provides a clear stopping point and records the successful resolution in logs and dashboards. This step is critical for reporting and distinguishes approved events from security incidents requiring follow-up.
</Accordion>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.