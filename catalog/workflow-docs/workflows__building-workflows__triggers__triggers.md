> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# About Workflow Triggers

> Learn about the workflow triggers supported by Blink.

<Card title="How this Helps" icon="lightbulb">
  Triggers allow users to automate processes in response to manual actions, scheduled intervals, or external system events.
</Card>

A trigger is an event that starts a workflow in Blink. When a trigger event occurs, Blink automatically executes the workflow based on the selected trigger type.

## Trigger Types

Blink workflows can be initiated through three primary types of triggers: on-demand, event-based, and scheduled. Each trigger type has its own execution model and use cases. On-demand triggers are manually initiated by users, event-based triggers respond to external events in real-time, and scheduled triggers run at intervals as configured when building the workflow.

Blink supports these primary trigger types:

<CardGroup cols={3}>
  <Card title="On-Demand Workflows" icon="user" href="/docs/workflows/building-workflows/triggers/on-demand-triggers">
    User enters parameters manually.
  </Card>

  <Card title="Event-Based Workflows" icon="bolt" href="/docs/workflows/building-workflows/triggers/event-based-triggers">
    Parameters auto-retrieved from triggers.
  </Card>

  <Card title="Scheduled Workflows" icon="clock" href="/docs/workflows/building-workflows/triggers/scheduled-triggers">
    Parameters predefined or fetched dynamically.
  </Card>
</CardGroup>

By selecting the appropriate trigger type, users can ensure their workflows execute efficiently and in alignment with operational requirements.

### On-Demand Triggers

On-demand triggers are initiated manually by a user. This trigger type is useful when workflows need to be executed in response to an ad hoc request. Users can start workflows through various interfaces as described in the following table:

<div className="integrations-table">
  | Interface | Description |
  | - | - |
  | **Manual Trigger** | Users with access to the Blink platform can also trigger workflows manually. |
  | **Blink Portal** | Allows authorized users to trigger workflows through a dedicated UI. |
  | **Slack & Microsoft Teams** | Enables workflow execution directly from messaging platforms. |
  | **Subflows** | Workflows that can be used when triggered by a parent workflow, typically useful when the subflow is an action that is needed by more than one parent workflow. |
</div>

<Accordion title="Use cases and examples" icon="magnifying-glass-plus">
  Use cases for on-demand triggers include executing diagnostic tools, provisioning access, or performing manual checks on system status.

  A security team runs a workflow from the Self-Service Portal to reset credentials for a compromised user.
</Accordion>

### Event-Based Triggers

Event-based triggers automatically initiate workflows in response to external events. These events originate from third-party integrations, webhooks, or Blink events (errors and runner notifications). Common sources are as described in the following table:

<div className="integrations-table">
  | **Trigger Type** | **Description** |
  | - | - |
  | **External event triggers** | Events triggered by third-party integrations. |
  | **[Custom Webhooks](/docs/workflows/building-workflows/triggers/event-based-triggers/webhooks)** | User-defined webhooks that trigger workflows. |
  | **[Web Forms](/docs/blink-platform/web-form/web-form)** | Create and share a secure, interactive web page designed to gather input. |
  | **Native Blink events** | Built-in events generated within Blink. |
  | **[Case Management](/docs/case-management/case-management)** events | Events associated with case tracking and management. |
</div>

<Accordion title="Use cases and examples" icon="magnifying-glass-plus">
  Event-based triggers are essential for real-time automation, such as responding to security threats, updating records, or handling service incidents.

  When a high-severity security alert is generated in Splunk, Blink automatically creates a ticket in Jira and notifies the security team.
</Accordion>

### Scheduled Triggers

Scheduled triggers initiate workflows at intervals configured for the workflow. This is ideal for recurring tasks that need to be executed automatically without manual intervention.

Users can configure schedules using:

<div className="integrations-table">
  | Scheduling Method | Description |
  | - | - |
  | **Fixed Intervals** | Run workflows hourly, daily, weekly, or at custom time frames. |
  | **Cron Expressions** | Specify complex scheduling patterns using standard cron syntax. |
</div>

<Accordion title="Use cases and examples" icon="magnifying-glass-plus">
  Typical use cases for scheduled triggers include generating reports, performing system backups, and sending periodic notifications.

  A daily report is generated and sent to stakeholders every morning at 8 AM.
</Accordion>

## How to Choose the Right Trigger Type

Selecting the appropriate trigger type depends on the nature of the workflow and the desired level of automation:

* Use **on-demand triggers** for workflows requiring manual initiation and immediate ad-hoc execution.
* Use **event-based triggers** to automate responses based on real-time events and system changes.
* Use **scheduled triggers** for repetitive, time-based automation tasks.

## See It In Action

<iframe src="https://demo.arcade.software/JJ8nzg4ORssXSsJsK2Cj?embed&show_copy_link=true" title="Create your First Table" frameborder="0" loading="lazy" webkitAllowFullScreen mozAllowFullScreen allowFullScreen allow="clipboard-write" className="iframe-webhook" width="100%" height="420" />

## Related Articles

<CardGroup cols={2}>
  <Card title="Configuring Triggers" icon="toggle-off" href="/docs/workflows/building-workflows/triggers/configuring-triggers">
    Set up triggers to automate workflow execution.
  </Card>

  <Card title="Event-Based Triggers" icon="bolt" href="/docs/workflows/building-workflows/triggers/event-based-triggers/event-based-triggers">
    Start workflows automatically based on events.
  </Card>

  <Card title="On-Demand Trigger" icon="user" href="/docs/workflows/building-workflows/triggers/on-demand-triggers/on-demand-triggers">
    Manually execute workflows whenever required.
  </Card>

  <Card title="Scheduled Workflow Trigger" icon="calendar" href="/docs/workflows/building-workflows/triggers/scheduled-triggers">
    Run workflows on a set schedule automatically.
  </Card>
</CardGroup>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.