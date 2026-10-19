> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Monitoring Workflows Health

> Monitor workflow health and execution metrics to track performance and identify issues in Blink.

You can track, analyze, and review workflow executions in three ways:

1. From the [Executions](#past-executions) page.
2. From the [Run Log tab](/docs/workflows/debugging-workflows/workflow-run-logs) within the workflow editor.
3. Through the [activity graph](#activity-graph), which highlights failures and their causes.

You can also choose to receive email notifications if a workflow fails. For setup instructions, see [Configuring Error Notifications](/docs/workflows/monitoring-workflows-health#configuring-error-notifications).

## Monitoring Workflows Activity

## Past Executions

To view all past workflow executions and their statuses, open your Workspace, then navigate to the left-hand navigation menu and select the Executions page.

<Frame>
  <img src="https://mintcdn.com/blinkops-2/xnKigMZdVI45SQhn/img/Automations/ExecutionsMenu.png?fit=max&auto=format&n=xnKigMZdVI45SQhn&q=85&s=8f9f54bca8bcbd7183ec454c6672248c" width="3452" height="2154" data-path="img/Automations/ExecutionsMenu.png" />
</Frame>

The page lists a history of workflow executions and their status. The status can be one of the following:

| Status | Icon | Description |
| - | - | - |
| Completed | <img src="https://mintcdn.com/blinkops-2/LJULXRaq3qGa0sq0/img/Automations/ExecutionsCheck.svg?fit=max&auto=format&n=LJULXRaq3qGa0sq0&q=85&s=7c70261b7b6b3430268281f4938c6403" width="20" height="20" data-path="img/Automations/ExecutionsCheck.svg" /> | The workflow finished running successfully without errors. |
| Stopped | <img src="https://mintcdn.com/blinkops-2/LJULXRaq3qGa0sq0/img/Automations/ExecutionPaused.svg?fit=max&auto=format&n=LJULXRaq3qGa0sq0&q=85&s=3bcb445781ee0813f6137d069ced73ec" width="20" height="20" data-path="img/Automations/ExecutionPaused.svg" /> | The workflow has been stopped by the creator or by its parent workflow. |
| In progress | <img src="https://mintcdn.com/blinkops-2/xnKigMZdVI45SQhn/img/Automations/ExecutionInProgress.png?fit=max&auto=format&n=xnKigMZdVI45SQhn&q=85&s=1a82fe127777bb28a83d84d12846f1bf" width="32" height="32" data-path="img/Automations/ExecutionInProgress.png" /> | The workflow is currently running and processing its steps. |
| Pending | <img src="https://mintcdn.com/blinkops-2/LJULXRaq3qGa0sq0/img/Automations/ExecutionsPending.svg?fit=max&auto=format&n=LJULXRaq3qGa0sq0&q=85&s=85692132aeecb36fed20e52edc4a783a" width="16" height="16" data-path="img/Automations/ExecutionsPending.svg" /> | The workflow is waiting—either for a step that requires human approval or for the [Wait](/docs/workflows/building-workflows/actions/basic-actions/flow-control-actions#wait) action to finish. |
| Failed | <img src="https://mintcdn.com/blinkops-2/LJULXRaq3qGa0sq0/img/Automations/ExecutionFailed.svg?fit=max&auto=format&n=LJULXRaq3qGa0sq0&q=85&s=dbc80ef2cbb8e7529f9ac51840da3cdd" width="20" height="20" data-path="img/Automations/ExecutionFailed.svg" /> | The workflow failed to execute successfully. |
| Timed out | <img src="https://mintcdn.com/blinkops-2/LJULXRaq3qGa0sq0/img/Automations/ExecutionTimedOut.svg?fit=max&auto=format&n=LJULXRaq3qGa0sq0&q=85&s=5e39d01ba949e5a411c9611195f9776b" width="20" height="20" data-path="img/Automations/ExecutionTimedOut.svg" /> | The workflow exceeded the maximum allowed run time and automatically timed out |

***

### Run Log Execution History

<Note>The **Run Log** displays executions from the last `30` days </Note>

Click on any execution and you will be redirected to the **Run Log** tab of that specific workflow.

* The left-hand side shows a list of the selected workflow's past executions.

* At the top of the page, a status bar shows relevant information related to the selected execution.

* If the workflow includes input parameters, it will display the user-provided inputs, the details of each step, and the corresponding output returned.

* <p>You can choose whether to display test runs in the Runs logs section. To adjust this, click the <Icon icon="bars-filter" iconType="solid" /> icon in the top-right corner, then check the box to show test runs or clear it to hide them. </p>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/xnKigMZdVI45SQhn/img/Automations/Executions.png?fit=max&auto=format&n=xnKigMZdVI45SQhn&q=85&s=278223a208b6e6fb74f68825b5e266d9" width="1727" height="1080" data-path="img/Automations/Executions.png" />
</Frame>

***

### Activity Graph

The activity graph is available for each active workflow and displays the workflow’s activity trends over the past `30 days`.

* Hover over the graph to see the total number of runs, along with the date of the last successful or failed execution.

* Click on the activity graph to open the **Executions** page for a detailed view.

<Frame>
  <img src="https://mintcdn.com/blinkops-2/eLYFBpTLBELPX82F/img/AutomationCanvas/ActivityGraph.png?fit=max&auto=format&n=eLYFBpTLBELPX82F&q=85&s=49c25593f57d20b3875b7177257be673" width="1728" height="1082" data-path="img/AutomationCanvas/ActivityGraph.png" />
</Frame>

***

## Monitoring Workflow Failure

### Error Indicator on the Activity Graph

<p>If the last run shown on the activity graph failed, the <Icon icon="circle-exclamation" color="#efc168" iconType="solid" /> will appear. Hover over this icon to see a tooltip with the time of the failure and the reason for the error. </p>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/eLYFBpTLBELPX82F/img/AutomationCanvas/ActivityGraphError.png?fit=max&auto=format&n=eLYFBpTLBELPX82F&q=85&s=c24640766c034aaf58c1936f110506d2" width="3130" height="172" data-path="img/AutomationCanvas/ActivityGraphError.png" />
</Frame>

***

### Monitoring Workflows Failure via Email

You can set up email notifications to alert you whenever a workflow fails. This ensures you are immediately aware of issues, such as failures in managing system, critical resources or production workflows, so you can respond quickly and minimize impact.

### Configuring Error Notifications

<Steps>
  <Step title="Turn On Notifications">
    From the [Workflow Overview](/docs/workflows/managing-workflows/workflow-overview-page) page of the selected workflow, toggle the **Notify on Error** option. A dialog box will appear.
  </Step>

  <Step title="Add Recipients">
    Enter the email addresses of the users who should receive failure notifications. Separate multiple addresses with a comma (`,`).

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/xnKigMZdVI45SQhn/img/Automations/NotifyOnError.gif?s=5c236e3272801a92a687035358c8d3e0" width="1300" height="720" data-path="img/Automations/NotifyOnError.gif" />
    </Frame>
  </Step>
</Steps>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.