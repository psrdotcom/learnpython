def rle_encode(str_val):
    tuple_list = []
    char_counter = 0
    len_str = len(str_val)-1

    for i in range(0, len_str):
        if str_val[i] == str_val[i+1]:
            char_counter = char_counter + 1
            if i == len_str-1:
                char_counter = char_counter + 1
                tuple_list.append((str_val[i], char_counter))
        else:
            char_counter = char_counter + 1
            tuple_list.append((str_val[i],char_counter))
            if i == len_str-1:
                tuple_list.append((str_val[i+1], 1))
            char_counter = 0
    return tuple_list

def rle_decode(enc_list):
    #print(enc_list)
    dec_str = ''

    for tup in enc_list:
        tmp_str = tup[0]*tup[1]
        dec_str += tmp_str

    return dec_str

input_str = 'Bookkeeping'
enc_list = rle_encode(input_str)
print(enc_list)
dec_str = rle_decode(enc_list)
print(dec_str)
