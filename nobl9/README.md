# Nobl9

## Overview
Nobl9 is a SLO platform that provides real-time, historical SLO reports. Nobl9 integrates with Datadog to collect SLI metrics and measure them against SLO targets. Since Nobl9 calculates error budgets of acceptable thresholds, it can trigger workflows and alerts when the error burn rate is too high or has been exceeded.

With the Datadog Nobl9 integration, you can:

- Pass business context through monitoring data
- Define and measure reliability goals
- Align activities against priorities set by the error budget

### SLO grid view
![SLO Grid View][4]

### SLO detail
![Detail][5]

### SLO report
![SLO Report][6]

### Service health dashboard
![Service Health Dashboard][7]

## Setup

All configuration happens on the Nobl9 SLO Platform.

1. Add the Datadog API endpoint to connect to your data source, either `https://api.datadoghq.com/` or `https://api.datadoghq.eu/` (required).
2. Enter a **Project** name. This field is intended for situations where multiple users are spread across multiple teams or projects. When the field is left blank, a default value appears.
3. The **Display Name** appears automatically when a name is entered in the **Name** field.
4. Enter a name for your data source (required). Metadata names are unique within each project and are validated against some RFC and DNS names. The data source name must contain only lowercase alphanumeric characters and dashes. For example: `my-datadog-data-source`.
5. Enter a description (optional). Add the team or owner details and explain why you created this specific data source. Descriptions provide immediate context for any team member.

For more information about creating SLOs on the Nobl9 platform, see Nobl9's [User Guide][1].

## Troubleshooting

Need help? Contact [Nobl9 Support][2] or [Datadog Support][3].

[1]: https://nobl9.github.io/techdocs_User_Guide/#service-level-objectives-38
[2]: https://nobl9.com/about/#contact
[3]: https://docs.datadoghq.com/help/
[4]: https://raw.githubusercontent.com/DataDog/integrations-extras/master/nobl9/images/grid_view.jpg
[5]: https://raw.githubusercontent.com/DataDog/integrations-extras/master/nobl9/images/slo_detail.png
[6]: https://raw.githubusercontent.com/DataDog/integrations-extras/master/nobl9/images/slo_report.png
[7]: https://raw.githubusercontent.com/DataDog/integrations-extras/master/nobl9/images/service_health.png
