# pipeline_executor_docker_call

# Step to produce
- Build all image:
```
# TODO
```
- Run docker caller service:
```
docker run -p <HOST_POST>:8080 -v /var/run/docker.sock:/var/run/docker.sock <CALLER_IMAGE>
```
