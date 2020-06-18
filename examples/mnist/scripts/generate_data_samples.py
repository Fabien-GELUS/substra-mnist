# Copyright 2018 Owkin, inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Script to generate data to be registered to Substra
Mnist example
"""

import os
import numpy as np
# Import dataset
print("Loading data from keras.datasets.mnist ...")
import keras
from keras.datasets import mnist

# the data, split between train and test sets
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# train features, train labels, test features, test labels
file_path = os.path.dirname(__file__)
root_path = os.path.join(file_path,'..')
assets_path = os.path.join(root_path, 'assets')

print("Data will be generated in : ",os.path.abspath(assets_path))

OUT_FILE = {
    os.path.join("train_data","features", "x_train.npy"): x_train,
    os.path.join("train_data","labels", "y_train.npy"): y_train,
    os.path.join("test_data", "features","x_test.npy"): x_test,
    os.path.join("test_data", "labels","y_test.npy"): y_test,

}

for filename, data in OUT_FILE.items():
    full_path = os.path.join(assets_path,filename)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    np.save(full_path, data)
    print("File created : ", filename)
    
