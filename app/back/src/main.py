from app.back.src.init import Init


def main(test_ctrl=False, test_pico_connection=False):
    return Init()(test_ctrl=test_ctrl, test_pico_connection=test_pico_connection)
