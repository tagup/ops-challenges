# Tagup Back-End Coding Exercise

Thanks for your interest in joining our team! In this exercise, you will create a minimalistic web application meant to receive sensor data and report statistics. It is intended to evaluate your technical + design abilities in advance of final stage interviews, and shouldn’t take more than 2 hours to complete.

At Tagup, developers actively influence design + work planning + commercial priorities, so if you believe something is underspecified, make whatever design decision you think is best and document your thought process + assumptions + uncertainties. Likewise, if you disagree with some part of the specification, you're encouraged to propose or implement alternative solutions and document your assumptions + reasoning.

## Technical Requirements

Please implement a basic web application that collects sensor data and reports statistics. Your server should have four routes:
- `POST /data` should accept JSON documents in the request body, with the form
    `[{"sensor": <str: sensor_id>, "timestamp": <str: iso 8601 timestamp>, "value": <float>}, ...]`
  - The sensor id is a string describing the sensor that generated the data. A single request can include data from multiple sensors.
  - The timestamp is an ISO 8601 string indicating when the data was collected. Timestamps may be represented in local timezone where the data is captured.
  - Value is the sensor value, represented as a floating point number.
- `GET /statistics/<sensor id>` should return a JSON document in the response body of the form 
  `{"last_measurement": <str: iso 8601 timestamp>, "count": <int>,
  "avg": <float>}`. 
    - the `last_measurement` value should be the time of the last measurement for the specified sensor posted to `/data` (the time included in the request body, *not* the time the request was made)
    - the `count` value should be the total number of measurements received by the server for the specified sensor
    - the `avg` value should be the arithmetic average of all values received for the sensor by the server.
- `DELETE /statistics/<sensor id>` should clear all received measurements for the sensor with the given ID, and the response should not include a body.
- `GET /healthz` should return a 204 response with no body if the server is ready to receive requests, and an error response (e.g. 400) otherwise.

Sample data that could be sent to `POST /data` or received from `GET /statistics/sensor1` is provided in the `samples` directory.

The server should be implemented in Python. You may use whatever web framework you are comfortable in (e.g. Flask or FastAPI). The server should be containerized using Docker. For the purposes of this exercise, you do not need to persist data to a database; the `GET` route only needs to capture measurements received since the server was started.

## Deliverable

Please share your submission as a link to a github repository containing your source code. If you do not have a github account, please create one. The github repository can be public or private; if private, please invite the following github users to collaborate:
- [wrvb](https://github.com/wrvb)
- [jtgarrity](https://github.com/jtgarrity)

Your code should be containerized using docker. Please include a `Dockerfile` that installs your dependencies and executes your server, listening for requests on port 8080. That is, we should be able to use the following commands to run your web application and access it at `localhost:8080`:
```
docker build -t exercise:latest .
docker run --rm -it -p 8080:8080 exercise:latest
```

If your submission includes any functionality not captured in the docker image (such as tests, static analysis, or sphinx-like documentation that must be built separately) please describe the functionality in a README.md file at the root of your repository.

## Tips

Show us how you create clean and maintainable code that produces the target result. In particular, we value clearly structured and well-documented code, designed for testability, maintainability, and performance. Adhere to PEP8 if possible, and use consistent naming schemes. Build something that we'd be happy to contribute to.

While this is only an exercise, try to design and implement your solution as you would do for real production code. Although they are beyond the scope of the exercise, consider how you might incorporate logging, monitoring, access control, persistence, and scalability. 

Feel free to add more features: we're curious about what you can think of. If, in a real production situation, you would advocate for any changes to this specification, feel free to note your deviations and your motivations. We'd expect the same if you worked with us! 
