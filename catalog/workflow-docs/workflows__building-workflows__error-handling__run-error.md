> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Run Workflow on Workflow Failure

> Create event-based workflows that trigger automatically when another workflow fails in Blink.

## Creating an Event-Based Workflow using the Blink Error Event

When a workflow fails, it is possible to execute another workflow to handle the failure. The workflow that handles the failure is an Event-Based Workflow that is triggered by a Blink Error. The purpose of this **trigger** is to execute a workflow in case another workflow encounters an error. The payload of the error event is the error returned from the step that failed the workflow execution.

<iframe src="https://demo.arcade.software/JV20qeTs2EyzJTnGg04o?embed&show_copy_link=true" title="Creating an Event-Based Automation using a Blink Error Event" frameborder="0" loading="lazy" webkitAllowFullScreen mozAllowFullScreen allowFullScreen allow="clipboard-write" className="iframe-webhook" width="100%" height="420" />

<Steps>
  <Step>
    Select the **Event-Based** Workflow option type.
  </Step>

  <Step>
    Select **Blink Error Event** and then select the "Continue". The **Blink Error Event** setup is displayed.
  </Step>

  <Step>
    Next, create the steps to handle the error to suit your needs.

    <Tip>You can use the **Blink Error Event** payload in the workflow steps, to reference data related to the error that occurred.</Tip>
  </Step>

  <Step>
    After finalizing your workflow, proceed by selecting the "Publish and Activate" button in the top-right corner, then return to your workspace.
  </Step>

  <Step>
    Select a published workflow you would like to add the **Blink Error Event** to.
  </Step>

  <Step>
    You will be navigated to the chosen [Workflow Overview](/docs/workflows/managing-workflows/workflow-overview-page) page.
  </Step>

  <Step>
    Under the **Run workflow on error** section, use the dropdown menu to select a previously created **Blink Error Event** workflow as the error handler. When an error occurs during execution of the selected workflow, the chosen **Blink Error Event** workflow will be triggered automatically to handle it.

    1. **Default** – Triggers the error-handling workflow configured as the default in your [workspace settings](/docs/blink-platform/workspaces/managing-your-workspace#workflows-default-error-handler).

    2. **Custom** – Allows you to select a specific error-handling workflow for the selected workflow, overriding the default error-handling workflow configured in your [workspace settings](/docs/blink-platform/workspaces/managing-your-workspace#workflows-default-error-handler).

    <Note>The dropdown can be left empty, meaning no error-handling logic will be applied to the selected workflow.</Note>
  </Step>

  <Step>
    Finish by, clicking the "X" button in the top-right corner to apply the changes.
  </Step>
</Steps>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.