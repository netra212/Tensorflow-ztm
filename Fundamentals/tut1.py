# Tensorflow purpose: turn data into numbers (tensors) and build machine learning algorithms to find patterns in them.

# Create timestamp. 
# import datetime 

# print("------------------------------------")
# print(f"Notebook last run (end-to-end): {datetime.datetime.now()}")
# print("------------------------------------")

'''
# tensors are kind of like NumPy arrays. Tensor as a multi-dimensional numerical representation of something. (Also, referred to as n-dimensional, where n can be any number). 
-> Using tensors to represent the price of houses.
-> Using tensors to represent the pixels of an image.
-> Using tensors to represent words.
-> Or it could be some other form of information (or data) you want to represent with numbers

# Note: 
The main difference between `tensors` and `NumPy arrays` (also an n-dimensional array of numbers) is that tensors can be used on GPUs (graphical processing units) and TPUs (tensor processing units).
'''

# print("------------------------------------")
import tensorflow as tf 
# print("\n Tensorflow Version: ",tf.__version__)
# print("------------------------------------")

# A scalar is known as a rank 0 tensor. Because it has no dimensions (it's just a number).
# Create a scalar (rank 0 tensor).
print("------------------------------------")
scalar = tf.constant(7)
print(scalar)
print("------------------------------------")

print("------------------------------------")
print("\nChecking the number of dimensions of a tensor: (ndim stands for number of dimensions.)")
print(scalar.ndim)


print("\nCreate a vector (more than 0 dimensions.)")
vector = tf.constant([10, 10])
print(vector)
print("\nDimension of vector: ", vector.ndim)

print("\nCreate a matrix (more than 1 dimension)")
matrix = tf.constant([[10, 7],
[7, 10]])
print(matrix)

print("\n# Create another matrix and define the datatype")
another_matrix = tf.constant([[10., 7.],
                        [3., 2.],
                        [8., 9.]], dtype=tf.float16) # specify the datatypes wiuth 'dtype'. 

print(another_matrix)
print("# Even though another_matrix contains more numbers, its dimension stay the same: ", another_matrix.ndim)

print("\n # How about a tensor? (more than 2 dimensions, although, all of the above items are also technically tensors.")
tensor = tf.constant([
    [[1, 2, 3], [4, 5, 6]], 
    [[7, 8, 9],[10, 11, 12]],
    [[13, 14, 15], [16, 17, 18]]
                    ])
print(tensor)   
print("shape of tensor: ", tensor.ndim)           
print("------------------------------------")

'''
The above is known as a rank 3 tensor (3-dimensions), however a tensor can have an arbitrary (unlimited) amount of dimensions.

For example, you might turn a series of images into tensors with shape (224, 224, 3, 32), where:
    -> 224, 224 (the first 2 dimensions) are the height and width of the images in pixels.
    -> 3 is the number of colour channels of the image (red, green blue).
    -> 32 is the batch size (the number of images a neural network sees at any one time).

Note:
a. scalar: a single number.
b. vector: a number with direction (e.g. wind speed with direction).
c. matrix: a 2-dimensional array of numbers.
d. tensor: an n-dimensional arrary of numbers (where n can be any number, a 0-dimension tensor is a scalar, a 1-dimension tensor is a vector).

# To add to the confusion, the terms matrix and tensor are often used interchangably.
'''


print("\n------------------------------------------------------------")
print("# Creating Tensors with tf.Variable()")
# Create the same tensor with tf.Variable() and tf.constant()
changeable_tensors = tf.Variable([10, 7])
unchangeable_tensors = tf.constant([10, 7])
print(changeable_tensors, unchangeable_tensors)

# Let's try to change the one element of the changeable tensors. 

# changeable_tensors[0] = 7 # will through an error (because it requires an .assign() method).

changeable_tensors[0].assign(90)
print(changeable_tensors)

# But if we try to change a value in tf.constant() tensor. 

# unchangeable_tensors[0].assign(78) # Will error (can't change tf.constant())
# print(unchangeable_tensors)


'''
# Which one should you use? tf.constant() or tf.Variable()?
=> It will depend on what your problem requires. However, most of the time, TensorFlow will automatically choose for you (when loading data or modelling data).

# Why would you want to create random tensors?
=> This is what neural networks use to intialize their weights (patterns) that they're trying to learn in the data.
For example, the process of a neural network learning often involves taking a random n-dimensional array of numbers and refining them until they represent some kind of pattern (a compressed way to represent the original data).

- A network learns by starting with random patterns (1) then going through demonstrative examples of data (2) whilst trying to update its random patterns to represent the examples (3).
'''


print("# We can create random tensors by using the tf.random.Generator class.")
print("# Create two random (but the same) tensors. ")
random_1 = tf.random.Generator.from_seed(42) # set the seed for reproducibility. 
random_1 = random_1.normal(shape=(3, 2)) # create tensor from a normal distribution. 

random_2 = tf.random.Generator.from_seed(42)
random_2 = random_2.normal(shape=(3, 2))

print("Random Number 1: ", random_1)
print("Random Number 2: ", random_2)

# Are they equal ?
# print(random_1, random_2, random_1 == random_2)


# Create two random (and different) tensors. 
random_3 = tf.random.Generator.from_seed(42)
random_3 = random_3.normal(shape=(3, 2))

random_4 = tf.random.Generator.from_seed(42)
random_4 = random_4.normal(shape=(3, 2))

# Check the tensors and see if they are equal. 
# print(random_3, random_4, random_1 == random_3, random_3 == random_4)


#  What if you wanted to shuffle the order of a tensor ?
# Let's say you working with 15,000 images of cats and dogs and the first 10,000 images of were of cats and the next 5,000 were of dogs. This order could effect how a neural network learns (it may overfit by learning the order of the data), instead, it might be a good idea to move your data around.
print("# shuffle a tensor (valuable for when we want to shuffle our data)")
not_shuffled = tf.random.Generator.from_seed(42)
not_shuffled = not_shuffled.normal(shape=(3, 2))

# Get different results each time. 
print("Getting an different tensors each time runs: ")
print(tf.random.shuffle(not_shuffled))

print("\n------------------------------------------------------------")






