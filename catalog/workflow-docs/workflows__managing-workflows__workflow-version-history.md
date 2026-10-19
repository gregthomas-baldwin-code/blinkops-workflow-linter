> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Workflow Version History

> Track and manage workflow version history to review changes and restore previous versions in Blink.

The Workflow Version History feature provides a complete record of every change made to a workflow from the moment it’s created. It lets you review past changes, compare any two versions side by side, and, when necessary, restore a previous version to revert unwanted changes or recover a stable state.

<Frame>
  <img src="https://mintcdn.com/blinkops-2/m23gCXrNxzZosSUE/img/Automations/version-history-pages.png?fit=max&auto=format&n=m23gCXrNxzZosSUE&q=85&s=990afd14df8b88095e89282d271fcf08" width="1728" height="1081" data-path="img/Automations/version-history-pages.png" />
</Frame>

***

To access the **Version History** feature, click the <Icon icon="square-ellipsis-vertical" iconType="solid" /> menu icon in the top-right corner of the workflow editor and select the "Version History" option or you can click the "All changes saved" link, and you will be redirected to the version history interface.

<Frame>
  <img src="https://mintcdn.com/blinkops-2/EyvCebRY_N-OMntw/img/Automations/AccessVersionHistory.png?fit=max&auto=format&n=EyvCebRY_N-OMntw&q=85&s=b1e990035249cd5cdfd9191174fe42d2" width="1728" height="1086" data-path="img/Automations/AccessVersionHistory.png" />
</Frame>

***

## Workflow Version History Timeline

The left-hand sidebar presents a complete timeline of all workflow versions, showing when each change was made, who made it, and which versions were published, including the currently published and active workflow version. This gives you clear visibility into how the workflow has evolved over time and makes it easy to track changes and contributions.

<Frame>
  <img src="https://mintcdn.com/blinkops-2/GqTIYEgYxsTXZgXu/img/Automations/WorkflowDetails.png?fit=max&auto=format&n=GqTIYEgYxsTXZgXu&q=85&s=25c295194a5e25da166c38ca2ef82460" width="1728" height="1093" data-path="img/Automations/WorkflowDetails.png" />
</Frame>

***

### Restoring a Workflow Version

Hover over a workflow in the left-hand sidebar and click the <Icon icon="square-ellipsis-vertical" iconType="solid" /> menu. A dialog box will appear, giving you the option to Restore a specific version of the workflow. This is useful if you need to revert to a previous state after making changes or to recover an earlier configuration.

By selecting the **Restore** option, you will be taken to the workflow editor with the restored version of the chosen workflow version. Here, you can make any necessary edits and save the selected workflow version as a draft or publish it.

<Frame>
  <img src="https://mintcdn.com/blinkops-2/m23gCXrNxzZosSUE/img/Automations/version-options.png?fit=max&auto=format&n=m23gCXrNxzZosSUE&q=85&s=5ea9386d918820f5f85c74b95c382042" width="1718" height="1084" data-path="img/Automations/version-options.png" />
</Frame>

***

### Add Version Description

<Steps>
  <Step>
    Hover over the workflow in the left-hand sidebar, click the <Icon icon="square-ellipsis-vertical" iconType="solid" /> menu, and select 'Add Version Description'.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/q8OWlsWmXsmoFXZL/img/Automations/EditVersionDescription.png?fit=max&auto=format&n=q8OWlsWmXsmoFXZL&q=85&s=3846fba5c9fe4091b468b938c35665fa" width="1718" height="1084" data-path="img/Automations/EditVersionDescription.png" />
    </Frame>
  </Step>

  <Step>
    In the dialog box, provide a name and write a brief description for the selected workflow version. This helps track changes and understand the purpose of each version.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/EyvCebRY_N-OMntw/img/Automations/AddVersionDescription.png?fit=max&auto=format&n=EyvCebRY_N-OMntw&q=85&s=63ed9443348131bd742a2c3e33f8237b" width="3440" height="2208" data-path="img/Automations/AddVersionDescription.png" />
    </Frame>
  </Step>

  <Step>
    Once entered, the description will be saved and associated with the selected workflow version, making it easy to identify later.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/q8OWlsWmXsmoFXZL/img/Automations/DescriptionAdded.png?fit=max&auto=format&n=q8OWlsWmXsmoFXZL&q=85&s=a238f45b277a91333dbd0cf936940343" width="1728" height="1083" data-path="img/Automations/DescriptionAdded.png" />
    </Frame>
  </Step>
</Steps>

***

## Highlight Changes, Compare and Sync Scrolling

<Tip>You can also select the checkboxes for all three features to enable them at the same time.</Tip>

### Highlight Changes

Selecting the 'Highlight Changes' checkbox will display the differences between the selected workflow version and the workflow version immediately preceding it.

* **<Badge color="green" size="sm">Green</Badge>** – Indicates a new step, input, or output has been added to the workflow.
* **<Badge color="blue" size="sm">Blue</Badge>** – Shows that an existing step, connection, step setting, input, or output has been modified.
* **<Badge color="red" size="sm">Red</Badge>** – Signifies that a step, input, or output has been removed.

<Tip>When changes to a step setting have been made, a special indicator will reflect a change has been made. </Tip>

The Status Indicator Bar provides a quick overview of the current state of the selected workflow version. It highlights key details, including:

* **Workflow Version Name** – Displays the name of the workflow version you are currently viewing or editing.
  * If the name has been modified, it is marked with an 'Updated' status to indicate pending changes.
* **Step Changes Summary** - How many steps, in the selected workflow version, were <Icon icon="circle-small" color="#18a0fb" iconType="solid" /> changed, <Icon icon="circle-small" color="#4fd16b" iconType="solid" /> added, or <Icon icon="circle-small" color="#e73c2e" iconType="solid" /> deleted.
* **Trigger** – Indicates whether the workflow trigger has changed.
  * A *'No changes'* status means the trigger remains the same
  * An 'Updated' indicator confirms that changes were made to the trigger configuration or that the trigger type was modified.
* **Inputs and Outputs** – Indicates whether any workflow inputs or outputs were added, removed, updated, reconfigured, or reordered.

<Frame>
  <img src="https://mintcdn.com/blinkops-2/m23gCXrNxzZosSUE/img/Automations/highlight-changes.png?fit=max&auto=format&n=m23gCXrNxzZosSUE&q=85&s=b848ccb3023ffbb3e131e669a40194c9" width="1728" height="1094" data-path="img/Automations/highlight-changes.png" />
</Frame>

***

### Compare

Selecting the 'Compare' checkbox enables a side-by-side comparison of two different workflow versions. When comparison mode is active, each version is clearly labeled with a **Newer** or **Older** indicator, making it easy to identify which version is the most recent and which represents the previous state. It also displays when the changes were made, who saved them, and whether the selected version has been published.

<Tip> Simply check the boxes for the workflow's versions you want to compare.</Tip>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/EyvCebRY_N-OMntw/img/Automations/CompareWorkflowVersions.png?fit=max&auto=format&n=EyvCebRY_N-OMntw&q=85&s=dd0bed68d610f7577711a01f0e930dcb" width="1726" height="1108" data-path="img/Automations/CompareWorkflowVersions.png" />
</Frame>

***

### Highlight and Compare Code Actions

In any [code action](/docs/workflows/building-workflows/actions/basic-actions/code-actions) or workflow actions that contains code or script, you can easily track changes made to your code, line by line.

* **<Badge color="green" size="sm">Green</Badge>** – Highlights lines of code that have been **added**.
* **<Badge color="red" size="sm">Red</Badge>** – Highlights lines of code that have been **removed**.

<Frame>
  <img src="https://mintcdn.com/blinkops-2/KbCR2JdZNrCqh8Nz/img/Automations/CompareCodeActions.png?fit=max&auto=format&n=KbCR2JdZNrCqh8Nz&q=85&s=fac76e37d4177b5f7cc9a4abee5e805a" width="1728" height="1093" data-path="img/Automations/CompareCodeActions.png" />
</Frame>

By clicking the <Icon icon="expand" /> icon, you can choose between two ways to view these changes:

1. **Unified Mode** – Displays all additions and deletions together in a single view.

<Frame>
  <img src="https://mintcdn.com/blinkops-2/ZnkNP7xHllEhfP_s/img/Automations/UnifiedMode.png?fit=max&auto=format&n=ZnkNP7xHllEhfP_s&q=85&s=1ed5be2d0224d8a3723a73af585f92ea" width="3420" height="2130" data-path="img/Automations/UnifiedMode.png" />
</Frame>

2. **Split Mode** – Shows the original code and the updated code side by side, making it easier to compare changes line by line.

<Frame>
  <img src="https://mintcdn.com/blinkops-2/KbCR2JdZNrCqh8Nz/img/Automations/SplitMode.png?fit=max&auto=format&n=KbCR2JdZNrCqh8Nz&q=85&s=aa79151078b483883ef68053719ed657" width="3428" height="2152" data-path="img/Automations/SplitMode.png" />
</Frame>

***

### Sync Scrolling

The Sync Scrolling feature can only be enabled when the Compare option is selected. When the 'Sync Scroll' option is selected, it keeps both workflow versions aligned as you scroll.

<iframe src="https://player.cloudinary.com/embed/?cloud_name=dsiyoh0ge&public_id=SyncScrolling_vqgukv&profile=cld-looping" width="640" height="360" allowfullscreen="true" frameborder="0" />

***


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.