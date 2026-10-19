> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating a New Connection

> Step-by-step guide to creating a new connection to an external service in Blink.

Connections allow you to securely link your Blink workflows to external systems and services. You can create a new connection from two locations within the platform:

<CardGroup col={1}>
  <Card title="The Connections Page" horizontal icon="circle-1" />

  <Card title="The Workflow Editor" horizontal icon="circle-2" />
</CardGroup>

***

### Creating a Connection from the Connections Page

Ideal for managing and organizing all your workspace connections in one place.

<Steps>
  <Step title="Open the Connections Page">
    Navigate to the **Connections** page in the Blink platform. You will see a table listing all existing connections in your workspace.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/LTL4io7BmEAPsFrF/img/Connections/ConnectionsPage.gif?s=e1f0a259b8eecbcb8c9cd09955532a99" width="1944" height="1080" data-path="img/Connections/ConnectionsPage.gif" />
    </Frame>
  </Step>

  <Step title="Start a New Connection">
    Click **Add connection** at the top of the page, then select a service provider from the list or search bar. Click on the provider’s icon to continue.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/LTL4io7BmEAPsFrF/img/Connections/AddNewConnection.gif?s=f59f8588d298f0e91084e17d6ad27282" width="1980" height="1080" data-path="img/Connections/AddNewConnection.gif" />
    </Frame>

    <Tip>
      **Note**:
      The <Icon icon="scribble" /> icon indicates that the connection is an MCP (Model Context Protocol)

      <Frame>
        <img src="https://mintcdn.com/blinkops-2/Tezxt8K43IuSekwF/img/Connections/MCPConnection.png?fit=max&auto=format&n=Tezxt8K43IuSekwF&q=85&s=74e3b37b339e8b88649232acfcb90e37" width="3448" height="2190" data-path="img/Connections/MCPConnection.png" />
      </Frame>
    </Tip>
  </Step>

  <Step title="Name and Describe Your Connection-(Optional) ">
    1. Edit the **Connection Name** (cannot be changed later).
    2. Add a **Description** to help identify the connection's purpose.
       <Note>**Note**: If available, select the MCP checkbox to configure the connection as an MCP (Model Context Protocol). Only connections with the <Icon icon="scribble" /> can be configured as an MCP.</Note>

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/LTL4io7BmEAPsFrF/img/Connections/RenameConnection.gif?s=0acb2f5cdfd7d21a72a3c62b63c70028" width="1980" height="1080" data-path="img/Connections/RenameConnection.gif" />
    </Frame>
  </Step>

  <Step title="Select a Connection Method">
    Choose a connection method supported by the selected vendor. Some vendors may offer up to three different connection methods.

    <Tip>The recommended method appears in the blue button. You can change the method later by editing the connection.</Tip>

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/LTL4io7BmEAPsFrF/img/Connections/ConnectionMethod.png?fit=max&auto=format&n=LTL4io7BmEAPsFrF&q=85&s=169756968c0f74ada783943af4eb107e" width="3568" height="2064" data-path="img/Connections/ConnectionMethod.png" />
    </Frame>
  </Step>

  <Step title="Configure Connection Parameters">
    Fill in the required parameters for the connection:

    * **Tags** (optional, used for categorization or filtering)
    * **Connection Type** (required)\
      <Note> Each connection type includes additional parameters specific to that method.</Note>
  </Step>

  <Step title="Test the connection (optional)">
    Click [**Test Connection**](#testing-a-connection) to ensure the configuration is valid before creating the connection.
  </Step>

  <Step title="Create the Connection">
    Click 'Create connection' to finalize the setup. The new connection will now appear on the 'Connections' page.
  </Step>
</Steps>

***

### Creating a Connection in the Workflow Editor

Ideal when you need to add or create a connection directly while building a workflow.

<Note> **Note**: If you have a personal account with the provider used in the step, you can create a connection using open authorization (OAuth) or [single sign-on (SSO)](/docs/getting-started/signing-in).</Note>

<Steps>
  <Step title="Select a Connection for the Step">
    In the [Workflow Editor](/docs/workflows/building-workflows/workflow-editor), navigate to a step that requires a connection. Click **Select connection**, then choose an existing connection or create a new one.
  </Step>

  <Step title="Create a New Connection">
    To create a new connection, click '**+ Create New Connection**'. The **New Connection** dialog will appear, displaying the available methods for the selected service.
  </Step>

  <Step title="Choose a Connection Method">
    Select the desired connection method for this integration.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/LTL4io7BmEAPsFrF/img/Connections/WorkflowConnection.gif?s=ff7c35f12cf277091c82c1e6f081396f" width="1296" height="720" data-path="img/Connections/WorkflowConnection.gif" />
    </Frame>
  </Step>

  <Step title="Fill in Connection Details">
    * Complete the required configuration fields:
    * **Tags** (optional)
    * **Connection Type** (mandatory)

    <Note>The selected type may prompt you to enter additional, vendor-specific parameters.</Note>
  </Step>

  <Step title="Test the Connection- (Optional)">
    Click [Test Connection](#testing-a-connection) to ensure your setup is working correctly before saving.
  </Step>

  <Step title="Finalize the Connection">
    Click 'Create connection'. The new connection will now be available and listed on the 'Connections' page.
  </Step>
</Steps>

***

## Testing a Connection

<Note> **Note**: Connections created with the `_OAuth_` method or with the `_Or sign in with_` method cannot be tested. A connection can only be tested when all mandatory parameters are filled in.</Note>

<Steps>
  <Step title="Open the Runner Selection Menu">
    Click the dropdown menu to see available runners.
  </Step>

  <Step title="Choose a Runner">
    Select the runner with which to test the connection. The default runner is ***Blink Cloud***.
  </Step>

  <Step title="Test the Connection">
    Click 'Test'. The result of the test will be displayed. Depending on the service provider, the information about the results differ.
  </Step>

  <Step title="Create the Connection">
    Click 'Create connection'. The connection is created and appears in your connections screen.
  </Step>
</Steps>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/LTL4io7BmEAPsFrF/img/Connections/TestConnection.gif?s=019643e23b7dc2ba2b523b6e4fceaa8f" width="1944" height="1080" data-path="img/Connections/TestConnection.gif" />
</Frame>

***

## Editing a Connection

You can update an existing connection at any time to change its configuration, authentication details, or tags.

To edit a connection, go to the **Connections** page and choose one of the following methods:

1. Click directly on the connection you want to edit, make your changes, and then click **Save**.

   <Frame>
     <img src="https://mintcdn.com/blinkops-2/LTL4io7BmEAPsFrF/img/Connections/EditConnection1.gif?s=07cb2e270d652567c9f457cbe5489e43" width="1944" height="1080" data-path="img/Connections/EditConnection1.gif" />
   </Frame>

**OR**

2. Click the <Icon icon="square-ellipsis-vertical" iconType="solid" /> icon next to the connection, select **Edit**, make your changes, and click **Save**.

   <Frame>
     <img src="https://mintcdn.com/blinkops-2/LTL4io7BmEAPsFrF/img/Connections/EditConnection2.gif?s=3b93d9c375cc3c98e11976dda1a9078f" width="1944" height="1080" data-path="img/Connections/EditConnection2.gif" />
   </Frame>

***


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.