**Title**
Add automatic runbook saving for final responses

**Description**
This pull request adds automatic runbook saving to the Django Teacher Agent workflow.

**What was done**
- Added a rule that saves every final user-facing response as a Markdown runbook before sending it in chat.
- Organized the saved files under the appropriate runbook folder based on the request type.
- Kept the saved content identical to the final response shown to the user.

**How it works**
- When the agent prepares a final response, it first writes that response to a Markdown file in the runbooks directory.
- The file name uses the current date and a short descriptive summary.
- The response is only sent after the runbook file has been created successfully.

**Why this is useful**
- Creates a record of agent responses for review and reference.
- Improves traceability of decisions and explanations.
- Keeps project knowledge documented in a simple, readable format.

**Notes**
- This change is additive and does not introduce breaking behavior.
- It improves documentation and workflow visibility without changing the core teaching purpose of the agent.