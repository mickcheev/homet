from users.models import User, TelegramUserKey
from functools import wraps


def check_reg():
    def decorator(func):
        @wraps(func)
        def inner(message, *args, **kwargs):
            try:
                usr = User.get(User.telegram_account == message.from_user.id)
            except Exception:
                return message.answer('You did not pass authentication\nBound your account via /bound command')

            return func(message, usr)
        return inner
    return decorator


def bound_account(key: str, telegram_id) -> str:
    try:
        usr: User = TelegramUserKey.get(TelegramUserKey.key == key).user
    except Exception:
        return 'You have entered an invalid key'
    else:
        usr.telegram_account = telegram_id
        usr.save()
        return f'You have authenticated as a:\n {usr.first_name} {usr.second_name}'
