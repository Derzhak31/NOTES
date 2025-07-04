from typing import Annotated, Optional, TYPE_CHECKING

from fastapi import Depends
from fastapi_users import BaseUserManager, FastAPIUsers, IntegerIDMixin
from fastapi_users.authentication import AuthenticationBackend, BearerTransport
from fastapi_users.authentication.strategy.db import DatabaseStrategy

from api.models.access_token import get_access_token_db
from api.models.users import get_user_db

if TYPE_CHECKING:
    from fastapi import Request
    from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
    from fastapi_users.authentication.strategy.db import AccessTokenDatabase
    from api.models import AccessToken, User


SECRET = "SECRET"


class UserManager(IntegerIDMixin, BaseUserManager["User", int]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(
        self, user: "User", request: Optional["Request"] = None
    ):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: "User", token: str, request: Optional["Request"] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: "User", token: str, request: Optional["Request"] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")


async def get_user_manager(
    user_db: Annotated["SQLAlchemyUserDatabase", Depends(get_user_db)],
):
    yield UserManager(user_db)


bearer_transport = BearerTransport(tokenUrl="auth/login")


def get_database_strategy(
    access_token_db: Annotated[
        "AccessTokenDatabase[AccessToken]", Depends(get_access_token_db)
    ],
) -> DatabaseStrategy:
    return DatabaseStrategy(access_token_db, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="access-token-db",
    transport=bearer_transport,
    get_strategy=get_database_strategy,
)

fastapi_users = FastAPIUsers["User", int](get_user_manager, [auth_backend])

# current_active_user = fastapi_users.current_user(active=True)
