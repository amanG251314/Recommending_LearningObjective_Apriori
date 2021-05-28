from flask import Flask, request
import PredictingObjective
import pandas as pd
import numpy as np


data_learner=pd.read_csv('Dataset_FYP.csv')
data_apriori=pd.read_csv('aprioridata.csv')


def GettingNumerical(x):
    try:
        c1 = int(list(x)[-3])
        a = list(x)[-1]
        b = list(x)[-2]
        c = list(x)[-3]
        d = c + b + a
        d = int(d)
        return d
    except:
        try:
            b1 = int(list(x)[-2])
            a = list(x)[-1]
            b = list(x)[-2]
            c = b + a
            c = int(c)
            return c
        except:
            a = int(list(x)[-1])
            return a
data_learner['Learner ID_encoded'] = data_learner['Learner ID'].apply(lambda x: GettingNumerical(x))



app = Flask(__name__)


@app.route('/model', methods=['POST'])
def LMSRecommend():
    data = request.get_json(force=True)

    neighbours=PredictingObjective.Neighbour(data_learner,data['input'])

    final_data = data_apriori.iloc[neighbours.index]
    a=PredictingObjective.preprocessing(final_data,data['unit'],data['neighbours'])

    b = PredictingObjective.apri(a)

    return "The New Learner is {}".format(b)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
