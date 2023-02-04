# Setup


### Create Docker Image and Container

```bash
make build-run
```

### Clean Docker Image and Container
```bash
make remove
```

### Sample Request
```bash
curl -X POST -H "Content-Type: application/json" -d '{"text":"I like you"}' localhost:80/sentpattern

# Output
{
  "pattern": "ThirdSentencePattern",
  "abbreviation": "SVO"
}
```

### Attention: Not HotReloading