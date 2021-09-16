from app.back.src.main import main

test_pico_connection = True

if test_pico_connection:
    blinker = main(test_pico_connection=True)
    blinker.blink()
else:
    ctrl = main()
    print(ctrl.get_pkm_by_id(1))
