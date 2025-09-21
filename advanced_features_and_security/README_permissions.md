# Permissions and Groups Setup

## Custom Permissions
Defined in `relationship_app/models.py` under the `Book` model:
- `can_view`
- `can_create`
- `can_edit`
- `can_delete`

## Groups
Configured in `setup_groups.py`:
- **Viewers** → `can_view`
- **Editors** → `can_view`, `can_create`, `can_edit`
- **Admins** → all permissions

## Enforcement
Permissions are checked in views using `@permission_required`.

## Testing
1. Create users in Django admin.
2. Assign them to groups.
3. Log in and test access to book list, create, edit, and delete pages.
