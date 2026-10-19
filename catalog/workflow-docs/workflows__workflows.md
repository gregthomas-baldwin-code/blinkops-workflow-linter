> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# About Workflows

> Learn about workflows, their components, and how they automate tasks across multiple systems through a centralized platform.

<Card title="How this Helps" icon="lightbulb">
  Workflows can be copied or moved to different workspaces, facilitating collaborative automation and task management. Learn more about copying or moving workflows between workspaces [here](/docs/workflows/workflow-packs/pack-options/move-or-copy-workflows).
</Card>

A workflow is a sequence of automated steps containing actions that are <Tooltip tip="An event that initiates the workflow.">triggered</Tooltip> by events, schedules, or manual input. Workflows, the backbone of automation in Blink, enable you to complete a specific task or process without manual intervention. They enable users to automate tasks across multiple systems, platforms and tools through a centralized platform.

Blink workflows can handle various levels of complexity:

* Simple, single-step processes such as for data validation
* Complex, multi-system operations involving multiple services and cross-platform automations that bridge different technologies
* Conditional steps that adapt based on inputs or results

<Accordion title="Example I: Automated User Access Review for Compliance" icon="memo-circle-info" iconType="solid" size={30}>
  A compliance officer at **Stark Industries** needs an automated workflow to **review user access permissions** across critical systems.

  The process begins (is triggered automatically) weekly (a **scheduled trigger**), initiating an audit of **user roles and permissions** in AWS IAM and Active Directory. The workflow then evaluates access levels against company policies, **flagging any unauthorized or excessive permissions** for review.

  If violations are detected, the workflow **notifies security and compliance teams**, instructing them how to proceed with remediation.
</Accordion>

# Workflow Architecture

The following image illustrates the workflow hierarchy in Blink:

<Frame>
  <img src="https://mintcdn.com/blinkops-2/iMIEUHxdi6cXuLI5/img/workflow-hierarchy.png?fit=max&auto=format&n=iMIEUHxdi6cXuLI5&q=85&s=83bc8963cf879b7d9d7865e416b21135" alt="Workflow Hierarchy" width="1946" height="2038" data-path="img/workflow-hierarchy.png" />
</Frame>

These components are as described in the following table:

<div className="integrations-table">
  | | Component | Description |
  | - | - | - |
  | 1 | **[Triggers](/docs/workflows/building-workflows/triggers/triggers)** | Events and their conditions that initiate a workflow. Blink workflows can be initiated through three primary types of triggers: [on-demand](/docs/workflows/building-workflows/triggers/on-demand-triggers/on-demand-triggers), [event-based](/docs/workflows/building-workflows/triggers/event-based-triggers/event-based-triggers), and [scheduled](/docs/workflows/building-workflows/triggers/scheduled-triggers). |
  | 2 | **[Steps](/docs/workflows/building-workflows/steps)** and **[Actions](/docs/workflows/building-workflows/actions/actions)** | Steps are individual units within a workflow, each designed to perform a specific task. Actions are the functional components within each step, executing tasks based on configured parameters. |
  | 3 | **[Flow controls](/docs/workflows/building-workflows/actions/basic-actions/flow-control-actions)** | Flow controls define how a workflow proceeds from one step to another based on conditions, loops, or branching logic. These include `if` conditions, `switch` statements, and loops that determine execution paths dynamically based on input values, action results, or external data. |
  | 4 | **[Outputs](/docs/workflows/building-workflows/steps)** | The final results or data produced by a workflow or any of its steps. Outputs can be used as inputs in subsequent workflows, stored for reporting, or sent as notifications to relevant stakeholders. Outputs can also be shared with users who triggered the workflow on-demand, or saved as part of a file for future use. |
</div>

<Tip>
  You can utilize the [Builder Copilot](/docs/builder-copilot/builder-copilot) to build new workflows and update existing ones efficiently, leveraging AI-powered automation to streamline workflow design.
</Tip>

<Accordion title="Example II: On New Splunk Incident - Open Ticket in ServiceNow and Notify Security Channel" icon="memo-circle-info" iconType="solid" size={30}>
  This <Tooltip tip="Pre-built workflow for common use cases.">[Blink workflow template](/docs/workflows/templates/templates)</Tooltip> automates the response to Splunk alerts by **creating a ServiceNow ticket** and **notifying the security team in Slack**, ensuring swift incident management.

  The flow appears as in the following screenshot:

  <Frame>
    <img src="https://mintcdn.com/blinkops-2/iMIEUHxdi6cXuLI5/img/workflow-hierarchy-splunk-example.png?fit=max&auto=format&n=iMIEUHxdi6cXuLI5&q=85&s=3f2f72640b70a6a4c5bdb2119167d38f" alt="Workflow Hierarchy Example" width="1350" height="1366" data-path="img/workflow-hierarchy-splunk-example.png" />
  </Frame>

  <Steps>
    <Step title="Trigger">
      A security alert **detected by a new Splunk event** triggers the workflow, initiating the automation process.
    </Step>

    <Step title="Generate Ticket Description">
      The workflow compiles key details from the Splunk alert to generate a structured **incident description**.

      * **Action:** Extracts alert owner, event type, results link, serial number, and event message if they exist.
      * **Outcome:** A detailed incident report is created.
    </Step>

    <Step title="Create Incident in ServiceNow">
      The workflow automatically **creates a new incident ticket** in ServiceNow with the alert details.

      * **Action:** Generates a high-priority ServiceNow ticket with a short description, the severity, impact and assignee.
      * **Outcome:** The incident is logged in ServiceNow, and the ticket number is generated for tracking.
    </Step>

    <Step title="Notify Security Team">
      The workflow **sends an alert to the security team** in Slack, including the incident details and ServiceNow ticket number.

      * **Action:** Posts a Slack message with the ticket number for the ServiceNow ticket.
      * **Outcome:** The workflow ends successfully.
    </Step>

    <Step title="Outputs">
      * `incident_details`
      * `ticket_id`
    </Step>
  </Steps>
</Accordion>

***

## Managed Workflows

A managed workflow is a locked, view-only workflow that is owned and maintained by Blink. You can view the workflow and run it in Test mode, but you cannot modify its logic, configuration, name, or description. Because managed workflows are maintained by Blink, Blink may update or modify them from time to time to improve their functionality and performance.

A <Icon icon="lock" /> Managed badge is displayed in:

1. The [Workflows page](/docs/workflows/workflows),
2. The [Workflow Overview page (in the header)](/docs/workflows/managing-workflows/workflow-overview-page),
3. The [Workflow Editor](/docs/workflows/building-workflows/workflow-editor),
4. The [Workflow's Run Log](/docs/workflows/debugging-workflows/workflow-run-logs),

to clearly indicate that the workflow is `view-only`.

<Frame>
  <img src="https://mintcdn.com/blinkops-2/3xG_00jOHqxhS9mc/img/Automations/LockingWorkflows.png?fit=max&auto=format&n=3xG_00jOHqxhS9mc&q=85&s=0a845e899eb37b32790e60d38f0d3868" width="1920" height="1080" data-path="img/Automations/LockingWorkflows.png" />
</Frame>

***

### Supported and Restrictions Actions for Managed Workflows

1. **Users can perform the following actions on a fully locked workflow**:
   * [Manage portal access](/docs/blink-platform/blink-portal/blink-portal#service-settings-in-the-blink-portal)
   * [Execute a test run](/docs/workflows/testing-workflows/testing-workflows#testing-different-workflow-trigger-types)
   * Cancel a running workflow
   * [Open the workflow's Run Log](/docs/workflows/debugging-workflows/workflow-run-logs)

2. **The following actions are not available for fully locked workflows**:
   * [Copy or move the workflow](/docs/workflows/workflow-packs/pack-options/move-or-copy-workflows)
   * Delete the workflow

3. **[Workflow Overview Settings](/docs/workflows/managing-workflows/workflow-overview-page)**- All workflow settings in the Workflow Overview page are `read-only`.

4. **API enforcement**: Locked workflows cannot be modified through the API or automated workflows. Any attempt to update a locked workflow will be unsuccessful

***

## Related Articles

<CardGroup cols={2}>
  <Card title="Triggers" icon="toggle-on" href="/docs/workflows/building-workflows/triggers">
    Configure triggers to start workflows based on events.
  </Card>

  <Card title="Steps" icon="arrow-progress" href="/docs/workflows/building-workflows/steps">
    Define and organize actions within a workflow.
  </Card>

  <Card title="Conditions" icon="code-fork" href="/docs/blink-platform/interface-components/condition-builder">
    Add logic to control workflow execution paths.
  </Card>

  <Card title="Creating a Workflow" icon="plus" href="/docs/workflows/creating-a-workflow">
    Build a new workflow from scratch in Blink.
  </Card>
</CardGroup>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.