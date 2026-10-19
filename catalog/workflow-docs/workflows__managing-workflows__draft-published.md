> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Controlling the Availability of a Published Workflow

> Understand the draft and published workflow states and how to manage workflow lifecycle in Blink.

## Published Workflows

* A published Workflow is the version that appears in your Workflow Pack and in the [Self-service portal](/docs/blink-platform/blink-portal/blink-portal). If it is active it will respond to preset triggers.
* By default, all [On-Demand](/docs/workflows/building-workflows/triggers/on-demand-triggers) Workflows are exposed as [Subflows](/docs/workflows/building-workflows/actions/basic-actions/subflow-actions) in the self-service portal. This function allows you to quickly and easily re-use a previously exposed Workflow while creating a new one.

## Controlling the Availability of a Published Workflow

The Active/Inactive toggle, which appears in the [Workflow Overview](/docs/workflows/managing-workflows/workflow-overview-page) page of your selected Workflow, controls the availability of a published Workflow. The toggle is only enabled for published Workflows. Unpublished Workflows show the Active/Inactive toggle button is disabled and set to *Inactive*.

**When Set to Active:**

* Publishing an active Workflow will not change the current state of the Workflow. The publish button shows **Publish**.

**When Set to Inactive:**

* Workflows cannot be executed by CLI, API, or a Trigger (On-Demand, Event-Based, or Scheduled).
* Self-service toggle in overview tab will be disabled.
* The Workflow will be removed from self-service portal.
* The **Run Workflow** button in the overview tab is shown, but disabled. Hovering over it will show this tooltip: *Workflow is Inactive and cannot be executed*.
* Workflow currently running will not be stopped.
* Workflow can still be executed from the edit screen.
* The **Publish** button in the edit mode is **Publish & Activate**. Publishing an Inactive Workflow automatically activates the Workflow.
* Attempts to run an inactive Workflow from the API returns *Workflow is Inactive and cannot be executed*.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.