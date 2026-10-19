> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Date-Time Utilities

> Date and time manipulation tools for parsing, comparing, and converting timestamps across different formats and timezones.

## Convert Epoch To ISO 8601

Convert epoch timestamps to ISO 8601 format in the UTC timezone. The action accepts single timestamps, comma-separated list, or JSON arrays and automatically converts them to standardized datetime format. When a timezone is specified, the action adjusts the timestamps from UTC to the target timezone while maintaining ISO 8601 formatting.

**Note**: When a list of epochs is provided, the output will be in a JSON list format.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Epoch Timestamp | The epoch timestamp to convert.<br /><br />Supported Input Format Examples:<br />• `1627890123, 1627890723, 1627891323`<br />• `["1627890123", "1627890723", "1627891323"]`<br />• `[1627890123, 1627890723, 1627891323]`<br />• `1627890123`<br />• `"1627890123"` |
  | Timezone | Include a `timezone` string to convert the `UTC` timestamp to a different timezone. The timezone string must be selected from the dropdown list.<br />Examples: Europe/Andorra, Asia/Kabul. |
  | Epoch Unit | Select the epoch timestamp unit. Use `Seconds` for standard Unix timestamps. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/EWHcjTVAxWjYFJ82/img/Utilities/datetime_utilities-epochtoiso8601.png?fit=max&auto=format&n=EWHcjTVAxWjYFJ82&q=85&s=dde92ca208c461255f81da819dc734a7" width="2264" height="800" data-path="img/Utilities/datetime_utilities-epochtoiso8601.png" />
</Frame>

## Convert ISO 8601 To Epoch

Convert ISO 8601 timestamp(s) to Epoch time. This action accepts a JSON array, comma-separated list, or single ISO 8601 timestamp.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | ISO 8601 Timestamp | The ISO 8601 timestamp(s) to convert to epoch format. Can be a single timestamp, a comma-separated list, or a valid JSON array.<br /><br />For more information on ISO 8601 format, refer to [ISO 8601 standards documentation](https://www.iso.org/iso-8601-date-and-time-format.html). |
  | Output Format | Select whether to return epoch time as seconds or milliseconds.<br /><br />Options: `Seconds`, `Milliseconds`, `Minutes` or `Hours` <br /><br />Default: `Seconds` |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/aSwCm9AAnnCD7gkQ/img/Utilities/datetime_utilities-convertiso8601toepoch.png?fit=max&auto=format&n=aSwCm9AAnnCD7gkQ&q=85&s=07657e12bc577781388040dac18ee540" width="2582" height="878" data-path="img/Utilities/datetime_utilities-convertiso8601toepoch.png" />
</Frame>

## Find Earliest Date

Returns the earliest date from a given list of dates.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Date List | A comma separated list or JSON array containing date strings.<br /><br />Each date string can be in a variety of common date formats. For example:<ul><li>`YYYY-MM-DD`</li><li>`DD/MM/YYYY`</li><li>`YYYY-MM-DDTHH:MM:SS`</li><li>`YYYY-MM-DDTHH:MM:SS.sssZ`</li><li>`YYYY-MM-DDTHH:MM:SS.sss+hh:mm`</li><li>`YYYY-MM-DDTHH:MM:SS.sss-hh:mm`</li><li>`Unix Timestamp`</li></ul>**Note**: Input dates that are `Timezone Aware` cannot be used along with `Timezone Naive` dates. All dates should either be in UTC format or have a clearly defined timezone. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/I0bBfTOFYhQg2L0_/img/Utilities/date_time_utilities-earliestdate.png?fit=max&auto=format&n=I0bBfTOFYhQg2L0_&q=85&s=7170193e5bfd64ee9fd3ec8eb4584172" width="1992" height="876" data-path="img/Utilities/date_time_utilities-earliestdate.png" />
</Frame>

## Find Latest Date

Returns the latest date from a given list of dates.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Date List | A comma separated list or JSON array containing date strings.<br /><br />Each date string can be in a variety of common date formats. For example:<ul><li>`YYYY-MM-DD`</li><li>`DD/MM/YYYY`</li><li>`YYYY-MM-DDTHH:MM:SS`</li><li>`YYYY-MM-DDTHH:MM:SS.sssZ`</li><li>`YYYY-MM-DDTHH:MM:SS.sss+hh:mm`</li><li>`YYYY-MM-DDTHH:MM:SS.sss-hh:mm`</li><li>`Unix Timestamp`</li></ul>**Note**: Input dates that are `Timezone Aware` cannot be used along with `Timezone Naive` dates. All dates should either be in UTC format or have a clearly defined timezone. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/I0bBfTOFYhQg2L0_/img/Utilities/date_time_utilities-latest.png?fit=max&auto=format&n=I0bBfTOFYhQg2L0_&q=85&s=418359f62b079221be8307cc19b07ee0" width="1846" height="810" data-path="img/Utilities/date_time_utilities-latest.png" />
</Frame>

## Get Epoch Time

Gets an epoch time specific or relative to a given time.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Time | Can be a specific date and hour, or a relative range. |
  | Epoch Format | Whether to display the epoch time as seconds or milliseconds. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/I0bBfTOFYhQg2L0_/img/Utilities/date_time_utilities-getepochtime.png?fit=max&auto=format&n=I0bBfTOFYhQg2L0_&q=85&s=b11886f6764b79023ccdab4a2b484b60" width="1994" height="878" data-path="img/Utilities/date_time_utilities-getepochtime.png" />
</Frame>

## Get Time Difference Between Timestamps

Get Time Difference, in **Seconds**, Between Two Different Timestamps.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Timestamp 1 | The first Timestamp. Can be a specific date and hour, or a relative range. |
  | Timestamp 2 | The second Timestamp. Can be a specific date and hour, or a relative range. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/I0bBfTOFYhQg2L0_/img/Utilities/date_time_utilities-gettimediff.png?fit=max&auto=format&n=I0bBfTOFYhQg2L0_&q=85&s=7c0437d3f891bc1467d919313d440cb0" width="1990" height="878" data-path="img/Utilities/date_time_utilities-gettimediff.png" />
</Frame>

## Get Timezone

Gets the timezone identifier from a latitude/longitude pair or from the current workspace.

Can be used in conjunction with the `Get Timezone Offset` to get the amount of seconds after GMT.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Location Type | Choose how the location for the timezone should be provided. |
  | Latitude | The degrees latitude of the desired position to get the time for. |
  | Longitude | The degrees longitude of the desired position to get the time for. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/I0bBfTOFYhQg2L0_/img/Utilities/date_time_utilities-gettimezone.png?fit=max&auto=format&n=I0bBfTOFYhQg2L0_&q=85&s=bbdeed9d1301c78361bb2fe30c8975c4" width="1990" height="878" data-path="img/Utilities/date_time_utilities-gettimezone.png" />
</Frame>

## Get Timezone Offset

Gets the timezone offset (in seconds) relative to GMT from a IANA timezone identifier.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Timezone Identifier | The IANA timezone identifier, usually provided as `{Country}/{City}`.<br />If given `UTC`, returns the offset of UTC time (`0`).<br />Visit [Wikipedia](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List) for a frequently updated list of names.<br />For the most updated list, visit the [IANA registry](https://www.iana.org/time-zones) and download the distribution file. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/I0bBfTOFYhQg2L0_/img/Utilities/date_time_utilities-timezoneoff.png?fit=max&auto=format&n=I0bBfTOFYhQg2L0_&q=85&s=ee438c9328327fa1f27c1daa3ee058e4" width="1992" height="876" data-path="img/Utilities/date_time_utilities-timezoneoff.png" />
</Frame>

## Modify Date Time

Add or subtract seconds, minutes, hours, days, or years to or from the specified timestamp.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Time Value | The timestamp to modify. Can be either Epoch (Unix timestamp) or ISO 8601 format.<br /><br />**Examples**:<br />• Epoch: `1627890123`<br />• ISO 8601: `2021-08-02T12:02:03Z` |
  | Operation | Select whether to add or subtract time.<br /><br />Options: `Add`, `Subtract` |
  | Seconds | Number of seconds to add or subtract. |
  | Minutes | Number of minutes to add or subtract. |
  | Hours | Number of hours to add or subtract. |
  | Days | Number of days to add or subtract. |
  | Years | Number of years to add or subtract.<br /><br />**Note**: Leap years are handled automatically. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/aSwCm9AAnnCD7gkQ/img/Utilities/datetime_utilities-modifydatetime.png?fit=max&auto=format&n=aSwCm9AAnnCD7gkQ&q=85&s=5fb0123146f0301638989bcadb0ad67b" width="2584" height="876" data-path="img/Utilities/datetime_utilities-modifydatetime.png" />
</Frame>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.