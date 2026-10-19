> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Dynamic Connections

> Use dynamic connections to assign service credentials at runtime based on workflow variables in Blink.

## Using Dynamic Connections

A dynamic connection allows you to assign a connection at runtime using a [dynamic variable](/docs/workflows/building-workflows/dynamic-variables/variable-picker#dynamic-variables-types). Instead of selecting a fixed connection, you can configure steps to reference a dynamic variable using the [variable picker](/docs/workflows/building-workflows/dynamic-variables/variable-picker), typically an [input parameter](/docs/workflows/building-workflows/triggers/on-demand-triggers/input-parameters), that resolves to a valid connection during execution.

<Steps>
  <Step title="Open the Variable Picker">
    In the workflow step that requires a connection, click on the **Connections Required** dropdown menu. This opens the [Variable Picker](/docs/workflows/building-workflows/dynamic-variables/variable-picker).

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/LTL4io7BmEAPsFrF/img/Connections/DynamicConnection.gif?s=89ac91398ddd3649a5c90534724e329e" width="1944" height="1080" data-path="img/Connections/DynamicConnection.gif" />
    </Frame>
  </Step>

  <Step title="Select a Dynamic Variable">
    Choose a dynamic variable (typically an input parameter) to assign the connection.

    <Warning>Ensure the connection type matches the expected type for the action. If the types don’t match, the step will fail to execute.</Warning>

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/LTL4io7BmEAPsFrF/img/Connections/AddDynamicConnection.gif?s=2f5208b9bdd7f120fd077fee2da3c110" width="1944" height="1080" data-path="img/Connections/AddDynamicConnection.gif" />
    </Frame>
  </Step>
</Steps>

***

### Example: Adding a Dynamic Connection via Input Parameters

You can configure actions in your workflow to use dynamic connections by passing the connection as an **input parameter**. This allows the connection to be selected at runtime, giving you greater flexibility and reusability across different workflows.

<Note><p>You can also obtain **Connection ID** in the 'Connections' page. Navigate to the 'Connections' page, click the <Icon icon="square-ellipsis-vertical" iconType="solid" /> icon next to the connection and select **Copy ID**. Use the `ID` in your steps, not the connection name.</p></Note>

<Steps>
  <Step title="Create an Input Parameter">
    Create an [input parameter](/docs/workflows/building-workflows/triggers/on-demand-triggers/input-parameters) and set its type to 'Connection' to allow the workflow to receive a connection ID at runtime.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/LTL4io7BmEAPsFrF/img/Connections/CreateInputConnection.gif?s=0e259740a306ed03950d9bb5819b7fbf" width="1944" height="1080" data-path="img/Connections/CreateInputConnection.gif" />
    </Frame>
  </Step>

  <Step title="Open the Variable Picker in a Step">
    In the workflow step that requires a connection, click on the 'Connections Required' dropdown menu to open the [Variable Picker](/docs/workflows/building-workflows/dynamic-variables/variable-picker).

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/LTL4io7BmEAPsFrF/img/Connections/DynamicConnection.gif?s=89ac91398ddd3649a5c90534724e329e" width="1944" height="1080" data-path="img/Connections/DynamicConnection.gif" />
    </Frame>
  </Step>

  <Step title="Select the Input Parameter">
    Select the input parameter you created in `Step 1` as the [dynamic variable](/docs/workflows/building-workflows/dynamic-variables/variable-picker#dynamic-variables-types) for the connection.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/LTL4io7BmEAPsFrF/img/Connections/AddGWDynamicConnection.gif?s=fc0b989b0a02213389866fb7a309ae3d" width="1944" height="1080" data-path="img/Connections/AddGWDynamicConnection.gif" />
    </Frame>
  </Step>

  <Step title="Run the Workflow with a Connection ID">
    Start the workflow and provide a valid connection ID through the input parameter. The step will use this connection during execution.
  </Step>
</Steps>

***


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.