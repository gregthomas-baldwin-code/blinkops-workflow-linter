> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Copy-Paste curl Commands

> HTTP steps can easily be created by copying cURL commands and pasting them on the edit screen.

# Copy-Paste cURL Commands

The *Copy-Paste cURL Command* feature allows you to effortlessly create and send `HTTP` requests by using keyboard shortcuts to copy (`Cmd` + `C` on macOS or `Ctrl + C` on Windows) and paste (`Cmd + V` on macOS or `Ctrl + V` on Windows) `cURL` commands directly into the Workflow Editor. This streamlines workflow setup, making it faster, more intuitive, and more efficient.

* If a valid `cURL` command is pasted in a Workflow step, it will be parsed into a [Send HTTP action](/docs/workflows/building-workflows/actions/basic-actions/http-actions/http-actions#send-http-request) with the [supported parameters](#supported-parameters).

* The [Send HTTP action](/docs/workflows/building-workflows/actions/basic-actions/http-actions/http-actions) created by copying and pasting the `cURL` command in a Workflow Step, will be added last to the list of actions that the Workflow steps may already have.

## Supported Parameters

<Info>
  * When a `cURL` command is pasted into the Workflow Editor, only [supported parameters](#supported-parameters) are processed. Unsupported parameters are ignored and skipped.

  * If any part of the `cURL` command is invalid, an error or a warning message will pop up in the bottom-right corner of the Workflow Editor and inform you of the issue.
</Info>

**Blink supports the following parameters:**

<div className="integrations-table">
  | Parameter | Aliases | Description |
  | - | - | - |
  | Request | `[-X, --request ] <command>` | Specifies the HTTP method (e.g., `GET`, `POST`, `PUT`, `DELETE`) to use. |
  | Data | `[-d, --data ] <data>` | Sends the specified data in request to the HTTP server. |
  | Header | `[-H, --header ] <header>` | Adds a custom header to the request. |
  | Cookie | `[-b, --cookie ] <header>` | Sends the specified data as a cookie in the request. |
  | Insecure | `['-k', '--insecure']` | Disables SSL certificate validation. |
  | Basic Authentication | `['-u', '--user'] <user:password>` | Encodes credentials in Base64 and adds them to the request header. |
  | User Agent | `['-A', '--user-agent']` | A string sent by your browser or app that tells servers and networks which application, operating system, version, and vendor you’re using to make the request. |
  | GET flag | `['-G', '--get']` | Forces the request type to `GET`. |
  | Head flag | `['-I', '--head']` | Forces the request type to `HEAD`. |
</div>

<Info>
  The `GET flag` (`-G` or `--get`) forces the `HTTP` request type to `GET`, but it can be overridden by the `-X` or `--request` flag. The `X` flag explicitly sets the request method (e.g., POST, PUT, DELETE), and if both flags are used, `-X` takes precedence. Use these options carefully to ensure your intended `HTTP` request type is correctly configured.
</Info>

## How to use the Copy-Paste cURL Commands in the Workflow Editor

1. **Start by copying a cURL command**

   **For example**:

```bash theme={"dark"}
  curl -X POST \
     -d '{"name": "John Doe", "email": "john.doe@example.com"}' \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -b "session_id=abcd1234; theme=dark" \
     -k \
     -u "username:password" \
     -A "MyApp/1.0 (Linux; x86_64)" \
     -G \
     "https://api.example.com/users/profile" 

```

2. **Open the Workflow Editor:** Navigate to the [Workflow Editor](/docs/workflows/building-workflows/workflow-editor) where you want to add the `cURL` command.

3. **Paste the command:** Use the keyboard shortcut `Cmd + V` (or `Ctrl + V` on Windows) to paste the `cURL` command directly into the Workflow Editor. It will automatically parse into a structured `HTTP` Action.

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/blinkops-2/img/Actions/CopyPasteCurlCommand.gif" />
</Frame>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.