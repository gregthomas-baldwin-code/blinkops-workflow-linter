> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Move or Copy Workflows Between Workspaces

> Move or copy individual workflows between packs and workspaces in Blink.

You can move or copy a workflow to a different [pack](/docs/workflows/workflow-packs/workflow-packs), either within the **same workspace** or across **different workspaces**, making it easy to organize and manage your workflows.

***

### Move or Copy a Workflow in the Same Workspace

<Steps>
  <Step title="Open Workflow Menu">
    Click the <Icon icon="square-ellipsis-vertical" iconType="solid" /> icon in the top-right corner of the workflow you want to move or copy, then select the **Move/Copy** option.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/eLYFBpTLBELPX82F/img/AutomationCanvas/AutomationSettings.png?fit=max&auto=format&n=eLYFBpTLBELPX82F&q=85&s=3c68dc45ecf081d572f5176bf19bcd7f" width="3582" height="2053" data-path="img/AutomationCanvas/AutomationSettings.png" />
    </Frame>
  </Step>

  <Step title="Choose Pack in Same Workspace">
    In the **Move/Copy** wizard, select your current workspace as the target. Then choose the destination pack and indicate whether you want to **Copy** or **Move** the workflow.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/eLYFBpTLBELPX82F/img/AutomationCanvas/AutomationOptionSameWorkspace.png?fit=max&auto=format&n=eLYFBpTLBELPX82F&q=85&s=ad01220209ceb906c5f46db04e7bd9f5" width="3582" height="2060" data-path="img/AutomationCanvas/AutomationOptionSameWorkspace.png" />
    </Frame>
  </Step>

  <Step title="Include Subflows (Optional)">
    If the workflow contains subflows, check the box to include them in the move or copy. Unchecking it will exclude subflows from the target pack.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/eLYFBpTLBELPX82F/img/AutomationCanvas/RelatedSubflows.png?fit=max&auto=format&n=eLYFBpTLBELPX82F&q=85&s=48e9bbe1d213b1c29b4b78ce1e92c4b8" width="3579" height="2056" data-path="img/AutomationCanvas/RelatedSubflows.png" />
    </Frame>
  </Step>
</Steps>

***

### Move or Copy a Workflow to a Different Workspace

<Note>When copying or moving a workflow to a **different workspace**, there are a few additional configuration steps you will need to complete.</Note>

<Steps>
  <Step title="Open Workflow Options">
    Click the <Icon icon="square-ellipsis-vertical" iconType="solid" /> icon in the top-right corner of the workflow and select the **Move/Copy** option.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/eLYFBpTLBELPX82F/img/AutomationCanvas/AutomationSettings.png?fit=max&auto=format&n=eLYFBpTLBELPX82F&q=85&s=3c68dc45ecf081d572f5176bf19bcd7f" width="3582" height="2053" data-path="img/AutomationCanvas/AutomationSettings.png" />
    </Frame>
  </Step>

  <Step title="Select Target Workspace and Pack">
    In the wizard, choose a **different workspace** as the target. Then select the target pack and choose whether to **Move** or **Copy** the workflow.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/eLYFBpTLBELPX82F/img/AutomationCanvas/AutomationOptions.png?fit=max&auto=format&n=eLYFBpTLBELPX82F&q=85&s=ab28f5b818759e3378c1fabc0e2270e7" width="3574" height="2060" data-path="img/AutomationCanvas/AutomationOptions.png" />
    </Frame>
  </Step>

  <Step title="Review and Configure Subflows">
    If your workflow includes **Subflow(s)**, they will automatically be copied or moved along with the parent workflow.

    * If a workflow or subflow with the same name exists in the target workspace, you’ll be prompted to rename it or use the existing one.
    * All subflows will be placed into the **same pack** as the parent workflow, regardless of their original location.

    <Note> Subflows from other packs in the origin workspace will be relocated to the same pack as their parent in the target workspace.</Note>

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/eLYFBpTLBELPX82F/img/AutomationCanvas/ReviewSubflow.png?fit=max&auto=format&n=eLYFBpTLBELPX82F&q=85&s=aaa8e72e9533040681ec82963647ab8f" width="3572" height="2030" data-path="img/AutomationCanvas/ReviewSubflow.png" />
    </Frame>
  </Step>

  <Step title="Set Connections">
    For each connection used by the workflow, select a corresponding [connection](/docs/workflows/building-workflows/connections/creating-connection) in the target workspace.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/eLYFBpTLBELPX82F/img/AutomationCanvas/SubflowConnection.png?fit=max&auto=format&n=eLYFBpTLBELPX82F&q=85&s=c0a0040f88619520550aad8be04b6297" width="3578" height="2056" data-path="img/AutomationCanvas/SubflowConnection.png" />
    </Frame>

    If no connections need to be configured, you may skip this step:

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/eLYFBpTLBELPX82F/img/AutomationCanvas/NoConnection.png?fit=max&auto=format&n=eLYFBpTLBELPX82F&q=85&s=936be7b57951d260cd79391eab892f1f" width="3576" height="2044" data-path="img/AutomationCanvas/NoConnection.png" />
    </Frame>
  </Step>

  <Step title="Set Activation Status">
    Choose the activation status of the copied or moved workflow:

    * Use the toggle to **Activate all workflows**, or
    * Activate individual workflows one by one.

    > Subflows will always be **activated** in the target workspace.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/eLYFBpTLBELPX82F/img/AutomationCanvas/ActivateSubflow.png?fit=max&auto=format&n=eLYFBpTLBELPX82F&q=85&s=aa7cec80de098a214973891977a2661b" width="3574" height="2052" data-path="img/AutomationCanvas/ActivateSubflow.png" />
    </Frame>
  </Step>

  <Step title="Enable Self-Sharing (Optional)">
    Decide whether to share the workflow to the [Blink Portal](/docs/blink-platform/blink-portal/blink-portal#share-workflows-to-the-blink-portal) using the toggle.

    <Info>
      You can only share a workflow via the self-service portal if it is marked as **Active** in the previous step.
    </Info>

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/eLYFBpTLBELPX82F/img/AutomationCanvas/SubflowSelfService.png?fit=max&auto=format&n=eLYFBpTLBELPX82F&q=85&s=d1c9e98aae7358e2301357a80e816a5d" width="3584" height="2054" data-path="img/AutomationCanvas/SubflowSelfService.png" />
    </Frame>
  </Step>

  <Step title="Finish and Confirm">
    Click the **Finish** button to complete the process. A confirmation popup will appear in the bottom-right corner indicating that the workflow has been successfully copied or moved.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/eLYFBpTLBELPX82F/img/AutomationCanvas/Successful.png?fit=max&auto=format&n=eLYFBpTLBELPX82F&q=85&s=c10a198b0fb7d702eb7e53f94af6e267" width="3578" height="2054" data-path="img/AutomationCanvas/Successful.png" />
    </Frame>
  </Step>
</Steps>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.