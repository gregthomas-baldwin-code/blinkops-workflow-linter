> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# API Actions

> Use API actions to call integration endpoints and interact with external services in Blink workflows.

API Actions in Blink let you interact directly with external services and applications through their APIs — without needing to write code.
Each Action represents a specific operation you can perform on a supported service (for example, “Create Ticket in Jira” or “Search Alerts in CrowdStrike”).

Blink includes hundreds of prebuilt API Actions across 350+ integrations, giving you instant access to well-tested, reliable operations that reflect the native capabilities of each tool.
You can use these Actions as building blocks in your workflows to automate complex processes across multiple systems seamlessly.

<Frame>
  <img src="https://mintcdn.com/blinkops-2/xAbpULuFsZlky6a2/img/Actions/githubListBranche.png?fit=max&auto=format&n=xAbpULuFsZlky6a2&q=85&s=5358059856f925fae360ee676c100968" width="1076" height="356" data-path="img/Actions/githubListBranche.png" />
</Frame>

## Running an Out-of-the-Box API Action:

<Steps>
  <Step title="Connect to a Service Provider">
    Before using any API Action, you need to create a connection to the external service provider. Go to the [Connections](/docs/workflows/building-workflows/connections/connections) page and authenticate using **OAuth** or your **API credentials**.
  </Step>

  <Step title="Choose an Action in the Workflow Editor">
    In the Workflow Editor, open the **Action Panel** or search for the external service provider you want to use. Select the **Action** that matches the operation you want your workflow to perform.
  </Step>

  <Step title="Configure the Action">
    Once you have added the action to your workflow, choose the **connection** you created earlier and fill in the **required input fields**.
  </Step>
</Steps>

***

## Step Settings: Include Full Response

<Note>**Note**: The "View Full Response" settings option is also applicable to [HTTP Actions](/docs/workflows/building-workflows/actions/basic-actions/http-actions/http-actions)</Note>

To view the full HTTP response from an HTTP request, click the <Icon icon="square-ellipsis-vertical" iconType="solid" /> icon next to the step, select **Settings**, and toggle the button to **Include full response**.

<Frame>
  <img src="https://mintcdn.com/blinkops-2/AprFKFty9nUikfm0/img/Actions/HTTPFullResponse.png?fit=max&auto=format&n=AprFKFty9nUikfm0&q=85&s=940948def741304aaf01b13b77586c71" width="1714" height="1068" data-path="img/Actions/HTTPFullResponse.png" />
</Frame>

This option can be useful, for instance, when you need to access the values from the response headers in subsequent steps to support your use case.

<Frame>
  <img src="https://mintcdn.com/blinkops-2/puhTpIp-fp4ylT0M/img/Actions/BeforeAfterResponse.png?fit=max&auto=format&n=puhTpIp-fp4ylT0M&q=85&s=6339c3aa27d729addc27af0114bb4346" width="3450" height="2154" data-path="img/Actions/BeforeAfterResponse.png" />
</Frame>

***


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.