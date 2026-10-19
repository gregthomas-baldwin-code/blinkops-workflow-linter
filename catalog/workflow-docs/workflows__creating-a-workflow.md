> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating a New Workflow

> How to create a new workflow in Blink using Builder Copilot or the manual workflow editor.

When creating a new automated workflow, you have two options:

<CardGroup col={2}>
  <Card title="Create a Workflow using the Builder Copilot" icon="robot" href="#create-a-workflow-using-the-builder-copilot">
    You can use the Builder Copilot to quickly generate and build a workflow using AI assistance.
  </Card>

  <Card title="Create a Workflow from Scratch" icon="wrench" href="#create-a-workflow-from-scratch">
    You can configure and build a workflow entirely from scratch, allowing you to customize every step and logic to fit your specific needs.
  </Card>
</CardGroup>

***

## Create a Workflow using the Builder Copilot

<Note>
  For more details on how to use the Builder Copilot—including its features and capabilities—refer to the [Builder Copilot documentation](/docs/builder-copilot/builder-copilot).
</Note>

<Steps>
  <Step title="Select or Create a Pack">
    Start by selecting an existing [Pack](/docs/workflows/workflow-packs/pack-management) or creating a new one. This is where your new workflow will be located.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/eLYFBpTLBELPX82F/img/AutomationCanvas/ChoosePack.png?fit=max&auto=format&n=eLYFBpTLBELPX82F&q=85&s=b163dadbac58319d4adf8ef764f056ce" width="1728" height="1078" data-path="img/AutomationCanvas/ChoosePack.png" />
    </Frame>
  </Step>

  <Step title="Create a New Workflow">
    In the top-right corner of the selected Pack, click 'New Workflow' to begin creating your workflow.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/eLYFBpTLBELPX82F/img/AutomationCanvas/NewAutomation.png?fit=max&auto=format&n=eLYFBpTLBELPX82F&q=85&s=5835f19396b06524552817ea1b7a6a3c" width="1720" height="1075" data-path="img/AutomationCanvas/NewAutomation.png" />
    </Frame>
  </Step>

  <Step title="Provide a Prompt to Builder Copilot">
    A dialog box will appear where you can enter a prompt describing the workflow you would like to create.

    <Tip>Provide clear and specific instructions for the Builder Copilot to receive the best results.</Tip>

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/eLYFBpTLBELPX82F/img/AutomationCanvas/Prompt.png?fit=max&auto=format&n=eLYFBpTLBELPX82F&q=85&s=5633d7f0b177f049a5e7b2f8daad12cf" width="3450" height="2162" data-path="img/AutomationCanvas/Prompt.png" />
    </Frame>
  </Step>

  <Step title="Generate the Workflow">
    After you have finished providing instructions for Builder Copilot, click on the 'Generate Workflow' button located in the bottom-right corner. The generation process may take a few seconds.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/eLYFBpTLBELPX82F/img/AutomationCanvas/LoadingPrompt.png?fit=max&auto=format&n=eLYFBpTLBELPX82F&q=85&s=16e177b1e3cf60b4308cce95f105c679" width="3455" height="1690" data-path="img/AutomationCanvas/LoadingPrompt.png" />
    </Frame>
  </Step>

  <Step title="Review and Refine the Workflow">
    Once the generation is complete, you will see a preview screen:

    * **Left panel**: Your original prompt (double-click to edit and regenerate).
    * **Right panel**: The workflow the Builder Copilot has created.
    * **Advanced options**: Add a description and tags for easier management later.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/zlMo8eiArHkFpK8P/img/AutomationCanvas/PreviewPromptAdvanced.png?fit=max&auto=format&n=zlMo8eiArHkFpK8P&q=85&s=4414f033264523caa8ae606b189fe5af" width="3452" height="2156" data-path="img/AutomationCanvas/PreviewPromptAdvanced.png" />
    </Frame>
  </Step>

  <Step title="Finalize in the Workflow Editor">
    You will be redirected to the Workflow Editor where you have the option to:

    * Modify or improve the generated logic either by using the [Builder Copilot](/docs/builder-copilot/builder-copilot) or by editing it manually to suit your needs.
    * [Test your workflow](/docs/workflows/testing-workflows/testing-workflows)

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/zlMo8eiArHkFpK8P/img/AutomationCanvas/FinalCanvas.png?fit=max&auto=format&n=zlMo8eiArHkFpK8P&q=85&s=7ab47d0ec7043d02937bedaf2e5e2a90" width="3448" height="2152" data-path="img/AutomationCanvas/FinalCanvas.png" />
    </Frame>
  </Step>

  <Step title="Publish the Workflow">
    Use the 'Publish & Activate' button to publish and activate your workflow for the first time. After the initial activation, any future changes you publish will simply update the most recent workflow version—without reactivating it.

    To learn more about the difference between published workflows and unpublished workflows, check out the documentation [here](/docs/workflows/building-workflows/workflow-editor#published-workflows-vs-unpublished-workflows).

    <Note> Only users with the [Owner user role](/docs/blink-platform/account-management/roles#1-owner), [Contributor user role](/docs/blink-platform/account-management/roles#2-contributor), or a custom role with the `workflow:publish` permission can publish workflows. To learn more about approving and publishing workflows, check out the documentation [here](/docs/workflows/managing-workflows/publish-approval/publish-approval). </Note>

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/zlMo8eiArHkFpK8P/img/AutomationCanvas/PublishButton.png?fit=max&auto=format&n=zlMo8eiArHkFpK8P&q=85&s=5a0c346986ee12dd516d528591d7ef30" width="1724" height="1076" data-path="img/AutomationCanvas/PublishButton.png" />
    </Frame>
  </Step>
</Steps>

***

## Create a Workflow from Scratch

<Steps>
  <Step title="Select or Create a Pack">
    Start by selecting an existing [Pack](/docs/workflows/workflow-packs/pack-management) or creating a new one. This is where your new workflow will be located.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/eLYFBpTLBELPX82F/img/AutomationCanvas/ChoosePack.png?fit=max&auto=format&n=eLYFBpTLBELPX82F&q=85&s=b163dadbac58319d4adf8ef764f056ce" width="1728" height="1078" data-path="img/AutomationCanvas/ChoosePack.png" />
    </Frame>
  </Step>

  <Step title="Create a New Workflow">
    In the top-right corner of the selected Pack, click 'New Workflow' to begin creating your workflow.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/eLYFBpTLBELPX82F/img/AutomationCanvas/NewAutomation.png?fit=max&auto=format&n=eLYFBpTLBELPX82F&q=85&s=5835f19396b06524552817ea1b7a6a3c" width="1720" height="1075" data-path="img/AutomationCanvas/NewAutomation.png" />
    </Frame>
  </Step>

  <Step title="Open the Workflow Editor">
    In the setup screen, click **Continue to Editor** in the bottom-right corner. This will take you to the Workflow Editor, where you can begin building your workflow from scratch.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/eLYFBpTLBELPX82F/img/AutomationCanvas/ContinueToEditor.png?fit=max&auto=format&n=eLYFBpTLBELPX82F&q=85&s=252b83c44c46a85d7b67823e170d8299" width="1728" height="1082" data-path="img/AutomationCanvas/ContinueToEditor.png" />
    </Frame>
  </Step>

  <Step title="Configure Workflow Settings">
    Before entering the editor, configure the workflow settings:

    <Tip>
      You can proceed with this step using the default values and make changes at a later stage, if needed.
    </Tip>

    <div className="integrations-table">
      | Parameter | Description | Default Value |
      | - | - | - |
      | **Name** | Enter a clear, descriptive name for your workflow. | New Workflow |
      | **[Pack](/docs/workflows/workflow-packs/workflow-packs)** | Select the Workflow Pack where this workflow will live. Packs help organize related workflows. | The Selected Pack |
      | **Icon** | Assign an icon to visually identify your workflow. | N/A |
      | **Trigger Type** | Choose how the workflow is triggered: via an [Event-Based Trigger](/docs/workflows/building-workflows/triggers/event-based-triggers/event-based-triggers), an [On-Demand Trigger](/docs/workflows/building-workflows/triggers/on-demand-triggers/on-demand-triggers), or a [Scheduled Trigger](/docs/workflows/building-workflows/triggers/scheduled-triggers). | On-Demand Trigger |
      | **Advanced – Description** | Provide a short summary of the workflow’s purpose and behavior. | N/A |
      | **Advanced – Tags** | Add tags to help categorize and filter your workflow within the platform. | N/A |
      | **Advanced – [Run Environment](/docs/blink-platform/runners/runners)** | Choose the runner environment that will execute the workflow steps. | [Blink Cloud](/docs/blink-platform/runners/runners#how-runners-work). |
    </div>

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/eLYFBpTLBELPX82F/img/AutomationCanvas/ConfigureSettings.png?fit=max&auto=format&n=eLYFBpTLBELPX82F&q=85&s=1bdb60060656af33cb2c118b3c7dffb8" width="3444" height="2162" data-path="img/AutomationCanvas/ConfigureSettings.png" />
    </Frame>
  </Step>

  <Step title="Build Your Workflow">
    Once you have completed the setup, you will be directed to the [Workflow Editor](/docs/workflows/building-workflows/workflow-editor). From here, you can build your workflow accordingly.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/zlMo8eiArHkFpK8P/img/AutomationCanvas/WorkflowEditor.png?fit=max&auto=format&n=zlMo8eiArHkFpK8P&q=85&s=defe8c9d86c60fc4d15ed775c1cb32b8" width="3452" height="2154" data-path="img/AutomationCanvas/WorkflowEditor.png" />
    </Frame>
  </Step>

  <Step title="Publish the Workflow">
    Use the 'Publish & Activate' button to publish and activate your workflow for the first time. After the initial activation, any future changes you publish will simply update the most recent workflow version—without reactivating it.

    To learn more about the difference between published workflows and unpublished workflows, check out the documentation [here](/docs/workflows/building-workflows/workflow-editor#published-workflows-vs-unpublished-workflows).

    <Note> Only users with the [Owner user role](/docs/blink-platform/account-management/roles#1-owner), [Contributor user role](/docs/blink-platform/account-management/roles#2-contributor), or a custom role with the `workflow:publish` permission can publish workflows. To learn more about approving and publishing workflows, check out the documentation [here](/docs/workflows/managing-workflows/publish-approval/publish-approval). </Note>

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/zlMo8eiArHkFpK8P/img/AutomationCanvas/FinalVersion.png?fit=max&auto=format&n=zlMo8eiArHkFpK8P&q=85&s=852ccf0ac433a501b0b2cf4959313bd0" width="1725" height="1081" data-path="img/AutomationCanvas/FinalVersion.png" />
    </Frame>
  </Step>
</Steps>

***

## Best Practices

<Accordion title="Workflow Creation Best Practices" icon="">
  Follow these best practices when creating workflows in Blink to build automated workflows that are secure, reliable, easy to troubleshoot, and maintainable.

  Whether you're creating your first workflow or building a complex automated workflows across multiple workspaces, these guidelines can help ensure your workflows are easy to understand and maintain.

  **1. Plan Your Workflow Before You Build**

  Before adding [steps](/docs/workflows/building-workflows/steps) to the [Workflow Editor](/docs/workflows/building-workflows/workflow-editor), define what the workflow should accomplish.

  Consider the following:

  * **What should trigger the workflow?**
  * **What should the workflow do?**
  * **What information does it need?**
  * **What systems does it need to interact with?**
  * **What should happen if a step fails?**
  * **What should the final outcome be?**

  A clear objective helps you determine the appropriate trigger, actions, variables, and flow controls before you start building.

  **Keep workflows focused**

  A workflow should have a clear and specific purpose.

  Avoid combining unrelated processes into a single workflow. If a workflow becomes difficult to understand or contains large amounts of unrelated logic, consider whether it can be divided into smaller workflows or reusable components.

  A well-designed workflow should be easy for another user to understand by reviewing the workflow canvas.

  ***

  **2. Build and Test Incrementally**

  Build your workflow step by step rather than creating the entire workflow before testing it.

  A recommended approach is:

  1. Configure the [trigger](/docs/workflows/building-workflows/triggers/configuring-triggers).
  2. Add the first [action](/docs/workflows/building-workflows/actions/actions).
  3. Test the step and review its output.
  4. Add the next [action](/docs/workflows/building-workflows/actions/actions).
  5. Pass values between steps using [dynamic variables](/docs/workflows/building-workflows/dynamic-variables/variable-picker).
  6. Add conditions or other flow controls where needed.
  7. [Test the workflow](/docs/workflows/testing-workflows/testing-workflows) again.
  8. Add appropriate [error handling](/docs/workflows/building-workflows/error-handling/error-handling).
  9. Review the completed workflow.
  10. Publish the workflow when it is ready.

  Testing as you build makes it easier to identify which step is causing an issue.

  ***

  Use [dynamic variables](/docs/workflows/building-workflows/dynamic-variables/variable-picker) whenever a value should come from the workflow rather than being manually entered.

  [Dynamic variables](/docs/workflows/building-workflows/dynamic-variables/variable-picker#dynamic-variables-types) can reference information such as:

  * Step outputs
  * Input parameters (only available in On-Demand Workflows)
  * Event data
  * Local variables
  * Global variables
  * Workflow metadata

  Use the **[Variable Picker](/docs/workflows/building-workflows/dynamic-variables/variable-picker#using-the-variable-picker-to-add-dynamic-variables)** whenever possible to select available values instead of manually entering complex variable expressions. This helps reduce syntax errors and makes it easier to identify the data available at each point in the workflow.

  **Do**

  Use a [dynamic value](/docs/workflows/building-workflows/dynamic-variables/variable-picker) when the value can change between workflow executions.

  For example, if a workflow should operate on whichever user triggered an event, use the user information from the event rather than entering a specific username.

  Use variables when a value is reused across multiple steps or needs to be referenced later. For example, storing a shared threshold or environment name in a variable allows you to update it in one place.

  **Don't**

  Hardcode values that should be determined at runtime.

  For example, avoid:

  ```text theme={"dark"}
  user@example.com
  ```

  if the workflow should operate on different users.

  **Avoid unnecessary variables**

  Don't create variables simply to pass a value between steps. If a value can be referenced directly from a previous step, reference it directly instead.

  **Keep variable types consistent**

  Avoid reusing the same variable for values with different data types or purposes. Assigning a different data type to an existing variable can result in unexpected behavior. Use separate variables with clear, descriptive names when values have different data types or purposes.

  **Inspect variables when needed**

  If you're unsure what a variable contains, use a **Print** step to inspect its value before using it in more complex logic.

  ***

  **4. Never Hardcode [Secret Global Variables](/docs/workflows/building-workflows/dynamic-variables/global-variables)**

  \*\*Never store passwords, API keys, access tokens, or other sensitive credentials directly in workflows. Hardcoded secrets can expose sensitive information and make credential rotation difficult.

  **Do**

  Use:

  * **Connections** to authenticate with external services.
  * **[Secret Global Variables](/docs/workflows/building-workflows/dynamic-variables/global-variables)** when a sensitive value needs to be reused across workflows.

  **Don't**

  Do not put credentials directly into:

  * Action parameters
  * Python or Bash scripts
  * Workflow YAML
  * Regular variables
  * URLs
  * Headers
  * Comments or notes

  For example, don't include credentials directly in a script:

  ```python theme={"dark"}
  api_key = "your-api-key"
  ```

  Instead, store the sensitive value securely and reference it dynamically.

  ***

  **5. Use [Connections](/docs/workflows/building-workflows/connections/connections) for External Services**

  When an action communicates with an external service, use a **Connection** whenever one is available.

  Connections centralize authentication and configuration and can be reused across workflows.

  **Do**

  Create and reuse a connection for external services such as:

  * SaaS applications
  * Security tools
  * Cloud platforms
  * Communication platforms
  * Ticketing systems

  **Don't**

  Don't store service credentials directly inside individual workflows when a Connection is available.

  Using Connections makes credential management easier and reduces the risk of exposing credentials in workflows.

  ***

  **7. Keep Steps Simple and Purposeful**

  Each step should have a clear purpose.

  For example:

  1. Retrieve the alert.
  2. Extract the relevant IP address.
  3. Enrich the IP address.
  4. Check the result.
  5. Take the appropriate response.

  Avoid creating steps that perform multiple unrelated tasks when separating the logic would make the workflow easier to understand.

  **Use descriptive step names**

  Give steps names that explain what they do.

  **Good:**

  ```text theme={"dark"}
  Get User Details
  Extract Source IP
  Check IP Reputation
  Create ServiceNow Incident
  Notify Security Team
  ```

  **Avoid:**

  ```text theme={"dark"}
  Step 1
  Test
  API
  New Action
  Check
  ```

  Clear naming is especially important when workflows are long or maintained by users other than the original author.

  ***

  **9. Use [Flow Controls](/docs/workflows/building-workflows/actions/basic-actions/flow-control-actions) for Decision-Making**

  Use conditions, switches, loops, and other \[flow controls]\(Flow Controls]\(/docs/workflows/building-workflows/actions/basic-actions/flow-control-actions) ) when a workflow needs to make decisions or process multiple values.

  For example:

  ```text theme={"dark"}
  Get Alert
      ↓
  Check Severity
      ↓
  Is severity Critical?
     ↙        ↘
   Yes         No
   ↓            ↓
  Respond      Continue
  ```

  Keep branching logic easy to follow. If a workflow contains many deeply nested conditions, consider whether the logic can be simplified or separated into reusable components.

  **Make dependencies clear**

  A step's output is only available after that step has executed. When using a step's output in a later step, make sure the workflow path guarantees that the source step runs first.

  This is particularly important when working with branches and conditional logic.

  ***

  **10. Validate Data Before Using It**

  Don't assume that an output always contains the value you expect.

  Before using data from a previous step, consider:

  * Can the value be missing?
  * Can it be `null`?
  * Can the list be empty?
  * Can the API return a different format?
  * Can the value have a different data type?

  Where appropriate, handle missing or unexpected values before passing them to downstream steps.

  If you're unsure what a step returns, use a Print step to inspect the output before building additional logic around it.

  ***

  **11. Design for Failure**

  External systems can fail, time out, return unexpected data, or become temporarily unavailable.

  Consider what should happen when:

  * An API request fails.
  * A connection is unavailable.
  * An expected value is missing.
  * An external service returns an unexpected response.
  * A workflow step times out.

  Use [Blink's error-handling](/docs/workflows/building-workflows/error-handling/error-handling) capabilities to define appropriate behavior rather than assuming every step will succeed.

  **Do**

  * Consider failure scenarios when designing the workflow.
  * Add appropriate error handling to critical workflows.
  * Decide whether a failure should stop the workflow or allow it to continue.
  * Make important failures visible to the appropriate users or systems.

  **Don't**

  * Assume external services will always be available.
  * Ignore failed steps.
  * Allow a workflow to continue with invalid or missing data when doing so could produce an incorrect result.

  ***

  **12. Test Safely**

  Always [test your workflow](/docs/workflows/testing-workflows/testing-workflows) before publishing it.

  Start by testing individual steps and then test the complete workflow.

  During testing, verify:

  * The trigger provides the expected data.
  * Each action receives the correct inputs.
  * Dynamic variables resolve to the expected values.
  * Conditions follow the expected path.
  * External services return the expected results.
  * Errors are handled appropriately.
  * The final output is correct.

  **Be aware of external effects**

  Workflow test runs can interact with external systems using configured Connections. Before testing, consider whether any action can create, modify, delete, or otherwise affect real data.

  **Do**

  * Use safe test data where possible.
  * Verify which Connections the workflow uses.
  * Consider the impact of actions before running the test.
  * Test destructive or irreversible actions carefully.

  **Don't**

  * Assume a test run cannot affect external systems.
  * Test destructive actions against production data without considering their impact.
  * Publish a workflow without testing it.
  * Don't leave [Mock outputs](/docs/workflows/building-workflows/steps#mock-output) enabled for production

  [Mock outputs](/docs/workflows/building-workflows/steps#mock-output) can be useful during development and testing, but should not be used for production executions where real data is required.

  Before publishing a workflow, verify that steps are configured to use real execution data.

  ***

  **13. Use Error Handling Consistently**

  For important workflows, establish a consistent approach to handling errors.

  Consider whether errors should:

  * Stop the workflow.
  * Be handled and allow the workflow to continue.
  * Trigger a notification.
  * Be logged for investigation.
  * Be passed to another workflow or process.

  Use workflow-level or workspace-level error handling where appropriate so that failures are handled consistently.

  ***

  **14. Review Workflows Before Publishing**

  Before publishing a workflow, review the complete workflow from beginning to end.

  Check that:

  * The workflow has a clear purpose.
  * The trigger is configured correctly.
  * All required inputs are available.
  * Dynamic variables reference the correct values.
  * Secrets are stored securely.
  * Connections are used for authentication.
  * Conditions and branches behave as expected.
  * Error handling is configured where needed.
  * There are no unnecessary steps or variables.
  * No mock outputs are enabled unintentionally.
  * Step names and descriptions are clear.
  * The workflow has been tested successfully.

  ***

  **15. Maintain Existing Workflows**

  Workflow maintenance is just as important as workflow creation.

  When modifying an existing workflow, consider how the change may affect current users and executions.

  **Use version history**

  Before making significant changes, review the workflow's version history. This allows you to understand previous changes and restore an earlier version if necessary.

  **Make changes incrementally**

  For significant changes:

  1. Understand the existing workflow.
  2. Identify what needs to change.
  3. Make the change.
  4. Test the affected steps.
  5. Test the complete workflow.
  6. Review the workflow before publishing the changes.

  **Coordinate changes**

  If a workflow is shared or maintained by multiple users, coordinate significant changes with the relevant team members.

  ***

  **16. [Use Builder Copilot](/docs/builder-copilot/builder-copilot) Carefully**

  When using [Builder Copilot](/docs/builder-copilot/builder-copilot) to modify a workflow, review the changes before applying or publishing them.

  For complex workflows, prefer targeted, step-level changes where possible. This makes it easier to understand what changed and reduces the risk of unintentionally affecting unrelated workflow logic.

  Always test the workflow after applying AI-generated changes.

  ***

  **17. Quick Do's and Don'ts**

  | Do | Don't |
  | - | - |
  | Use Connections for external service authentication | Hardcode credentials in workflows |
  | Use Secret Global Variables for reusable sensitive values | Store secrets in regular variables |
  | Use dynamic variables for runtime data | Hardcode values that change between executions |
  | Keep variable types consistent | Reuse a variable for different data types |
  | Give steps descriptive names | Leave steps named `Step 1`, `Test`, etc. |
  | Validate data before using it | Assume an API always returns the expected value |
  | Test individual steps as you build | Wait until the entire workflow is finished to test |
  | Test carefully when actions affect external systems | Assume test runs cannot affect real systems |
  | Disable mock outputs before production use | Leave mock data enabled in production |
  | Add error handling to important workflows | Assume every action will succeed |
  | Keep workflows focused | Put unrelated processes into one large workflow |
  | Review significant changes before publishing | Publish untested changes |
  | Use version history when making major changes | Make significant changes without reviewing the existing workflow |
  | Review Builder Copilot changes before publishing | Assume AI-generated changes are automatically correct |
</Accordion>

## Related Articles

<CardGroup cols={2}>
  <Card title="Workflow Editor" icon="plus" href="/docs/workflows/building-workflows/workflow-editor">
    Build a new workflow from scratch in the Workflow Editor.
  </Card>

  <Card title="Triggers" icon="toggle-on" href="/docs/workflows/building-workflows/triggers">
    Configure triggers to start workflows based on events.
  </Card>

  <Card title="Steps" icon="arrow-progress" href="/docs/workflows/building-workflows/steps">
    Define and organize actions within a workflow.
  </Card>

  <Card title="Conditions" icon="code-fork" href="/docs/blink-platform/interface-components/condition-builder">
    Add logic to control workflow execution paths.
  </Card>
</CardGroup>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.