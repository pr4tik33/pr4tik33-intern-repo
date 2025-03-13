# Understanding Git: Staging vs. Committing

## What is the difference between staging and committing?
Staging is the process of adding changes to the staging area, a temporary holding space where you can review and modify changes before committing them. Committing is the act of saving the changes in the staging area to the repository's history, creating a new snapshot of the project locally.

## Why does Git separate these two steps?
Git separates staging and committing to provide more control over the version history. This separation allows you to:
- Review changes before finalizing them.
- Group related changes into a single commit.
- Exclude certain changes from a commit.

## When would you want to stage changes without committing?
You might want to stage changes without committing when:
- You are working on multiple features or fixes simultaneously and want to commit them separately.
- You need to review or test changes before finalizing them.
- You want to create a clean and organized commit history by grouping related changes together.

## Why is pushing directly to main problematic?
- Pushing directly to main could cause the codebase to break.
- It bypass the oppurtunity for code reviews.
- It could be easy to override the progress done by other collaborators if they push it without pulling first or could cause messy conflicts that are hard to resolve.

## How do branches help with reviewing code?
- By creating branches based on features, bugs fixes and improvements it makes it easier to review changes based on that.
- Typically we make pull request when merging to main branch or parent branch which is then reviewed.
- With separate branches, developers can test their changes in isolation without distrupting production or other collaborators.

## What happens if two people edit the same file on different branches?
- If the changes in both branches do not conflict git can automatically merge the changes without issues.
- If both developers have made changes to the same part of the file, a merge conflict will occur which needs to be manually resolved by developer.