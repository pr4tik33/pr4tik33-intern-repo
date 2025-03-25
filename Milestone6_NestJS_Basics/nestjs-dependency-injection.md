## How does dependency injection improve maintainability?
It promotes loose coupling, making it easier to modify, test, and extend components without changing dependent code.

## What is the purpose of the @Injectable() decorator?
`@Injectable()` decorator marks a class as a provider, allowing NestJS to manage its lifecycle and inject it into other components automatically.

Note for self: we can use different kind of scope by passing as argument inside the Injectable decorator.
eg:
`@Injectable({ scope: Scope.REQUEST })`
`@Injectable({ scope: Scope.TRANSIENT })`

## What are the different types of provider scopes, and when would you use each?
Different types are Singleton scope which is the default scope and only one instances is created and shared across all the application, request scope which last till the process is completed and transient scope which is unique on every injection.

Below are the times they are useful:

- Singleton (Default): Shared instance across the app (best for shared services).
- Request: New instance per request (useful for request-specific data).
- Transient: New instance every time it's injected (useful for lightweight, disposable services).

## How does NestJS automatically resolve dependencies?
It uses constructor injection and its built-in dependency injection container to instantiate and provide the required dependencies when a class is requested.