> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using Files in Workflows

> Work with files in Blink workflows, including uploading, downloading, and passing files between steps.

The files mechanism allows Workflows builders to create, edit and use files which are persisted between executions of steps in a Workflow. The lifespan of files is aligned with the lifespan of the execution of the Workflow - when the execution is finished, the files are deleted.

## File object

Each file object contains 3 fields:

1. `identifier`, which is the unique identifier of the file.

   * This field is used in various actions including [upload file](/docs/workflows/building-workflows/actions/basic-actions/http-actions/http-actions#send-http-upload-file-request) or [send file via Slack](/docs/integrations/slack/actions/send-file).

2. `size`, which is the size of the file in bytes.

3. `path`, which is the absolute path to the file:

   * This field can be used in [Bash](/docs/workflows/building-workflows/actions/basic-actions/code-actions)/[Python](/docs/workflows/building-workflows/actions/basic-actions/code-actions) steps when you want to perform some action on the file (e.g. if you want to print the file in [Bash](/docs/workflows/building-workflows/actions/basic-actions/code-actions), you can run the `cat` command and use the file path as the argument).

## Expression Language and Variable Picker Support

When creating the Workflow, the file objects are available in the variable picker under the files section.

1. To access the `File Identifier`, `File Path` and the `File Size`, use the [variable picker](/docs/workflows/building-workflows/dynamic-variables/variable-picker#using-the-variable-picker-to-add-dynamic-variables) under the [files](/docs/workflows/building-workflows/dynamic-variables/variable-picker#dynamic-variables-types)

2. Select `WorkingDirectory` under the [file](/docs/workflows/building-workflows/dynamic-variables/variable-picker#dynamic-variables-types) section of the Variable Picker.

<Frame>
  <img src="https://mintcdn.com/blinkops-2/XMlZfP6f_keDWota/img/Actions/VarPickerFiles.png?fit=max&auto=format&n=XMlZfP6f_keDWota&q=85&s=21c9df7fe62b791abb4fcc116af39960" width="1725" height="1079" data-path="img/Actions/VarPickerFiles.png" />
</Frame>

3. Then choose `WorkingDirectory|identifier`, `WorkingDirectory|path` or `WorkingDirectory|size` according to the respective inputs.

<Frame>
  <img src="https://mintcdn.com/blinkops-2/ZUtie3exEe7_7B_M/img/Actions/FileObjectVarPicker.png?fit=max&auto=format&n=ZUtie3exEe7_7B_M&q=85&s=751e69f8a2cf50b47a36e4ce01c05528" width="1727" height="1073" data-path="img/Actions/FileObjectVarPicker.png" />
</Frame>

4. [Blink's Expression Language](/docs/workflows/building-workflows/dynamic-variables/expression-language/workflow-engine-functions) supports accessing the file objects using the `get_file` function.

```js theme={"dark"}
{{get_file("WorkingDirectory").identifier}}
```

<Frame>
  <img src="https://mintcdn.com/blinkops-2/XMlZfP6f_keDWota/img/Actions/VarPickFileExpressionLanguage.png?fit=max&auto=format&n=XMlZfP6f_keDWota&q=85&s=aaec2afbb838e8da0387303c2638bd3b" width="1719" height="1078" data-path="img/Actions/VarPickFileExpressionLanguage.png" />
</Frame>

* It returns an object containing the 3 fields: the files `identifier`, `path` and `size`

<Frame>
  <img src="https://mintcdn.com/blinkops-2/-eoT09amno25RB5l/img/Actions/GetFileExpressionLanguage.png?fit=max&auto=format&n=-eoT09amno25RB5l&q=85&s=09930eb38c3de602458e50219aaf75a3" width="1724" height="1075" data-path="img/Actions/GetFileExpressionLanguage.png" />
</Frame>

## Limitations

Each execution may create up to `100` files with a total size of `30 GiB` (gibibytes).

The maximum size for each file is `10GiB` (gibibytes).

## Example Use Cases

* [Download a file](/docs/workflows/building-workflows/actions/utility-actions/file_system-utilities#download-file-from-url) and [send it via Slack](/docs/integrations/slack/actions/send-file).

* Create a file using [Bash](/docs/workflows/building-workflows/actions/basic-actions/code-actions)/[Python](/docs/workflows/building-workflows/actions/basic-actions/code-actions) and [upload it to a remote server](/docs/workflows/building-workflows/actions/basic-actions/http-actions/http-actions).

* Generate a [Steampipe Report](/docs/workflows/building-workflows/actions/advanced-actions/database-actions/steampipe-report-actions) as a file and [send it as an attachment in an email](/docs/workflows/building-workflows/actions/advanced-actions/email-actions).


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.