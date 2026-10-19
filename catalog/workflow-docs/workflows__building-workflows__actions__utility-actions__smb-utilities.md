> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SMB Utilities

> Manage files and directories on remote SMB shares.

All SMB actions require an SMB connection. For setup instructions, refer to the [SMB integration](/docs/integrations/smb) page.

## Create Directory On SMB

Create a new directory on a remote SMB share.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | SMB Share Name | The name of the SMB share. For example - `SharedFolder`. |
  | Directory Path | The directory path to create within the SMB share. For example - `Documents/NewFolder`.<br /><br />**Note:** The parent directory must exist before executing the action. |
</div>

## Download File from SMB

Download a file from a remote SMB share to the local filesystem.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | SMB Share Name | The name of the SMB share. For example - `SharedFolder`. |
  | Remote File Path | The file path within the SMB share to download. For example - `Documents/report.txt`. |
  | Local File Path | The destination file path to save to within the working directory. For example - `report.txt`.<br /><br />**Note:** If the local file path contains directories, those directories must exist otherwise the file won't be downloaded. |
  | Working Directory | The directory where the downloaded file will be saved. The filesystem state is preserved across steps using this directory, ensuring that files and changes persist for continuity.<br /><br />For more information, refer to the [Create Working Directory](/docs/workflows/building-workflows/actions/utility-actions/file_system-utilities#create-working-directory) action documentation for guidance on setting up and selecting working directories. |
</div>

## List SMB Directory Contents

List files and subdirectories in a directory on a remote SMB share.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | SMB Share Name | The name of the SMB share. For example - `SharedFolder`. |
  | Directory Path | The directory path within the SMB share to list. Leave empty to list the SMB share root. For example - `Documents`. |
  | Filter | A pattern to filter the listed files and folders, leave empty to list all. For example - `*.txt` to list only text files, or `report*` to list files or directories starting with "report". |
</div>

## List SMB Shares

List all available SMB shares on a remote SMB server.

## Remove Directory From SMB

Remove a directory from a remote SMB share.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | SMB Share Name | The name of the SMB share. For example - `SharedFolder`. |
  | Directory Path | The directory path to remove within the SMB share. For example - `Documents/OldFolder`.<br /><br />**Note:** To remove a non-empty directory, the `Recursive Delete` checkbox must be enabled. |
  | Recursive Delete | Select to remove the directory recursively.<br /><br />**Note:** When selected, all files and subdirectories within the specified path will be deleted. |
</div>

## Remove File From SMB

Delete a file from a remote SMB share.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | SMB Share Name | The name of the SMB share. For example - `SharedFolder`. |
  | Remote File Path | The file path within the SMB share to delete. For example - `Documents/report.txt`. |
</div>

## Rename File On SMB

Rename or move a file on a remote SMB share.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | SMB Share Name | The name of the SMB share. For example - `SharedFolder`. |
  | Current File Path | The current file path within the SMB share. For example - `Documents/old_name.txt`. |
  | New File Path | The new file path within the SMB share. For example - `Documents/new_name.txt`. |
</div>

## Upload File To SMB

Upload a file from the local filesystem to a remote SMB share.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | SMB Share Name | The name of the SMB share. For example - `SharedFolder`. |
  | Remote File Path | The destination file path within the SMB share. For example - `Documents/report.txt`. |
  | File Path | The path of the file to upload. |
  | Working Directory | The directory where the file is located. The filesystem state is preserved across steps using this directory, ensuring that files and changes persist for continuity.<br /><br />For more information, refer to the [Create Working Directory](/docs/workflows/building-workflows/actions/utility-actions/file_system-utilities#create-working-directory) action documentation for guidance on setting up and selecting working directories. |
</div>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.