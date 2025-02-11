# Using Miniconda

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