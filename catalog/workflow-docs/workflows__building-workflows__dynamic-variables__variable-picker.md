> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Dynamic Variables

> Dynamic variables are variables that are generated during workflow execution. These variables enable workflows to adapt to real-time data, allowing workflows to function dynamically rather than relying on inputs that contain static values. They can represent various types of data, including metadata, user input, step outputs, or event payloads. To simplify the process of selecting and using dynamic variables, Blink provides the [Variable Picker](#using-the-variable-picker-to-add-dynamic-variables)—a tool that allows users to insert dynamic variables without needing to understand complex expression syntax.

## Dynamic Variables Types

<div className="flow-table">
  | Dynamic Variable Type | Description |
  | - | - |
  | [Steps](/docs/workflows/building-workflows/steps) | Step-related variables include status, outputs, or results from previous workflow steps. |
  | [Local variable](/docs/workflows/building-workflows/actions/basic-actions/flow-control-actions#set-variables) | Variables that are created within the workflow using the [Set Variable action](/docs/workflows/building-workflows/actions/basic-actions/flow-control-actions#set-variables) |
  | [Files](/docs/workflows/building-workflows/files) | Variables that represent files used in the workflow, including file paths, sizes, and identifiers. |
  | [Global variables](/docs/workflows/building-workflows/dynamic-variables/global-variables) | Variables defined within a Workspace and accessible across the entire workspace. [Global variables](/docs/workflows/building-workflows/dynamic-variables/global-variables) can be *Raw value* or *Secret*. |
  | [Metadata](/docs/workflows/workflows) | Metadata variables provide workflow-related information: <ol><li>The <Tooltip tip="`automation_name`">name</Tooltip> of the current workflow</li><li>A <Tooltip tip="`automation_url`">link</Tooltip> to the current workflow</li><li> The<Tooltip tip="`automation_id`">workflow's ID</Tooltip></li><li>The associated <Tooltip tip="`workspace_id`">workspace's ID</Tooltip></li><li>The <Tooltip tip="`pack_id`">pack's ID</Tooltip> that the workflow belongs to</li><li>The <Tooltip tip="`execution_id`">current execution ID</Tooltip></li><li> A <Tooltip tip="`execution_url`">link</Tooltip> to the current execution</li><li>The <Tooltip tip="`start_time`">timer</Tooltip> at which execution began</li><li>The <Tooltip tip="`user_email`">email</Tooltip> of the user who started the execution </li><li><Tooltip tip="`user_groups`">Groups</Tooltip> the current user is a member of</li></ol> |
  | [Input Parameters](/docs/workflows/building-workflows/triggers/on-demand-triggers/input-parameters)- Only available in [On-demand workflows](/docs/workflows/building-workflows/triggers/on-demand-triggers/on-demand-triggers) | These are values defined when triggering an [On-demand workflow](/docs/workflows/building-workflows/triggers/on-demand-triggers/on-demand-triggers). |
  | [Event payload](/docs/workflows/building-workflows/triggers/event-based-triggers/webhooks)- Only available in [Event-based workflows](/docs/workflows/building-workflows/triggers/event-based-triggers/event-based-triggers) | This refers to the data received from the triggering event in an [Event-based workflows](/docs/workflows/building-workflows/triggers/event-based-triggers/event-based-triggers). When an event occurs, it generates specific data that is passed into the workflow, enabling it to execute the necessary actions based on the event's details. |
</div>

## Adding Dynamic Variables in Workflows

There are two distinct ways in which you can add dynamic variables to input parameters throughout Workflows.

<CardGroup col={2}>
  <Card title="The Variable Picker" href="/docs/workflows/building-workflows/dynamic-variables/variable-picker#using-the-variable-picker-to-add-dynamic-variables" icon="plus">
    The Variable Picker allows users to insert dynamic variables easily into workflows without manually writing expressions. It is compatible with all input types.
  </Card>

  <Card title="Blinks Expression Language" href="/docs/workflows/building-workflows/dynamic-variables/expression-language/workflow-engine-variables" icon="brackets-curly">
    The Dynamic Variables can also be added manually using the [expression language ](/docs/workflows/building-workflows/dynamic-variables/expression-language/workflow-engine-variables) syntax.
  </Card>
</CardGroup>

### Using the Variable Picker to Add Dynamic Variables

<Note>**Note**: When using the same dynamic variable in multiple steps with different value types, the variable will always take the value type from the last step where it was set. The first value type will be overwritten by the second one. </Note>

<Steps>
  <Step title="Access the Variable Picker">
    Click the <Icon icon="plus" color="#000000" /> button in the parameter field
    where you want to use a variable.
  </Step>

  <Step title="Search for a Specific Variable">
    In the Variable Picker, type to search for a specific variable.
  </Step>

  <Step title="Select the Desired Variable">
    Select the desired variable. It appears in the picker’s headline.
  </Step>

  <Step title="View the Variable Tag in the Step Field">
    The variable tag is displayed in the step's input field.
  </Step>

  <Step title="Workflow Executes and Replaces the Tag">
    When executed, the workflow replaces the tag with the actual value.

    <Frame>
      <video controls autoPlay muted zoom loop allowFullScreen className="w-full aspect-video" src="https://www.dropbox.com/scl/fi/nyr6iuih7f7eev94kdeez/UpdatingDynamicVar.mp4?rlkey=ig2uljy479uyy1b4a1k52f9pd&st=zshrtcfx&dl&raw=1" />
    </Frame>
  </Step>
</Steps>

***

## Preview the Values of Dynamic Variables in Steps

<Steps>
  <Step>
    To quickly inspect a step, click the <Icon icon="eye" /> icon. This opens a view showing all input parameters for that step.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/LmvHav-_uM6LAZXY/img/Automations/PreviewModeIcon.png?fit=max&auto=format&n=LmvHav-_uM6LAZXY&q=85&s=9f7455760088ea71e5cd0988960ac2b0" width="1728" height="1078" data-path="img/Automations/PreviewModeIcon.png" />
    </Frame>
  </Step>

  <Step>
    In preview mode, you can see the actual values of all dynamic variables used in the step’s input parameters

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/LmvHav-_uM6LAZXY/img/Automations/PreviewMode.png?fit=max&auto=format&n=LmvHav-_uM6LAZXY&q=85&s=44508f966cf6c2bb755f02d9f805f638" width="1728" height="1078" data-path="img/Automations/PreviewMode.png" />
    </Frame>

    You can view dynamic variables alongside their actual values by clicking the <Icon icon="expand" /> icon in the top-right corner of the text input to enlarge the preview. Then, select the <Icon icon="eye" /> icon to display both the dynamic variables and their corresponding values side by side.
    From the panel on the left of the expanded preview, you can directly edit the dynamic variables. Any changes you make will instantly update on the right side, allowing you to see in real time how adjustments affect the final output.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/s7QlpiBlLa84CUZO/img/Automations/PreviewModeEnlarged.png?fit=max&auto=format&n=s7QlpiBlLa84CUZO&q=85&s=7d603cfc32d957345c899b9fd1b4d22d" width="3456" height="2154" data-path="img/Automations/PreviewModeEnlarged.png" />
    </Frame>
  </Step>
</Steps>

## <Warning>In preview mode, dynamic variables in the [python action](/docs/workflows/building-workflows/dynamic-variables/expression-language/workflow-engine-variables#python-actions) cannot be displayed. You can view input values from other scripting languages ([Bash](/docs/workflows/building-workflows/actions/basic-actions/code-actions#run-bash-script), [PowerShell](/docs/integrations/powershell), and [Node.js](/docs/workflows/building-workflows/actions/basic-actions/code-actions#run-node-js-script)), but Python- generated dynamic values are not available to preview.</Warning>

## Referencing a Key in a JSON Object

If a workflow step outputs a JSON object, you can reference a specific key:

<Steps>
  <Step>Click the desired key in the JSON output.</Step>
  <Step>The value copies to your clipboard.</Step>

  <Step>
    Paste the value into another step where needed.
  </Step>
</Steps>

<Frame>
  <video controls autoPlay muted zoom loop allowFullScreen className="w-full aspect-video" src="https://www.dropbox.com/scl/fi/z3ubsqu9siu7dxqrw4a57/JSONDotWalking.mp4?rlkey=kfgeahtmkh4pgczj8ihwaj3y6&st=i5igsuiu&raw=1" />
</Frame>

### Using Expression Language with Dynamic Variables

The Dynamic Variables can also be added manually using [expression language](/docs/workflows/building-workflows/dynamic-variables/expression-language/workflow-engine-variables) syntax.

1. To see the supported syntax to manually add a Dynamic Variable to a workflow input, click [here](/docs/workflows/building-workflows/dynamic-variables/expression-language/workflow-engine-variables)
2. Functions can be added to Dynamic Variables or Static Variables. To see the supported syntax of adding *Functions* to Dynamic Variable, click [here](/docs/workflows/building-workflows/dynamic-variables/expression-language/workflow-engine-functions)
3. Operators can be added to Dynamic Variables or Static Variables. To see the supported syntax of adding *Operators* to Dynamic Variables, click [here](/docs/workflows/building-workflows/dynamic-variables/expression-language/workflow-engine-operators)

## Recommendations and Limitations

* Avoid reusing the same dynamic variable in multiple steps with different value types; the last assigned type takes precedence.
* Ensure the workflow is correctly structured to prevent missing values in dynamic variables.

## Related Articles

<CardGroup cols={2}>
  <Card title="Global Variables" icon="globe" href="/docs/workflows/building-workflows/dynamic-variables/global-variables">
    Configure triggers to start workflows based on events.
  </Card>

  <Card title="Expression Language" icon="brackets-curly" href="/docs/workflows/building-workflows/dynamic-variables/expression-language/workflow-engine-variables">
    Define and organize actions within a workflow.
  </Card>

  <Card title="Workflow Engine Functions" icon="brackets-curly" href="/docs/workflows/building-workflows/dynamic-variables/expression-language/workflow-engine-functions">
    Add logic to control workflow execution paths.
  </Card>

  <Card title="Workflow Engine Operators" icon="plus" href="/docs/workflows/building-workflows/dynamic-variables/expression-language/workflow-engine-operators">
    Build a new workflow from scratch in Blink.
  </Card>
</CardGroup>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.