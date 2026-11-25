# HTTP and curl

| Code | Meaning |
|---|---|
| 200 | OK |
| 201 | Created |
| 400 | Bad request |
| 401 | Authentication required or invalid |
| 403 | Forbidden |
| 404 | Not found |
| 429 | Too many requests |
| 500 | Server error |

```bash
curl -fsS --max-time 15 https://jsonplaceholder.typicode.com/posts/1
curl -I --max-time 15 https://example.com
curl -fsS --max-time 15 -H 'Content-Type: application/json' \
  -d '{"title":"Example","body":"Test","userId":1}' \
  https://jsonplaceholder.typicode.com/posts
```
JSONPlaceholder simulates writes. Never paste real tokens into public issue logs.

## Official reference

[HTTP and curl documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP)
