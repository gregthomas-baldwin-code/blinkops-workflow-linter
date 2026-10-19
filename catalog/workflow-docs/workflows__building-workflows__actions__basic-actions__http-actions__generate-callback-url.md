> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Generate Callback URL Action

> Generate callback URLs to receive asynchronous responses and webhook data in Blink workflows.

## Generate Callback URL Action

<Note> Generate callback URLs to receive asynchronous responses and webhook data in Blink workflows.</Note>

The **Generate Callback URL** action creates a unique, temporary URL that external systems can use to send data back to your workflow.

To send data back through the callback URL, the request must be authenticated. You can authenticate in either of these ways:

* **Callback URL API Key** – Enable the "Include API Key" option. This creates an API key and embeds it in the callback URL. Use this same key when you send the response.
* **[Blink API Key](https://docs.blinkops.com/docs/blink-platform/account-management/api-keys)** – Send the response with a valid Blink API Key that has workflow-execution permissions.

To leverage this callback URL, you need to:

1. Send it to the external system (e.g. via a custom HTTP request).
2. Add a [Wait Action](https://docs.blinkops.com/docs/workflows/building-workflows/actions/basic-actions/flow-control-actions#wait) to the following step to pause the workflow until the callback response is received. When data is sent to the callback URL, the workflow automatically resumes and continues to the next step using the data returned by the external system.

<Frame>
  <img src="https://mintcdn.com/blinkops-2/Bqx0vG0GE-s9GMJB/img/Actions/CallbackURL.png?fit=max&auto=format&n=Bqx0vG0GE-s9GMJB&q=85&s=eb5c518391b47d562a5bc4e165a2810b" width="1154" height="392" data-path="img/Actions/CallbackURL.png" />
</Frame>

***

## Handling Callback Responses in Workflows

After generating a Callback URL using the Generate Callback URL action, immediately add a [Wait Action](https://docs.blinkops.com/docs/workflows/building-workflows/actions/basic-actions/flow-control-actions#wait) to the next step. This pauses workflow execution while the external service completes its process and sends back data upon completion.

<Frame>
  <img src="https://mintcdn.com/blinkops-2/Bqx0vG0GE-s9GMJB/img/Actions/CallbackWaitAction.png?fit=max&auto=format&n=Bqx0vG0GE-s9GMJB&q=85&s=ac1d10986c067773c03115e9911916b3" width="3456" height="2160" data-path="img/Actions/CallbackWaitAction.png" />
</Frame>

***

## Configuring the Third-Party System to Respond

Once the external system receives the callback URL, it needs to be configured to send its response back to Blink. Here's exactly how to do that.

### Request Method and URL

The external system must send an **HTTP POST** request to the callback URL provided by Blink.

```bash theme={"dark"}
POST <callback_url>
```

### Request Headers

Include the following headers in the request:

| Header | Value |
| - | - |
| `Content-Type` | `application/json` |
| `Authorization` | `Bearer <your-api-key>` *(if not embedded in the URL)* |

**Authentication options:**

* **If you enabled "Include API Key"** when generating the callback URL, the API key is already embedded in the URL. No `Authorization` header is needed.
* **If you are using a Blink API Key**, pass it as a Bearer token in the `Authorization` header:

  ```bash theme={"dark"}
  Authorization: Bearer <your-blink-api-key>
  ```

### Request body

Send the response data as a **JSON object** in the request body. Blink will make this data available to subsequent steps in your workflow.

```json theme={"dark"}
{
  "status": "completed",
  "ticket_id": "TKT-4821",
  "assigned_to": "jane.doe@example.com",
  "sla_due": "2025-06-10T14:00:00Z"
}
```

Any valid JSON structure is accepted — Blink passes the full body to the next workflow step as-is.

### Example: cURL

```bash theme={"dark"}
curl -X POST "<callback_url>" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <your-blink-api-key>" \
  -d '{
    "status": "completed",
    "ticket_id": "TKT-4821",
    "assigned_to": "jane.doe@example.com",
    "sla_due": "2025-06-10T14:00:00Z"
  }'
```

<Note> If the API key is embedded in the callback URL, you can omit the `Authorization` header entirely. </Note>

### What Happens After the Response is Sent

Once Blink receives a valid POST request at the callback URL:

1. The **[Wait Action](https://docs.blinkops.com/docs/workflows/building-workflows/actions/basic-actions/flow-control-actions#wait)** is released and workflow execution resumes.
2. The JSON body from the response is available as output data in all subsequent workflow steps.
3. The callback URL is invalidated- it can only be used once per workflow execution.

***

## Example Use Case

Callback URLs are especially useful in workflows that involve asynchronous interactions with third-party systems.

For example, a customer uses Blink to automate support ticket triage:

* When an end user submits a support request through the customer's support portal, a Blink workflow is triggered to create a corresponding ticket in the external ticketing system (passing along the callback URL).
* After creating the ticket, the [Wait Action](https://docs.blinkops.com/docs/workflows/building-workflows/actions/basic-actions/flow-control-actions#wait) pauses the workflow until the ticket is assigned and its SLA is defined on the ticketing system's side.
* Once those updates occur, the ticketing system sends the relevant details back to Blink via an HTTP POST to the callback URL, with the ticket data as a JSON body.
* Blink resumes the workflow and passes the updated ticket information to the next step.

In this scenario, the callback URL enables smooth, secure coordination between Blink and the external ticketing platform, allowing the workflow to handle asynchronous operations seamlessly.

<Frame>
  <img src="https://mintcdn.com/blinkops-2/A3Cskmxe1KKs_WFj/img/Actions/GenerateCallbackURLExample.png?fit=max&auto=format&n=A3Cskmxe1KKs_WFj&q=85&s=3fd7cfa206f4ef99b58d03a78c686927" width="1726" height="1085" data-path="img/Actions/GenerateCallbackURLExample.png" />
</Frame>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.