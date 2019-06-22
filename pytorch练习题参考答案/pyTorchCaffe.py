#-*-coding:utf-8-*-
import re
import torch
import torch.nn
import torch.nn.functional as F

class Solver(solver_name):
    def __init__(self):
        self.solver_name = solver_name
        self.HashMap = {}
    #读取sovler.prototxt
    def read_solver(self):
        fid = open(self.solver_name)
        lines = fid.readlines()
        fid.close()
        for line in lines:
            #去掉#及其后面的内容
            if re.match('#.*?',line) is None:
                pass
            else:
                line = line.strip('\r\n')
                line = line.replace(' ', '')
                name, value = line.split(':')
                self.HashMap[name] = value
class Model(trainval_name):
    #读取train_val.prototxt
    def __init__(self):
        self.model_name = trainval_name
    def get_key_value(self, layer_str,key_name):
        key_value = re.search(key_name + ': ".*?"', layer).group(0).split('"')[1]
        return key_value
    def read_trainval(self):
        fid = open(trainval_name)
        proto_str = fid.read()
        fid.close()
        layer_names = []
        layers = proto_str.split('layer')[1:]
        for layer in layers:
            layer_name = get_key_value(proto_str, 'name')
            type_name = get_key_value(proto_str,'type')
            if layer_name == 'Convolution':
                num_output = get_key_value(proto_str, 'num_output')
                kernel_size = get_key_value(proto_str, 'kernel_size')
    #train
if __name__== '__main__':
    solver = Solver('mnist.sovler')
    lr_policy = solver.HashMap['lr_policy']
    base_lr = solver.HashMap['base_lr']
    display = solver.HashMap['display']
    max_iter =solver.HashMap['max_iter']
    snapshot = solver.HashMap['snapshot']
    solver_mode = sovler.HashMap['solver_mode']
    test_iter = solver.HashMap['test_iter']
    test_interval = sovler.HashMap['test_interval']
    optimizer_name = solver.HashMap['type']
    optimizer = ''
    if optimizer_name =='Adam':
        optimizer = torch.optim.Adam(model.params(), lr = base_lr)
    for t in range(0, max_iter):
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        if t % snapshot == 0:
            torch.save(model.state_dict(), str(t) + 'params.caffemodel')
    print('done!')
