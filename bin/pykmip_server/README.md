## Setup the project

Create a virtual environment:

```sh
python3.11 -m venv .venv
```

Activate it:

```sh
. ./.venv/bin/activate`
```

Install dependencies:

```sh
pip3 install -r requirements.txt
```

Generate the keys and certificates:

```sh
cd bin/pykmip_server/certs
./generate.sh
```
 

## Server Configuration

In the `server.conf` file, make sure that:

- `auth_suite` is set to `TLS1.2`; TLS 1.0 is now unsupported by many tools, including `curl`\
- `enable_tls_client_auth` is set to `False` to avoir verifying the client certificate X509 extensions (or the
  `generate.sh` script must be modified to add them)

## Server Start

From the project root, run:

```sh
 PYTHONPATH=. python3 ./bin/run_server.py
 ```

Not: `run_server.py` has been modified to run properly on MacOS.

## Client

To test the connection, use `curl`. On MacOS, install `openssl` first, then install `curl`, so that curl uses the right
version of `openssl`. Then make sure, that the `homebrew curl` is used:

```sh
echo 'export PATH="$HOME/homebrew/opt/curl/bin:$PATH"' >> ~/.zshrc
```

Then, from the project root, run:

```sh
curl -v -X POST --insecure \
--key ./bin/pykmip_server/certs/client.key \
--cert ./bin/pykmip_server/certs/client.crt \
--cacert ./bin/pykmip_server/certs/ca.crt  \
https://localhost:5696/kmip
```

At the end of the handshake, `curl` should print `Request completely sent off` 

