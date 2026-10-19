> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# HTTP Actions

> The Blink platform offers various HTTP actions such as GET, POST, PATCH, PUT, DELETE, HEAD, OPTIONS, and GraphQL.

## Actions

### Send HTTP Request

Execute an HTTP request with the chosen method on a provided URL.

| Parameter | Description |
| - | - |
| Method | The HTTP method to use in the request. |
| URL | The URL to communicate with. |
| Body | The content of the request body. |
| Headers | Request Headers to be added to the request, as a string in the format of `Name: Value`, separated by new lines.<br /><br />For example:<br /><pre><code>Content-Type: application/json<br />Accept: application/json</code></pre> |
| Cookies | Web cookies to include in the request in the format `Name: Value`, separated by new lines.<br /><br />For example:<br /><pre><code>Session: gr32tsd266yfg3u3t132kyl<br />Authentication: token123</code></pre> |
| Retry On Rate Limit | When checked, and rate limits are reached, the system will retry the HTTP request after the designated time period specified in the rate limit headers or through the use of exponential backoff. |
| Disable SSL Enforcement | When checked, the SSL verification of the server's certificate chain and host name will be skipped.<br /><br />This option may increase security vulnerabilities, but can be useful for testing or when custom verification is employed. |

### Send HTTP GraphQL Request

Executes GraphQL query on provided URL.

| Parameter | Description |
| - | - |
| URL | The URL to communicate with. |
| Query | GraphQL query. |
| Variables | GraphQL query variables. |
| Headers | Request Headers to be added to the request in the format Name: Value.<br />For example: `Content-Type: application/json`. |
| Retry On Rate Limit | If enabled, and when rate limits are reached, the system will retry the HTTP request after the designated time period specified in the rate limit headers or through the use of exponential backoff. |
| Disable SSL Enforcement | Enable this option to skip SSL verification of the server's certificate chain and host name. This may increase security vulnerabilities, but can be useful for testing or when custom verification is employed. |

### Send HTTP Upload File Request

Uploads a file to the provided URL using an HTTP request.

| Parameter | Description |
| - | - |
| Method | Which HTTP method to use in the file upload request. The default value for the request is POST. |
| URL | The URL to communicate with. |
| Body | The content of the request body. |
| Headers | Request Headers to be added to the request, as a string in the format of `Name: Value`, separated by new lines.<br /><br />For example:<br /><pre><code>Content-Type: application/json<br />Accept: application/json</code></pre> |
| File Identifier | The identifier of the file. You can create a file identifier using the [Set File Variable](/docs/workflows/building-workflows/actions/utility-actions/file_system-utilities) action. |
| File Param Name | The parameter name of the file to upload. |
| Cookies | Web cookies to include in the request in the format `Name: Value`, separated by new lines.<br /><br />For example:<br /><pre><code>Session: gr32tsd266yfg3u3t132kyl<br />Authentication: token123</code></pre> |
| Retry On Rate Limit | When checked, and rate limits are reached, the system will retry the HTTP request after the designated time period specified in the rate limit headers or through the use of exponential backoff. |
| Disable SSL Enforcement | When checked, the SSL verification of the server's certificate chain and host name will be skipped.<br /><br />This option may increase security vulnerabilities, but can be useful for testing or when custom verification is employed. |

<Note> Learn about how Blink handles [Rate Limits](/docs/workflows/building-workflows/error-handling/error#generic-rate-limit) automatically in HTTP requests.</Note>

## Standard non-authenticated HTTP requests

The most basic way to use HTTP Actions is without authentication.

## Authenticated HTTP requests to existing service providers

HTTP Actions can be used with most of the Blink connection types to send authenticated requests to existing service providers in Blink.
For example, to send an authenticated request to GitHub's API, use a GitHub connection.

<Frame>
  <img src="https://mintcdn.com/blinkops-2/LiDiL34PEmIGHJGK/img/Actions/http1.png?fit=max&auto=format&n=LiDiL34PEmIGHJGK&q=85&s=504274fc4a441842edb7b4b4da67083b" width="880" height="361" data-path="img/Actions/http1.png" />
</Frame>

## Authenticated HTTP requests to unsupported service providers

Blink adds support for additional service providers on a weekly basis. To use Actions with a service provider that is not currently supported, there are two options:

1. Contact the Blink team to request integration with a new service provider. [Contact us.](https://www.blinkops.com/contact-us/)
2. Use generic HTTP Actions to communicate with unsupported service providers, as explained below.

### Using generic HTTP actions to communicate with unsupported service providers

HTTP Actions can be used with one of the three HTTP connection types to send authenticated requests to service providers that aren't currently supported by Blink:

1. HTTP Basic Authentication
2. HTTP Bearer Authentication
3. HTTP Custom Authentication

For example, to communicate with a service provider called `X` that isn't supported by Blink and requires Basic Authentication:

1. Create an `HTTP Basic Authentication` connection with the required credentials.

   <Frame>
     <img src="https://mintcdn.com/blinkops-2/LiDiL34PEmIGHJGK/img/Actions/http2.png?fit=max&auto=format&n=LiDiL34PEmIGHJGK&q=85&s=27fa060df312fa92afff37162e80b4dc" width="748" height="616" data-path="img/Actions/http2.png" />
   </Frame>

2. Use the connection to perform the Action, and the outgoing HTTP request will be sent with the appropriate authentication headers.

   <Frame>
     <img src="https://mintcdn.com/blinkops-2/LiDiL34PEmIGHJGK/img/Actions/http3.png?fit=max&auto=format&n=LiDiL34PEmIGHJGK&q=85&s=b15742223557108989348a56c5332ade" width="894" height="371" data-path="img/Actions/http3.png" />
   </Frame>

## Usage Via Paste

HTTP steps can easily be created using the paste feature on the edit screen.
If a valid curl command is pasted, it will be parsed into an HTTP step with the appropriate request type, URL, body, headers, and cookies.
If a URL is pasted, an HTTP GET step will be created using the provided URL.

The HTTP actions created this way will be added last to the list of actions that the Workflow may already have.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.