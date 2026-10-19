> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Ask a Question via Email

> Send interactive questions via email and use responses to drive workflow decisions in Blink.

The *"Ask A Question via Email"* action allows you to send questions to specified e-mail addresses with responses that you configure. This action then receives the responses and lets you reference the selected answers in later steps of your workflow.

***

## Creating a Workflow using the *Ask a question via Email* Action

1. In the Workflow Editor, click to open the Action panel and search for "*Ask a question via Email*" action. Alternatively, you can drag the action to the step.

<Frame>
  <img src="https://mintcdn.com/blinkops-2/LiDiL34PEmIGHJGK/img/Actions/questionemail.png?fit=max&auto=format&n=LiDiL34PEmIGHJGK&q=85&s=bf043a24dab0e83fcfa6a064330bbbd1" width="903" height="790" data-path="img/Actions/questionemail.png" />
</Frame>

2. Enter the following parameters in your step.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | To | The recipient's email address |
  | Subject | Email subject |
  | Question | Questions to be answered |
  | Answers | Possible answers separated by a comma |
  | Timeout in minutes (optional) | Timeout in minutes for the recipient to respond |
  | Default timeout response (optional) | The default answer if the recipient does not respond |
</div>

<Note>
  While the user is waiting for a response, the Step output shows *Workflow execution paused*.

  The recipient receives an email with a question and possible answers. An answer is selected and the Workflow continues to run in accordance with the answer.
</Note>

4. The recipient will then receive the question to their Email.

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/blinkops-2/img/Actions/Email.png" />
</Frame>

5. You can then navigate back to your workflow where you can find the response to your question in the output of your Workflow.

<Frame>
  <img src="https://mintcdn.com/blinkops-2/LiDiL34PEmIGHJGK/img/Actions/questionemailview.png?fit=max&auto=format&n=LiDiL34PEmIGHJGK&q=85&s=2ccaea13bcf7945d5e3e563a67fc4915" width="2428" height="1010" data-path="img/Actions/questionemailview.png" />
</Frame>

***

## Ask a question via email using an SMTP server

This action works the exact same way as the [Ask a question via E-mail](#creating-a-workflow-using-the-ask-a-question-via-email-action) however it allows you to *Ask a question via E-mail* using a **SMTP Server**

<Frame>
  <img src="https://mintcdn.com/blinkops-2/LiDiL34PEmIGHJGK/img/Actions/questionemailSMPT.png?fit=max&auto=format&n=LiDiL34PEmIGHJGK&q=85&s=05ccb77829bbd344ed14f46ca122c58f" width="896" height="772" data-path="img/Actions/questionemailSMPT.png" />
</Frame>

In order to use this action, you need to create a connection by navigating to the top-right hand corner of your Step, select "Connection required" and then select an existing connection or create a new connection by selecting **Create new connection**. Select the **SMTP Server** option and fill out all the necessary fields and then click create connection

<Frame>
  <img src="https://mintcdn.com/blinkops-2/LiDiL34PEmIGHJGK/img/Actions/emailsmptconnection.png?fit=max&auto=format&n=LiDiL34PEmIGHJGK&q=85&s=2230a6a5373481916b0d630aa16407b2" width="1086" height="1294" data-path="img/Actions/emailsmptconnection.png" />
</Frame>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.