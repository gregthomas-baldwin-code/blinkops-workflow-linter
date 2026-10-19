> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Ask a Question via Google Chat

> Send interactive questions via Google Chat and use responses to drive workflow decisions in Blink.

The "Ask a Question via Google Chat" action integrates the Blink Bot (part of the Blink app) into your workspace, allowing you to perform common Google Chat actions within your workflows and triggers.
Questions from Blink to Google Chat are sent through this bot.

This action allows you to send a question to specific users or channels in Google Chat with responses that you configure.
It then receives the selected response and lets you reference it in later steps of your workflow.

<Tip>The **Blink Bot** is named **Blink** by default and displays the Blink logo.</Tip>

***

## Creating a Workflow Using the *Ask a Question via Google Chat* Action

### Add the Blink App to Your Google Chat Account

<Steps>
  <Step title="Open the Google Workspace Marketplace">
    Go to your [Google Chat](/docs/integrations/google-chat) account and click the **+** icon in the right-hand navigation bar.
    This will open the **Google Workspace Marketplace**.
    Search for *Blink* and select the Blink app card.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/-eoT09amno25RB5l/img/Actions/GoogleChatFindApps.png?fit=max&auto=format&n=-eoT09amno25RB5l&q=85&s=190c8de24fe4ee96dd70cdc975cc2e0e" width="702" height="530" data-path="img/Actions/GoogleChatFindApps.png" />
    </Frame>
  </Step>

  <Step title="Install the Blink App">
    Click the **Install** button to begin installation.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/-eoT09amno25RB5l/img/Actions/GoogleChatSelectChatOption.png?fit=max&auto=format&n=-eoT09amno25RB5l&q=85&s=ec706e6b132203898e4827dcd0b04993" width="801" height="644" data-path="img/Actions/GoogleChatSelectChatOption.png" />
    </Frame>
  </Step>

  <Step title="Authorize Blink Access to Google Chat">
    You’ll be taken to a sign-in page prompting you to log into your Blink account and authorize access to your Google Chat account.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/-eoT09amno25RB5l/img/Actions/GoogleChatConfigure.png?fit=max&auto=format&n=-eoT09amno25RB5l&q=85&s=6834e92254d27ca0f169f07d85bceab9" width="469" height="191" data-path="img/Actions/GoogleChatConfigure.png" />
    </Frame>
  </Step>

  <Step title="Confirm Successful Installation">
    After installation, you’ll receive a confirmation message.
    Click **Done** to proceed.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/-eoT09amno25RB5l/img/Actions/GoogleChatInstalled.png?fit=max&auto=format&n=-eoT09amno25RB5l&q=85&s=e08f7b51cc69133c5a875a3d836ce19a" width="3562" height="2060" data-path="img/Actions/GoogleChatInstalled.png" />
    </Frame>
  </Step>

  <Step title="Add Blink App to a Google Chat Space">
    Click the **Add to space** button to include the Blink app in your Google Chat space.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/-eoT09amno25RB5l/img/Actions/GoogleChatSelectSpace.png?fit=max&auto=format&n=-eoT09amno25RB5l&q=85&s=5d5e1f96d9f87643100bbf2dc15e6fec" width="1596" height="1284" data-path="img/Actions/GoogleChatSelectSpace.png" />
    </Frame>
  </Step>

  <Step title="Grant Permissions to Blink">
    Allow Blink access to your Space and click **Continue**.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/yRkQ-wRlnQIXwr-A/img/Actions/AccessToSpace.png?fit=max&auto=format&n=yRkQ-wRlnQIXwr-A&q=85&s=5053b6e26b07a19921275c8b23699bbb" width="3566" height="2044" data-path="img/Actions/AccessToSpace.png" />
    </Frame>
  </Step>

  <Step title="Select Space for the Blink App">
    Choose the Space you want to add the Blink app to and enter the name.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/deay2AiePWJDKGEh/img/Actions/SpaceName.png?fit=max&auto=format&n=deay2AiePWJDKGEh&q=85&s=5a28b34b83d8e98d42b9ac0c6469e208" width="3394" height="1986" data-path="img/Actions/SpaceName.png" />
    </Frame>
  </Step>

  <Step title="Verify Blink Bot in Google Chat Space">
    You will be redirected to your selected Space and receive a message from the Blink app confirming successful integration.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/yRkQ-wRlnQIXwr-A/img/Actions/BlinkAppInSpace.png?fit=max&auto=format&n=yRkQ-wRlnQIXwr-A&q=85&s=829073b0967aecc4f9eaa2432acc0ecb" width="3574" height="2052" data-path="img/Actions/BlinkAppInSpace.png" />
    </Frame>
  </Step>
</Steps>

***

### Navigate to the Blink Platform

<Steps>
  <Step title="Add the 'Ask a Question via Google Chat' Action">
    In the Workflow Editor, open the **Action panel** and search for the *"Ask a question via Google Chat"* action.
    Alternatively, you can drag the action into the step.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/yRkQ-wRlnQIXwr-A/img/Actions/AskAQuestionGC.png?fit=max&auto=format&n=yRkQ-wRlnQIXwr-A&q=85&s=ead099734a5adfd00c174df8ef3e4a0e" width="1722" height="1078" data-path="img/Actions/AskAQuestionGC.png" />
    </Frame>
  </Step>

  <Step title="Configure Action Parameters">
    Enter the following parameters in your step:

    <div className="integrations-table">
      | Parameter | Description |
      | - | - |
      | Space | The resource name of the Google Chat Space. |
      | Subject | The subject or title of the question. |
      | Question | The question to be answered. |
      | Answers | Possible answers, separated by commas. |
      | Add answers in free text | Allows recipients to submit answers in free text. |
      | Include user info | Includes the user’s information with their response. |
      | **Advanced** – Response message | A message shown to the recipient after they respond. |
      | **Advanced** – Timeout in minutes (optional) | How long to wait for a response before timing out. |
      | **Advanced** – Default timeout response | The default answer used if the recipient does not respond in time. |
    </div>
  </Step>

  <Step title="Create or Select Google Chat Connection">
    Click ***Connection required*** in the top-right corner of your step. Once complete, click **Create connection** to proceed.

    <Tip>If a Google Chat connection already exists, select it from the list. Otherwise, create a new connection by selecting **Google Chat connection** and follow the steps in the [Google Chat connection guideline](/docs/integrations/google-chat). </Tip>

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/-eoT09amno25RB5l/img/Actions/GoogleChatConnection.png?fit=max&auto=format&n=-eoT09amno25RB5l&q=85&s=661c5728f2813b30c7346eb262348e73" width="1727" height="1080" data-path="img/Actions/GoogleChatConnection.png" />
    </Frame>
  </Step>

  <Step title="Run the Workflow to Send the Question">
    Run the step to send your configured question to Google Chat.

    <Note>
      While the recipient is responding, the step output will show: *Workflow execution paused*.
    </Note>

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/-eoT09amno25RB5l/img/Actions/GoogleChatAskQuestionAction.png?fit=max&auto=format&n=-eoT09amno25RB5l&q=85&s=b0ed2de20d54ac87f1090c431f4446e5" width="1717" height="1059" data-path="img/Actions/GoogleChatAskQuestionAction.png" />
    </Frame>
  </Step>

  <Step title="Question Appears in Google Chat Space">
    When the workflow runs, the selected Space will receive the question. Recipients can respond by interacting with the message card.

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/-eoT09amno25RB5l/img/Actions/GoogleChatAskQuestionMessage.png?fit=max&auto=format&n=-eoT09amno25RB5l&q=85&s=fc4b6e655488eedaf590d82c6afc47d6" width="1724" height="1072" data-path="img/Actions/GoogleChatAskQuestionMessage.png" />
    </Frame>
  </Step>

  <Step title="View the Response from Google Chat in the Workflow">
    Navigate back to your workflow to view the response in the step's output.

    <Note> If no response is received before the timeout period, the **default timeout response** will be used. </Note>

    <Frame>
      <img src="https://mintcdn.com/blinkops-2/-eoT09amno25RB5l/img/Actions/GoogleChatAskQuestionAnswer.png?fit=max&auto=format&n=-eoT09amno25RB5l&q=85&s=ab00fe05070bb71554b11418c1ae7b41" width="1727" height="1073" data-path="img/Actions/GoogleChatAskQuestionAnswer.png" />
    </Frame>
  </Step>
</Steps>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.