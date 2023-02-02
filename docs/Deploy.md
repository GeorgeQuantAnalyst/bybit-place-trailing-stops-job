---
title: Deploy on test/prod server
date: 22.1.2023
description: Short guidance how deploy app on VPS server
tags: Support
---

# Copy build app to server
```
cd ~/SourceCode/bybit-place-trailing-stops-job/dist
scp bybit-place-trailing-stops-job-0.1.0rc1.tar.gz test1@{server_ip_address}:/home/test1/
```

# Connect to server
```
ssh test1@{server_ip_address}
```

# Copy build to app folder and unzip
```
mv bybit-place-trailing-stops-job-0.1.0rc1.tar.gz app/bybit-place-trailing-stops-job/
cd app/bybit-place-trailing-stops-job/
tar xf bybit-place-trailing-stops-job-0.1.0rc1.tar.gz
```


# Prepare app
```
cd bybit-place-trailing-stops-job-0.1.0rc1
make prepare
cp ~/config_backup/logger.conf .
cp ~/config_backup/config.yaml .

crontab -e
```

**Update crontab file**
```
*/5 * * * * cd /home/test1/app/bybit-place-trailing-stops-job/bybit-place-trailing-stops-job-0.1.0rc1; make run
```


# Restart cron service
```
service cron reload
```

# Verify app
```
grep "Start job" log/bybit_place_trailing_stops_job/bybit_place_trailing_stops_job.log
grep "ERROR" log/bybit_place_trailing_stops_job/bybit_place_trailing_stops_job.log
tail -f log/bybit_place_trailing_stops_job/bybit_place_trailing_stops_job.log
```
