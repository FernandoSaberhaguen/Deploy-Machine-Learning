from utils import Utils
from models import Models

if __name__ == '__main__':
    utils = Utils()

    models = Models()
    data = utils.load_from_csv('./in/housing.csv')
    X, y = utils.feature_target(data, ['MEDV', 'B', 'DIS', 'CHAS'],['MEDV'])
    
    models.grid_training(X,y)

    #data.head(4)
