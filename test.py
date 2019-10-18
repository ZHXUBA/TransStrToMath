# -*- coding: utf-8 -*- 
# Time : 2019/7/4 13:13 
# Author : PGZXB 
# Site : 中国
# File : .py 
# 本库的作用：将外界传入的 {多项式 f({})} 由字符串转化为可计算
# 本库的输入符号的系统：加：+   减：- 乘：* 除：/   乘方：^
# 其他符号暂不支持，且不支持（）的使用，优先级为：最后加减其他由左到右


class TransStrToMath:
    import math

    def __init__(self, fx: str):
        self.x_key_value = []
        self.ffx = fx
        self.fx_sym = []
        self.fx_other_sym = []
        self.fxlist = []
        self.mathfx = []
        self.error = 0
    def trans_str_to_list(self):
        # substrct_num = add_num = 0

        for fx_value in self.fx:
            if fx_value == "+":
                # add_num += 1
                self.fx_sym.append('+')
            elif fx_value == "-":
                # substrct_num += 1
                self.fx_sym.append('-')
            # str( input('输入y='))
        self.fx_key_value = '_'.join('_'.join(self.fx.split('+')).split('-')).split('_')
        self.fx_other_sym = [p*0 for p in range(len(self.fx_key_value))]
        # print(self.fx_key_value)
        for j in range(0, len(self.fx_key_value)):
            syms = ['*', '/', '^']
            for sym in syms:
                if sym in self.fx_key_value[j]:
                    number = self.fx_key_value[j].index(sym)/2-1/2
                    self.fx_key_value[j] = '_{0}_'.format(sym).join(self.fx_key_value[j].split(sym))

        for k in range(len(self.fx_key_value)):
            self.fx_key_value[k] = self.fx_key_value[k].split('_')

        # print(self.fx_key_value)
        for j in range(0, len(self.fx_key_value)):
            self.fx_other_sym[j] = [q * 0 for q in range(int(len(self.fx_key_value[j]) / 2 - 1 / 2))]
            syms = ['*', '/', '^']
            for sym in syms:
                if sym in self.fx_key_value[j]:
                    number = self.fx_key_value[j].index(sym) / 2 - 1 / 2
                    self.fx_other_sym[j][int(number)] = sym
            for sym in syms:
                if sym in self.fx_key_value[j]:
                    self.fx_key_value[j].remove(sym)
        # self.fx_other_sym.remove(1)

    def trans_finalsym(self):
        sym_num = len(self.fx_sym)
        self.mathfx = float(self.fxlist[0])
        for i in range(0, sym_num):
            if self.fx_sym[i] == '+':
                self.mathfx = self.mathfx+float(self.fxlist[i+1])
            elif self.fx_sym[i] == '-':
                self.mathfx = self.mathfx-float(self.fxlist[i+1])

    def trans_othersym(self):
        # num = 0
        self.fxlist = list(range(len(self.fx_key_value)))
        for k in range(len(self.fx_key_value)):
            # num = num+len(self.fx_key_value[k])
            self.fxlist[k] = self.fx_key_value[k][0]
        for j in range(len(self.fx_key_value)):
            for i in range(len(self.fx_key_value[j])-1):

                    # 定义两元运算：乘、除、乘方
                    if self.fx_other_sym[j][i] == '*':
                        self.fxlist[j] = float(self.fxlist[j])*float(self.fx_key_value[j][i+1])
                    elif self.fx_other_sym[j][i] == '^':
                        self.fxlist[j] = float(self.fxlist[j])**float(self.fx_key_value[j][i+1])
                    elif self.fx_other_sym[j][i] == '/':
                        self.fxlist[j] = float(self.fxlist[j])/float(self.fx_key_value[j][i+1])
                    # 自定义运算模块： elif self.fx_other_sym[i+j] == 'sym':
                    #   self.fxlist[j] = float(self.fxlist[j]) function of the sym float(self.fx_key_value[j][i+1])
                    # 定义一元运算 ：三角函数（sin（）、cos（）、tan（）、开平方（sqr（））、对数（lg（），ln（）（其他底数对数用换底公式表达））
                    else:
                        self.fxlist = list(range(len(self.fx_key_value)))
                        print('您输入的表达式中有未定义运算，您可以自己定义！')

    def trans_to_math(self):
        try:
            self.trans_str_to_list()
            self.trans_othersym()
            self.trans_finalsym()
            return self.mathfx
        except BaseException :
            return ''

    def devoloper_model(self):
        print("开发者模式:")
        print("\tfx_key_value : ", self.fx_key_value)
        print("\tfx_sym : ", self.fx_sym)
        print("\tfx_other_sym : ", self.fx_other_sym)
        print("\tfxlist : ", self.fxlist)


if __name__ == '__main__':
    import numpy as np
    var = input('ddd:')
    x = np.arange(0, 1, 0.1)
    y = []
    for inx in x:
        # trans1 = trans_str_to_matn.TransStrToMath(input().format(X=inx))
        y.append(TransStrToMath(var.format(inx)).trans_to_math())
    # self.canvas1.create_line(self.x_fx)
    print(x, type(x))
    print(y)
