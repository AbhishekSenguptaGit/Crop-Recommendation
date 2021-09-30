## imports
import os
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.externals import joblib
import keys
import cPickle, urllib2

'''
model class that holds
input = this years weather data by zip code
classifier = the random forrest classifier
mlb = the lable binarizer
validZips = list of US zipcodes
us_farms = list of ceritified US organic farms 
'''
class model(object):
    def __init__(self, input, classifier, mlb, validZips, us_farms ):
        self.input = input
        self.classifier = classifier
        self.validZips = validZips
        self.farms = us_farms
        self.mlb = mlb

    '''
    gets a list of organic farms by zipcode
    @param zip, the zipcode to query
    @return the list of farms for that zipcode
    '''  
    def getFarms(self, zip):
        return self.farms[self.farms["Zip_Code"] == int(zip)]
    
    '''
    validates the zipcode query in validZips 
    and return the feature vector
    @param zip, the zipcode to query
    @return the feature vector for the zipcode
    if is valid or None
    '''  
    def submitZip(self, zip):
        '''validate the zipcode'''
        if int(zip) in self.validZips:
            return self.input[self.input.index==int(zip)]
        else:
            return None

    '''
    use the classifier to predict the probabilities
    based on the input returned from submitZip
    @param x_input, from submitZip
    @param limit, limit the returned list to top #
    @return top # of rankings
    '''          
    def predict(self,x_input,limit):
        '''load data into model and output probabilities'''
        x = x_input
        probabilities = np.zeros(self.mlb.classes_.shape)
        for c in range(len(self.classifier.estimators_)):
            probabilities[c] = self.classifier.estimators_[c].predict_proba(x)[0][1]
        rankings = zip(self.mlb.classes_, probabilities)
        rankings.sort(key=lambda x: x[1],reverse=True)
        return rankings[0:limit]

'''
load the model with the pickle dumps
the resource directory is assumed to be in 
the static folder under subfolder res
@return the model() object
'''     
def loadModel():
    resources_dir = os.getcwd() + "/static/res/" # main resource directory
    # aws_app_assets = "https://%s.s3.amazonaws.com/static/res/" % keys.AWS_BUCKET_NAME
    input = joblib.load(resources_dir + 'input.pkl')
    classifier = joblib.load(resources_dir + 'classifier.pkl')
    mlb = joblib.load(resources_dir + 'mlb.pkl')
    farms = joblib.load(resources_dir + 'farms.pkl')
    zipcodes = joblib.load(resources_dir + 'us_zips.pkl')

    # input = cPickle.load(urllib2.urlopen(aws_app_assets + 'input.pkl'))
    # classifier = cPickle.load(urllib2.urlopen(aws_app_assets + 'classifier.pkl'))
    # mlb = cPickle.load(urllib2.urlopen(aws_app_assets + 'mlb.pkl'))
    # farms = cPickle.load(urllib2.urlopen(aws_app_assets + 'farms.pkl'))
    # zipcodes = cPickle.load(urllib2.urlopen(aws_app_assets + 'us_zips.pkl'))

    mymodel = model(input, classifier, mlb, zipcodes, farms)
    return mymodel
