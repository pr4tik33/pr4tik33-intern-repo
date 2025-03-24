## What are the key differences between NestJS and Express.js?

1. NestJS follows a modular, opinionated structure inspired by Angular, making it suitable for large-scale applications. In contrast, Express.js is minimalist and unopinionated, giving developers full control over how they structure their projects.
2. NestJS is built with TypeScript by default, whereas Express.js primarily uses JavaScript, with optional TypeScript support.
3. NestJS has a built-in DI system that promotes modularity and testability, while Express.js lacks this feature, requiring manual dependency management.
4. NestJS also relies on decorators (e.g., `@Controller()`, `@Injectable()`, `@Get()`) to simplify routing and dependency management. Express.js, on the other hand, uses middleware and function-based routing, requiring more manual setup.

## Why does NestJS use decorators extensively?
NestJS uses decorators extensively because they provide a structured and declarative way to define metadata for classes, methods, and properties. This makes the code more readable, maintainable, and scalable.

## How does NestJS handle dependency injection?
Dependency Injection (DI) in NestJS operates through its Inversion of Control (IoC) container, which automatically manages the representation and injection of dependencies. When a class is marked with the @Injectable() decorator, it becomes a provider that can be injected into other classes. 


## What benefits does modular architecture provide in a large-scale app?
Modular software architecture improves scalability, maintainability, and reusability. Developers can modify or replace specific modules without affecting the entire system. Modularization programming speeds up development by enabling parallel work on different components which is what a large scale app would require since multiple people would be working on it.


Resources: 
https://www.geeksforgeeks.org/what-is-nestjs/
https://www.geeksforgeeks.org/dependency-injection-in-nestjs/
