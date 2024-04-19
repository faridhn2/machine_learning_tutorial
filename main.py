def ma3(input_list):
    # return ma3_list
    ma3_list = [0,0]
    for i in range (len(input_list)):
        if i > 1:
            ma3_num = (input_list[i-2]+input_list[i-1]+input_list[i])/3
            number_round = round(ma3_num,1)
            ma3_list.append(number_round)
    return ma3_list            