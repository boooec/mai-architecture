## Тестирование производительности без/с кешированием при помощи утилиты wrk

### Без кеширования

```
$ wrk -t1 -c10 -d10s -s auth.lua http://localhost:8000/users/admin
Running 10s test @ http://localhost:8000/users/admin
  1 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    34.28ms   34.28ms 348.67ms   94.74%
    Req/Sec   348.90     77.26   414.00     85.71%
  3418 requests in 10.01s, 590.81KB read
Requests/sec:    341.58
Transfer/sec:     59.04KB

$ wrk -t5 -c10 -d10s -s auth.lua http://localhost:8000/users/admin
Running 10s test @ http://localhost:8000/users/admin
  5 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    31.25ms   22.73ms 278.45ms   93.29%
    Req/Sec    70.62     13.74    90.00     88.44%
  3493 requests in 10.01s, 603.77KB read
Requests/sec:    348.96
Transfer/sec:     60.32KB

$ wrk -t10 -c10 -d10s -s auth.lua http://localhost:8000/users/admin
Running 10s test @ http://localhost:8000/users/admin
  10 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    32.37ms   26.78ms 301.28ms   93.42%
    Req/Sec    35.07      8.71    50.00     86.77%
  3335 requests in 10.01s, 576.46KB read
Requests/sec:    333.06
Transfer/sec:     57.57KB
```

### С кешированием:

```
$ wrk -t1 -c10 -d10s -s auth.lua http://localhost:8000/users/admin
Running 10s test @ http://localhost:8000/users/admin
  1 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    12.54ms    2.86ms  48.76ms   91.51%
    Req/Sec   807.60     64.12     0.91k    81.00%
  8041 requests in 10.01s, 1.36MB read
Requests/sec:    803.32
Transfer/sec:    138.86KB

$ wrk -t5 -c10 -d10s -s auth.lua http://localhost:8000/users/admin
Running 10s test @ http://localhost:8000/users/admin
  5 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    12.71ms    2.39ms  42.40ms   92.58%
    Req/Sec   158.54     10.10   181.00     80.80%
  7906 requests in 10.01s, 1.33MB read
Requests/sec:    789.96
Transfer/sec:    136.56KB

$ wrk -t10 -c10 -d10s -s auth.lua http://localhost:8000/users/admin
Running 10s test @ http://localhost:8000/users/admin
  10 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    12.65ms    2.37ms  42.61ms   88.46%
    Req/Sec    79.38      5.82    90.00     72.30%
  7940 requests in 10.01s, 1.34MB read
Requests/sec:    792.96
Transfer/sec:    137.06KB
```
