> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Workflow Run Logs

> Use workflow run logs to debug execution issues and inspect step-level inputs and outputs in Blink.

<Note>The **Run Log** displays executions from the last `30` days.</Note>

The "Run Log" provides a detailed record of every execution of a selected workflow. It allows you to review past runs, verify whether each step was successful, and troubleshoot errors when they occur. By capturing both test runs and active runs, the run log ensures full visibility into workflow performance over time. This makes it an essential tool for monitoring reliability, validating changes, and maintaining a clear audit trail of automation activity.

## Run Log Panel

<Frame>
  <img src="https://mintcdn.com/blinkops-2/L42GziBE86iOLtcJ/img/Automations/ExecutionsLogs.png?fit=max&auto=format&n=L42GziBE86iOLtcJ&q=85&s=eeef158cd0c6abf5ebcadf36a1b6d5ba" width="1727" height="1078" data-path="img/Automations/ExecutionsLogs.png" />
</Frame>

<div className="integrations-table">
  | | Title | Description |
  | - | - | - |
  | **1** | <p>[Filter](#filtering-run-logs) - <Icon icon="bars-filter" /> </p> | Allows you to display or hide the **test run logs** in the run log panel. |
  | **2** | **Active Run Log** | Represents a run log entry of the selected workflow's execution history. Displays the run number, timestamp, and the user who initiated the run. |
  | **3** | **Test Run Log** | Identifies the selected workflow's executions that were triggered in **Test Mode**. These are marked with a "TEST" label for quick visibility. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/L42GziBE86iOLtcJ/img/Automations/RunLogs.png?fit=max&auto=format&n=L42GziBE86iOLtcJ&q=85&s=8d3086708afdb62e38ca24e04d9beab8" width="1728" height="1080" data-path="img/Automations/RunLogs.png" />
</Frame>

***

## Filtering Run Logs

<p>In the run log panel on the left, click the <Icon icon="bars-filter" /> icon to filter run logs. You can filter logs based on the following categories:</p>

* **Show test runs** – Displays all workflows executed as test runs.
* **Triggered as a subflow** – Shows workflows that were triggered as part of another workflow.
* **Completed** – Lists workflows that finished successfully without errors.
* **Failed** – Shows workflows that encountered errors and did not complete.
* **Cancelled** – Displays workflows that were manually or automatically cancelled during execution.
* **Pending** – Lists workflows that are waiting to start execution.
* **Running** – Shows workflows that are currently in progress.
* **Timeout** – Displays workflows where one or more steps exceeded their allowed execution time.
* **Timeframe** – Filters workflows based on a selected time range:
  * **All** – Shows all workflow runs (default).
  * **Last Hour** – Shows workflows executed within the past hour.
  * **Last 24 Hours** – Shows workflows executed within the past day.
  * **Last 7 Days** – Shows workflows executed within the past week.
  * **Last 30 Days** – Shows workflows executed within the past 30 days.
  * **Custom** – Allows you to define your own timeframe for workflow filtering.

<Frame>
  <img src="https://mintcdn.com/blinkops-2/s5mCUVOu-GPF1GFO/img/Automations/FilteringRunLogs.png?fit=max&auto=format&n=s5mCUVOu-GPF1GFO&q=85&s=57b93865b37608668c31342b62f32971" width="1728" height="1079" data-path="img/Automations/FilteringRunLogs.png" />
</Frame>

***

## Additional Information about the Execution

<div className="integrations-table">
  | | Title | Description |
  | - | - | - |
  | **4** | **Execution Status** | Indicates the status of selected run log. To see all statuses, navigate to this [section](#viewing-automated-workflow-outputs) |
  | **5** | **Run Number** | The unique run identifier in the workflow’s execution history (e.g., *Run 4*). |
  | **6** | **Execution Timestamp** | Displays the exact date and time when the workflow was executed. |
  | **7** | **Executed By** | The user who initiated the workflow run, shown with their email address or the trigger that initiated the workflow run. |
  | **8** | **[Runner](/docs/blink-platform/runners/runners)** | Identifies the runner (e.g., **Blink Cloud**) used to execute the workflow. |
  | **9** | **Execution Duration** | Shows the total runtime taken to complete the workflow (e.g., *15s 556ms*). |
  | **10** | **Summary of the Workflow's Execution Status** | Displays the total number of time the workflow executed successfully vs. failed. |
  | **11** | **The Selected Workflow** | The selected workflow, including step name, type, run duration, and execution status. |
</div>

<Tip>When a workflow contains a [subflow](/docs/workflows/building-workflows/actions/basic-actions/subflow-actions), it will display information about the [subflow](/docs/workflows/building-workflows/actions/basic-actions/subflow-actions) alongside the parent workflow’s details. </Tip>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/yZJnWm6iaLXvyxN7/img/Automations/SubflowRunLog.png?fit=max&auto=format&n=yZJnWm6iaLXvyxN7&q=85&s=09fdf2f18c5c96af2b154a0a4980944b" width="1725" height="1079" data-path="img/Automations/SubflowRunLog.png" />
</Frame>

***

## Viewing Automated Workflow Outputs

View past executions in the *Execution History* tab. The left-hand side of the screen lists a history of executions and their status. The status can be one of the following:

<div className="flow-table">
  | Status | Icon | Description |
  | - | - | - |
  | Completed | <img src="https://mintcdn.com/blinkops-2/LJULXRaq3qGa0sq0/img/Automations/ExecutionsCheck.svg?fit=max&auto=format&n=LJULXRaq3qGa0sq0&q=85&s=7c70261b7b6b3430268281f4938c6403" width="20" height="20" data-path="img/Automations/ExecutionsCheck.svg" /> | The workflow executed successfully without any errors. |
  | Stopped | <img src="https://mintcdn.com/blinkops-2/LJULXRaq3qGa0sq0/img/Automations/ExecutionPaused.svg?fit=max&auto=format&n=LJULXRaq3qGa0sq0&q=85&s=3bcb445781ee0813f6137d069ced73ec" width="20" height="20" data-path="img/Automations/ExecutionPaused.svg" /> | The workflow has been stopped by the creator. |
  | In progress | <img src="https://mintcdn.com/blinkops-2/LJULXRaq3qGa0sq0/img/Automations/ExecutionsPending.svg?fit=max&auto=format&n=LJULXRaq3qGa0sq0&q=85&s=85692132aeecb36fed20e52edc4a783a" width="16" height="16" data-path="img/Automations/ExecutionsPending.svg" /> | The workflow is in the process of running. |
  | Pending | <img src="https://mintcdn.com/blinkops-2/LJULXRaq3qGa0sq0/img/Automations/ExecutionsInProgress.svg?fit=max&auto=format&n=LJULXRaq3qGa0sq0&q=85&s=f3508b190e7385f2f545f121a5fdc0eb" width="20" height="20" data-path="img/Automations/ExecutionsInProgress.svg" /> | A step in the workflow is waiting for approval or an external response. |
  | Failed | <img src="https://mintcdn.com/blinkops-2/LJULXRaq3qGa0sq0/img/Automations/ExecutionFailed.svg?fit=max&auto=format&n=LJULXRaq3qGa0sq0&q=85&s=dbc80ef2cbb8e7529f9ac51840da3cdd" width="20" height="20" data-path="img/Automations/ExecutionFailed.svg" /> | The workflow failed to execute successfully. |
  | Timed out | <img src="https://mintcdn.com/blinkops-2/LJULXRaq3qGa0sq0/img/Automations/ExecutionTimedOut.svg?fit=max&auto=format&n=LJULXRaq3qGa0sq0&q=85&s=5e39d01ba949e5a411c9611195f9776b" width="20" height="20" data-path="img/Automations/ExecutionTimedOut.svg" /> | A step in the workflow has timed out. |
</div>

***

## Settings

In the top right corner, you can click on the <Icon icon="square-ellipsis-vertical" iconType="solid" /> icon,  to access the options in the dropdown menu:

1. [Edit Yaml](/docs/workflows/building-workflows/workflow-yaml)- Make any changes to the workflow's *"YAML*" format

2. [Download Yaml](/docs/workflows/building-workflows/workflow-yaml)- download the workflow's *"YAML"* to your desktop as a `.yaml` file

3. "Settings" to view and edit details of the selected Workflow

4. [Version History](/docs/workflows/managing-workflows/workflow-version-history) to access various version histories for the selected workflow.

<Frame>
  <img src="https://mintcdn.com/blinkops-2/L42GziBE86iOLtcJ/img/Automations/RunLogSettings.png?fit=max&auto=format&n=L42GziBE86iOLtcJ&q=85&s=2e734a16317a162d2b74c20e8a9b84b5" width="1720" height="1075" data-path="img/Automations/RunLogSettings.png" />
</Frame>

***

## Re-run Previous Inputs of a Workflow's Execution

The "Rerun with published version" feature enables you to execute the current published version of a selected Workflow using the input parameter's values from a previous execution.

<Note>Please note, the "Rerun with published version" feature is only applicable for [Event-Based Workflows](/docs/workflows/building-workflows/triggers/event-based-triggers/event-based-triggers) and [On-Demand Workflows](/docs/workflows/building-workflows/triggers/on-demand-triggers/on-demand-triggers).</Note>

<Steps>
  <Step title="Access the Run Logs">
    In the Workflow Editor, navigate to the *"Run Log*" tab to access the selected workflow's run logs.
  </Step>

  <Step title="Choose an Execution to Re-Run*">
    <p>In the left-hand sidebar, select the <Icon icon="square-ellipsis-vertical" iconType="solid" /> icon of the execution you want to re-run with its input parameter values. Then click the "Rerun with published version" button. </p>

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/zt4LRY_YQzqawmcY/img/Automations/AllowRerun.png?fit=max&auto=format&n=zt4LRY_YQzqawmcY&q=85&s=3ba35d91c01443b1e3fe49d64c67be12" width="1727" height="1083" data-path="img/Automations/AllowRerun.png" />
    </Frame>
  </Step>

  <Step title="Confirm Input Parameters">
    A pop-up window will appear, showing all the input values from the selected run. If the published version has any new input parameters, they will also be displayed and you will need to fill them in.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/L42GziBE86iOLtcJ/img/Automations/RerunWorkflow.png?fit=max&auto=format&n=L42GziBE86iOLtcJ&q=85&s=716d52aff36bde07042a1e69c722c3d3" width="3446" height="2124" data-path="img/Automations/RerunWorkflow.png" />
    </Frame>
  </Step>
</Steps>

***

## Viewing the Event Payload of Event-Based Automated Workflow

See the *payload* that triggered a certain event.

<Note>**Please note** that this is relevant for [event-based workflows](/docs/workflows/building-workflows/triggers/event-based-triggers/event-based-triggers) triggered by [webhooks](/docs/workflows/building-workflows/triggers/event-based-triggers/webhooks), polling and pre-defined events.</Note>

<Steps>
  <Step title="Access the Run Logs">
    In the Workflow Editor, navigate to the *"Run Log*" tab to access the selected workflow's run logs.
  </Step>

  <Step title="View and Reuse Event Payloads">
    To view the event payload of an event-based workflow, click **View Event** next to the **Trigger**. An **Event** dialog box will open, allowing you to review or copy the event for use in creating another workflow.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/yZJnWm6iaLXvyxN7/img/Automations/ViewEvent.png?fit=max&auto=format&n=yZJnWm6iaLXvyxN7&q=85&s=5f3f7d6f7015dd2fb36cca2436d827f8" width="1728" height="1083" data-path="img/Automations/ViewEvent.png" />
    </Frame>
  </Step>
</Steps>

### Interactive Tutorial Guide:

You can also refer to the following tutorial guides for a more in-depth understanding of how to use the Workflow Editor and Workflow Run Logs

<iframe src="https://demo.arcade.software/YXmhHJOT6K9R27JFNiBg?embed&show_copy_link=true" title="Editor and Run Logs" frameborder="0" loading="lazy" webkitAllowFullScreen mozAllowFullScreen allowFullScreen allow="clipboard-write" className="iframe-webhook" width="100%" height="420" />


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.