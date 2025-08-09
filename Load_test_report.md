ive run locust on local because i didn't able to deploy that on docker

### Request Summary

| Type | Name     | # Requests | # Fails | Average (ms) | Min (ms) | Max (ms) | Average size (bytes) | RPS  | Failures/s |
|-------|----------|------------|---------|--------------|----------|----------|---------------------|------|------------|
| POST  | /predict | 16,943     | 16,943  | 13.71        | 2        | 10,279   | 69.85               | 4.85 | 4.85       |
| **Aggregated** |          | 16,943     | 16,943  | 13.71        | 2        | 10,279   | 69.85               | 4.85 | 4.85       |

### Response Time Statistics

| Method | Name     | 50%ile (ms) | 60%ile (ms) | 70%ile (ms) | 80%ile (ms) | 90%ile (ms) | 95%ile (ms) | 99%ile (ms) | 100%ile (ms) |
|--------|----------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|--------------|
| POST   | /predict | 7           | 7           | 8           | 9           | 9           | 10          | 13          | 10,000       |
| **Aggregated** |          | 7           | 7           | 8           | 9           | 9           | 10          | 13          | 10,000       |

### Failures Statistics

| # Failures | Method | Name     | Message                                                                                         |
|------------|--------|----------|------------------------------------------------------------------------------------------------|
| 10         | POST   | /predict | ConnectionRefusedError(10061, '[WinError 10061] No connection could be made because the target machine actively refused it.') |
| 4480       | POST   | /predict | HTTPError('422 Client Error: Unprocessable Entity for url: /predict')                          |
| 12453      | POST   | /predict | HTTPError('404 Client Error: Not Found for url: /predict')                                    |

