### About

It's simple task for ctf pwn category wrapped in docker container for easy deploy.

### Usage

Copy this repo and run docker container

```sh
git clone https://github.com/PYfffE/kiddypwn
cd kiddypwn

docker build -t pwn-task .
docker run -p 1337:1337 --rm -d pwn-task
```

Connect to task using netcat
```sh
nc 127.0.0.1 1337
```
