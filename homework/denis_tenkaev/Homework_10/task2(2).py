def repeat_me(count):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(count):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat_me(count=4)
def example(text):
    print(text)


example("print me")
# Этот пример я погуглил и почитал про декораторы с
# аргументами, поэтому можно сказать не сам сделал, но идею понял.
