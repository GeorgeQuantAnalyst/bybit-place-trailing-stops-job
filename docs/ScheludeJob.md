---
title: Schelude job
date: 22.1.2023
description: Short guidance how schelude job in CRON table
tags: Support
---

# How schelude job run every 5 minutes

```bash
crontab -e # Update crontab, add code from below section on end file or update existing record
crontab -l # Print crontab for verify update
service cron reload
```

**Record for schelude job**
```crontab
*/5 * * * * cd /home/{USER}/App/job/bybit-place-trailing-stops-job-{VERSION}/;./run.sh 
```

Note: Edit home directory and app version.


# How stop repeating job
Remove record for our app in CRON table.

```bash
crontab -e # Update crontab, remove record for our app
crontab -l # Print crontab for verify update
service cron reload
```

**Example record for our app in CRON table**
```crontab
*/5 * * * * cd /home/{USER}/App/job/bybit-place-trailing-stops-job-{VERSION}/;./run.sh
```