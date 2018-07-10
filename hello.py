
def hello(name):
  if not name:
    print("hello world!")
  else:
    print("hello " + name)


if __name__ == '__main__':
  input_name = input("Please input a name to continue: ")
  hello(input_name)
