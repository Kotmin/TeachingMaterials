from ct.timing import timing

a = '0'


@timing
def static_print():
    print("Score: 0")


@timing
def concat_print():
    print("Score: " + a)


@timing
def f_str_print():
    print(f"Score: {a}")


@timing
def regular_print():
    print("Score: ",a)


@timing
def percentage_print():
    print("Score: %s"%(a))


@timing
def format_print():
    print("Score: {0}".format(a))


# Poglądowo
static_print()

# I. miejsce
concat_print()
f_str_print()

regular_print()

percentage_print()
format_print()





# https://docs.python.org/3/tutorial/inputoutput.html

