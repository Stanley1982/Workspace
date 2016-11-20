import progagation_model

d = 1.0
f = 900.0
hb = 40.0
hm = 1.5
scenario = [1, 2, 3, 4]

for i in range(0, 4):
    path_loss = progagation_model.okumura_model_path_loss(d, f, hb, hm, scenario[i])
    print (scenario[i], "path loss is:",  path_loss)

path_loss = progagation_model.free_space_path_loss(d, f)
print ("fee space", "path loss is:", path_loss)

