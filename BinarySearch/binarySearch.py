import math

list_numbers = [
  9,
  12,
  15,
  18,
  19,
  20,
  22,
  25,
  26,
  26,
  33,
  37,
  38,
  41,
  47,
  47,
  50,
  55,
  57,
  60,
  68,
  80,
  87,
  90,
  98,
  100,
  103,
  108,
  109,
  109,
  116,
  120,
  120,
  124,
  127,
  128,
  131,
  135,
  135,
  139,
  143,
  145,
  151,
  155,
  156,
  158,
  163,
  164,
  165,
  169,
  169,
  173,
  174,
  176,
  177,
  178,
  181,
  182,
  182,
  183,
  184,
  189,
  192,
  195,
  200,
  201,
  203,
  204,
  207,
  213,
  217,
  222,
  222,
  222,
  227,
  228,
  233,
  235,
  237,
  239,
  239,
  243,
  248,
  251,
  252,
  257,
  260,
  260,
  263,
  268,
  270,
  271,
  271,
  276,
  281,
  284,
  285,
  295,
  297,
  298,
]

def binarySearch(sel_list, target):
    step = 0
    loc_min = 0
    loc_max = len(sel_list)-1

    while(loc_min <= loc_max):
        loc_now = math.floor((loc_min + loc_max) / 2)
        print(loc_now)
        loc_val = sel_list[loc_now]
        step += 1
        if loc_val == target:
            print(f"Step = {step}時，找到參數在位置{loc_now}")
            return loc_now
        elif loc_val > target:
            loc_max = loc_now - 1  # 注意：此處必須-1
            print(f"loc_max = {loc_max}")
        elif loc_val < target:
            loc_min = loc_now + 1  # 注意：此處必須+1
            print(f"loc_min = {loc_min}")
    print("目標參數並不在此陣列中")
        



binarySearch(list_numbers, 300)