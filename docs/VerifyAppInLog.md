---
title: Verify app in log
date: 22.1.2023
description: Verification of the functionality of the application in the log
tags: Support
---

# Check run job every x minutes by setting in CRON table
Command
```bash
cd /home/{USER}/App/log/bybit_place_trailing_stops_job
grep "Start job" bybit_place_trailing_stops_job.log
```

Example result
```log
2023-01-22 12:35:01,592] p7877 {bybit_place_trailing_stops_job.py:21} INFO - Start job
2023-01-22 12:40:01,754] p8268 {bybit_place_trailing_stops_job.py:21} INFO - Start job
2023-01-22 12:45:01,862] p8371 {bybit_place_trailing_stops_job.py:21} INFO - Start job
2023-01-22 12:50:02,095] p8865 {bybit_place_trailing_stops_job.py:21} INFO - Start job
2023-01-22 12:55:01,424] p9571 {bybit_place_trailing_stops_job.py:21} INFO - Start job
2023-01-22 13:00:01,408] p9642 {bybit_place_trailing_stops_job.py:21} INFO - Start job
2023-01-22 13:05:01,529] p10263 {bybit_place_trailing_stops_job.py:21} INFO - Start job
2023-01-22 13:10:01,624] p10884 {bybit_place_trailing_stops_job.py:21} INFO - Start job
2023-01-22 13:15:01,344] p11082 {bybit_place_trailing_stops_job.py:21} INFO - Start job
2023-01-22 13:20:01,683] p11412 {bybit_place_trailing_stops_job.py:21} INFO - Start job
2023-01-22 13:25:01,815] p11700 {bybit_place_trailing_stops_job.py:21} INFO - Start job
2023-01-22 13:30:02,102] p12734 {bybit_place_trailing_stops_job.py:21} INFO - Start job
```

# Check loading open positions
Command
```bash
cd /home/{USER}/App/log/bybit_place_trailing_stops_job
grep "Count active positions" bybit_place_trailing_stops_job.log 
```

Example result
```log
2023-01-22 13:05:02,191] p10263 {bybit_place_trailing_stops_job.py:39} INFO - Count active positions: 0
2023-01-22 13:10:02,302] p10884 {bybit_place_trailing_stops_job.py:39} INFO - Count active positions: 3
2023-01-22 13:15:02,023] p11082 {bybit_place_trailing_stops_job.py:39} INFO - Count active positions: 2
2023-01-22 13:20:02,474] p11412 {bybit_place_trailing_stops_job.py:39} INFO - Count active positions: 2
2023-01-22 13:25:02,490] p11700 {bybit_place_trailing_stops_job.py:39} INFO - Count active positions: 2
2023-01-22 13:30:02,643] p12734 {bybit_place_trailing_stops_job.py:39} INFO - Count active positions: 2
2023-01-22 13:35:02,631] p13198 {bybit_place_trailing_stops_job.py:39} INFO - Count active positions: 2
```

# Check list of errors in log
Command
```bash
cd /home/{USER}/App/log/bybit_place_trailing_stops_job
grep "ERROR" bybit_place_trailing_stops_job.log 
```

```log
2023-01-22 11:15:02,466] p3638 {__main__.py:20} ERROR - Error in app: 
2023-01-22 11:20:01,840] p4612 {__main__.py:20} ERROR - Error in app: 
2023-01-22 11:25:02,167] p4702 {__main__.py:20} ERROR - Error in app: 
2023-01-22 11:30:01,493] p4769 {__main__.py:20} ERROR - Error in app: 
2023-01-22 11:35:01,822] p4831 {__main__.py:20} ERROR - Error in app: 
2023-01-22 11:40:02,149] p4965 {__main__.py:20} ERROR - Error in app: 
2023-01-22 11:45:01,474] p5020 {__main__.py:20} ERROR - Error in app: 
2023-01-22 11:50:01,801] p5073 {__main__.py:20} ERROR - Error in app: 
2023-01-22 11:55:02,131] p5123 {__main__.py:20} ERROR - Error in app: 
2023-01-22 12:00:01,435] p5379 {__main__.py:20} ERROR - Error in app: 
```

# Detail info for specific error
Command
```bash
cd /home/{USER}/App/log/bybit_place_trailing_stops_job
grep "2023-01-22 12:00:01,435] p5379 {__main__.py:20} ERROR - Error in app" -A 50 -B 10 bybit_place_trailing_stops_job.log 
```

```log
requests.exceptions.ConnectionError: HTTPSConnectionPool(host='api-testnet.bybit.com', port=443): Max retries exceeded with url: /private/linear/position/list?api_key=2WdFpdmjIvXQ29y6PX&recv_window=5000&timestamp=1674384902129&sign=4bb2c7c23825878af1c631caf2633700c4709681ebdd38114c66ac8c0b0dce59 (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x7fb639c47bb0>: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution'))
2023-01-22 12:00:01,417] p5379 {__main__.py:12} INFO - 
---------------------------------------------------------------------
bybit-place-traling-stops_job 0.0.1rc1
---------------------------------------------------------------------

2023-01-22 12:00:01,418] p5379 {_http_manager.py:49} DEBUG - Initializing HTTP session.
2023-01-22 12:00:01,432] p5379 {bybit_place_trailing_stops_job.py:21} INFO - Start job
2023-01-22 12:00:01,433] p5379 {bybit_place_trailing_stops_job.py:23} INFO - Loading data
2023-01-22 12:00:01,434] p5379 {connectionpool.py:1003} DEBUG - Starting new HTTPS connection (1): api-testnet.bybit.com:443
2023-01-22 12:00:01,435] p5379 {__main__.py:20} ERROR - Error in app: 
Traceback (most recent call last):
  File "/home/jirka/App/job/bybit-place-trailing-stops-job-0.0.1rc1/venv/lib/python3.8/site-packages/urllib3/connection.py", line 174, in _new_conn
    conn = connection.create_connection(
  File "/home/jirka/App/job/bybit-place-trailing-stops-job-0.0.1rc1/venv/lib/python3.8/site-packages/urllib3/util/connection.py", line 72, in create_connection
    for res in socket.getaddrinfo(host, port, family, socket.SOCK_STREAM):
  File "/usr/lib/python3.8/socket.py", line 918, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno -3] Temporary failure in name resolution

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/jirka/App/job/bybit-place-trailing-stops-job-0.0.1rc1/venv/lib/python3.8/site-packages/urllib3/connectionpool.py", line 703, in urlopen
    httplib_response = self._make_request(
  File "/home/jirka/App/job/bybit-place-trailing-stops-job-0.0.1rc1/venv/lib/python3.8/site-packages/urllib3/connectionpool.py", line 386, in _make_request
    self._validate_conn(conn)
  File "/home/jirka/App/job/bybit-place-trailing-stops-job-0.0.1rc1/venv/lib/python3.8/site-packages/urllib3/connectionpool.py", line 1042, in _validate_conn
    conn.connect()
  File "/home/jirka/App/job/bybit-place-trailing-stops-job-0.0.1rc1/venv/lib/python3.8/site-packages/urllib3/connection.py", line 358, in connect
    self.sock = conn = self._new_conn()
  File "/home/jirka/App/job/bybit-place-trailing-stops-job-0.0.1rc1/venv/lib/python3.8/site-packages/urllib3/connection.py", line 186, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPSConnection object at 0x7f60b15c4bb0>: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/jirka/App/job/bybit-place-trailing-stops-job-0.0.1rc1/venv/lib/python3.8/site-packages/requests/adapters.py", line 489, in send
    resp = conn.urlopen(
  File "/home/jirka/App/job/bybit-place-trailing-stops-job-0.0.1rc1/venv/lib/python3.8/site-packages/urllib3/connectionpool.py", line 787, in urlopen
    retries = retries.increment(
  File "/home/jirka/App/job/bybit-place-trailing-stops-job-0.0.1rc1/venv/lib/python3.8/site-packages/urllib3/util/retry.py", line 592, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='api-testnet.bybit.com', port=443): Max retries exceeded with url: /private/linear/position/list?api_key=2WdFpdmjIvXQ29y6PX&recv_window=5000&timestamp=1674385201433&sign=41b2133b36735cc1746b649389704b4f88430ef4a87b82042e23f38b31bdff38 (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x7f60b15c4bb0>: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution'))
```