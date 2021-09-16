from app.back.src.init import Init


def main():
    return Init()()


if __name__ == '__main__':
    ctrl = main()

    print(ctrl.get_pkm_by_id(1))
