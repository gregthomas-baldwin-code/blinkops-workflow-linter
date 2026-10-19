> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Step Output Transformation

> Use Builder Copilot to transform and manipulate data outputs within your Blink workflows.

<Note>
  This feature is part of Blink’s Interactive AI Actions and is subject to the same tenant-level limits that apply to those actions:

  * Up to `40 requests per minute`
  * Up to `3 MB` of processed data per minute
</Note>

Transform the output of a step that contains any `JSON data` using guidance from [Builder Copilot](/docs/builder-copilot/builder-copilot) or manually entering a `JQ command`. This feature uses build-time AI to generate JQ commands from your text prompts, allowing you to reshape data formats or focus on essential information.

<Steps>
  <Step title="Open the Transform Output Editor">
    In the Workflow's step output, click the 'Transform' button in the top right corner to open the *Transform Output Editor*.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/puhTpIp-fp4ylT0M/img/Actions/ActionTransform.png?fit=max&auto=format&n=puhTpIp-fp4ylT0M&q=85&s=50302b788785f8a89f9d69127afc5961" width="1726" height="1076" data-path="img/Actions/ActionTransform.png" />
    </Frame>
  </Step>

  <Step title="Generate a Transformation Prompt or JQ Command">
    This will use the last-received JSON data as the sample. Continue by entering your prompt in plain English with Builder Copilot or add a `JQ Command` manually, then click Generate. You can edit the generated `JQ command` if it's not exactly what you need.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/puhTpIp-fp4ylT0M/img/Actions/ActionTransformGenerating.png?fit=max&auto=format&n=puhTpIp-fp4ylT0M&q=85&s=8143041923b77ee2153a88960ff233b1" width="3442" height="2156" data-path="img/Actions/ActionTransformGenerating.png" />
    </Frame>
  </Step>

  <Step title="Preview and Apply the Transformed Output">
    It will also immediately run the generated script with the sample input data and show the result in the "transformed output" section. To apply the transformed output to your Workflow, click the "Apply" button.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/puhTpIp-fp4ylT0M/img/Actions/ActionTranformOutput.png?fit=max&auto=format&n=puhTpIp-fp4ylT0M&q=85&s=0aeb74363f32af0a5d884e9f9bc2d912" width="3452" height="2156" data-path="img/Actions/ActionTranformOutput.png" />
    </Frame>
  </Step>

  <Step title="Compare Original and Transformed Outputs">
    You can find the transformed output data in the "*Output (transformed)*" tab. You can also see the original output, in the *Original Output* tab.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/puhTpIp-fp4ylT0M/img/Actions/ActionTransformResult.png?fit=max&auto=format&n=puhTpIp-fp4ylT0M&q=85&s=5f9c92093f7aa9ce0abe26f93ebd50bb" width="3456" height="2158" data-path="img/Actions/ActionTransformResult.png" />
    </Frame>
  </Step>
</Steps>

***

## Step Output Transformation and Dynamic Variables

<Steps>
  <Step title="Dynamic Variables are supported in the Copilot Prompt or JQ Command ">
    Using the [Variable Picker](/docs/workflows/building-workflows/dynamic-variables/variable-picker) you can add dynamic variables into either the Copilot transformation prompt or JQ command, enabling you to easily extract and return the specific information you need.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/YX1eg7W4joM6Bz52/img/Actions/CopilotTransformationPrompt.png?fit=max&auto=format&n=YX1eg7W4joM6Bz52&q=85&s=6b55edbf871916d8f029df4b403bc779" width="3450" height="2148" data-path="img/Actions/CopilotTransformationPrompt.png" />
    </Frame>
  </Step>

  <Step title="Use the Transformed Step Output as a Dynamic Variables">
    With the help of the [Variable Picker](/docs/workflows/building-workflows/dynamic-variables/variable-picker), you can access a [step dynamic variable](/docs/workflows/building-workflows/dynamic-variables/variable-picker#dynamic-variables-types) and choose either the step's original output (`original_output`) or its transformed output (`output`).

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/1LTMWwcM8W-jYX0Y/img/Actions/OriginalOutputDynamic.png?fit=max&auto=format&n=1LTMWwcM8W-jYX0Y&q=85&s=12d4b8cd065e4b1b47c7aa926612db3b" width="1727" height="1083" data-path="img/Actions/OriginalOutputDynamic.png" />
    </Frame>
  </Step>
</Steps>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.