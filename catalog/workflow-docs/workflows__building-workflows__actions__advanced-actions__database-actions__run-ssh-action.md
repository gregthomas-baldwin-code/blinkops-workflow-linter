> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Run SSH Action

> This action allows the user to perform SSH through Blink. Secure Shell (SSH) is a cryptographic network protocol for operating network services securely over an unsecured network.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Host | The host to connect to, can be ip address or hostname. |
  | Port | The SSH port. |
  | Command | The commands to run. |
  | Additional Error Validation | Select additional validation method to apply to the SSH response and determine the success/failure of the action:<br />• **Default (Bash)**: Relies on standard `Bash` exit codes (0 = success, non-zero = failure). This is the recommended option for most cases.<br />• **Regex**: Use a custom regular expression to detect errors in the command output. The action fails if the regex pattern matches any part of the output. Select this option for detecting specific error messages.<br />• **None**: No additional error validation is applied. Select this option when running commands that don't conform to standard conventions or when you intend to handle errors manually in your workflow. |
  | RegEx Pattern | The regular expression pattern used to detect errors in the command output. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/3_6WnkGGmnkZFzEe/img/Actions/RunSSHCommand.png?fit=max&auto=format&n=3_6WnkGGmnkZFzEe&q=85&s=981a1d541bc6ae0e71d360b05b86bf6b" width="1812" height="798" data-path="img/Actions/RunSSHCommand.png" />
</Frame>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.