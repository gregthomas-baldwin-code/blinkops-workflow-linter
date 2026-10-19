> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Publish Approval as the Workspace Owner

> Review and approve workflow publish requests as an owner in Blink's workflow governance process.

When publishing a workflow, you have the ability to control how it is shared and used within your workspace. To ensure proper governance and oversight, you can require approval from the workspace owner before the workflow is published or made available to others. This helps maintain security, consistency, and alignment with organizational policies while still enabling collaboration and automation at scale.

***

<Steps>
  <Step>
    As the workspace owner, you will receive an email notification when another user requests approval to publish a workflow to your workspace.
  </Step>

  <Step>
    The email notification includes key details about the request, such as the target workspace, the time the request was submitted, the workflow version, the request ID, and an optional note from the requester explaining the purpose of the workflow or the changes made.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/rnR3ZbI-RrvCvfuN/img/Automations/approval-management-10.png?fit=max&auto=format&n=rnR3ZbI-RrvCvfuN&q=85&s=3b95d3c5ea3e91cfe9ef19d631e4631e" width="3119" height="1854" data-path="img/Automations/approval-management-10.png" />
    </Frame>
  </Step>

  <Step>
    To review the request, click the Review Request button in the email. This will take you directly to the approval screen.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/rnR3ZbI-RrvCvfuN/img/Automations/approval-management-11.png?fit=max&auto=format&n=rnR3ZbI-RrvCvfuN&q=85&s=e673e28f32861db35a1cc840ad193446" width="3125" height="1829" data-path="img/Automations/approval-management-11.png" />
    </Frame>
  </Step>

  <Step>
    A popup will display the requested workflow for approval, along with all its details. You can also explore the [Workflow Version History](/docs/workflows/managing-workflows/workflow-version-history) as well as you can also compare the published workflow version with the version sent for approval.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/rnR3ZbI-RrvCvfuN/img/Automations/approval-management-13.png?fit=max&auto=format&n=rnR3ZbI-RrvCvfuN&q=85&s=88d7915804e7029960715296926f7462" width="3578" height="2058" data-path="img/Automations/approval-management-13.png" />
    </Frame>
  </Step>

  <Step>
    As the approver, you can choose to either Approve or Deny the request to publish the workflow to your workspace.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/rnR3ZbI-RrvCvfuN/img/Automations/approval-management-14.png?fit=max&auto=format&n=rnR3ZbI-RrvCvfuN&q=85&s=6c130ba492dcf4182b2293caa9dd4d92" width="3578" height="2058" data-path="img/Automations/approval-management-14.png" />
    </Frame>
  </Step>

  <Step>
    If you select 'Deny', a confirmation popup will appear prompting you to provide a reason for the rejection. This feedback is shared with the requester to explain why the approval was denied. Click 'Deny' to finalize your decision.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/rnR3ZbI-RrvCvfuN/img/Automations/approval-management-15.png?fit=max&auto=format&n=rnR3ZbI-RrvCvfuN&q=85&s=af58fe3cfb03087814e89908d5d80922" width="3584" height="2064" data-path="img/Automations/approval-management-15.png" />
    </Frame>
  </Step>

  <Step>
    If you select 'Approve', a confirmation popup will appear where you can optionally add a note for the requester. Click 'Approve' to confirm your decision.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/rnR3ZbI-RrvCvfuN/img/Automations/approval-management-16.png?fit=max&auto=format&n=rnR3ZbI-RrvCvfuN&q=85&s=7978c0d3ae2929ed1aa94991f9c04e3b" width="3576" height="2046" data-path="img/Automations/approval-management-16.png" />
    </Frame>
  </Step>

  <Step>
    After approving the request, you can complete the process by clicking the 'Publish' button, which publishes the approved workflow to your workspace.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/rnR3ZbI-RrvCvfuN/img/Automations/approval-management-17.png?fit=max&auto=format&n=rnR3ZbI-RrvCvfuN&q=85&s=2dc4321c130fd589a932b756651f410e" width="3577" height="2046" data-path="img/Automations/approval-management-17.png" />
    </Frame>
  </Step>
</Steps>

***

## Approval Management as the Workspace Owner

By default, the "Approval Management" page is pre-filtered to show only requests that are still relevant for action:

* Pending (waiting for approval)
* Approved
* Denied

<Note>
  **Note:**

  * The **Approval Management** page is on the tenant level, therefore if you are the owner of a few different workspaces you can see all the publish approval requests from all your workspaces.

  * You can also **deny** or **approve** the request from the 'Approval Management Table' by clicking the <Icon icon="square-ellipsis-vertical" iconType="solid" /> icon and selecting a **request action**.
</Note>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/pHeYU9Z5VQjsofss/img/Automations/ApprovalManagemntTable.png?fit=max&auto=format&n=pHeYU9Z5VQjsofss&q=85&s=f3e7e1a838f2d051a65c0f823728de43" width="3451" height="1902" data-path="img/Automations/ApprovalManagemntTable.png" />
</Frame>

| | Field | Description |
| - | - | - |
| **1** | **Workflow Name** | The name of the workflow for which a publish approval request was submitted. |
| **2** | **Workspace Name** | The workspace where the workflow resides and where the publish request was initiated. |
| **3** | **Requested By** | The user who submitted the request to publish the workflow. |
| **4** | **Approved By** | The user who approved the workflow for publishing. Displays `—` if the request has not yet been approved. |
| **5** | **Published By** | The user who published the workflow after approval. Displays `—` until the workflow is published. |
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