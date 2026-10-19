> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Workflows Runtime Limitations

> System limits for Blink workflows, including execution queues, timeouts, and resource constraints.

<Note>**Note**: These limitations apply only at the workflow level and do not extend to the tenant or workspace level</Note>

## Workflows and Workflow Executions

<div className="flow-table">
  | Feature | Description | Limit Value | Notes |
  | - | - | - | - |
  | Webhook Payload | Maximum supported payload size for webhook triggers. | `application/json`: **20 MB**<br />`application/x-www-form-urlencoded`: **10 MB** | Requests that exceed the applicable payload limit are rejected, and the workflow will not run. |
  | A Workflow's Output | Maximum output size of a workflow | `20MB` | |
  | Workflow Execution Time | Maximum duration for a workflow to run. | `12 hours` (default: `2 hours`) | Visit the [More In-Depth Explanation of Time Limitations](/docs/workflows/system-limits#more-in-depth-explanation-of-timeout-limitations) section, for a more detailed explanation. |
  | Execution History | Maximum number of entries stored in a workflow's execution history from the past `30` days. | `100` in the past `30` days | Contact [support](mailto:support@blinkops.com) if you need to increase the number of history entries. |
</div>

## Execution Queue

Each execution first enters the execution queue. If capacity is available, it runs immediately; otherwise, it waits in the queue until capacity becomes available.

Execution queue limits are defined at two levels:

1. The **workspace level**, which controls concurrency of workflows in individual workspaces.
2. The **tenant level**, which governs overall activity across all workspaces within the tenant.

<div className="flow-table">
  | Feature | Description | Limit Value | Notes |
  | - | - | - | - |
  | Execution Queue **(Workspace)** | The maximum number of workflows that can run concurrently within a specific workspace. | `40` | Additional workflows beyond this limit are placed in a queue and will run as capacity becomes available. While this may introduce a brief delay, all queued executions will still be processed. Visit this [section](/docs/workflows/running-workflows/running-workflows), for a more detailed explanation. |
  | Execution Queue **(Tenant)** | The maximum number of workflows that can run concurrently across all workspaces under the tenant. | `50` | The limit is shared across all workspaces in the tenant. When multiple workflows are queued across different workspaces in the tenant, Blink cycles through the workspaces in turn, giving each one a fair opportunity to run its next batch of workflow. This helps ensure balanced resource usage across the entire tenant. Visit this [section](/docs/workflows/running-workflows/running-workflows), for a more detailed explanation. |
</div>

<Accordion title="Execution Queue Exceptions" icon="square-exclamation">
  * [On-demand workflows](/docs/workflows/building-workflows/triggers/on-demand-triggers/on-demand-triggers) bypass the queue.

  * Workflows that include any [Interactive Actions](/docs/workflows/building-workflows/actions/advanced-actions/interactive-actions/interactive-actions), [Web Forms](/docs/blink-platform/web-form/web-form), or the [Wait action](/docs/workflows/building-workflows/actions/basic-actions/flow-control-actions#wait) with a timeout greater than `60` seconds are not immediately added to the execution queue.
    Instead, they are placed in a pending state while waiting for input or a response from an external user. These pending workflows do not count toward the execution concurrency limit. Once a response is received, if the execution queue has available capacity, the workflow will proceed to execute immediately. If the queue is full at that moment, the workflow will enter the queue and wait its turn to execute.

  * For workflows configured to run in series, every single execution enters the main execution queue immediately upon creation. Once in the main queue, executions are then placed in a dedicated serial workflow queue, where they wait their turn to run in order
</Accordion>

***

## Steps

<div className="flow-table">
  | Limit Description | Limit Value | Notes |
  | - | - | - |
  | Maximum total output size across all step outputs (results) in a workflow | `20MB` | This is the combined limit for all steps in the workflow, not per individual step. For larger outputs, save the result to a file using the [step configuration](/docs/workflows/building-workflows/steps#step-settings). |
  | Maximum number of completed steps in a workflow | `5000` | |
  | The maximum duration, in seconds, between each step retry | `60 seconds` | |
  | Default timeout for a step | `1 minute` | Visit the [More In-Depth Explanation of Time Limitations](/docs/workflows/system-limits#more-in-depth-explanation-of-timeout-limitations) section, for a more detailed explanation. |
  | Maximum number of [HTTP Steps](https://docs.blinkops.com/docs/workflows/building-workflows/actions/basic-actions/http-actions) per minute | `1200` | Applies to [Blink Cloud Runners](/docs/blink-platform/runners/runners) only. |
  | The Maximum time a step can run for | `2 hours`-`12 hours` | Visit the [More In-Depth Explanation of Time Limitations](/docs/workflows/system-limits#more-in-depth-explanation-of-timeout-limitations) section, for a more detailed explanation. |
</div>

### More In-Depth Explanation of Timeout Limitations

Timeouts can be defined at two levels: [Step](#step-level-timeout) and [Workflow](#workflow-level-timeout)

<AccordionGroup>
  <Accordion title="Step-Level Timeout" icon="alarm-exclamation">
    <Note>**Note**: Each step can run between `2` and `12` hours. If needed, a step can stay paused for up to `14` days. Internal steps (like, the [Print action](/docs/workflows/building-workflows/actions/utility-actions/miscellaneous-utilities#print), the [Flow control actions](/docs/workflows/building-workflows/actions/basic-actions/flow-control-actions) and certain [Utility actions](/docs/workflows/building-workflows/actions/utility-actions/array-utilities)) follow the main execution timeout, while external steps (like [HTTP actions](/docs/workflows/building-workflows/actions/basic-actions/authentication), [Python actions](/docs/workflows/building-workflows/actions/basic-actions/code-actions#run-python), or [Bash actions](/docs/workflows/building-workflows/actions/basic-actions/code-actions#run-bash-script)) default to `60` seconds but can be set anywhere from `1` second up to the overall execution timeout.</Note>

    Defines the maximum time a step can run before it must complete.

    * **configuration:** The step timeout is adjustable in the step settings, with a default of `60 seconds`.<Note>**Note**: Each step can run between `2` and `12` hours. If needed, a step can stay paused for up to `14` days. Internal steps (like, the [Print action](/docs/workflows/building-workflows/actions/utility-actions/miscellaneous-utilities#print), the [Flow control actions](/docs/workflows/building-workflows/actions/basic-actions/flow-control-actions) and certain [Utility actions](/docs/workflows/building-workflows/actions/utility-actions/array-utilities)) follow the main execution timeout, while external steps (like [HTTP actions](/docs/workflows/building-workflows/actions/basic-actions/authentication), [Python actions](/docs/workflows/building-workflows/actions/basic-actions/code-actions#run-python), or [Bash actions](/docs/workflows/building-workflows/actions/basic-actions/code-actions#run-bash-script)) default to `60` seconds but can be set anywhere from `1` second up to the overall execution timeout. For more information, visit the [workflow limitation documentation](/docs/workflows/system-limits#more-in-depth-explanation-of-timeout-limitations)</Note>

    * **What happens when time runs out?**

      * If a step exceeds its allowed time, it will fail resulting in the entire workflow to fail, unless ['continue on error'](/docs/workflows/building-workflows/error-handling/run-error) is enabled.

    <Accordion icon="circle-exclamation" title="Exceptions- Interactive Actions and the Wait Action">
      The [Wait Action](/docs/workflows/building-workflows/actions/basic-actions/flow-control-actions#wait-for-time-interval) and [Interactive Actions](/docs/workflows/building-workflows/actions/advanced-actions/interactive-actions/interactive-actions) pause the workflow while awaiting user response, placing it in a pending state.

      * These steps can remain paused for up to `14 days`.

      * If the timeout is reached, the step is automatically completed, and the workflow continues without failure.

      **Example**

      A workflow has a `2-hour` timeout.

      * It runs for `1 hour`, then pauses at step with an [Interactive Action](/docs/workflows/building-workflows/actions/advanced-actions/interactive-actions/interactive-actions).

      * The step containing the [Interactive Action](/docs/workflows/building-workflows/actions/advanced-actions/interactive-actions/interactive-actions) remains paused for `3 hours`.

      * Once the user responds, the workflow resumes and completes execution.

      * The total execution time is recorded as `1 hour` (excluding the `3-hour` pause), meaning the workflow does not time out.
    </Accordion>
  </Accordion>

  <Accordion title="Workflow-Level Timeout" icon="alarm-exclamation">
    Specifies the maximum duration a workflow can run before it is terminated.

    * **configuration**: Set in workflow settings under 'Execution Timeout (in hours)' field.
      * The default timeout is `2 hours`.
      * The maximum limit is `12 hours`.

    * **What happens when time runs out?**
      1. If a workflow exceeds its configured execution time, it will fail with a timeout status.

      2. Any steps that have not yet started will remain in a 'not started' state.

      3. If a workflow times out while a step is still running, that step will **not** be cancelled. It will continue to run to completion or failure, even after the overall workflow has timed out.
  </Accordion>
</AccordionGroup>

***

## Actions

<div className="flow-table">
  | Feature | Limit Description | Limit Value | Notes |
  | - | - | - | - |
  | [Global Variables](/docs/workflows/building-workflows/dynamic-variables/global-variables) | Maximum size of a Global Variable | `1MB` | |
  | [Set Variable Flow Control Action](/docs/workflows/building-workflows/actions/basic-actions/flow-control-actions#set-variables) | Maximum size for a value in the Set Variable action | `20MB` | |
  | [Wait Flow Control Action](/docs/workflows/building-workflows/actions/basic-actions/flow-control-actions#wait-for-time-interval) | Maximum timeout duration for the Wait action | `14 Days` | A workflow may wait in a pending state (paused) for a total of up to 30 days. If it has not completed within 30 days from its start date, it will be terminated automatically. |
  | [Interactive Actions](/docs/workflows/building-workflows/actions/advanced-actions/interactive-actions/interactive-actions) | Maximum timeout for Interactive Actions | `14 Days` | <ul><li>A workflow may wait in a pending state (paused) for a total of up to 30 days. If it has not completed within 30 days from its start date, it will be terminated automatically.</li><li>Visit the [Exceptions- Interactive Actions and the Wait Action](#exceptions-interactive-actions-and-the-wait-action) under [More In-Depth Explanation of Timeout Limitations](#more-in-depth-explanation-of-timeout-limitations) section, for a more detailed breakdown.</li></ul> |
  | [Wait For Web Form Response Action](/docs/blink-platform/web-form/web-form-actions) | Maximum timeout for Web Form Response action | `14 Days` | <ul><li>A workflow may wait in a pending state (paused) for a total of up to 30 days. If it has not completed within 30 days from its start date, it will be terminated automatically. </li><li> Visit the [Exceptions- Interactive Actions and the Wait Action](#exceptions-interactive-actions-and-the-wait-action) under [More In-Depth Explanation of Timeout Limitations](#step-level-timeout), for a more detailed breakdown. </li></ul> |
  | [Synchronous Subflows](/docs/workflows/building-workflows/actions/basic-actions/subflow-actions) | Timeout for Synchronous Subflows | Limited by parent workflow timeout | A synchronous subflow must finish within the parent workflow’s timeout (e.g., 10 min for a 10-minute parent workflow). |
  | [Webhooks](/docs/workflows/building-workflows/triggers/event-based-triggers/webhooks) | Maximum number of executions per minute per workflow | `1800` | |
  | Polling Interval | Minimum time between each poll | `1 min` | Default is set to `5 min` |
  | [Scheduled Triggers](/docs/workflows/building-workflows/triggers/scheduled-triggers) | Minimum time frequency for scheduled workflows | `1 min` | Default is set to `5 min` |
</div>

***

## Files

<div className="flow-table">
  | Limit Description | Limit Value | Notes |
  | - | - | - |
  | Maximum file size for a single step | `500MB` | Does not apply if using your own [Object Storage](/docs/blink-platform/runners/object-storage/s3-object-storage). |
  | Maximum total file size across all steps in a workflow | `1500MB` | Does not apply if using your own [Object Storage](/docs/blink-platform/runners/object-storage/s3-object-storage). |
  | Maximum number of files that can be created in one workflow execution | `100` | |
</div>

***


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.