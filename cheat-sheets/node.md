# Node.js

```js
// save as app.mjs; run node app.mjs
import { readFile } from 'node:fs/promises';
try {
  const data = JSON.parse(await readFile('package.json', 'utf8'));
  console.log(data.name);
} catch (error) {
  console.error(error.message);
  process.exitCode = 1;
}
```
Use supported Node releases, async I/O, locked dependencies and environment variables for secrets.

## Official reference

[Node.js documentation](https://nodejs.org/api/)
