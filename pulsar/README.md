# Agent Check: Pulsar

## Overview

This check monitors [Pulsar][1] through the Datadog Agent.

## Setup

Follow the instructions below to install and configure this check for an Agent running on a host. For containerized environments, see the [Autodiscovery Integration Templates][2] for guidance on applying these instructions.

### Installation

To install the Pulsar check on your host:

1. Install the [developer toolkit](https://docs.datadoghq.com/developers/integrations/new_check_howto/#developer-toolkit) on any machine.
2. Clone the integrations-extras repository:

   ```shell
   git clone https://github.com/DataDog/integrations-extras.git.
   ```

3. Update your `ddev` config with the `integrations-extras/` path:

   ```shell
   ddev config set extras ./integrations-extras
   ```

4. To build the `Pulsar` package, run:

   ```shell
   ddev -e release build pulsar
   ```
5. [Download the Datadog Agent](https://app.datadoghq.com/account/settings#agent).
6. Upload the build artifact to any host with an Agent and run
   ```shell
   datadog-agent integration install -w path/to/pulsar/dist/<ARTIFACT_NAME>.whl
   ```

### Configuration

1. Edit the `pulsar.d/conf.yaml` file, in the `conf.d/` folder at the root of your Agent's configuration directory to start collecting your Pulsar performance data. See the [sample pulsar.d/conf.yaml][3] for all available configuration options.

2. [Restart the Agent][4].

### Validation

Run the [Agent's status subcommand][5] and look for `pulsar` under the Checks section.

## Data Collected

### Metrics

See [metadata.csv][6] for a list of metrics provided by this check.

### Service Checks

pulsar does not include any service checks.

### Events

pulsar does not include any events.

## Troubleshooting

Need help? Contact [Datadog support][7].

[1]: https://pulsar.apache.org/
[2]: https://docs.datadoghq.com/agent/kubernetes/integrations/
[3]: https://github.com/DataDog/integrations-extras/blob/master/pulsar/datadog_checks/pulsar/data/conf.yaml.example
[4]: https://docs.datadoghq.com/agent/guide/agent-commands/#start-stop-and-restart-the-agent
[5]: https://docs.datadoghq.com/agent/guide/agent-commands/#agent-status-and-information
[6]: https://github.com/DataDog/integrations-extras/blob/master/pulsar/metadata.csv
[7]: https://docs.datadoghq.com/help/
