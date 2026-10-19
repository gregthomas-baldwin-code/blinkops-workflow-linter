> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Action Error References

> Understand error structures and how to handle step-level errors in Blink workflow executions.

## Examples of Error Structure

<Tabs>
  <Tab title="Example One">
    ```json theme={"dark"}
    {
      "error_code": "InvalidStatusCodeBlinkHttpErr",
      "message": "Blink received an invalid status code after sending an HTTP request to the vendor",
      "data": {
        "request": {
          "host": "httpbin.org",
          "method": "GET",
          "path": "/status/500"
        },
        "response": {
          "body": "",
          "headers": {
            "Access-Control-Allow-Credentials": ["true"],
            "Access-Control-Allow-Origin": ["*"],
            "Content-Length": ["0"],
            "Content-Type": ["text/html; charset=utf-8"],
            "Date": ["Wed, 02 Aug 2023 08:04:20 GMT"],
            "Server": ["gunicorn/19.9.0"]
          },
          "status_code": 500
        }
      }
    }
    ```
  </Tab>

  <Tab title="Example Two">
    ```json theme={"dark"}
    {
      "error_code": "SlackChannelNotFoundBlinkHttpErr",
      "message": "Either the channel does not exist or in the case of a private channel, the Slack App specified in the connection may not be a part of the channel. For more information please see https://docs.blinkops.com/docs/integrations/slack#link-connection-to-a-specific-channel",
      "data": {
        "request": {
          "host": "slack.com",
          "method": "POST",
          "path": "/api/chat.postMessage"
        },
        "response": {
          "body": {
            "error": "channel_not_found",
            "ok": false
          },
          "headers": {
            "Access-Control-Allow-Headers": [
              "slack-route, x-slack-version-ts, x-b3-traceid, x-b3-spanid, x-b3-parentspanid, x-b3-sampled, x-b3-flags"
            ],
            "Access-Control-Allow-Origin": ["*"],
            "Access-Control-Expose-Headers": ["x-slack-req-id, retry-after"],
            "Cache-Control": ["private, no-cache, no-store, must-revalidate"],
            "Content-Length": ["40"],
            "Content-Type": ["application/json; charset=utf-8"],
            "Date": ["Wed, 02 Aug 2023 08:42:59 GMT"],
            "Expires": ["Sat, 26 Jul 1997 05:00:00 GMT"],
            "Pragma": ["no-cache"],
            "Referrer-Policy": ["no-referrer"],
            "Server": ["Apache"],
            "Strict-Transport-Security": [
              "max-age=31536000; includeSubDomains; preload"
            ],
            "Vary": ["Accept-Encoding"],
            "Via": [
              "1.1 slack-prod.tinyspeck.com, envoy-www-iad-zkbbofin, envoy-edge-dub-xxiobhim"
            ],
            "X-Accepted-Oauth-Scopes": ["chat:write"],
            "X-Backend": [
              "main_normal main_canary_with_overflow main_control_with_overflow"
            ],
            "X-Content-Type-Options": ["nosniff"],
            "X-Edge-Backend": ["envoy-www"],
            "X-Envoy-Upstream-Service-Time": ["83"],
            "X-Oauth-Scopes": [
              "channels:manage,channels:history,channels:read,chat:write,chat:write.public,groups:write,groups:read,groups:history,files:write,im:read,im:write,im:history,mpim:read,mpim:write,mpim:history,reactions:write,usergroups:write,users:read,users.profile:read,users:read.email,team:read"
            ],
            "X-Server": ["slack-www-hhvm-main-iad-jkkc"],
            "X-Slack-Backend": ["r"],
            "X-Slack-Edge-Shared-Secret-Outcome": ["no-match"],
            "X-Slack-Req-Id": ["147ce5feb7ec705030ac447e30724f8b"],
            "X-Slack-Shared-Secret-Outcome": ["no-match"],
            "X-Slack-Unique-Id": ["ZMoXE5U8lj8ns695KBe2tgAAEBA"],
            "X-Xss-Protection": ["0"]
          },
          "status_code": 200
        }
      }
    }
    ```
  </Tab>
</Tabs>

## Error Structure Explained

1. `error_code`: Is the name of the Error Code.

2. `message`: Provides a descriptive explanation of the error that occurred.

3. `data`: Contains any additional information related to the error being returned such as the request method, host and path.

4. `response`: Contains the `Headers` and the `body` of the request sent.

<Info>
  **NOTE**

  Please be aware that each error is unique. Consequently, some errors may encompass additional data fields, while others might have fewer data fields. This variation depends on the executed action and the specific error encountered. The above Error Structure serves as just one example among several different types of error structures. However, they consistently encompass the essential components of **error\_code, message, data and body**.
</Info>

## Error Types

<Tabs>
  <Tab title="HTTP ERRORS and REQUEST ERRORS">
    | Error Type | Error Code | Error Message |
    | - | - | - |
    | HTTP ERROR | BLINK\_HTTP\_ERR\_INVALID\_STATUS\_CODE | Blink received an invalid status code after sending an HTTP request to the vendor |
    | HTTP ERROR | BLINK\_HTTP\_ERR\_PAYLOAD\_ERROR | Blink received an error in the response body after sending an HTTP request to the vendor |
    | HTTP ERROR | BLINK\_HTTP\_ERR\_RATE\_LIMIT | Blink encountered a rate-limit after sending an HTTP request to the vendor |
    | HTTP ERROR | BLINK\_HTTP\_ERR\_RATE\_LIMIT\_TIMEOUT | The wait duration for API rate limit reset is longer than the request timeout |
    | REQUEST ERROR | BLINK\_HTTP\_ERR\_MISSING\_REQUIRED\_PARAM | Missing mandatory parameter `%s` |
    | REQUEST ERROR | BLINK\_HTTP\_ERR\_PAYLOAD\_LIMIT | Blink failed to parse the base URL (%s) for this action |
    | REQUEST ERROR | BLINK\_HTTP\_ERR\_BASE\_URL | Blink failed to join the base URL with the user's relative path for this action |
  </Tab>

  <Tab title="JIRA ERRORS">
    <div className="integrations-table">
      | Error Type | Error Code | Error Message |
      | - | - | - |
      | JIRA ERROR | BLINK\_HTTP\_ERR\_JIRA\_USER\_NOT\_FOUND | The user email input did not match any Jira user |
      | JIRA ERROR | BLINK\_HTTP\_ERR\_JIRA\_USER\_AMBIGUOS | The user email input matched more than one user |
    </div>
  </Tab>

  <Tab title="SLACK ERRORS">
    <div className="integrations-table">
      | Error Type | Error Code | Error Message |
      | - | - | - |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_UNMARSHAL\_OPEN\_CONVERSATIONS | Failed to unmarshal open conversations: %s |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_CHANNEL\_NOT\_FOUND. | Either the channel does not exist or in the case of a private channel, the Slack App specified in the connection may not be a part of the channel. For more information please see [https://docs.blinkops.com/docs/integrations/slack#link-connection-to-a-specific-channel](https://docs.blinkops.com/docs/integrations/slack#link-connection-to-a-specific-channel) |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_DUPLICATE\_CHANNEL\_NOT\_FOUND. | Channel associated with client\_msg\_id was invalid |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_DUPLICATE\_MESSAGE\_NOT\_FOUND. | No duplicate message exists associated with client\_msg\_id |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_NOT\_IN\_CHANNEL. | Cannot read/post user messages to a channel they are not in |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_IS\_ARCHIVED. | Channel has been archived |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_MSG\_TOO\_LONG. | Message text is too long |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_NO\_TEXT. | No message text provided |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_RESTRICTED\_ACTION. | A workspace preference prevents the authenticated user from posting |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_RESTRICTED\_ACTION\_READ\_ONLY\_CHANNEL | Cannot post any message into a read-only channel |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_RESTRICTED\_ACTION\_THREAD\_ONLY\_CHANNEL. | Cannot post top-level messages into a thread-only channel |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_RESTRICTED\_ACTION\_NON\_THREADABLE\_CHANNEL | Cannot post thread replies into a non\_threadable channel |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_RESTRICTED\_ACTION\_THREAD\_LOCKED. | Cannot post replies to a thread that has been locked by admins |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_PAYLOAD\_ERROR. | Blink received an error in the response body after sending an HTTP request to the vendor |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_TOO\_MANY\_ATTACHMENTS. | Too many attachments were provided with this message. A maximum of 100 attachments are allowed on a message |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_TOO\_MANY\_CONTACT\_CARDS. | Too many contact\_cards were provided with this message. A maximum of 10 contact cards are allowed on a message |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_RATE\_LIMITE. | Application has posted too many messages, read the Rate Limit documentation for more information |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_AS\_USER\_NOT\_SUPPORTED. | The as\_user parameter does not function with workspace apps |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_EKM\_ACCESS\_DENIED. | Administrators have suspended the ability to post a message |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_SLACK\_CONNECT\_FILE\_LINK\_SHARING\_BLOCKED. | Admin has disabled Slack File sharing in all Slack Connect communications |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_INVALID\_BLOCKS. | Blocks submitted with this message are not valid communications |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_INVALID\_BLOCKS\_FORMAT. | The blocks is not a valid JSON object or doesn't match the Block Kit syntax |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_TEAM\_ACCESS\_NOT\_GRANTED. | The token used is not granted the specific workspace access required to complete this request |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_NOT\_AUTHED. | No authentication token provided |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_INVALID\_AUTH. | Some aspect of authentication cannot be validated. Either the provided token is invalid or the request originates from an IP address disallowed from making the request |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_TOKEN\_REVOKED. | Authentication token is for a deleted user or workspace or the app has been removed when using a user token |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_TOKEN\_EXPIRED. | Authentication token has expired |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_NO\_PERMISSION | The workspace token used in this request does not have the permissions necessary to complete the request. Make sure your app is a member of the conversation it's attempting to post a message to |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_ORG\_LOGIN\_REQUIRED. | The workspace is undergoing an enterprise migration and will not be available until migration is complete |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_MISSING\_SCOPE. | The token used is not granted the specific scope permissions required to complete this request |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_NOT\_ALLOWED\_TOKEN\_TYPE. | The token type used in this request is not allowed |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_METHOD\_DEPRECATED. | The method has been deprecated |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_DEPRECATED\_ENDPOINT. | The endpoint has been deprecated |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_TWO\_FACTOR\_SETUP\_REQUIRED. | Two factor setup is required |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_ENTERPRISE\_IS\_RESTRICTED | The method cannot be called from an Enterprise |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_INVALID\_ARGUMENTS | The method was either called with invalid arguments or some detail about the arguments passed is invalid, which is more likely when using complex arguments like blocks or attachments |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_INVALID\_ARG\_NAME | The method was passed an argument whose name falls outside the bounds of accepted or expected values. This includes very long names and names with non-alphanumeric characters other than \_. If you get this error, it is typically an indication that you have made a very malformed API call |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_INVALID\_ARRAY\_ARG | The method was passed an array as an argument. Please only input valid strings |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_INVALID\_CHARSET | The method was called via a POST request, but the charset specified in the Content-Type header was invalid. Valid charset names are: utf-8 iso-8859-1 |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_INVALID\_FORM\_DATA | The method was called via a POST request with Content-Type application/x-www-form-urlencoded or multipart/form-data, but the form data was either missing or syntactically invalid |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_INVALID\_POST\_TYPE | The method was called via a POST request, but the specified Content-Type was invalid. Valid types are: application/json application/x-www-form-urlencoded multipart/form-data text/plain |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_MISSING\_POST\_TYPE | The method was called via a POST request and included a data payload, but the request did not include a Content-Type header |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_TEAM\_ADDED\_TO\_ORG | The workspace associated with your request is currently undergoing migration to an Enterprise Organization. Web API and other platform operations will be intermittently unavailable until the transition is complete |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_RATELIMITED | The request has been ratelimited. Refer to the Retry-After header for when to retry the request |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_ACCESSLIMITED | Access to this method is limited on the current network |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_REQUEST\_TIMEOUT | The method was called via a POST request, but the POST data was either missing or truncated |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_SERVICE\_UNAVAILABLE | The service is temporarily unavailable |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_FATAL\_ERROR | The server could not complete your operation(s) without encountering a catastrophic error. It's possible some aspect of the operation succeeded before the error was raised |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_INTERNAL\_ERROR. | The server could not complete your operation(s) without encountering an error, likely due to a transient issue on our end. It's possible some aspect of the operation succeeded before the error was raised |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_NAME\_TAKEN | A channel cannot be created with the given name |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_NO\_CHANNEL | Value passed for name was empty |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_INVALID\_NAME\_REQUIRED | Value passed for name was empty |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_INVALID\_NAME\_PUNCTUATION | A value passed for name contained only punctuation |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_INVALID\_NAME\_MAXLENGTH | Value passed for name exceeded max length |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_INVALID\_NAME\_SPECIALS | Value passed for name contained unallowed special characters or uppercase characters |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_INVALID\_NAME | Value passed for name was invalid |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_TOO\_MANY\_CONVOS\_FOR\_TEAM | The workspace has exceeded its limit of public and private channels |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_CANNOT\_CREATE\_CHANNEL | This channel is unable to be created |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_MISSING\_ARGUMENT | A required argument is missing |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_FEATURE\_NOT\_ENABLED | Two factor setup is required |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_CHANNEL\_TYPE\_NOT\_SUPPORTED | The provided channel\_id was a DM, MPDM, or the 'general' channel |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_DEFAULT\_ORG\_WIDE\_CHANNEL | Users may not be invited to the default org-wide channel |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_USER\_MUST\_BE\_ADMIN | The token provided must be associated with an Org Admin or Owner |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_FAILED\_FOR\_SOME\_USERS | The method failed for a subset of the users passed |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_NOT\_REACTABLE | Whatever you passed in, like a file or file\_comment, can't be reacted to anymore. Your app can react to messages though |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_TOO\_MANY\_EMOJI | The limit for distinct reactions (i.e emoji) on the item has been reached |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_MESSAGE\_NOT\_FOUND | Message specified by channel and timestamp does not exist |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_ALREADY\_REACTED | The specified item already has the user/reaction combination |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_BAD\_TIMESTAMP | Value passed for timestamp was invalid |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_TOO\_MANY\_REACTIONS | The request has been ratelimited. Refer to the Retry-After header for when to retry the request |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_NO\_ITEM\_SPECIFIED | Combination of channel and timestamp was not specified |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_EXTERNAL\_CHANNEL\_MIGRATING | The channel is in the process of being migrated |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_THREAD\_LOCKED | Reactions are disabled as the specified message is part of a locked thread |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_TEAM\_NOT\_FOUND | team\_id was not found |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_INVALID\_EMAIL | Email address was not valid |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_ALREADY\_IN\_TEAM | The user is already on the team |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_FAILED\_TO\_VALIDATE\_CUSTOM\_MESSAGE | extra\_message was invalid |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_USER\_DISABLED | The user is disabled |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_FAILED\_TO\_SEND\_INVITE | The invite failed to send |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_ALREADY\_IN\_TEAM\_INVITED\_USER | The user has already been invited to the team |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_FAILED\_TO\_VALIDATE\_CUSTOM\_MESSAGE | The extra\_message was invalid |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_FAILED\_LOOKING\_UP\_USER | We couldn't find the requested user |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_EDIT\_WINDOW\_CLOSED | The message cannot be edited due to the team message edit settings |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_FAILED\_TO\_VALIDATE\_CALLER | The token calling this method doesn't have permission to invite a user |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_USERS\_NOT\_FOUND | The Value passed for user was invalid |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_FAILED\_TO\_VALIDATE\_TEAM | The team calling this method was invalid |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_POSTING\_TO\_GENERAL\_CHANNEL\_DENIED | An admin has restricted posting to the #general channel |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_FAILED\_TO\_VALIDATE\_CHANNELS | One or more channels supplied are invalid |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_SLACK\_CONNECT\_CLIP\_SHARING\_BLOCKED | Admin has disabled Clip sharing in Slack Connect channels |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_SLACK\_CONNECT\_FILE\_UPLOAD\_SHARING\_BLOCKED | Admin has disabled File uploads in all Slack Connect communications |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_FAILED\_TO\_VALIDATE\_EXPIRATION | The expiration\_ts was invalid |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_MALWARE\_DETECTED | This file may contain a virus or other malware and can't be uploaded to Slack |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_SLACK\_CONNECT\_BLOCKED\_FILE\_TYPE | File uploads with certain types are blocked in all Slack Connect communications |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_CANT\_UPDATE\_MESSAGE | Authenticated user does not have permission to update this message |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_CANT\_BROADCAST\_MESSAGE | Unable to broadcast this message |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_UPDATE\_FAILED | Internal update failure |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_EDIT\_WINDOW\_CLOSED | The message cannot be edited due to the team message edit settings |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_NO\_DUAL\_BROADCAST\_CONTENT\_UPDATE | Can't broadcast an old reply and update the content at the same time |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_IS\_INACTIVE | The message cannot be edited within a frozen, archived, or deleted channel |
      | SLACK ERROR | BLINK\_HTTP\_ERR\_SLACK\_INVALID\_ATTACHMENTS | The attachments were invalid |
    </div>
  </Tab>
</Tabs>

## Generic Rate-Limit

Rate limiting controls how often requests can be made to a system or service. It sets a maximum number of requests allowed within a certain period (seconds, minutes, or hours). When this limit is reached, the system may delay or reject further requests until the next time period starts. Blink handles rate limit errors automatically. This is how we do it:

In the Blink Ops Editor, when sending an HTTP request as part of an action, if the Blink system receives the response code `429`, it indicates that the generic rate limit has been reached. Additionally, the presence of headers `X-RateLimit-Remaining` or `X-Rate-Limit-Remaining` with a value of `0` confirms this limit has been reached.

The system will then check for the `X-RateLimit-Reset` and `X-Rate-Limit-Reset` headers. If these headers are present, they provide an epoch time indicating when you can resume sending requests. The system will automatically retry at that specified time.

Additionally, if the `Retry-After` header is found, it indicates the number of seconds to wait before retrying. The system will automatically retry after the specified duration.

In the absence of these headers, the system will employ an exponential backoff strategy, starting with a delay of `100ms`. The retries will continue until the step reaches its configured timeout. If the required wait duration for the API rate limit reset exceeds the step timeout, the following message will be returned: “The wait duration for API rate limit reset is longer than the request timeout”.

In [HTTP actions](/docs/workflows/building-workflows/actions/basic-actions/http-actions/http-actions), the advanced settings include an option to **Retry on Rate Limit**. This feature can be enabled by checking the corresponding box. To disable it, simply uncheck the box.

<Note>**Note:** In all other HTTP-based actions available on the Blink Platform, the **Retry on Rate Limit** feature is always automatically enabled.</Note>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/-eoT09amno25RB5l/img/Actions/GenericRateLimit.png?fit=max&auto=format&n=-eoT09amno25RB5l&q=85&s=d9a134b6b7ac71448f13eb479b6647a1" width="3584" height="1992" data-path="img/Actions/GenericRateLimit.png" />
</Frame>

<Tip>
  **TIP**

  To prevent these errors, we recommend reducing the number of requests sent through the chosen HTTP action.
</Tip>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.