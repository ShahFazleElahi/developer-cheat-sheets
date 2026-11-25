# JavaScript

```js
const orders = [{ total: 120, paid: true }, { total: 80, paid: false }];
const revenue = orders.filter(o => o.paid).reduce((sum, o) => sum + o.total, 0);
console.log(revenue); // 120
const names = ['Ada', 'Linus'].map(name => name.toUpperCase());
const user = { profile: { name: 'Ada' } };
console.log(user.profile?.name ?? 'Unknown');
```

```js
async function getJSON(url) {
  const res = await fetch(url, { signal: AbortSignal.timeout(10000) });
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json();
}
```
Use `const` by default, strict equality, and explicit error handling. Validate external data before trusting it.

## Official reference

[JavaScript documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
