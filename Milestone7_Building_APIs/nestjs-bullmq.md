## Why is BullMQ used instead of handling tasks directly in API requests?
BullMQ is used to offload long-running or resource-intensive tasks from API requests to a background job queue. That means API response will be fast and the main thread isn't blocked, improving scalability and user experience.

## How does Redis help manage job queues in BullMQ?
Redis acts as the underlying data store for BullMQ, providing queue management, concurrency, ensuring persistency, and enabling real-time notification for job events like completion or failure.

## What happens if a job fails? How can failed jobs be retried?
**Job Failure:**
- If a job fails, BullMQ marks it as "failed" and stores the error details in Redis.
- The failure can be due to application errors, worker crashes, or invalid job data.

**Retrying Failed Jobs:**
- BullMQ supports automatic retries based on the configuration (e.g., attempts and backoff options).
- Failed jobs can also be manually retried using the BullMQ API or a dashboard.

