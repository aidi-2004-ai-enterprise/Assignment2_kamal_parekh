# Assignment2_kamal_parekh
1. What edge cases might break your model in production that aren't in your training data?
   
Sometimes real-world data throws curveballs—like missing or malformed features, unexpected categorical values (e.g., a new island or sex value), or extreme numbers way outside training ranges. For example, if the model never saw a penguin with negative body mass or an island called “Atlantis,” it might fail or give garbage predictions. Handling those gracefully with input validation and fallback logic is key.

2. What happens if your model file becomes corrupted?
   
If the model file is corrupted or missing, the app might crash or refuse to start. Ideally, we’d have checks during startup to verify model integrity, maybe fallback to a backup model, or return clear errors so we know something’s wrong before hitting users. Monitoring logs and alerts help catch this quickly.

3. What's a realistic load for a penguin classification service?

Probably not super high unless it’s for a scientific study or large-scale automated monitoring. Maybe dozens to hundreds of requests per minute? But if it’s embedded in a big app or exposed publicly, loads could spike unpredictably. It’s good to test from low loads up to thousands per minute to be safe.

4. How would you optimize if response times are too slow?

First, profile to find bottlenecks: is model loading slow? Is preprocessing heavy? Then, you might:
Cache the loaded model in memory 
Use batch prediction if applicable
Optimize data preprocessing (e.g., avoid redundant one-hot encoding)
Use a lighter model or quantize it
Scale horizontally with more instances
Use async endpoints or faster servers.

5. What metrics matter most for ML inference APIs?

Latency: How fast is each prediction?
Throughput: How many requests per second?
Error rate: Percentage of failed or invalid responses
Resource usage: CPU, memory per request
Prediction accuracy (tracked offline) to catch model drift.

6. Why is Docker layer caching important for build speed? (Did you leverage it?)

Docker caches each step (layer) during build, so if your code or dependencies don’t change, the build is much faster next time. For example, installing dependencies is slow, but if requirements.txt hasn’t changed, Docker won’t reinstall every build. Leveraging this saves time and resources during iterative development.

7. What security risks exist with running containers as root?

Running as root inside a container means if someone escapes the container, they could have full system access, risking your host OS. It also increases risks if attackers exploit vulnerabilities inside the container. It’s safer to run as a non-root user with least privileges, reducing attack surface.

8. How does cloud auto-scaling affect your load test results?

Auto-scaling spins up new instances when load increases, so initial response times might be slower during scale-up. Load tests should simulate gradual increase to see how well the system scales and recovers, and also test cold start latency. Without proper auto-scaling config, requests could fail or queue.

9. What would happen with 10x more traffic?

If the infrastructure can’t scale accordingly, you’d see increased latency, possible timeouts, and errors. You might max out CPU/memory or hit connection limits. Planning for scale means adding more replicas, load balancing, and possibly optimizing the model or using caching layers.

10. How would you monitor performance in production?

Use a combination of logging, metrics, and tracing tools:
Track latency, throughput, error rates with Prometheus/Grafana or cloud monitoring.
Log predictions and errors for audit and debugging.
Use alerts for anomalies like spikes in errors or latency.
Monitor container health and resource usage.

11. How would you implement blue-green deployment?
Keep two identical production environments (blue and green). Deploy new version to the idle one (green), test it live, then switch traffic over from blue to green with minimal downtime. If problems occur, rollback is easy by switching back. This reduces risk and downtime during updates.

12. What would you do if deployment fails in production?

Immediately rollback to the last stable version. Check logs to identify the root cause. If it’s a quick fix, patch and redeploy carefully. Communicate with stakeholders, and run extra tests on staging to avoid repeating issues. Automate rollback where possible for faster recovery.

13. What happens if your container uses too much memory?

The container runtime (like Docker or Kubernetes) may kill the container to protect the host, causing downtime. High memory usage can also degrade performance. To avoid this, set resource limits, optimize your app, and monitor memory usage continuously. Consider scaling or optimizing the model if memory is a bottleneck.

