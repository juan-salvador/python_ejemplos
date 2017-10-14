def mi_funcion(param1, param2="def", *tupl, **dic):
    """

    :param param1:
    :param param2:
    :param tupl:
    :param dic:
    :return:
    """
    print(param1)
    print(param2)
    for arg in tupl:
        print(arg)
    for kw in dic.keys():
        print(kw, ":", dic[kw])


mi_funcion(param1="pr1", tpl=("esto", "es", "parte", "de", "la", "tupla"),
           dic="palabra", paabra="significado")
