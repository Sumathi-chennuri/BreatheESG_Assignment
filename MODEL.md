# Data Model

## Company Model

Stores company information.

Fields:

- id
- name

---

## ActivityRecord Model

Stores ESG activity data.

Fields:

- source
- category
- quantity
- unit
- scope
- suspicious
- status
- company

---

## Relationship

One Company can have many Activity Records.

Relationship:

```txt
Company → ActivityRecord
One-to-Many
```
