import joblib as jl
import numpy as np
import os

model_path = os.path.join(os.path.dirname(__file__), 'models/urcheck_rf.joblib')
model = jl.load(model_path)

def main(args):

    res_temp = {"headers": {'content-type': 'application/json; charset=UTF-8'}, 
                "body": ""}
    try:
        input_list = []
        # this order matters
        # age,sex,cough,fever,chills,sore_throat,headache,fatigue
        print(args)
        input_list.append(args["age"])
        input_list.append(args["gender"])
        input_list.append(args.get("cough", 0))
        input_list.append(args.get("fever", 0))
        input_list.append(args.get("chills", 0))
        input_list.append(args.get("sore", 0))
        input_list.append(args.get("headache", 0))
        input_list.append(args.get("fatigue", 0))

        # check for datatypes
        input_list = [float(i) for i in input_list]
        # make prediction using sklearn model
        pred_str = make_prediction(model, input_list)
        # return from main function should be dict/json.
        # it should have headers/body
        res_temp['body'] = {'result': pred_str}
    except Exception as e:
        print(e)
        res_temp['body'] = {'result': 'Please fill all fields to get the results',
                            'exception': str(e)}
    return res_temp


def make_prediction(model, input_list):
    input_arr = np.array(input_list).reshape(1,-1)
    pred = model.predict(input_arr)
    # print(pred)
    if pred[0] > 0:
        return 'High'
    return 'Low'


if __name__ == "__main__":
    a = [30,  0,  0,  0,  0,  0,  0,  0]
    ur = make_prediction(model, a)
    # print(ur)
    assert ur == 'Low', 'something is wrong'