
import argparse


def main():

    # Training settings
    parser = argparse.ArgumentParser(description='Main script for training, testingand using some model')

    # Select function to run
    parser.add_argument('--name_model', type=str, default=None,
                        help=' Give the model name (Default: None)')
    parser.add_argument('--operation', type=str, default=64, choices=["train", "predict"],
                        help='the kind of operation: train and test the model or predict some data (default: predict)')
    parser.add_argument('--architecture', type=str, default='tensorflow', choices=["tensorflow", "pytorch", "scikit-learn"],
                        help=' return the type of architecture (default: tensorflow)')
    parser.add_argument('--path_inputs', type=str, # if train use to model, if predict use to predic data
                        help='Path file or url to input model (default: None)')
    parser.add_argument('--transform', type=bool,
                        help='Flag to indicates if the input must be transformed (default: False)')
    
    # TODO: Change to a config file?
    # parameters
    parser.add_argument('--batch-size', type=int, default=64,
                        help='input batch size for training (default: 64)')
    parser.add_argument('--test-batch-size', type=int, default=1000,
                        help='input batch size for testing (default: 1000)')
    parser.add_argument('--epochs', type=int, default=14,
                        help='number of epochs to train (default: 14)')
    parser.add_argument('--lr', type=float, default=1.0,
                        help='learning rate (default: 1.0)')
    parser.add_argument('--gamma', type=float, default=0.7,
                        help='Learning rate step gamma (default: 0.7)')
    parser.add_argument("--optimizer", default="Adam", choices=["SGD", "Adadelta", "Adam"],
                    help="Optimizer of choice for training. (default=Adam)")
    
    # Save model
    parser.add_argument('--save-model', action='store_true', default=True,
                        help='For saving the current model and their parameters')
    
    # Device and GPU settings
    parser.add_argument("--gpuid", default=[0], nargs='+', type=int,
                    help="ID of gpu device to use. Empty implies CPU usage.")
    parser.add_argument('--no-cuda', action='store_true', default=False,
                        help='disables CUDA training') 
    parser.add_argument('--no-mps', action='store_true', default=False,
                        help='disables macOS GPU training')


    # Set device when avaible?
    # if use_cuda:
    #     device = torch.device("cuda")
    # elif use_mps:
    #     device = torch.device("mps")
    # else:
    #     device = torch.device("cpu")

    train_kwargs = {'batch_size': args.batch_size, 'learning_rate': args.lr, 'epochs': args.epochs, 'optimizer': args.optimizer}
    test_kwargs = {'batch_size': args.test_batch_size}
    
    operations = {"train": train, "predict": predict}

