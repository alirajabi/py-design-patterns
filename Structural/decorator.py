from functools import wraps


def make_bold(fn):
    return getwrapped(fn, "b")


def make_italic(fn):
    return getwrapped(fn, "i")


def getwrapped(function, tag):
    # This makes the decorator transparent in terms of its name and docstring
    @wraps(function)
    def wrapped():
        # Grab the return value of the function being decorated
        function_result = function()

        # Add new functionality to the function being decorated
        return "<%s>%s</%s>" % (tag, function_result, tag)

    return wrapped


@make_bold
@make_italic
def hello():
    """a decorated hello world"""
    return "hello world"


if __name__ == '__main__':
    print('result:{}   name:{}   doc:{}'.format(hello(), hello.__name__, hello.__doc__))
