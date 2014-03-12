from __future__ import division
import decimal


# Get context
context = decimal.getcontext()

# Decimal math operations shortcut
add = context.add
divide_int = context.divide_int
remainder = context.remainder
divide = context.divide
multiply = context.multiply
subtract = context.subtract

# Decimal shortcut
D = decimal.Decimal


def quantize(func):
    """
    Decorator to change output decimal to 2 places
    """

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.quantize(D('0.01'))

    return wrapper


def round(amount):
    """
    Python implementation of Malaysian's "Jimat dan SENang Kira"
    @param float amount to convert
    @return Decimal rounded amount
    """
    cost = D(amount)
    integer = divide_int(cost, D(1.00))
    tenths = divide(divide_int(multiply(remainder(cost, D(1.00)), D(10.00)), D(1.00)), D(10.00))
    hundredths = subtract(subtract(cost, integer), tenths).quantize(D('0.01'))

    @quantize
    def round_up():
        return add(add(integer, tenths), D(0.10))

    @quantize
    def round_down():
        return add(integer, tenths)

    @quantize
    def round_half():
        return add(add(integer, tenths), D(0.05))

    @quantize
    def no_round():
        return add(add(integer, tenths), hundredths)

    if hundredths in (map(D,['0.01', '0.02'])):
        return round_down()
    elif hundredths in (map(D, ['0.03', '0.04', '0.06', '0.07'])):
        return round_half()
    elif hundredths in (map(D, ['0.08', '0.09'])):
        return round_up()
    else:
        return no_round()
