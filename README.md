# 15150-HW-Starter
We can do better than the released template.

    The 'template.tex' the 150 staff gives us is nice, but with a little
scripting we can be slightly lazier. Using the following syntax

    shell> startHW.py <homework number>

a starter file will be generated for you, adding your name, Andrew ID, Section,
and current date.

    Enjoy! Let me know if you catch any bugs, whether it is in startHW.py or
the modded LaTeX template.

Some notes on my modded template:
    You can modify the template used (see resources/template.tex) to add your
own commands or remove mine. The ones I've added include \tab, \code, commands
for work and span of a function, left and right grouping symbols, and a symbol
for the set of natural numbers.
    Syntax for both \work and \span are as follows
        \work{function_name}{parameters}
        \funspan{function_name}{parameters}
Note that you must be in math mode to use either command (for subscripting).
