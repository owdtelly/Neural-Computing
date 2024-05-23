import torch.nn as nn
import torch


class MLP(nn.Module):

    def __init__(self, input_size, hidden_size, output_size, dropout=0.5):
        super(MLP, self).__init__()
        self.dropout = nn.Dropout(dropout)
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()

    def forward(self, X):
        X = self.relu(self.fc1(X))
        X = self.dropout(X)
        X = self.sigmoid(self.fc2(X))

        return X
