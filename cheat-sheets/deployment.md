# Deployment checklist

## Before release

- Install pinned dependencies with `npm ci` when a lockfile exists.
- Run the project-defined lint, typecheck, test and build commands.
- Verify that secrets are ignored and production variables are set.
- Review database migrations and back up important data.
- Apply reviewed Prisma migrations with `npx prisma migrate deploy` when the project uses Prisma.
- Verify authentication, permissions, health endpoint and representative workflows.

```bash
git status --short
npm ci
npm run build
```
Deploy from a reviewed commit. Do not use `prisma migrate reset` against production. Check hosting terms and quotas.

## Official reference

[Deployment checklist documentation](https://vercel.com/docs)
