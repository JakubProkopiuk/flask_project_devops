## Performance summary (loader.io – 250 clients / 1 min)

| Stack | Avg. response time | Successful responses | Report |
|-------|-------------------|----------------------|--------|
| **Flask + uWSGI + nginx** | **89 ms** | 250 / 250 | [view](deploy/flask_uwsgi_nginx/BENCHMARK.md) |
| Flask + ASGI (Uvicorn) + nginx | 93 ms | 250 / 250 | [view](deploy/flask_asgi_nginx/BENCHMARK.md) |
| FastAPI + ASGI (Uvicorn) + nginx | 93 ms | 250 / 250 | [view](deploy/fastapi_asgi_nginx/BENCHMARK.md) |

> The average response times differ only slightly across the three stacks.  
> FastAPI + ASGI and Flask + ASGI perform almost identically, while Flask + uWSGI
> is marginally faster under this load profile.  
> All tests completed with a **100 % success rate**—no time-outs or 4xx/5xx errors.

