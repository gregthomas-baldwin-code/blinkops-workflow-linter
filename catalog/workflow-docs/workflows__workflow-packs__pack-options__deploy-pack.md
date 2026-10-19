> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy Pack to Workspace(s)

> Deploy a workflow pack to activate its workflows and make them available for execution in Blink.

The deploy pack to workspace feature establishes a deployment pipeline for workflows from development to production stages. The deploy pack to workspace feature replaces the contents of the pack in the target workspace with the contents of the pack from the origin workspace, while retaining the metadata of the workflow(s) in the target pack, including their share state, activation state, and connection mapping.

<Note>
  **Note**:

  * Workflows with the same name will be overridden by the latest **published** versions from the origin workspace.

  * Both the **published** and **draft versions** of workflows in the target workspace will be replaced by the deployed versions.
</Note>

## Deploying Packs to Workspace(s)

<Steps>
  <Step title="Open the Menu">
    Click the <Icon icon="square-ellipsis-vertical" iconType="solid" /> button in the top-right corner of the workflow pack and select **Deploy pack to workspace**.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/4a8dMD2Jv5wsADYv/img/AutomationCanvas/deploy-pack.png?fit=max&auto=format&n=4a8dMD2Jv5wsADYv&q=85&s=2d23c73f07ae21e9b4471e8c80862ee9" width="1728" height="1085" data-path="img/AutomationCanvas/deploy-pack.png" />
    </Frame>
  </Step>

  <Step title="Select Target Workspaces">
    In the **Deploy Pack to Workspace** pop-up, select the workspace(s) where you want to deploy the pack.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/eLYFBpTLBELPX82F/img/AutomationCanvas/choose-target-workspace.png?fit=max&auto=format&n=eLYFBpTLBELPX82F&q=85&s=fa341a01af15125b7190bc58b0fc3646" width="3452" height="2168" data-path="img/AutomationCanvas/choose-target-workspace.png" />
    </Frame>
  </Step>

  <Step title="Set Workflow Connections">
    For each connection used in the workflows, assign the appropriate [connection](/docs/workflows/building-workflows/connections/creating-connection) in the **target workspace**. This ensures the workflows can run successfully once deployed.\
    You may also update connections later in the [Workflow Editor](/docs/workflows/building-workflows/workflow-editor) tab.

    <Note> **Note**: If you have previously deployed this pack and configured connections, those settings will be **preserved** for future deployments.</Note>

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/eLYFBpTLBELPX82F/img/AutomationCanvas/automation-connections.png?fit=max&auto=format&n=eLYFBpTLBELPX82F&q=85&s=8ab0e70025a3188f612d1cf2cc5ee80f" width="3448" height="2158" data-path="img/AutomationCanvas/automation-connections.png" />
    </Frame>

    <Tip>**TIP** Although it is possible to configure connections later, it is strongly recommended to complete this step now to avoid potential errors and delays. </Tip>

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/4a8dMD2Jv5wsADYv/img/AutomationCanvas/warning-connection.png?fit=max&auto=format&n=4a8dMD2Jv5wsADYv&q=85&s=7d43aab908da845b8b93c4f467cb356f" width="3456" height="2192" data-path="img/AutomationCanvas/warning-connection.png" />
    </Frame>
  </Step>

  <Step title="Proceed Without Connections (Optional)">
    If no connections are required at this stage, you may skip this step and continue to deployment.
  </Step>

  <Step title="Finish Deployment">
    Click the **Finish** button in the bottom-right corner. An operation result popup will confirm that the pack was deployed successfully.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/eLYFBpTLBELPX82F/img/AutomationCanvas/SuccessfullyDeployed.png?fit=max&auto=format&n=eLYFBpTLBELPX82F&q=85&s=ea03fa3f0a749c6b266158a6c625e9c6" width="1730" height="1085" data-path="img/AutomationCanvas/SuccessfullyDeployed.png" />
    </Frame>
  </Step>

  <Step title="Verify in Target Workspace">
    Navigate to the target workspace to view the deployed pack and its workflows.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/4a8dMD2Jv5wsADYv/img/AutomationCanvas/deployed-workspace.png?fit=max&auto=format&n=4a8dMD2Jv5wsADYv&q=85&s=cf2238453448b82d8cd5abaccaafcbbe" width="1725" height="1080" data-path="img/AutomationCanvas/deployed-workspace.png" />
    </Frame>
  </Step>
</Steps>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.