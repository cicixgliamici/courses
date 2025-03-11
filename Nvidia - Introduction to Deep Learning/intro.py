import torch
import torch.nn as nn

# Custom convolutional block with common CNN operations
 """
        A convolutional block containing:
        - Conv2d layer
        - Batch normalization
        - ReLU activation
        - Dropout regularization
        - Max pooling
        
        Args:
            in_ch (int): Number of input channels
            out_ch (int): Number of output channels
            dropout_p (float): Dropout probability (0-1)
"""
class MyConvBlock(nn.Module):
    def __init__(self, in_ch, out_ch, dropout_p):
        kernel_size = 3
        super().__init__()

        # Sequential container for operations
        self.model = nn.Sequential(
            # Conv layer with padding to maintain spatial dimensions
            nn.Conv2d(in_ch, out_ch, kernel_size, stride=1, padding=1),
            # Batch normalization for stability and faster training
            nn.BatchNorm2d(out_ch),
            # Non-linear activation
            nn.ReLU(),
            # Regularization to prevent overfitting
            nn.Dropout(dropout_p),
            # Downsampling with max pooling
            nn.MaxPool2d(2, stride=2)
        )

    def forward(self, x):
        """Forward pass through the block"""
        return self.model(x)

"""
    Calculate accuracy for a batch
    
    Args:
        output (torch.Tensor): Model predictions (logits)
        y (torch.Tensor): Ground truth labels
        N (int): Total number of samples in dataset (train/val)
    
    Returns:
        float: Accuracy for this batch as portion of total samples
"""
def get_batch_accuracy(output, y, N):
    # Get predicted class indices
    pred = output.argmax(dim=1, keepdim=True)
    # Count correct predictions
    correct = pred.eq(y.view_as(pred)).sum().item()
    # Return accuracy proportion relative to total dataset size
    return correct / N


"""
    Training loop for one epoch
    
    Args:
        model (nn.Module): Model to train
        train_loader (DataLoader): Training data loader
        train_N (int): Total training samples
        random_trans (transforms): Data augmentation transforms
        optimizer (optim.Optimizer): Optimization algorithm
        loss_function: Loss criterion (e.g., CrossEntropyLoss)
 """
def train(model, train_loader, train_N, random_trans, optimizer, loss_function):
    epoch_loss = 0
    epoch_accuracy = 0

    # Set model to training mode
    model.train()
    
    # Iterate over batches
    for x, y in train_loader:
        # Apply data augmentation and forward pass
        output = model(random_trans(x))
        
        # Reset gradients
        optimizer.zero_grad()
        
        # Calculate loss
        batch_loss = loss_function(output, y)
        
        # Backpropagation
        batch_loss.backward()
        
        # Update weights
        optimizer.step()

        # Accumulate loss and accuracy
        epoch_loss += batch_loss.item()  # Note: This sums mean batch losses
        epoch_accuracy += get_batch_accuracy(output, y, train_N)

    # Print epoch statistics
    print('Train - Loss: {:.4f} Accuracy: {:.4f}'.format(
        epoch_loss,       # Sum of mean batch losses
        epoch_accuracy))  # Total correct / train_N


"""
    Validation loop
    
    Args:
        model (nn.Module): Trained model
        valid_loader (DataLoader): Validation data loader
        valid_N (int): Total validation samples
        loss_function: Loss criterion
"""
def validate(model, valid_loader, valid_N, loss_function):
    val_loss = 0
    val_accuracy = 0

    # Set model to evaluation mode
    model.eval()
    
    # Disable gradient computation
    with torch.no_grad():
        for x, y in valid_loader:
            # Forward pass
            output = model(x)

            # Accumulate loss and accuracy
            val_loss += loss_function(output, y).item()
            val_accuracy += get_batch_accuracy(output, y, valid_N)

    # Print validation statistics
    print('Valid - Loss: {:.4f} Accuracy: {:.4f}'.format(
        val_loss,        # Sum of mean batch losses 
        val_accuracy))   # Total correct / valid_N


"""
Key notes about the code:
The MyConvBlock implements a common CNN pattern: Conv -> BN -> ReLU -> Dropout -> Pooling
Training uses data augmentation (random_trans) while validation does not
Loss accumulation sums mean batch losses (might not represent true dataset average if batches vary in size)
Accuracy is calculated as total correct predictions divided by dataset size
The validation loop runs with torch.no_grad() to save memory and computation
Both training and validation outputs show accumulated values (not averaged per batch)
"""
