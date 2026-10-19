> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# About Builder Copilot

> Overview of Builder Copilot, the AI assistant that helps you create and modify Blink workflows using natural language.

<Note>
  This feature is part of Blink’s Interactive AI Actions and is subject to the same tenant-level limits that apply to those actions:

  * Up to `40 requests per minute`
  * Up to `3 MB` of processed data per minute
</Note>

The Builder Copilot is an innovative feature that helps users to create custom workflows from the ground up, using the advanced capabilities of generative AI to enhance and streamline workflows within the Workflow Editor.

<Frame>
  <img src="https://mintcdn.com/blinkops-2/RNRSqed-fSgxO9ZA/img/Copilot/BuilderCopilot.png?fit=max&auto=format&n=RNRSqed-fSgxO9ZA&q=85&s=56c852decfb9fbb48744e5f87c54f6c7" width="3448" height="2146" data-path="img/Copilot/BuilderCopilot.png" />
</Frame>

***

### Safe Use of AI

<Note>It is important that Blink does not use customer data for AI training. We adhere to industry standards to ensure your data remains secure, never stored or utilized for these purposes.</Note>

***

## Using the Builder Copilot on an Entire Workflow

<Warning>
  **Please note**

  1. Populating step inputs with Builder Copilot does not support [Blink's Table actions](/docs/blink-platform/tables/tables-in-workflows).
  2. In some cases, results may include incorrect or invalid details. It is recommended to validate the generated actions.
</Warning>

<Steps>
  <Step title="Navigate to the Workflow Editor">
    Open your workspace and select **[Create New Workflow](/docs/workflows/creating-a-workflow)** and configure the workflow settings.
  </Step>

  <Step title="Open the Prompt Interface">
    In the top-left corner select the `Builder Copilot` icon. A prompt interface will appear.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/0rPJkngpDAMJuuqo/img/Copilot/CopilotIcon.png?fit=max&auto=format&n=0rPJkngpDAMJuuqo&q=85&s=20a376975b8c434a3b33a2f84f910b52" width="1728" height="1077" data-path="img/Copilot/CopilotIcon.png" />
    </Frame>
  </Step>

  <Step title="Generate the Workflow">
    Provide `Builder Copilot` with detailed instructions specifying the type of Workflow you want it to create and then press generate.**It may take a few seconds to generate the Workflow**.

    <Tip>Explore the best methods for generating the ideal prompt by visiting [Best Practices for using Builder Copilot](#best-practices)</Tip>

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/0rPJkngpDAMJuuqo/img/Copilot/copilot2.png?fit=max&auto=format&n=0rPJkngpDAMJuuqo&q=85&s=f8ec71aca275bc12abf467057a314de8" width="3452" height="2154" data-path="img/Copilot/copilot2.png" />
    </Frame>
  </Step>

  <Step title="The Completed and Built Workflow">
    Once the process is complete, `Builder Copilot` will update your canvas with a recommendation based on your prompt.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/0rPJkngpDAMJuuqo/img/Copilot/copilot6.png?fit=max&auto=format&n=0rPJkngpDAMJuuqo&q=85&s=57c33089b2dd28436fb1ccca8e58e10f" width="3456" height="2164" data-path="img/Copilot/copilot6.png" />
    </Frame>
  </Step>

  <Step title="Undo or Redo any Changes Made">
    At any stage you can also undo or redo any changes made by the `Builder Copilot` by clicking on the **undo** or **redo** arrows in the top-right corner.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/0rPJkngpDAMJuuqo/img/Copilot/Undo.png?fit=max&auto=format&n=0rPJkngpDAMJuuqo&q=85&s=4a5d0c0a97259b21a884549afdf51d3b" width="1727" height="1079" data-path="img/Copilot/Undo.png" />
    </Frame>
  </Step>

  <Step title="Review and Modify the Built Workflow">
    Lastly, you can either make additional changes to the Workflow that `Builder Copilot` has just created or save it to your workspace for future use.
    <Tip> Before executing your Workflow, double-check your Workflow to ensure it meets your requirements perfectly.</Tip>
  </Step>
</Steps>

***

## Builder Copilot Block Generation

Within the canvas, the Builder Copilot enables you to generate complete workflow blocks, consisting of single or multiple steps, with a single prompt. This streamlines the creation process by eliminating the need to manually add and configure each step individually.

<Steps>
  <Step title="Open the Prompt Interface">
    Click the 'Builder Copilot' icon on the canvas or next to a step to open the Builder Copilot's prompt interface. In the prompt field, provide clear and detailed instructions describing the workflow block you want to generate. Once your prompt is ready, click **Generate** to proceed. **It may take a few seconds to generate the workflow blocks and for more complex logic, it may take a while longer**.
    <Tip> To improve your results, refer to [Best Practices for using Builder Copilot](#best-practices). </Tip>

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/0rPJkngpDAMJuuqo/img/Copilot/CopilotStep1.png?fit=max&auto=format&n=0rPJkngpDAMJuuqo&q=85&s=f0b57779c892db199f5e093254e9056c" width="3456" height="2154" data-path="img/Copilot/CopilotStep1.png" />
    </Frame>
  </Step>

  <Step title="Review and Modify the Generated Block">
    Once the workflow block is generated, all newly created steps are automatically highlighted for easy identification. The prompt interface remains open, allowing you to modify your instructions and regenerate the block if needed.

    <Tip>You can update a step by editing its input values or by replacing the step entirely.</Tip>

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/0rPJkngpDAMJuuqo/img/Copilot/CopilotSteps.png?fit=max&auto=format&n=0rPJkngpDAMJuuqo&q=85&s=0658bcb4c00d61adde48d48c7c5e134d" width="3456" height="2154" data-path="img/Copilot/CopilotSteps.png" />
    </Frame>
  </Step>
</Steps>

***

## Best Practices

1. Be clear and precise: Providing clear and specific instructions will assist `Builder Copilot` in understanding your instructions clearly.
2. Use complete integration names: For example, instead of using generic terms like **Compute Instance**, specify the full name of the relevant integrations, such as **AWS EC2 Compute Instance**.
3. Refrain from using unknown or unrecognized vendors in your prompt.
4. Using the word **loop** in your prompt will likely generate a looping action in the results. Try to be as descriptive as possible about what you want the **loop** action to accomplish.
5. Keep it simple and concise: To tackle complex workflows effectively, consider breaking your prompt instructions into bullet points, ensuring each bullet point prompt is concise and straightforward. For Example:

<Frame>
  <img src="https://mintcdn.com/blinkops-2/0rPJkngpDAMJuuqo/img/Copilot/copilot-example-one.png?fit=max&auto=format&n=0rPJkngpDAMJuuqo&q=85&s=72466c416241ab37a35210b903f4b725" width="3456" height="2162" data-path="img/Copilot/copilot-example-one.png" />
</Frame>

**OR**

<Frame>
  <img src="https://mintcdn.com/blinkops-2/0rPJkngpDAMJuuqo/img/Copilot/copilot-example-two.png?fit=max&auto=format&n=0rPJkngpDAMJuuqo&q=85&s=7f7577f590b5eb4b46bb8d8d4dd40044" width="3454" height="2162" data-path="img/Copilot/copilot-example-two.png" />
</Frame>

***


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.