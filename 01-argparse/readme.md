# Argparse in python

- Parser for command-line options, arguments and sub-commands

---

```python
import argparse

parser = argparse.ArgumentParser(description="my argparse program") # create a parser

# add argument
#       - arguments without (--) are positional arguments
#       - arguments with (--) are optional arguments, and are None by default
#       - to use multiple name for same arg `comma separate them`
#       - if you only want to use an argument as true or false, use action="store_true"
#       - you can also use `default` key to specify default value instead of None
#       - help msg is printed when user runs program with `--help`

# positional arguments (required) - (name, number)
parser.add_argument("name", type=str, help="display name")
parser.add_argument("number", type=int, help="display square of a given number")

# optional arguments (until set required to True)
parser.add_argument("-v", "--verbosity",
                    help="increase output verbosity", action="store_true")
parser.add_argument("--hostname",help="Print hostname ", default="127.0.0.1",)
parser.add_argument("--no-of-workers", type=int,help="number of workers", choices=[1,2,3,4,5], default=2)
parser.add_argument("--meow","-m",help="meows back", action="count", default=0)



args = parser.parse_args() # <--- parse the arguments from the command line

print(f"{args=}")
print(f"{args.__dict__=}")

answer = args.number**2
print(answer)
```