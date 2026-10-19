> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Sharing Packs

> Share workflow packs with other workspaces to enable cross-team automation collaboration in Blink.

## Sharing Packs to Workspaces

Use the steps below to share a pack with one or more workspaces. Sharing allows you to maintain a central source of truth while enabling teams in different workspaces to access the same packs and its workflows

<Steps>
  <Step title="Open the Share Menu">
    To begin, locate the pack you want to share on the **Workflows** page. Click the <Icon icon="square-ellipsis-vertical" iconType="solid" /> button on the top-right corner of the pack. Select 'Share pack to workspace'. A pop-up will appear listing all available workspaces.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/eLYFBpTLBELPX82F/img/AutomationCanvas/ShareMenu.png?fit=max&auto=format&n=eLYFBpTLBELPX82F&q=85&s=d41960bacf8ead392d4fc5402a3464f7" width="1728" height="1081" data-path="img/AutomationCanvas/ShareMenu.png" />
    </Frame>
  </Step>

  <Step title="Select Target Workspaces">
    Check the box next to each **workspace** you want to share the pack with. Then click 'Apply'.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/eLYFBpTLBELPX82F/img/AutomationCanvas/SharedWithWorkSpace.png?fit=max&auto=format&n=eLYFBpTLBELPX82F&q=85&s=1aac2c0f68e740b4a95a782c8ec26662" width="1728" height="1087" data-path="img/AutomationCanvas/SharedWithWorkSpace.png" />
    </Frame>
  </Step>

  <Step title="Verify Shared Workspaces">
    Once shared, the pack will appear in the selected workspaces. You will also be able to see which user shared the pack.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/eLYFBpTLBELPX82F/img/AutomationCanvas/SharedWithWorkSpaces.png?fit=max&auto=format&n=eLYFBpTLBELPX82F&q=85&s=610070597b200519fceddd58ad10687b" width="1728" height="1086" data-path="img/AutomationCanvas/SharedWithWorkSpaces.png" />
    </Frame>
  </Step>

  <Step title="Set Workflow Connections in Target Workspace">
    After sharing, go to each target workspace and set up the required connections for the workflows using the **Set Connection** option. If connections aren't configured, the workflow will show a red error icon and cannot run or be saved.

    <Warning>If connection setup is skipped in the target workspace, workflows will fail to execute and cannot be saved. Always complete connection mapping after sharing. </Warning>

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/eLYFBpTLBELPX82F/img/AutomationCanvas/SetConnection.png?fit=max&auto=format&n=eLYFBpTLBELPX82F&q=85&s=181a413d84764574191675269f569878" width="1728" height="1083" data-path="img/AutomationCanvas/SetConnection.png" />
    </Frame>
  </Step>
</Steps>

***

## Unsharing a Pack with Workspaces

To remove a shared pack from a workspace:

<Steps>
  <Step title="Open the Share Menu">
    Follow steps 1–2 above to access the pack’s sharing options.
  </Step>

  <Step title="Deselect Target Workspace">
    Uncheck the box next to the **workspace** you want to unshare the pack from.
  </Step>

  <Step title="Apply Changes">
    Click the **Apply** button in the bottom-right corner. The pack will be unshared and no longer visible in that workspace.
  </Step>
</Steps>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/eLYFBpTLBELPX82F/img/AutomationCanvas/UnselectSharedPack.png?fit=max&auto=format&n=eLYFBpTLBELPX82F&q=85&s=263d620a2e1b9dace2ffc686dde5279a" width="1728" height="1081" data-path="img/AutomationCanvas/UnselectSharedPack.png" />
</Frame>

***

## Sharing Packs with Sub-Tenants

<Note>**Note**: This option is only available to **Admin Tenants** in multi-tenant environments. If you are not currently using a multi-tenant setup and would like access to this feature, please contact the Blink Customer Success team.</Note>

Admin Tenants can share workflow packs with one or more sub-tenants using the steps below.

<Steps>
  <Step title="Open the Share Menu">
    Locate the pack you want to share. Click the <Icon icon="square-ellipsis-vertical" iconType="solid" /> button in the top-right corner of the pack. Choose the 'Share pack to tenant' option.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/eLYFBpTLBELPX82F/img/AutomationCanvas/ShareMenu.png?fit=max&auto=format&n=eLYFBpTLBELPX82F&q=85&s=d41960bacf8ead392d4fc5402a3464f7" width="1728" height="1081" data-path="img/AutomationCanvas/ShareMenu.png" />
    </Frame>
  </Step>

  <Step title="Choose Sub-Tenants">
    The 'Share Pack with Sub-tenants' wizard will open. Select the checkboxes next to the sub-tenant(s) you want to share the pack with.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/eLYFBpTLBELPX82F/img/AutomationCanvas/SubTenant.png?fit=max&auto=format&n=eLYFBpTLBELPX82F&q=85&s=f949727a00a75abb87d34863255fe936" width="1728" height="1088" data-path="img/AutomationCanvas/SubTenant.png" />
    </Frame>
  </Step>

  <Step title="Choose Workspaces and Apply">
    Select the workspace(s) within the sub-tenant where the pack should be shared, then click 'Apply' in the bottom-right corner.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/eLYFBpTLBELPX82F/img/AutomationCanvas/SharedWithOneSub.png?fit=max&auto=format&n=eLYFBpTLBELPX82F&q=85&s=ea3d5e13b01a2c50d89c277299ca0c28" width="1717" height="1078" data-path="img/AutomationCanvas/SharedWithOneSub.png" />
    </Frame>

    <Tip> **TIP**: Use the search bar at the top of the wizard to quickly find tenants or workspaces.</Tip>
  </Step>

  <Step title="Confirm Share from Your Workspace">
    Once applied, return to your current workspace. You will now see that the pack has been successfully shared with the selected sub-tenant(s).

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/eLYFBpTLBELPX82F/img/AutomationCanvas/SharedByOneTenant.png?fit=max&auto=format&n=eLYFBpTLBELPX82F&q=85&s=f024b77a51df81d8eb73bcd80c35dcba" width="1730" height="1080" data-path="img/AutomationCanvas/SharedByOneTenant.png" />
    </Frame>
  </Step>

  <Step title="View Shared Pack in Sub-Tenant">
    The sub-tenant(s) will also be able to view the pack in their workspace, along with the name of the tenant that shared it.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/eLYFBpTLBELPX82F/img/AutomationCanvas/PackWithSub.png?fit=max&auto=format&n=eLYFBpTLBELPX82F&q=85&s=01e99b03ea9d1e0cc600136f1eed0d98" width="1728" height="1085" data-path="img/AutomationCanvas/PackWithSub.png" />
    </Frame>
  </Step>
</Steps>

***

## Unsharing a Pack with Sub-Tenants

To remove a pack from a sub-tenant:

<Steps>
  <Step title="Reopen the Sub-Tenant Share Wizard">
    Repeat steps 1 and 2 from the sharing process to access the **Share Pack with Sub-tenants** wizard.
  </Step>

  <Step title="Deselect Sub-Tenants">
    Uncheck the box next to the tenant(s) you want to unshare the pack from.
  </Step>

  <Step title="Finish to Apply Changes">
    Click the 'Finish' button in the bottom-right corner to apply the changes.
  </Step>
</Steps>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/eLYFBpTLBELPX82F/img/AutomationCanvas/DeselectTenants.png?fit=max&auto=format&n=eLYFBpTLBELPX82F&q=85&s=16df8d1b8e4be74f195b290cf2762c5f" width="1728" height="1085" data-path="img/AutomationCanvas/DeselectTenants.png" />
</Frame>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.