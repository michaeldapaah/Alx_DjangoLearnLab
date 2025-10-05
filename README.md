### Authentication & Permissions
- Authentication is handled via TokenAuthentication.
- Each user must request a token from `/api-token-auth/` with their username and password.
- Include the token in the Authorization header: `Authorization: Token <"1288f88c82e41806192399f2a506439a7ba07866">`.
- By default, only authenticated users can access the API (`IsAuthenticated`).
