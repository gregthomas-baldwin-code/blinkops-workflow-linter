> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using On-Demand Triggers

> Learn how to build on-demand workflows to execute from the Self Service Portal.

<Card title="How this Helps" icon="lightbulb">
  On-demand workflows are useful for running tasks that need to be executed immediately or at the user's discretion. They provide flexibility and control over when specific workflows are triggered, making them ideal for scenarios where timing is critical or user input is required.
</Card>

An on-demand workflow runs when triggered via one of the following avenues:

<div className="integrations-table">
  | Interface | Description |
  | - | - |
  | **Manual Trigger** | Users with access to the Blink platform can also trigger workflows manually. |
  | **Blink Portal** | Allows authorized users to trigger workflows through a dedicated UI. |
  | **Slack & Microsoft Teams** | Enables workflow execution directly from messaging platforms. |
  | **Subflows** | Workflows that can be used when triggered by a parent workflow, typically useful when the subflow is an action that is needed by more than one parent workflow. |
</div>

When relevant, the user who triggers the workflow enters the required parameters.

<Note>
  The *file* [input parameter](/docs/workflows/building-workflows/triggers/on-demand-triggers/input-parameters) is not supported in triggered [subflows](/docs/workflows/building-workflows/actions/basic-actions/subflow-actions).
</Note>

<Note>
  Need help finding the right trigger type for your use case? See [About Triggers](/docs/workflows/building-workflows/triggers/triggers).
</Note>

## Create an On-Demand Workflow

1. [Create a new workflow](/docs/workflows/creating-a-workflow), and select **On-Demand** when prompted.

   <Frame>
     <img src="https://mintcdn.com/blinkops-2/xnKigMZdVI45SQhn/img/Automations/OnDemandAdvanced.gif?s=a406d5d6434e3b390d8316910a71aa85" width="1944" height="1080" data-path="img/Automations/OnDemandAdvanced.gif" />
   </Frame>

   Once you click **Create Workflow**, the canvas loads with your initial configurations. The first part of the workflow appears as **Trigger: On-Demand**.

2. In the **Workflow Editor**, locate the **Trigger: On-Demand** section and click **+** to configure <Tooltip text="Input parameters">[the parameters that the user should define](/docs/workflows/building-workflows/triggers/on-demand-triggers/input-parameters)</Tooltip> when triggering the workflow.

   <iframe src="https://demo.arcade.software/dfVhPko1FabyZK3VUeW5?embed&show_copy_link=true" title="Create your First Table" frameborder="0" loading="lazy" webkitAllowFullScreen mozAllowFullScreen allowFullScreen allow="clipboard-write" className="iframe-webhook" width="100%" height="420" />

3. Enter a memorable name for the trigger and enter the type. *Optionally*, mark the **Required parameter** checkbox.

   <Frame>
     <img src="https://mintcdn.com/blinkops-2/xnKigMZdVI45SQhn/img/Automations/EnterInputParams.gif?s=3521cc80e1c4b3ad0897a506cac48ed0" width="1944" height="1080" data-path="img/Automations/EnterInputParams.gif" />
   </Frame>

4. To customize how the input appears in the form, click **Configure how this parameter appears** in the input form and modify the:

   * **Display Name**: The label shown to users for this input parameter.
   * **Placeholder** *(available for relevant types)*: Optional sample text displayed inside the input field to guide users on the expected format (for example, a sample username or email address).
   * **Default Value**: The value automatically used if the user does not provide an input.
   * **Instructions Text**
     * **Tooltip**: Contextual text that appears on hover, offering additional explanation or clarification for the parameter.
     * **Helper Text**: Supporting text shown below the input field to guide the user on how to complete it correctly.
     * **Description**: The text shown to the user, either as a tooltip or as helper text, depending on the selected option.

   <Frame>
     <img src="https://mintcdn.com/blinkops-2/EHFuvoqhz9d_YX_e/img/Automations/AdvancedInputSettings.png?fit=max&auto=format&n=EHFuvoqhz9d_YX_e&q=85&s=c0376779595baaf228d3b318a763c268" width="1723" height="1077" data-path="img/Automations/AdvancedInputSettings.png" />
   </Frame>

5. Click **Add** to save the input parameter and close the window.

   <Frame>
     <img src="https://mintcdn.com/blinkops-2/4a8dMD2Jv5wsADYv/img/Automations/AddInputButton.gif?s=9a12157b8b69c6ba6959e127943e25b9" width="1944" height="1080" data-path="img/Automations/AddInputButton.gif" />
   </Frame>

***

## See It In Action

<iframe src="https://demo.arcade.software/bNaX7C8ogr3VD3cTk03w?embed&show_copy_link=true" title="Creating an on-demand automation" frameborder="0" loading="lazy" webkitAllowFullScreen mozAllowFullScreen allowFullScreen allow="clipboard-write" className="iframe-webhook" width="100%" height="420" />

## What Next?

Once you've finished configuring the workflow, it's time to test it. Once you're satisfied with the results, you can publish the workflow to make it available in the Self-Service Portal.

All of the steps following the trigger will run when a user activates the workflow from the **Self Service Portal** based on the parameters they enter and any other conditions you've configured.

## Related Articles

<CardGroup cols={3}>
  <Card title="Testing Workflows" icon="magnifying-glass-arrows-rotate" href="/docs/workflows/testing-workflows">
    Validate workflows to ensure they run as expected.
  </Card>

  <Card title="Managing Workflow Permissions" icon="folder-gear" href="/docs/blink-platform/account-management/roles#workspaces-role-scope">
    Control user access and execution rights.
  </Card>

  <Card title="Using Input Parameters" icon="pen-field" href="/docs/workflows/building-workflows/triggers/on-demand-triggers/input-parameters">
    Pass dynamic data into workflows with input parameters.
  </Card>
</CardGroup>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.