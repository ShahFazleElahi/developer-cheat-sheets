# TypeScript

```ts
type User = { id: string; role: 'admin' | 'member' };
function canManage(user: User): boolean {
  return user.role === 'admin';
}
function isUser(value: unknown): value is User {
  if (typeof value !== 'object' || value === null) return false;
  const u = value as Record<string, unknown>;
  return typeof u.id === 'string' && (u.role === 'admin' || u.role === 'member');
}
```

```ts
type Result<T> = { ok: true; data: T } | { ok: false; error: string };
function unwrap<T>(result: Result<T>): T {
  if (!result.ok) throw new Error(result.error);
  return result.data;
}
```
Enable `strict` in tsconfig. Types disappear at runtime, so validate untrusted inputs.

## Official reference

[TypeScript documentation](https://www.typescriptlang.org/docs/)
