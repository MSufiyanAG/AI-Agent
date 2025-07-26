## Docker Model Runner

``` bash
curl.exe -X POST http://localhost:12434/engines/v1/chat/completions \`
    -H "Content-Type: application/json" \`
    -d "{
        \`"model\`": \`"ai/gemma3:4B-Q4_0\`",
        \`"messages\`": [
            {
                \`"role\`": \`"system\`",
                \`"content\`": \`"You are a helpful assistant.\`"
            },
            {
                \`"role\`": \`"user\`",
                \`"content\`": \`"Please write 500 words about the fall of Rome.\`"
            }
        ]
    }"
```

## from within container
```bash
curl -X POST http://model-runner.docker.internal/engines/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "ai/gemma3:4B-Q4_0",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "Please write 500 words about the fall of Rome."
            }
        ]
    }'
```