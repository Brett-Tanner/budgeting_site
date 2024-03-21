# Database design

## Budgets

Have a way of easily copying budgets from month to month along with their categories.

### Fields

| Field | Type | Null | Key | Default | Extras |
| ----- | ---- | ---- | --- | ------- | ----- |
| user_id | int | NO | FK | NULL | NULL |
| shared_with | int/jsonb/array | YES | FK | NULL/[] | NULL |
| income | int | NO | NO | 0 | NULL |
| start_date | date | NO | NO | NULL | NULL |
| end_date | date | NO | NO | NULL | NULL |

### Associations

- Belong to a user
- Has many shared users through SharedBudgets
- Have many transactions
- Have many categories

## Categories

### Fields

| Field | Type | Null | Key | Default | Extras |
| ----- | ---- | ---- | --- | ------- | ----- |
| budget_id | int | NO | FK | NULL | INDEX |
| name | varchar | NO | NO | NULL | NULL |

### Associations

- Belongs to a budget
- Belongs to a user through budget
- Has many transactions

## SharedBudgets

### Fields

| Field | Type | Null | Key | Default | Extras |
| ----- | ---- | ---- | --- | ------- | ----- |
| budget_id | int | NO | FK | NULL | NULL |
| user_id | int | NO | FK | NULL | NULL |

### Associations

- Belong to a budget
- Belong to a user

## Rules

### Fields

| Field | Type | Null | Key | Default | Extras |
| ----- | ---- | ---- | --- | ------- | ----- |
| pattern | varchar | NO | NO | NULL | NULL |
| category_id | int | NO | FK | NULL | NULL |

### Associations

- Belong to a category

## Transactions

### Fields

| Field | Type | Null | Key | Default | Extras |
| ----- | ---- | ---- | --- | ------- | ----- |
| user_id | int | NO | FK | NULL | NULL |
| category_id | int | NO | FK | NULL | INDEX |
| amount | int | NO | NO | 0 | NULL |
| description | varchar | YES | NO | '' | NULL |
| created_at | timestamp | NO | NO | NULL | NULL |

### Associations

- Belong to a user
- Belong to a category
- Belong to a budget through category
