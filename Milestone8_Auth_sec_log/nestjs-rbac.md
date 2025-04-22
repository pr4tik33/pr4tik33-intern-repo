## How does Auth0 store and manage user roles?
Auth0 stores user roles in its Authorization Core or Authorization Extension. Roles are assigned to users and linked to permissions, which are then included in the user's access token. This allows applications to enforce role-based access control (RBAC) during authorization.

## What is the purpose of a guard in NestJS?
A guard in NestJS is used to determine whether a request should be processed by a route handler. Guards implement custom authorization logic, such as checking user roles or permissions, and can block unauthorized requests.

## How would you restrict access to an API endpoint based on user roles?
To restrict access based on user roles in NestJS these are few simple steps:

- Use a Guard to check the user's roles from the request or token.
- Implement a custom guard using CanActivate to validate roles.
- Apply the guard to the endpoint using the @UseGuards() decorator.

```@UseGuards(RolesGuard)
@Roles('admin')
@Get('protected')
getProtectedData() {
  return 'This is restricted to admins.';
}```

## What are the security risks of improper authorization, and how can they be mitigated?
The security risks of improper authorization are as follows:
- Unauthorized access to sensitive data.
- Data breaches due to insufficient role validation.

This could be mitigated in following ways:
- By implementing strict RBAC policies
- Validate roles and permissions at every endpoints
- Use of secure token based auth with role claims.
