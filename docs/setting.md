## Setting

Edit setting values on config.yaml

*If an environment variable exists, that value will override the yaml variable

#### Note: Please notice the working dir `src/service_platform/runtime/settings`

For development:

```bash
export ENVIRONMENT=local
cp config.example.yaml config.local.yaml
```

## JWT

Generate JWT Secret key and Public key

```shell
ssh-keygen -t rsa -b 4096 -m PEM -E SHA512 -f jwtRS512.key
openssl rsa -in jwtRS512.key -pubout -outform PEM -out jwtRS512.key.pub
```

Encode the key

```shell
cat jwtRS512.key | base64
cat jwtRS512.key.pub | base64
```

## DB

Postgres and Redis can be launched on docker
`docker-compose up -d`
