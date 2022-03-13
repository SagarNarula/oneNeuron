import numpy as np
import os
import joblib   


class Perceptron:
  def __init__(self,eta:float=None,epochs:int=None):
    self.weights=np.random.randn(3)*1e-4
    training=(eta is not None) and (epochs is not None)
    if training:
      print(f'Initial weights before training {self.weights}')
      self.eta=eta
      self.epochs=epochs
  def fit(self,X,y):
    self.X=X
    self.y=y
    X_with_bias = np.c_[self.X, -np.ones((len(self.X), 1))]
    print(f"X with bias: \n{X_with_bias}")
        
    for epoch in range(self.epochs):
        print("--"*10)
        print(f"for epoch >> {epoch}")
        print("--"*10)
        z = self._z_outcome(X_with_bias, self.weights)
        y_hat = self.activation_function(z)
        print(f"predicted value after forward pass: \n{y_hat}")

        self.error= self.y - y_hat
        print(f"error :{self.error}")

        self.weights=self.weights+self.eta*np.dot(X_with_bias.T,self.error)
        print(f"updated weights after epoch: {epoch}/{self.epochs}: \n{self.weights}")
        print("##"*10)


  def _z_outcome(self,inputs, weights):
     return np.dot(inputs,weights)

  def activation_function(self,z):
    return np.where(z>0,1,0)

  def predict(self,X):

    X_with_bias = np.c_[X, -np.ones((len(X), 1))]
    z = self._z_outcome(X_with_bias, self.weights)
    return self.activation_function(z)
  
  def total_loss(self):
    total_loss=np.sum(self.error)
    print(f"\ntotal loss: {total_loss}\n")
    return total_loss
  
  def _create_dir_return_path(self, model_dir, filename):
    os.makedirs(model_dir, exist_ok=True)
    return os.path.join(model_dir, filename)
    
  def save(self, filename, model_dir=None):
    if model_dir is not None:
      model_file_path = self._create_dir_return_path(model_dir, filename)
      joblib.dump(self, model_file_path)
    else:
      model_file_path = self._create_dir_return_path("model", filename)
      joblib.dump(self, model_file_path)
    
  def load(self, filepath):
        return joblib.load(filepath)



