import progagation_model

d = 1.0
f = 900.0
hb = 40.0
hm = 1.5
scenario = 4

path_loss = progagation_model.okumura_model_path_loss(d, f, hb, hm, scenario)

print ("path loss is:", path_loss)

