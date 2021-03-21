# /How to dev

1. Create the .env files based on .env.template (More info in [this section](env.md))
2. Run the command

```bash
docker-compose up -d --build
```

3. If you need to run only some modules you can do it like this:

```bash
docker-compose up -d --build module1 module2...
```

### Useful links

- [MongoDB Schemas](mongo/schemas/)
- [Redis PubSub Messages](redis/)
- [Env Files](env.md)
- [Components/Deploy Diagram](diagrams/)
