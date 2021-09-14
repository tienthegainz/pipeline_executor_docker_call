# pipeline_executor_docker_call

## Step to reproduce
- Build all image:
```
# TODO
```
- Run docker caller service:
```
# Bind mount the host's docker engine folder
docker run -dp <HOST_POST>:8080 -v /var/run/docker.sock:/var/run/docker.sock <CALLER_IMAGE>
```
