> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Publish Approval as the Builder

> Submit workflows for publish approval as a builder in Blink's workflow governance process.

When publishing a workflow, you have the ability to control how it is shared and used within your workspace. To ensure proper governance and oversight, you can require approval from the workspace owner before the workflow is published or made available to others. This helps maintain security, consistency, and alignment with organizational policies while still enabling collaboration and automation at scale.

<Note>**Note**: When you publish a new workflow, or update an existing one, without having the `workflow:publish` permission, the action will require approval from a workspace approver. Approvers are users who have the `workflow:approve` permission within the workspace.</Note>

***

<Steps>
  <Step>
    After creating or updating the workflow, click the Publish button in the top-right corner of the editor.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/rnR3ZbI-RrvCvfuN/img/Automations/approval-management-1.png?fit=max&auto=format&n=rnR3ZbI-RrvCvfuN&q=85&s=4b91a1884af454e4b569305f85c24c74" width="3838" height="1908" data-path="img/Automations/approval-management-1.png" />
    </Frame>
  </Step>

  <Step>
    The Publish Approval dialog will appear.
  </Step>

  <Step>
    Select one or more <Tooltip tip="An approver is any user in the workspace who has the `workflow:approve` permission">approvers</Tooltip> from the dropdown list.

    <Note>**Note:** The available names are determined by whether any [approval settings](/docs/blink-platform/account-management/general#approvals) have been enabled. These settings are configured by the [tenant admin](/docs/blink-platform/account-management/roles#1-admin).</Note>

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/rnR3ZbI-RrvCvfuN/img/Automations/approval-management-3.png?fit=max&auto=format&n=rnR3ZbI-RrvCvfuN&q=85&s=8930d3013d0bf33661a2801ea92e0bd3" width="3840" height="1906" data-path="img/Automations/approval-management-3.png" />
    </Frame>
  </Step>

  <Step title="Optional:">
    Add a note to explain your request or describe the changes made to the workflow. This note will be visible to the approver.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/rnR3ZbI-RrvCvfuN/img/Automations/approval-management-2.png?fit=max&auto=format&n=rnR3ZbI-RrvCvfuN&q=85&s=0c2929509ee9db878027e05345d72edf" width="3810" height="1904" data-path="img/Automations/approval-management-2.png" />
    </Frame>
  </Step>

  <Step>
    Confirm your request by clicking the 'Request Approval' button.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/rnR3ZbI-RrvCvfuN/img/Automations/approval-management-7.png?fit=max&auto=format&n=rnR3ZbI-RrvCvfuN&q=85&s=f81ed9dc19fe306cd27a08b7f8e6c5aa" width="3838" height="1908" data-path="img/Automations/approval-management-7.png" />
    </Frame>
  </Step>

  <Step>
    You will see a confirmation message indicating that your approval request was successfully submitted. The request is now pending review by the workspace approver.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/rnR3ZbI-RrvCvfuN/img/Automations/approval-management-5.png?fit=max&auto=format&n=rnR3ZbI-RrvCvfuN&q=85&s=01f7e63be893a0753f849a31d7df79e9" width="3814" height="1902" data-path="img/Automations/approval-management-5.png" />
    </Frame>
  </Step>

  <Step>
    Once the approver makes a decision, you will receive an email notification. The notification includes:

    * **The target workspace**

    * **The request submission time**

    * **The workflow version**

    * **The request ID**

    * **Any notes or comments added by the approver**

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/rnR3ZbI-RrvCvfuN/img/Automations/email-request-approval.png?fit=max&auto=format&n=rnR3ZbI-RrvCvfuN&q=85&s=064c8faa6cae7a19cd2b98535b6c198b" width="1730" height="1318" data-path="img/Automations/email-request-approval.png" />
    </Frame>
  </Step>

  <Step>
    For more details, click 'Review Workflow' in the email notification.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/rnR3ZbI-RrvCvfuN/img/Automations/email-request-approval-2.png?fit=max&auto=format&n=rnR3ZbI-RrvCvfuN&q=85&s=80ba2f48a115c7ecd9bfbe05d092832f" width="1730" height="1318" data-path="img/Automations/email-request-approval-2.png" />
    </Frame>
  </Step>

  <Step>
    A popup will open showing the workflow and its approval status. From this view, you can:

    * **See the approval status in the top-left corner**

    * **Review the workflow name and version history**

    * **Edit the workflow (if permitted) using the option in the top-right corner**

    * **View and add comments related to the approval request**

    * **If the builder adds comments, the approver will be notified by email.**

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/rnR3ZbI-RrvCvfuN/img/Automations/approval-management-8.png?fit=max&auto=format&n=rnR3ZbI-RrvCvfuN&q=85&s=4baf19c425cb17ee9c3b8bb8cd824b6b" width="3824" height="1910" data-path="img/Automations/approval-management-8.png" />
    </Frame>

    <Note> **Note**: Please note that if the workspace owner approves the request, the builder will be allowed to publish this version of the workflow, as long as it stays unchanged or no newer version has been published. </Note>
  </Step>
</Steps>

***

## Approval Management as a Workspace Builder

In the sidebar, you can access the *Approval Management* page, where a table contains details about the workflow(s) you have submitted for approval requests.

By default, the "Approval Management" page is pre-filtered to show only requests that are still relevant for action:

* Pending (waiting for approval)
* Approved
* Denied

You can also request a 'Publish Approval' request from the 'Approval Management' Table by clicking the <Icon icon="square-ellipsis-vertical" iconType="solid" /> icon and selecting a request action.

<Frame>
  <img src="https://mintcdn.com/blinkops-2/pHeYU9Z5VQjsofss/img/Automations/ApprovalManagemntTable.png?fit=max&auto=format&n=pHeYU9Z5VQjsofss&q=85&s=f3e7e1a838f2d051a65c0f823728de43" width="3451" height="1902" data-path="img/Automations/ApprovalManagemntTable.png" />
</Frame>

| | Field | Description |
| - | - | - |
| **1** | **Workflow Name** | The name of the workflow for which a publish approval request was submitted. |
| **2** | **Workspace Name** | The workspace where the workflow resides and where the publish request was initiated. |
| **3** | **Requested By** | The user who submitted the request to publish the workflow. |
| **4** | **Approved By** | The user who approved the workflow for publishing. |
| **5** | **Published By** | The user who published the workflow after approval. |
| **6** | **Request ID** | A unique identifier assigned to the workflow publish request, used for tracking and auditing. |
| **7** | **Requested At** | The date and time when the publish approval request was created. |
| **8** | **Status** | The current state of the publish request. Possible values include **Pending Approval**, **Approved**, **Published**, and **Version Denied**. |
| **9** | **Status Filter** | A dropdown used to filter workflow approval requests by status: **Pending**, **Approved**, **Denied**, **Cancelled**, **Published**, or **Timeout**. |
| **10** | **Workflow Name Filter** | A dropdown used to filter approval requests by workflow name. |
| **11** | **Workspace Filter** | A dropdown used to filter approval requests by workspace. |
| **12** | **Requested By Filter** | A dropdown used to filter approval requests by the user who submitted them. |
| **13** | **Search Bar** | A free-text search used to quickly locate approval requests by workflow name, request ID, or requester. |

***


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.