## FQA

### How to fix SSL error: unable to get local issuer certificate?

#### ERROR:

```
INFO:     127.0.0.1:59531 - "POST /api/user/google/login HTTP/1.1" 401 Unauthorized
ERROR:service_platform.settings:Error verify_access_token: Cannot connect to host www.googleapis.com:443 ssl:True [SSLCertVerificationError: (1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1000)')]
```

#### FIX:

Install the necessary certificates for Python to verify SSL connections:

```bash
bash /Applications/Python*/Install\ Certificates.command
```
