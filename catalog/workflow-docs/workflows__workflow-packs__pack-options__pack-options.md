> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Pack Options

> Overview of available options for managing and organizing workflow packs in Blink.

Packs offer a flexible way to organize and manage your workflows across different environments. Depending on your use case, whether you are collaborating across workspaces, maintaining version control, or distributing workflows to customers—there are several options available for how you interact with and manage Packs.

Use this guide to understand the available Pack options and determine which one best fits your needs:

<CardGroup>
  <Card title="Copy/Move Packs" icon="circle-1" href="/docs/workflows/workflow-packs/pack-options/copy-moving-packs" iconType="solid" horizontal />

  <Card title="Copy/Move Workflows" icon="circle-4" href="/docs/workflows/workflow-packs/pack-options/move-or-copy-workflows" iconType="solid" horizontal />

  <Card title="Share Packs to a different Workspace" icon="circle-2" href="/docs/workflows/workflow-packs/pack-options/sharing-packs" iconType="solid" horizontal />

  <Card title="Deploy Pack to Workspace" icon="circle-5" href="/docs/workflows/workflow-packs/pack-options/deploy-pack" iconType="solid" horizontal />

  <Card title="Share Packs with Sub-Tenants" icon="circle-3" href="/docs/workflows/workflow-packs/pack-options/sharing-packs#sharing-packs-with-sub-tenants" iconType="solid" horizontal />
</CardGroup>

***

## Choosing the Right Pack Option

Each Pack option serves a different purpose depending on how you want to manage, share, or migrate your workflows. Whether you're organizing workflows within a workspace, distributing them across tenants, or setting up a deployment pipeline between environments—this section will help you understand which action to take.

***

### Copy/Move Workflows

The [Copy/Move Workflows](/docs/workflows/workflow-packs/pack-options/move-or-copy-workflows) feature is a good option to choose when you would like to copy or move a workflow to a different pack in the same or different workspace.

***

### The Copy/Move Pack

The [Copy/Move Packs](/docs/workflows/workflow-packs/pack-options/copy-moving-packs) feature is a good option to choose when you would like to copy a pack and its workflow(s) to a different target workspace or you would like to move a pack and its workflow(s) from its original workspace to a different target workspace. You also have the option to edit the pack's workflow(s) in the editors tab in both the original workspace and the target workspace.

***

### Share Packs to Different Workspaces

* The [Share Packs to a different Workspace](/docs/workflows/workflow-packs/pack-options/sharing-packs) feature is a good option to choose when you would like manage a pack in one central workspace, but deploy it for use in multiple workspaces. Each workspace the pack is shared to, may have different connections used on the same workflows.

* The [Share Packs to a different Workspace](/docs/workflows/workflow-packs/pack-options/sharing-packs) feature is a good option to choose because it makes workflows in shared packs on the target workspace a read-only state. This helps keep a consistent logic across all workspaces and ensures that important workflows stay safe and unchanged.

***

### Share Packs with Sub-Tenants

The [Share Packs with Sub-Tenants](/docs/workflows/workflow-packs/pack-options/sharing-packs#sharing-packs-with-sub-tenants) feature is a good option to choose if you are an **Admin Tenant** managing customers in multiple different tenants and you would like to share the pack from your workspace with one or more sub-tenants.

***

### Deploy Pack to Workspace

<Note>**Note**: Please note that this feature is limited and only accessible to customers upon request </Note>

* The [Deploy Pack to Workspace](/docs/workflows/workflow-packs/pack-options/deploy-pack) feature retains the metadata of the workflow(s) in the **target** pack, including their share state, activation state, and connection mapping.

* The [Deploy Pack to Workspace](/docs/workflows/workflow-packs/pack-options/deploy-pack) feature is a good option to choose when you want to create a deployment pipeline for your pack's workflow between its development and production stages. It allows you to work on your workflow in a development/test environment and then once the workflow is ready and finalized it allows you to deploy your pack to the **target workspace**.

***


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.