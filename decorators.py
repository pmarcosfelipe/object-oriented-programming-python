from typing import Any


def my_decorator(func):
  def wrapper():
    print("before function call...")
    func()
    print("after function call...")

  return wrapper

@my_decorator
def my_function():
  print("calling my_function")


my_function()


class MyClassDecorator:
  def __init__(self, func) -> None:
    self.func = func

  def __call__(self) -> Any:
    print("MyClassDecorator: before function call...")
    self.func
    print("MyClassDecorator: after function call...")


@MyClassDecorator
def my_other_function():
  print("calling my_other_function")

my_other_function()