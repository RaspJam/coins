from coin import BANK

def command(name: str):
    def decorator(func):
        option = getattr(func, "__option__", None)
        BANK.add_command(name, func if option is None else None)
        if option is not None:
            BANK.add_option(name, option, func)
        return func

    return decorator


def option(name: str):
    def decorator(func):
        if hasattr(func, "__option__"):
            raise ValueError(
                "Function already has `__option__` metadata!"
            )
        func.__option__ = name
        return func

    return decorator

# TODO: error on cases like this
# @option("alarm")
# def set_alarm():
#     pass
