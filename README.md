# Creating and Exporting Miniconda Environment

In Miniconda an environment was created called 'cs_assign1'
```ruby
$ conda create --name cs_assign1 python=3.10
```


Then to activate the environment in Miniconda
```ruby
$ conda activate cs_assign1
```


Once the environment is activated, two packages were installed: Numpy and Matplotlib
```ruby
$ conda install Numpy
$ conda install Matplotlib
```


Environment was then exported
```ruby
$ conda env export > requirements.yaml
```


Inside VS Code teminal create an environment for requirements.yaml
```ruby
conda create --name cs_assign1 --file requirements.yaml
```



## Inside Main Branch

This is an updated version of one of the decorator examples in class
```ruby
import random

def cache(func):
    cache_dic = {}
    def wrapper(*args):
        if args in cache_dic:
            return cache_dic[args]
        result = func(*args)
        cache_dic[args] = result
        return result
    return wrapper


@cache
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


def main():
    random_number = random.randint(1,100)
    print(random_number)

    print(fib(random_number))


if __name__ == "__main__":
    main()
```


### Picture

This is the code to add and Image
```ruby
![Alt text](image_url)
```

Here is an image
![This is Ducky my dog](Ducky.jpg)