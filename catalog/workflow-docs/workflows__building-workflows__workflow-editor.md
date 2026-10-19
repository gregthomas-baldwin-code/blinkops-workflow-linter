> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# The Workflow Editor

> Navigate and use the Blink workflow editor to build, configure, and test automated workflows.

The **Workflow Editor** is the core visual interface for building automated security workflows in Blink. It allows you to create custom workflows by combining [Blink actions](/docs/integrations/blink/actions) with actions from [third-party integrations](/docs/integrations/integrations) —enabling you to automate routine tasks, respond to incidents, and standardize security processes across your organization.
The Workflow Editor lets you go from idea to automation in seconds. With a visual, no-code interface and low-code flexibility when needed, you can quickly build and customize workflows to match your exact security needs. Drag and drop actions, configure triggers, and define logic—all without writing code. And when you do want to go deeper, the [Builder Copilot](/docs/builder-copilot/builder-copilot) is there to help generate and build workflows so your team can automate faster, smarter, and with confidence.
<Note>The new workflow editor is in its beta phase of testing. You can switch between the classic and new editor at any time by clicking the 'Try New Editor' button in the top-right corner of the workflow editor.</Note>

***

## The Workflow Editor's Interface and Features

The following image illustrates the Workflow Editor's Interface and its core features

<Note>**Note:** This image is provided as an example of the Workflow Editor interface. The appearance of your own workflow may vary depending on how you configure your triggers, steps, and actions.</Note>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/3xG_00jOHqxhS9mc/img/Automations/WorkflowEditorFeaturesNew.png?fit=max&auto=format&n=3xG_00jOHqxhS9mc&q=85&s=d50a839a92d0b67cc2e2f425e16ab29c" width="1728" height="1077" data-path="img/Automations/WorkflowEditorFeaturesNew.png" />
</Frame>

These components are as described in the following table:

<div className="integrations-table">
  | | Component | Description |
  | - | - | - |
  | 1 | **[The Action Panel](/docs/workflows/building-workflows/actions/actions)** | This panel on the left lists all available integrations and their respective actions. You can search or scroll to explore actions and drag them into your workflow steps. |
  | 2 | **[Builder Copilot](/docs/builder-copilot/builder-copilot#using-the-builder-copilot-on-an-entire-workflow)** | The 'Builder Copilot' icon opens Builder Copilot. By entering a prompt, the Copilot will assist in reconstructing the **entire** workflow to align as closely as possible with the provided instructions. |
  | 3 | **[The Editor Tab](/docs/workflows/building-workflows/workflow-editor)** and **[The Run Log Tab](/docs/workflows/debugging-workflows/workflow-run-logs)** | Switch between the 'Editor' for designing your workflow and the 'Run Log' to view past executions, inspect inputs/outputs, and troubleshoot errors. |
  | 4 | **[Test Parameters](/docs/workflows/testing-workflows/testing-workflows)** | Use the "Test Parameters" button to provide inputs when testing [on-demand workflows](/docs/workflows/building-workflows/triggers/on-demand-triggers/on-demand-triggers) and [event-based workflows](/docs/workflows/building-workflows/triggers/event-based-triggers/event-based-triggers). Click "Test Run" to execute the workflow in test mode, ideal for validating logic before publishing. |
  | 5 | **[Test Run Button](/docs/workflows/testing-workflows/testing-workflows)** | Click "Test Run" to execute the workflow in test mode, ideal for validating logic before publishing. |
  | 6 | **['All changes saved' indicator](/docs/workflows/building-workflows/workflow-editor#autosave-and-manually-save-workflow-draft) or Manually Saved Draft** | Indicates that all workflow changes have been automatically saved. Select the indicator to view the workflow's version history, or use the adjacent icon to manually save the current state as a new draft version. |
  | 7 | **[Publish and Activate Button](#published-workflows-vs-unpublished-workflows)** | The “Publish & Activate” button is used to publish and activate your workflow the first time. Subsequent publishes will update the version without reactivating the workflow. |
  | 8 | **[Workflow Settings](/docs/workflows/building-workflows/workflow-editor#workflow-editor-settings)** | Opens the Workflow Settings, where you can configure and access workflow properties. |
  | 9 | **Action Button Shortcuts** | Provides quick access to common editor tools, including **[Floating Notes](#comments)** for adding note to the workflow's components, **[Multi-select](/docs/workflows/building-workflows/steps#multiselect-step-and-bulk-actions)** for selecting and managing multiple steps at once, and **Undo/Redo** to quickly revert or reapply changes made during editing. |
  | 10 | **[Trigger Configuration](/docs/workflows/building-workflows/triggers/configuring-triggers)** | Triggers define the conditions under which a workflow is initiated. In this section, you can configure the trigger type selected for the workflow. In the example shown, an [Event-Based Trigger](/docs/workflows/building-workflows/triggers/event-based-triggers/event-based-triggers) is used, which activates the workflow in response to a specific event—such as a [Splunk query result](/docs/integrations/splunk/triggers/new-query-search-event). |
  | 11 | **[Trigger Type](/docs/workflows/building-workflows/triggers/triggers)** | A trigger is an event that starts a workflow in Blink. When a trigger event occurs, Blink automatically executes the workflow based on the selected trigger type: 1. [On Demand Trigger](/docs/workflows/building-workflows/triggers/on-demand-triggers/on-demand-triggers), 2. [Event-Based Triggers](/docs/workflows/building-workflows/triggers/event-based-triggers/event-based-triggers) and [Scheduled Triggers](/docs/workflows/building-workflows/triggers/scheduled-triggers) |
  | 12 | **[Steps](/docs/workflows/building-workflows/steps)** and **[Actions](/docs/workflows/building-workflows/actions/actions)** | Steps are the building blocks of a Workflow and are arranged in a logical order to complete a workflow. Actions are added to a step and perform a defined task based on integration capabilities. |
  | 13 | **[The Inline Action Panel](/docs/workflows/building-workflows/actions/actions)** | The 'Inline Action Panel' appears when adding a new step. It provides quick access to available actions, categorized by integrations, and allows for fast step configuration. |
  | 14 | **[Outputs](/docs/workflows/building-workflows/steps)** | **Outputs** refer to the final results or data generated by a workflow after it runs. These outputs can be used in various ways—for example, passed into [subflows](/docs/workflows/building-workflows/actions/basic-actions/subflow-actions), displayed in the [Self-Service Portal](/docs/blink-platform/blink-portal/blink-portal), or reviewed in the [execution run logs](/docs/workflows/debugging-workflows/workflow-run-logs#viewing-automated-workflow-outputs) for debugging purposes. |
  | 15 | **Toolbar** | This toolbar on the right lets you zoom in/out of the canvas and quickly navigate through complex workflows. It includes reset, expand, collapse and zoom control |
</div>

## Comments

Comments let you add information and context directly to the canvas, making it easier to explain workflow logic, document implementation details, and collaborate with your team.

To enable Comments, click the <Icon icon="sticky-note" /> icon in the top-right corner of the Workflow Editor. Click it again to disable Comments.

You can add comments to the workflow canvas or attach them to specific workflow entities, such as steps, inputs, triggers, and outputs. Use comments to provide guidance or preserve important context.

<Note>Comments added in the Workflow Editor are also stored in the [workflow's YAML structure](/docs/workflows/building-workflows/workflow-yaml). </Note>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/JYZrejEoCY1Hd82o/img/Automations/FloatingNotes.png?fit=max&auto=format&n=JYZrejEoCY1Hd82o&q=85&s=0f4919392ff72a88e15cf76ed72e8e99" width="1721" height="1081" data-path="img/Automations/FloatingNotes.png" />
</Frame>

***

## Adding Actions to Steps

In the editor, you can add actions to a step in one of two ways.

<CardGroup col={2}>
  <Card title="Drag and Drop" icon="computer-mouse">
    To create a step using drag and drop, select an action from the Action Panel on the left and drag it onto the canvas.
  </Card>

  <Card title="Inline Adding" icon="plus">
    <p> Alternatively, click the <Icon icon="plus" color="grey" /> icon in the center of the canvas to open the [inline action panel](#understanding-the-inline-action-panel), choose an action and add it to a step. You can choose from flow control actions, subflow or use the search bar to find a specific action across all integrations. </p>
  </Card>
</CardGroup>

<Frame>
  <video controls autoPlay muted zoom loop allowFullScreen className="w-full aspect-video" src="https://res.cloudinary.com/dsiyoh0ge/video/upload/v1747817027/AddingStepsNew_xlzsvj.mp4" />
</Frame>

<Note> To learn more about how [steps](/docs/workflows/building-workflows/steps) work in the Workflow Editor—including their logic, configuration, and behavior—refer to the [steps documentation](/docs/workflows/building-workflows/steps).</Note>

***

## Understanding the Inline Action Panel

<img src="https://mintcdn.com/blinkops-2/ieTbsV6fIpmAIOOJ/img/Actions/actionpanel.svg?fit=max&auto=format&n=ieTbsV6fIpmAIOOJ&q=85&s=6cc7ff0e37cd34d4858a13deb2bfdb44" width="568" height="256" data-path="img/Actions/actionpanel.svg" />

<Tip><p>Click the <Icon icon="circle-chevron-down" color="grey" /> button, to view all available options in the Action Panel.</p></Tip>

When you click the <Icon icon="plus" color="grey" /> icon in the center of the canvas, the **Action Panel** opens. This panel lets you add new steps to your workflow and is divided into the following sections:

1. **Search Bar** – Quickly locate a specific action by typing its name into the search bar.

2. **[The Builder Copilot](/docs/builder-copilot/builder-copilot)** - Your AI assistant for building step logic. Use Builder Copilot to describe what you want to achieve in the step, and it will suggest the right action for you. You can add a single step or multiple steps.
   <Tip> In the Blink Builder, while you can use the Copilot at the workflow level, we recommend adding dedicated step(s) instead. Using Copilot at the workflow level applies changes globally, which can override downstream behavior and lead to unintended results—especially in complex workflows. For a more modular and iterative approach, use Copilot to add logic at the step level, where changes are more targeted and controlled.</Tip>

3. **[Actions](/docs/workflows/building-workflows/actions/actions)**\
   A categorized list of all available actions you can use in your workflow:
   * **All Actions**: Browse the complete library of Blink’s built-in actions.
   * **[Utility Actions](/docs/workflows/building-workflows/actions/actions#action-types)**: General-purpose actions like formatting text, transforming data, or waiting for a specified duration.
   * **[Subflows](/docs/workflows/building-workflows/actions/basic-actions/subflow-actions)**:
     * Subflows are reusable [on-demand workflows](/docs/workflows/building-workflows/triggers/on-demand-triggers/on-demand-triggers) that can be called as a step from other workflows. They help modularize your automation logic, reduce duplication, and simplify maintenance.

4. **[Agents](/docs/agent-builder/agent-builder)**- All your custom built [Agents](/docs/agent-builder/building-the-agent)
   <Tip>Agent features are available in the action panel only if they have been enabled for your workspace. This configuration can be performed by users with the [Tenant Admin](/docs/blink-platform/account-management/roles#1-admin) user role.</Tip>

5. **[Flow Control Actions](/docs/workflows/building-workflows/actions/basic-actions/flow-control-actions)**
   * These actions help define the logic and structure of your workflow. Use them to add conditions, loops, parallel branches, or control how and when different parts of your workflow are executed.

***

## Workflow Editor Settings

<p> In the top-right corner of the Workflow Editor, you can access the setting by clicking on the <Icon icon="square-ellipsis-vertical" iconType="solid" /> menu and choosing from the following </p>

1. [Edit Yaml](/docs/workflows/building-workflows/workflow-yaml)- Open the `YAML` view of your workflow and make any desired changes.
2. [Download YAML](/docs/workflows/building-workflows/workflow-yaml#download-yaml-format-of-a-workflow)- Download your workflow in YAML format.
3. [Settings](/docs/workflows/managing-workflows/workflow-overview-page) - This opens the Workflow Overview page. Manage workflow-level settings such as its name, description, tags, or visibility settings.
4. [Version History](/docs/workflows/managing-workflows/workflow-version-history)- View and manage the workflow’s version history. You can compare changes, see timestamps, and restore previous versions if needed.

<Frame>
  <img src="https://mintcdn.com/blinkops-2/a1x5rkcHl8cjjsSc/img/Automations/EditorSettingsNew.png?fit=max&auto=format&n=a1x5rkcHl8cjjsSc&q=85&s=e32817f2e8ec258e29203a4b52a485ba" width="1728" height="1080" data-path="img/Automations/EditorSettingsNew.png" />
</Frame>

***

## Autosave and Manually Save Workflow Draft

When you make changes to a workflow in the Workflow Editor:

1. **Your changes are automatically saved by the system**
   * To view the timestamp of your most recent update, hover over the *All Changes Saved* indicator in the top-right corner. Clicking this indicator opens the [version history](/docs/workflows/managing-workflows/workflow-version-history), where you can review previous versions or restore a prior state if needed.
   * If the workflow fails to save (for example, due to a lost internet connection), the autosave indicator will change to *Not Saved*. Hover over it to view additional details, if available.

<Frame>
  <img src="https://mintcdn.com/blinkops-2/a1x5rkcHl8cjjsSc/img/Automations/AutosaveNew.png?fit=max&auto=format&n=a1x5rkcHl8cjjsSc&q=85&s=c23648f7e88027716162accb9ccc7476" width="1728" height="1079" data-path="img/Automations/AutosaveNew.png" />
</Frame>

2. **You can also manually save a draft version**
   * Click the <Icon icon="save" /> icon next to the Publish button, then enter a version name and an optional description. This will create a new draft version of the workflow.

<Note>**Note**: To avoid conflicts or potential loss of work, please be aware that concurrent editing is restricted. If a user is currently working in the editor, others will be unable to edit the same workflow to ensure a seamless process.</Note>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/y1nmLcoC3RqwQdln/img/Automations/ManuallySave.png?fit=max&auto=format&n=y1nmLcoC3RqwQdln&q=85&s=0c43d4738fbb38d430fa14d089c62459" width="1728" height="1082" data-path="img/Automations/ManuallySave.png" />
</Frame>

***

## Published Workflows Vs Unpublished Workflows

When managing workflows, it is essential to differentiate between published and unpublished workflow versions. Unpublished workflows represent draft versions with changes that have not been published yet, while published workflows are finalized and ready for execution. You can identify the status of a workflow in multiple places: the workflow list, the workflow overview page, or the workflow editor.

<Tip>
  To learn more about how to control the availability of a published workflow, check out the documentation [here](/docs/workflows/managing-workflows/draft-published).
</Tip>

You can distinguish between a published and an unpublished workflow by looking at the:

<Accordion title="The Workflow Editor" icon="circle-1">
  [The Workflow Editor](/docs/workflows/building-workflows/workflow-editor): Within the Workflow Editor, hover over the Published button. If there are unpublished changes, a notification will appear, stating that certain changes are not included in the published version. You can also access the Version History to review all changes made to the workflow.

  <Frame>
    <img src="https://mintcdn.com/blinkops-2/s_B_vBsuBTungkU8/img/Automations/UnpublishedChangesNew.png?fit=max&auto=format&n=s_B_vBsuBTungkU8&q=85&s=aad7470bab8a135944dd0abac8120471" width="1727" height="1079" data-path="img/Automations/UnpublishedChangesNew.png" />
  </Frame>
</Accordion>

<Accordion title="The Workflows Page" icon="circle-2">
  * A yellow dot (<Icon icon="circle" color="#e7a235" iconType="solid" size={7} />) appears on the left-hand side of any workflow with unpublished changes. This serves as a quick visual indicator that a newer draft version exists.

      <Frame>
        <img src="https://mintcdn.com/blinkops-2/xnKigMZdVI45SQhn/img/Automations/OrangeDot.png?fit=max&auto=format&n=xnKigMZdVI45SQhn&q=85&s=219ba7e06ebe1214f62eb40391bc7978" width="3584" height="2056" data-path="img/Automations/OrangeDot.png" />
      </Frame>
</Accordion>

<Accordion title="The Workflow Overview Page" icon="circle-3">
  [The Workflow Overview Page](/docs/workflows/managing-workflows/workflow-overview-page): To view more details, select the workflow and click the Overview button. On the Workflow Overview page, you will see a notification at the bottom highlighting that unpublished changes exist. Additionally, you’ll find an option to view the latest draft of the workflow for further details.

  <Frame>
    <img src="https://mintcdn.com/blinkops-2/4a8dMD2Jv5wsADYv/img/Automations/DraftVersionDetailsNew.png?fit=max&auto=format&n=4a8dMD2Jv5wsADYv&q=85&s=ee87d95204bf2626cda834d01df64505" width="1727" height="1081" data-path="img/Automations/DraftVersionDetailsNew.png" />
  </Frame>
</Accordion>

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