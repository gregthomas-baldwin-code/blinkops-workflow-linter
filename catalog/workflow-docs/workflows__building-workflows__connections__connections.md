> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# About Connections

> Overview of connections in Blink for authenticating workflows with external services and integrations.

A connection is how a [Workflow](/docs/workflows/workflows) communicates with an external service to perform an action. It provides the necessary authentication and authorization details, either through user credentials or specific authentication parameters required by the target system, so that the workflow can successfully interact with that service.

Connections can be established with a wide range of cloud platforms, security tools, and monitoring systems, including popular services like [AWS](/docs/integrations/aws), [Kubernetes](/docs/integrations/kubernetes), [Slack](/docs/integrations/slack), and [Azure](/docs/integrations/azure). All credentials and configuration data are stored securely using a secret manager.

Once a connection is set up, it can be reused across any future workflows and even shared with other workspaces. This reusability helps streamline workflow creation and ensures a consistent and secure integration process.

<Frame>
  <img src="https://mintcdn.com/blinkops-2/LTL4io7BmEAPsFrF/img/Connections/ConnectionsList2.png?fit=max&auto=format&n=LTL4io7BmEAPsFrF&q=85&s=c5d9d2d4927c3671876d379af7b46411" width="3456" height="2164" data-path="img/Connections/ConnectionsList2.png" />
</Frame>

***

## Connection Types in Blink

Blink supports multiple types of connections to integrate with external services and systems. These connection types allow you to authenticate and interact with APIs, servers, and email services, whether they are cloud-based, on-premises, or custom. Below is an overview of the different connection types supported in the platform:

1. **External Service Providers**: Each third-party service provider (e.g., Slack, Jira, AWS) has its own dedicated connection type. Blink offers out-of-the-box integrations for many popular platforms.
   <Tip>To view the full list and learn how to configure each connection, visit the [Integrations](/docs/integrations/integrations) section of the documentation. </Tip>

2. **HTTP-Based Connections**: Blink provides three flexible HTTP connection types for authenticating with services not yet supported natively. These types allow you to attach custom authentication headers to your requests:
   * **HTTP Basic Authentication**: Use a username and password to authenticate using the Basic Auth scheme.
   * **HTTP Bearer Authentication**: Authenticate using a bearer token passed in the Authorization header.
   * **HTTP Custom Authentication**: Add up to three custom headers for more advanced or proprietary authentication schemes.

3. **SSH Connections**: Use SSH connections to securely connect to remote servers and run actions over SSH. You will need to provide a private key, username, and optionally a passphrase to encrypt the key.

4. **Email Server (SMTP) Connections**: Use this connection type to send emails through your own SMTP server rather than Blink’s default mail service. This is useful when you need to ensure delivery from a specific domain or enforce internal mail routing policies.

***

## Understanding Your Connections

Each connection includes key details, described in the table below:

<Frame>
  <img src="https://mintcdn.com/blinkops-2/LTL4io7BmEAPsFrF/img/Connections/ConnectionDescription.png?fit=max&auto=format&n=LTL4io7BmEAPsFrF&q=85&s=27f2c8417dd7a2e776fb75a6e8047204" width="1728" height="1082" data-path="img/Connections/ConnectionDescription.png" />
</Frame>

<div className="integrations-table">
  | | Variable | Description |
  | - | - | - |
  | 1 | **Name** | The user-defined name for the connection. |
  | 2 | **Description** | **Optional** - A short description of the connection. |
  | 3 | **Workspace** | Indicates the workspace where the connection was originally created. If the connection is shared from another workspace, that workspace’s name will be shown. |
  | 4 | **Shared With** | The names of the workspaces this connection is shared with. To view those workspaces, click **Edit** > **Sharing & Permissions**. |
  | 5 | **Used By** | The number of workflows (from your workspace and shared workspaces) currently using this connection. To view these workflows, click **Edit** > **Sharing & Permissions**. |
</div>

***

## Related Articles

<CardGroup cols={2}>
  <Card title="Creating a Connection" icon="plus" href="/docs/workflows/building-workflows/connections/creating-connection">
    Step-by-step guide to setting up new connections in the Blink platform.
  </Card>

  <Card title="Sharing Connections" icon="share" href="/docs/workflows/building-workflows/connections/sharing-connection">
    Learn how to securely share existing connections across different workspaces.
  </Card>

  <Card title="Using Connections" icon="network-wired" href="/docs/workflows/building-workflows/connections/dynamic-connection">
    Understand how to apply existing connections within your workflows.
  </Card>

  <Card title="Connecting to an On-Premises App" icon="link" href="/docs/workflows/building-workflows/connections/connecting-on-premises">
    Learn how to configure connections to on-premises applications.
  </Card>
</CardGroup>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.