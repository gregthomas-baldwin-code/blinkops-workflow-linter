> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom Actions

> Create and manage custom actions to extend Blink's built-in capabilities with your own logic.

Custom Actions allow you to create reusable actions tailored to your specific needs by combining existing actions into a single unit. This simplifies workflow creation and promotes consistency across workflows.

***

## Creating a New Custom Action

<Note>**Note:** The 'If', 'If else', 'For Each', 'Variable', 'Wait', 'Note', and 'End Run' actions cannot be customized. </Note>

<Steps>
  <Step title="Navigate to Settings">
    On the right-hand side of the step, click <Icon icon="square-ellipsis-vertical" iconType="solid" /> the **Save as new custom action** option.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/eGvvjNfAh_mfFLpc/img/Actions/CustomAction.png?fit=max&auto=format&n=eGvvjNfAh_mfFLpc&q=85&s=de95da04a0c03d89bef8665ec100b10b" width="1727" height="1081" data-path="img/Actions/CustomAction.png" />
    </Frame>
  </Step>

  <Step title="Configure the Custom Action">
    Enter the following parameters:

    1. A *Custom Action name*
    2. Select a *Vendor* or create a new one
    3. Enter a description
    4. In *Advanced Settings*, you can edit the `YAML` format

           <Frame>
             <img src="https://mintcdn.com/blinkops-2/eGvvjNfAh_mfFLpc/img/Actions/AddCustomActionParam.png?fit=max&auto=format&n=eGvvjNfAh_mfFLpc&q=85&s=0d791ac056b716a5ac987e3695916aad" width="3440" height="2162" data-path="img/Actions/AddCustomActionParam.png" />
           </Frame>
  </Step>

  <Step title="Save and Reuse">
    <Note>**Note:** A `custom action` label will appear next to it, indicating that it is a custom action.</Note>

    Click 'Create' to save your custom action. It will now appear under the selected vendor in the action library and will be available to all users in your workspace.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/eGvvjNfAh_mfFLpc/img/Actions/CustomActionLabel.png?fit=max&auto=format&n=eGvvjNfAh_mfFLpc&q=85&s=94ebe676cdc2614515ecc1637e9adbd0" width="1725" height="1081" data-path="img/Actions/CustomActionLabel.png" />
    </Frame>
  </Step>
</Steps>

***

## Editing a Custom Action

<Warning>Any updates to this custom action will automatically affect every workflow where it is used.</Warning>

<Steps>
  <Step>
    In the left-hand side action panel, click the <Icon icon="square-ellipsis-vertical" iconType="solid" /> and select the 'Edit custom action'.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/nVapLLtZUrBaK31W/img/Actions/EditCustomAction.png?fit=max&auto=format&n=nVapLLtZUrBaK31W&q=85&s=41e1951ff5c7cde06f81553e8bc6f830" width="1728" height="1083" data-path="img/Actions/EditCustomAction.png" />
    </Frame>
  </Step>

  <Step>
    Make the necessary changes and click the 'Update' button to apply the changes.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/nVapLLtZUrBaK31W/img/Actions/EditCustomActionParams.png?fit=max&auto=format&n=nVapLLtZUrBaK31W&q=85&s=6c0939379765d99a666ab930ec30223d" width="3456" height="2176" data-path="img/Actions/EditCustomActionParams.png" />
    </Frame>
  </Step>
</Steps>

***

## Using Custom Actions

Add a custom action to a step the same way as creating a regular step:

* **Drag and drop**: To use a custom action, drag and drop the Action onto the canvas from the Action panel. At the top of the panel you can see the flow control actions and beneath them a list of external service providers. To see the available Actions, open a service.
* **Inline adding**: Click on the box in the middle of the canvas. Search for the custom action in the search bar and select it.

***

## Configuring Custom Action Inputs

When you create a Custom Action, you can configure or edit its YAML in the **Advanced Settings** YAML editor.

Inputs determine which values users can provide when they add the Custom Action to a workflow. This allows you to make the Custom Action reusable while controlling which parts of its configuration can be changed.

### Custom Action Input Types

When configuring a Custom Action, you can define the type of input users can provide. Select the input type based on the kind of value the parameter expects.

| Parameter / Input Type | Description | Example |
| - | - | - |
| `string` | Single-line text input | URL, region, working directory, package name |
| `textarea` | Multi-line text input | Text or longer content |
| `bool` | Boolean value displayed as a checkbox | Enable/disable SSL verification |
| `dropdown` | Select one value from a predefined list | HTTP method, Python version |
| `dynamic_dropdown` | Dropdown populated dynamically using an autofill fetcher | GCP project |
| `code:python` | Python code editor | Python script |
| `code:bash` | Bash code editor | Bash script |
| `code:json` | JSON code editor | HTTP request body |
| `code:map` | Map/key-value code editor | HTTP headers, cookies |
| `name` | Defines the internal name of the parameter | `url`, `project`, `working_directory` |
| `display_name` | Defines the name displayed to users | `URL`, `Project`, `Working Directory` |
| `description` | Provides a description or instructions for the parameter | `The URL to communicate with.` |
| `required` | Determines whether the parameter is mandatory | `true` / `false` |
| `default_value` | Sets a default value for the parameter | `3.8.16`, `true` |
| `placeholder` | Provides guidance or an example in the input field | `Enter text to print...` |
| `options` | Defines the available values for a dropdown | `GET`, `POST`, `PUT`, `DELETE` |
| `autofill` | Defines how a dynamic dropdown is populated | `gcp.SearchProjects` |
| `group_type` | Determines whether the parameter appears under Basic or Advanced settings | `basic` / `advanced` |
| `var_picker_sections` | Makes specific Variable Picker sections available for the parameter | `files` |
| `icon_name` | Defines the icon associated with the parameter | `files` |

<Accordion title="Custom Action YAML example">
  ```yaml theme={"dark"}
  action_to_run: http.getV2
  connection_optional: false
  parameters:
      - name: project
        display_name: Project
        description: Project ID for this request.
        required: true
        type: dynamic_dropdown
        group_type: basic
        autofill:
          fetcher: gcp.SearchProjects
      - name: region
        display_name: Region
        description: Name of the region scoping this request.
        required: true
        type: string
        group_type: basic
      - name: targetHttpsProxy
        display_name: Target Https Proxy
        description: Name of the TargetHttpsProxy resource to return.
        required: true
        type: string
        group_type: basic
  action_to_run_param_values:
      retryOnRateLimit: "true"
      url: https://compute.googleapis.com/compute/v1/projects/{{params["project"]}}/regions/{{params["region"]}}/targetHttpsProxies/{{params["targetHttpsProxy"]}}?alt=json
  ```

  <Frame>
    <img src="https://mintcdn.com/blinkops-2/EFrkYrDAq4IrCLvy/img/Actions/CustomActionExample.png?fit=max&auto=format&n=EFrkYrDAq4IrCLvy&q=85&s=bb16eeb8d762a3d89d33eb5b1957e89c" width="2328" height="798" data-path="img/Actions/CustomActionExample.png" />
  </Frame>
</Accordion>

<Accordion title="Best Practices">
  When defining Custom Action inputs and parameters:

  * Expose only the values that users need to configure.
  * Use the input type that best matches the value the underlying custom action expects.
  * Use descriptive display names.
  * Choose an input type that matches the expected value.
  * Use required inputs only when they are necessary.
  * Use predefined options when the accepted values are known.
  * Provide defaults when there is a safe and useful default.
  * Add descriptions or placeholders when the expected input is not obvious.
  * Avoid exposing internal implementation details that users do not need to configure.
  * Test the Custom Action with both static and dynamic values before making it available to other users.
</Accordion>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.