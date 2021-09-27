from app.back.src.init import Init

if __name__ == '__main__':

    ctrl = Init()() 

    [print(pkm) for pkm in ctrl.get_all_pkms()]
    print(ctrl.get_pkm_by_id(2))
    print(ctrl.get_pkm_by_name("mew"))