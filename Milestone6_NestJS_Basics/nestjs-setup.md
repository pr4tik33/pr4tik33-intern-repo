## What files are included in a default NestJS project?
Files that included in a default NestJS project are listed below:
1. Dist folder
2. node_modules folder
3. src folder
4. test folder

and the core files are listed below:


**app.controller.spec.ts** -	The unit tests for the controller.
**app.controller.ts** - A basic controller with a single route.
**app.module.ts** - The root module of the application.
**app.service.ts** -	A basic service with a single method.
**main.ts**	- The entry file of the application which uses the core function NestFactory to create a Nest application instance.


## How does main.ts bootstrap a NestJS application?
1. Creating the NestJS Application
The main.ts file calls `NestFactory.create(AppModule)`, which creates an instance of the NestJS application using the root module (AppModule). This sets up the dependency injection container, loads modules, and prepares the app to handle requests.

2. Starting the HTTP Server
After creating the app instance, `app.listen(port)` starts the HTTP server, making the application accessible on the specified port.

Workflow of main.ts
-Import NestFactory and AppModule.
-Create the NestJS application instance.
-Apply any necessary configurations (e.g., validation, CORS).
-Start listening for incoming requests.

## What is the role of AppModule in the project?

## How does NestJS structure help with scalability?




![npm run start screenshot](image.png)
![hello world](image-1.png)