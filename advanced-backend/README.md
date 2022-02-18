# Tagup Back-End Advanced Coding Exercise

Thanks for your interest in joining our team! In this exercise, you will create a minimalistic web application meant to receive sensor data and report statistics. It is intended to evaluate your technical abilities in advance of an extended interview, and shouldn’t take more than a few hours to complete.

## Technical Requirements

Please implement a basic horizontally-scalable service that collects sensor data and reports statistics. Your application should have four routes:
- `POST /data` should accept JSON documents in the request body, with the form
    `[{"sensor": <str: sensor_id>, "timestamp": <str: iso 8601 timestamp>, "value": <float>}, ...]`
  - The sensor id is a string describing the sensor that generated the data. A single request can include data from multiple sensors.
  - The timestamp is an ISO 8601 string indicating when the data was collected. Timestamps may be represented in local time where the data is captured.
  - Value is the sensor value, represented in floating point.
- `GET /statistics/<sensor id>` should return a JSON document in the response body of the form 
  `{"last_measurement": <str: iso 8601 timestamp>, "count": <int>,
  "avg": <float>}`. 
    - the `last_measurement` value should be the time of the last measurement posted for that sensor id to `/data` (the time included in the request body, *not* the time the request was made)
    - the `count` value should be the total number of measurements received for that sensor id.
    - the `avg` value should be the arithmetic average of all values received for the sensor id.
- `DELETE /statistics/<sensor id>` should clear any statistics for the sensor with the given ID, and the response should not include a body.
- `GET /healthz` should return a 204 response with no body if the server is ready to receive requests, and an error response (e.g. 400) otherwise.

Sample data that could be sent to `POST /data` or received from `GET /statistics/sensor1` is provided in the `samples` directory.

The server should be implemented in Python, in whatever web framework you are most comfortable in (e.g. Flask or FastAPI). It should be containerized using Docker, and should be deployable using Kubernetes.  For the purposes of this exercise, data does not need to persist across server restarts, but server responses should be correct even if there are multiple instances behind a load balancer (so an example architecture might include a central database or cache to act as a system of record).

## Deliverable

Please share your submission as a link to a github repository containing your source code. If you do not have a github account, please create one. The github repository can be public or private; if private, please invite the following github users to collaborate:
- [wrvb](https://github.com/wrvb)
- [jtgarrity](https://github.com/jtgarrity)

Your code should be containerized using docker. Please include a `Dockerfile` that installs your dependencies and executes your server, listening for requests on port 8080. That is, we should be able to use the following commands to run your web application and access it at `localhost:8080`:
```
docker build -t exercise:latest .
docker run --rm -it -p 8080:8080 exercise:latest
```

In addition, you should include a kubernetes manifest in YAML that creates a replica set with two instances of your service. We will build your docker image, push it to a private ECR repository, and deploy it using `kubectl apply -f <manifest.yaml>`; we will access your service using port forwarding. You do not need to configure an ingreess for TLS or external DNS accessibility.

If your submission includes any functionality not captured in the docker image (such as tests, static analysis, or sphinx-like documentation that must be built separately) please describe the functionality in a README.md file at the root of your repository.

## Tips

Show us how you create clean and maintainable code that produces the target result. In particular, we value clearly structured and well-documented code, designed for testability, maintainability, and performance. Adhere to PEP8 if possible, and use consistent naming schemes. Build something that we'd be happy to contribute to.

While this is only an exercise, try to design and implement your solution as you would do for real production code. Although they are beyond the scope of the exercise, consider how you might incorporate logging, monitoring, access control, persistence, and scalability. 

Feel free to add more features: we're curious about what you can think of. If, in a real production situation, you would advocate for any changes to this specification, feel free to note your deviations and your motivations. We'd expect the same if you worked with us! 
