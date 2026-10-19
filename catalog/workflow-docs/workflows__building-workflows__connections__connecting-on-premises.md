> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Connecting to an On-Premises App

> Connect Blink workflows to on-premises systems and private networks using self-hosted runners.

If your application is hosted on-premises and cannot be accessed by the [Blink Cloud Runner](/docs/blink-platform/runners/runners), you will need to take one of the following steps to establish a connection:

1. **Allow Cloud Access**: Open the necessary firewall ports to enable Blink Cloud Runners to reach your on-premises application.

**OR**

2. **Use a Self-Hosted Runner**: Set up a Self-Hosted Runner that has network access to the application.
   * Refer to the [Self-Hosted Runners](/docs/blink-platform/runners/secret-managers/hashicorp-vault) documentation for setup instructions.
   * Once the Runner is configured, you can select it when [testing your connection](/docs/workflows/building-workflows/connections/creating-connection).


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.