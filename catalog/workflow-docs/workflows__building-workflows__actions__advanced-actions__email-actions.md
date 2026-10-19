> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Email Actions

> The Blink platform enables you to send e-mails both using an SMTP server and on behalf of Blink and get e-mails using IMAP server.

<CardGroup>
  <Card title="Send Email via Blink" icon="envelope" href="#send-email-via-blink" iconType="solid" horizontal />

  <Card title="Send Email via an SMTP Server" icon="server" href="#send-email-via-an-smtp-server" iconType="solid" horizontal />

  <Card title="List Email Messages via IMAP" icon="list" href="#list-email-messages-via-imap" iconType="solid" horizontal />

  <Card title="Send an Email via Gmail" icon="envelope" href="#send-email-via-gmail" iconType="solid" horizontal />
</CardGroup>

The Blink platform enables you to trigger a workflow on every new email message using an IMAP server.

<CardGroup>
  <Card title="On New Message" icon="envelope" href="#on-new-message" iconType="solid" horizontal />
</CardGroup>

<Note>
  When configuring email actions, you can choose to write the content using either **Markdown** or **HTML** syntax.

  1. **Using Markdown (`md`)**:
     * Set the **Content Field Type** parameter to **rich text**.
     * This enables a [rich text editor](/docs/blink-platform/interface-components/rich-text-editor) that supports Markdown formatting.

  2. **Using HTML**:
     * Set the **Content Field Type** parameter to **regular text**.
     * Additionally, set the **Content Type** parameter to `"text/html"`.
     * This allows you to write content using HTML syntax.

  Ensure you configure these parameters correctly based on your preferred formatting style.
</Note>

## SMTP Email

### Creating an SMTP Email Server connection

To create the connection you need:

* A username
* A password
* An SMTP host
* An SMTP port

#### Creating your connection

1. In the Blink platform, navigate to the **Connections** page > **Add connection**. A New Connection dialog box opens displaying icons of external service providers available.
2. Select the **SMTP Email Server** icon. A dialog box with name of the connection and connection methods appear.
3. (Optional) Edit the name of the connection. At a later stage you cannot edit the name.
4. Select **SMTP Email Server** as the method to make the connection.
5. Fill in the parameters:
   * A username
   * The password
   * The SMTP host
   * The SMTP port
6. (Optional) Click **Test Connection** to test it.
7. Click **Create connection**. The new connection appears on the **Connections** page.

### Actions

#### Send Email via an SMTP Server

Send an e-mail using an SMTP server.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | From | The email address used to deliver the message. This address should be a verified sender in your SMTP server. |
  | To | List of addresses - each one on a different line - to send the email to. |
  | Subject | This is the subject of the mail. |
  | Content | The body of the mail, write up your mail to send as you wish. |
  | Sender Display Name | The sender's name to be displayed to the recipient (if not specified, defaults to the email's domain name). |
  | Content Type | Representation of the Content-Type in the email body content. |
  | Custom Headers | The custom headers to add to the email. For Example: Header1:Value1 Header2:Value2 ... |
  | Attachment Name | The name of the attachment. |
  | Attachment Files | A comma-separated list of file identifiers for the attachment. |
  | Attachment Body | The body of the attachment. |
</div>

## IMAP Email

### Creating an IMAP Email Server connection

To create the connection you need:

* A username
* A password
* An IMAP host
* An IMAP port

#### Creating your connection

1. In the Blink platform, navigate to the **Connections** page > **Add connection**. A New Connection dialog box opens displaying icons of external service providers available.
2. Select the **IMAP Email Server** icon. A dialog box with name of the connection and connection methods appear.
3. (Optional) Edit the name of the connection. At a later stage you cannot edit the name.
4. Select **IMAP Email Server** as the method to make the connection.
5. Fill in the parameters:
   * A username
   * The password
   * The IMAP host
   * The IMAP port
6. (Optional) Click **Test Connection** to test it.
7. Click **Create connection**. The new connection appears on the **Connections** page.

### Actions

#### List Email Messages via IMAP

List email messages for specific email address.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Filter Since Date | Filters emails sent from the specified date onward. |
  | Include Seen Emails | When checked, all emails including those already seen will be displayed. If unchecked, only unseen email messages will be displayed. |
  | Limit | The maximum number of email messages returned. |
</div>

### Triggers

#### On New Message

Triggers a workflow on every new message.

##### Sample Event

```json theme={"dark"}
{
  "date": "2022-12-20T11:22:45+02:00",
  "subject": "test",
  "from": [
    {
      "PersonalName": "John Doe",
      "AtDomainList": "",
      "MailboxName": "John",
      "HostName": "john@test.com"
    }
  ],
  "sender": [
    {
      "PersonalName": "John Doe",
      "AtDomainList": "",
      "MailboxName": "John",
      "HostName": "john@test.com"
    }
  ],
  "reply_to": [
    {
      "PersonalName": "John Doe",
      "AtDomainList": "",
      "MailboxName": "John",
      "HostName": "john@test.com"
    }
  ],
  "to": [
    {
      "PersonalName": "Bar Foo",
      "AtDomainList": "",
      "MailboxName": "foo",
      "HostName": "foo@test.com"
    }
  ],
  "cc": null,
  "bcc": null,
  "in_reply_to": "",
  "message_id": "<CAGRyKpNGHkvieaAoAPPUP=wSshQdSzaavp1_qW_ieMGAMaS88Q@mail.gmail.com>",
  "body": "this is a test body"
}
```

## Blink Email

### Actions

#### Send Email via Blink

Send an e-mail on behalf of Blink.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Recipient | The email address of the recipient. |
  | Subject | The subject of the email. |
  | Content Field Type | The type of content to send:<br />• `Regular Text` - Send a plain text message.<br />• `Rich Text` - Send an HTML-formatted message with styling and structure. |
  | Content | The body of the email as plain text (for Regular Text) / The HTML body of the email (for Rich Text).<br /><br />For Rich Text example:<br /><pre><code>\<h1>Your Weekly Update\</h1><br />\<p>This is the update content.\</p></code></pre> |
  | Carbon Copy (CC) | A list of email addresses to receive a copy of the email, separated by new lines.<br /><br />For example:<br /><pre><code>[bob@example.com](mailto:bob@example.com)<br />[jane@example.com](mailto:jane@example.com)</code></pre>These recipients will be visible to all other recipients. |
  | Blind Carbon Copy (BCC) | A list of email addresses to receive a blind copy of the email, separated by new lines.<br /><br />For example:<br /><pre><code>[bob@example.com](mailto:bob@example.com)<br />[jane@example.com](mailto:jane@example.com)</code></pre>These recipients will not be visible to other recipients. |
  | Content Type | The representation of the `Content-Type` header in the email body content.<br /><br />**Important**: Make sure to select the `text/html` when using `Rich Text`. |
  | Custom Headers | A list of custom headers to add to the email.<br /><br />For example:<br /><pre><code>Header1:Value1<br />Header2:Value2</code></pre> |
  | Attachment Files | A comma-separated list of file identifiers to attach to the email. |
  | Custom Attachment Name | The name for a custom attachment file. |
  | Custom Attachment Body | The content for a custom attachment file. |
</div>

## Send Email Via Gmail

Create the connection by using one of the following methods:

* [Gmail](/docs/integrations/gmail)
* [Service Account](/docs/integrations/gmail)

\*\* Ensure the relevant APIs from the following list are enabled: \*\*

* [Gmail API](https://console.cloud.google.com/apis/api/gmail.googleapis.com)

### Creating your connection

1. In the Blink platform, navigate to the Connections page > Add connection. A New Connection dialog box opens displaying icons of external service providers available.
2. Select the Gmail icon. A dialog box with name of the connection and connection methods appear.
3. Edit the name of the connection. At a later stage you cannot edit the name. (Optional)
4. Click Gmail to authenticate using OAuth.
5. Sign in using your credentials.

## Parameters

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Attachment Files | A comma-separated list of file identifiers for the attachment. |
  | Bcc | A comma-separated list of emails for BCC recipients of the message. |
  | CC | A comma-separated list of email for CC recipients of the message. |
  | Content | The body of the mail. |
  | From User ID | The email of the user from which to send the email.<br />The special value 'me' can be used if the connection is OAuth to identify as the authenticated user. |
  | Subject | This is the subject of the mail. |
  | To | A comma-separated list of email recipients for the message. |
</div>

## Example Output

```json theme={"dark"}
{
  "id": "1879ef5cc8e70395",
  "threadId": "1879ef5cc8e70395",
  "labelIds": ["UNREAD", "SENT", "INBOX"]
}
```


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.