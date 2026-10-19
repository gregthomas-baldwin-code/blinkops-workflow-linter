> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Global Variables

> Define global variables once and reuse them across multiple workflows in your Blink workspace.

<Note>**Note**: Global variables can be added with the [Variable Picker](/docs/workflows/building-workflows/dynamic-variables/variable-picker#using-the-variable-picker-to-add-dynamic-variables).</Note>

## Global Variable Types

There are two distinct types of Global Variables:

1. <p> <Icon icon="globe" /> **Raw value variable:** </p>

   * Stores plain text values that are visible to anyone with access to the workflow.
   * Typically used for non-sensitive information like configuration settings or default values.

2. <p> <Icon icon="lock" />  **Secret variables** </p>

   * Store sensitive information like API keys, passwords, or tokens in an encrypted format.
   * Their values are hidden in the workflow editor and logs for security reasons.

   <Tip>
     Use **Secret Global Variables** whenever handling sensitive or confidential data to ensure it remains secure throughout the workflow execution.
   </Tip>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/le_txZXPIK1riSeD/img/GlobalVariables/GlobalVariablePage.png?fit=max&auto=format&n=le_txZXPIK1riSeD&q=85&s=87c8c3c49d96e384663e17fe530cc6c7" width="1728" height="1082" data-path="img/GlobalVariables/GlobalVariablePage.png" />
</Frame>

***

## Creating a New Global Variable

<Steps>
  <Step title="Add new global variable">
    <p>On the left-hand side navigation menu, click the <Icon icon="globe" /> icon > **New Variable**. The **New Global Variable** dialog box opens.</p>
  </Step>

  <Step title="Enter the following parameters">
    <div className="integrations-table">
      | Parameter | Description |
      | - | - |
      | Name | Name of global variable. |
      | Value | Value of the variable. |
      | Secret | Select the checkbox if you wish to define the variable as secret. Uses the default secret manager of the workspace. |
      | **Optional**- Description | A description about the Global Variable |
      | **Optional**- Tags | Create and assign tags to categorize and group global variables for easier discovery, filtering, and organization across workflows. |
    </div>
  </Step>

  <Step title="Click Create">
    Your newly created variable will be added to the table.

    <Frame>
      <video controls autoPlay muted zoom loop allowFullScreen className="w-full aspect-video" src="https://www.dropbox.com/scl/fi/5iah7lspjlww8t86ji3za/GlobalVariable.mp4?rlkey=odys9pmpb9tjkmgzuwvybxnmb&st=x2hvbkit&raw=1" />
    </Frame>
  </Step>
</Steps>

***

## Using Global Variables in Workflows

Use global variables anywhere that the variable picker is available. All existing global variables can be found in the **GLOBAL VARIABLES** section in the variable picker.

<Steps>
  <Step title="Access the Variable Picker">
    Click **+** to open the [Variable Picker](/docs/workflows/building-workflows/dynamic-variables/variable-picker#using-the-variable-picker-to-add-dynamic-variables).
  </Step>

  <Step title="Select the Global Variable">
    Select a global variable. In this example we are selecting the "Default Slack Variable" option.

    * If it is a *secret global variable*, the variable value is not displayed.
    * If it is a *raw value variable*, its value is displayed on the right-hand side of the variable picker.
  </Step>

  <Step title="Add it to the Workflow">
    Click **Add**. The global variable is defined in your Workflow Step.

    <Frame>
      <video controls autoPlay muted zoom loop allowFullScreen className="w-full aspect-video" src="https://www.dropbox.com/scl/fi/xor0yhavbojzzx7bbirr1/GlobalVarPicker.mp4?rlkey=fmq9wra0zum5i9vcw9byvde8m&st=38ejjjvj&raw=1" />
    </Frame>
  </Step>
</Steps>

***

## Global Variables Actions

<Frame>
  <img src="https://mintcdn.com/blinkops-2/ECv5yZuj7RZID_QY/img/GlobalVariables/GlobalVariableActions.png?fit=max&auto=format&n=ECv5yZuj7RZID_QY&q=85&s=3eac35356b9c57be88e620e7bcbc4121" width="1728" height="1082" data-path="img/GlobalVariables/GlobalVariableActions.png" />
</Frame>

***

### Set Global Variable

Creates a raw global variable or updates an existing raw or secret global variable.

<Note>**IMPORTANT**: You cannot create a secret global variable using this action. However, you can update an existing secret global variable.</Note>

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Variable Name | The name of the new/existing global variable. Once created/updated, it is available for all Workflows in a workspace. |
  | Variable Value | Assign a value to the global variable. Value is string only, limited to 1 MB size. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/ofndyjl5pT7G9RPS/img/Actions/CreateGlobalVariable.png?fit=max&auto=format&n=ofndyjl5pT7G9RPS&q=85&s=aeb8099c1316f9f1f72cf38d8b5658a4" width="2168" height="716" data-path="img/Actions/CreateGlobalVariable.png" />
</Frame>

***

***

### Delete Global Variable

Deletes a Global Variable.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Variable Name | The name of the global variable to delete. Once deleted, it is no longer available for any other Workflows in the workspace. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/ofndyjl5pT7G9RPS/img/Actions/DeleteGlobalVariable.png?fit=max&auto=format&n=ofndyjl5pT7G9RPS&q=85&s=70ac2a68a8e3eae52b7a5967336208a2" width="2164" height="704" data-path="img/Actions/DeleteGlobalVariable.png" />
</Frame>

***

### Get Global Variable

Gets the value of a Global Variable.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Variable Name | The name of the global variable to get. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/65NqQ4rXp1zAxdMH/img/Actions/GetGlobalVariable.png?fit=max&auto=format&n=65NqQ4rXp1zAxdMH&q=85&s=752ab6dbb4d215adb2d583a5464fcc92" width="2164" height="698" data-path="img/Actions/GetGlobalVariable.png" />
</Frame>

***

### List Global Variables

Get a list of **all** the Global Variables.

* No parameters required.

* The results are returned in the output as `JSON` format.

* You can tick the "Exclude Secrets" checkbox to exclude global secrets from the `JSON` output.

<Frame>
  <img src="https://mintcdn.com/blinkops-2/OZZc0vIK-3gQE9jh/img/Actions/ListGlobalVar.png?fit=max&auto=format&n=OZZc0vIK-3gQE9jh&q=85&s=fbaa909ba39c27fa1baba4eca733f1e6" width="1082" height="354" data-path="img/Actions/ListGlobalVar.png" />
</Frame>

***


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.