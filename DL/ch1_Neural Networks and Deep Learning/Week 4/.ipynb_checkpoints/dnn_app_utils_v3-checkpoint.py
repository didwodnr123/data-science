{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import h5py\n",
    "\n",
    "\n",
    "def sigmoid(Z):\n",
    "    \"\"\"\n",
    "    Implements the sigmoid activation in numpy\n",
    "    \n",
    "    Arguments:\n",
    "    Z -- numpy array of any shape\n",
    "    \n",
    "    Returns:\n",
    "    A -- output of sigmoid(z), same shape as Z\n",
    "    cache -- returns Z as well, useful during backpropagation\n",
    "    \"\"\"\n",
    "    \n",
    "    A = 1/(1+np.exp(-Z))\n",
    "    cache = Z\n",
    "    \n",
    "    return A, cache\n",
    "\n",
    "def relu(Z):\n",
    "    \"\"\"\n",
    "    Implement the RELU function.\n",
    "\n",
    "    Arguments:\n",
    "    Z -- Output of the linear layer, of any shape\n",
    "\n",
    "    Returns:\n",
    "    A -- Post-activation parameter, of the same shape as Z\n",
    "    cache -- a python dictionary containing \"A\" ; stored for computing the backward pass efficiently\n",
    "    \"\"\"\n",
    "    \n",
    "    A = np.maximum(0,Z)\n",
    "    \n",
    "    assert(A.shape == Z.shape)\n",
    "    \n",
    "    cache = Z \n",
    "    return A, cache\n",
    "\n",
    "\n",
    "def relu_backward(dA, cache):\n",
    "    \"\"\"\n",
    "    Implement the backward propagation for a single RELU unit.\n",
    "\n",
    "    Arguments:\n",
    "    dA -- post-activation gradient, of any shape\n",
    "    cache -- 'Z' where we store for computing backward propagation efficiently\n",
    "\n",
    "    Returns:\n",
    "    dZ -- Gradient of the cost with respect to Z\n",
    "    \"\"\"\n",
    "    \n",
    "    Z = cache\n",
    "    dZ = np.array(dA, copy=True) # just converting dz to a correct object.\n",
    "    \n",
    "    # When z <= 0, you should set dz to 0 as well. \n",
    "    dZ[Z <= 0] = 0\n",
    "    \n",
    "    assert (dZ.shape == Z.shape)\n",
    "    \n",
    "    return dZ\n",
    "\n",
    "def sigmoid_backward(dA, cache):\n",
    "    \"\"\"\n",
    "    Implement the backward propagation for a single SIGMOID unit.\n",
    "\n",
    "    Arguments:\n",
    "    dA -- post-activation gradient, of any shape\n",
    "    cache -- 'Z' where we store for computing backward propagation efficiently\n",
    "\n",
    "    Returns:\n",
    "    dZ -- Gradient of the cost with respect to Z\n",
    "    \"\"\"\n",
    "    \n",
    "    Z = cache\n",
    "    \n",
    "    s = 1/(1+np.exp(-Z))\n",
    "    dZ = dA * s * (1-s)\n",
    "    \n",
    "    assert (dZ.shape == Z.shape)\n",
    "    \n",
    "    return dZ\n",
    "\n",
    "\n",
    "def load_data():\n",
    "    train_dataset = h5py.File('datasets/train_catvnoncat.h5', \"r\")\n",
    "    train_set_x_orig = np.array(train_dataset[\"train_set_x\"][:]) # your train set features\n",
    "    train_set_y_orig = np.array(train_dataset[\"train_set_y\"][:]) # your train set labels\n",
    "\n",
    "    test_dataset = h5py.File('datasets/test_catvnoncat.h5', \"r\")\n",
    "    test_set_x_orig = np.array(test_dataset[\"test_set_x\"][:]) # your test set features\n",
    "    test_set_y_orig = np.array(test_dataset[\"test_set_y\"][:]) # your test set labels\n",
    "\n",
    "    classes = np.array(test_dataset[\"list_classes\"][:]) # the list of classes\n",
    "    \n",
    "    train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))\n",
    "    test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))\n",
    "    \n",
    "    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes\n",
    "\n",
    "\n",
    "def initialize_parameters(n_x, n_h, n_y):\n",
    "    \"\"\"\n",
    "    Argument:\n",
    "    n_x -- size of the input layer\n",
    "    n_h -- size of the hidden layer\n",
    "    n_y -- size of the output layer\n",
    "    \n",
    "    Returns:\n",
    "    parameters -- python dictionary containing your parameters:\n",
    "                    W1 -- weight matrix of shape (n_h, n_x)\n",
    "                    b1 -- bias vector of shape (n_h, 1)\n",
    "                    W2 -- weight matrix of shape (n_y, n_h)\n",
    "                    b2 -- bias vector of shape (n_y, 1)\n",
    "    \"\"\"\n",
    "    \n",
    "    np.random.seed(1)\n",
    "    \n",
    "    W1 = np.random.randn(n_h, n_x)*0.01\n",
    "    b1 = np.zeros((n_h, 1))\n",
    "    W2 = np.random.randn(n_y, n_h)*0.01\n",
    "    b2 = np.zeros((n_y, 1))\n",
    "    \n",
    "    assert(W1.shape == (n_h, n_x))\n",
    "    assert(b1.shape == (n_h, 1))\n",
    "    assert(W2.shape == (n_y, n_h))\n",
    "    assert(b2.shape == (n_y, 1))\n",
    "    \n",
    "    parameters = {\"W1\": W1,\n",
    "                  \"b1\": b1,\n",
    "                  \"W2\": W2,\n",
    "                  \"b2\": b2}\n",
    "    \n",
    "    return parameters     \n",
    "\n",
    "\n",
    "def initialize_parameters_deep(layer_dims):\n",
    "    \"\"\"\n",
    "    Arguments:\n",
    "    layer_dims -- python array (list) containing the dimensions of each layer in our network\n",
    "    \n",
    "    Returns:\n",
    "    parameters -- python dictionary containing your parameters \"W1\", \"b1\", ..., \"WL\", \"bL\":\n",
    "                    Wl -- weight matrix of shape (layer_dims[l], layer_dims[l-1])\n",
    "                    bl -- bias vector of shape (layer_dims[l], 1)\n",
    "    \"\"\"\n",
    "    \n",
    "    np.random.seed(1)\n",
    "    parameters = {}\n",
    "    L = len(layer_dims)            # number of layers in the network\n",
    "\n",
    "    for l in range(1, L):\n",
    "        parameters['W' + str(l)] = np.random.randn(layer_dims[l], layer_dims[l-1]) / np.sqrt(layer_dims[l-1]) #*0.01\n",
    "        parameters['b' + str(l)] = np.zeros((layer_dims[l], 1))\n",
    "        \n",
    "        assert(parameters['W' + str(l)].shape == (layer_dims[l], layer_dims[l-1]))\n",
    "        assert(parameters['b' + str(l)].shape == (layer_dims[l], 1))\n",
    "\n",
    "        \n",
    "    return parameters\n",
    "\n",
    "def linear_forward(A, W, b):\n",
    "    \"\"\"\n",
    "    Implement the linear part of a layer's forward propagation.\n",
    "\n",
    "    Arguments:\n",
    "    A -- activations from previous layer (or input data): (size of previous layer, number of examples)\n",
    "    W -- weights matrix: numpy array of shape (size of current layer, size of previous layer)\n",
    "    b -- bias vector, numpy array of shape (size of the current layer, 1)\n",
    "\n",
    "    Returns:\n",
    "    Z -- the input of the activation function, also called pre-activation parameter \n",
    "    cache -- a python dictionary containing \"A\", \"W\" and \"b\" ; stored for computing the backward pass efficiently\n",
    "    \"\"\"\n",
    "    \n",
    "    Z = W.dot(A) + b\n",
    "    \n",
    "    assert(Z.shape == (W.shape[0], A.shape[1]))\n",
    "    cache = (A, W, b)\n",
    "    \n",
    "    return Z, cache\n",
    "\n",
    "def linear_activation_forward(A_prev, W, b, activation):\n",
    "    \"\"\"\n",
    "    Implement the forward propagation for the LINEAR->ACTIVATION layer\n",
    "\n",
    "    Arguments:\n",
    "    A_prev -- activations from previous layer (or input data): (size of previous layer, number of examples)\n",
    "    W -- weights matrix: numpy array of shape (size of current layer, size of previous layer)\n",
    "    b -- bias vector, numpy array of shape (size of the current layer, 1)\n",
    "    activation -- the activation to be used in this layer, stored as a text string: \"sigmoid\" or \"relu\"\n",
    "\n",
    "    Returns:\n",
    "    A -- the output of the activation function, also called the post-activation value \n",
    "    cache -- a python dictionary containing \"linear_cache\" and \"activation_cache\";\n",
    "             stored for computing the backward pass efficiently\n",
    "    \"\"\"\n",
    "    \n",
    "    if activation == \"sigmoid\":\n",
    "        # Inputs: \"A_prev, W, b\". Outputs: \"A, activation_cache\".\n",
    "        Z, linear_cache = linear_forward(A_prev, W, b)\n",
    "        A, activation_cache = sigmoid(Z)\n",
    "    \n",
    "    elif activation == \"relu\":\n",
    "        # Inputs: \"A_prev, W, b\". Outputs: \"A, activation_cache\".\n",
    "        Z, linear_cache = linear_forward(A_prev, W, b)\n",
    "        A, activation_cache = relu(Z)\n",
    "    \n",
    "    assert (A.shape == (W.shape[0], A_prev.shape[1]))\n",
    "    cache = (linear_cache, activation_cache)\n",
    "\n",
    "    return A, cache\n",
    "\n",
    "def L_model_forward(X, parameters):\n",
    "    \"\"\"\n",
    "    Implement forward propagation for the [LINEAR->RELU]*(L-1)->LINEAR->SIGMOID computation\n",
    "    \n",
    "    Arguments:\n",
    "    X -- data, numpy array of shape (input size, number of examples)\n",
    "    parameters -- output of initialize_parameters_deep()\n",
    "    \n",
    "    Returns:\n",
    "    AL -- last post-activation value\n",
    "    caches -- list of caches containing:\n",
    "                every cache of linear_relu_forward() (there are L-1 of them, indexed from 0 to L-2)\n",
    "                the cache of linear_sigmoid_forward() (there is one, indexed L-1)\n",
    "    \"\"\"\n",
    "\n",
    "    caches = []\n",
    "    A = X\n",
    "    L = len(parameters) // 2                  # number of layers in the neural network\n",
    "    \n",
    "    # Implement [LINEAR -> RELU]*(L-1). Add \"cache\" to the \"caches\" list.\n",
    "    for l in range(1, L):\n",
    "        A_prev = A \n",
    "        A, cache = linear_activation_forward(A_prev, parameters['W' + str(l)], parameters['b' + str(l)], activation = \"relu\")\n",
    "        caches.append(cache)\n",
    "    \n",
    "    # Implement LINEAR -> SIGMOID. Add \"cache\" to the \"caches\" list.\n",
    "    AL, cache = linear_activation_forward(A, parameters['W' + str(L)], parameters['b' + str(L)], activation = \"sigmoid\")\n",
    "    caches.append(cache)\n",
    "    \n",
    "    assert(AL.shape == (1,X.shape[1]))\n",
    "            \n",
    "    return AL, caches\n",
    "\n",
    "def compute_cost(AL, Y):\n",
    "    \"\"\"\n",
    "    Implement the cost function defined by equation (7).\n",
    "\n",
    "    Arguments:\n",
    "    AL -- probability vector corresponding to your label predictions, shape (1, number of examples)\n",
    "    Y -- true \"label\" vector (for example: containing 0 if non-cat, 1 if cat), shape (1, number of examples)\n",
    "\n",
    "    Returns:\n",
    "    cost -- cross-entropy cost\n",
    "    \"\"\"\n",
    "    \n",
    "    m = Y.shape[1]\n",
    "\n",
    "    # Compute loss from aL and y.\n",
    "    cost = (1./m) * (-np.dot(Y,np.log(AL).T) - np.dot(1-Y, np.log(1-AL).T))\n",
    "    \n",
    "    cost = np.squeeze(cost)      # To make sure your cost's shape is what we expect (e.g. this turns [[17]] into 17).\n",
    "    assert(cost.shape == ())\n",
    "    \n",
    "    return cost\n",
    "\n",
    "def linear_backward(dZ, cache):\n",
    "    \"\"\"\n",
    "    Implement the linear portion of backward propagation for a single layer (layer l)\n",
    "\n",
    "    Arguments:\n",
    "    dZ -- Gradient of the cost with respect to the linear output (of current layer l)\n",
    "    cache -- tuple of values (A_prev, W, b) coming from the forward propagation in the current layer\n",
    "\n",
    "    Returns:\n",
    "    dA_prev -- Gradient of the cost with respect to the activation (of the previous layer l-1), same shape as A_prev\n",
    "    dW -- Gradient of the cost with respect to W (current layer l), same shape as W\n",
    "    db -- Gradient of the cost with respect to b (current layer l), same shape as b\n",
    "    \"\"\"\n",
    "    A_prev, W, b = cache\n",
    "    m = A_prev.shape[1]\n",
    "\n",
    "    dW = 1./m * np.dot(dZ,A_prev.T)\n",
    "    db = 1./m * np.sum(dZ, axis = 1, keepdims = True)\n",
    "    dA_prev = np.dot(W.T,dZ)\n",
    "    \n",
    "    assert (dA_prev.shape == A_prev.shape)\n",
    "    assert (dW.shape == W.shape)\n",
    "    assert (db.shape == b.shape)\n",
    "    \n",
    "    return dA_prev, dW, db\n",
    "\n",
    "def linear_activation_backward(dA, cache, activation):\n",
    "    \"\"\"\n",
    "    Implement the backward propagation for the LINEAR->ACTIVATION layer.\n",
    "    \n",
    "    Arguments:\n",
    "    dA -- post-activation gradient for current layer l \n",
    "    cache -- tuple of values (linear_cache, activation_cache) we store for computing backward propagation efficiently\n",
    "    activation -- the activation to be used in this layer, stored as a text string: \"sigmoid\" or \"relu\"\n",
    "    \n",
    "    Returns:\n",
    "    dA_prev -- Gradient of the cost with respect to the activation (of the previous layer l-1), same shape as A_prev\n",
    "    dW -- Gradient of the cost with respect to W (current layer l), same shape as W\n",
    "    db -- Gradient of the cost with respect to b (current layer l), same shape as b\n",
    "    \"\"\"\n",
    "    linear_cache, activation_cache = cache\n",
    "    \n",
    "    if activation == \"relu\":\n",
    "        dZ = relu_backward(dA, activation_cache)\n",
    "        dA_prev, dW, db = linear_backward(dZ, linear_cache)\n",
    "        \n",
    "    elif activation == \"sigmoid\":\n",
    "        dZ = sigmoid_backward(dA, activation_cache)\n",
    "        dA_prev, dW, db = linear_backward(dZ, linear_cache)\n",
    "    \n",
    "    return dA_prev, dW, db\n",
    "\n",
    "def L_model_backward(AL, Y, caches):\n",
    "    \"\"\"\n",
    "    Implement the backward propagation for the [LINEAR->RELU] * (L-1) -> LINEAR -> SIGMOID group\n",
    "    \n",
    "    Arguments:\n",
    "    AL -- probability vector, output of the forward propagation (L_model_forward())\n",
    "    Y -- true \"label\" vector (containing 0 if non-cat, 1 if cat)\n",
    "    caches -- list of caches containing:\n",
    "                every cache of linear_activation_forward() with \"relu\" (there are (L-1) or them, indexes from 0 to L-2)\n",
    "                the cache of linear_activation_forward() with \"sigmoid\" (there is one, index L-1)\n",
    "    \n",
    "    Returns:\n",
    "    grads -- A dictionary with the gradients\n",
    "             grads[\"dA\" + str(l)] = ... \n",
    "             grads[\"dW\" + str(l)] = ...\n",
    "             grads[\"db\" + str(l)] = ... \n",
    "    \"\"\"\n",
    "    grads = {}\n",
    "    L = len(caches) # the number of layers\n",
    "    m = AL.shape[1]\n",
    "    Y = Y.reshape(AL.shape) # after this line, Y is the same shape as AL\n",
    "    \n",
    "    # Initializing the backpropagation\n",
    "    dAL = - (np.divide(Y, AL) - np.divide(1 - Y, 1 - AL))\n",
    "    \n",
    "    # Lth layer (SIGMOID -> LINEAR) gradients. Inputs: \"AL, Y, caches\". Outputs: \"grads[\"dAL\"], grads[\"dWL\"], grads[\"dbL\"]\n",
    "    current_cache = caches[L-1]\n",
    "    grads[\"dA\" + str(L-1)], grads[\"dW\" + str(L)], grads[\"db\" + str(L)] = linear_activation_backward(dAL, current_cache, activation = \"sigmoid\")\n",
    "    \n",
    "    for l in reversed(range(L-1)):\n",
    "        # lth layer: (RELU -> LINEAR) gradients.\n",
    "        current_cache = caches[l]\n",
    "        dA_prev_temp, dW_temp, db_temp = linear_activation_backward(grads[\"dA\" + str(l + 1)], current_cache, activation = \"relu\")\n",
    "        grads[\"dA\" + str(l)] = dA_prev_temp\n",
    "        grads[\"dW\" + str(l + 1)] = dW_temp\n",
    "        grads[\"db\" + str(l + 1)] = db_temp\n",
    "\n",
    "    return grads\n",
    "\n",
    "def update_parameters(parameters, grads, learning_rate):\n",
    "    \"\"\"\n",
    "    Update parameters using gradient descent\n",
    "    \n",
    "    Arguments:\n",
    "    parameters -- python dictionary containing your parameters \n",
    "    grads -- python dictionary containing your gradients, output of L_model_backward\n",
    "    \n",
    "    Returns:\n",
    "    parameters -- python dictionary containing your updated parameters \n",
    "                  parameters[\"W\" + str(l)] = ... \n",
    "                  parameters[\"b\" + str(l)] = ...\n",
    "    \"\"\"\n",
    "    \n",
    "    L = len(parameters) // 2 # number of layers in the neural network\n",
    "\n",
    "    # Update rule for each parameter. Use a for loop.\n",
    "    for l in range(L):\n",
    "        parameters[\"W\" + str(l+1)] = parameters[\"W\" + str(l+1)] - learning_rate * grads[\"dW\" + str(l+1)]\n",
    "        parameters[\"b\" + str(l+1)] = parameters[\"b\" + str(l+1)] - learning_rate * grads[\"db\" + str(l+1)]\n",
    "        \n",
    "    return parameters\n",
    "\n",
    "def predict(X, y, parameters):\n",
    "    \"\"\"\n",
    "    This function is used to predict the results of a  L-layer neural network.\n",
    "    \n",
    "    Arguments:\n",
    "    X -- data set of examples you would like to label\n",
    "    parameters -- parameters of the trained model\n",
    "    \n",
    "    Returns:\n",
    "    p -- predictions for the given dataset X\n",
    "    \"\"\"\n",
    "    \n",
    "    m = X.shape[1]\n",
    "    n = len(parameters) // 2 # number of layers in the neural network\n",
    "    p = np.zeros((1,m))\n",
    "    \n",
    "    # Forward propagation\n",
    "    probas, caches = L_model_forward(X, parameters)\n",
    "\n",
    "    \n",
    "    # convert probas to 0/1 predictions\n",
    "    for i in range(0, probas.shape[1]):\n",
    "        if probas[0,i] > 0.5:\n",
    "            p[0,i] = 1\n",
    "        else:\n",
    "            p[0,i] = 0\n",
    "    \n",
    "    #print results\n",
    "    #print (\"predictions: \" + str(p))\n",
    "    #print (\"true labels: \" + str(y))\n",
    "    print(\"Accuracy: \"  + str(np.sum((p == y)/m)))\n",
    "        \n",
    "    return p\n",
    "\n",
    "def print_mislabeled_images(classes, X, y, p):\n",
    "    \"\"\"\n",
    "    Plots images where predictions and truth were different.\n",
    "    X -- dataset\n",
    "    y -- true labels\n",
    "    p -- predictions\n",
    "    \"\"\"\n",
    "    a = p + y\n",
    "    mislabeled_indices = np.asarray(np.where(a == 1))\n",
    "    plt.rcParams['figure.figsize'] = (40.0, 40.0) # set default size of plots\n",
    "    num_images = len(mislabeled_indices[0])\n",
    "    for i in range(num_images):\n",
    "        index = mislabeled_indices[1][i]\n",
    "        \n",
    "        plt.subplot(2, num_images, i + 1)\n",
    "        plt.imshow(X[:,index].reshape(64,64,3), interpolation='nearest')\n",
    "        plt.axis('off')\n",
    "        plt.title(\"Prediction: \" + classes[int(p[0,index])].decode(\"utf-8\") + \" \\n Class: \" + classes[y[0,index]].decode(\"utf-8\"))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}